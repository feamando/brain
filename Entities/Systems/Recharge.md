---
$schema: brain://entity/system/v1
$id: entity/system/recharge
$type: system
$version: 1
$created: '2026-01-22T08:31:01.678549Z'
$updated: '2026-01-30T10:24:58.301617'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/system/elevar
  confidence: 0.869
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/system/hello-connect
  confidence: 0.8586
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.678549Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Recharge
---

# Recharge

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Third-party integration for Shopify projects; Sameer can now manage setup (from: Sameer:Nikita 1:1 - 2025/12/05 15:29 CET)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:50*

## Gdocs Context

- [2026-01-02] Third-party integration for Good Chop project, Sameer can now manage setup (from: Sameer:Nikita 1:1 - 2025/12/05 15:29 CET)


- [2026-01-02] Partner system with issues being resolved for Shopify project (from: Ali:Nikita 1:1 - 2025/12/09 17:47 CET - )