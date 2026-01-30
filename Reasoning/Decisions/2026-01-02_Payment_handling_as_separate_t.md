---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-payment-handling-as-separate-t
$type: project
$version: 1
$created: '2026-01-22T08:31:02.124427Z'
$updated: '2026-01-30T15:14:18.294759'
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
  timestamp: '2026-01-22T08:31:02.124427Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Payment Handling As Separate T
---

# Decision: Payment handling as separate transaction from subscription

**Date:** 2026-01-02
**Source:** GDocs - PRD: Enabling One-Time-Purchase (OTP) Capabilities
**Confidence:** medium


## Decision

Payment handling as separate transaction from subscription

## Participants

Not specified

## Context

Similar to how HelloFresh Market (HFM) is currently charged, OTP would be a separate payment for customers who may also be ordering a regular subscription box

---
*Extracted from GDocs on 2026-01-02*
