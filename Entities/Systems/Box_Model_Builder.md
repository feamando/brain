---
$schema: brain://entity/system/v1
$id: entity/system/box-model-builder
$type: system
$version: 1
$created: '2026-01-22T08:31:01.675408Z'
$updated: '2026-01-30T10:28:12.921363'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/food
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/fresh
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
  timestamp: '2026-01-22T08:31:01.675408Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Box Model Builder
$orphan_reason: pending_enrichment
---

# Box_Model_Builder

**Type:** component
**Created:** 2026-01-02
**Source:** github extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] New hook implementation for pets table box content (GitHub commits)

## Related Entities

[To be filled]

## Notes

- Created automatically from github analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Github Context

- [2026-01-02] Optimization and new override capabilities added (GitHub commits)


- [2026-01-02] New functionality added for GSheet upload, feeding guide, and logic improvements (GitHub commits)

- [2026-01-02] Enhanced with arguments support (GitHub commits)

- [2026-01-02] Extended with calorie range overrides and general override functionality (GitHub commits)

- [2026-01-02] Distribution logic updated for fresh and dry food models (GitHub commits)

- [2026-01-02] Minor improvements applied (GitHub commits)

- [2026-01-02] Initial setup for kn-box-model-builder (GitHub commits)