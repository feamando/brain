---
$schema: brain://entity/experiment/v1
$id: entity/experiment/exp-gai-7510-permanent-10-percent-explore
$type: experiment
$version: 6
$created: '2026-01-22T08:31:00.833092Z'
$updated: '2026-01-30T14:50:43.062497+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/factor
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/data
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/brand/factor-
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/system/jira
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.833092Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/experiment/v1
  message: Migrated from v1 to v2 schema
name: Exp Gai 7510 Permanent 10 Percent Explore
$orphan_reason: no_external_data
---

# GAI-7510_permanent_10_percent_explore**Description:** Set up permanent explore for Factor and US onsite, to collect data for building machine learning models**Status:** active**ID:** `gai-7510_permanent_10_percent_explore`## Linked Context*   *No Jira tickets linked explicitly.*
## Metrics & Goals
*Last Synced: 2026-01-07 10:24*