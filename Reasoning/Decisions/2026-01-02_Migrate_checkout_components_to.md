---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-migrate-checkout-components-to
$type: project
$version: 1
$created: '2026-01-22T08:31:02.147257Z'
$updated: '2026-01-30T10:28:14.154272'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:02.147257Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Migrate Checkout Components To
$orphan_reason: pending_enrichment
---

# Decision: Migrate checkout components to use useActivationCheckoutSkuPricing hook

**Date:** 2026-01-02
**Source:** GitHub - commits github_0007
**Confidence:** medium
**Ticket:** TPT-2362

## Decision

Migrate checkout components to use useActivationCheckoutSkuPricing hook

## Participants

Unknown

## Context

Standardize pricing logic across checkout components for consistency and maintainability

---
*Extracted from GitHub on 2026-01-02*
