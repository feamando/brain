---
$schema: brain://entity/system/v1
$id: entity/system/whitelabel
$type: system
$version: 2
$created: '2026-01-22T08:31:01.621496Z'
$updated: '2026-01-30T13:57:09.169368+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/system/good-chop
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
- type: mentioned_in
  target: entity/system/slack
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.621496Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Whitelabel
$orphan_reason: no_external_data
---

# Whitelabel

**Type:** system
**Created:** 2026-01-02
**Source:** slack extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Shared legacy dashboard infrastructure that Good Chop is migrating away from (#tribe-new-ventures-product)

## Related Entities

[To be filled]

## Notes

- Created automatically from slack analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Github Context

- [2026-01-02] Layout props groomed for better organization (GitHub commits)
