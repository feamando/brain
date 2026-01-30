---
$schema: brain://entity/project/v1
$id: entity/project/aleksei-akireikin
$type: project
$version: 1
$created: '2026-01-22T08:31:01.249219Z'
$updated: '2026-01-22T10:41:35.356754+00:00'
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
  timestamp: '2026-01-22T08:31:01.249219Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.356758+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Aleksei Akireikin
---

# Aleksei Akireikin

## Metadata
- **Type**: Person
- **Role**: Engineering Manager
- **Team**: [[Squad_Missions]] (Loyalty & Virality)

## Context
Engineering Manager for the Missions squad.
