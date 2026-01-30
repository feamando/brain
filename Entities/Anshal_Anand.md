---
$schema: brain://entity/project/v1
$id: entity/project/anshal-anand
$type: project
$version: 1
$created: '2026-01-22T08:31:01.221572Z'
$updated: '2026-01-22T10:41:35.300084+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-missions
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.221572Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.300085+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Anshal Anand
---

# Anshal Anand

## Metadata
- **Type**: Person
- **Role**: Product Manager
- **Team**: [[Squad_Missions]] (Loyalty & Virality)

## Context
Product Manager for the Missions squad.
