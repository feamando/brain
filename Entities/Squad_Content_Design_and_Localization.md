---
$schema: brain://entity/project/v1
$id: entity/project/squad-content-design-and-localization
$type: project
$version: 7
$created: '2026-01-22T08:31:01.167518Z'
$updated: '2026-01-30T14:34:20.949921+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.167518Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.209619+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
- timestamp: '2026-01-22T10:41:57.452182+00:00'
  type: orphan_cleanup
  actor: system/orphan_cleaner
  changes:
  - field: $relationships
    operation: cleanup
    count: 1
name: Squad Content Design And Localization
---

# Squad: Content Design & Localization

## Metadata
- **Type**: Squad
- **Tribe**: UX
- **Slack**: `#cma-...-squad`
- **PM**: [[None]]
- **EM**: [[None]]
- **KPI (Q1 2026)**: 

## Focus & Scope
Responsible for Content Design & Localization within the UX tribe.

## Resources
