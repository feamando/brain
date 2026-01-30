---
$schema: brain://entity/project/v1
$id: entity/project/squad-observability
$type: project
$version: 7
$created: '2026-01-22T08:31:01.177157Z'
$updated: '2026-01-30T14:34:30.301569+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.177157Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Squad Observability
---

# Squad: Observability

## Metadata
- **Type**: Squad
- **Tribe**: TBD
- **Status**: Active

## Focus & Scope
*Auto-generated stub. Please add details.*

## Codebase Ownership
- [ftcp-core-components](https://github.com/hellofresh/ftcp-core-components)
  - Paths: `argo-cd-applications/templates/metrics.yaml, values/metrics/*, argo-cd-applications/templates/logging.yaml, values/logging/*, argo-cd-applications/templates/grafana-cloud.yaml (+1 more)`