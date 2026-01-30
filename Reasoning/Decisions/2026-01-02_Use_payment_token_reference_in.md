---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-use-payment-token-reference-in
$type: project
$version: 1
$created: '2026-01-22T08:31:01.866305Z'
$updated: '2026-01-30T15:14:17.228491'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: otp
  confidence: 0.65
  source: body_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.866305Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Use Payment Token Reference In
---

# Decision: Use payment token reference instead of storing payment details

**Date:** 2026-01-02
**Source:** GDocs - PRD: Enabling One-Time-Purchase (OTP) Capabilities
**Confidence:** medium


## Decision

Use payment token reference instead of storing payment details

## Participants

Not specified

## Context

Payment details are never stored in the HF system for security compliance

---
*Extracted from GDocs on 2026-01-02*
