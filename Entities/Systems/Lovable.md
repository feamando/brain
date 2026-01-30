---
$schema: brain://entity/system/v1
$id: entity/system/lovable
$type: system
$version: 1
$created: '2026-01-22T08:31:01.734255Z'
$updated: '2026-01-30T10:24:58.360012'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/system/lokalize
  confidence: 0.8738
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/system/tpt-funnel
  confidence: 0.8723
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/system/good-chop
  confidence: 0.8586
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.734255Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Lovable
---

# Lovable

**Type:** system
**Created:** 2026-01-02
**Source:** slack extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Development platform being used for TPT funnel revamp (#tribe-new-ventures-product)

## Related Entities

[To be filled]

## Notes

- Created automatically from slack analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
