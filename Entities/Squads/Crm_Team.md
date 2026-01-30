---
$schema: brain://entity/squad/v1
$id: entity/squad/crm-team
$type: squad
$version: 1
$created: '2026-01-22T08:31:01.320638Z'
$updated: '2026-01-30T10:22:52.486057'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/squad/cma
  confidence: 0.8926
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/new-ventures-systems-squad-nvs
  confidence: 0.8467
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/tam
  confidence: 0.8576
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/squad/new-ventures-systems-squad
  confidence: 0.8744
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/squad/goodchop-squad
  confidence: 0.8374
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.320638Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/squad/v1
  message: Migrated from v1 to v2 schema
name: Crm Team
---

# Crm_Team

**Type:** squad
**Created:** 2026-01-02
**Source:** slack extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Team requiring new interaction process with commercial teams (#tribe-new-ventures-product)

## Related Entities

[To be filled]

## Notes

- Created automatically from slack analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
