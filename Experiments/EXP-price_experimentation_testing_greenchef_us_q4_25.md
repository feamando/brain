---
$schema: brain://entity/experiment/v1
$id: entity/experiment/exp-price-experimentation-testing-greenchef-us-q4-25
$type: experiment
$version: 1
$created: '2026-01-22T08:31:00.749915Z'
$updated: '2026-01-30T10:18:45.796248'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/experiment/exp-price-experimentation-testing-hellofresh-gb-q4-25-reten
  confidence: 0.8709
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-price-experimentation-testing-hellofresh-dk-q4-25-v2
  confidence: 0.8702
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/experiment/exp-price-experimentation-testing-hellofresh-ca-q4-25
  confidence: 0.899
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.749915Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/experiment/v1
  message: Migrated from v1 to v2 schema
name: Exp Price Experimentation Testing Greenchef Us Q4 25
---

# price_experimentation_testing_greenchef_us_q4_25**Description:** No description provided.**Status:** active**ID:** `price_experimentation_testing_greenchef_us_q4_25`## Linked Context*   *No Jira tickets linked explicitly.*
## Metrics & Goals
*Last Synced: 2026-01-07 10:24*