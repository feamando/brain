---
$schema: brain://entity/experiment/v1
$id: entity/experiment/exp-fincc-6905-processout-for-group4
$type: experiment
$version: 1
$created: '2026-01-22T08:31:00.725825Z'
$updated: '2026-01-22T08:31:00.725825Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/experiment/exp-fincc-6952-processout-group-5
  confidence: 0.9022
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-fincc-6905-processout-for-us
  confidence: 0.8678
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-fincc-6820-enable-processout-for-group3
  confidence: 0.8648
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-fincc-6905-processout-for-fj
  confidence: 0.8295
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.65
- type: similar_to
  target: entity/experiment/exp-fincc-6934-processout-fully-rolled-out-countries
  confidence: 0.7403
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.65
- type: similar_to
  target: entity/experiment/exp-fincc-6154-enable-processout-at-checkout-for-credit-card
  confidence: 0.6638
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.65
- type: similar_to
  target: entity/experiment/exp-pcon-2219-express-checkout-experiment-factor-cg-ye
  confidence: 0.6531
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.65
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.725825Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/experiment/v1
  message: Migrated from v1 to v2 schema
name: Exp Fincc 6905 Processout For Group4
---

# fincc-6905_processout_for_group4**Description:** Processout experiment for BE, DE, LU, NL, NO, NZ, SE**Status:** active**ID:** `fincc-6905_processout_for_group4`## Linked Context*   *No Jira tickets linked explicitly.*
## Metrics & Goals
*Last Synced: 2026-01-07 10:24*