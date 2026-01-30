---
$schema: brain://entity/system/v1
$id: entity/system/hellofresh-app
$type: system
$version: 1
$created: '2026-01-22T08:31:01.675845Z'
$updated: '2026-01-30T10:28:12.922512'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/hellofresh
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/engagement
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/mobile-app
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/engagement-tribe
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/fresh
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.675845Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Hellofresh App
$orphan_reason: pending_enrichment
---

# Hellofresh_App

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Primary mobile application tracked by multiple engagement squads (from: CMA Squad overview)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Gdocs Context

- [2026-01-02] Primary product for Engagement tribe squads (Inspire, Act) (from: CMA Squad overview)


- [2026-01-02] Primary platform for Engagement tribe metrics (downloads, DAU/MAU ratio) (from: CMA Squad overview)

- [2026-01-02] Primary mobile application being enhanced across all initiatives (from: Consumer Mega-Alliance Roadmap)

- [2026-01-02] Primary platform for all initiatives with focus on increasing DAU/MAU ratio (from: Consumer Mega-Alliance Roadmap)