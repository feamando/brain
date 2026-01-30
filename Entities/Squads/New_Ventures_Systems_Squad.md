---
$schema: brain://entity/squad/v1
$id: entity/squad/new-ventures-systems-squad
$type: squad
$version: 1
$created: '2026-01-22T08:31:01.319284Z'
$updated: '2026-01-30T10:22:52.429297'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/squad/new-ventures-systems-squad-nvs
  confidence: 0.9762
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/goodchop-squad
  confidence: 0.9097
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/crm-team
  confidence: 0.8744
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/cma
  confidence: 0.8628
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/good-chop-squad
  confidence: 0.8338
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/cross-selling-puma-squad
  confidence: 0.8029
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/squad/tam
  confidence: 0.8522
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/squad/the-pets-table-squad
  confidence: 0.8146
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/squad/market-innovation-optimization-squad
  confidence: 0.8485
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.319284Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/squad/v1
  message: Migrated from v1 to v2 schema
name: New Ventures Systems Squad
---

# New_Ventures_Systems_Squad

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
