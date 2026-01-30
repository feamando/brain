---
$schema: brain://entity/project/v1
$id: entity/project/squad-checkout
$type: project
$version: 1
$created: '2026-01-22T08:31:01.230389Z'
$updated: '2026-01-30T15:14:15.775946'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: has_contributor
  target: entity/person/nikita-gorshkov
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.230389Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Squad Checkout
---

# Squad: Checkout

## Metadata
- **Type**: Squad
- **Tribe**: TBD
- **Status**: Active

## Focus & Scope
*Auto-generated stub. Please add details.*

## Codebase Ownership
- [web](https://github.com/hellofresh/web)
  - Paths: `/app/data-access/checkout-offer-consent, /app/data-access/customer, /app/data-access/delivery-options, /app/data-access/single-page-checkout, /app/data-access/subscriptions/__test-data__ (+69 more)`