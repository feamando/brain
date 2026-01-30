---
$schema: brain://entity/experiment/v1
$id: entity/experiment/exp-fincc-6783-enable-token-fetch-by-subscription
$type: experiment
$version: 6
$created: '2026-01-22T08:31:00.876401Z'
$updated: '2026-01-30T14:50:43.087546+00:00'
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
  timestamp: '2026-01-22T08:31:00.876401Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/experiment/v1
  message: Migrated from v1 to v2 schema
name: Exp Fincc 6783 Enable Token Fetch By Subscription
$orphan_reason: no_external_data
---

# fincc-6783-enable_token_fetch_by_subscription**Description:** Decide whether to use subscription or legacy token id to fetch token**Status:** active**ID:** `fincc-6783-enable_token_fetch_by_subscription`## Linked Context*   *No Jira tickets linked explicitly.*
## Metrics & Goals
*Last Synced: 2026-01-07 10:24*