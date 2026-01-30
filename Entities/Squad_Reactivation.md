---
$schema: brain://entity/project/v1
$id: entity/project/squad-reactivation
$type: project
$version: 1
$created: '2026-01-22T08:31:01.120559Z'
$updated: '2026-01-30T10:12:09.073748'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: otp
  confidence: 0.65
  source: body_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.120559Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Squad Reactivation
---

# Squad: Reactivation

## Metadata
- **Type**: Squad
- **Tribe**: TBD
- **Status**: Active

## Focus & Scope
*Auto-generated stub. Please add details.*

## Codebase Ownership
- [web](https://github.com/hellofresh/web)
  - Paths: `/app/data-access/customer-orders, /app/data-access/one-time-purchase, /app/data-access/reactivation, /app/data-access/recipes, /app/e2e-tests/live/hf-reactivation-domain (+121 more)`