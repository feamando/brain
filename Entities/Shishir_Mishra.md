---
$schema: brain://entity/project/v1
$id: entity/project/shishir-mishra
$type: project
$version: 1
$created: '2026-01-22T08:31:01.195700Z'
$updated: '2026-01-22T10:41:35.253288+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/squad-customer-service-experience
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.195700Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.253290+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Shishir Mishra
---

# Shishir Mishra

## Metadata
- **Type**: Person
- **Role**: Product Manager
- **Team**: [[Squad_Customer_Service_Experience]] (Shopping Foundation)

## Context
Product Manager for the Customer Service Experience squad.
