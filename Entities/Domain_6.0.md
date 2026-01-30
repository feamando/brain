---
$schema: brain://entity/project/v1
$id: entity/project/domain-60
$type: project
$version: 1
$created: '2026-01-22T08:31:01.100958Z'
$updated: '2026-01-22T10:41:35.083758+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/patrick-stal-marcus-von-franck
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/person/marcus-von-franck
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
  timestamp: '2026-01-22T08:31:01.100958Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.083761+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 3
name: Domain 6.0
---

# Domain: 6.0

## Metadata
- **Type**: Domain
- **Alliance**: 9.0
- **Commercial Leader**: [[Patrick Stal Marcus von Franck]]
- **Tech Leader**: [[Marcus von Franck]]
- **Approver**: [[Assaf Ronen]]

## Strategy Documents
- [Domain Objective Document]()
- [Yearly Plan Document]()

## Context
Part of the 9.0 alliance.
