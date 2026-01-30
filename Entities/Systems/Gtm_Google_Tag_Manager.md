---
$schema: brain://entity/system/v1
$id: entity/system/gtm-google-tag-manager
$type: system
$version: 1
$created: '2026-01-22T08:31:01.744454Z'
$updated: '2026-01-30T10:28:13.095349'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/system/google
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/cade
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/ally
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/system/checkout
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.744454Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Gtm Google Tag Manager
$orphan_reason: pending_enrichment
---

# Gtm_Google_Tag_Manager

**Type:** system
**Created:** 2026-01-02
**Source:** github extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Extensive tracking improvements across multiple flows (GitHub commits)

## Related Entities

[To be filled]

## Notes

- Created automatically from github analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Github Context

- [2026-01-02] Event tracking integration for OTP checkout (GitHub commits)


- [2026-01-02] Fixed to include proper attributes for OTP order tracking (GitHub commits)

- [2026-01-02] Multi-cadence event tracking implementation (GitHub commits)

- [2026-01-02] Updated with OTP attributes for product change events (GitHub commits)