---
$schema: brain://entity/project/v1
$id: entity/project/incomm
$type: project
$version: 1
$created: '2026-01-22T08:31:00.959591Z'
$updated: '2026-01-30T10:09:00.108436'
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
  timestamp: '2026-01-22T08:31:00.959591Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Incomm
---

# InComm Integration

**Status:** Active
**Priority:** Medium
**Owner:** Nikita Gorshkov / Elaine Tobin

## Overview
Retail gift card program integration with InComm. Enables "Transferred Value" (TV) activation and redemption.

## Key Features
- **Custom PINs:** Custom-prefixed PINs for HelloFresh.
- **Reporting:** Merchant name and location data.
- **Error Handling:** Specific timeout/retry logic.

## Stakeholders
- **HelloFresh:** Nikita Gorshkov, Elaine Tobin, Elysa Viti
- **InComm:** Philip Pidoux-Koronya (Relationship), Jacob Gabiam (Solutions)

## Timeline
- **Contracting:** Delayed to Jan 2026 due to legal review cutoff.
- **Launch:** TBD (post-contract).

## Changelog
- **2025-12-08:** Kickoff meeting held. Scope defined. Legal review delayed.

## Gdocs Context

- [2026-01-02] Payment processor and gift card platform provider (from: InComm / HelloFresh Tech Integration  - )

---
*Last updated: 2026-01-02 16:51*


- [2026-01-02] Gift card activation and value management platform provider (from: InComm / HelloFresh Tech Integration  - )

- [2026-01-02] Integration partner for HelloFresh retail gift card program mentioned in email notes (from: CMA Squad overview)