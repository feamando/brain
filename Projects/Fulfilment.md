---
$schema: brain://entity/project/v1
$id: entity/project/fulfilment
$type: project
$version: 1
$created: '2026-01-22T08:31:00.956901Z'
$updated: '2026-01-30T10:18:58.266971'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/project/decisions
  confidence: 0.9595
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.92
- type: similar_to
  target: entity/project/data
  confidence: 0.9592
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.92
- type: similar_to
  target: entity/project/operations-enablement
  confidence: 0.9492
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.92
- type: similar_to
  target: entity/project/foundations
  confidence: 0.9419
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.92
- type: similar_to
  target: entity/project/operations-intl
  confidence: 0.9284
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/project/operations-na
  confidence: 0.9228
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.956901Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Fulfilment
---

# Fulfilment

**Type:** project
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Tech team alliance with incoming dependencies (from: [WIP] 2025YP Dependencies Master)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
