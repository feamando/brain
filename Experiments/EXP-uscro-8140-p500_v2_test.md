---
$schema: brain://entity/experiment/v1
$id: entity/experiment/exp-uscro-8140-p500-v2-test
$type: experiment
$version: 6
$created: '2026-01-22T08:31:00.882730Z'
$updated: '2026-01-30T14:50:43.090597+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/p500
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/system/jira
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.882730Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/experiment/v1
  message: Migrated from v1 to v2 schema
name: Exp Uscro 8140 P500 V2 Test
$orphan_reason: no_external_data
---

# uscro-8140-P500_v2_test**Description:** No description provided.**Status:** active**ID:** `uscro-8140-p500_v2_test`## Linked Context*   *No Jira tickets linked explicitly.*
## Metrics & Goals
*Last Synced: 2026-01-07 10:24*