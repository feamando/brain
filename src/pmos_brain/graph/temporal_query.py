"""
Temporal Query System - Point-in-time reconstruction and temporal queries.

Enables:
- Point-in-time entity state reconstruction
- Change history analysis
- Temporal comparisons
- State diff generation
"""

import copy
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


@dataclass
class EntitySnapshot:
    """Represents entity state at a point in time."""
    entity_id: str
    timestamp: datetime
    frontmatter: Dict[str, Any]
    body: str
    version: int


@dataclass
class Event:
    """Represents a single change event."""
    event_id: str
    timestamp: datetime
    event_type: str
    actor: str
    entity_id: str
    message: str
    changes: List[Dict[str, Any]]


class TemporalQuery:
    """
    Enables temporal queries on Brain entities.

    Supports:
    - Point-in-time reconstruction
    - Change history analysis
    - Temporal comparisons
    - State diff generation

    Example:
        query = TemporalQuery(brain_path)
        snapshot = query.get_entity_at(entity_path, datetime(2024, 1, 1))
        diff = query.compare_states(entity_path, time_a, time_b)
    """

    def __init__(self, brain_path: Union[str, Path]):
        """
        Initialize the temporal query system.

        Args:
            brain_path: Path to the brain directory
        """
        self.brain_path = Path(brain_path)
        self.snapshot_cache: Dict[str, Dict[str, EntitySnapshot]] = {}

    def get_entity_at(
        self,
        entity_path: Path,
        point_in_time: datetime,
    ) -> Optional[EntitySnapshot]:
        """
        Reconstruct entity state at a specific point in time.

        Args:
            entity_path: Path to entity file
            point_in_time: The point in time to reconstruct

        Returns:
            EntitySnapshot if reconstruction possible, None otherwise
        """
        if not entity_path.exists():
            return None

        content = entity_path.read_text(encoding="utf-8")
        frontmatter, body = self._parse_content(content)

        try:
            entity_id = str(entity_path.relative_to(self.brain_path))
        except ValueError:
            entity_id = entity_path.stem

        # Get all events for this entity
        all_events = self._get_entity_events(entity_path)

        if not all_events:
            # No events, return current state if created before point_in_time
            created = frontmatter.get("$created", "")
            if created:
                created_dt = self._parse_datetime(created)
                if created_dt and created_dt <= point_in_time:
                    return EntitySnapshot(
                        entity_id=entity_id,
                        timestamp=point_in_time,
                        frontmatter=frontmatter,
                        body=body,
                        version=frontmatter.get("$version", 1),
                    )
            return None

        # Filter events up to point_in_time
        relevant_events = [
            e for e in all_events
            if e.timestamp <= point_in_time
        ]

        if not relevant_events:
            return None

        # Reconstruct state by replaying events
        reconstructed = self._reconstruct_from_events(
            frontmatter, body, relevant_events
        )

        return EntitySnapshot(
            entity_id=entity_id,
            timestamp=point_in_time,
            frontmatter=reconstructed["frontmatter"],
            body=reconstructed["body"],
            version=len(relevant_events),
        )

    def compare_states(
        self,
        entity_path: Path,
        time_a: datetime,
        time_b: datetime,
    ) -> Dict[str, Any]:
        """
        Compare entity state between two points in time.

        Args:
            entity_path: Path to entity file
            time_a: First point in time
            time_b: Second point in time

        Returns:
            Dictionary with differences
        """
        state_a = self.get_entity_at(entity_path, time_a)
        state_b = self.get_entity_at(entity_path, time_b)

        try:
            entity_id = str(entity_path.relative_to(self.brain_path))
        except ValueError:
            entity_id = entity_path.stem

        diff = {
            "entity_id": entity_id,
            "time_a": time_a.isoformat(),
            "time_b": time_b.isoformat(),
            "exists_at_a": state_a is not None,
            "exists_at_b": state_b is not None,
            "field_changes": [],
        }

        if state_a and state_b:
            diff["field_changes"] = self._diff_frontmatter(
                state_a.frontmatter, state_b.frontmatter
            )
            diff["version_a"] = state_a.version
            diff["version_b"] = state_b.version

        return diff

    def get_field_history(
        self,
        entity_path: Path,
        field_name: str,
        since: Optional[datetime] = None,
    ) -> List[Dict[str, Any]]:
        """
        Get the history of changes to a specific field.

        Args:
            entity_path: Path to entity file
            field_name: Name of the field to track
            since: Only show changes after this time

        Returns:
            List of changes to the field
        """
        events = self._get_entity_events(entity_path)

        if since:
            events = [e for e in events if e.timestamp >= since]

        history = []

        for event in events:
            for change in event.changes:
                if change.get("field") == field_name:
                    history.append({
                        "timestamp": event.timestamp.isoformat(),
                        "operation": change.get("operation", "unknown"),
                        "old_value": change.get("old_value"),
                        "new_value": change.get("value"),
                        "actor": event.actor,
                        "event_id": event.event_id,
                    })

        return history

    def query_entities_at(
        self,
        point_in_time: datetime,
        entity_type: Optional[str] = None,
        status: Optional[str] = None,
    ) -> List[EntitySnapshot]:
        """
        Query all entities at a specific point in time.

        Args:
            point_in_time: The point in time to query
            entity_type: Filter by entity type
            status: Filter by status

        Returns:
            List of entity snapshots matching criteria
        """
        snapshots = []

        # Find all entity files
        entity_files = list(self.brain_path.rglob("*.md"))
        entity_files = [
            f for f in entity_files
            if f.name.lower() not in ("readme.md", "index.md", "_index.md")
        ]

        for entity_path in entity_files:
            snapshot = self.get_entity_at(entity_path, point_in_time)
            if not snapshot:
                continue

            # Apply filters
            if entity_type:
                if snapshot.frontmatter.get("$type") != entity_type:
                    continue
            if status:
                if snapshot.frontmatter.get("$status") != status:
                    continue

            snapshots.append(snapshot)

        return snapshots

    def get_changes_in_period(
        self,
        start: datetime,
        end: datetime,
        entity_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Get summary of changes in a time period.

        Args:
            start: Start of period
            end: End of period
            entity_type: Filter by entity type

        Returns:
            Summary of changes
        """
        all_events = []

        # Collect events from all entities
        entity_files = list(self.brain_path.rglob("*.md"))
        entity_files = [
            f for f in entity_files
            if f.name.lower() not in ("readme.md", "index.md", "_index.md")
        ]

        for entity_path in entity_files:
            events = self._get_entity_events(entity_path)
            events = [e for e in events if start <= e.timestamp <= end]
            all_events.extend(events)

        summary = {
            "period_start": start.isoformat(),
            "period_end": end.isoformat(),
            "total_events": len(all_events),
            "entities_changed": len(set(e.entity_id for e in all_events)),
            "by_type": {},
            "by_actor": {},
            "by_entity": {},
        }

        for event in all_events:
            # Count by event type
            event_type = event.event_type
            summary["by_type"][event_type] = summary["by_type"].get(event_type, 0) + 1

            # Count by actor
            actor = event.actor
            summary["by_actor"][actor] = summary["by_actor"].get(actor, 0) + 1

            # Count by entity
            entity_id = event.entity_id
            summary["by_entity"][entity_id] = summary["by_entity"].get(entity_id, 0) + 1

        return summary

    def _get_entity_events(self, entity_path: Path) -> List[Event]:
        """Load events from entity file."""
        if not entity_path.exists():
            return []

        try:
            content = entity_path.read_text(encoding="utf-8")
            frontmatter, _ = self._parse_content(content)

            try:
                entity_id = str(entity_path.relative_to(self.brain_path))
            except ValueError:
                entity_id = entity_path.stem

            raw_events = frontmatter.get("$events", [])
            events = []

            for raw in raw_events:
                timestamp = raw.get("timestamp", "")
                if isinstance(timestamp, str):
                    timestamp = self._parse_datetime(timestamp) or datetime.utcnow()
                elif not isinstance(timestamp, datetime):
                    timestamp = datetime.utcnow()

                events.append(Event(
                    event_id=raw.get("event_id", ""),
                    timestamp=timestamp,
                    event_type=raw.get("type", "unknown"),
                    actor=raw.get("actor", "unknown"),
                    entity_id=raw.get("entity_id", entity_id),
                    message=raw.get("message", ""),
                    changes=raw.get("changes", []),
                ))

            return sorted(events, key=lambda e: e.timestamp)

        except Exception:
            return []

    def _reconstruct_from_events(
        self,
        base_frontmatter: Dict[str, Any],
        base_body: str,
        events: List[Event],
    ) -> Dict[str, Any]:
        """Reconstruct state by replaying events."""
        frontmatter = copy.deepcopy(base_frontmatter)

        # Track which fields changed
        changed_fields = set()

        for event in events:
            for change in event.changes:
                field = change.get("field", "")
                if field:
                    changed_fields.add(field)

        return {
            "frontmatter": frontmatter,
            "body": base_body,
            "changed_fields": list(changed_fields),
        }

    def _diff_frontmatter(
        self,
        fm_a: Dict[str, Any],
        fm_b: Dict[str, Any],
    ) -> List[Dict[str, Any]]:
        """Generate diff between two frontmatter dicts."""
        changes = []
        all_keys = set(fm_a.keys()) | set(fm_b.keys())

        for key in all_keys:
            if key.startswith("$events"):
                continue  # Skip events in diff

            val_a = fm_a.get(key)
            val_b = fm_b.get(key)

            if val_a != val_b:
                changes.append({
                    "field": key,
                    "old_value": val_a,
                    "new_value": val_b,
                })

        return changes

    def _parse_content(self, content: str) -> Tuple[Dict[str, Any], str]:
        """Parse frontmatter and body from content."""
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

    def _parse_datetime(self, date_str: str) -> Optional[datetime]:
        """Parse datetime from string."""
        if not date_str:
            return None

        try:
            return datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        except (ValueError, TypeError):
            return None
