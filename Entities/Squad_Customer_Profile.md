---
$schema: brain://entity/project/v1
$id: entity/project/squad-customer-profile
$type: project
$version: 1
$created: '2026-01-22T08:31:01.205561Z'
$updated: '2026-01-30T10:22:41.241761'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/person/wellney-yarra
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/abbas-ali-awan
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/wellney-yarra
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.205561Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.271195+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Customer Profile
---

# Squad: Customer Profile

## Metadata
- **Type**: Squad
- **Tribe**: Shopping Journey
- **Slack**: `#squad-customer-profile`
- **PM**: [[Wellney Yarra]]
- **EM**: [[Abbas Ali Awan]]
- **KPI (Q1 2026)**: Profile Completion Rate

## Focus & Scope
Responsible for Customer Profile within the Shopping Journey tribe.

## Resources
- [More Information](Customer Profile Kick Off)
