---
$schema: brain://entity/person/v1
$id: entity/person/bea
$type: person
$version: 3
$created: '2026-01-22T08:31:01.422252Z'
$updated: '2026-01-30T14:48:56.466360+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/system/good-chop
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
  timestamp: '2026-01-22T08:31:01.422252Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/person/v1
  message: Migrated from v1 to v2 schema
name: Bea
$orphan_reason: no_external_data
---

# Bea

**Type:** person
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Following up on silo visibility (from: Good Chop tech sync up)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:50*
