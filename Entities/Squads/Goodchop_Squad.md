---
$schema: brain://entity/squad/v1
$id: entity/squad/goodchop-squad
$type: squad
$version: 1
$created: '2026-01-22T08:31:01.319731Z'
$updated: '2026-01-30T10:22:52.448648'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/squad/new-ventures-systems-squad-nvs
  confidence: 0.8913
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/good-chop-squad
  confidence: 0.8788
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/cma
  confidence: 0.847
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/crm-team
  confidence: 0.8374
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/squad-nv-good-chop
  confidence: 0.8063
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/plans-squad
  confidence: 0.813
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/squad/tam
  confidence: 0.8407
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/squad/new-ventures-systems-squad
  confidence: 0.9097
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.319731Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/squad/v1
  message: Migrated from v1 to v2 schema
name: Goodchop Squad
---

# Goodchop_Squad

**Type:** squad
**Created:** 2026-01-02
**Source:** slack extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] One of the New Ventures squads (#tribe-new-ventures-leads-internal)

## Related Entities

[To be filled]

## Notes

- Created automatically from slack analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
