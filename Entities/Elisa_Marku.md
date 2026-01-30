---
$schema: brain://entity/project/v1
$id: entity/project/elisa-marku
$type: project
$version: 1
$created: '2026-01-22T08:31:01.137127Z'
$updated: '2026-01-22T10:41:35.147118+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-menu-discovery
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.137127Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.147120+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Elisa Marku
---

# Elisa Marku

## Metadata
- **Type**: Person
- **Role**: Product Manager
- **Team**: [[Squad_Menu_Discovery]] (Shopping Journey)

## Context
Product Manager for the Menu Discovery squad.
