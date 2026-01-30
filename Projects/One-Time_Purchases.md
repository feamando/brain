---
$schema: brain://entity/project/v1
$id: entity/project/one-time-purchases
$type: project
$version: 1
$created: '2026-01-22T08:31:00.952159Z'
$updated: '2026-01-22T08:31:00.952159Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/project/one-time-purchases-otp
  confidence: 0.9208
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.92
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.952159Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: One Time Purchases
---

# One-Time_Purchases

**Type:** project
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Delayed to W2'2026 (from: GoC H1 2026 Product Prioritization - WIP)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
