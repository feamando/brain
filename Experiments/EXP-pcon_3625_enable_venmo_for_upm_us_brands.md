---
$schema: brain://entity/experiment/v1
$id: entity/experiment/exp-pcon-3625-enable-venmo-for-upm-us-brands
$type: experiment
$version: 6
$created: '2026-01-22T08:31:00.888274Z'
$updated: '2026-01-30T14:50:43.094888+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/system/jira
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/system/venmo
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.888274Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/experiment/v1
  message: Migrated from v1 to v2 schema
name: Exp Pcon 3625 Enable Venmo For Upm Us Brands
$orphan_reason: no_external_data
---

# pcon_3625_enable_venmo_for_upm_us_brands**Description:** No description provided.**Status:** active**ID:** `pcon_3625_enable_venmo_for_upm_us_brands`## Linked Context*   *No Jira tickets linked explicitly.*
## Metrics & Goals
*Last Synced: 2026-01-07 10:24*