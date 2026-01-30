---
$schema: brain://entity/project/v1
$id: entity/project/aov-squad
$type: project
$version: 1
$created: '2026-01-22T08:31:00.937223Z'
$updated: '2026-01-22T08:31:00.937223Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/project/aov-focused-squad
  confidence: 0.9476
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.92
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.937223Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Aov Squad
---

# Aov_Squad

**Type:** project
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] New self-funded squad to be created in Q2 with dedicated KPI focused on average order value (from: 2026 Yearly Plan - Consumer Mega-Allianc)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:50*
