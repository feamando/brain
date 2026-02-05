#!/usr/bin/env python3
"""
Brain Setup Script

Initializes a new Brain instance with the proper folder structure,
validates configuration, and runs initial health checks.

Usage:
    python setup.py                    # Interactive setup
    python setup.py --path ./my-brain  # Specify brain path
    python setup.py --check            # Just validate existing setup
"""

import os
import sys
import argparse
import json
from pathlib import Path
from datetime import datetime

# Folders to create
BRAIN_FOLDERS = [
    "Entities",
    "Projects", 
    "Architecture",
    "Strategy",
    "Decisions",
    "Inbox",
    "Inbox/Slack",
    "Inbox/Jira",
    "Inbox/GitHub",
    ".schema",
    ".snapshots",
]

# Files to create
BRAIN_FILES = {
    "registry.yaml": """# Brain Entity Registry
# Auto-generated - do not edit manually

entities: {}
projects: {}
teams: {}

metadata:
  created: {timestamp}
  version: "1.0"
""",
    "Entities/.gitkeep": "",
    "Projects/.gitkeep": "",
    "Architecture/.gitkeep": "",
    "Strategy/.gitkeep": "",
    "Decisions/.gitkeep": "",
    "Inbox/.gitkeep": "",
}


def create_folder_structure(brain_path: Path) -> None:
    """Create the Brain folder structure."""
    print(f"\nCreating Brain at: {brain_path}")
    
    for folder in BRAIN_FOLDERS:
        folder_path = brain_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"  Created: {folder}/")


def create_initial_files(brain_path: Path) -> None:
    """Create initial Brain files."""
    print("\nCreating initial files...")
    
    timestamp = datetime.now().isoformat()
    
    for filename, content in BRAIN_FILES.items():
        file_path = brain_path / filename
        if not file_path.exists():
            content = content.format(timestamp=timestamp)
            file_path.write_text(content)
            print(f"  Created: {filename}")
        else:
            print(f"  Exists:  {filename}")


def copy_schemas(brain_path: Path, repo_path: Path) -> None:
    """Copy schema files to Brain."""
    schema_src = repo_path / ".schema"
    schema_dst = brain_path / ".schema"
    
    if schema_src.exists():
        print("\nCopying schemas...")
        for schema_file in schema_src.glob("*.json"):
            dst_file = schema_dst / schema_file.name
            dst_file.write_text(schema_file.read_text())
            print(f"  Copied: {schema_file.name}")


def validate_setup(brain_path: Path) -> bool:
    """Validate the Brain setup."""
    print("\nValidating setup...")
    
    errors = []
    
    # Check folders
    for folder in BRAIN_FOLDERS:
        if not (brain_path / folder).exists():
            errors.append(f"Missing folder: {folder}")
    
    # Check registry
    if not (brain_path / "registry.yaml").exists():
        errors.append("Missing registry.yaml")
    
    # Check schemas
    schema_path = brain_path / ".schema"
    if not schema_path.exists() or not list(schema_path.glob("*.json")):
        errors.append("Missing schema files in .schema/")
    
    if errors:
        print("\n  Errors found:")
        for error in errors:
            print(f"    - {error}")
        return False
    
    print("  All checks passed!")
    return True


def main():
    parser = argparse.ArgumentParser(description="Initialize PM-OS Brain")
    parser.add_argument("--path", type=Path, default=Path("./brain"),
                       help="Path to create Brain (default: ./brain)")
    parser.add_argument("--check", action="store_true",
                       help="Only validate existing setup")
    args = parser.parse_args()
    
    brain_path = args.path.resolve()
    repo_path = Path(__file__).parent
    
    if args.check:
        if validate_setup(brain_path):
            print("\nBrain setup is valid!")
            sys.exit(0)
        else:
            print("\nBrain setup has issues.")
            sys.exit(1)
    
    print("=" * 60)
    print("PM-OS Brain Setup")
    print("=" * 60)
    
    create_folder_structure(brain_path)
    create_initial_files(brain_path)
    copy_schemas(brain_path, repo_path)
    
    if validate_setup(brain_path):
        print("\n" + "=" * 60)
        print("Setup complete!")
        print("=" * 60)
        print(f"\nYour Brain is ready at: {brain_path}")
        print("\nNext steps:")
        print("  1. Copy examples/config/config.yaml to your user directory")
        print("  2. Copy examples/config/.env.example to .env and fill in values")
        print("  3. Create your first entity in Entities/")
        print("  4. Run: python tools/brain_loader.py --list-all")
    else:
        print("\nSetup completed with warnings.")
        sys.exit(1)


if __name__ == "__main__":
    main()
