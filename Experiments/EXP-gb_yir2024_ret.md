---
$schema: brain://entity/experiment/v1
$id: entity/experiment/exp-gb-yir2024-ret
$type: experiment
$version: 1
$created: '2026-01-22T08:31:00.765161Z'
$updated: '2026-01-22T08:31:00.765161Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/experiment/exp-us-yir2024-ret
  confidence: 0.9348
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-fj-yir2024-ret
  confidence: 0.9092
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.765161Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/experiment/v1
  message: Migrated from v1 to v2 schema
name: Exp Gb Yir2024 Ret
---

# GB_YIR2024_RET**Description:** No description provided.**Status:** active**ID:** `gb_yir2024_ret`## Linked Context*   *No Jira tickets linked explicitly.*
## Metrics & Goals
*Last Synced: 2026-01-07 10:24*