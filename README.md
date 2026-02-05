# Brain: Semantic Knowledge Graph Framework

This repository contains the **framework, schemas, and tools** for the PM-OS Brain - a semantic knowledge graph for AI agents.

**Important:** This repo contains the service definition, schemas, and tools. Actual entity data, personal information, and content should remain in your local PM-OS installation and should NOT be committed to this repository.

## Repository Contents

```
brain/
├── .schema/           # JSON schemas for entity validation
├── tools/             # Python tools for Brain operations
│   ├── enrichers/     # Data enrichment from external sources
│   └── tests/         # Unit tests
├── Entities/          # Placeholder (data stays local)
├── Projects/          # Placeholder (data stays local)
├── Architecture/      # Placeholder (data stays local)
├── Strategy/          # Placeholder (data stays local)
├── Inbox/             # Placeholder (data stays local)
└── README.md
```

## What This Repo Contains

### Schemas (`.schema/`)
JSON schemas defining entity structures:
- `entity.schema.json` - Base entity schema
- `person.schema.json` - People entities
- `team.schema.json` - Team entities
- `squad.schema.json` - Squad entities
- `project.schema.json` - Project entities
- `event.schema.json` - Event entities
- `registry.schema.json` - Entity registry schema
- `relationship.schema.json` - Relationship definitions

### Tools (`tools/`)

#### Core Tools
| Tool | Description |
|------|-------------|
| `brain_loader.py` | Load and query Brain entities |
| `brain_search.py` | Search across all entities |
| `brain_query.py` | Structured entity queries |
| `brain_index.py` | Build and maintain search index |
| `brain_graph.py` | Graph traversal and visualization |
| `brain_updater.py` | Update entity content |
| `unified_brain_writer.py` | Create and write entities |

#### Enrichment Tools
| Tool | Description |
|------|-------------|
| `brain_enrich.py` | Main enrichment orchestrator |
| `brain_enrichment_orchestrator.py` | Multi-source enrichment pipeline |
| `enrichment_pipeline.py` | Pipeline execution framework |
| `enrichers/slack_enricher.py` | Enrich from Slack data |
| `enrichers/jira_enricher.py` | Enrich from Jira tickets |
| `enrichers/github_enricher.py` | Enrich from GitHub repos |
| `enrichers/gdocs_enricher.py` | Enrich from Google Docs |
| `enrichers/context_enricher.py` | Enrich from context files |

#### Relationship Tools
| Tool | Description |
|------|-------------|
| `relationship_builder.py` | Build entity relationships |
| `relationship_normalizer.py` | Normalize relationship types |
| `relationship_auditor.py` | Audit relationship integrity |
| `relationship_decay.py` | Handle stale relationships |
| `body_relationship_extractor.py` | Extract relationships from content |
| `embedding_edge_inferrer.py` | Infer relationships via embeddings |

#### Quality & Maintenance
| Tool | Description |
|------|-------------|
| `entity_validator.py` | Validate entities against schemas |
| `quality_scorer.py` | Score entity completeness |
| `graph_health.py` | Check graph health metrics |
| `orphan_analyzer.py` | Find orphaned entities |
| `orphan_cleaner.py` | Clean up orphaned entities |
| `stale_entity_detector.py` | Detect stale entities |
| `reference_validator.py` | Validate entity references |

#### Data Management
| Tool | Description |
|------|-------------|
| `canonical_resolver.py` | Resolve entity aliases |
| `registry_v2_builder.py` | Build entity registry |
| `schema_migrator.py` | Migrate schemas between versions |
| `migration_runner.py` | Run data migrations |
| `snapshot_manager.py` | Create/restore snapshots |
| `temporal_query.py` | Query historical states |
| `event_store.py` | Store entity events |
| `extraction_hints.py` | Entity extraction hints |

## What This Repo Does NOT Contain

- Entity data (people, projects, teams)
- Private content or documents
- State files (registry.yaml, content_index.json, etc.)
- Inbox data or caches

## Philosophy

- **Markdown is the Database:** All knowledge stored in structured Markdown files
- **Entity-Oriented:** Files organized by what they *are* (Project, Team, Decision)
- **Living Documents:** Files meant to be updated, refined, and refactored
- **Local Data:** Your actual data stays local - only the framework is shared

## Relationship Types

Entities connect via typed relationships in YAML frontmatter:

| Forward | Inverse | Usage |
|---------|---------|-------|
| `owner` | `owns` | Person → Project/Domain |
| `member_of` | `has_member` | Person → Team |
| `blocked_by` | `blocks` | Project → Project/Issue |
| `depends_on` | `dependency_for` | Project → Project |
| `relates_to` | `relates_to` | Generic connection |
| `part_of` | `has_part` | Sub-component → System |

## Usage

```bash
# Load brain context
python3 tools/brain_loader.py

# Search entities
python3 tools/brain_search.py --query "project name"

# Validate entities
python3 tools/entity_validator.py --path Entities/

# Run enrichment
python3 tools/brain_enrich.py --source slack

# Check graph health
python3 tools/graph_health.py
```

## Local Setup

Your local Brain data lives in `user/brain/` within your PM-OS installation. Copy the tools to `common/tools/brain/` and schemas to `user/brain/.schema/`.

## Requirements

```
pyyaml>=6.0
jsonschema>=4.0
```

---

*Part of [PM-OS](https://github.com/hellofresh/hf-pm-os)*
