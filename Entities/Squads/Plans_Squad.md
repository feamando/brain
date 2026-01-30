---
$schema: brain://entity/squad/v1
$id: entity/squad/plans-squad
$type: squad
$version: 1
$created: '2026-01-22T08:31:01.315701Z'
$updated: '2026-01-22T08:31:01.315701Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/squad/goodchop-squad
  confidence: 0.813
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.315701Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/squad/v1
  message: Migrated from v1 to v2 schema
name: Plans Squad
---

# Plans_Squad

**Type:** squad
**Created:** 2026-01-02
**Source:** slack extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Squad that enabled initial orders and will fix Description field issue (#squad-nv-good-chop)

## Related Entities

[To be filled]

## Notes

- Created automatically from slack analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
