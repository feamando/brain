---
$schema: brain://entity/project/v1
$id: entity/project/squad-delivery-network
$type: project
$version: 7
$created: '2026-01-22T08:31:01.152150Z'
$updated: '2026-01-30T14:34:08.295246+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.152150Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Squad Delivery Network
---

# Squad: Delivery Network

## Metadata
- **Type**: Squad
- **Tribe**: TBD
- **Status**: Active

## Focus & Scope
*Auto-generated stub. Please add details.*

## Codebase Ownership
- [tardis-community](https://github.com/hellofresh/tardis-community)
  - Paths: `pipelines/logistics/delivery-network/**`
- [web](https://github.com/hellofresh/web)
  - Paths: `/app/data-access/regions, /app/spaces/checkout/modules/__shared_context/experiments/tada, /app/spaces/legacy/modules/checkout-fragment/src/experiments/tada`
- [delivery-options-service](https://github.com/hellofresh/delivery-options-service) (Owner)
- [api-v2](https://github.com/hellofresh/api-v2)
  - Paths: `src/Handler/Subscription/PostSubscriptionSearchHandler.php, src/Handler/Subscription/GetSubscriptionProductFamilySearchHandler.php`