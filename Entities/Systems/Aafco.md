---
$schema: brain://entity/system/v1
$id: entity/system/aafco
$type: system
$version: 1
$created: '2026-01-22T08:31:01.729381Z'
$updated: '2026-01-30T10:28:13.057583'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/the-pets-table
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/eric
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
  timestamp: '2026-01-22T08:31:01.729381Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Aafco
$orphan_reason: pending_enrichment
---

# Aafco

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Association of American Feed Control Officials - nutritional standards authority (from: Notes - The Pets Table - Weekly Check-in)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Github Context

- [2026-01-02] Compliance sections added for nutritional standards (GitHub commits)
