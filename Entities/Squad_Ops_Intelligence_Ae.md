---
$schema: brain://entity/project/v1
$id: entity/project/squad-ops-intelligence-ae
$type: project
$version: 7
$created: '2026-01-22T08:31:01.138146Z'
$updated: '2026-01-30T14:33:55.222735+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/hellofresh
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/data
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/fresh
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/brand/meta
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.138146Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Squad Ops Intelligence Ae
$orphan_reason: no_external_data
---

# Squad: Ops Intelligence Ae

## Metadata
- **Type**: Squad
- **Tribe**: TBD
- **Status**: Active

## Focus & Scope
*Auto-generated stub. Please add details.*

## Codebase Ownership
- [tardis-community](https://github.com/hellofresh/tardis-community)
  - Paths: `pipelines/intl-scm-analytics/scm-business-intelligence/ops-intelligence-ae/**`