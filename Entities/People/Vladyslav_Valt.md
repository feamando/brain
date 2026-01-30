---
$schema: brain://entity/person/v1
$id: entity/person/vladyslav-valt
$type: person
$version: 1
$created: '2026-01-22T08:31:01.402327Z'
$updated: '2026-01-30T14:58:48.923316'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: otp
  confidence: 0.65
  source: body_extraction
  last_verified: '2026-01-30'
- type: maintains
  target: entity/system/mss-cart-service
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: maintains
  target: entity/system/vms-variety-meal-service
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: maintains
  target: entity/system/bob-intfood
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.402327Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/person/v1
  message: Migrated from v1 to v2 schema
name: Vladyslav Valt
---

# Vladyslav_Valt

**Type:** person
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Main Back-end PIC (from: PRD: Enabling One-Time-Purchase (OTP) Ca)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
