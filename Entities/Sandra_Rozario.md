---
$schema: brain://entity/project/v1
$id: entity/project/sandra-rozario
$type: project
$version: 1
$created: '2026-01-22T08:31:01.189198Z'
$updated: '2026-01-30T14:09:00.244303'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-feedback
  since: null
  until: null
  role: null
  metadata: null
- type: owns
  target: entity/experiment/exp-auto-save-web-au-bias
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: owns
  target: entity/experiment/exp-auto-save-web-us-bias
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: works_on
  target: entity/project/active-ux-experience-initiative
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.189198Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.241908+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Sandra Rozario
---

# Sandra Rozario

## Metadata
- **Type**: Person
- **Role**: Product Manager
- **Team**: [[Squad_Feedback]] (Shopping Journey)

## Context
Product Manager for the Feedback squad.
