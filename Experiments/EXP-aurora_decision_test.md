---
$schema: brain://entity/experiment/v1
$id: entity/experiment/exp-aurora-decision-test
$type: experiment
$version: 1
$created: '2026-01-22T08:31:00.745581Z'
$updated: '2026-01-22T08:31:00.745581Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/experiment/exp-aurora-show-demo
  confidence: 0.863
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.745581Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/experiment/v1
  message: Migrated from v1 to v2 schema
name: Exp Aurora Decision Test
---

# aurora decision test**Description:** No description provided.**Status:** active**ID:** `aurora_decision_test`## Linked Context*   *No Jira tickets linked explicitly.*
## Metrics & Goals
*Last Synced: 2026-01-07 10:24*