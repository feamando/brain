---
$schema: brain://entity/project/v1
$id: entity/project/bruno-klarin
$type: project
$version: 1
$created: '2026-01-22T08:31:01.211313Z'
$updated: '2026-01-22T10:41:35.281338+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-rewards
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.211313Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.281340+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Bruno Klarin
---

# Bruno Klarin

## Metadata
- **Type**: Person
- **Role**: Engineering Manager
- **Team**: [[Squad_Rewards]] (Loyalty & Virality)

## Context
Engineering Manager for the Rewards squad.
