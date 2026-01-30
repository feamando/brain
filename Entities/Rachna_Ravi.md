---
$schema: brain://entity/project/v1
$id: entity/project/rachna-ravi
$type: project
$version: 1
$created: '2026-01-22T08:31:01.206190Z'
$updated: '2026-01-22T10:41:35.272708+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-share
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.206190Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.272710+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Rachna Ravi
---

# Rachna Ravi

## Metadata
- **Type**: Person
- **Role**: Product Manager
- **Team**: [[Squad_Share]] (Loyalty & Virality)

## Context
Product Manager for the Share squad.
