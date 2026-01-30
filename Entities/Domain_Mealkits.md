---
$schema: brain://entity/project/v1
$id: entity/project/domain-mealkits
$type: project
$version: 1
$created: '2026-01-22T08:31:01.231307Z'
$updated: '2026-01-22T10:41:57.456564+00:00'
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
  timestamp: '2026-01-22T08:31:01.231307Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.320133+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
- timestamp: '2026-01-22T10:41:57.456565+00:00'
  type: orphan_cleanup
  actor: system/orphan_cleaner
  changes:
  - field: $relationships
    operation: cleanup
    count: 1
name: Domain Mealkits
---

# Domain: Mealkits

## Metadata
- **Type**: Domain
- **Alliance**: Global Physical Product
- **Commercial Leader**: [[Adam Kalikow , Ed Boyes]]
- **Tech Leader**: [[Nina Wagner]]
- **Approver**: [[Ed Boyes]]

## Strategy Documents
- [Domain Objective Document](2026 Domain Objectives: Meal Kits)
- [Yearly Plan Document]([WIP] 2026 HFG Global Product Development Yearly Plan)

## Context
Part of the Global Physical Product alliance.
