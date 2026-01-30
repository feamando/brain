---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-remove-storage-values-for-fact
$type: project
$version: 1
$created: '2026-01-22T08:31:01.833182Z'
$updated: '2026-01-30T10:28:13.359294'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.833182Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Remove Storage Values For Fact
$orphan_reason: pending_enrichment
---

# Decision: Remove storage values for Factor Form OTP

**Date:** 2026-01-02
**Source:** GitHub - commits github_0009
**Confidence:** medium
**Ticket:** RTEVMS-2291

## Decision

Remove storage values for Factor Form OTP

## Participants

Unknown

## Context

Clean up storage implementation for OTP checkout flow

---
*Extracted from GitHub on 2026-01-02*
