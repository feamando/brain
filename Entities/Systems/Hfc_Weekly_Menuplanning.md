---
$schema: brain://entity/system/v1
$id: entity/system/hfc-weekly-menuplanning
$type: system
$version: 1
$created: '2026-01-22T08:31:01.607836Z'
$updated: '2026-01-22T08:31:01.607836Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/system/mp-menu-planning
  confidence: 0.9098
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.607836Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Hfc Weekly Menuplanning
---

# Hfc_Weekly_Menuplanning

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Slack channel for weekly menu planning coordination (from: HFCA - CCM Recipes)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
