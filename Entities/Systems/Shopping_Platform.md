---
$schema: brain://entity/system/v1
$id: entity/system/shopping-platform
$type: system
$version: 1
$created: '2026-01-22T08:31:01.618901Z'
$updated: '2026-01-22T08:31:01.618901Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/system/shopping-experience
  confidence: 0.8864
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.618901Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Shopping Platform
---

# Shopping_Platform

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Platform space requiring multi-subscription support (from: Maria:Nikita 1:1 - 2025/12/16 17:59 CET )

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
