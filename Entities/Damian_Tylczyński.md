---
$schema: brain://entity/project/v1
$id: entity/project/damian-tylczyski
$type: project
$version: 1
$created: '2026-01-22T08:31:01.184486Z'
$updated: '2026-01-30T14:46:22.350927'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-monoliths
  since: null
  until: null
  role: null
  metadata: null
- type: owns
  target: entity/experiment/exp-dxperiment-009-fr-filtered-check-the-delivery
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: related_to
  target: entity/person/marat
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.184486Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.234482+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Damian Tylczyński
---

# Damian Tylczyński

## Metadata
- **Type**: Person
- **Role**: Engineering Manager
- **Team**: [[Squad_Monoliths]] (Consumer Core)

## Context
Engineering Manager for the Monoliths squad.
