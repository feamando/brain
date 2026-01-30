---
$schema: brain://entity/experiment/v1
$id: entity/experiment/exp-nz-2-tier-saver-plan
$type: experiment
$version: 7
$created: '2026-01-22T08:31:00.807850Z'
$updated: '2026-01-30T14:50:43.046055+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.807850Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/experiment/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:57.438475+00:00'
  type: orphan_cleanup
  actor: system/orphan_cleaner
  changes:
  - field: $relationships
    operation: cleanup
    count: 1
name: Exp Nz 2 Tier Saver Plan
$orphan_reason: no_external_data
---

# NZ-2-tier-saver-plan**Description:** No description provided.**Status:** active**ID:** `nz-2-tier-saver-plan`## Linked Context*   **Jira:** [[NZ-2]]## Metrics & Goals
*Last Synced: 2026-01-07 10:24*