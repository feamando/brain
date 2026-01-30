---
$schema: brain://entity/system/v1
$id: entity/system/salesforce
$type: system
$version: 1
$created: '2026-01-22T08:31:01.757247Z'
$updated: '2026-01-30T10:28:13.161671'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/person/ally
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.757247Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Salesforce
$orphan_reason: pending_enrichment
---

# Salesforce

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] CRM system not receiving OTP events (from: OTP Topics - 2025/12/29 16:00 CET - Note)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:50*

## Gdocs Context

- [2026-01-02] Not receiving OTP events, critical blocker for launch (from: OTP Topics - 2025/12/29 16:00 CET - Note)
