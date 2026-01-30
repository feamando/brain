---
$schema: brain://entity/project/v1
$id: entity/project/domain-marketing
$type: project
$version: 1
$created: '2026-01-22T08:31:01.201236Z'
$updated: '2026-01-22T10:41:35.261787+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/person/patrick-stal
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
  timestamp: '2026-01-22T08:31:01.201236Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.261790+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 4
name: Domain Marketing
---

# Domain: Marketing

## Metadata
- **Type**: Domain
- **Alliance**: Global Marketing
- **Commercial Leader**: [[Patrick Stal]]
- **Tech Leader**: [[Patrick Stal]]
- **Approver**: [[Assaf Ronen]]

## Strategy Documents
- [Domain Objective Document](2026 HFG Domain Objectives | Marketing)
- [Yearly Plan Document](2026 Global Marketing Yearly Plan)

## Context
Part of the Global Marketing alliance.
