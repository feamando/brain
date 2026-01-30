---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-extend-dashboard-bundles-logic
$type: project
$version: 1
$created: '2026-01-22T08:31:01.955988Z'
$updated: '2026-01-30T10:28:13.677566'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.955988Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Extend Dashboard Bundles Logic
$orphan_reason: pending_enrichment
---

# Decision: Extend dashboard bundles logic to show OTP/subscription selection modal similar to credit page

**Date:** 2026-01-02
**Source:** GDocs - VMS OTP UAT - Part 2 - 2025/12/30 09:27 EST - Note
**Confidence:** medium


## Decision

Extend dashboard bundles logic to show OTP/subscription selection modal similar to credit page

## Participants

Edwin Torres, Hamed Karimian

## Context

Current dashboard bundles section only affects subscription orders, needs to support OTP orders

---
*Extracted from GDocs on 2026-01-02*
