---
$schema: brain://entity/experiment/v1
$id: entity/experiment/exp-aurora-predictive-metrtics-qa-2-1
$type: experiment
$version: 1
$created: '2026-01-22T08:31:00.725027Z'
$updated: '2026-01-22T08:31:00.725027Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/experiment/exp-aurora-predictive-metrics-qa-2
  confidence: 0.8804
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-aurora-predictive-metrics-qa-4
  confidence: 0.8787
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-aurora-predictive-qa-6
  confidence: 0.8707
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-aurora-predictive-8
  confidence: 0.8654
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-aurora-predictive-metrics-qa-3
  confidence: 0.8617
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-aurora-predictive-qa-5
  confidence: 0.8556
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-aurora-qa-predictive-1
  confidence: 0.8257
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.65
- type: similar_to
  target: entity/experiment/exp-aurora-show-demo
  confidence: 0.8176
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.65
- type: similar_to
  target: entity/experiment/exp-aurora-decision-test
  confidence: 0.7738
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.65
- type: similar_to
  target: entity/experiment/exp-aurora-correct-converted-only
  confidence: 0.7634
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.65
- type: similar_to
  target: entity/experiment/exp-aurora-test-bar-raiser
  confidence: 0.7055
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.65
- type: similar_to
  target: entity/experiment/exp-aurora-test-sequential
  confidence: 0.7033
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.65
- type: similar_to
  target: entity/experiment/exp-tessa-aurora-test-
  confidence: 0.6912
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.65
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.725027Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/experiment/v1
  message: Migrated from v1 to v2 schema
name: Exp Aurora Predictive Metrtics Qa 2 1
---

# aurora-predictive-metrtics-qa-2_1**Description:** Addinng metrics from historical table (contain all weeks). Cloning again to avoid update of current results, just to be safe**Status:** active**ID:** `aurora-predictive-metrtics-qa-2_1`## Linked Context*   *No Jira tickets linked explicitly.*
## Metrics & Goals
*Last Synced: 2026-01-07 10:24*