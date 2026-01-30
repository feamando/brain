---
$schema: brain://entity/system/v1
$id: entity/system/live
$type: system
$version: 1
$created: '2026-01-22T08:31:01.603503Z'
$updated: '2026-01-30T10:24:58.073770'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/system/staging
  confidence: 0.918
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/system/pcs-v2
  confidence: 0.8573
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/system/search
  confidence: 0.8528
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.603503Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Live
---

# Live

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Production environment missing necessary configuration setting (from: Tech Sync Good Chop - 2025/12/17 21:00 C)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:50*
