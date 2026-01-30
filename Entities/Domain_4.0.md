---
$schema: brain://entity/project/v1
$id: entity/project/domain-40
$type: project
$version: 1
$created: '2026-01-22T08:31:01.223539Z'
$updated: '2026-01-22T10:41:35.303471+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/dan-seidel-mark-hemming
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/dan-seidel
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/person/assaf-ronen
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.223539Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.303472+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 3
name: Domain 4.0
---

# Domain: 4.0

## Metadata
- **Type**: Domain
- **Alliance**: 4.0
- **Commercial Leader**: [[Dan Seidel Mark Hemming]]
- **Tech Leader**: [[Dan Seidel]]
- **Approver**: [[Assaf Ronen]]

## Strategy Documents
- [Domain Objective Document]()
- [Yearly Plan Document]()

## Context
Part of the 4.0 alliance.
