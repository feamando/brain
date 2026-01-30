---
$schema: brain://entity/project/v1
$id: entity/project/a-dos-arbaaz-dossani
$type: project
$version: 1
$created: '2026-01-22T08:31:01.250254Z'
$updated: '2026-01-30T15:36:08.944612'
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
- type: works_on
  target: entity/project/nvb-team-nv-backend
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: works_on
  target: entity/project/cart-foundation-squad-squad-cart-foundation
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: works_on
  target: entity/project/squad-cart-foundation
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: related_to
  target: entity/person/katerina-scoullos
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: related_to
  target: entity/person/arbaaz-dossani
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: maintains
  target: entity/system/customer-recurring-selection-service-crs
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: member_of
  target: entity/squad/cart-foundation-squad
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.250254Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.358808+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: (A Dos) Arbaaz Dossani
---

# (A-Dos) Arbaaz Dossani

## Metadata
- **Type**: Person
- **Role**: Engineering Manager
- **Team**: [[Squad_Cross_Selling_and_Subscription_Flexibility]] (Shopping Foundation)

## Context
Engineering Manager for the Cross Selling and Subscription Flexibility squad.
