---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-add-validation-to-prevent-otp
$type: project
$version: 1
$created: '2026-01-22T08:31:02.111921Z'
$updated: '2026-01-30T10:28:14.078475'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:02.111921Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Add Validation To Prevent Otp
$orphan_reason: pending_enrichment
---

# Decision: Add validation to prevent OTP from being added by default

**Date:** 2026-01-02
**Source:** GitHub - commits github_0010
**Confidence:** medium
**Ticket:** RTEVMS-2342

## Decision

Add validation to prevent OTP from being added by default

## Participants

Unknown

## Context

Hotfix to ensure OTP is only added when explicitly selected by user

---
*Extracted from GitHub on 2026-01-02*
