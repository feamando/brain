---
$schema: brain://entity/squad/v1
$id: entity/squad/market-innovation-optimization-squad
$type: squad
$version: 1
$created: '2026-01-22T08:31:01.318834Z'
$updated: '2026-01-22T08:31:01.318834Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/squad/squad-market-io
  confidence: 0.8597
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/new-ventures-systems-squad
  confidence: 0.8485
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/new-ventures-systems-squad-nvs
  confidence: 0.8407
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/mio-market-innovation-and-optimization
  confidence: 0.8245
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/cma
  confidence: 0.8057
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.318834Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/squad/v1
  message: Migrated from v1 to v2 schema
name: Market Innovation Optimization Squad
---

# Market_Innovation_Optimization_Squad

**Type:** squad
**Created:** 2026-01-02
**Source:** slack extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] New squad structure introduced later (#tribe-new-ventures-leads-internal)

## Related Entities

[To be filled]

## Notes

- Created automatically from slack analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Slack Context

- [2026-01-02] MIO squad working on BNL migration and IT Cap reporting (#tribe-new-ventures-leads-internal)
