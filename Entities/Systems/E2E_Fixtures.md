---
$schema: brain://entity/system/v1
$id: entity/system/e2e-fixtures
$type: system
$version: 1
$created: '2026-01-22T08:31:01.687439Z'
$updated: '2026-01-30T10:28:12.951446'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/data
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/ally
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/testing
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.687439Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: E2E Fixtures
$orphan_reason: pending_enrichment
---

# E2E_Fixtures

**Type:** system
**Created:** 2026-01-02
**Source:** github extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Updated with perPortion data for portioned products testing (GitHub commits)

## Related Entities

[To be filled]

## Notes

- Created automatically from github analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
