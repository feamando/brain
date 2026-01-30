---
$schema: brain://entity/system/v1
$id: entity/system/tableau
$type: system
$version: 1
$created: '2026-01-22T08:31:01.711847Z'
$updated: '2026-01-30T10:28:13.015961'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/new-ventures
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/data
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/dashboards
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/ally
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/system/dashboard
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.711847Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Tableau
$orphan_reason: pending_enrichment
---

# Tableau

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Source of truth for cancellation metrics (from: PRD: Cancellation Funnel Unification)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Gdocs Context

- [2026-01-02] Source of truth for cancellation metrics (from: PRD: Cancellation Funnel Unification)


- [2026-01-02] Dashboard platform for multiple retention and analytics dashboards (from: New Ventures: PA Backlog)

- [2026-01-02] Dashboard platform for multiple retention and analytics dashboards (from: New Ventures: PA Backlog)

- [2026-01-02] Data visualization tool for training (from: Product - Onboarding Checklist (Deo/Beat)