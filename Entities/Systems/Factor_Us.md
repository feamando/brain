---
$schema: brain://entity/system/v1
$id: entity/system/factor-us
$type: system
$version: 1
$created: '2026-01-22T08:31:01.756808Z'
$updated: '2026-01-30T10:28:13.151391'
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
  target: entity/project/meal-selection
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/mega
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/mark
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
  timestamp: '2026-01-22T08:31:01.756808Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Factor Us
$orphan_reason: pending_enrichment
---

# Factor_Us

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Target brand for meal selection and signup (from: Spike - Precheckout Meal Selection FJ)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:50*

## Gdocs Context

- [2026-01-02] Market receiving priority for Penguin personalization rollout and specific tech requirements (from: 2026 Yearly Plan - Consumer Mega-Allianc)
