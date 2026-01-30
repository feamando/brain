---
$schema: brain://entity/project/v1
$id: entity/project/squad-shipping-and-tracking
$type: project
$version: 7
$created: '2026-01-22T08:31:01.178242Z'
$updated: '2026-01-30T14:34:32.363119+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.178242Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Squad Shipping And Tracking
---

# Squad: Shipping And Tracking

## Metadata
- **Type**: Squad
- **Tribe**: TBD
- **Status**: Active

## Focus & Scope
*Auto-generated stub. Please add details.*

## Codebase Ownership
- [tardis-community](https://github.com/hellofresh/tardis-community)
  - Paths: `pipelines/logistics/shipping-and-tracking/**`
- [web](https://github.com/hellofresh/web)
  - Paths: `/app/data-access/tracking, /app/pages/delivery-tracking, /app/scripts/next/plugins/redirects/delivery-tracking, /app/scripts/next/plugins/rewrites/delivery-tracking, /app/spaces/delivery-tracking (+4 more)`
- [label-generation-service](https://github.com/hellofresh/label-generation-service) (Owner)