---
$schema: brain://entity/brand/v1
$id: entity/brand/hfnl-hellofresh-netherlands
$type: brand
$version: 1
$created: '2026-01-22T08:31:01.294527Z'
$updated: '2026-01-30T10:28:11.964801'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/hellofresh
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/netherlands
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/fresh
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
  timestamp: '2026-01-22T08:31:01.294527Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/brand/v1
  message: Migrated from v1 to v2 schema
name: Hfnl Hellofresh Netherlands
$orphan_reason: pending_enrichment
---

# Hfnl_Hellofresh_Netherlands

**Type:** brand
**Created:** 2026-01-02
**Source:** github extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Plan type switcher added to account settings with feature flag (GitHub commits)

## Related Entities

[To be filled]

## Notes

- Created automatically from github analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
