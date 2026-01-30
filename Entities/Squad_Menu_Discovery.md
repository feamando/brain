---
$schema: brain://entity/project/v1
$id: entity/project/squad-menu-discovery
$type: project
$version: 1
$created: '2026-01-22T08:31:01.150433Z'
$updated: '2026-01-30T10:22:34.997629'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/person/elisa-marku
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/brandon-donato-long
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/elisa-marku
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.150433Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.170567+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Menu Discovery
---

# Squad: Menu Discovery

## Metadata
- **Type**: Squad
- **Tribe**: Shopping Journey
- **Slack**: `#squad-menu-discovery`
- **PM**: [[Elisa Marku]]
- **EM**: [[Brandon Donato-Long]]
- **KPI (Q1 2026)**: Menu Add-to-Cart Rate

## Focus & Scope
Responsible for Menu Discovery within the Shopping Journey tribe.

## Resources
