---
$schema: brain://entity/project/v1
$id: entity/project/domain--
$type: project
$version: 1
$created: '2026-01-22T08:31:01.234785Z'
$updated: '2026-01-22T10:41:35.326872+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/tim-schoenharl
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
  timestamp: '2026-01-22T08:31:01.234785Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.326874+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: 'Domain  '
---

# Domain: -

## Metadata
- **Type**: Domain
- **Alliance**: Global Intelligent Platforms Mega-Alliance
- **Commercial Leader**: [[]]
- **Tech Leader**: [[Tim Schoenharl]]
- **Approver**: [[Assaf Ronen]]

## Strategy Documents
- [Domain Objective Document]()
- [Yearly Plan Document](2026 HelloTech Intelligent Platforms Year Plan)

## Context
Part of the Global Intelligent Platforms Mega-Alliance alliance.

## Changelog
- **2025-12-16:** Context update: **Good Chop Hiring:** Opening mid-level designer role immediately (replace David). Focus on systematic design execution.
- **2025-12-11:** Context update: **Group Alias Fix:** Resolved email issue with "tribe NV" group alias - setting was only allowing HelloFresh emails, needed fix for Lokalise service a
- **2025-12-09:** Context update: **Staffing/Contracts:** Budget approval for Tishia secured. Jama approved an 18-month analytics support contract role (separate from a permanent produ
