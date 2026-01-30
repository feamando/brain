---
$schema: brain://entity/project/v1
$id: entity/project/domain-20
$type: project
$version: 1
$created: '2026-01-22T08:31:01.193788Z'
$updated: '2026-01-22T10:41:35.249665+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/adam-park-ed-boyes
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.193788Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.249668+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Domain 2.0
---

# Domain: 2.0

## Metadata
- **Type**: Domain
- **Alliance**: 2.0
- **Commercial Leader**: [[Adam Park Ed Boyes]]
- **Tech Leader**: [[]]
- **Approver**: [[]]

## Strategy Documents
- [Domain Objective Document]()
- [Yearly Plan Document]()

## Context
Part of the 2.0 alliance.
