---
$schema: brain://entity/project/v1
$id: entity/project/domain-70
$type: project
$version: 1
$created: '2026-01-22T08:31:01.132879Z'
$updated: '2026-01-22T10:41:35.136207+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/person/assaf-ronen
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/tilman-eichstaedt
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
  timestamp: '2026-01-22T08:31:01.132879Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.136210+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 3
name: Domain 7.0
---

# Domain: 7.0

## Metadata
- **Type**: Domain
- **Alliance**: 14.0
- **Commercial Leader**: [[Assaf Ronen]]
- **Tech Leader**: [[Tilman Eichstaedt]]
- **Approver**: [[Dominik Richter]]

## Strategy Documents
- [Domain Objective Document]()
- [Yearly Plan Document]()

## Context
Part of the 14.0 alliance.
