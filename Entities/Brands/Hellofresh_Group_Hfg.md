---
$schema: brain://entity/brand/v1
$id: entity/brand/hellofresh-group-hfg
$type: brand
$version: 1
$created: '2026-01-22T08:31:01.284517Z'
$updated: '2026-01-22T08:31:01.284517Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/brand/hellofresh-group
  confidence: 0.9624
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/brand/hfg-hello-fresh-group
  confidence: 0.8547
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.284517Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/brand/v1
  message: Migrated from v1 to v2 schema
name: Hellofresh Group Hfg
---

# Hellofresh_Group_Hfg

**Type:** brand
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Parent company implementing OTP capabilities across brands (from: PRD: Enabling One-Time-Purchase (OTP) Ca)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
