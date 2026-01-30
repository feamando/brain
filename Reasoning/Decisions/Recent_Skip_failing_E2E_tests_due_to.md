---
$schema: brain://entity/project/v1
$id: entity/project/recent-skip-failing-e2e-tests-due-to
$type: project
$version: 1
$created: '2026-01-22T08:31:01.941045Z'
$updated: '2026-01-30T10:28:13.638466'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.941045Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Recent Skip Failing E2E Tests Due To
$orphan_reason: pending_enrichment
---

# Decision: Skip failing E2E tests due to staging rollout impact

**Date:** Recent
**Source:** Slack - #squad-nv-pet-food
**Confidence:** high


## Decision

Skip failing E2E tests due to staging rollout impact

## Participants

U03UN2C25UL, U01KNE98YLR

## Context

Tests failing due to brand rollout on staging, blocking multiple PRs

---
*Extracted from Slack on 2026-01-02*
