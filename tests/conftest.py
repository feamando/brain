#!/usr/bin/env python3
"""
Shared pytest fixtures for brain enrichment tests.

Provides:
- test_brain_dir: temp directory with 50+ entities across 5 types
- Helper to create entity markdown files with valid YAML frontmatter
"""

import shutil
import tempfile
from pathlib import Path

import pytest
import yaml


def _create_entity(
    brain_dir: Path,
    subdir: str,
    filename: str,
    frontmatter: dict,
    body: str,
) -> Path:
    """Create a mock entity markdown file with YAML frontmatter."""
    entity_dir = brain_dir / subdir
    entity_dir.mkdir(parents=True, exist_ok=True)
    fm_yaml = yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)
    content = f"---\n{fm_yaml}---\n{body}"
    path = entity_dir / f"{filename}.md"
    path.write_text(content, encoding="utf-8")
    return path


@pytest.fixture
def test_brain_dir(tmp_path):
    """Create a temp brain directory with 50+ entities across 5+ types.

    Entity distribution:
    - 15 persons
    - 10 projects
    - 8 teams
    - 7 systems
    - 5 experiments
    - 5 squads
    Total: 50 entities
    """
    brain = tmp_path / "brain"
    brain.mkdir()

    # --- 15 Persons ---
    for i in range(1, 16):
        name = f"person_{i:02d}"
        rels = []
        tags = ["engineering"]

        if i <= 5:
            rels.append({
                "type": "member_of",
                "target": "entity/team/team-alpha",
                "source": "manual",
                "confidence": 0.95,
            })
            tags.append("team-alpha")
        elif i <= 10:
            rels.append({
                "type": "member_of",
                "target": "entity/team/team-beta",
                "source": "manual",
                "confidence": 0.90,
            })
            tags.append("team-beta")

        if i == 1:
            rels.append({
                "type": "similar_to",
                "target": "entity/person/person-02",
                "confidence": 0.82,
                "source": "auto_embedding",
                "last_verified": "2026-01-15",
                "metadata": {"model": "all-MiniLM-L6-v2", "threshold": 0.80},
            })
        if i == 2:
            rels.append({
                "type": "similar_to",
                "target": "entity/person/person-01",
                "confidence": 0.82,
                "source": "auto_embedding",
                "last_verified": "2026-01-15",
                "metadata": {"model": "all-MiniLM-L6-v2", "threshold": 0.80},
            })

        if i == 3:
            rels.append({
                "type": "manages",
                "target": "entity/project/project-alpha",
                "source": "manual",
                "confidence": 0.95,
            })

        _create_entity(brain, "Entities/Persons", name, {
            "$id": f"entity/person/person-{i:02d}",
            "$type": "person",
            "$status": "active",
            "$confidence": 0.85,
            "$tags": tags,
            "$relationships": rels,
        }, f"# Person {i:02d}\n\nSoftware engineer working on platform services. "
           f"Specializes in backend development and API design. "
           f"Contributor to multiple internal projects.\n")

    # --- 10 Projects ---
    project_names = [
        ("project_alpha", "Checkout Redesign", ["checkout", "frontend"]),
        ("project_beta", "API Gateway Migration", ["api", "infrastructure"]),
        ("project_gamma", "Search Optimization", ["search", "performance"]),
        ("project_delta", "Mobile App Refresh", ["mobile", "ux"]),
        ("project_epsilon", "Data Pipeline Overhaul", ["data", "etl"]),
        ("project_zeta", "Auth System Upgrade", ["auth", "security"]),
        ("project_eta", "Notification Engine", ["notifications", "messaging"]),
        ("project_theta", "Analytics Dashboard", ["analytics", "reporting"]),
        ("project_iota", "CI/CD Improvement", ["devops", "automation"]),
        ("project_kappa", "Documentation Portal", ["docs", "developer-experience"]),
    ]

    for idx, (slug, title, tags) in enumerate(project_names, 1):
        rels = []
        if idx <= 6:
            rels.append({
                "type": "owned_by",
                "target": f"entity/team/team-{'alpha' if idx <= 3 else 'beta'}",
                "source": "manual",
                "confidence": 0.95,
            })
        if idx == 3:
            rels.append({
                "type": "similar_to",
                "target": "entity/project/project-delta",
                "confidence": 0.88,
                "source": "auto_embedding",
                "last_verified": "2026-01-20",
                "metadata": {"model": "all-MiniLM-L6-v2", "threshold": 0.85},
            })

        _create_entity(brain, "Projects", slug, {
            "$id": f"entity/project/{slug.replace('_', '-')}",
            "$type": "project",
            "$status": "active" if idx <= 7 else "archived",
            "$confidence": 0.90,
            "$tags": tags,
            "$relationships": rels,
        }, f"# {title}\n\n{title} project focusing on improving platform capabilities. "
           f"Key initiative for Q1 2026 roadmap. Involves cross-team collaboration.\n")

    # --- 8 Teams ---
    team_names = [
        ("team_alpha", "Platform Core", ["platform", "backend"]),
        ("team_beta", "Frontend Experience", ["frontend", "ux"]),
        ("team_gamma", "Data Engineering", ["data", "ml"]),
        ("team_delta", "DevOps", ["infrastructure", "cicd"]),
        ("team_epsilon", "Security", ["security", "compliance"]),
        ("team_zeta", "Mobile", ["mobile", "ios", "android"]),
        ("team_eta", "QA Automation", ["testing", "automation"]),
        ("team_theta", "Design Systems", ["design", "ux"]),
    ]

    for idx, (slug, name, tags) in enumerate(team_names, 1):
        rels = []
        if idx <= 2:
            rels.append({
                "type": "part_of",
                "target": "entity/squad/squad-platform",
                "source": "manual",
                "confidence": 0.95,
            })
        elif idx <= 4:
            rels.append({
                "type": "part_of",
                "target": "entity/squad/squad-infrastructure",
                "source": "manual",
                "confidence": 0.90,
            })
        if idx == 1:
            rels.append({
                "type": "collaborates_with",
                "target": "entity/team/team-beta",
                "source": "manual",
                "confidence": 0.85,
            })

        _create_entity(brain, "Entities/Teams", slug, {
            "$id": f"entity/team/{slug.replace('_', '-')}",
            "$type": "team",
            "$status": "active",
            "$confidence": 0.90,
            "$tags": tags,
            "$relationships": rels,
        }, f"# {name}\n\n{name} team responsible for core platform components. "
           f"Works on reliability, scalability, and developer tooling.\n")

    # --- 7 Systems ---
    system_names = [
        ("auth_service", "Authentication Service", ["auth", "oauth"]),
        ("api_gateway", "API Gateway", ["api", "routing"]),
        ("message_queue", "Message Queue", ["messaging", "async"]),
        ("cache_layer", "Cache Layer", ["redis", "caching"]),
        ("search_engine", "Search Engine", ["elasticsearch", "search"]),
        ("monitoring", "Monitoring Stack", ["observability", "metrics"]),
        ("deploy_pipeline", "Deploy Pipeline", ["cicd", "deployment"]),
    ]

    for idx, (slug, name, tags) in enumerate(system_names, 1):
        rels = []
        if idx == 1:
            rels.append({
                "type": "depends_on",
                "target": "entity/system/cache-layer",
                "source": "manual",
                "confidence": 0.95,
            })
        elif idx == 2:
            rels.append({
                "type": "depends_on",
                "target": "entity/system/auth-service",
                "source": "manual",
                "confidence": 0.95,
            })
        elif idx == 3:
            rels.append({
                "type": "depends_on",
                "target": "entity/system/monitoring",
                "source": "manual",
                "confidence": 0.85,
            })

        _create_entity(brain, "Entities/Systems", slug, {
            "$id": f"entity/system/{slug.replace('_', '-')}",
            "$type": "system",
            "$status": "active",
            "$confidence": 0.85,
            "$tags": tags,
            "$relationships": rels,
        }, f"# {name}\n\n{name} providing core infrastructure capabilities. "
           f"Deployed on Kubernetes with high-availability configuration.\n")

    # --- 5 Experiments ---
    experiment_names = [
        ("dark_mode", "Dark Mode UI", ["ux", "experiment"]),
        ("checkout_v2", "Checkout Flow V2", ["checkout", "ab-test"]),
        ("search_ranking", "Search Ranking ML", ["ml", "search"]),
        ("push_notif", "Push Notification Timing", ["notifications", "engagement"]),
        ("onboarding_flow", "Onboarding Simplification", ["onboarding", "conversion"]),
    ]

    for idx, (slug, name, tags) in enumerate(experiment_names, 1):
        rels = []
        if idx == 1:
            rels.append({
                "type": "tests_hypothesis_for",
                "target": "entity/project/project-delta",
                "source": "manual",
                "confidence": 0.80,
            })

        _create_entity(brain, "Entities/Experiments", slug, {
            "$id": f"entity/experiment/{slug.replace('_', '-')}",
            "$type": "experiment",
            "$status": "running" if idx <= 3 else "concluded",
            "$confidence": 0.75,
            "$tags": tags,
            "$relationships": rels,
        }, f"# {name}\n\n{name} experiment to validate hypothesis about user behavior. "
           f"Running A/B test with 50/50 traffic split.\n")

    # --- 5 Squads ---
    squad_names = [
        ("squad_platform", "Platform Squad", ["platform"]),
        ("squad_infrastructure", "Infrastructure Squad", ["infrastructure"]),
        ("squad_growth", "Growth Squad", ["growth", "acquisition"]),
        ("squad_retention", "Retention Squad", ["retention", "engagement"]),
        ("squad_data", "Data Squad", ["data", "analytics"]),
    ]

    for idx, (slug, name, tags) in enumerate(squad_names, 1):
        rels = []
        if idx == 1:
            rels.append({
                "type": "collaborates_with",
                "target": "entity/squad/squad-infrastructure",
                "source": "manual",
                "confidence": 0.85,
            })

        _create_entity(brain, "Entities/Squads", slug, {
            "$id": f"entity/squad/{slug.replace('_', '-')}",
            "$type": "squad",
            "$status": "active",
            "$confidence": 0.90,
            "$tags": tags,
            "$relationships": rels,
        }, f"# {name}\n\n{name} cross-functional squad focused on platform delivery. "
           f"Includes engineering, product, and design members.\n")

    # --- Non-entity files (should be excluded from analysis) ---
    (brain / "README.md").write_text("# Brain\nKnowledge graph root.\n", encoding="utf-8")
    index_dir = brain / "Entities"
    index_dir.mkdir(exist_ok=True)
    (index_dir / "_index.md").write_text("# Entity Index\n", encoding="utf-8")
    snapshots_dir = brain / ".snapshots"
    snapshots_dir.mkdir(exist_ok=True)
    (snapshots_dir / "snap_2026-01-01.md").write_text("---\n$id: snap\n---\nSnapshot\n", encoding="utf-8")

    yield brain

    # Teardown handled by tmp_path fixture


@pytest.fixture
def fixtures_dir():
    """Path to the static fixtures/ directory."""
    return Path(__file__).parent / "fixtures"


@pytest.fixture
def empty_brain_dir(tmp_path):
    """An empty brain directory for edge-case testing."""
    brain = tmp_path / "brain"
    brain.mkdir()
    yield brain
