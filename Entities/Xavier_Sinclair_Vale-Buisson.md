---
$schema: brain://entity/project/v1
$id: entity/project/xavier-sinclair-vale-buisson
$type: project
$version: 1
$created: '2026-01-22T08:31:01.097014Z'
$updated: '2026-01-30T14:58:48.948107'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-cart
  since: null
  until: null
  role: null
  metadata: null
- type: works_on
  target: entity/project/squad-agent-experience
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: maintains
  target: entity/system/bob-intfood
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.097014Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.076297+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Xavier Sinclair Vale Buisson
---

# Xavier Sinclair Vale-Buisson

## Metadata
- **Type**: Person
- **Role**: Product Manager
- **Team**: [[Squad_Cart]] (Shopping Foundation)

## Context
Product Manager for the Cart squad.
