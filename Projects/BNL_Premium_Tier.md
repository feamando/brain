---
$schema: brain://entity/project/v1
$id: entity/project/bnl-premium-tier
$type: project
$version: 7
$created: '2026-01-22T08:31:01.085270Z'
$updated: '2026-01-30T14:33:04.879871+00:00'
$confidence: 0.43
$source: unknown
$status: Active - Critical Blocker
$relationships:
- type: mentioned_in
  target: entity/project/netherlands
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/mark
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/system/live
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.085270Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:57.448873+00:00'
  type: orphan_cleanup
  actor: system/orphan_cleaner
  changes:
  - field: $relationships
    operation: cleanup
    count: 1
name: Bnl Premium Tier
id: project-bnl-premium-tier
title: BNL Premium Tier (Benelux)
last_updated: 2025-12-08
$orphan_reason: no_external_data
---

# BNL Premium Tier

## Executive Summary

Premium tier offering for Benelux (Belgium, Netherlands, Luxembourg) markets. Currently blocked by a technical issue preventing menu display.

## Current Status

**CRITICAL BLOCKER:** Missing preference string field due to incorrect "is menu add-on" tag. This blocks menu display entirely.

## Required Actions

| Owner | Action | Status |
|-------|--------|--------|
| Xiao | Change product family type to "core" to fix menu display | Critical |
| NL Team | Test end-to-end on live (Week 4 Thursday) | Pending |

## Timeline

- **Dec 11:** BNL Monetization Weekly - 2nd Round

## Changelog
- **2025-12-09:** Context update: **BNL Premium Tier**: Missing preference string field blocks menu display.
- **2025-12-08:** Context update: **BNL Premium Tier**: Missing preference string field blocks menu display. (From 12/05)

- **2025-12-08:** Stub created from daily context synthesis - CRITICAL blocker flagged