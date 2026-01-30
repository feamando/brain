---
$schema: brain://entity/experiment/v1
$id: entity/experiment/exp-rtevms-2001-multi-box-discounts
$type: experiment
$version: 6
$created: '2026-01-22T08:31:00.892371Z'
$updated: '2026-01-30T14:50:43.096841+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/system/jira
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.892371Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/experiment/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:57.441046+00:00'
  type: orphan_cleanup
  actor: system/orphan_cleaner
  changes:
  - field: $relationships
    operation: cleanup
    count: 1
name: Exp Rtevms 2001 Multi Box Discounts
$orphan_reason: no_external_data
---

# RTEVMS-2001 Multi Box Discounts**Description:** No description provided.**Status:** active**ID:** `rtevms-2001_multi_box_discounts`## Linked Context*   **Jira:** [[RTEVMS-2001]]## Metrics & Goals
*Last Synced: 2026-01-07 10:24*