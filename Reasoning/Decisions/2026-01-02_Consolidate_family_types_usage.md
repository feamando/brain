---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-consolidate-family-types-usage
$type: project
$version: 1
$created: '2026-01-22T08:31:02.117290Z'
$updated: '2026-01-30T10:28:14.090879'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:02.117290Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Consolidate Family Types Usage
$orphan_reason: pending_enrichment
---

# Decision: Consolidate family types usage and remove topper references

**Date:** 2026-01-02
**Source:** GitHub - commits github_0012
**Confidence:** medium
**Ticket:** TPT-2357

## Decision

Consolidate family types usage and remove topper references

## Participants

Unknown

## Context

Simplify PetsTable implementation and reduce technical debt

---
*Extracted from GitHub on 2026-01-02*
