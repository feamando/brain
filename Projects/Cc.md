---
$schema: brain://entity/project/v1
$id: entity/project/cc
$type: project
$version: 8
$created: '2026-01-22T08:31:01.030601Z'
$updated: '2026-01-30T14:31:57.110505+00:00'
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
  target: entity/system/good-chop
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
  target: entity/system/pricing-service
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.030601Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Cc
$orphan_reason: no_external_data
---

# Cc

**Type:** project
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Feature with refund issues and pricing service blockers, currently at 10% rollout (from: Good Chop tech sync up)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:50*

## Gdocs Context

- [2026-01-02] Customer at Checkout project, currently at 10% performance, blocked by payment issues (from: Good Chop tech sync up)


- [2026-01-02] Abbreviation for Charge at Checkout experiment mentioned in meeting title (from: Refund from Owl for C@C - 2025/12/08 13:)