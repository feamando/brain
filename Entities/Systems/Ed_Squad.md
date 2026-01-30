---
$schema: brain://entity/system/v1
$id: entity/system/ed-squad
$type: system
$version: 1
$created: '2026-01-22T08:31:01.641500Z'
$updated: '2026-01-22T08:31:01.641500Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/system/md-squad
  confidence: 0.8715
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.641500Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Ed Squad
---

# Ed_Squad

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Squad that incorporated Factor Tech incremental asks into prioritization (from: 2026 Yearly Plan - Consumer Mega-Allianc)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:50*

## Gdocs Context

- [2026-01-02] Squad where Factor Tech incremental asks were pulled into prioritization (from: 2026 Yearly Plan - Consumer Mega-Allianc)
