---
$schema: brain://entity/project/v1
$id: entity/project/edu-morni
$type: project
$version: 1
$created: '2026-01-22T08:31:01.167004Z'
$updated: '2026-01-22T10:41:35.207958+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-inspire
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.167004Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.207962+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Edu Morôni
---

# Edu Morôni

## Metadata
- **Type**: Person
- **Role**: Engineering Manager
- **Team**: [[Squad_Inspire]] (Engagement)

## Context
Engineering Manager for the Inspire squad.
