---
$schema: brain://entity/project/v1
$id: entity/project/lisa-trueblood
$type: project
$version: 1
$created: '2026-01-22T08:31:01.161863Z'
$updated: '2026-01-22T10:41:35.197191+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-inspire
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.161863Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.197193+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Lisa Trueblood
---

# Lisa Trueblood

## Metadata
- **Type**: Person
- **Role**: Product Manager
- **Team**: [[Squad_Inspire]] (Engagement)

## Context
Product Manager for the Inspire squad.
