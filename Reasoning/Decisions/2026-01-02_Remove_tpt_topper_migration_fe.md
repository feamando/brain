---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-remove-tpt-topper-migration-fe
$type: project
$version: 1
$created: '2026-01-22T08:31:01.929808Z'
$updated: '2026-01-30T10:28:13.607972'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.929808Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Remove Tpt Topper Migration Fe
$orphan_reason: pending_enrichment
---

# Decision: Remove tpt_topper_migration feature flag

**Date:** 2026-01-02
**Source:** GitHub - commits github_0014
**Confidence:** medium
**Ticket:** TPT-2357

## Decision

Remove tpt_topper_migration feature flag

## Participants

Unknown

## Context

Migration completed, feature flag no longer needed for cleanup

---
*Extracted from GitHub on 2026-01-02*
