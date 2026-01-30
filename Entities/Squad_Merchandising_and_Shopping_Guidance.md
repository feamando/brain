---
$schema: brain://entity/project/v1
$id: entity/project/squad-merchandising-and-shopping-guidance
$type: project
$version: 1
$created: '2026-01-22T08:31:01.243032Z'
$updated: '2026-01-30T10:22:43.346720'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/person/laura-mneimneh
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/person/shruti-patil
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/laura-mneimneh
  confidence: 1.0
  last_verified: '2026-01-30'
- type: related_to
  target: entity/project/shruti-patil
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.243032Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.342791+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Merchandising And Shopping Guidance
---

# Squad: Merchandising & Shopping Guidance

## Metadata
- **Type**: Squad
- **Tribe**: Shopping Journey
- **Slack**: `#squad-merchandising`
- **PM**: [[Laura Mneimneh]]
- **EM**: [[Shruti Patil]]
- **KPI (Q1 2026)**: Merchandising Component  Add-to-Cart Rate

## Focus & Scope
Responsible for Merchandising & Shopping Guidance within the Shopping Journey tribe.

## Resources
