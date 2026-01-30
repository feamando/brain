---
$schema: brain://entity/project/v1
$id: entity/project/ahmed-wagdi
$type: project
$version: 1
$created: '2026-01-22T08:31:01.131482Z'
$updated: '2026-01-22T10:41:35.133128+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-the-pets-table
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.131482Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.133131+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Ahmed Wagdi
---

# Ahmed Wagdi

## Metadata
- **Type**: Person
- **Role**: Engineering Manager
- **Team**: [[Squad_The_Pets_Table]] (New Ventures)

## Context
Engineering Manager for the The Pets Table squad.
