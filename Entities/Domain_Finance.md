---
$schema: brain://entity/project/v1
$id: entity/project/domain-finance
$type: project
$version: 1
$created: '2026-01-22T08:31:01.220727Z'
$updated: '2026-01-22T10:41:35.298601+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/fabien-simon
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
  timestamp: '2026-01-22T08:31:01.220727Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.298603+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 4
name: Domain Finance
---

# Domain: Finance

## Metadata
- **Type**: Domain
- **Alliance**: Global Finance
- **Commercial Leader**: [[Fabien Simon]]
- **Tech Leader**: [[Fabien Simon]]
- **Approver**: [[Dominik Richter]]

## Strategy Documents
- [Domain Objective Document](FINANCE 2026 HFG Domain Objectives - FINAL)
- [Yearly Plan Document]()

## Context
Part of the Global Finance alliance.
