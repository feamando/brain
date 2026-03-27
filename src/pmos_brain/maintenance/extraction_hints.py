"""
Brain Extraction Hints Generator

Generates actionable hints about missing entity fields and which MCP
sources can provide them.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml

# Field-to-MCP-source mapping
# Maps entity types to their fields and potential data sources
FIELD_SOURCES: Dict[str, Dict[str, List[str]]] = {
    "person": {
        "email": ["hr_system", "slack:user_lookup", "gdocs:directory"],
        "slack_handle": ["slack:user_lookup", "hr_system"],
        "manager": ["hr_system", "gdocs:org_chart", "confluence:team_pages"],
        "team": ["hr_system", "jira:project_membership", "confluence:team_pages"],
        "expertise": ["jira:assigned_issues", "github:prs", "confluence:authored_docs"],
        "role": ["hr_system", "gdocs:org_chart", "confluence:team_pages"],
        "$relationships": [
            "jira:project_membership",
            "github:pr_reviewers",
            "slack:channel_members",
        ],
    },
    "team": {
        "owner": ["hr_system", "confluence:team_pages", "jira:project_lead"],
        "members": ["hr_system", "slack:channel_members", "jira:project_membership"],
        "mission": ["confluence:team_pages", "gdocs:team_charter"],
        "description": ["confluence:team_pages", "gdocs:team_charter"],
        "$relationships": ["jira:related_projects", "confluence:team_pages"],
    },
    "squad": {
        "owner": ["hr_system", "confluence:squad_pages", "jira:project_lead"],
        "members": ["hr_system", "slack:channel_members", "jira:board_members"],
        "tribe": ["confluence:org_structure", "hr_system"],
        "mission": ["confluence:squad_pages", "gdocs:squad_charter"],
        "tech_stack": ["github:repo_languages", "confluence:architecture_docs"],
        "$relationships": ["jira:related_projects", "github:repo_dependencies"],
    },
    "project": {
        "owner": ["jira:project_lead", "confluence:project_page", "gdocs:prds"],
        "team": ["jira:project_membership", "confluence:project_page"],
        "status": ["jira:project_status", "confluence:project_page"],
        "start_date": ["jira:project_created", "confluence:project_page"],
        "target_date": ["jira:versions", "confluence:roadmap"],
        "description": [
            "confluence:project_page",
            "gdocs:prds",
            "jira:project_description",
        ],
        "$relationships": ["jira:linked_projects", "confluence:related_pages"],
    },
    "domain": {
        "owner": ["confluence:domain_pages", "gdocs:architecture_docs"],
        "description": ["confluence:domain_pages", "gdocs:architecture_docs"],
        "systems": ["confluence:architecture_docs", "github:repo_topics"],
        "$relationships": ["confluence:domain_pages", "github:repo_dependencies"],
    },
    "experiment": {
        "owner": ["jira:issue_assignee", "confluence:experiment_docs"],
        "hypothesis": ["confluence:experiment_docs", "gdocs:experiment_plans"],
        "status": ["jira:issue_status", "statsig:experiment_status"],
        "start_date": ["jira:issue_created", "statsig:experiment_start"],
        "end_date": ["statsig:experiment_end", "jira:resolution_date"],
        "results": ["statsig:experiment_results", "confluence:experiment_results"],
        "$relationships": ["jira:linked_issues", "confluence:related_experiments"],
    },
    "system": {
        "owner": ["github:repo_owner", "confluence:system_docs"],
        "description": ["github:repo_readme", "confluence:system_docs"],
        "tech_stack": ["github:repo_languages", "confluence:architecture_docs"],
        "dependencies": [
            "github:package_json",
            "github:requirements_txt",
            "confluence:architecture_docs",
        ],
        "$relationships": [
            "github:repo_dependencies",
            "confluence:system_integrations",
        ],
    },
    "brand": {
        "owner": ["confluence:brand_pages", "gdocs:brand_strategy"],
        "description": ["confluence:brand_pages", "gdocs:brand_strategy"],
        "market": ["confluence:brand_pages", "gdocs:market_analysis"],
        "status": ["confluence:brand_pages", "jira:brand_project_status"],
        "$relationships": ["confluence:brand_pages", "jira:brand_projects"],
    },
}

# Priority levels for fields
FIELD_PRIORITY: Dict[str, Dict[str, str]] = {
    "person": {
        "email": "medium",
        "slack_handle": "low",
        "manager": "high",
        "team": "high",
        "expertise": "medium",
        "role": "high",
        "$relationships": "high",
    },
    "team": {
        "owner": "high",
        "members": "high",
        "mission": "medium",
        "description": "medium",
        "$relationships": "high",
    },
    "squad": {
        "owner": "high",
        "members": "high",
        "tribe": "high",
        "mission": "medium",
        "tech_stack": "medium",
        "$relationships": "high",
    },
    "project": {
        "owner": "high",
        "team": "high",
        "status": "high",
        "start_date": "medium",
        "target_date": "medium",
        "description": "medium",
        "$relationships": "medium",
    },
    "domain": {
        "owner": "high",
        "description": "medium",
        "systems": "medium",
        "$relationships": "medium",
    },
    "experiment": {
        "owner": "high",
        "hypothesis": "high",
        "status": "high",
        "start_date": "medium",
        "end_date": "medium",
        "results": "high",
        "$relationships": "low",
    },
    "system": {
        "owner": "high",
        "description": "medium",
        "tech_stack": "medium",
        "dependencies": "high",
        "$relationships": "high",
    },
    "brand": {
        "owner": "high",
        "description": "medium",
        "market": "medium",
        "status": "medium",
        "$relationships": "medium",
    },
}


@dataclass
class ExtractionHint:
    """A hint for extracting missing data."""

    entity_id: str
    entity_type: str
    field: str
    priority: str
    sources: List[str]
    current_value: Optional[Any] = None


@dataclass
class ExtractionHintsReport:
    """Report of extraction hints for entities."""

    total_entities: int
    entities_with_gaps: int
    total_hints: int
    high_priority_hints: int
    hints_by_source: Dict[str, int] = field(default_factory=dict)
    hints_by_field: Dict[str, int] = field(default_factory=dict)
    hints: List[ExtractionHint] = field(default_factory=list)


class ExtractionHintsGenerator:
    """
    Generates actionable extraction hints for missing Brain entity fields.

    Based on TKS constructive retrieval principle: track expected fields
    and guide enrichment pipeline to fill specific gaps.
    """

    def __init__(self, brain_path: Path):
        """Initialize the hints generator."""
        self.brain_path = brain_path

    def generate_hints(
        self,
        entity_type: Optional[str] = None,
        priority_filter: Optional[str] = None,
        entity_id: Optional[str] = None,
    ) -> ExtractionHintsReport:
        """
        Generate extraction hints for entities.

        Args:
            entity_type: Filter by entity type
            priority_filter: Filter by priority (high, medium, low)
            entity_id: Filter by specific entity ID

        Returns:
            ExtractionHintsReport with all hints
        """
        hints: List[ExtractionHint] = []
        total_entities = 0
        entities_with_gaps = 0
        hints_by_source: Dict[str, int] = {}
        hints_by_field: Dict[str, int] = {}

        # Scan entities
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

                eid = frontmatter.get(
                    "$id", str(entity_path.relative_to(self.brain_path))
                )
                etype = frontmatter.get("$type", "unknown")

                # Apply filters
                if entity_type and etype != entity_type:
                    continue
                if entity_id and eid != entity_id:
                    continue

                total_entities += 1

                # Get field sources for this entity type
                field_sources = FIELD_SOURCES.get(etype, {})
                field_priorities = FIELD_PRIORITY.get(etype, {})

                entity_hints = []
                for field_name, sources in field_sources.items():
                    # Check if field is missing or empty
                    value = frontmatter.get(field_name)
                    is_missing = value is None or (
                        isinstance(value, (list, dict, str)) and not value
                    )

                    if is_missing:
                        priority = field_priorities.get(field_name, "medium")

                        # Apply priority filter
                        if priority_filter and priority != priority_filter:
                            continue

                        hint = ExtractionHint(
                            entity_id=eid,
                            entity_type=etype,
                            field=field_name,
                            priority=priority,
                            sources=sources,
                            current_value=value,
                        )
                        entity_hints.append(hint)

                        # Track by source
                        for source in sources:
                            source_key = source.split(":")[
                                0
                            ]  # e.g., "jira" from "jira:project_lead"
                            hints_by_source[source_key] = (
                                hints_by_source.get(source_key, 0) + 1
                            )

                        # Track by field
                        hints_by_field[field_name] = (
                            hints_by_field.get(field_name, 0) + 1
                        )

                if entity_hints:
                    entities_with_gaps += 1
                    hints.extend(entity_hints)

            except Exception:
                continue

        # Sort hints by priority
        priority_order = {"high": 0, "medium": 1, "low": 2}
        hints.sort(
            key=lambda h: (priority_order.get(h.priority, 1), h.entity_type, h.field)
        )

        high_priority = sum(1 for h in hints if h.priority == "high")

        return ExtractionHintsReport(
            total_entities=total_entities,
            entities_with_gaps=entities_with_gaps,
            total_hints=len(hints),
            high_priority_hints=high_priority,
            hints_by_source=hints_by_source,
            hints_by_field=hints_by_field,
            hints=hints,
        )

    def get_hints_for_enricher(
        self,
        source: str,
        limit: int = 50,
    ) -> List[ExtractionHint]:
        """
        Get hints filtered by MCP source.

        Useful for guiding a specific enricher (e.g., JiraEnricher) to
        fill gaps it can address.

        Args:
            source: MCP source name (jira, slack, github, etc.)
            limit: Max hints to return

        Returns:
            List of hints that can be addressed by this source
        """
        report = self.generate_hints()
        relevant_hints = []

        for hint in report.hints:
            for hint_source in hint.sources:
                if source in hint_source.lower():
                    relevant_hints.append(hint)
                    break

            if len(relevant_hints) >= limit:
                break

        return relevant_hints

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
