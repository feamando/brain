---
$schema: brain://entity/system/v1
$id: entity/system/sem-comp
$type: system
$version: 1
$created: '2026-01-22T08:31:01.696257Z'
$updated: '2026-01-30T10:24:58.382525'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/system/sem-search-engine-marketing
  confidence: 0.9017
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/system/sem-brand
  confidence: 0.8595
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/system/sem-nb
  confidence: 0.9416
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.696257Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Sem Comp
---

# Sem_Comp

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Search Engine Marketing - Competitor targeting channel (from: Good Chop: Tests Control Center (TCC))

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
