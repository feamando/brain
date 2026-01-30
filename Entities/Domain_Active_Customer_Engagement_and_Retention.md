---
$schema: brain://entity/project/v1
$id: entity/project/domain-active-customer-engagement-and-retention
$type: project
$version: 1
$created: '2026-01-22T08:31:01.113341Z'
$updated: '2026-01-22T10:41:35.102462+00:00'
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
  target: entity/project/dina-mehrez
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.113341Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.102469+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 4
name: Domain Active Customer Engagement And Retention
---

# Domain: Active Customer Engagement & Retention

## Metadata
- **Type**: Domain
- **Alliance**: Global Customer Experience
- **Commercial Leader**: [[Assaf Ronen]]
- **Tech Leader**: [[Dina Mehrez]]
- **Approver**: [[Assaf Ronen]]

## Strategy Documents
- [Domain Objective Document](2026 Domain Objectives: Customer Engagement & Retention)
- [Yearly Plan Document](2026 - Global Customer Experience - HFG Functional Yearly Plan Template)

## Context
Part of the Global Customer Experience alliance.

## Codebase Ownership
- [shared-mobile-modules](https://github.com/hellofresh/shared-mobile-modules)
  - Paths: `/src/assets/images/cooking-mode, /src/data-access/query/consumer-planner, /src/features/cooking-mode-feature, /src/features/image-cloudinary-with-placeholder, /src/features/recipe-detail/components/grocery-list-button (+2 more)`