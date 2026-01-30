---
$schema: brain://entity/brand/v1
$id: entity/brand/marley-spoon
$type: brand
$version: 1
$created: '2026-01-22T08:31:01.315269Z'
$updated: '2026-01-30T10:28:12.008951'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/person/mark
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/ally
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.315269Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/brand/v1
  message: Migrated from v1 to v2 schema
name: Marley Spoon
$orphan_reason: pending_enrichment
---

# Marley_Spoon

**Type:** brand
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Competitor referenced for benchmarking cancellation language ('easily cancel') (from: 2nd iteration of new T&Cs for Activation)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Gdocs Context

- [2026-01-02] Competitor referenced for 'easily cancel' language (from: 2nd iteration of new T&Cs for Activation)
