---
$schema: brain://entity/project/v1
$id: entity/project/beatrice
$type: project
$version: 1
$created: '2026-01-22T08:31:01.219564Z'
$updated: '2026-01-30T10:22:46.170795'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/person/beatrice-dimarucut
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/team-new-ventures
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.219564Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.296358+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 3
name: Beatrice
redirect: '[[Entities/Beatrice_Dimarucut.md]]'
---

# Beatrice

**Redirect to:** [[Beatrice_Dimarucut.md]]

This entity has been consolidated. See [[Beatrice_Dimarucut.md]] for the canonical record.