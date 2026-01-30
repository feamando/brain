---
$schema: brain://entity/project/v1
$id: entity/project/domain-30
$type: project
$version: 1
$created: '2026-01-22T08:31:01.207614Z'
$updated: '2026-01-22T10:41:35.275644+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/person/ed-boyes
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/jama-musse-cho-hwang
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/person/jake-fear
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.207614Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.275645+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 3
name: Domain 3.0
---

# Domain: 3.0

## Metadata
- **Type**: Domain
- **Alliance**: 3.0
- **Commercial Leader**: [[Ed Boyes]]
- **Tech Leader**: [[Jama Musse Cho Hwang]]
- **Approver**: [[Jake Fear]]

## Strategy Documents
- [Domain Objective Document]()
- [Yearly Plan Document]()

## Context
Part of the 3.0 alliance.
