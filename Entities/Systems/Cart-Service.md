---
$schema: brain://entity/system/v1
$id: entity/system/cart-service
$type: system
$version: 2
$created: '2026-01-22T08:31:01.609579Z'
$updated: '2026-01-30T14:57:00.383267'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: maintained_by
  target: entity/person/nikita-gorshkov
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: maintained_by
  target: entity/person/leo-lee
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.609579Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Cart Service
---

# Cart-Service

**Type:** api
**Created:** 2026-01-02
**Source:** github extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Migration completed, references being cleaned up (GitHub commits)

## Related Entities

[To be filled]

## Notes

- Created automatically from github analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Github Context

- [2026-01-02] Migration with backwards compatibility and tracing implementation (GitHub commits)


- [2026-01-02] Target of Factor Form migration effort (GitHub commits)