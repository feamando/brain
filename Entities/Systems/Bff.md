---
$schema: brain://entity/system/v1
$id: entity/system/bff
$type: system
$version: 1
$created: '2026-01-22T08:31:01.722151Z'
$updated: '2026-01-30T10:28:13.040446'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/new-ventures
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/mobile-app
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/new-ventures-tribe
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
  timestamp: '2026-01-22T08:31:01.722151Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Bff
$orphan_reason: pending_enrichment
---

# Bff

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Backend-for-Frontend migration nearly complete in mobile app (from: New Ventures Tribe - Weekly Standup Note)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:50*

## Gdocs Context

- [2026-01-02] Backend for Frontend migration nearly complete in mobile app (from: New Ventures Tribe - Weekly Standup Note)


- [2026-01-02] Backend for Frontend migration in mobile app (historical) (from: New Ventures Tribe - Weekly Standup Note)