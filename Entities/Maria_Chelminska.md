---
$schema: brain://entity/project/v1
$id: entity/project/maria-chelminska
$type: project
$version: 1
$created: '2026-01-22T08:31:01.233790Z'
$updated: '2026-01-22T10:41:35.324793+00:00'
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
  timestamp: '2026-01-22T08:31:01.233790Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.324795+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Maria Chelminska
---

# Maria Chelminska

## Metadata
- **Type**: Person
- **Role**: Product Manager
- **Team**: [[Squad_The_Pets_Table]] (New Ventures)

## Context
Product Manager for the The Pets Table squad.

## Changelog
- **2025-12-09:** Context update: [ ] **Prateek Jajoo & Maria Chelminska**: Share prototype for tailored cancellation deflection with Beatrice Dimarucut.
