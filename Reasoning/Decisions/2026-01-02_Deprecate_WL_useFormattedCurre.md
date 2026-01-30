---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-deprecate-wl-useformattedcurre
$type: project
$version: 1
$created: '2026-01-22T08:31:01.985214Z'
$updated: '2026-01-30T10:28:13.751951'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.985214Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Deprecate Wl Useformattedcurre
$orphan_reason: pending_enrichment
---

# Decision: Deprecate WL useFormattedCurrency util

**Date:** 2026-01-02
**Source:** GitHub - commits github_0013
**Confidence:** medium
**Ticket:** TPT-2357

## Decision

Deprecate WL useFormattedCurrency util

## Participants

Unknown

## Context

Consolidate currency formatting utilities to reduce duplication

---
*Extracted from GitHub on 2026-01-02*
