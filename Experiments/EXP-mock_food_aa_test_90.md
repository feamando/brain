---
$schema: brain://entity/experiment/v1
$id: entity/experiment/exp-mock-food-aa-test-90
$type: experiment
$version: 7
$created: '2026-01-22T08:31:00.814180Z'
$updated: '2026-01-30T14:50:43.049640+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/food
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
  timestamp: '2026-01-22T08:31:00.814180Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/experiment/v1
  message: Migrated from v1 to v2 schema
name: Exp Mock Food Aa Test 90
$orphan_reason: no_external_data
---

# Mock Food AA test 90**Description:** No description provided.**Status:** active**ID:** `mock_food_aa_test_90`## Linked Context*   *No Jira tickets linked explicitly.*
## Metrics & Goals
*Last Synced: 2026-01-07 10:24*