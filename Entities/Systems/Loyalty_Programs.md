---
$schema: brain://entity/system/v1
$id: entity/system/loyalty-programs
$type: system
$version: 1
$created: '2026-01-22T08:31:01.656187Z'
$updated: '2026-01-22T08:31:01.656187Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/system/free-for-life-program
  confidence: 0.8988
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.656187Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Loyalty Programs
---

# Loyalty_Programs

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Customer retention system to benefit from beverage launch (from: Request- tech support for DACH juices la)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Gdocs Context

- [2026-01-02] Customer retention programs to benefit from beverage launch (from: Request- tech support for DACH juices la)
