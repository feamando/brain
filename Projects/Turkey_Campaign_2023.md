---
$schema: brain://entity/project/v1
$id: entity/project/turkey-campaign-2023
$type: project
$version: 1
$created: '2026-01-22T08:31:00.941130Z'
$updated: '2026-01-22T08:31:00.941130Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/project/turkey-campaign-codes
  confidence: 0.9747
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.92
- type: similar_to
  target: entity/project/turkey-campaigns
  confidence: 0.9694
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.92
- type: similar_to
  target: entity/project/turkey-campaign
  confidence: 0.9689
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.92
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.941130Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Turkey Campaign 2023
---

# Turkey_Campaign_2023

**Type:** project
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Multiple turkey-related promo codes (ORGANIC TURKEY, TURKEY ACTIVATION NAE, TURKEY REACTIVATION NAE, TURKEY CODE 2023) (from: Good Chop Marketing Vouchers)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
