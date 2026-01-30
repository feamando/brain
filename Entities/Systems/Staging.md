---
$schema: brain://entity/system/v1
$id: entity/system/staging
$type: system
$version: 1
$created: '2026-01-22T08:31:01.649475Z'
$updated: '2026-01-30T10:24:58.084963'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/system/live
  confidence: 0.918
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.649475Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Staging
---

# Staging

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Environment where configuration was correct and menus synced from live (from: Tech Sync Good Chop - 2025/12/17 21:00 C)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:50*
