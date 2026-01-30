---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-remove-suspense-to-disable-ske
$type: project
$version: 1
$created: '2026-01-22T08:31:01.813752Z'
$updated: '2026-01-30T10:28:13.310104'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.813752Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Remove Suspense To Disable Ske
$orphan_reason: pending_enrichment
---

# Decision: Remove Suspense to disable skeleton display

**Date:** 2026-01-02
**Source:** GitHub - commits github_0021
**Confidence:** medium
**Ticket:** TPT-2283

## Decision

Remove Suspense to disable skeleton display

## Participants

Unknown

## Context

Skeleton display was causing undesired UX behavior

---
*Extracted from GitHub on 2026-01-02*
