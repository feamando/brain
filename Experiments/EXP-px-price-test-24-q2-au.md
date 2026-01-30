---
$schema: brain://entity/experiment/v1
$id: entity/experiment/exp-px-price-test-24-q2-au
$type: experiment
$version: 1
$created: '2026-01-22T08:31:00.746708Z'
$updated: '2026-01-22T08:31:00.746708Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/experiment/exp-px-price-test-24-q2-us
  confidence: 0.9815
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-px-price-test-24-q3-de
  confidence: 0.9628
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-px-price-test-25-q3-ch-hf
  confidence: 0.9461
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-px-price-test-25-q4-de-hf
  confidence: 0.9371
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-px-price-test-25-q3-ch-hf-clean
  confidence: 0.9248
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-px-price-test-24-q2-au-bau-filter
  confidence: 0.911
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-px-price-test-24-q2-au-bau-filter-v2
  confidence: 0.9066
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-px-price-test-24-q2-us-bau-filter
  confidence: 0.8933
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-px-price-test-24-q3-de-bau-filter
  confidence: 0.8785
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.746708Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/experiment/v1
  message: Migrated from v1 to v2 schema
name: Exp Px Price Test 24 Q2 Au
---

# px-price-test-24-q2-au**Description:** No description provided.**Status:** active**ID:** `px-price-test-24-q2-au`## Linked Context*   *No Jira tickets linked explicitly.*
## Metrics & Goals
*Last Synced: 2026-01-07 10:24*