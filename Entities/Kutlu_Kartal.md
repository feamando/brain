---
$schema: brain://entity/project/v1
$id: entity/project/kutlu-kartal
$type: project
$version: 1
$created: '2026-01-22T08:31:01.190683Z'
$updated: '2026-01-22T10:41:35.245198+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-consumer-acceleration
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.190683Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.245200+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Kutlu Kartal
---

# Kutlu Kartal

## Metadata
- **Type**: Person
- **Role**: Engineering Manager
- **Team**: [[Squad_Consumer_Acceleration]] (Consumer Foundations)

## Context
Engineering Manager for the Consumer Acceleration squad.
