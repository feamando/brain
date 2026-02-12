#!/usr/bin/env python3
"""
PM-OS Brain Event Helpers (Standalone)

Centralized module for creating and appending events to Brain entities.
All write paths MUST use this module instead of constructing event dicts directly.

Usage:
    from event_helpers import EventHelper

    event = EventHelper.create_event(
        event_type="field_update",
        actor="system/brain_updater",
        changes=[{"field": "status", "operation": "set", "value": "active"}],
        message="Updated status from context",
    )
    frontmatter = EventHelper.append_to_frontmatter(frontmatter, event)
"""

from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional
from uuid import uuid4

# ---------------------------------------------------------------------------
# Inline schema definitions (ported from schemas/brain/event.py)
# ---------------------------------------------------------------------------

try:
    from pydantic import BaseModel, Field

    HAS_PYDANTIC = True
except Exception:
    HAS_PYDANTIC = False


class EventType(str, Enum):
    """Types of changes that can be logged."""

    # Field changes
    FIELD_UPDATE = "field_update"
    FIELD_ADD = "field_add"
    FIELD_REMOVE = "field_remove"

    # Relationship changes
    RELATIONSHIP_ADD = "relationship_add"
    RELATIONSHIP_REMOVE = "relationship_remove"
    RELATIONSHIP_UPDATE = "relationship_update"

    # Status changes
    STATUS_CHANGE = "status_change"

    # Entity lifecycle
    ENTITY_CREATE = "entity_create"
    ENTITY_ARCHIVE = "entity_archive"
    ENTITY_RESTORE = "entity_restore"

    # Metadata updates
    CONFIDENCE_UPDATE = "confidence_update"
    VERIFICATION = "verification"


if HAS_PYDANTIC:

    class FieldChange(BaseModel):
        """A single field change within an event."""

        field: str = Field(
            ...,
            description="Field path that changed (e.g., 'role', '$relationships')",
        )

        operation: str = Field(
            ...,
            description="Operation performed: set, append, remove, update",
        )

        value: Optional[Any] = Field(
            default=None,
            description="New value (for set/append) or removed value (for remove)",
        )

        old_value: Optional[Any] = Field(
            default=None,
            description="Previous value (for audit trail)",
        )

    class ChangeEvent(BaseModel):
        """
        An immutable record of a change to an entity.

        Events are append-only and enable:
        - Full audit trail
        - Point-in-time reconstruction
        - Change attribution
        """

        event_id: str = Field(
            default_factory=lambda: f"evt-{uuid4().hex[:12]}",
            description="Unique event identifier",
        )

        timestamp: datetime = Field(
            default_factory=lambda: datetime.now(timezone.utc),
            description="When the change occurred (UTC)",
        )

        type: EventType = Field(
            ...,
            description="Type of change",
        )

        actor: str = Field(
            ...,
            description="Who/what made the change (e.g., 'user/jane', 'system/daily_context')",
        )

        changes: List[FieldChange] = Field(
            default_factory=list,
            description="List of field changes in this event",
        )

        correlation_id: Optional[str] = Field(
            default=None,
            description="ID to correlate related events",
        )

        source: Optional[str] = Field(
            default=None,
            description="Source system or document that triggered this change",
        )

        message: Optional[str] = Field(
            default=None,
            description="Human-readable description of the change",
        )

else:
    # Lightweight fallback when pydantic is not installed
    from dataclasses import dataclass, field as dc_field

    @dataclass
    class FieldChange:  # type: ignore[no-redef]
        """A single field change within an event (dataclass fallback)."""

        field: str = ""
        operation: str = ""
        value: Optional[Any] = None
        old_value: Optional[Any] = None

        def model_dump(self, **_kwargs: Any) -> Dict[str, Any]:
            return {
                "field": self.field,
                "operation": self.operation,
                "value": self.value,
                "old_value": self.old_value,
            }

    @dataclass
    class ChangeEvent:  # type: ignore[no-redef]
        """An immutable record of a change to an entity (dataclass fallback)."""

        event_id: str = ""
        timestamp: datetime = dc_field(default_factory=lambda: datetime.now(timezone.utc))
        type: EventType = EventType.FIELD_UPDATE
        actor: str = ""
        changes: List[FieldChange] = dc_field(default_factory=list)  # type: ignore[type-arg]
        correlation_id: Optional[str] = None
        source: Optional[str] = None
        message: Optional[str] = None

        def model_dump(self, **_kwargs: Any) -> Dict[str, Any]:
            return {
                "event_id": self.event_id,
                "timestamp": self.timestamp,
                "type": self.type,
                "actor": self.actor,
                "changes": self.changes,
                "correlation_id": self.correlation_id,
                "source": self.source,
                "message": self.message,
            }


# ---------------------------------------------------------------------------
# Event compaction settings
# ---------------------------------------------------------------------------
MAX_EVENTS_PER_ENTITY = 10
COMPACT_THRESHOLD = MAX_EVENTS_PER_ENTITY


class EventHelper:
    """Centralized event creation and management for Brain entities."""

    @staticmethod
    def create_event(
        event_type: str,
        actor: str,
        changes: Optional[List[Dict[str, Any]]] = None,
        message: str = "",
        source: Optional[str] = None,
        correlation_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Create a standardized event dict validated through ChangeEvent Pydantic model.

        Args:
            event_type: Must be a valid EventType value (e.g., "field_update", "relationship_add")
            actor: Who/what made the change (e.g., "system/relationship_builder", "user/jane")
            changes: List of field change dicts with keys: field, operation, value, old_value (optional)
            message: Human-readable description of the change
            source: Source system (e.g., "jira:PROJ-123", "body_extraction")
            correlation_id: ID to correlate related events (e.g., "context-2026-02-11")

        Returns:
            YAML-safe dict matching ChangeEvent schema
        """
        # Validate event_type against enum
        validated_type = EventType(event_type)

        # Build FieldChange objects for validation
        field_changes = []
        for change in (changes or []):
            field_changes.append(
                FieldChange(
                    field=change["field"],
                    operation=change["operation"],
                    value=change.get("value"),
                    old_value=change.get("old_value"),
                )
            )

        # Create and validate through Pydantic model
        event = ChangeEvent(
            event_id=f"evt-{uuid4().hex[:12]}",
            timestamp=datetime.now(timezone.utc),
            type=validated_type,
            actor=actor,
            changes=field_changes,
            source=source,
            correlation_id=correlation_id,
            message=message,
        )

        # Convert to YAML-safe dict
        data = event.model_dump(mode="python")

        # Ensure timestamp is ISO string for YAML
        data["timestamp"] = event.timestamp.isoformat()

        # Convert EventType enum to string value
        data["type"] = event.type.value

        # Convert FieldChange objects to plain dicts, dropping None values
        data["changes"] = []
        for fc in event.changes:
            change_dict: Dict[str, Any] = {
                "field": fc.field,
                "operation": fc.operation,
            }
            if fc.value is not None:
                change_dict["value"] = fc.value
            if fc.old_value is not None:
                change_dict["old_value"] = fc.old_value
            data["changes"].append(change_dict)

        # Drop None optional fields for cleaner YAML
        if data.get("source") is None:
            del data["source"]
        if data.get("correlation_id") is None:
            del data["correlation_id"]
        if data.get("message") is None:
            del data["message"]

        return data

    @staticmethod
    def append_to_frontmatter(
        frontmatter: Dict[str, Any],
        event: Dict[str, Any],
        increment_version: bool = True,
        update_timestamp: bool = True,
    ) -> Dict[str, Any]:
        """
        Append an event to entity frontmatter, atomically updating version and timestamp.

        Args:
            frontmatter: Entity YAML frontmatter dict (modified in place)
            event: Event dict from create_event()
            increment_version: Whether to increment $version
            update_timestamp: Whether to update $updated

        Returns:
            The modified frontmatter dict
        """
        if "$events" not in frontmatter:
            frontmatter["$events"] = []

        frontmatter["$events"].append(event)

        if increment_version:
            frontmatter["$version"] = frontmatter.get("$version", 0) + 1

        if update_timestamp:
            frontmatter["$updated"] = datetime.now(timezone.utc).isoformat()

        # Run compaction if over threshold
        frontmatter = EventHelper.compact_events(frontmatter)

        return frontmatter

    @staticmethod
    def create_field_update(
        actor: str,
        field: str,
        new_value: Any,
        old_value: Any = None,
        source: Optional[str] = None,
        message: Optional[str] = None,
        correlation_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Factory for field update events."""
        changes = [{"field": field, "operation": "set", "value": new_value}]
        if old_value is not None:
            changes[0]["old_value"] = old_value

        return EventHelper.create_event(
            event_type=EventType.FIELD_UPDATE.value,
            actor=actor,
            changes=changes,
            message=message or f"Updated {field}",
            source=source,
            correlation_id=correlation_id,
        )

    @staticmethod
    def create_relationship_event(
        actor: str,
        target: str,
        rel_type: str,
        operation: str = "add",
        source: Optional[str] = None,
        message: Optional[str] = None,
        correlation_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Factory for relationship add/remove events."""
        if operation == "add":
            event_type = EventType.RELATIONSHIP_ADD.value
            op = "append"
        elif operation == "remove":
            event_type = EventType.RELATIONSHIP_REMOVE.value
            op = "remove"
        else:
            event_type = EventType.RELATIONSHIP_UPDATE.value
            op = "update"

        return EventHelper.create_event(
            event_type=event_type,
            actor=actor,
            changes=[{
                "field": "$relationships",
                "operation": op,
                "value": {"type": rel_type, "target": target},
            }],
            message=message or f"Relationship {operation}: {rel_type} -> {target}",
            source=source,
            correlation_id=correlation_id,
        )

    @staticmethod
    def create_status_change(
        actor: str,
        old_status: Optional[str],
        new_status: str,
        source: Optional[str] = None,
        message: Optional[str] = None,
        correlation_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Factory for status change events."""
        changes = [{"field": "$status", "operation": "set", "value": new_status}]
        if old_status is not None:
            changes[0]["old_value"] = old_status

        return EventHelper.create_event(
            event_type=EventType.STATUS_CHANGE.value,
            actor=actor,
            changes=changes,
            message=message or f"Status changed: {old_status} -> {new_status}",
            source=source,
            correlation_id=correlation_id,
        )

    @staticmethod
    def compact_events(
        frontmatter: Dict[str, Any],
        max_events: int = MAX_EVENTS_PER_ENTITY,
    ) -> Dict[str, Any]:
        """
        Compact events to stay within token budget.

        Strategy: keep first event (creation), last (max_events - 2) events,
        and one compacted summary of the middle.

        Args:
            frontmatter: Entity frontmatter dict (modified in place)
            max_events: Maximum events to retain

        Returns:
            The modified frontmatter dict
        """
        events = frontmatter.get("$events", [])
        if len(events) <= max_events:
            return frontmatter

        first = events[0]
        keep_recent = max_events - 2  # Reserve 2 slots: first + summary
        recent = events[-keep_recent:]
        middle = events[1:-keep_recent]

        # Build summary of compacted events
        compacted_fields = set()
        compacted_actors = set()
        for evt in middle:
            for change in evt.get("changes", []):
                compacted_fields.add(change.get("field", "unknown"))
            compacted_actors.add(evt.get("actor", "unknown"))

        # Get time range
        first_ts = middle[0].get("timestamp", "") if middle else ""
        last_ts = middle[-1].get("timestamp", "") if middle else ""

        summary_event = {
            "event_id": f"evt-compacted-{uuid4().hex[:8]}",
            "timestamp": last_ts,
            "type": "compacted_summary",
            "actor": "system/event_compaction",
            "message": (
                f"Compacted {len(middle)} events "
                f"({first_ts[:10]} to {last_ts[:10]}). "
                f"Fields: {', '.join(sorted(compacted_fields))}. "
                f"Actors: {', '.join(sorted(compacted_actors))}."
            ),
            "changes": [],
        }

        frontmatter["$events"] = [first, summary_event] + recent
        return frontmatter
