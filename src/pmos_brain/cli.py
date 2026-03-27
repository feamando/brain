#!/usr/bin/env python3
"""
PM-OS Brain CLI

Commands:
    pmos-brain search <query>     Search entities
    pmos-brain list [--type TYPE] List entities
    pmos-brain get <path>         Get entity details
    pmos-brain validate           Validate brain structure
    pmos-brain setup <path>       Initialize new brain
    pmos-brain events <command>   Query entity events
    pmos-brain index              Generate BRAIN.md index
    pmos-brain query <query>      Combined BRAIN+GRAPH query
    pmos-brain mcp                Start MCP server
    pmos-brain vector <command>   Vector search operations
    pmos-brain resolve <ref>      Resolve entity reference
    pmos-brain enrich [--mode]    Run enrichment pipeline
"""

import argparse
import sys
from pathlib import Path


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="pmos-brain",
        description="PM-OS Brain - Semantic Knowledge Graph CLI"
    )
    parser.add_argument("--version", action="version", version="%(prog)s 3.2.0")

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Search command
    search_parser = subparsers.add_parser("search", help="Search entities")
    search_parser.add_argument("query", help="Search query")
    search_parser.add_argument("--type", "-t", help="Entity type filter")
    search_parser.add_argument("--limit", "-n", type=int, default=10, help="Max results")
    search_parser.add_argument("--brain", "-b", default="./brain", help="Brain path")
    search_parser.add_argument("--semantic", action="store_true", help="Use semantic (vector) search")

    # List command
    list_parser = subparsers.add_parser("list", help="List entities")
    list_parser.add_argument("--type", "-t", help="Entity type filter")
    list_parser.add_argument("--brain", "-b", default="./brain", help="Brain path")

    # Get command
    get_parser = subparsers.add_parser("get", help="Get entity details")
    get_parser.add_argument("path", help="Entity path")
    get_parser.add_argument("--brain", "-b", default="./brain", help="Brain path")

    # Validate command
    validate_parser = subparsers.add_parser("validate", help="Validate brain")
    validate_parser.add_argument("--brain", "-b", default="./brain", help="Brain path")

    # Setup command
    setup_parser = subparsers.add_parser("setup", help="Initialize brain")
    setup_parser.add_argument("path", help="Path for new brain")

    # Events command
    events_parser = subparsers.add_parser("events", help="Query entity events")
    events_sub = events_parser.add_subparsers(dest="events_command", help="Event commands")

    # events timeline
    timeline_parser = events_sub.add_parser("timeline", help="Show entity event timeline")
    timeline_parser.add_argument("entity", help="Entity path relative to brain dir")
    timeline_parser.add_argument("--brain", "-b", default="./brain", help="Brain path")

    # events recent
    recent_parser = events_sub.add_parser("recent", help="Show recent events")
    recent_parser.add_argument("--days", type=int, default=1, help="Number of days (default: 1)")
    recent_parser.add_argument("--actor", type=str, help="Filter by actor")
    recent_parser.add_argument("--limit", type=int, default=50, help="Max events (default: 50)")
    recent_parser.add_argument("--brain", "-b", default="./brain", help="Brain path")

    # events stats
    stats_parser = events_sub.add_parser("stats", help="Show event statistics")
    stats_parser.add_argument("--since", type=str, help="Start date (YYYY-MM-DD)")
    stats_parser.add_argument("--brain", "-b", default="./brain", help="Brain path")

    # Index command
    index_parser = subparsers.add_parser("index", help="Generate BRAIN.md index")
    index_parser.add_argument("--brain", "-b", default="./brain", help="Brain path")
    index_parser.add_argument("--output", "-o", type=Path, help="Output file path")
    index_parser.add_argument("--config", "-c", type=Path, help="Team config YAML file")

    # Query command (NEW in v3.1.0)
    query_parser = subparsers.add_parser("query", help="Combined BRAIN+GRAPH query")
    query_parser.add_argument("query", help="Query string")
    query_parser.add_argument("--brain", "-b", default="./brain", help="Brain path")
    query_parser.add_argument("--limit", "-n", type=int, default=10, help="Max results")
    query_parser.add_argument("--no-graph", action="store_true", help="Skip graph expansion")
    query_parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")

    # MCP command (NEW in v3.1.0)
    mcp_parser = subparsers.add_parser("mcp", help="Start Brain MCP server")
    mcp_parser.add_argument("--brain", "-b", default="./brain", help="Brain path")

    # Vector command (NEW in v3.1.0)
    vector_parser = subparsers.add_parser("vector", help="Vector search operations")
    vector_sub = vector_parser.add_subparsers(dest="vector_command", help="Vector commands")

    vector_build = vector_sub.add_parser("build", help="Build vector index")
    vector_build.add_argument("--brain", "-b", default="./brain", help="Brain path")

    vector_query = vector_sub.add_parser("query", help="Semantic search")
    vector_query.add_argument("query", help="Search query")
    vector_query.add_argument("--brain", "-b", default="./brain", help="Brain path")
    vector_query.add_argument("--limit", "-n", type=int, default=10, help="Max results")

    vector_stats = vector_sub.add_parser("stats", help="Show index statistics")
    vector_stats.add_argument("--brain", "-b", default="./brain", help="Brain path")

    # Resolve command (NEW in v3.1.0)
    resolve_parser = subparsers.add_parser("resolve", help="Resolve entity reference")
    resolve_parser.add_argument("reference", help="Entity reference (id, slug, path, or alias)")
    resolve_parser.add_argument("--brain", "-b", default="./brain", help="Brain path")

    # Enrich command (NEW in v3.1.0)
    enrich_parser = subparsers.add_parser("enrich", help="Run enrichment pipeline")
    enrich_parser.add_argument("--brain", "-b", default="./brain", help="Brain path")
    enrich_parser.add_argument(
        "--mode", choices=["full", "quick", "report", "boot", "orphan"],
        default="full", help="Enrichment mode"
    )
    enrich_parser.add_argument("--dry-run", action="store_true", help="Preview changes without applying")
    enrich_parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed progress")
    enrich_parser.add_argument("--rollback", action="store_true", help="Rollback last enrichment")
    enrich_parser.add_argument("--timeout", type=int, help="Timeout in seconds")

    # Maintenance subcommand (v3.3.0)
    maint_parser = subparsers.add_parser("maintenance", help="Brain maintenance tools")
    maint_sub = maint_parser.add_subparsers(dest="maint_command")

    stale_p = maint_sub.add_parser("stale", help="Detect stale entities")
    stale_p.add_argument("--brain", type=str, help="Brain path")
    stale_p.add_argument("--type", type=str, help="Filter by entity type")
    stale_p.add_argument("--threshold", type=int, help="Override staleness threshold (days)")

    orphans_p = maint_sub.add_parser("orphans", help="Clean orphan relationships")
    orphans_p.add_argument("--brain", type=str, help="Brain path")
    orphans_p.add_argument("--dry-run", action="store_true", default=True)
    orphans_p.add_argument("--apply", action="store_true")

    snap_p = maint_sub.add_parser("snapshot", help="Manage snapshots")
    snap_p.add_argument("action", choices=["create", "list", "cleanup"], nargs="?", default="list")
    snap_p.add_argument("--brain", type=str, help="Brain path")

    hints_p = maint_sub.add_parser("hints", help="Show extraction hints")
    hints_p.add_argument("--brain", type=str, help="Brain path")
    hints_p.add_argument("--type", type=str, help="Filter by entity type")
    hints_p.add_argument("--priority", choices=["high", "medium", "low"])

    # Relationships subcommand (v3.3.0)
    rel_parser = subparsers.add_parser("relationships", help="Relationship maintenance")
    rel_sub = rel_parser.add_subparsers(dest="rel_command")

    audit_p = rel_sub.add_parser("audit", help="Audit relationship quality")
    audit_p.add_argument("--brain", type=str, help="Brain path")
    audit_p.add_argument("--fix", action="store_true", help="Auto-fix issues")

    norm_p = rel_sub.add_parser("normalize", help="Normalize relationship targets")
    norm_p.add_argument("--brain", type=str, help="Brain path")
    norm_p.add_argument("--dry-run", action="store_true", default=True)
    norm_p.add_argument("--apply", action="store_true")

    decay_p = rel_sub.add_parser("decay", help="Check relationship staleness")
    decay_p.add_argument("--brain", type=str, help="Brain path")
    decay_p.add_argument("--threshold", type=int, default=90, help="Days threshold")

    args = parser.parse_args()

    if args.command == "search":
        cmd_search(args)
    elif args.command == "list":
        list_entities(args)
    elif args.command == "get":
        get_entity(args)
    elif args.command == "validate":
        validate(args)
    elif args.command == "setup":
        setup(args)
    elif args.command == "events":
        cmd_events(args)
    elif args.command == "index":
        cmd_index(args)
    elif args.command == "query":
        cmd_query(args)
    elif args.command == "mcp":
        cmd_mcp(args)
    elif args.command == "vector":
        cmd_vector(args)
    elif args.command == "resolve":
        cmd_resolve(args)
    elif args.command == "enrich":
        cmd_enrich(args)
    elif args.command == "maintenance":
        _handle_maintenance(args)
    elif args.command == "relationships":
        _handle_relationships(args)
    else:
        parser.print_help()


def cmd_search(args):
    """Search entities."""
    brain_path = Path(args.brain)

    if getattr(args, "semantic", False):
        # Semantic (vector) search
        try:
            from pmos_brain.vector.index import BrainVectorIndex
        except ImportError:
            print("Error: Vector search requires: pip install pmos-brain[vector]", file=sys.stderr)
            sys.exit(1)
        try:
            vi = BrainVectorIndex(brain_path)
            results = vi.query(args.query, n_results=args.limit)
            if results:
                print(f"Found {len(results)} results (semantic):\n")
                for r in results:
                    score = f"{r.get('distance', 0):.3f}" if "distance" in r else "?"
                    print(f"  [{r.get('type', '?')}] {r.get('id', '?')}  (score: {score})")
            else:
                print("No results found.")
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Keyword search
        from pmos_brain.core.search import BrainSearch
        try:
            searcher = BrainSearch(brain_path)
            results = searcher.search(args.query, limit=args.limit)
            if results:
                print(f"Found {len(results)} results:\n")
                for r in results:
                    name = getattr(r, "name", None) or getattr(r, "entity_id", str(r))
                    etype = getattr(r, "entity_type", "?")
                    path = getattr(r, "path", "")
                    print(f"  [{etype}] {name}")
                    if path:
                        print(f"    Path: {path}")
            else:
                print("No results found.")
        except FileNotFoundError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)


# Alias for backward compatibility
search = cmd_search


def list_entities(args):
    """List entities."""
    from pmos_brain import Brain
    try:
        brain = Brain(args.brain)
        entities = brain.list_entities(entity_type=args.type)
        print(f"Found {len(entities)} entities:\n")
        for entity in sorted(entities, key=lambda e: e.name):
            print(f"  [{entity.entity_type}] {entity.name}")
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def get_entity(args):
    """Get entity details."""
    from pmos_brain import Brain
    try:
        brain = Brain(args.brain)
        entity = brain.get(args.path)
        if entity:
            print(f"Name: {entity.name}")
            print(f"Type: {entity.entity_type}")
            print(f"Path: {entity.path}")
            if entity.aliases:
                print(f"Aliases: {', '.join(entity.aliases)}")
            if entity.relationships:
                print(f"Relationships:")
                for rel_type, targets in entity.relationships.items():
                    print(f"  {rel_type}: {targets}")
            print(f"\n{entity.content[:500]}...")
        else:
            print(f"Entity not found: {args.path}")
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def validate(args):
    """Validate brain structure."""
    from pmos_brain import Brain
    try:
        brain = Brain(args.brain)
        stats = brain.stats
        print("Brain validation passed!")
        print(f"  Total entities: {stats['total_entities']}")
        print(f"  Persons: {stats['persons']}")
        print(f"  Projects: {stats['projects']}")
        print(f"  Teams: {stats['teams']}")
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def setup(args):
    """Initialize new brain."""
    path = Path(args.path)

    folders = ["Entities", "Projects", "Architecture", "Strategy", "Decisions", "Inbox", ".schema"]

    print(f"Creating brain at: {path}")
    for folder in folders:
        (path / folder).mkdir(parents=True, exist_ok=True)
        print(f"  Created: {folder}/")

    # Create registry
    (path / "registry.yaml").write_text("entities: {}\nprojects: {}\nteams: {}\n")
    print("  Created: registry.yaml")

    print("\nBrain initialized successfully!")
    print(f"\nNext steps:")
    print(f"  1. Add entities to {path}/Entities/")
    print(f"  2. Run: pmos-brain --brain {path} list")


def cmd_events(args):
    """Handle events subcommands."""
    from datetime import datetime, timedelta, timezone
    from pmos_brain.storage.event_store import EventStore

    if not hasattr(args, "events_command") or not args.events_command:
        print("Usage: pmos-brain events {timeline,recent,stats}", file=sys.stderr)
        sys.exit(1)

    brain_path = Path(args.brain)
    store = EventStore(brain_path)

    if args.events_command == "timeline":
        entity_path = brain_path / args.entity
        if not entity_path.exists() and not args.entity.endswith(".md"):
            entity_path = brain_path / f"{args.entity}.md"
        if not entity_path.exists():
            print(f"Entity not found: {args.entity}", file=sys.stderr)
            sys.exit(1)

        timeline = store.get_entity_timeline(entity_path)
        if not timeline:
            print(f"No events found for {args.entity}")
            return

        print(f"Timeline for {args.entity}")
        print(f"{'=' * 60}")
        for entry in timeline:
            ts = entry["timestamp"][:19]
            etype = entry["event_type"]
            actor = entry["actor"]
            message = entry.get("message", "")
            print(f"\n  {ts}  [{etype}]")
            print(f"  Actor: {actor}")
            if message:
                print(f"  Message: {message}")
        print(f"\n{'=' * 60}")
        print(f"Total: {len(timeline)} events")

    elif args.events_command == "recent":
        since = datetime.now(timezone.utc) - timedelta(days=args.days)
        actors = [args.actor] if args.actor else None
        events = store.query_events(since=since, actors=actors, limit=args.limit)

        if not events:
            print(f"No events in the last {args.days} day(s)")
            return

        print(f"Recent events (last {args.days} day(s))")
        print(f"{'=' * 60}")
        for event in events:
            ts = event.timestamp.strftime("%Y-%m-%d %H:%M")
            print(f"\n  {ts}  [{event.event_type}]  {event.entity_id}")
            print(f"  Actor: {event.actor}")
            if event.message:
                print(f"  Message: {event.message[:80]}")
        print(f"\n{'=' * 60}")
        print(f"Total: {len(events)} events")

    elif args.events_command == "stats":
        since = None
        if args.since:
            since = datetime.fromisoformat(args.since).replace(tzinfo=timezone.utc)

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
            for actor, count in sorted(by_actor.items(), key=lambda x: -x[1]):
                pct = count / total * 100 if total else 0
                print(f"  {actor:30s} {count:5d}  ({pct:.1f}%)")

        print(f"{'=' * 60}")


def cmd_index(args):
    """Generate BRAIN.md compressed index."""
    from pmos_brain.core.index_generator import BrainIndexGenerator

    brain_path = Path(args.brain)
    team_config = None

    if args.config:
        try:
            import yaml
            with open(args.config, encoding="utf-8") as f:
                config_data = yaml.safe_load(f) or {}
            team_config = {
                "user": config_data.get("user", {}),
                "manager": config_data.get("team", {}).get("manager"),
                "reports": config_data.get("team", {}).get("reports", []),
                "stakeholders": config_data.get("team", {}).get("stakeholders", []),
            }
        except Exception as e:
            print(f"Warning: Could not load config: {e}", file=sys.stderr)

    generator = BrainIndexGenerator(brain_path=brain_path, team_config=team_config)
    content = generator.generate()

    output_path = args.output or (brain_path / "BRAIN.md")
    output_path.write_text(content, encoding="utf-8")
    size_kb = len(content.encode("utf-8")) / 1024
    print(f"Generated {output_path} ({size_kb:.1f}KB)")


def cmd_query(args):
    """Combined BRAIN+GRAPH query."""
    from pmos_brain.core.query import BrainQuery
    try:
        bq = BrainQuery(brain_path=Path(args.brain))
        result = bq.query(
            args.query,
            limit=args.limit,
            expand_graph=not args.no_graph,
        )
        if args.format == "json":
            import json
            output = {
                "query": result.query,
                "results": [
                    {"id": r.entity_id, "score": r.score, "type": r.entity_type}
                    for r in result.results
                ],
                "seed_count": result.seed_count,
                "graph_expanded": result.graph_expanded,
                "latency_ms": result.latency_ms,
            }
            print(json.dumps(output, indent=2))
        else:
            print(f"Query: {result.query}")
            print(f"Results: {len(result.results)} (seeds: {result.seed_count}, "
                  f"graph: {'yes' if result.graph_expanded else 'no'}, "
                  f"{result.latency_ms:.0f}ms)\n")
            for r in result.results:
                score = f"{r.score:.3f}" if hasattr(r, "score") else "?"
                print(f"  [{r.entity_type}] {r.entity_id}  (score: {score})")
            for w in result.warnings:
                print(f"\n  Warning: {w}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_mcp(args):
    """Start Brain MCP server."""
    import os
    os.environ.setdefault("BRAIN_PATH", str(Path(args.brain).resolve()))
    try:
        from pmos_brain.mcp.server import mcp as mcp_server
        mcp_server.run()
    except ImportError:
        print("Error: MCP server requires: pip install pmos-brain[mcp]", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_vector(args):
    """Vector search operations."""
    try:
        from pmos_brain.vector.index import BrainVectorIndex
    except ImportError:
        print("Error: Vector search requires: pip install pmos-brain[vector]", file=sys.stderr)
        sys.exit(1)

    brain_path = Path(args.brain)

    if not hasattr(args, "vector_command") or not args.vector_command:
        print("Usage: pmos-brain vector {build,query,stats}", file=sys.stderr)
        sys.exit(1)

    if args.vector_command == "build":
        vi = BrainVectorIndex(brain_path)
        vi.build()
        print("Vector index built successfully.")
    elif args.vector_command == "query":
        vi = BrainVectorIndex(brain_path)
        results = vi.query(args.query, n_results=args.limit)
        if results:
            print(f"Found {len(results)} results:\n")
            for r in results:
                score = f"{r.get('distance', 0):.3f}" if "distance" in r else "?"
                print(f"  [{r.get('type', '?')}] {r.get('id', '?')}  (score: {score})")
        else:
            print("No results found.")
    elif args.vector_command == "stats":
        vi = BrainVectorIndex(brain_path)
        stats = vi.stats()
        print(f"Vector Index Statistics:")
        for k, v in stats.items():
            print(f"  {k}: {v}")


def cmd_resolve(args):
    """Resolve entity reference to canonical path."""
    from pmos_brain.resolver.canonical import CanonicalResolver
    try:
        resolver = CanonicalResolver(brain_path=Path(args.brain))
        result = resolver.resolve(args.reference)
        if result:
            print(f"Resolved: {args.reference}")
            print(f"  Path: {result}")
        else:
            print(f"Could not resolve: {args.reference}")
            # Show similar
            similar = resolver.find_similar(args.reference, limit=5)
            if similar:
                print(f"\n  Did you mean:")
                for s in similar:
                    print(f"    - {s}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_enrich(args):
    """Run enrichment pipeline."""
    from pmos_brain.enrichers.orchestrator import BrainEnrichmentOrchestrator
    try:
        verbose = getattr(args, "verbose", False)
        dry_run = getattr(args, "dry_run", False)
        orchestrator = BrainEnrichmentOrchestrator(
            brain_path=Path(args.brain),
            verbose=verbose,
        )
        result = orchestrator.run(mode=args.mode, dry_run=dry_run)
        print(f"Enrichment complete ({args.mode} mode)")
        if dry_run:
            print("  (dry run — no changes applied)")
        print(f"  Entities: {result.baseline_entities}")
        print(f"  Soft edges added: {result.soft_edges_added}")
        print(f"  Density: {result.baseline_density:.3f} → {result.final_density:.3f}")
        if result.orphans_reduced:
            print(f"  Orphans reduced: {result.orphans_reduced}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def _handle_maintenance(args):
    """Handle maintenance subcommands."""
    from pathlib import Path
    brain_path = Path(getattr(args, 'brain', None) or './brain')

    if args.maint_command == "stale":
        from pmos_brain.maintenance.stale_detector import StaleEntityDetector
        detector = StaleEntityDetector(brain_path)
        stale = detector.detect_stale(
            threshold_days=getattr(args, 'threshold', None),
            entity_type=getattr(args, 'type', None),
        )
        print(f"Found {len(stale)} stale entities")
        for entity in stale[:20]:
            print(f"  {entity.entity_id} ({entity.entity_type}) - {entity.days_stale}d stale")
            print(f"    Reasons: {', '.join(entity.staleness_reasons)}")

    elif args.maint_command == "orphans":
        from pmos_brain.maintenance.orphan_cleaner import OrphanCleaner
        cleaner = OrphanCleaner(brain_path)
        orphans = cleaner.analyze_orphans()
        print(cleaner.generate_report(orphans))

    elif args.maint_command == "snapshot":
        from pmos_brain.maintenance.snapshot_manager import SnapshotManager
        manager = SnapshotManager(brain_path)
        action = getattr(args, 'action', 'list')
        if action == "create":
            path = manager.create_snapshot()
            print(f"Created snapshot: {path}")
        elif action == "list":
            for s in manager.list_snapshots():
                print(f"  {s['timestamp']} - {s['size_bytes']/1024:.1f}KB")
        elif action == "cleanup":
            removed = manager.cleanup_old_snapshots(dry_run=True)
            print(f"Would remove {len(removed)} old snapshots")

    elif args.maint_command == "hints":
        from pmos_brain.maintenance.extraction_hints import ExtractionHintsGenerator
        gen = ExtractionHintsGenerator(brain_path)
        report = gen.generate_hints(
            entity_type=getattr(args, 'type', None),
            priority_filter=getattr(args, 'priority', None),
        )
        print(f"Entities with gaps: {report.entities_with_gaps}/{report.total_entities}")
        print(f"High priority hints: {report.high_priority_hints}")
        for hint in report.hints[:20]:
            print(f"  [{hint.priority}] {hint.entity_id}: missing {hint.field}")

    else:
        print("Usage: pmos-brain maintenance {stale,orphans,snapshot,hints}", file=sys.stderr)
        sys.exit(1)


def _handle_relationships(args):
    """Handle relationship subcommands."""
    from pathlib import Path
    brain_path = Path(getattr(args, 'brain', None) or './brain')

    if args.rel_command == "audit":
        from pmos_brain.relationships.auditor import RelationshipAuditor
        auditor = RelationshipAuditor(brain_path)
        result = auditor.audit()
        print(f"Entities: {result.total_entities}, Relationships: {result.total_relationships}")
        print(f"Issues: {result.total_issues}")
        if result.orphan_targets:
            print(f"  Orphan targets: {len(result.orphan_targets)}")
        if result.missing_inverses:
            print(f"  Missing inverses: {len(result.missing_inverses)}")
        if result.duplicate_relationships:
            print(f"  Duplicates: {len(result.duplicate_relationships)}")

    elif args.rel_command == "normalize":
        from pmos_brain.relationships.normalizer import RelationshipNormalizer
        normalizer = RelationshipNormalizer(brain_path)
        dry_run = not getattr(args, 'apply', False)
        result = normalizer.normalize_all(dry_run=dry_run)
        print(normalizer.get_normalization_report(result))

    elif args.rel_command == "decay":
        from pmos_brain.relationships.decay import RelationshipDecayMonitor
        monitor = RelationshipDecayMonitor(brain_path)
        report = monitor.scan_relationships(threshold_days=args.threshold)
        print(f"Stale relationships: {report.stale_relationships}/{report.total_relationships}")
        for stale in report.stale_list[:10]:
            print(f"  {stale.entity_id} -> {stale.target}: {stale.days_stale}d stale")

    else:
        print("Usage: pmos-brain relationships {audit,normalize,decay}", file=sys.stderr)
        sys.exit(1)


# CLI entry points for pyproject.toml scripts
def events():
    """Entry point for brain-events command."""
    # Rewrite sys.argv to route through main
    sys.argv = ["pmos-brain", "events"] + sys.argv[1:]
    main()


def index():
    """Entry point for brain-index command."""
    sys.argv = ["pmos-brain", "index"] + sys.argv[1:]
    main()


def mcp():
    """Entry point for brain-mcp command."""
    sys.argv = ["pmos-brain", "mcp"] + sys.argv[1:]
    main()


def vector():
    """Entry point for brain-vector command."""
    sys.argv = ["pmos-brain", "vector"] + sys.argv[1:]
    main()


def query():
    """Entry point for brain-query command."""
    sys.argv = ["pmos-brain", "query"] + sys.argv[1:]
    main()


def resolve():
    """Entry point for brain-resolve command."""
    sys.argv = ["pmos-brain", "resolve"] + sys.argv[1:]
    main()


def enrich():
    """Entry point for brain-enrich command."""
    sys.argv = ["pmos-brain", "enrich"] + sys.argv[1:]
    main()


def graph():
    """Placeholder for brain-graph command."""
    print("Graph commands not yet implemented in CLI.", file=sys.stderr)
    sys.exit(1)


def quality():
    """Placeholder for brain-quality command."""
    print("Quality commands not yet implemented in CLI.", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
