---
$schema: brain://entity/system/v1
$id: entity/system/api-v2
$type: system
$version: 1
$created: '2026-01-22T08:31:01.753727Z'
$updated: '2026-01-30T10:28:13.123194'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/consumer-core
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/ally
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.753727Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Api V2
$orphan_reason: pending_enrichment
---

# Api-V2

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Technical migration target for Consumer Core squads (from: CMA Squad overview)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Gdocs Context

- [2026-01-02] Migration target for Consumer Core squads across multiple domains (from: CMA Squad overview)


- [2026-01-02] Legacy monolith system maintained by Consumer Core (from: [Active] 2025 Consumer Core Operating Mo)