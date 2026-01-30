---
$schema: brain://entity/system/v1
$id: entity/system/katana
$type: system
$version: 1
$created: '2026-01-22T08:31:01.642855Z'
$updated: '2026-01-30T15:14:16.790994'
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
  timestamp: '2026-01-22T08:31:01.642855Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Katana
---

# Katana

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Service that should receive events from Kafka topics, experiencing rollout issues (from: VMS OTP UAT - Part 2 - 2025/12/30 09:27 )

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Gdocs Context

- [2026-01-02] System not receiving events from OTP orders, blocking customer product fulfillment (from: OTP Topics - 2025/12/29 16:00 CET - Note)


- [2026-01-02] Not receiving events from OTP, critical blocker for launch (from: OTP Topics - 2025/12/29 16:00 CET - Note)

- [2026-01-02] Only current system that supports required B2B functionality out of the box (from: Connect on CA B2B Shopify Integration - )

- [2026-01-02] Only current system that supports required B2B functionality out of the box (from: Connect on CA B2B Shopify Integration - )

- [2026-01-02] US integration that needs to be stripped out for Canadian implementation (from: HF CA B2B - 2025/12/17 16:46 CET - Notes)

- [2026-01-02] Technical system mentioned for simplification (from: PRD: Enabling One-Time-Purchase (OTP) Ca)

- [2026-01-02] System mentioned for simplification (from: PRD: Enabling One-Time-Purchase (OTP) Ca)

- [2026-01-02] Technical system mentioned for simplification (from: PRD: Enabling One-Time-Purchase (OTP) Ca)

- [2026-01-02] System mentioned for simplification (from: PRD: Enabling One-Time-Purchase (OTP) Ca)

- [2026-01-02] System mentioned in OTP order traceability ticket (from: The Pets Table - 2026 BP v1 (Internal))