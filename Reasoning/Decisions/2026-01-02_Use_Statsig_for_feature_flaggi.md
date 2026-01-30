---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-use-statsig-for-feature-flaggi
$type: project
$version: 1
$created: '2026-01-22T08:31:01.934153Z'
$updated: '2026-01-30T10:28:13.621422'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.934153Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Use Statsig For Feature Flaggi
$orphan_reason: pending_enrichment
---

# Decision: Use Statsig for feature flagging OTP and plan switcher features

**Date:** 2026-01-02
**Source:** GitHub - commits github_0005
**Confidence:** medium
**Ticket:** MIO-60

## Decision

Use Statsig for feature flagging OTP and plan switcher features

## Participants

Unknown

## Context

Centralized feature flag management with local storage override capability

---
*Extracted from GitHub on 2026-01-02*
