---
$schema: brain://entity/brand/v1
$id: entity/brand/global-talent
$type: brand
$version: 1
$created: '2026-01-22T08:31:01.276195Z'
$updated: '2026-01-22T08:31:01.276195Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/brand/activate-talent
  confidence: 0.9453
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.276195Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/brand/v1
  message: Migrated from v1 to v2 schema
name: Global Talent
---

# Global_Talent

**Type:** brand
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Offshore contractor agency with variable commission rates by country (from: Offshore Contractor Agencies)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
