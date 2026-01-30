---
$schema: brain://entity/system/v1
$id: entity/system/sem-nb
$type: system
$version: 1
$created: '2026-01-22T08:31:01.692603Z'
$updated: '2026-01-30T10:24:58.158048'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/system/sem-comp
  confidence: 0.9416
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/system/sem-search-engine-marketing
  confidence: 0.9145
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.692603Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Sem Nb
---

# Sem_Nb

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Search Engine Marketing - New Business channel (from: Good Chop: Tests Control Center (TCC))

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
