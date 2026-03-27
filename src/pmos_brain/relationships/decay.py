"""
Brain Relationship Decay Monitor

Tracks relationship staleness and confidence decay.
Identifies relationships that need re-verification.
"""

from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml


@dataclass
class StaleRelationship:
    """A relationship flagged as stale."""

    entity_id: str
    entity_type: str
    relationship_type: str
    target: str
    base_confidence: float
    decayed_confidence: float
    last_verified: Optional[date]
    days_stale: int
    source: Optional[str] = None


@dataclass
class RelationshipDecayReport:
    """Summary report of relationship staleness."""

    total_entities: int
    total_relationships: int
    stale_relationships: int
    avg_confidence: float
    avg_decayed_confidence: float
    stale_by_type: Dict[str, int] = field(default_factory=dict)
    stale_list: List[StaleRelationship] = field(default_factory=list)


class RelationshipDecayMonitor:
    """
    Monitors relationship staleness and confidence decay.

    Based on TKS temporal decay formula:
    conf(t) = max(floor, base * (1 - decay_rate * weeks_stale))
    """

    # Default staleness thresholds by relationship type (days)
    STALENESS_THRESHOLDS = {
        "reports_to": 90,  # Org structure - relatively stable
        "manages": 90,
        "member_of": 60,  # Team membership changes more often
        "owns": 60,
        "works_with": 45,  # Collaboration relationships
        "collaborates_with": 45,
        "depends_on": 30,  # Technical dependencies
        "blocks": 14,  # Should be resolved quickly
        "related_to": 90,
        "similar_to": 120,  # Inferred relationships - more stable
        "default": 90,
    }

    def __init__(
        self,
        brain_path: Path,
        decay_rate: float = 0.01,
        confidence_floor: float = 0.3,
    ):
        """
        Initialize the decay monitor.

        Args:
            brain_path: Path to brain directory
            decay_rate: Weekly decay rate (default: 1%)
            confidence_floor: Minimum confidence (default: 0.3)
        """
        self.brain_path = brain_path
        self.decay_rate = decay_rate
        self.confidence_floor = confidence_floor

    def scan_relationships(
        self,
        as_of: Optional[date] = None,
        threshold_days: Optional[int] = None,
    ) -> RelationshipDecayReport:
        """
        Scan all entities for relationship staleness.

        Args:
            as_of: Date to check against (default: today)
            threshold_days: Override default threshold

        Returns:
            RelationshipDecayReport with findings
        """
        check_date = as_of or date.today()

        total_entities = 0
        total_relationships = 0
        stale_relationships = []
        confidence_sum = 0.0
        decayed_sum = 0.0
        stale_by_type: Dict[str, int] = {}

        # Find all entity files
        entity_files = list(self.brain_path.rglob("*.md"))
        entity_files = [
            f
            for f in entity_files
            if f.name.lower() not in ("readme.md", "index.md", "_index.md")
            and ".snapshots" not in str(f)
            and ".schema" not in str(f)
        ]

        for entity_path in entity_files:
            try:
                content = entity_path.read_text(encoding="utf-8")
                frontmatter, _ = self._parse_content(content)

                if not frontmatter:
                    continue

                total_entities += 1
                entity_id = frontmatter.get(
                    "$id", str(entity_path.relative_to(self.brain_path))
                )
                entity_type = frontmatter.get("$type", "unknown")
                relationships = frontmatter.get("$relationships", [])

                for rel in relationships:
                    if not isinstance(rel, dict):
                        continue

                    total_relationships += 1

                    rel_type = rel.get("type", "unknown")
                    target = rel.get("target", "unknown")
                    base_confidence = rel.get("confidence", 1.0)
                    last_verified = self._parse_date(rel.get("last_verified"))
                    since = self._parse_date(rel.get("since"))
                    source = rel.get("source")

                    # Compute decayed confidence
                    decayed = self._compute_decay(
                        base_confidence,
                        last_verified or since,
                        check_date,
                    )

                    confidence_sum += base_confidence
                    decayed_sum += decayed

                    # Check if stale
                    threshold = threshold_days or self.STALENESS_THRESHOLDS.get(
                        rel_type, self.STALENESS_THRESHOLDS["default"]
                    )

                    ref_date = last_verified or since
                    days_stale = (check_date - ref_date).days if ref_date else 999

                    if days_stale > threshold:
                        stale_rel = StaleRelationship(
                            entity_id=entity_id,
                            entity_type=entity_type,
                            relationship_type=rel_type,
                            target=target,
                            base_confidence=base_confidence,
                            decayed_confidence=round(decayed, 3),
                            last_verified=last_verified,
                            days_stale=days_stale,
                            source=source,
                        )
                        stale_relationships.append(stale_rel)
                        stale_by_type[rel_type] = stale_by_type.get(rel_type, 0) + 1

            except Exception:
                continue

        return RelationshipDecayReport(
            total_entities=total_entities,
            total_relationships=total_relationships,
            stale_relationships=len(stale_relationships),
            avg_confidence=(
                round(confidence_sum / total_relationships, 3)
                if total_relationships
                else 0
            ),
            avg_decayed_confidence=(
                round(decayed_sum / total_relationships, 3)
                if total_relationships
                else 0
            ),
            stale_by_type=stale_by_type,
            stale_list=sorted(stale_relationships, key=lambda x: -x.days_stale),
        )

    def _compute_decay(
        self,
        base_confidence: float,
        reference_date: Optional[date],
        as_of: date,
    ) -> float:
        """Compute decayed confidence."""
        if not reference_date:
            return max(self.confidence_floor, base_confidence * 0.7)

        days_stale = (as_of - reference_date).days
        if days_stale <= 0:
            return base_confidence

        weeks_stale = days_stale / 7
        decay = self.decay_rate * weeks_stale
        decayed = base_confidence * (1 - decay)

        return max(self.confidence_floor, min(base_confidence, decayed))

    def _parse_date(self, value: Any) -> Optional[date]:
        """Parse date from various formats."""
        if not value:
            return None
        if isinstance(value, date):
            return value
        if isinstance(value, datetime):
            return value.date()
        if isinstance(value, str):
            try:
                return date.fromisoformat(value[:10])
            except ValueError:
                return None
        return None

    def _parse_content(self, content: str) -> Tuple[Dict[str, Any], str]:
        """Parse YAML frontmatter from content."""
        if not content.startswith("---"):
            return {}, content

        parts = content.split("---", 2)
        if len(parts) < 3:
            return {}, content

        try:
            frontmatter = yaml.safe_load(parts[1]) or {}
            return frontmatter, parts[2]
        except yaml.YAMLError:
            return {}, content
