---
$schema: brain://entity/project/v1
$id: entity/project/domain-10
$type: project
$version: 1
$created: '2026-01-22T08:31:01.164643Z'
$updated: '2026-01-22T10:41:35.203485+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/nina-wagner
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/person/ed-boyes
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.164643Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.203486+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Domain 1.0
---

# Domain: 1.0

## Metadata
- **Type**: Domain
- **Alliance**: 1.0
- **Commercial Leader**: [[Adam Kalikow 
Ed Boyes]]
- **Tech Leader**: [[Nina Wagner]]
- **Approver**: [[Ed Boyes]]

## Strategy Documents
- [Domain Objective Document](2026 Domain Objectives: Meal Kits)
- [Yearly Plan Document]([WIP] 2026 HFG Global Product Development Yearly Plan)

## Context
Part of the 1.0 alliance.
