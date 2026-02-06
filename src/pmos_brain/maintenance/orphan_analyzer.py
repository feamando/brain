"""
Orphan Analyzer - Analyzes and tracks orphan entities.

Provides:
- Orphan detection and classification
- Orphan reason tracking
- Cleanup recommendations
"""

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


# Entity types that are legitimately standalone (don't need relationships)
STANDALONE_TYPES = [
    "glossary",      # Reference documents
    "template",      # Templates
    "archive",       # Archived items
]

# Entity types that definitely should have relationships
CONNECTED_TYPES = [
    "person",
    "team",
    "squad",
    "project",
    "system",
    "experiment",
    "brand",
]


@dataclass
class OrphanAnalysis:
    """Analysis of orphan entities."""
    total_entities: int
    total_orphans: int
    orphans_by_type: Dict[str, int] = field(default_factory=dict)
    orphans_by_reason: Dict[str, int] = field(default_factory=dict)
    orphan_details: List[Dict[str, Any]] = field(default_factory=list)


class OrphanAnalyzer:
    """
    Analyzes and tracks orphan entities.

    Updates $orphan_reason field to distinguish:
    - pending_enrichment: Not yet processed
    - no_external_data: Enrichers found nothing
    - standalone: Legitimately independent
    - enrichment_failed: Processing failed

    Example:
        analyzer = OrphanAnalyzer(brain_path)
        analysis = analyzer.analyze()
        print(f"Total orphans: {analysis.total_orphans}")
    """

    def __init__(self, brain_path: Union[str, Path]):
        """
        Initialize the analyzer.

        Args:
            brain_path: Path to brain directory
        """
        self.brain_path = Path(brain_path)

    def analyze(
        self,
        entity_type: Optional[str] = None,
        limit: int = 1000,
    ) -> OrphanAnalysis:
        """
        Analyze all orphan entities.

        Args:
            entity_type: Filter by entity type
            limit: Maximum orphans to analyze

        Returns:
            OrphanAnalysis with detailed breakdown
        """
        total_entities = 0
        total_orphans = 0
        orphans_by_type: Dict[str, int] = {}
        orphans_by_reason: Dict[str, int] = {}
        orphan_details: List[Dict[str, Any]] = []

        for entity_path in self._get_entity_files():
            try:
                content = entity_path.read_text(encoding="utf-8")
                frontmatter, _ = self._parse_content(content)

                if not frontmatter:
                    continue

                total_entities += 1
                entity_id = frontmatter.get("$id", "")
                etype = frontmatter.get("$type", "unknown")
                relationships = frontmatter.get("$relationships", [])
                orphan_reason = frontmatter.get("$orphan_reason")

                # Apply type filter
                if entity_type and etype != entity_type:
                    continue

                # Check if orphan (no relationships)
                if not relationships:
                    total_orphans += 1
                    orphans_by_type[etype] = orphans_by_type.get(etype, 0) + 1

                    # Track by reason
                    reason = orphan_reason or "untracked"
                    orphans_by_reason[reason] = orphans_by_reason.get(reason, 0) + 1

                    if len(orphan_details) < limit:
                        orphan_details.append({
                            "id": entity_id,
                            "type": etype,
                            "name": frontmatter.get("name", ""),
                            "reason": orphan_reason,
                            "confidence": frontmatter.get("$confidence", 0),
                            "source": frontmatter.get("$source", "unknown"),
                        })

            except Exception:
                continue

        return OrphanAnalysis(
            total_entities=total_entities,
            total_orphans=total_orphans,
            orphans_by_type=orphans_by_type,
            orphans_by_reason=orphans_by_reason,
            orphan_details=orphan_details,
        )

    def mark_pending_enrichment(
        self,
        dry_run: bool = False,
        limit: int = 1000,
    ) -> int:
        """
        Mark orphans without a reason as pending_enrichment.

        Args:
            dry_run: If True, don't write changes
            limit: Maximum entities to update

        Returns:
            Number of entities updated
        """
        updated = 0

        for entity_path in self._get_entity_files():
            try:
                content = entity_path.read_text(encoding="utf-8")
                frontmatter, body = self._parse_content(content)

                if not frontmatter:
                    continue

                relationships = frontmatter.get("$relationships", [])
                orphan_reason = frontmatter.get("$orphan_reason")

                # Only update orphans without a reason
                if not relationships and not orphan_reason:
                    frontmatter["$orphan_reason"] = "pending_enrichment"

                    if not dry_run:
                        frontmatter["$updated"] = datetime.now().isoformat()
                        new_content = self._format_content(frontmatter, body)
                        entity_path.write_text(new_content, encoding="utf-8")

                    updated += 1

                    if updated >= limit:
                        break

            except Exception:
                continue

        return updated

    def mark_standalone(
        self,
        entity_types: Optional[List[str]] = None,
        dry_run: bool = False,
        limit: int = 1000,
    ) -> int:
        """
        Mark certain entity types as standalone.

        Args:
            entity_types: Types to mark as standalone (default: STANDALONE_TYPES)
            dry_run: If True, don't write changes
            limit: Maximum entities to update

        Returns:
            Number of entities updated
        """
        types_to_mark = entity_types or STANDALONE_TYPES
        updated = 0

        for entity_path in self._get_entity_files():
            try:
                content = entity_path.read_text(encoding="utf-8")
                frontmatter, body = self._parse_content(content)

                if not frontmatter:
                    continue

                etype = frontmatter.get("$type", "unknown")
                relationships = frontmatter.get("$relationships", [])

                # Mark orphan entities of specified types as standalone
                if etype in types_to_mark and not relationships:
                    frontmatter["$orphan_reason"] = "standalone"

                    if not dry_run:
                        frontmatter["$updated"] = datetime.now().isoformat()
                        new_content = self._format_content(frontmatter, body)
                        entity_path.write_text(new_content, encoding="utf-8")

                    updated += 1

                    if updated >= limit:
                        break

            except Exception:
                continue

        return updated

    def mark_no_external_data(
        self,
        entity_ids: List[str],
        dry_run: bool = False,
    ) -> int:
        """
        Mark specific entities as no_external_data.

        Called after enrichment attempts find nothing.

        Args:
            entity_ids: List of entity IDs to mark
            dry_run: If True, don't write changes

        Returns:
            Number of entities updated
        """
        updated = 0
        ids_set = set(entity_ids)

        for entity_path in self._get_entity_files():
            try:
                content = entity_path.read_text(encoding="utf-8")
                frontmatter, body = self._parse_content(content)

                if not frontmatter:
                    continue

                entity_id = frontmatter.get("$id", "")
                relationships = frontmatter.get("$relationships", [])

                if entity_id in ids_set and not relationships:
                    frontmatter["$orphan_reason"] = "no_external_data"

                    if not dry_run:
                        frontmatter["$updated"] = datetime.now().isoformat()
                        new_content = self._format_content(frontmatter, body)
                        entity_path.write_text(new_content, encoding="utf-8")

                    updated += 1

            except Exception:
                continue

        return updated

    def clear_reason_for_connected(
        self,
        dry_run: bool = False,
    ) -> int:
        """
        Clear $orphan_reason for entities that now have relationships.

        Args:
            dry_run: If True, don't write changes

        Returns:
            Number of entities updated
        """
        updated = 0

        for entity_path in self._get_entity_files():
            try:
                content = entity_path.read_text(encoding="utf-8")
                frontmatter, body = self._parse_content(content)

                if not frontmatter:
                    continue

                relationships = frontmatter.get("$relationships", [])
                orphan_reason = frontmatter.get("$orphan_reason")

                # Clear reason if entity now has relationships
                if relationships and orphan_reason:
                    del frontmatter["$orphan_reason"]

                    if not dry_run:
                        frontmatter["$updated"] = datetime.now().isoformat()
                        new_content = self._format_content(frontmatter, body)
                        entity_path.write_text(new_content, encoding="utf-8")

                    updated += 1

            except Exception:
                continue

        return updated

    def get_orphan_rate(self) -> float:
        """
        Get the orphan rate as a percentage.

        Returns:
            Percentage of entities that are orphans
        """
        analysis = self.analyze()
        if analysis.total_entities == 0:
            return 0.0
        return (analysis.total_orphans / analysis.total_entities) * 100

    def _get_entity_files(self) -> List[Path]:
        """Get all entity files in brain."""
        files = list(self.brain_path.rglob("*.md"))
        return [
            f for f in files
            if f.name.lower() not in ("readme.md", "index.md", "_index.md")
            and ".snapshots" not in str(f)
            and ".schema" not in str(f)
        ]

    def _parse_content(self, content: str) -> Tuple[Dict[str, Any], str]:
        """Parse YAML frontmatter from content."""
        if not HAS_YAML:
            return {}, content

        if not content.startswith("---"):
            return {}, content

        parts = content.split("---", 2)
        if len(parts) < 3:
            return {}, content

        try:
            frontmatter = yaml.safe_load(parts[1]) or {}
            return frontmatter, parts[2]
        except Exception:
            return {}, content

    def _format_content(self, frontmatter: Dict[str, Any], body: str) -> str:
        """Format frontmatter and body back to markdown."""
        if not HAS_YAML:
            return body

        yaml_str = yaml.dump(
            frontmatter,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
        )
        return f"---\n{yaml_str}---{body}"
