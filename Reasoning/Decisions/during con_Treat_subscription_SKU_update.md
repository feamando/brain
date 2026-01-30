---
$schema: brain://entity/project/v1
$id: entity/project/during-con-treat-subscription-sku-update
$type: project
$version: 1
$created: '2026-01-22T08:31:02.002415Z'
$updated: '2026-01-30T10:28:13.803083'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:02.002415Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: During Con Treat Subscription Sku Update
$orphan_reason: pending_enrichment
---

# Decision: Treat subscription SKU update issue as separate initiative rather than bug fix

**Date:** during con
**Source:** Slack - #tribe-new-ventures-internal
**Confidence:** high


## Decision

Treat subscription SKU update issue as separate initiative rather than bug fix

## Participants

U01AKGWGLC8, UE4HG114J

## Context

Investigation revealed the behavior where deliveries don't update SKU when subscription changes is expected behavior, not a bug. Requires customer experience changes to fix.

---
*Extracted from Slack on 2026-01-02*
