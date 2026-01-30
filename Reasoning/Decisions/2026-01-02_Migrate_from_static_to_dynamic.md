---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-migrate-from-static-to-dynamic
$type: project
$version: 1
$created: '2026-01-22T08:31:01.881056Z'
$updated: '2026-01-30T10:28:13.482841'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.881056Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Migrate From Static To Dynamic
$orphan_reason: pending_enrichment
---

# Decision: Migrate from static to dynamic subscription cadence

**Date:** 2026-01-02
**Source:** GitHub - commits github_0019
**Confidence:** medium
**Ticket:** RTEVMS-1950

## Decision

Migrate from static to dynamic subscription cadence

## Participants

Unknown

## Context

Enable more flexible subscription cadence handling

---
*Extracted from GitHub on 2026-01-02*
