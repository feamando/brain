---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-remove-statsig-for-factor-form
$type: project
$version: 1
$created: '2026-01-22T08:31:01.984195Z'
$updated: '2026-01-30T10:28:13.749703'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.984195Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Remove Statsig For Factor Form
$orphan_reason: pending_enrichment
---

# Decision: Remove Statsig for Factor Form OTP configuration

**Date:** 2026-01-02
**Source:** GitHub - commits github_0019
**Confidence:** medium
**Ticket:** RTEVMS-2274

## Decision

Remove Statsig for Factor Form OTP configuration

## Participants

Unknown

## Context

Moving to direct configuration instead of feature flag service

---
*Extracted from GitHub on 2026-01-02*
