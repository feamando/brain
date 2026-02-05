# Brain: Semantic Knowledge Graph Framework

This repository contains the **framework and schemas** for the PM-OS Brain - a semantic knowledge graph for AI agents. 

**Important:** This repo contains only the service definition, schemas, and folder structure. Actual entity data, personal information, and content should remain in your local PM-OS installation and should NOT be committed to this repository.

## What This Repo Contains

- `.schema/` - JSON schemas defining entity structures (person, project, team, etc.)
- Placeholder folders showing the expected directory structure
- This README documenting the architecture

## What This Repo Does NOT Contain

- Entity data (people, projects, teams)
- Private content or documents
- State files (registry.yaml, content_index.json, etc.)
- Inbox data or caches

## Philosophy

- **Markdown is the Database:** All knowledge is stored in structured Markdown files
- **Entity-Oriented:** Files are organized by what they *are* (Project, Team, Decision), not when they happened
- **Living Documents:** Files are meant to be updated, refined, and refactored over time
- **Local Data:** Your actual data stays local - only the framework is shared

## Directory Structure

| Directory | Purpose |
|-----------|---------|
| `/Entities` | People, Teams, and external Companies |
| `/Projects` | Long-running initiatives with goals and roadmaps |
| `/Architecture` | Technical systems, data flows, platform docs |
| `/Strategy` | Strategic documents and planning |
| `/Inbox` | Transient storage for data processing |

## Schema Reference

The `.schema/` directory contains JSON schemas for all entity types:

| Schema | Description |
|--------|-------------|
| `entity.schema.json` | Base entity schema |
| `person.schema.json` | People entities |
| `team.schema.json` | Team entities |
| `squad.schema.json` | Squad entities |
| `project.schema.json` | Project entities |
| `event.schema.json` | Event entities |
| `registry.schema.json` | Entity registry schema |
| `relationship.schema.json` | Relationship definitions |

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

## Usage with PM-OS

This framework is used by PM-OS tools:

```bash
# Load brain context
python3 common/tools/brain/brain_loader.py

# Enrich entities
python3 common/tools/brain/brain_enricher.py

# Search brain
python3 common/tools/brain/brain_search.py --query "project name"
```

## Local Setup

Your local Brain data lives in `user/brain/` within your PM-OS installation. The schemas from this repo are used to validate entity structure.

---

*Part of [PM-OS](https://github.com/hellofresh/hf-pm-os)*
