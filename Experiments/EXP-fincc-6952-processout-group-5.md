---
$schema: brain://entity/experiment/v1
$id: entity/experiment/exp-fincc-6952-processout-group-5
$type: experiment
$version: 1
$created: '2026-01-22T08:31:00.767866Z'
$updated: '2026-01-30T10:18:45.729444'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/experiment/exp-fincc-6905-processout-for-us
  confidence: 0.9201
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-fincc-6905-processout-for-fj
  confidence: 0.883
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-fincc-6820-enable-processout-for-group3
  confidence: 0.8686
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-fincc-6905-processout-for-group4
  confidence: 0.9022
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.767866Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/experiment/v1
  message: Migrated from v1 to v2 schema
name: Exp Fincc 6952 Processout Group 5
---

# fincc-6952-processout-group-5**Description:** Processout Group 5 Experiment**Status:** active**ID:** `fincc-6952-processout-group-5`## Linked Context*   *No Jira tickets linked explicitly.*
## Metrics & Goals
*Last Synced: 2026-01-07 10:24*