---
$schema: brain://entity/project/v1
$id: entity/project/first-thre-skip-failing-cypress-test-chec
$type: project
$version: 1
$created: '2026-01-22T08:31:01.989643Z'
$updated: '2026-01-30T10:28:13.763088'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.989643Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: First Thre Skip Failing Cypress Test Chec
$orphan_reason: pending_enrichment
---

# Decision: Skip failing Cypress test checkoutWithTwoWeekCadence.spec.ts on master to unblock PRs

**Date:** First thre
**Source:** Slack - #squad-nv-good-chop
**Confidence:** high


## Decision

Skip failing Cypress test checkoutWithTwoWeekCadence.spec.ts on master to unblock PRs

## Participants

U03EN3N4KM4

## Context

Test was persistently failing on master and blocking multiple PRs from merging

---
*Extracted from Slack on 2026-01-02*
