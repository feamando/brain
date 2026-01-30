---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-otp-launch-scheduled-for-w02-t-2
$type: project
$version: 1
$created: '2026-01-22T08:31:01.927486Z'
$updated: '2026-01-30T15:14:17.357289'
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
  timestamp: '2026-01-22T08:31:01.927486Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Otp Launch Scheduled For W02 T 2
---

# Decision: OTP Launch scheduled for W02 (to 90% of users)

**Date:** 2026-01-02
**Source:** GDocs - Notes: Hamed <> Nikita 1:1
**Confidence:** medium


## Decision

OTP Launch scheduled for W02 (to 90% of users)

## Participants

Unknown

## Context

Evaluated multiple launch options (W50, W51 at 90%, W51 at 10%, W02). Chose W02 to mitigate risk with dev availability, avoid breaking Factor during holidays, and launch before peak season. Feature flag to turn on in W02 but everything ready by EOY.

---
*Extracted from GDocs on 2026-01-02*
