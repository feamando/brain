---
$schema: brain://entity/project/v1
$id: entity/project/priscila-koeck-machado
$type: project
$version: 1
$created: '2026-01-22T08:31:01.117423Z'
$updated: '2026-01-22T10:41:35.108350+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-client-platform
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.117423Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.108352+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Priscila Koeck Machado
---

# Priscila Koeck Machado

## Metadata
- **Type**: Person
- **Role**: Product Manager
- **Team**: [[Squad_Client_Platform]] (Consumer Foundations)

## Context
Product Manager for the Client Platform squad.
