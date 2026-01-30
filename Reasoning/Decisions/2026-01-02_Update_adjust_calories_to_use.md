---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-update-adjust-calories-to-use
$type: project
$version: 1
$created: '2026-01-22T08:31:01.847499Z'
$updated: '2026-01-30T10:28:13.396005'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.847499Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Update Adjust Calories To Use
$orphan_reason: pending_enrichment
---

# Decision: Update adjust calories to use new portion options behind feature flag

**Date:** 2026-01-02
**Source:** GitHub - commits github_0002
**Confidence:** medium
**Ticket:** TPT-2518

## Decision

Update adjust calories to use new portion options behind feature flag

## Participants

Unknown

## Context

Gradual rollout of new portion calculation logic with feature flag control

---
*Extracted from GitHub on 2026-01-02*
