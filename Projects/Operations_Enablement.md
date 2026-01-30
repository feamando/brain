---
$schema: brain://entity/project/v1
$id: entity/project/operations-enablement
$type: project
$version: 1
$created: '2026-01-22T08:31:00.965894Z'
$updated: '2026-01-30T10:19:40.064349'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/project/decisions
  confidence: 0.9336
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.92
- type: similar_to
  target: entity/project/data
  confidence: 0.9232
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.92
- type: similar_to
  target: entity/project/operations-intl
  confidence: 0.9647
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/project/operations-na
  confidence: 0.949
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/project/fulfilment
  confidence: 0.9492
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.965894Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Operations Enablement
---

# Operations_Enablement

**Type:** project
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Tech team alliance with incoming dependencies (from: [WIP] 2025YP Dependencies Master)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
