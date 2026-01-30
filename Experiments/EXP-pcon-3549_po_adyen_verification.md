---
$schema: brain://entity/experiment/v1
$id: entity/experiment/exp-pcon-3549-po-adyen-verification
$type: experiment
$version: 7
$created: '2026-01-22T08:31:00.815221Z'
$updated: '2026-01-30T14:50:43.050097+00:00'
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
  target: entity/system/adyen
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.815221Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/experiment/v1
  message: Migrated from v1 to v2 schema
name: Exp Pcon 3549 Po Adyen Verification
$orphan_reason: no_external_data
---

# pcon-3549_po_adyen_verification**Description:** No description provided.**Status:** active**ID:** `pcon-3549_po_adyen_verification`## Linked Context*   *No Jira tickets linked explicitly.*
## Metrics & Goals
*Last Synced: 2026-01-07 10:24*