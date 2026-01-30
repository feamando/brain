---
$schema: brain://entity/project/v1
$id: entity/project/domain-90
$type: project
$version: 1
$created: '2026-01-22T08:31:01.238421Z'
$updated: '2026-01-22T10:41:35.334138+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/ana-garcia
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
  timestamp: '2026-01-22T08:31:01.238421Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.334140+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Domain 9.0
---

# Domain: 9.0

## Metadata
- **Type**: Domain
- **Alliance**: 17.0
- **Commercial Leader**: [[Ana Garcia]]
- **Tech Leader**: [[Ana Garcia (Tech Support: Suman Rao Marc Huvelin  / INTL WFS: Philipp Börner)]]
- **Approver**: [[Dominik Richter]]

## Strategy Documents
- [Domain Objective Document]()
- [Yearly Plan Document]()

## Context
Part of the 17.0 alliance.
