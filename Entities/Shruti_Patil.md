---
$schema: brain://entity/project/v1
$id: entity/project/shruti-patil
$type: project
$version: 1
$created: '2026-01-22T08:31:01.214761Z'
$updated: '2026-01-22T10:41:35.287472+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-merchandising-and-shopping-guidance
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.214761Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.287475+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Shruti Patil
---

# Shruti Patil

## Metadata
- **Type**: Person
- **Role**: Engineering Manager
- **Team**: [[Squad_Merchandising_and_Shopping_Guidance]] (Shopping Journey)

## Context
Engineering Manager for the Merchandising & Shopping Guidance squad.
