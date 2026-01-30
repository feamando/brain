---
$schema: brain://entity/project/v1
$id: entity/project/plan-types-tpt-does-not-use-plan-type-as
$type: project
$version: 1
$created: '2026-01-22T08:31:02.000995Z'
$updated: '2026-01-30T10:28:13.792311'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:02.000995Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Plan Types Tpt Does Not Use Plan Type As
$orphan_reason: pending_enrichment
---

# Decision: TPT does not use plan_type as a separate subscription-level entity; it's baked into SKU

**Date:** Plan types
**Source:** Slack - #tribe-new-ventures-product
**Confidence:** high


## Decision

TPT does not use plan_type as a separate subscription-level entity; it's baked into SKU

## Participants

U03TY4YJU4X, U03UMPD2NNS

## Context

Clarifying data model differences between brands after PA reported plan_types aren't used at subscription level

---
*Extracted from Slack on 2026-01-02*
