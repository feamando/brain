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
    parser.add_argument("--version", action="version", version="%(prog)s 3.1.0")

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
        orchestrator = BrainEnrichmentOrchestrator(brain_path=Path(args.brain))
        result = orchestrator.run(mode=args.mode)
        print(f"Enrichment complete ({args.mode} mode)")
        if hasattr(result, "summary"):
            print(f"  {result.summary}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
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
