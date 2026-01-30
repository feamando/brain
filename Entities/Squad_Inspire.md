---
$schema: brain://entity/project/v1
$id: entity/project/squad-inspire
$type: project
$version: 1
$created: '2026-01-22T08:31:01.125515Z'
$updated: '2026-01-30T10:22:37.187066'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/person/lisa-trueblood
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/edu-morni
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/lisa-trueblood
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.125515Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.121504+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Inspire
---

# Squad: Inspire

## Metadata
- **Type**: Squad
- **Tribe**: Engagement
- **Slack**: `#engagement-inspire-squad`
- **PM**: [[Lisa Trueblood]]
- **EM**: [[Edu Morôni]]
- **KPI (Q1 2026)**: Percentage of HelloFresh app downloads who save a recipe to their cookbook

## Focus & Scope
Responsible for Inspire within the Engagement tribe.

## Resources
