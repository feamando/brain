---
$schema: brain://entity/system/v1
$id: entity/system/sns
$type: system
$version: 2
$created: '2026-01-22T08:31:01.655730Z'
$updated: '2026-01-30T13:58:40.369966+00:00'
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
  timestamp: '2026-01-22T08:31:01.655730Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Sns
$orphan_reason: no_external_data
---

# Sns

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Subscription service with tiered discount structure based on MOV thresholds (from: Factor Form Weekly Tech - Business Sync)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Gdocs Context

- [2026-01-02] Subscription service with tiered discount structure based on MOV (Minimum Order Value) thresholds (from: Factor Form Weekly Tech - Business Sync)


- [2026-01-02] Subscription service with tiered discount structure based on MOV thresholds (from: Factor Form Weekly Tech - Business Sync)

- [2026-01-02] Subscribe and Save model with tiered discounts for first and subsequent boxes (from: Pricing OTP vs. SNS)

- [2026-01-02] Subscribe and Save model offering tiered discounts (40%/20% above MOV, 10% below MOV) (from: Pricing OTP vs. SNS)