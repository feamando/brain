---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-temporarily-revert-reactivatio
$type: project
$version: 1
$created: '2026-01-22T08:31:01.957924Z'
$updated: '2026-01-30T15:14:17.420197'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: nikita
  confidence: 0.65
  source: body_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.957924Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Temporarily Revert Reactivatio
---

# Decision: Temporarily revert reactivation page to old pricing endpoint

**Date:** 2026-01-02
**Source:** GDocs - Maria:Nikita 1:1 - 2025/12/16 17:59 CET - Notes by
**Confidence:** medium


## Decision

Temporarily revert reactivation page to old pricing endpoint

## Participants

Nikita Gorshkov

## Context

New pricing endpoint incorrectly flags vouchers as fraudulent for multi-subscription users; need to secure value before holidays despite creating future overhead

---
*Extracted from GDocs on 2026-01-02*
