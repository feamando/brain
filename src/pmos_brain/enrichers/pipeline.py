"""
Enrichment Pipeline - Orchestrates entity enrichment from data sources.

Features:
- Parallel enricher execution
- Batch processing
- Rate limiting
- Checkpoint progress for resumability
"""

import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Union


@dataclass
class EnrichmentResult:
    """Result of enriching an entity."""
    entity_id: str
    source: str
    success: bool
    fields_updated: int = 0
    error: Optional[str] = None


@dataclass
class PipelineProgress:
    """Tracks pipeline progress for resumability."""
    started_at: str
    last_checkpoint: str
    total_entities: int = 0
    processed_entities: int = 0
    successful: int = 0
    failed: int = 0
    sources_completed: List[str] = field(default_factory=list)
    current_source: Optional[str] = None
    last_entity_id: Optional[str] = None


class EnrichmentPipeline:
    """
    Orchestrates entity enrichment from multiple data sources.

    Supports parallel execution, rate limiting, and checkpointing.

    Example:
        pipeline = EnrichmentPipeline(brain_path)
        summary = pipeline.run(sources=["gdocs", "slack"])
        print(f"Processed: {summary['processed']}")
    """

    SOURCES = ["gdocs", "slack", "jira", "github", "context"]

    def __init__(
        self,
        brain_path: Union[str, Path],
        max_workers: int = 4,
        batch_size: int = 10,
        rate_limit: int = 60,  # requests per minute
        checkpoint_file: Optional[Path] = None,
    ):
        """
        Initialize the enrichment pipeline.

        Args:
            brain_path: Path to brain directory
            max_workers: Number of parallel workers
            batch_size: Batch size for processing
            rate_limit: Max requests per minute
            checkpoint_file: File to store progress checkpoints
        """
        self.brain_path = Path(brain_path)
        self.max_workers = max_workers
        self.batch_size = batch_size
        self.rate_limit = rate_limit
        self.checkpoint_file = checkpoint_file or self.brain_path / ".enrichment_checkpoint.json"

        self.progress: Optional[PipelineProgress] = None
        self.results: List[EnrichmentResult] = []
        self._enrichers: Dict[str, Any] = {}

        # Rate limiting
        self._request_times: List[float] = []

    def register_enricher(self, source: str, enricher: Any) -> None:
        """
        Register a custom enricher for a source.

        Args:
            source: Source name (e.g., "gdocs", "slack")
            enricher: Enricher instance with enrich() method
        """
        self._enrichers[source] = enricher

    def run(
        self,
        sources: Optional[List[str]] = None,
        resume: bool = True,
        dry_run: bool = False,
    ) -> Dict[str, Any]:
        """
        Run the enrichment pipeline.

        Args:
            sources: List of sources to process (default: all)
            resume: Resume from checkpoint if available
            dry_run: Preview without making changes

        Returns:
            Summary of enrichment results
        """
        sources = sources or self.SOURCES

        # Load or create progress
        if resume and self.checkpoint_file.exists():
            self.progress = self._load_checkpoint()
        else:
            self.progress = PipelineProgress(
                started_at=datetime.utcnow().isoformat(),
                last_checkpoint=datetime.utcnow().isoformat(),
            )

        # Count total entities
        entity_files = list(self.brain_path.rglob("*.md"))
        entity_files = [f for f in entity_files if f.name.lower() not in ("readme.md", "index.md")]
        self.progress.total_entities = len(entity_files)

        # Process each source
        for source in sources:
            if source in self.progress.sources_completed:
                continue

            self.progress.current_source = source

            enricher = self._get_enricher(source)
            if not enricher:
                continue

            # Get data for this source
            source_data = self._load_source_data(source)
            if not source_data:
                self.progress.sources_completed.append(source)
                continue

            # Process in batches
            results = self._process_source(source, source_data, enricher, dry_run)
            self.results.extend(results)

            self.progress.sources_completed.append(source)
            self._save_checkpoint()

        return self._get_summary()

    def _get_enricher(self, source: str) -> Any:
        """Get the enricher for a source."""
        # Check registered enrichers first
        if source in self._enrichers:
            return self._enrichers[source]

        # Try to import built-in enrichers
        try:
            if source == "gdocs":
                from pmos_brain.enrichers.gdocs_enricher import GDocsEnricher
                return GDocsEnricher(self.brain_path)
            elif source == "slack":
                from pmos_brain.enrichers.slack_enricher import SlackEnricher
                return SlackEnricher(self.brain_path)
            elif source == "jira":
                from pmos_brain.enrichers.jira_enricher import JiraEnricher
                return JiraEnricher(self.brain_path)
            elif source == "github":
                from pmos_brain.enrichers.github_enricher import GitHubEnricher
                return GitHubEnricher(self.brain_path)
            elif source == "context":
                from pmos_brain.enrichers.context_enricher import ContextEnricher
                return ContextEnricher(self.brain_path)
        except ImportError:
            pass

        return None

    def _load_source_data(self, source: str) -> List[Dict[str, Any]]:
        """Load raw data for a source."""
        data_dir = self.brain_path / "Inbox" / source.capitalize()

        if not data_dir.exists():
            # Try alternative paths
            alt_paths = [
                self.brain_path / "Inbox" / source.upper(),
                self.brain_path / "inbox" / source,
            ]
            for alt in alt_paths:
                if alt.exists():
                    data_dir = alt
                    break
            else:
                return []

        data = []
        for file in data_dir.glob("*.json"):
            try:
                with open(file, "r") as f:
                    content = json.load(f)
                    if isinstance(content, list):
                        data.extend(content)
                    else:
                        data.append(content)
            except Exception:
                continue

        return data

    def _process_source(
        self,
        source: str,
        data: List[Dict[str, Any]],
        enricher: Any,
        dry_run: bool,
    ) -> List[EnrichmentResult]:
        """Process all data from a source."""
        results = []

        # Process in batches
        for i in range(0, len(data), self.batch_size):
            batch = data[i:i + self.batch_size]

            # Rate limiting
            self._wait_for_rate_limit()

            if self.max_workers > 1:
                # Parallel processing
                with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                    futures = {
                        executor.submit(
                            self._enrich_item, enricher, item, dry_run
                        ): item
                        for item in batch
                    }

                    for future in as_completed(futures):
                        try:
                            result = future.result()
                            results.append(result)
                            if self.progress:
                                self.progress.processed_entities += 1
                                if result.success:
                                    self.progress.successful += 1
                                else:
                                    self.progress.failed += 1
                        except Exception:
                            if self.progress:
                                self.progress.failed += 1
            else:
                # Sequential processing
                for item in batch:
                    result = self._enrich_item(enricher, item, dry_run)
                    results.append(result)
                    if self.progress:
                        self.progress.processed_entities += 1

            # Checkpoint after each batch
            self._save_checkpoint()

        return results

    def _enrich_item(
        self,
        enricher: Any,
        item: Dict[str, Any],
        dry_run: bool,
    ) -> EnrichmentResult:
        """Enrich a single item."""
        try:
            entity_id = item.get("entity_id") or item.get("id") or "unknown"
            fields_updated = enricher.enrich(item, dry_run=dry_run)

            return EnrichmentResult(
                entity_id=entity_id,
                source=getattr(enricher, "source_name", "unknown"),
                success=True,
                fields_updated=fields_updated if isinstance(fields_updated, int) else 0,
            )
        except Exception as e:
            return EnrichmentResult(
                entity_id=item.get("entity_id", "unknown"),
                source=getattr(enricher, "source_name", "unknown"),
                success=False,
                error=str(e),
            )

    def _wait_for_rate_limit(self) -> None:
        """Wait if necessary to respect rate limit."""
        now = time.time()

        # Remove old timestamps
        self._request_times = [t for t in self._request_times if now - t < 60]

        if len(self._request_times) >= self.rate_limit:
            # Wait until oldest request is more than 60 seconds old
            wait_time = 60 - (now - self._request_times[0])
            if wait_time > 0:
                time.sleep(wait_time)

        self._request_times.append(time.time())

    def _load_checkpoint(self) -> PipelineProgress:
        """Load progress from checkpoint file."""
        try:
            with open(self.checkpoint_file, "r") as f:
                data = json.load(f)
                return PipelineProgress(**data)
        except Exception:
            return PipelineProgress(
                started_at=datetime.utcnow().isoformat(),
                last_checkpoint=datetime.utcnow().isoformat(),
            )

    def _save_checkpoint(self) -> None:
        """Save progress to checkpoint file."""
        if self.progress:
            self.progress.last_checkpoint = datetime.utcnow().isoformat()
            try:
                with open(self.checkpoint_file, "w") as f:
                    json.dump(self.progress.__dict__, f, indent=2)
            except Exception:
                pass

    def _get_summary(self) -> Dict[str, Any]:
        """Get pipeline execution summary."""
        return {
            "total_entities": self.progress.total_entities if self.progress else 0,
            "processed": self.progress.processed_entities if self.progress else 0,
            "successful": self.progress.successful if self.progress else 0,
            "failed": self.progress.failed if self.progress else 0,
            "sources_completed": self.progress.sources_completed if self.progress else [],
            "results": [r.__dict__ for r in self.results[:100]],  # First 100 results
        }
