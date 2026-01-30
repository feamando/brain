---
$schema: brain://entity/experiment/v1
$id: entity/experiment/exp-gap-993-cen-mwdvsswd-fj
$type: experiment
$version: 1
$created: '2026-01-22T08:31:00.752328Z'
$updated: '2026-01-22T10:41:57.434390+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/experiment/exp-gap-1213-us-hellorefreshdm-2025w26
  confidence: 0.8839
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.752328Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/experiment/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:57.434393+00:00'
  type: orphan_cleanup
  actor: system/orphan_cleaner
  changes:
  - field: $relationships
    operation: cleanup
    count: 1
name: Exp Gap 993 Cen Mwdvsswd Fj
---

# GAP-993-CEN-MWDvsSWD-FJ**Description:** No description provided.**Status:** active**ID:** `gap-993-cen-mwdvsswd-fj`## Linked Context*   **Jira:** [[GAP-993]]## Metrics & Goals
*Last Synced: 2026-01-07 10:24*