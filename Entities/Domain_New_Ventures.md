---
$schema: brain://entity/project/v1
$id: entity/project/domain-new-ventures
$type: project
$version: 1
$created: '2026-01-22T08:31:01.129034Z'
$updated: '2026-01-22T10:41:57.450555+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/jama-musse-holger-hammel
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
  timestamp: '2026-01-22T08:31:01.129034Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.128229+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
- timestamp: '2026-01-22T10:41:57.450557+00:00'
  type: orphan_cleanup
  actor: system/orphan_cleaner
  changes:
  - field: $relationships
    operation: cleanup
    count: 1
name: Domain New Ventures
---

# Domain: New Ventures

## Metadata
- **Type**: Domain
- **Alliance**: TAM Alliance
- **Commercial Leader**: [[TPT Laurent Guillemain, GC, Seb Tron, Yury Trofimov]]
- **Tech Leader**: [[Jama Musse Holger Hammel]]
- **Approver**: [[Dominik Richter]]

## Strategy Documents
- [Domain Objective Document](2026 Good Chop Domain Objectives

2026 HFG Domain Objectives - The Pets Table)
- [Yearly Plan Document](2026 Yearly Plan - Consumer Mega-Alliance - New Ventures)

## Context
Part of the TAM Alliance alliance.
