---
$schema: brain://entity/project/v1
$id: entity/project/deo-nathaniel
$type: project
$version: 1
$created: '2026-01-22T08:31:01.218908Z'
$updated: '2026-01-22T10:41:35.294843+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-cross-selling-and-subscription-flexibility
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.218908Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.294845+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Deo Nathaniel
---

# Deo Nathaniel

## Metadata
- **Type**: Person
- **Role**: Product Manager
- **Team**: [[Squad_Cross_Selling_and_Subscription_Flexibility]] (Shopping Foundation)

## Context
Product Manager for the Cross Selling and Subscription Flexibility squad.
