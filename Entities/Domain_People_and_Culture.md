---
$schema: brain://entity/project/v1
$id: entity/project/domain-people-and-culture
$type: project
$version: 1
$created: '2026-01-22T08:31:01.197234Z'
$updated: '2026-01-22T10:41:35.256300+00:00'
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
  timestamp: '2026-01-22T08:31:01.197234Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.256304+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 4
name: Domain People And Culture
---

# Domain: People & Culture

## Metadata
- **Type**: Domain
- **Alliance**: Global People
- **Commercial Leader**: [[Ana Garcia]]
- **Tech Leader**: [[Ana Garcia]]
- **Approver**: [[Dominik Richter]]

## Strategy Documents
- [Domain Objective Document](2026 People Domain Objectives)
- [Yearly Plan Document](2026 People Yearly Plan)

## Context
Part of the Global People alliance.
