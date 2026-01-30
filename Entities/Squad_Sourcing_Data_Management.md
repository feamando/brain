---
$schema: brain://entity/project/v1
$id: entity/project/squad-sourcing-data-management
$type: project
$version: 4
$created: '2026-01-22T08:31:01.227671Z'
$updated: '2026-01-30T14:35:10.988761+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.227671Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Squad Sourcing Data Management
---

# Squad: Sourcing Data Management

## Metadata
- **Type**: Squad
- **Tribe**: TBD
- **Status**: Active

## Focus & Scope
*Auto-generated stub. Please add details.*

## Codebase Ownership
- [tardis-community](https://github.com/hellofresh/tardis-community)
  - Paths: `pipelines/ingredient-to-product/strategic-procurement/**`
- [culinary-planning-service](https://github.com/hellofresh/culinary-planning-service)
  - Paths: `**/*skusubstitution/**, **/baml_src/**`