---
$schema: brain://entity/experiment/v1
$id: entity/experiment/exp-de-ec-price-test-25-q4
$type: experiment
$version: 1
$created: '2026-01-22T08:31:00.745014Z'
$updated: '2026-01-22T08:31:00.745014Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/experiment/exp-px-price-test-25-q4-de-hf
  confidence: 0.8825
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-px-price-test-24-q3-de
  confidence: 0.8719
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-px-price-test-25-q3-ch-hf
  confidence: 0.8633
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.745014Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/experiment/v1
  message: Migrated from v1 to v2 schema
name: Exp De Ec Price Test 25 Q4
---

# de-ec-price-test-25-q4**Description:** No description provided.**Status:** active**ID:** `de-ec-price-test-25-q4`## Linked Context*   *No Jira tickets linked explicitly.*
## Metrics & Goals
*Last Synced: 2026-01-07 10:24*