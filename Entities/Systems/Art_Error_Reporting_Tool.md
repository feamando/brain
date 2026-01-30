---
$schema: brain://entity/system/v1
$id: entity/system/art-error-reporting-tool
$type: system
$version: 1
$created: '2026-01-22T08:31:01.714061Z'
$updated: '2026-01-30T10:28:13.021384'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/person/ally
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/system/checkout
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.714061Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Art Error Reporting Tool
$orphan_reason: pending_enrichment
---

# Art_Error_Reporting_Tool

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Tool that is NOT used for cancellations, clarified during meeting (from: [Please Prio] Charge@Checkout OWL: Refun)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:50*
