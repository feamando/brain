---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-migrate-price-selector-to-use
$type: project
$version: 1
$created: '2026-01-22T08:31:02.153522Z'
$updated: '2026-01-30T10:28:14.168983'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:02.153522Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Migrate Price Selector To Use
$orphan_reason: pending_enrichment
---

# Decision: Migrate price selector to use price endpoint

**Date:** 2026-01-02
**Source:** GitHub - commits github_0019
**Confidence:** medium
**Ticket:** GOC-3276

## Decision

Migrate price selector to use price endpoint

## Participants

Unknown

## Context

Standardize price data retrieval through dedicated endpoint

---
*Extracted from GitHub on 2026-01-02*
