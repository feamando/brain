---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-client-side-only-mounting-for
$type: project
$version: 1
$created: '2026-01-22T08:31:02.037006Z'
$updated: '2026-01-30T10:28:13.895033'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:02.037006Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Client Side Only Mounting For
$orphan_reason: pending_enrichment
---

# Decision: Client-side only mounting for PetInfoHeader

**Date:** 2026-01-02
**Source:** GitHub - commits github_0006
**Confidence:** medium
**Ticket:** TPT-2440

## Decision

Client-side only mounting for PetInfoHeader

## Participants

Unknown

## Context

Ensuring PetInfoHeader component mounts only on client-side to prevent SSR issues

---
*Extracted from GitHub on 2026-01-02*
