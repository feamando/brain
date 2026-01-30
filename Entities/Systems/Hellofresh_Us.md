---
$schema: brain://entity/system/v1
$id: entity/system/hellofresh-us
$type: system
$version: 1
$created: '2026-01-22T08:31:01.666939Z'
$updated: '2026-01-30T10:28:12.900778'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/factor
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/hellofresh
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/meal-selection
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/fresh
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/brand/factor-
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.666939Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Hellofresh Us
$orphan_reason: pending_enrichment
---

# Hellofresh_Us

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Source brand for customers entering Factor US signup funnel (from: Spike - Precheckout Meal Selection FJ)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Gdocs Context

- [2026-01-02] Target market and primary brand (from: PRD: (🥇MVP) Cross-Selling as Market Inte)


- [2026-01-02] Mentioned in email about 2025-W48 Recipe Report with menu scores and SKU launches (from: TPT SKU Complexity Calculator)

## Slack Context

- [2026-01-02] Enabled on NV-CRM but events are not actually used (#squad-market-io)
