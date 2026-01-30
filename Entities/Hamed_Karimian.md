---
$schema: brain://entity/project/v1
$id: entity/project/hamed-karimian
$type: project
$version: 1
$created: '2026-01-22T08:31:01.149068Z'
$updated: '2026-01-22T10:41:35.168297+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-factor-form
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.149068Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.168299+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Hamed Karimian
---

# Hamed Karimian

## Metadata
- **Type**: Person
- **Role**: Product Manager
- **Team**: [[Squad_Factor_Form]] (New Ventures)

## Context
Product Manager for the Factor Form squad.

## Changelog
- **2025-12-11:** Context update: [ ] **Hamed Karimian**: Confirm OTP final launch date by early next week.
