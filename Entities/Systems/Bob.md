---
$schema: brain://entity/system/v1
$id: entity/system/bob
$type: system
$version: 1
$created: '2026-01-22T08:31:01.668287Z'
$updated: '2026-01-22T08:31:01.668287Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/system/owl
  confidence: 0.8564
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.668287Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Bob
---

# Bob

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] System where refunds work correctly (from: Good Chop tech sync up)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Gdocs Context

- [2026-01-02] Refunds work via this system (from: Good Chop tech sync up)


- [2026-01-02] System where refunds work correctly (from: Good Chop tech sync up)

- [2026-01-02] System where orders are visible and successfully created (from: OTP Topics - 2025/12/29 16:00 CET - Note)

- [2026-01-02] System where orders are visible and successfully created (from: OTP Topics - 2025/12/29 16:00 CET - Note)

- [2026-01-02] Previous system whose behavior is being replicated; agents already trained on its processes (from: [Please Prio] Charge@Checkout OWL: Refun)

- [2026-01-02] System where refunds work correctly; uses same refund service endpoint as Owl Orders tab (from: Refund from Owl for C@C - 2025/12/08 13:)

- [2026-01-02] Current workaround contact for AL issues (from: Beatrice <> Nikita Weekly 1:1 Notes)

- [2026-01-02] Legacy system previously used for charge checkout, currently used as a workaround during AL migration (from: Beatrice:Nikita 1:1 - 2025/12/11 10:01 C)

- [2026-01-02] Platform used for bulk subscription cancellations (from: KN - Reset To Trial Customers)

- [2026-01-02] Attribution system based on vouchers (from: GoC H1 2026 Product Prioritization - WIP)