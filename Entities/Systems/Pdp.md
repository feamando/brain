---
$schema: brain://entity/system/v1
$id: entity/system/pdp
$type: system
$version: 1
$created: '2026-01-22T08:31:01.694339Z'
$updated: '2026-01-30T15:14:16.888860'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: nikita
  confidence: 0.65
  source: body_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: otp
  confidence: 0.65
  source: body_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.694339Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Pdp
---

# Pdp

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] New design discussed on Nov 7, 2025 (from: Notes: Hamed <> Nikita 1:1)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Gdocs Context

- [2026-01-02] New design discussed (from: Notes: Hamed <> Nikita 1:1)


- [2026-01-02] Product Detail Page serving as master editor for purchase options (from: Factor Form | One Time Purchase)