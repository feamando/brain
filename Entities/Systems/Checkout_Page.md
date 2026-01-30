---
$schema: brain://entity/system/v1
$id: entity/system/checkout-page
$type: system
$version: 1
$created: '2026-01-22T08:31:01.735675Z'
$updated: '2026-01-30T10:24:58.502286'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/system/checkout-flow
  confidence: 0.887
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.735675Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Checkout Page
---

# Checkout_Page

**Type:** component
**Created:** 2026-01-02
**Source:** github extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Enhanced with OTP attributes and payment error tracking (GitHub commits)

## Related Entities

[To be filled]

## Notes

- Created automatically from github analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
