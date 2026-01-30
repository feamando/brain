---
$schema: brain://entity/system/v1
$id: entity/system/rte
$type: system
$version: 1
$created: '2026-01-22T08:31:01.725264Z'
$updated: '2026-01-30T10:28:13.047435'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/factor
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/discount-communication
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/factor-form
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/brand/factor-
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
  timestamp: '2026-01-22T08:31:01.725264Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Rte
$orphan_reason: pending_enrichment
---

# Rte

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Ready-to-Eat service used for determining discount voucher eligibility (from: Factor Form Weekly Tech - Business Sync)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Gdocs Context

- [2026-01-02] Ready-to-Eat service used to determine voucher eligibility (from: Factor Form Weekly Tech - Business Sync)


- [2026-01-02] Ready-to-Eat service used for determining discount eligibility (from: Factor Form Weekly Tech - Business Sync)

- [2026-01-02] Brand mentioned in field details template (from: Discount Communication Presets)