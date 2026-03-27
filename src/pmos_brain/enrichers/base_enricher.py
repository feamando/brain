"""
Base Enricher - Abstract base class for data source enrichers.

Provides common functionality for all enrichers:
- Entity loading and saving
- Frontmatter parsing
- Relationship management
"""

from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


class BaseEnricher(ABC):
    """
    Abstract base class for Brain enrichers.

    Subclasses must implement:
    - source_name: Name of the data source
    - enrich(): Process a single item and update entities

    Example:
        class MyEnricher(BaseEnricher):
            source_name = "my_source"

            def enrich(self, item, dry_run=False):
                # Find matching entity
                entity = self.find_entity(item["name"])
                if entity:
                    self.update_entity_field(entity, "field", item["value"])
                    return 1  # fields updated
                return 0
    """

    source_name: str = "unknown"

    def __init__(self, brain_path: Union[str, Path]):
        """
        Initialize the enricher.

        Args:
            brain_path: Path to the brain directory
        """
        self.brain_path = Path(brain_path)
        self._entity_cache: Dict[str, Path] = {}

    @abstractmethod
    def enrich(self, item: Dict[str, Any], dry_run: bool = False) -> int:
        """
        Enrich entities from a single data item.

        Args:
            item: Data item from the source
            dry_run: If True, don't write changes

        Returns:
            Number of fields updated
        """
        pass

    def find_entity(
        self,
        name: str,
        entity_type: Optional[str] = None,
    ) -> Optional[Path]:
        """
        Find an entity by name.

        Args:
            name: Entity name to search for
            entity_type: Optional type filter

        Returns:
            Path to entity file, or None
        """
        # Normalize name for comparison
        name_lower = name.lower().replace(" ", "_").replace("-", "_")

        for entity_path in self._get_entity_files():
            try:
                content = entity_path.read_text(encoding="utf-8")
                frontmatter, _ = self._parse_content(content)

                # Check name matches
                entity_name = frontmatter.get("name", "")
                entity_name_normalized = entity_name.lower().replace(" ", "_").replace("-", "_")

                if name_lower == entity_name_normalized:
                    if entity_type and frontmatter.get("$type") != entity_type:
                        continue
                    return entity_path

                # Also check $id
                entity_id = frontmatter.get("$id", "")
                if name_lower in entity_id.lower():
                    if entity_type and frontmatter.get("$type") != entity_type:
                        continue
                    return entity_path

            except Exception:
                continue

        return None

    def find_entity_by_id(self, entity_id: str) -> Optional[Path]:
        """
        Find an entity by its $id.

        Args:
            entity_id: Entity $id to search for

        Returns:
            Path to entity file, or None
        """
        # Check cache
        if entity_id in self._entity_cache:
            return self._entity_cache[entity_id]

        for entity_path in self._get_entity_files():
            try:
                content = entity_path.read_text(encoding="utf-8")
                frontmatter, _ = self._parse_content(content)

                eid = frontmatter.get("$id", "")
                if eid:
                    self._entity_cache[eid] = entity_path

                if eid == entity_id:
                    return entity_path

            except Exception:
                continue

        return None

    def update_entity_field(
        self,
        entity_path: Path,
        field: str,
        value: Any,
        dry_run: bool = False,
    ) -> bool:
        """
        Update a single field on an entity.

        Args:
            entity_path: Path to entity file
            field: Field name to update
            value: New value
            dry_run: If True, don't write

        Returns:
            True if field was updated
        """
        try:
            content = entity_path.read_text(encoding="utf-8")
            frontmatter, body = self._parse_content(content)

            if not frontmatter:
                return False

            # Don't overwrite with empty value
            if not value and field in frontmatter:
                return False

            # Check if value changed
            if frontmatter.get(field) == value:
                return False

            frontmatter[field] = value
            frontmatter["$updated"] = datetime.now().isoformat()
            frontmatter["$source"] = self.source_name

            if not dry_run:
                new_content = self._format_content(frontmatter, body)
                entity_path.write_text(new_content, encoding="utf-8")

            return True

        except Exception:
            return False

    def add_relationship(
        self,
        entity_path: Path,
        target_id: str,
        rel_type: str,
        confidence: float = 1.0,
        dry_run: bool = False,
    ) -> bool:
        """
        Add a relationship to an entity.

        Args:
            entity_path: Path to entity file
            target_id: Target entity $id
            rel_type: Relationship type
            confidence: Confidence score
            dry_run: If True, don't write

        Returns:
            True if relationship was added
        """
        try:
            content = entity_path.read_text(encoding="utf-8")
            frontmatter, body = self._parse_content(content)

            if not frontmatter:
                return False

            relationships = frontmatter.get("$relationships", [])

            # Check if relationship already exists
            for rel in relationships:
                if isinstance(rel, dict) and rel.get("target") == target_id:
                    return False  # Already exists

            # Add new relationship
            new_rel = {
                "type": rel_type,
                "target": target_id,
                "confidence": confidence,
                "source": self.source_name,
                "last_verified": datetime.now().isoformat(),
            }
            relationships.append(new_rel)

            frontmatter["$relationships"] = relationships
            frontmatter["$updated"] = datetime.now().isoformat()

            if not dry_run:
                new_content = self._format_content(frontmatter, body)
                entity_path.write_text(new_content, encoding="utf-8")

            return True

        except Exception:
            return False

    def has_existing_event(self, entity_frontmatter: dict, event_type: str, field: str = None) -> bool:
        """Check if an event of this type already exists for this field."""
        events = entity_frontmatter.get("$events", [])
        for event in events:
            if not isinstance(event, dict):
                continue
            if event.get("type") != event_type:
                continue
            if field:
                changes = event.get("changes", [])
                if any(c.get("field") == field for c in changes if isinstance(c, dict)):
                    return True
            else:
                return True
        return False

    def has_existing_event_by_correlation(self, entity_frontmatter: dict, correlation_id: str) -> bool:
        """Check if an event with this correlation ID already exists."""
        events = entity_frontmatter.get("$events", [])
        return any(
            isinstance(e, dict) and e.get("correlation_id") == correlation_id
            for e in events
        )

    def deduplicate_events(self, entity_frontmatter: dict) -> int:
        """Remove duplicate events based on (type, field, timestamp). Returns count removed."""
        events = entity_frontmatter.get("$events", [])
        if not events:
            return 0

        seen = set()
        deduped = []
        removed = 0

        for event in events:
            if not isinstance(event, dict):
                deduped.append(event)
                continue

            key_parts = [event.get("type", ""), event.get("timestamp", "")]
            changes = event.get("changes", [])
            if changes and isinstance(changes[0], dict):
                key_parts.append(changes[0].get("field", ""))
            key = tuple(key_parts)

            if key in seen:
                removed += 1
            else:
                seen.add(key)
                deduped.append(event)

        if removed > 0:
            entity_frontmatter["$events"] = deduped
        return removed

    def calculate_confidence(self, entity_frontmatter: dict) -> float:
        """Calculate entity confidence: completeness(40%) + source_reliability(40%) + freshness(20%)."""
        # Completeness: ratio of non-empty fields
        total_fields = 0
        filled_fields = 0
        for key, value in entity_frontmatter.items():
            if key.startswith("$"):
                continue
            total_fields += 1
            if value is not None and value != "" and value != []:
                filled_fields += 1
        completeness = filled_fields / max(total_fields, 1)

        # Source reliability: average confidence of relationships
        relationships = entity_frontmatter.get("$relationships", [])
        if relationships:
            confs = [r.get("confidence", 0.5) for r in relationships if isinstance(r, dict)]
            reliability = sum(confs) / len(confs) if confs else 0.5
        else:
            reliability = 0.5

        # Freshness: based on $updated field
        freshness = 0.5
        updated = entity_frontmatter.get("$updated")
        if updated:
            try:
                from datetime import datetime, timezone
                if isinstance(updated, str):
                    updated_dt = datetime.fromisoformat(updated.replace("Z", "+00:00"))
                    days_old = (datetime.now(timezone.utc) - updated_dt).days
                    freshness = max(0.1, 1.0 - (days_old / 365))
            except Exception:
                pass

        return round(completeness * 0.4 + reliability * 0.4 + freshness * 0.2, 3)

    def extract_mentions(self, text: str, alias_index: dict = None) -> list:
        """Find entity mentions in text using alias index.

        Args:
            text: Text to scan for mentions
            alias_index: Dict mapping alias (lowercase) -> entity_id

        Returns:
            List of entity_id strings found in text
        """
        if not alias_index or not text:
            return []

        import re
        text_lower = text.lower()
        found = []
        seen = set()

        for alias, entity_id in alias_index.items():
            if len(alias) < 3:
                continue
            if entity_id in seen:
                continue
            pattern = r"\b" + re.escape(alias) + r"\b"
            if re.search(pattern, text_lower):
                found.append(entity_id)
                seen.add(entity_id)

        return found

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
