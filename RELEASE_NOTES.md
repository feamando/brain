# Brain v1.2 Release Notes

**Release Date:** 2026-01-30
**Total Entities:** 3,454

## Overview

Initial release of the PM-OS Brain knowledge base with time-series entity system.

## Contents

### Entity Categories
- **Entities/** - 282 people, teams, and domains
- **Projects/** - 348 project contexts with stakeholders
- **Experiments/** - 330 A/B test records
- **Strategy/** - 43 strategic documents
- **Technical/** - Architecture patterns and conventions
- **Reasoning/** - FPF reasoning artifacts
- **Inbox/** - Processing queue for new information

### Key Files
- `registry.yaml` - Entity index with canonical references
- `content_index.json` - Full-text search index
- `entity_aliases.json` - Alias resolution mappings
- `Glossary.md` - Domain vocabulary

## Brain Schema v1.2 Features

- **Canonical References** - All entities use `entity/{type}/{slug}` format
- **Bidirectional Relationships** - Typed relationships with temporal validity
- **Event Sourcing** - Full change history with timestamps
- **Quality Scoring** - Automated completeness and freshness metrics
- **Rich Metadata** - Confidence scores, sources, validity periods

## Graph Health

- Orphan Rate: 18.6% (target: <30%)
- Relationship Coverage: 56%+ of entities
- Average Relationships: 1.7 per entity

## Usage

Load this brain with PM-OS:
```
/brain-load
```

Query the brain:
```
/q-query "Who works on mobile?"
```
