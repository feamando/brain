---
$schema: brain://entity/project/v1
$id: entity/project/abbas-ali-awan
$type: project
$version: 1
$created: '2026-01-22T08:31:01.246121Z'
$updated: '2026-01-30T14:08:59.265255'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-customer-profile
  since: null
  until: null
  role: null
  metadata: null
- type: works_on
  target: entity/project/elysium
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.246121Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.348186+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Abbas Ali Awan
---

# Abbas Ali Awan

## Metadata
- **Type**: Person
- **Role**: Engineering Manager
- **Team**: [[Squad_Customer_Profile]] (Shopping Journey)

## Context
Engineering Manager for the Customer Profile squad.
