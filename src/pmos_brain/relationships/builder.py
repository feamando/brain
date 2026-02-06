"""
Relationship Builder - Bidirectional relationship management.

Enforces bidirectional relationship creation - when A→B is created,
automatically creates B→A with the inverse relationship type.
"""

from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


# Comprehensive inverse relationship mapping
INVERSE_RELATIONSHIPS = {
    # Organizational
    "reports_to": "manages",
    "manages": "reports_to",
    "member_of": "has_member",
    "has_member": "member_of",
    "leads": "led_by",
    "led_by": "leads",

    # Ownership
    "owns": "owned_by",
    "owned_by": "owns",
    "maintains": "maintained_by",
    "maintained_by": "maintains",
    "managed_by": "manages",

    # Collaboration
    "works_with": "works_with",  # Symmetric
    "collaborates_with": "collaborates_with",  # Symmetric
    "stakeholder_of": "has_stakeholder",
    "has_stakeholder": "stakeholder_of",
    "works_on": "has_contributor",
    "has_contributor": "works_on",

    # Dependencies
    "depends_on": "depended_on_by",
    "depended_on_by": "depends_on",
    "blocks": "blocked_by",
    "blocked_by": "blocks",
    "uses": "used_by",
    "used_by": "uses",

    # Hierarchy
    "parent_of": "child_of",
    "child_of": "parent_of",
    "part_of": "has_part",
    "has_part": "part_of",
    "belongs_to": "contains",
    "contains": "belongs_to",

    # Content relationships
    "mentioned_in": "mentions",
    "mentions": "mentioned_in",
    "related_to": "related_to",  # Symmetric
    "similar_to": "similar_to",  # Symmetric
    "documented_in": "documents",
    "documents": "documented_in",

    # Experiments
    "has_experiment": "part_of",
}


@dataclass
class RelationshipResult:
    """Result of a relationship creation operation."""
    source_id: str
    target_id: str
    forward_type: str
    inverse_type: str
    forward_created: bool
    inverse_created: bool
    forward_existed: bool
    inverse_existed: bool


class RelationshipBuilder:
    """
    Creates bidirectional relationships between Brain entities.

    Ensures that when a relationship A→B is created, the inverse
    relationship B→A is also created automatically.

    Example:
        builder = RelationshipBuilder(brain_path)
        result = builder.create_bidirectional(
            source_id="entity/person/john",
            target_id="entity/team/growth",
            relationship_type="member_of",
        )
    """

    def __init__(self, brain_path: Union[str, Path]):
        """
        Initialize the relationship builder.

        Args:
            brain_path: Path to brain directory
        """
        self.brain_path = Path(brain_path)
        self._entity_cache: Dict[str, Path] = {}

    def create_bidirectional(
        self,
        source_id: str,
        target_id: str,
        relationship_type: str,
        confidence: float = 1.0,
        source: Optional[str] = None,
        since: Optional[date] = None,
        role: Optional[str] = None,
        dry_run: bool = False,
    ) -> RelationshipResult:
        """
        Create a bidirectional relationship between two entities.

        Args:
            source_id: Source entity $id
            target_id: Target entity $id
            relationship_type: Forward relationship type (e.g., "member_of")
            confidence: Confidence score [0,1]
            source: Source of relationship data
            since: When relationship started
            role: Optional role context
            dry_run: If True, don't write changes

        Returns:
            RelationshipResult with creation status
        """
        # Get inverse relationship type
        inverse_type = self.get_inverse_type(relationship_type)

        # Create forward relationship (source → target)
        forward_created, forward_existed = self._add_relationship(
            entity_id=source_id,
            target_id=target_id,
            rel_type=relationship_type,
            confidence=confidence,
            source=source,
            since=since,
            role=role,
            dry_run=dry_run,
        )

        # Create inverse relationship (target → source)
        inverse_created, inverse_existed = self._add_relationship(
            entity_id=target_id,
            target_id=source_id,
            rel_type=inverse_type,
            confidence=confidence,
            source=source,
            since=since,
            role=role,
            dry_run=dry_run,
        )

        return RelationshipResult(
            source_id=source_id,
            target_id=target_id,
            forward_type=relationship_type,
            inverse_type=inverse_type,
            forward_created=forward_created,
            inverse_created=inverse_created,
            forward_existed=forward_existed,
            inverse_existed=inverse_existed,
        )

    def get_inverse_type(self, relationship_type: str) -> str:
        """
        Get the inverse relationship type.

        Args:
            relationship_type: Forward relationship type

        Returns:
            Inverse relationship type
        """
        # Check known inverses
        if relationship_type in INVERSE_RELATIONSHIPS:
            return INVERSE_RELATIONSHIPS[relationship_type]

        # Generate inverse for unknown types
        if relationship_type.startswith("has_"):
            return relationship_type[4:] + "_of"
        if relationship_type.endswith("_of"):
            return "has_" + relationship_type[:-3]
        if relationship_type.endswith("_by"):
            return relationship_type[:-3] + "s"
        if relationship_type.endswith("s") and not relationship_type.endswith("_by"):
            return relationship_type[:-1] + "_by"

        # Default: prefix with "inverse_"
        return f"inverse_{relationship_type}"

    def ensure_inverse_exists(
        self,
        source_id: str,
        relationship: Dict[str, Any],
        dry_run: bool = False,
    ) -> bool:
        """
        Ensure the inverse of an existing relationship exists.

        Args:
            source_id: ID of entity that has the relationship
            relationship: The existing relationship dict
            dry_run: If True, don't write changes

        Returns:
            True if inverse was created or already existed
        """
        target_id = relationship.get("target", "")
        if not target_id:
            return False

        rel_type = relationship.get("type", "related_to")
        inverse_type = self.get_inverse_type(rel_type)

        created, existed = self._add_relationship(
            entity_id=target_id,
            target_id=source_id,
            rel_type=inverse_type,
            confidence=relationship.get("confidence", 1.0),
            source=relationship.get("source"),
            since=self._parse_date(relationship.get("since")),
            role=relationship.get("role"),
            dry_run=dry_run,
        )

        return created or existed

    def fix_all_inverses(
        self,
        dry_run: bool = False,
        limit: int = 1000,
    ) -> Dict[str, int]:
        """
        Scan all entities and create missing inverse relationships.

        Args:
            dry_run: If True, don't write changes
            limit: Maximum inverses to create

        Returns:
            Stats dict with counts
        """
        stats = {
            "entities_scanned": 0,
            "relationships_checked": 0,
            "inverses_created": 0,
            "inverses_existed": 0,
        }

        for entity_path in self._get_entity_files():
            try:
                content = entity_path.read_text(encoding="utf-8")
                frontmatter, body = self._parse_content(content)

                if not frontmatter:
                    continue

                stats["entities_scanned"] += 1
                entity_id = frontmatter.get("$id", "")
                relationships = frontmatter.get("$relationships", [])

                for rel in relationships:
                    if not isinstance(rel, dict):
                        continue

                    stats["relationships_checked"] += 1

                    # Check if inverse exists
                    target_id = rel.get("target", "")
                    if not target_id:
                        continue

                    inverse_exists = self._relationship_exists(target_id, entity_id)
                    if inverse_exists:
                        stats["inverses_existed"] += 1
                    else:
                        if self.ensure_inverse_exists(entity_id, rel, dry_run):
                            stats["inverses_created"] += 1

                    if stats["inverses_created"] >= limit:
                        break

                if stats["inverses_created"] >= limit:
                    break

            except Exception:
                continue

        return stats

    def _add_relationship(
        self,
        entity_id: str,
        target_id: str,
        rel_type: str,
        confidence: float,
        source: Optional[str],
        since: Optional[date],
        role: Optional[str],
        dry_run: bool,
    ) -> Tuple[bool, bool]:
        """Add a relationship to an entity."""
        entity_path = self._find_entity_file(entity_id)
        if not entity_path:
            return False, False

        try:
            content = entity_path.read_text(encoding="utf-8")
            frontmatter, body = self._parse_content(content)

            if not frontmatter:
                return False, False

            relationships = frontmatter.get("$relationships", [])

            # Check if relationship already exists
            for rel in relationships:
                if isinstance(rel, dict) and rel.get("target") == target_id:
                    return False, True  # Already exists

            # Build new relationship
            new_rel = {
                "type": rel_type,
                "target": target_id,
                "confidence": confidence,
                "last_verified": date.today().isoformat(),
            }

            if source:
                new_rel["source"] = source
            if since:
                new_rel["since"] = since.isoformat()
            if role:
                new_rel["role"] = role

            relationships.append(new_rel)
            frontmatter["$relationships"] = relationships

            if not dry_run:
                frontmatter["$updated"] = datetime.now().isoformat()
                new_content = self._format_content(frontmatter, body)
                entity_path.write_text(new_content, encoding="utf-8")

            return True, False

        except Exception:
            return False, False

    def _relationship_exists(self, entity_id: str, target_id: str) -> bool:
        """Check if a relationship to target exists on entity."""
        entity_path = self._find_entity_file(entity_id)
        if not entity_path:
            return False

        try:
            content = entity_path.read_text(encoding="utf-8")
            frontmatter, _ = self._parse_content(content)

            relationships = frontmatter.get("$relationships", [])
            for rel in relationships:
                if isinstance(rel, dict) and rel.get("target") == target_id:
                    return True
            return False
        except Exception:
            return False

    def _find_entity_file(self, entity_id: str) -> Optional[Path]:
        """Find the file path for an entity ID."""
        # Check cache first
        if entity_id in self._entity_cache:
            return self._entity_cache[entity_id]

        for entity_path in self._get_entity_files():
            try:
                content = entity_path.read_text(encoding="utf-8")
                frontmatter, _ = self._parse_content(content)
                eid = frontmatter.get("$id", "")

                # Cache this mapping
                if eid:
                    self._entity_cache[eid] = entity_path

                if eid == entity_id:
                    return entity_path
            except Exception:
                continue

        return None

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

    def _parse_date(self, value: Any) -> Optional[date]:
        """Parse date from various formats."""
        if not value:
            return None
        if isinstance(value, date):
            return value
        if isinstance(value, str):
            try:
                return date.fromisoformat(value[:10])
            except ValueError:
                return None
        return None
