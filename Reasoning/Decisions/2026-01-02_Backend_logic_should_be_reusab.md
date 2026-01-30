---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-backend-logic-should-be-reusab
$type: project
$version: 1
$created: '2026-01-22T08:31:01.864001Z'
$updated: '2026-01-30T15:14:17.223313'
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
  timestamp: '2026-01-22T08:31:01.864001Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Backend Logic Should Be Reusab
---

# Decision: Backend logic should be reusable between web and mobile

**Date:** 2026-01-02
**Source:** GDocs - Beatrice:Nikita 1:1 - 2025/12/11 10:01 CET - Notes
**Confidence:** medium


## Decision

Backend logic should be reusable between web and mobile

## Participants

Unknown

## Context

New code is being written for both web and app simultaneously, allowing for code reuse including all backend logic

---
*Extracted from GDocs on 2026-01-02*
