---
$schema: brain://entity/system/v1
$id: entity/system/freshchat-integration
$type: system
$version: 1
$created: '2026-01-22T08:31:01.644706Z'
$updated: '2026-01-30T10:24:58.189731'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/system/freshchat
  confidence: 0.9844
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/system/hellodev
  confidence: 0.9552
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.644706Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Freshchat Integration
---

# Freshchat_Integration

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Integration being released in HelloDev (from: Notes - AI Bytes Assemble)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:50*

## Gdocs Context

- [2026-01-02] Released in HelloDev product (from: Notes - AI Bytes Assemble)
