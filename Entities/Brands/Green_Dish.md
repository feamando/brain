---
$schema: brain://entity/brand/v1
$id: entity/brand/green-dish
$type: brand
$version: 1
$created: '2026-01-22T08:31:01.305135Z'
$updated: '2026-01-30T10:28:11.989207'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/reactivation
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/reactivation-page
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
  timestamp: '2026-01-22T08:31:01.305135Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/brand/v1
  message: Migrated from v1 to v2 schema
name: Green Dish
$orphan_reason: pending_enrichment
---

# Green_Dish

**Type:** brand
**Created:** 2026-01-02
**Source:** github extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] UI improvements including storage/prep steps, padding fixes, and reactivation page updates (GitHub commits)

## Related Entities

[To be filled]

## Notes

- Created automatically from github analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
