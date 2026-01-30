---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-separate-payment-processing-fo
$type: project
$version: 1
$created: '2026-01-22T08:31:01.908436Z'
$updated: '2026-01-30T15:14:17.318719'
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
  timestamp: '2026-01-22T08:31:01.908436Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Separate Payment Processing Fo
---

# Decision: Separate payment processing for OTP similar to HelloFresh Market (HFM)

**Date:** 2026-01-02
**Source:** GDocs - PRD: Enabling One-Time-Purchase (OTP) Capabilities
**Confidence:** medium


## Decision

Separate payment processing for OTP similar to HelloFresh Market (HFM)

## Participants

Not specified

## Context

Customers ordering both subscription and OTP items need separate payment handling

---
*Extracted from GDocs on 2026-01-02*
