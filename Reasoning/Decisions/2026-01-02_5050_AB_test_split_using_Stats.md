---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-5050-ab-test-split-using-stats
$type: project
$version: 1
$created: '2026-01-22T08:31:02.121663Z'
$updated: '2026-01-30T10:28:14.100198'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:02.121663Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 5050 Ab Test Split Using Stats
$orphan_reason: pending_enrichment
---

# Decision: 50/50 A/B test split using Statsig

**Date:** 2026-01-02
**Source:** GDocs - PRD: Beam Integration for The Pets Table
**Confidence:** medium


## Decision

50/50 A/B test split using Statsig

## Participants

Not specified

## Context

Measure impact on gross CVR and secondary metrics

---
*Extracted from GDocs on 2026-01-02*
