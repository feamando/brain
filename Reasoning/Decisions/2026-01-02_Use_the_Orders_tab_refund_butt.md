---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-use-the-orders-tab-refund-butt
$type: project
$version: 1
$created: '2026-01-22T08:31:02.171068Z'
$updated: '2026-01-30T10:28:14.211275'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:02.171068Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Use The Orders Tab Refund Butt
$orphan_reason: pending_enrichment
---

# Decision: Use the Orders tab refund button instead of error reporting tab for refunds

**Date:** 2026-01-02
**Source:** GDocs - Refund from Owl for C@C - 2025/12/08 13:15 CET - N
**Confidence:** medium


## Decision

Use the Orders tab refund button instead of error reporting tab for refunds

## Participants

Shishir Mishra, Beatrice Dimarucut

## Context

The Orders tab uses the updated refund service endpoint like Bob, while error reporting may use an older RabbitMQ topic method

---
*Extracted from GDocs on 2026-01-02*
