---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-gate-50-off-discount-for-facto-3
$type: project
$version: 1
$created: '2026-01-22T08:31:02.028491Z'
$updated: '2026-01-30T10:28:13.871117'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:02.028491Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Gate 50 Off Discount For Facto 3
$orphan_reason: pending_enrichment
---

# Decision: Gate 50% off discount for Factor Actives with $65+ MOV, with fallback logic

**Date:** 2026-01-02
**Source:** GDocs - Factor Form Weekly Tech - Business Sync
**Confidence:** medium


## Decision

Gate 50% off discount for Factor Actives with $65+ MOV, with fallback logic

## Participants

Laura Loughran, Jordon Smith

## Context

If RTE active, apply special voucher; if not RTE active, default back to regular voucher (40% off)

---
*Extracted from GDocs on 2026-01-02*
