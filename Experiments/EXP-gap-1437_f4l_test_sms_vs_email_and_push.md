---
$schema: brain://entity/experiment/v1
$id: entity/experiment/exp-gap-1437-f4l-test-sms-vs-email-and-push
$type: experiment
$version: 6
$created: '2026-01-22T08:31:00.912318Z'
$updated: '2026-01-30T14:50:43.108142+00:00'
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
  timestamp: '2026-01-22T08:31:00.912318Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/experiment/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:57.442273+00:00'
  type: orphan_cleanup
  actor: system/orphan_cleaner
  changes:
  - field: $relationships
    operation: cleanup
    count: 1
name: Exp Gap 1437 F4L Test Sms Vs Email And Push
$orphan_reason: no_external_data
---

# GAP-1437 F4L test SMS vs Email and Push**Description:** No description provided.**Status:** active**ID:** `gap-1437_f4l_test_sms_vs_email_and_push`## Linked Context*   **Jira:** [[GAP-1437]]## Metrics & Goals
*Last Synced: 2026-01-07 10:24*