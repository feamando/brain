---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-redirect-active-subscription-u
$type: project
$version: 1
$created: '2026-01-22T08:31:01.828353Z'
$updated: '2026-01-30T10:28:13.346792'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.828353Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Redirect Active Subscription U
$orphan_reason: pending_enrichment
---

# Decision: Redirect active subscription users from reactivation page

**Date:** 2026-01-02
**Source:** GitHub - commits github_0009
**Confidence:** medium
**Ticket:** TPT-2413

## Decision

Redirect active subscription users from reactivation page

## Participants

Unknown

## Context

Prevent users with active subscriptions from accessing plan reactivation flow

---
*Extracted from GitHub on 2026-01-02*
