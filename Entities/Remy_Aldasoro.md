---
$schema: brain://entity/project/v1
$id: entity/project/remy-aldasoro
$type: project
$version: 1
$created: '2026-01-22T08:31:01.116105Z'
$updated: '2026-01-30T14:57:53.403407'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-act
  since: null
  until: null
  role: null
  metadata: null
- type: owns
  target: entity/experiment/exp-tpt-allergens-in-the-funnel-layer
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: works_on
  target: entity/project/active-ux-experience-initiative
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: related_to
  target: entity/person/remy
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: related_to
  target: entity/person/theresa-stolberg
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: related_to
  target: entity/person/naseem-hasan
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: maintains
  target: entity/system/sprig
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.116105Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.106404+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Remy Aldasoro
---

# Remy Aldasoro

## Metadata
- **Type**: Person
- **Role**: Product Manager
- **Team**: [[Squad_Act]] (Engagement)

## Context
Product Manager for the Act squad.
