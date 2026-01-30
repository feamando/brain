---
$schema: brain://entity/project/v1
$id: entity/project/tushar-raina
$type: project
$version: 1
$created: '2026-01-22T08:31:01.236872Z'
$updated: '2026-01-22T10:41:35.330306+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-personalization
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.236872Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.330310+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Tushar Raina
---

# Tushar Raina

## Metadata
- **Type**: Person
- **Role**: Product Manager
- **Team**: [[Squad_Personalization]] (Shopping Foundation)

## Context
Product Manager for the Personalization squad.
