---
$schema: brain://entity/squad/v1
$id: entity/squad/good-chop-squad
$type: squad
$version: 1
$created: '2026-01-22T08:31:01.322001Z'
$updated: '2026-01-30T10:22:52.556181'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/squad/cma
  confidence: 0.8081
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/tam
  confidence: 0.8454
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/squad/new-ventures-systems-squad
  confidence: 0.8338
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/squad/goodchop-squad
  confidence: 0.8788
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/squad/new-ventures-systems-squad-nvs
  confidence: 0.8358
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/squad/squad-nv-good-chop
  confidence: 0.8467
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.322001Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/squad/v1
  message: Migrated from v1 to v2 schema
name: Good Chop Squad
---

# Good_Chop_Squad

**Type:** squad
**Created:** 2026-01-02
**Source:** slack extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Squad working on Good Chop brand, completed peak readiness documentation (#tribe-new-ventures-leads-internal)

## Related Entities

[To be filled]

## Notes

- Created automatically from slack analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
