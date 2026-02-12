#!/usr/bin/env python3
"""
PM-OS Brain Index Generator

Generates a compressed BRAIN.md index for agent context.
Two-source architecture: config for "who matters", entity files for relationship data.

Output: pipe-delimited compressed index (~8KB) with:
  - Tier 1: Team members (manager, reports, stakeholders) with full relationships
  - Tier 2: Connected entities (one-hop from Tier 1) + hot topics, compact format

Usage (library):
    from pmos_brain.core.index_generator import BrainIndexGenerator
    gen = BrainIndexGenerator(brain_path=Path("~/brain"), team_config={...})
    content = gen.generate()

Usage (CLI):
    python -m pmos_brain.core.index_generator --brain-path PATH
    python -m pmos_brain.core.index_generator --brain-path PATH --output BRAIN.md
    python -m pmos_brain.core.index_generator --brain-path PATH --config team.yaml
"""

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

import yaml


class BrainIndexGenerator:
    """Generates compressed BRAIN.md index from config + entity files.

    Args:
        brain_path: Path to the brain directory containing registry.yaml and entity files.
        team_config: Optional dict describing team structure. Expected shape::

            {
                "user": {"name": "Jane Smith", "position": "Director"},
                "manager": {"id": "john-doe", "name": "John Doe", "role": "VP"},
                "reports": [
                    {"id": "alice-b", "name": "Alice B", "role": "PM", "squad": "Alpha"},
                ],
                "stakeholders": [
                    {"id": "bob-c", "name": "Bob C", "role": "CTO"},
                ],
            }
    """

    MAX_TIER2 = 120

    def __init__(self, brain_path: Path, team_config: Optional[Dict] = None):
        self.brain_path = Path(brain_path)
        self.team_config = team_config or {}
        self.registry: Dict[str, Any] = {}
        self._hot_topics: List[str] = []
        self._load_registry()

    def _load_registry(self):
        """Load registry for ID-to-file mapping."""
        registry_file = self.brain_path / "registry.yaml"
        if registry_file.exists():
            with open(registry_file, encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
            self.registry = data.get("entities", {})

    def _resolve_entity_path(self, entity_id: str) -> Optional[Path]:
        """Resolve entity ID to file path via registry."""
        slug = entity_id
        if "/" in entity_id:
            parts = entity_id.split("/")
            slug = parts[-1]

        entry = self.registry.get(slug)
        if entry and "$ref" in entry:
            return self.brain_path / entry["$ref"]

        for key, entry in self.registry.items():
            if key == slug or key.endswith(slug):
                if "$ref" in entry:
                    return self.brain_path / entry["$ref"]

        return None

    def _parse_frontmatter(self, filepath: Path) -> Dict[str, Any]:
        """Parse YAML frontmatter from entity file."""
        if not filepath.exists():
            return {}
        try:
            content = filepath.read_text(encoding="utf-8")
            if not content.startswith("---"):
                return {}
            parts = content.split("---", 2)
            if len(parts) < 3:
                return {}
            return yaml.safe_load(parts[1]) or {}
        except Exception:
            return {}

    def _load_tier1_entities(self) -> List[Dict[str, Any]]:
        """Load Tier 1 entities: manager + direct reports + stakeholders + self.

        Merges config data (role, squad) with entity file data (relationships).
        """
        members: List[Dict[str, Any]] = []

        # Self
        user_cfg = self.team_config.get("user", {})
        user_name = user_cfg.get("name", "")
        user_id = user_name.lower().replace(" ", "-").replace("_", "-")
        if user_id:
            members.append({
                "id": user_id,
                "name": user_name,
                "role": user_cfg.get("position", ""),
                "squad": "",
                "source": "self",
            })

        # Manager
        mgr = self.team_config.get("manager")
        if mgr:
            members.append({
                "id": mgr.get("id", ""),
                "name": mgr.get("name", ""),
                "role": mgr.get("role", ""),
                "squad": "",
                "source": "manager",
            })

        # Direct reports
        for report in self.team_config.get("reports", []):
            members.append({
                "id": report.get("id", ""),
                "name": report.get("name", ""),
                "role": report.get("role", ""),
                "squad": report.get("squad", ""),
                "source": "report",
            })

        # Stakeholders
        for sh in self.team_config.get("stakeholders", []):
            members.append({
                "id": sh.get("id", ""),
                "name": sh.get("name", ""),
                "role": sh.get("role", ""),
                "squad": "",
                "source": "stakeholder",
            })

        # For each member, load entity file for relationships
        tier1: List[Dict[str, Any]] = []
        seen_ids: Set[str] = set()
        for member in members:
            mid = member["id"]
            if not mid or mid in seen_ids:
                continue
            seen_ids.add(mid)

            entity_path = self._resolve_entity_path(mid)
            relationships: List[str] = []
            entity_type = "person"

            if entity_path:
                fm = self._parse_frontmatter(entity_path)
                entity_type = fm.get("$type", "person")
                raw_rels = fm.get("$relationships", [])
                skip_types = {"mentioned_in", "similar_to"}
                structural_types = {"reports_to", "manages", "member_of", "leads", "owns"}
                structural_rels: List[str] = []
                other_rels: List[str] = []
                for rel in raw_rels:
                    rel_type = rel.get("type", "related_to")
                    if rel_type in skip_types:
                        continue
                    target = rel.get("target", "")
                    if "/" in target:
                        target = target.split("/")[-1]
                    if target.startswith("exp-"):
                        continue
                    confidence = rel.get("confidence", 1.0)
                    if confidence < 0.5:
                        continue
                    if target:
                        pair = f"{rel_type}:{target}"
                        if rel_type in structural_types:
                            structural_rels.append(pair)
                        else:
                            other_rels.append(pair)
                relationships = (structural_rels + other_rels)[:12]

            tier1.append({
                "id": mid,
                "name": member["name"],
                "type": entity_type,
                "role": member["role"] or "",
                "squad": member["squad"] or "",
                "status": "active",
                "relationships": relationships,
                "source": member["source"],
            })

        return tier1

    def _load_tier2_entities(self, tier1: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Load Tier 2: one-hop relationship targets from Tier 1 + hot topics."""
        tier1_ids = {e["id"] for e in tier1}
        tier2_ids: Set[str] = set()
        tier2: List[Dict[str, Any]] = []

        for entity in tier1:
            for rel in entity.get("relationships", []):
                if ":" in rel:
                    target = rel.split(":", 1)[1]
                    if target and target not in tier1_ids and target not in tier2_ids:
                        tier2_ids.add(target)

        for ht_id in self._hot_topics:
            if ht_id not in tier1_ids and ht_id not in tier2_ids:
                tier2_ids.add(ht_id)

        for entity_id in sorted(tier2_ids):
            if len(tier2) >= self.MAX_TIER2:
                break

            entry = self.registry.get(entity_id, {})
            if not entry:
                continue

            entity_type = entry.get("$type", "unknown")
            status = entry.get("$status", "active")
            name = entity_id.replace("-", " ").replace("_", " ").title()

            ref = entry.get("$ref", "")
            if ref:
                entity_path = self.brain_path / ref
                if entity_path.exists():
                    fm = self._parse_frontmatter(entity_path)
                    name = fm.get("name", name)
                    entity_type = fm.get("$type", entity_type)
                    status = fm.get("$status", status)

            tier2.append({
                "id": entity_id,
                "type": entity_type,
                "name": name,
                "status": status,
            })

        return tier2

    def set_hot_topics(self, hot_topics: List[str]) -> None:
        """Set hot topic entity IDs to include in Tier 2."""
        self._hot_topics = list(hot_topics)

    def _format_index(self, tier1: List[Dict], tier2: List[Dict]) -> str:
        """Format the compressed index as pipe-delimited markdown."""
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        total = len(tier1) + len(tier2)

        lines = [
            "# BRAIN.md — Entity Index",
            f"<!-- Generated: {now} | Entities: {total} | Tier1: {len(tier1)} | Tier2: {len(tier2)} -->",
            "",
            "## Team (Tier 1)",
            "id|type|role|squad|status|relationships",
        ]

        for e in tier1:
            rels = ",".join(e.get("relationships", []))
            line = f"{e['id']}|{e['type']}|{e.get('role', '')}|{e.get('squad', '')}|{e['status']}|{rels}"
            lines.append(line)

        lines.append("")
        lines.append("## Connected Entities (Tier 2)")
        lines.append("id|type|name|status")

        for e in tier2:
            line = f"{e['id']}|{e['type']}|{e['name']}|{e['status']}"
            lines.append(line)

        lines.append("")
        return "\n".join(lines)

    def generate(self) -> str:
        """Generate the complete BRAIN.md index."""
        tier1 = self._load_tier1_entities()
        tier2 = self._load_tier2_entities(tier1)
        return self._format_index(tier1, tier2)


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Generate BRAIN.md compressed index")
    parser.add_argument("--brain-path", type=Path, required=True, help="Path to brain directory")
    parser.add_argument("--output", type=Path, help="Output file path")
    parser.add_argument("--config", type=Path, help="Path to team config YAML file")
    parser.add_argument("--hot-topics", nargs="*", help="Entity IDs to include as hot topics")
    args = parser.parse_args()

    team_config: Optional[Dict] = None
    if args.config:
        with open(args.config, encoding="utf-8") as f:
            team_config = yaml.safe_load(f) or {}

    generator = BrainIndexGenerator(brain_path=args.brain_path, team_config=team_config)

    if args.hot_topics:
        generator.set_hot_topics(args.hot_topics)

    content = generator.generate()

    output_path = args.output or (generator.brain_path / "BRAIN.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    size_kb = len(content.encode("utf-8")) / 1024
    print(f"Generated {output_path} ({size_kb:.1f}KB)")


if __name__ == "__main__":
    main()
