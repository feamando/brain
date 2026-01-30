---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-separate-payment-processing-fo-2
$type: project
$version: 1
$created: '2026-01-22T08:31:02.010638Z'
$updated: '2026-01-30T15:14:17.999096'
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
  timestamp: '2026-01-22T08:31:02.010638Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Separate Payment Processing Fo 2
---

# Decision: Separate payment processing for OTP vs regular subscription boxes

**Date:** 2026-01-02
**Source:** GDocs - PRD: Enabling One-Time-Purchase (OTP) Capabilities
**Confidence:** medium


## Decision

Separate payment processing for OTP vs regular subscription boxes

## Participants

Not specified

## Context

Similar to current HFM charging model to maintain clear transaction separation

---
*Extracted from GDocs on 2026-01-02*
