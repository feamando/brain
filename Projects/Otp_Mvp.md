---
$schema: brain://entity/project/v1
$id: entity/project/otp-mvp
$type: project
$version: 1
$created: '2026-01-22T08:31:00.994997Z'
$updated: '2026-01-30T10:19:32.084820'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: otp
  confidence: 0.7
  source: body_extraction
  last_verified: '2026-01-30'
- type: similar_to
  target: entity/project/otp-mvp-one-time-purchase
  confidence: 0.9239
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.994997Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Otp Mvp
---

# Otp_Mvp

**Type:** project
**Created:** 2026-01-02
**Source:** slack extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] One-time purchase MVP project requiring escalation and priority (#tribe-new-ventures-product)

## Related Entities

[To be filled]

## Notes

- Created automatically from slack analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
