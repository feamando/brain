#!/usr/bin/env python3
"""
PM-OS Brain Event Query

Query and inspect events across Brain entities.
Provides both a Python API (EventQuery class) and a CLI entry point.

Commands (CLI):
    timeline <entity_path>            Show event timeline for an entity
    recent [--days N] [--actor X]     Show recent events
    stats [--since DATE]              Show event counts by type and actor

Usage (CLI):
    pmos-event-query timeline Entities/People/Jane_Smith.md
    pmos-event-query recent --days 7
    pmos-event-query recent --actor system/jira_enricher
    pmos-event-query stats --since 2026-02-01

Usage (Python API):
    from pmos_brain.storage.event_query import EventQuery

    eq = EventQuery("/path/to/brain")
    timeline = eq.timeline("Entities/People/Jane_Smith.md")
    recent = eq.recent(days=7, actor="system/jira_enricher")
    stats = eq.stats(since="2026-02-01")
"""

import argparse
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from pmos_brain.storage.event_store import EventStore


# ---------------------------------------------------------------------------
# EventQuery: clean Python API
# ---------------------------------------------------------------------------

class EventQuery:
    """High-level query interface for Brain events.

    Wraps an :class:`EventStore` and exposes ``timeline``, ``recent``, and
    ``stats`` as pure-data methods (no printing, no ``sys.exit``).

    Example::

        eq = EventQuery("/path/to/brain")
        for entry in eq.timeline("Entities/People/Jane_Smith.md"):
            print(entry["timestamp"], entry["event_type"])
    """

    def __init__(self, brain_path: str | Path):
        self.brain_path = Path(brain_path)
        self.store = EventStore(self.brain_path)

    # -- timeline -----------------------------------------------------------

    def timeline(self, entity_ref: str) -> List[Dict[str, Any]]:
        """Return the event timeline for a single entity.

        Args:
            entity_ref: Entity path relative to the brain directory, e.g.
                ``"Entities/People/Jane_Smith.md"``.

        Returns:
            List of timeline dicts (timestamp, event_type, actor, message,
            changes).  Empty list when the entity has no events.

        Raises:
            FileNotFoundError: If the entity file cannot be located.
        """
        entity_path = self._resolve_entity(entity_ref)
        return self.store.get_entity_timeline(entity_path)

    # -- recent -------------------------------------------------------------

    def recent(
        self,
        days: int = 1,
        actor: Optional[str] = None,
        entity_type: Optional[str] = None,
        limit: int = 50,
    ) -> List[Dict[str, Any]]:
        """Return recent events across all entities.

        Args:
            days: Look-back window in days (default ``1``).
            actor: Optional actor filter.
            entity_type: Optional entity-type directory filter.
            limit: Maximum number of events to return.

        Returns:
            List of event dicts sorted by timestamp descending.
        """
        since = datetime.now(timezone.utc) - timedelta(days=days)

        entity_pattern = None
        if entity_type:
            entity_pattern = f"Entities/**/{entity_type}/**/*.md"

        actors = [actor] if actor else None

        events = self.store.query_events(
            since=since,
            actors=actors,
            entity_pattern=entity_pattern,
            limit=limit,
        )

        return [
            {
                "timestamp": e.timestamp.isoformat(),
                "event_type": e.event_type,
                "actor": e.actor,
                "entity_id": e.entity_id,
                "message": e.message,
                "changes": e.changes,
            }
            for e in events
        ]

    # -- stats --------------------------------------------------------------

    def stats(
        self,
        since: Optional[str | datetime] = None,
    ) -> Dict[str, Any]:
        """Return event statistics.

        Args:
            since: Optional start boundary.  Accepts an ISO-8601 date string
                (``"2026-02-01"``) or a :class:`datetime` instance.

        Returns:
            Dict with keys ``total``, ``by_type``, ``by_actor``.
        """
        since_dt = self._coerce_datetime(since)

        by_type = self.store.count_events(since=since_dt, group_by="type")
        by_actor = self.store.count_events(since=since_dt, group_by="actor")
        total = sum(by_type.values())

        return {
            "total": total,
            "by_type": by_type,
            "by_actor": by_actor,
            "since": since_dt.isoformat() if since_dt else None,
        }

    # -- helpers ------------------------------------------------------------

    def _resolve_entity(self, entity_ref: str) -> Path:
        """Resolve *entity_ref* to an existing file inside the brain."""
        entity_path = self.brain_path / entity_ref
        if entity_path.exists():
            return entity_path

        # Try appending .md
        if not entity_ref.endswith(".md"):
            entity_path = self.brain_path / f"{entity_ref}.md"
            if entity_path.exists():
                return entity_path

        raise FileNotFoundError(f"Entity not found: {entity_ref}")

    @staticmethod
    def _coerce_datetime(value: Optional[str | datetime]) -> Optional[datetime]:
        if value is None:
            return None
        if isinstance(value, datetime):
            return value
        return datetime.fromisoformat(value).replace(tzinfo=timezone.utc)


# ---------------------------------------------------------------------------
# CLI command implementations
# ---------------------------------------------------------------------------

def cmd_timeline(store: EventStore, brain_path: Path, entity_ref: str) -> int:
    """Show event timeline for an entity."""
    entity_path = brain_path / entity_ref

    if not entity_path.exists():
        # Try with .md extension
        if not entity_ref.endswith(".md"):
            entity_path = brain_path / f"{entity_ref}.md"
        if not entity_path.exists():
            print(f"Entity not found: {entity_ref}", file=sys.stderr)
            return 1

    timeline = store.get_entity_timeline(entity_path)

    if not timeline:
        print(f"No events found for {entity_ref}")
        return 0

    print(f"Timeline for {entity_ref}")
    print(f"{'=' * 60}")

    for entry in timeline:
        ts = entry["timestamp"][:19]
        etype = entry["event_type"]
        actor = entry["actor"]
        message = entry.get("message", "")
        changes = entry.get("changes", [])

        print(f"\n  {ts}  [{etype}]")
        print(f"  Actor: {actor}")
        if message:
            print(f"  Message: {message}")
        if changes:
            for c in changes:
                field = c.get("field", "?")
                op = c.get("operation", "?")
                value = c.get("value", "")
                old = c.get("old_value")
                change_str = f"    {field}: {op}"
                if old is not None:
                    change_str += f" ({old} -> {value})"
                elif value:
                    change_str += f" = {value}"
                print(change_str)

    print(f"\n{'=' * 60}")
    print(f"Total: {len(timeline)} events")
    return 0


def cmd_recent(
    store: EventStore,
    brain_path: Path,
    days: int = 1,
    actor: Optional[str] = None,
    entity_type: Optional[str] = None,
    limit: int = 50,
) -> int:
    """Show recent events."""
    since = datetime.now(timezone.utc) - timedelta(days=days)

    # Scope to entity type directory if specified
    entity_pattern = None
    if entity_type:
        entity_pattern = f"Entities/**/{entity_type}/**/*.md"

    actors = [actor] if actor else None

    events = store.query_events(
        since=since,
        actors=actors,
        entity_pattern=entity_pattern,
        limit=limit,
    )

    if not events:
        print(f"No events in the last {days} day(s)")
        if actor:
            print(f"  (filtered by actor: {actor})")
        return 0

    print(f"Recent events (last {days} day(s))")
    if actor:
        print(f"  Actor filter: {actor}")
    print(f"{'=' * 60}")

    for event in events:
        ts = event.timestamp.strftime("%Y-%m-%d %H:%M")
        print(f"\n  {ts}  [{event.event_type}]  {event.entity_id}")
        print(f"  Actor: {event.actor}")
        if event.message:
            print(f"  Message: {event.message[:80]}")

    print(f"\n{'=' * 60}")
    print(f"Total: {len(events)} events")
    return 0


def cmd_stats(
    store: EventStore,
    since: Optional[datetime] = None,
) -> int:
    """Show event statistics."""
    by_type = store.count_events(since=since, group_by="type")
    by_actor = store.count_events(since=since, group_by="actor")

    total = sum(by_type.values())
    since_str = since.strftime("%Y-%m-%d") if since else "all time"

    print(f"Event Statistics (since {since_str})")
    print(f"{'=' * 60}")
    print(f"Total events: {total}")

    if by_type:
        print(f"\nBy type:")
        for etype, count in sorted(by_type.items(), key=lambda x: -x[1]):
            pct = count / total * 100 if total else 0
            print(f"  {etype:30s} {count:5d}  ({pct:.1f}%)")

    if by_actor:
        print(f"\nBy actor:")
        for actor_name, count in sorted(by_actor.items(), key=lambda x: -x[1]):
            pct = count / total * 100 if total else 0
            print(f"  {actor_name:30s} {count:5d}  ({pct:.1f}%)")

    print(f"{'=' * 60}")
    return 0


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Query Brain entity events",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # timeline command
    timeline_parser = subparsers.add_parser(
        "timeline", help="Show entity event timeline",
    )
    timeline_parser.add_argument(
        "entity", help="Entity path relative to brain dir",
    )

    # recent command
    recent_parser = subparsers.add_parser("recent", help="Show recent events")
    recent_parser.add_argument(
        "--days", type=int, default=1, help="Number of days (default: 1)",
    )
    recent_parser.add_argument("--actor", type=str, help="Filter by actor")
    recent_parser.add_argument(
        "--type", type=str, dest="entity_type",
        help="Filter by entity type directory",
    )
    recent_parser.add_argument(
        "--limit", type=int, default=50, help="Max events (default: 50)",
    )

    # stats command
    stats_parser = subparsers.add_parser("stats", help="Show event statistics")
    stats_parser.add_argument(
        "--since", type=str, help="Start date (YYYY-MM-DD)",
    )

    # brain path (global)
    parser.add_argument(
        "--brain-path", type=Path, required=True,
        help="Path to brain directory",
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    brain_path: Path = args.brain_path
    store = EventStore(brain_path)

    if args.command == "timeline":
        return cmd_timeline(store, brain_path, args.entity)

    elif args.command == "recent":
        return cmd_recent(
            store,
            brain_path,
            days=args.days,
            actor=args.actor,
            entity_type=args.entity_type,
            limit=args.limit,
        )

    elif args.command == "stats":
        since = None
        if args.since:
            since = datetime.fromisoformat(args.since).replace(tzinfo=timezone.utc)
        return cmd_stats(store, since=since)

    return 0


if __name__ == "__main__":
    sys.exit(main())
