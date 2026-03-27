#!/usr/bin/env python3
"""
Brain Enrichment Orchestrator

Runs all brain quality tools in sequence to improve graph density,
identify gaps, and maintain relationship health.

Usage:
    python -m pmos_brain.enrichers.orchestrator                    # Full enrichment
    python -m pmos_brain.enrichers.orchestrator --quick            # Quick mode (soft edges only)
    python -m pmos_brain.enrichers.orchestrator --report           # Report only (no changes)
    python -m pmos_brain.enrichers.orchestrator --boot             # Boot-time mode (minimal, fast)
    python -m pmos_brain.enrichers.orchestrator --orphan           # Orphan cleanup mode

Runs:
    1. Graph health baseline
    2. Soft edge inference (by entity type)
    3. Relationship decay scan
    4. Extraction hints summary
    5. Graph health comparison

Orphan Mode runs:
    Phase 1 (body): Body text relationship extraction
    Phase 2 (external): Pluggable external enrichment
    Phase 3 (inference): Soft edge inference for remaining orphans
    Phase 4 (cleanup): Mark remaining orphans with appropriate reason
"""

import argparse
import hashlib
import json
import os
import signal
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Protocol

from pmos_brain.vector.edge_inferrer import EmbeddingEdgeInferrer, EdgeInferenceReport
from pmos_brain.graph.graph_health import GraphHealth, GraphHealthReport
from pmos_brain.maintenance.orphan_analyzer import OrphanAnalyzer
from pmos_brain.core.entity_cache import EntityCache

# Optional imports - may not be available in all installations
try:
    from pmos_brain.relationships.body_extractor import BodyRelationshipExtractor
    HAS_BODY_EXTRACTOR = True
except ImportError:
    HAS_BODY_EXTRACTOR = False

try:
    from pmos_brain.maintenance.extraction_hints import ExtractionHintsGenerator, ExtractionHintsReport
    HAS_EXTRACTION_HINTS = True
except ImportError:
    HAS_EXTRACTION_HINTS = False

try:
    from pmos_brain.relationships.decay import RelationshipDecayMonitor, RelationshipDecayReport
    HAS_RELATIONSHIP_DECAY = True
except ImportError:
    HAS_RELATIONSHIP_DECAY = False

try:
    from pmos_brain.vector.index import BrainVectorIndex, VECTOR_AVAILABLE
except ImportError:
    VECTOR_AVAILABLE = False


class ExternalEnricher(Protocol):
    """Protocol for pluggable external enrichers."""

    def enrich_orphans(
        self,
        entity_types: List[str],
        limit: int,
        dry_run: bool,
    ) -> Dict[str, Any]:
        """
        Enrich orphan entities from an external source.

        Args:
            entity_types: Entity types to enrich
            limit: Maximum entities to process
            dry_run: If True, don't apply changes

        Returns:
            Dict with at least 'enriched' count
        """
        ...


@dataclass
class EnrichmentResult:
    """Results from a full enrichment run."""

    timestamp: str
    mode: str

    # Baseline
    baseline_entities: int = 0
    baseline_relationships: int = 0
    baseline_orphans: int = 0
    baseline_density: float = 0.0

    # Actions taken
    soft_edges_added: int = 0
    soft_edges_by_type: Dict[str, int] = field(default_factory=dict)

    # Post-enrichment
    final_entities: int = 0
    final_relationships: int = 0
    final_orphans: int = 0
    final_density: float = 0.0

    # Insights
    stale_relationships: int = 0
    high_priority_hints: int = 0
    top_missing_fields: List[str] = field(default_factory=list)

    # Improvements
    density_improvement: float = 0.0
    orphans_reduced: int = 0

    # Orphan mode results
    body_relationships_created: int = 0
    external_enriched: int = 0
    orphans_marked_no_data: int = 0
    orphans_marked_standalone: int = 0

    # Performance metrics (v3.3.0)
    cache_entities_loaded: int = 0
    cache_load_time_ms: float = 0.0
    parallel_enabled: bool = False
    parallel_wall_clock_ms: float = 0.0
    parallel_types_processed: int = 0
    # Incremental metrics
    incremental_enabled: bool = False
    entities_changed: int = 0
    entities_skipped: int = 0
    types_scanned: int = 0
    types_skipped: int = 0
    # ANN metrics
    ann_enabled: bool = False
    ann_queries: int = 0
    ann_fallback_to_bruteforce: int = 0


class BrainEnrichmentOrchestrator:
    """
    Orchestrates all Brain enrichment tools.

    Modes:
    - full: Run all tools, apply changes
    - quick: Soft edges only
    - report: Analysis only, no changes
    - boot: Minimal checks for boot-time
    - orphan: Focused orphan cleanup
    """

    # Soft edge thresholds by entity type
    SOFT_EDGE_CONFIG = {
        "brand": {"threshold": 0.85, "limit": 50},
        "system": {"threshold": 0.85, "limit": 100},
        "squad": {"threshold": 0.80, "limit": 50},
        "team": {"threshold": 0.80, "limit": 50},
        "experiment": {"threshold": 0.85, "limit": 50},
        "person": {"threshold": 0.80, "limit": 300},
        "project": {
            "threshold": 0.88,
            "limit": 300,
        },  # Higher threshold for projects (many artifacts)
        "component": {
            "threshold": 0.90,
            "limit": 200,
        },  # High threshold - components have specific names
        "decision": {
            "threshold": 0.90,
            "limit": 200,
        },  # Decision records reference squads/people
    }

    # Boot mode: only these entity types (fast)
    BOOT_ENTITY_TYPES = ["brand", "squad", "team"]

    def __init__(
        self,
        brain_path: Path,
        verbose: bool = False,
        external_enrichers: Optional[List[ExternalEnricher]] = None,
    ):
        """
        Initialize the orchestrator.

        Args:
            brain_path: Path to the brain directory
            verbose: Enable verbose output
            external_enrichers: Optional list of pluggable external enrichers
                for orphan cleanup mode. Each must implement the
                ExternalEnricher protocol.
        """
        self.brain_path = brain_path
        self.verbose = verbose
        self.external_enrichers = external_enrichers or []

        # Initialize tools
        self.graph_health = GraphHealth(brain_path)

        self.decay_monitor = None
        if HAS_RELATIONSHIP_DECAY:
            self.decay_monitor = RelationshipDecayMonitor(brain_path)

        self.hints_generator = None
        if HAS_EXTRACTION_HINTS:
            self.hints_generator = ExtractionHintsGenerator(brain_path)

    def run(
        self,
        mode: str = "full",
        dry_run: bool = False,
    ) -> EnrichmentResult:
        """
        Run Brain enrichment.

        Args:
            mode: full, quick, report, boot, or orphan
            dry_run: Preview changes without applying

        Returns:
            EnrichmentResult with all metrics
        """
        result = EnrichmentResult(
            timestamp=datetime.now().isoformat(),
            mode=mode,
        )

        # Step 1: Baseline
        if self.verbose:
            print("Step 1: Analyzing baseline graph health...")

        baseline = self.graph_health.analyze()
        result.baseline_entities = baseline.total_entities
        result.baseline_relationships = baseline.total_relationships
        result.baseline_orphans = baseline.orphan_entities
        result.baseline_density = baseline.density_score

        # Orphan mode: run specialized cleanup
        if mode == "orphan":
            return self._run_orphan_cleanup(result, dry_run)

        if mode == "report":
            # Report mode: just analyze
            self._run_analysis(result)
            result.final_entities = result.baseline_entities
            result.final_relationships = result.baseline_relationships
            result.final_orphans = result.baseline_orphans
            result.final_density = result.baseline_density
            return result

        # Load entity cache
        cache_start = time.time()
        cache = EntityCache(self.brain_path)
        cache.load()
        result.cache_entities_loaded = len(cache.entities) if hasattr(cache, 'entities') else 0
        result.cache_load_time_ms = (time.time() - cache_start) * 1000

        # Snapshot (for rollback support)
        if not dry_run and mode not in ("report",):
            self._create_snapshot()

        # Step 2: Soft edge inference
        if self.verbose:
            print("Step 2: Running soft edge inference...")

        entity_types = (
            self.BOOT_ENTITY_TYPES
            if mode == "boot"
            else list(self.SOFT_EDGE_CONFIG.keys())
        )

        # Incremental processing
        incremental = os.environ.get("PMOS_ENRICH_INCREMENTAL", "0") == "1"
        result.incremental_enabled = incremental

        if incremental:
            saved_state = self._load_incremental_state()
            current_hashes = self._compute_type_hashes()
            changed_types = self._get_changed_types(current_hashes, saved_state)
            # Filter entity_types to only changed ones
            entity_types = [t for t in entity_types if t in changed_types or t.rstrip("s") in changed_types]
            result.types_skipped = len(self.SOFT_EDGE_CONFIG) - len(entity_types)
            result.types_scanned = len(entity_types)

        # Parallel or sequential scan
        parallel = os.environ.get("PMOS_ENRICH_PARALLEL", "0") == "1"
        result.parallel_enabled = parallel

        if parallel and len(entity_types) > 1:
            self._parallel_scan(entity_types, dry_run, result)
        else:
            for entity_type in entity_types:
                config = self.SOFT_EDGE_CONFIG.get(
                    entity_type, {"threshold": 0.85, "limit": 50}
                )

                if self.verbose:
                    print(f"  - {entity_type} (threshold={config['threshold']})...")

                try:
                    inferrer = EmbeddingEdgeInferrer(
                        self.brain_path,
                        threshold=config["threshold"],
                    )
                    report = inferrer.scan_for_edges(
                        entity_type=entity_type,
                        limit=config["limit"],
                    )

                    if report.edges and not dry_run:
                        applied = inferrer.apply_edges(report.edges)
                        result.soft_edges_added += applied
                        result.soft_edges_by_type[entity_type] = applied
                    elif report.edges:
                        result.soft_edges_by_type[entity_type] = len(report.edges)

                except Exception as e:
                    if self.verbose:
                        print(f"    Warning: {e}")

        # Save incremental state
        if incremental and not dry_run:
            self._save_incremental_state({"type_hashes": current_hashes})

        # Step 3: Analysis (skip in boot mode)
        if mode != "boot":
            self._run_analysis(result)

        # Step 4: Final metrics
        if self.verbose:
            print("Step 4: Measuring final graph health...")

        final = self.graph_health.analyze()
        result.final_entities = final.total_entities
        result.final_relationships = final.total_relationships
        result.final_orphans = final.orphan_entities
        result.final_density = final.density_score

        # Calculate improvements
        result.density_improvement = result.final_density - result.baseline_density
        result.orphans_reduced = result.baseline_orphans - result.final_orphans

        return result

    def _run_analysis(self, result: EnrichmentResult) -> None:
        """Run decay and hints analysis."""
        # Relationship decay
        if self.decay_monitor:
            if self.verbose:
                print("Step 3a: Scanning relationship staleness...")

            decay_report = self.decay_monitor.scan_relationships()
            result.stale_relationships = decay_report.stale_relationships

        # Extraction hints
        if self.hints_generator:
            if self.verbose:
                print("Step 3b: Generating extraction hints...")

            hints_report = self.hints_generator.generate_hints(priority_filter="high")
            result.high_priority_hints = hints_report.high_priority_hints
            result.top_missing_fields = list(hints_report.hints_by_field.keys())[:5]

    def _run_orphan_cleanup(
        self,
        result: EnrichmentResult,
        dry_run: bool,
    ) -> EnrichmentResult:
        """
        Run orphan cleanup mode.

        Phases:
        1. Body text relationship extraction
        2. External enrichment (pluggable enrichers)
        3. Soft edge inference for remaining orphans
        4. Mark remaining orphans with appropriate reason
        """
        # Phase 1: Body text extraction
        if self.verbose:
            print("Phase 1: Body text relationship extraction...")

        if HAS_BODY_EXTRACTOR:
            try:
                body_extractor = BodyRelationshipExtractor(self.brain_path)
                body_report = body_extractor.scan(orphans_only=True, limit=1000)

                if body_report.relationships and not dry_run:
                    applied = body_extractor.apply(body_report.relationships)
                    result.body_relationships_created = applied
                elif body_report.relationships:
                    result.body_relationships_created = len(body_report.relationships)

                if self.verbose:
                    print(
                        f"  Found {len(body_report.relationships)} potential relationships"
                    )
                    print(f"  Applied: {result.body_relationships_created}")
            except Exception as e:
                if self.verbose:
                    print(f"  Warning: Body extraction failed: {e}")
        else:
            if self.verbose:
                print("  Skipped: body relationship extractor not available")

        # Phase 2: External enrichment (pluggable)
        if self.verbose:
            print("Phase 2: External enrichment...")

        total_external_enriched = 0
        for enricher in self.external_enrichers:
            enricher_name = type(enricher).__name__
            try:
                enricher_results = enricher.enrich_orphans(
                    entity_types=["project", "person", "system", "experiment"],
                    limit=100,
                    dry_run=dry_run,
                )
                enriched_count = enricher_results.get("enriched", 0)
                total_external_enriched += enriched_count

                if self.verbose:
                    print(f"  {enricher_name}: enriched {enriched_count} entities")
            except Exception as e:
                if self.verbose:
                    print(f"  {enricher_name} skipped: {e}")

        result.external_enriched = total_external_enriched

        if not self.external_enrichers and self.verbose:
            print("  No external enrichers configured")

        # Phase 3: Soft edge inference for remaining orphans
        if self.verbose:
            print("Phase 3: Soft edge inference for remaining orphans...")

        for entity_type in ["project", "system", "person"]:
            try:
                inferrer = EmbeddingEdgeInferrer(
                    self.brain_path,
                    threshold=0.85,
                )
                report = inferrer.scan_for_edges(
                    entity_type=entity_type,
                    limit=50,
                )

                if report.edges and not dry_run:
                    applied = inferrer.apply_edges(report.edges)
                    result.soft_edges_added += applied
                elif report.edges:
                    result.soft_edges_added += len(report.edges)

            except Exception as e:
                if self.verbose:
                    print(f"    {entity_type}: {e}")

        if self.verbose:
            print(f"  Soft edges added: {result.soft_edges_added}")

        # Phase 4: Mark remaining orphans
        if self.verbose:
            print("Phase 4: Marking remaining orphans...")

        try:
            orphan_analyzer = OrphanAnalyzer(self.brain_path)

            # Mark standalone types
            standalone_count = orphan_analyzer.mark_standalone(dry_run=dry_run)
            result.orphans_marked_standalone = standalone_count

            # Clear reason for now-connected entities
            orphan_analyzer.clear_reason_for_connected(dry_run=dry_run)

            if self.verbose:
                print(f"  Marked {standalone_count} as standalone")
        except Exception as e:
            if self.verbose:
                print(f"  Orphan analysis failed: {e}")

        # Final metrics
        if self.verbose:
            print("Measuring final graph health...")

        final = self.graph_health.analyze()
        result.final_entities = final.total_entities
        result.final_relationships = final.total_relationships
        result.final_orphans = final.orphan_entities
        result.final_density = final.density_score

        result.density_improvement = result.final_density - result.baseline_density
        result.orphans_reduced = result.baseline_orphans - result.final_orphans

        return result

    def _parallel_scan(
        self,
        entity_types: list,
        dry_run: bool,
        result: EnrichmentResult,
    ) -> None:
        """Run soft edge inference in parallel across entity types."""
        start = time.time()
        futures = {}

        with ThreadPoolExecutor(max_workers=min(4, len(entity_types))) as executor:
            for entity_type in sorted(entity_types):
                config = self.SOFT_EDGE_CONFIG.get(
                    entity_type, {"threshold": 0.85, "limit": 50}
                )
                futures[executor.submit(
                    self._scan_single_type, entity_type, config, dry_run
                )] = entity_type

            for future in as_completed(futures):
                entity_type = futures[future]
                try:
                    edges_count = future.result()
                    if edges_count > 0:
                        result.soft_edges_added += edges_count
                        result.soft_edges_by_type[entity_type] = edges_count
                except Exception as e:
                    if self.verbose:
                        print(f"    {entity_type}: {e}")

        result.parallel_wall_clock_ms = (time.time() - start) * 1000
        result.parallel_types_processed = len(entity_types)

    def _scan_single_type(
        self,
        entity_type: str,
        config: dict,
        dry_run: bool,
    ) -> int:
        """Scan a single entity type for soft edges. Thread-safe (read-only scan)."""
        try:
            inferrer = EmbeddingEdgeInferrer(
                self.brain_path,
                threshold=config["threshold"],
            )
            report = inferrer.scan_for_edges(
                entity_type=entity_type,
                limit=config["limit"],
            )
            if report.edges and not dry_run:
                return inferrer.apply_edges(report.edges)
            elif report.edges:
                return len(report.edges)
            return 0
        except Exception:
            return 0

    def _load_incremental_state(self) -> dict:
        """Load incremental enrichment state."""
        state_path = self.brain_path / ".enrichment-state.json"
        if state_path.exists():
            try:
                import json as _json
                content = state_path.read_text()
                if len(content) > 512_000:  # 500KB cap
                    return {}
                return _json.loads(content)
            except Exception:
                return {}
        return {}

    def _save_incremental_state(self, state: dict) -> None:
        """Save incremental enrichment state."""
        import json as _json
        state_path = self.brain_path / ".enrichment-state.json"
        state_path.write_text(_json.dumps(state, indent=2))

    def _compute_type_hashes(self) -> dict:
        """Compute content hashes per entity type."""
        type_hashes = {}
        for entity_path in self.brain_path.rglob("*.md"):
            if entity_path.name.lower() in ("readme.md", "index.md", "_index.md"):
                continue
            if ".snapshots" in str(entity_path):
                continue
            try:
                content = entity_path.read_bytes()
                h = hashlib.sha256(content).hexdigest()[:16]
                # Determine type from parent dir name
                parent = entity_path.parent.name.lower()
                type_key = parent.rstrip("s")  # "Entities" -> "entitie" — use actual type from file
                if type_key not in type_hashes:
                    type_hashes[type_key] = []
                type_hashes[type_key].append(h)
            except Exception:
                continue
        # Combine hashes per type
        return {k: hashlib.sha256("".join(sorted(v)).encode()).hexdigest()[:16]
                for k, v in type_hashes.items()}

    def _get_changed_types(self, current_hashes: dict, saved_state: dict) -> set:
        """Determine which entity types have changed since last run."""
        saved_hashes = saved_state.get("type_hashes", {})
        changed = set()
        for type_key, current_hash in current_hashes.items():
            if saved_hashes.get(type_key) != current_hash:
                changed.add(type_key)
        # Also include types that were removed
        for type_key in saved_hashes:
            if type_key not in current_hashes:
                changed.add(type_key)
        return changed

    def _create_snapshot(self) -> Optional[str]:
        """Create git-based pre-enrichment snapshot."""
        import subprocess
        try:
            # Check if in git repo
            result = subprocess.run(
                ["git", "rev-parse", "--is-inside-work-tree"],
                cwd=self.brain_path,
                capture_output=True, text=True,
            )
            if result.returncode != 0:
                return None

            # Create stash
            result = subprocess.run(
                ["git", "stash", "create"],
                cwd=self.brain_path,
                capture_output=True, text=True,
            )
            stash_ref = result.stdout.strip()
            if stash_ref:
                snapshot_path = self.brain_path / ".enrichment-snapshot"
                snapshot_path.write_text(stash_ref)
                return stash_ref
            return None
        except Exception:
            return None

    def rollback(self) -> bool:
        """Rollback to pre-enrichment snapshot."""
        import subprocess
        snapshot_path = self.brain_path / ".enrichment-snapshot"
        if not snapshot_path.exists():
            raise FileNotFoundError("No enrichment snapshot found")

        stash_ref = snapshot_path.read_text().strip()
        try:
            subprocess.run(
                ["git", "checkout", "."],
                cwd=self.brain_path,
                capture_output=True, check=True,
            )
            subprocess.run(
                ["git", "stash", "apply", stash_ref],
                cwd=self.brain_path,
                capture_output=True, check=True,
            )
            snapshot_path.unlink()
            return True
        except Exception:
            return False


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Run Brain enrichment to improve graph quality"
    )
    parser.add_argument(
        "--mode",
        choices=["full", "quick", "report", "boot", "orphan"],
        default="full",
        help="Enrichment mode",
    )
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Shortcut for --mode quick",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Shortcut for --mode report",
    )
    parser.add_argument(
        "--boot",
        action="store_true",
        help="Shortcut for --mode boot (minimal, fast)",
    )
    parser.add_argument(
        "--orphan",
        action="store_true",
        help="Shortcut for --mode orphan (orphan cleanup)",
    )
    parser.add_argument(
        "--brain-path",
        type=Path,
        help="Path to brain directory",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without applying",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose output",
    )
    parser.add_argument(
        "--embed",
        action="store_true",
        help="Rebuild vector index after enrichment (for semantic search)",
    )
    parser.add_argument(
        "--output",
        choices=["text", "json"],
        default="text",
        help="Output format",
    )

    args = parser.parse_args()

    # Resolve mode shortcuts
    mode = args.mode
    if args.quick:
        mode = "quick"
    elif args.report:
        mode = "report"
    elif args.boot:
        mode = "boot"
    elif args.orphan:
        mode = "orphan"

    # Resolve brain path
    if not args.brain_path:
        args.brain_path = Path.cwd() / "brain"

    # Run enrichment
    orchestrator = BrainEnrichmentOrchestrator(
        args.brain_path,
        verbose=args.verbose or args.output == "text",
    )

    result = orchestrator.run(mode=mode, dry_run=args.dry_run)

    # Rebuild vector index if requested (skip in boot mode - too slow)
    if args.embed and mode != "boot" and not args.dry_run:
        try:
            if VECTOR_AVAILABLE:
                if args.verbose or args.output == "text":
                    print("Step 5: Rebuilding vector index...")
                vi = BrainVectorIndex(args.brain_path)
                vi_stats = vi.build_index()
                if args.verbose or args.output == "text":
                    print(f"  Indexed {vi_stats['entities_indexed']} entities")
            else:
                if args.verbose or args.output == "text":
                    print("Step 5: Skipped vector index (dependencies not installed)")
        except Exception as e:
            if args.verbose or args.output == "text":
                print(f"Step 5: Vector index rebuild failed: {e}")

    # Output
    if args.output == "json":
        output = {
            "timestamp": result.timestamp,
            "mode": result.mode,
            "baseline": {
                "entities": result.baseline_entities,
                "relationships": result.baseline_relationships,
                "orphans": result.baseline_orphans,
                "density": result.baseline_density,
            },
            "actions": {
                "soft_edges_added": result.soft_edges_added,
                "by_type": result.soft_edges_by_type,
            },
            "final": {
                "entities": result.final_entities,
                "relationships": result.final_relationships,
                "orphans": result.final_orphans,
                "density": result.final_density,
            },
            "insights": {
                "stale_relationships": result.stale_relationships,
                "high_priority_hints": result.high_priority_hints,
                "top_missing_fields": result.top_missing_fields,
            },
            "improvements": {
                "density_change": round(result.density_improvement, 4),
                "orphans_reduced": result.orphans_reduced,
            },
        }
        # Add orphan mode details
        if result.mode == "orphan":
            output["orphan_cleanup"] = {
                "body_relationships": result.body_relationships_created,
                "external_enriched": result.external_enriched,
                "marked_standalone": result.orphans_marked_standalone,
            }
        print(json.dumps(output, indent=2))
    else:
        print()
        print("=" * 60)
        print("Brain Enrichment Complete")
        print("=" * 60)
        print(f"Mode: {result.mode}")
        print(f"Timestamp: {result.timestamp}")
        print()

        print("Baseline:")
        print(f"  Entities: {result.baseline_entities}")
        print(f"  Relationships: {result.baseline_relationships}")
        print(f"  Orphans: {result.baseline_orphans}")
        print(f"  Density: {result.baseline_density:.3f}")
        print()

        if result.soft_edges_added > 0 or result.soft_edges_by_type:
            print("Soft Edges Added:")
            print(f"  Total: {result.soft_edges_added}")
            for etype, count in result.soft_edges_by_type.items():
                print(f"  - {etype}: {count}")
            print()

        # Orphan mode details
        if result.mode == "orphan":
            print("Orphan Cleanup:")
            print(f"  Body relationships created: {result.body_relationships_created}")
            print(f"  External enriched: {result.external_enriched}")
            print(f"  Marked standalone: {result.orphans_marked_standalone}")
            print()

        print("Final:")
        print(f"  Entities: {result.final_entities}")
        print(f"  Relationships: {result.final_relationships}")
        print(f"  Orphans: {result.final_orphans}")
        print(f"  Density: {result.final_density:.3f}")
        print()

        if result.stale_relationships > 0 or result.high_priority_hints > 0:
            print("Insights:")
            print(f"  Stale relationships: {result.stale_relationships}")
            print(f"  High-priority hints: {result.high_priority_hints}")
            if result.top_missing_fields:
                print(f"  Top missing: {', '.join(result.top_missing_fields)}")
            print()

        print("Improvements:")
        density_pct = (
            result.density_improvement / max(result.baseline_density, 0.001)
        ) * 100
        print(
            f"  Density: {result.baseline_density:.3f} -> {result.final_density:.3f} ({density_pct:+.1f}%)"
        )
        print(f"  Orphans reduced: {result.orphans_reduced}")
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
