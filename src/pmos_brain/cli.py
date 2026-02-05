#!/usr/bin/env python3
"""
PM-OS Brain CLI

Commands:
    pmos-brain search <query>     Search entities
    pmos-brain list [--type TYPE] List entities
    pmos-brain get <path>         Get entity details
    pmos-brain validate           Validate brain structure
    pmos-brain setup <path>       Initialize new brain
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
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")
    
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Search command
    search_parser = subparsers.add_parser("search", help="Search entities")
    search_parser.add_argument("query", help="Search query")
    search_parser.add_argument("--type", "-t", help="Entity type filter")
    search_parser.add_argument("--limit", "-n", type=int, default=10, help="Max results")
    search_parser.add_argument("--brain", "-b", default="./brain", help="Brain path")
    
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
    
    args = parser.parse_args()
    
    if args.command == "search":
        search(args)
    elif args.command == "list":
        list_entities(args)
    elif args.command == "get":
        get_entity(args)
    elif args.command == "validate":
        validate(args)
    elif args.command == "setup":
        setup(args)
    else:
        parser.print_help()


def search(args):
    """Search entities."""
    from pmos_brain import Brain
    try:
        brain = Brain(args.brain)
        results = brain.search(args.query, entity_type=args.type, limit=args.limit)
        if results:
            print(f"Found {len(results)} results:\n")
            for entity in results:
                print(f"  [{entity.entity_type}] {entity.name}")
                print(f"    Path: {entity.path}")
        else:
            print("No results found.")
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


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


if __name__ == "__main__":
    main()
