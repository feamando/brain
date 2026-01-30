---
$schema: brain://entity/brand/v1
$id: entity/brand/mr-and-kn
$type: brand
$version: 1
$created: '2026-01-22T08:31:01.278531Z'
$updated: '2026-01-30T10:28:11.930674'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/charge-at-checkout
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/ally
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/system/checkout
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/system/slack
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.278531Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/brand/v1
  message: Migrated from v1 to v2 schema
name: Mr And Kn
$orphan_reason: pending_enrichment
---

# Mr_And_Kn

**Type:** brand
**Created:** 2026-01-02
**Source:** slack extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Brands affected by initial order deprecation blocking Charge at Checkout (#squad-nv-good-chop)

## Related Entities

[To be filled]

## Notes

- Created automatically from slack analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
