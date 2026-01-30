---
$schema: brain://entity/project/v1
$id: entity/project/squad-exp-squad
$type: project
$version: 7
$created: '2026-01-22T08:31:01.124612Z'
$updated: '2026-01-30T14:33:42.794744+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.124612Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Squad Exp Squad
---

# Squad: Exp Squad

## Metadata
- **Type**: Squad
- **Tribe**: TBD
- **Status**: Active

## Focus & Scope
*Auto-generated stub. Please add details.*

## Codebase Ownership
- [tardis-community](https://github.com/hellofresh/tardis-community)
  - Paths: `pipelines/adtech/experimentation-core/**`
- [web](https://github.com/hellofresh/web)
  - Paths: `/app/data-access/experiment, /app/e2e-tests/pr/experimentation-events, /app/features/aa-test-feature, /app/libs/experiment, /app/libs/experimentation-poc-statsig (+6 more)`