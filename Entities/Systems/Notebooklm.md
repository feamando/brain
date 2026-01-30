---
$schema: brain://entity/system/v1
$id: entity/system/notebooklm
$type: system
$version: 1
$created: '2026-01-22T08:31:01.699057Z'
$updated: '2026-01-30T10:28:12.980476'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/tam-product
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/decisions
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
  timestamp: '2026-01-22T08:31:01.699057Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Notebooklm
$orphan_reason: pending_enrichment
---

# Notebooklm

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Referenced as tool for in-depth processes and potentially for automatically documenting key decisions from meeting transcriptions (from: TAM Product: Context-driven Product Mana)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Gdocs Context

- [2026-01-02] Tool for sharing MAR/QARs and tactical reports with team and stakeholders (from: TAM Product: Context-driven Product Mana)


- [2026-01-02] Tool for sharing team reports, MAR/QARs and tactical reports with stakeholders (from: TAM Product: Context-driven Product Mana)