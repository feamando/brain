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
