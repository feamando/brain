---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-avoid-deprecated-gateway-in-pl
$type: project
$version: 1
$created: '2026-01-22T08:31:01.806389Z'
$updated: '2026-01-30T10:28:13.291054'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.806389Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Avoid Deprecated Gateway In Pl
$orphan_reason: pending_enrichment
---

# Decision: Avoid deprecated gateway in place order hook

**Date:** 2026-01-02
**Source:** GitHub - commits github_0018
**Confidence:** medium
**Ticket:** GOC-3222

## Decision

Avoid deprecated gateway in place order hook

## Participants

Unknown

## Context

Removing usage of deprecated gateway to maintain code health and avoid future breaking changes

---
*Extracted from GitHub on 2026-01-02*
