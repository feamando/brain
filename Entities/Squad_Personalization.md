---
$schema: brain://entity/project/v1
$id: entity/project/squad-personalization
$type: project
$version: 1
$created: '2026-01-22T08:31:01.217785Z'
$updated: '2026-01-30T10:22:46.111022'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/person/tushar-raina
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/person/bartosz-raciborski
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/bartosz-raciborski
  confidence: 1.0
  last_verified: '2026-01-30'
- type: related_to
  target: entity/project/tushar-raina
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.217785Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.292833+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Personalization
---

# Squad: Personalization

## Metadata
- **Type**: Squad
- **Tribe**: Shopping Foundation
- **Slack**: `#cma-squad-personalization`
- **PM**: [[Tushar Raina]]
- **EM**: [[Bartosz Raciborski]]
- **KPI (Q1 2026)**: Predicted CLV per Intervention

## Focus & Scope
Responsible for Personalization within the Shopping Foundation tribe.

## Resources
