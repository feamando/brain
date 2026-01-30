---
$schema: brain://entity/project/v1
$id: entity/project/decisions
$type: project
$version: 1
$created: '2026-01-22T08:31:01.086343Z'
$updated: '2026-01-30T10:19:58.669142'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/project/fulfilment
  confidence: 0.9595
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/project/operations-enablement
  confidence: 0.9336
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.086343Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Decisions
---

# Decisions

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
