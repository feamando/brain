---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-skip-pcs-call-for-otp-users
$type: project
$version: 1
$created: '2026-01-22T08:31:01.829723Z'
$updated: '2026-01-30T15:14:17.148278'
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
  timestamp: '2026-01-22T08:31:01.829723Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Skip Pcs Call For Otp Users
---

# Decision: Skip PCS call for OTP users

**Date:** 2026-01-02
**Source:** GitHub - commits github_0011
**Confidence:** medium
**Ticket:** GOC-3357

## Decision

Skip PCS call for OTP users

## Participants

Unknown

## Context

Optimization for one-time purchase users who don't need subscription-related PCS calls

---
*Extracted from GitHub on 2026-01-02*
