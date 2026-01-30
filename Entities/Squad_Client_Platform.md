---
$schema: brain://entity/project/v1
$id: entity/project/squad-client-platform
$type: project
$version: 1
$created: '2026-01-22T08:31:01.107593Z'
$updated: '2026-01-30T10:22:30.954565'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/person/priscila-koeck-machado
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/wellington-lima-freire
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/priscila-koeck-machado
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.107593Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.093818+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Client Platform
---

# Squad: Client Platform

## Metadata
- **Type**: Squad
- **Tribe**: Consumer Foundations
- **Slack**: `#squad-client-platform`
- **PM**: [[Priscila Koeck Machado]]
- **EM**: [[Wellington Lima Freire]]
- **KPI (Q1 2026)**: % of consumer squads that deploy a user-impacting feature at least once every 2 weeks

## Focus & Scope
Responsible for Client Platform within the Consumer Foundations tribe.

## Resources
