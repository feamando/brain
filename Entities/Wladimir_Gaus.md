---
$schema: brain://entity/project/v1
$id: entity/project/wladimir-gaus
$type: project
$version: 1
$created: '2026-01-22T08:31:01.180531Z'
$updated: '2026-01-22T10:41:35.228970+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-act
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.180531Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.228973+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Wladimir Gaus
---

# Wladimir Gaus

## Metadata
- **Type**: Person
- **Role**: Engineering Manager
- **Team**: [[Squad_Act]] (Engagement)

## Context
Engineering Manager for the Act squad.
