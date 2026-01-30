---
$schema: brain://entity/system/v1
$id: entity/system/vms-error-metric
$type: system
$version: 1
$created: '2026-01-22T08:31:01.756364Z'
$updated: '2026-01-30T10:28:13.148568'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/data
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/good-shop
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/nikita
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/evan
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/simon
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.756364Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Vms Error Metric
$orphan_reason: pending_enrichment
---

# Vms_Error_Metric

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Metric being reported on by Simon in extended report to include Good shop and TPT data (from: Series-evanikita-11.md)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:50*

## Gdocs Context

- [2026-01-02] Metric being reported on by Simon in extended report to include Good shop and TPT data (from: Series-evanikita-11.md)
