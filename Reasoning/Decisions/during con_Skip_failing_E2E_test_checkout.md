---
$schema: brain://entity/project/v1
$id: entity/project/during-con-skip-failing-e2e-test-checkout
$type: project
$version: 1
$created: '2026-01-22T08:31:02.032114Z'
$updated: '2026-01-30T10:28:13.881876'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:02.032114Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: During Con Skip Failing E2E Test Checkout
$orphan_reason: pending_enrichment
---

# Decision: Skip failing E2E test checkoutWithTrialBoxWithCutsSelection.spec.ts to unblock PR

**Date:** during con
**Source:** Slack - #squad-nv-good-chop
**Confidence:** high


## Decision

Skip failing E2E test checkoutWithTrialBoxWithCutsSelection.spec.ts to unblock PR

## Participants

UR4A299NX, U03UCPY6MHQ

## Context

Test was consistently failing and blocking PR #54289, will be fixed and unskipped later

---
*Extracted from Slack on 2026-01-02*
