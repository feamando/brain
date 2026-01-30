---
$schema: brain://entity/project/v1
$id: entity/project/priyank-khanna
$type: project
$version: 1
$created: '2026-01-22T08:31:01.189729Z'
$updated: '2026-01-22T10:41:35.243237+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-shopping-platform
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.189729Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.243238+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Priyank Khanna
---

# Priyank Khanna

## Metadata
- **Type**: Person
- **Role**: Product Manager
- **Team**: [[Squad_Shopping_Platform]] (Shopping Foundation)

## Context
Product Manager for the Shopping Platform squad.
