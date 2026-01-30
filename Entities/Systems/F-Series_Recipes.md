---
$schema: brain://entity/system/v1
$id: entity/system/f-series-recipes
$type: system
$version: 1
$created: '2026-01-22T08:31:01.710514Z'
$updated: '2026-01-30T10:24:58.321251'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/system/f00002-series
  confidence: 0.8898
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/system/f01905-f01908
  confidence: 0.9316
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.710514Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: F Series Recipes
---

# F-Series_Recipes

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Recipe ID naming convention (F00002, F01907, F01908, F01912, F01928, F01932) (from: [VIEW ONLY] F_ Meal & Add On Database)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
