---
$schema: brain://entity/project/v1
$id: entity/project/domain-80
$type: project
$version: 1
$created: '2026-01-22T08:31:01.232048Z'
$updated: '2026-01-22T10:41:35.322017+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/greg-chisholm-christian-gaertner
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/christian-gaertner-greg-chisholm
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/dominik-richter
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.232048Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.322019+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 3
name: Domain 8.0
---

# Domain: 8.0

## Metadata
- **Type**: Domain
- **Alliance**: 16.0
- **Commercial Leader**: [[Greg Chisholm Christian Gaertner]]
- **Tech Leader**: [[Christian Gaertner Greg Chisholm]]
- **Approver**: [[Dominik Richter]]

## Strategy Documents
- [Domain Objective Document]()
- [Yearly Plan Document]()

## Context
Part of the 16.0 alliance.
