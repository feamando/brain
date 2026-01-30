---
$schema: brain://entity/project/v1
$id: entity/project/bnl-migration
$type: project
$version: 9
$created: '2026-01-22T08:31:00.988495Z'
$updated: '2026-01-30T14:50:43.150765+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/person/ally
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/system/slack
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/system/it-cap
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.988495Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Bnl Migration
$orphan_reason: no_external_data
---

# Bnl_Migration

**Type:** project
**Created:** 2026-01-02
**Source:** slack extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Migration project attributed to ACT-A-8 KR for IT capitalization (#tribe-new-ventures-leads-internal)

## Related Entities

[To be filled]

## Notes

- Created automatically from slack analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
