---
$schema: brain://entity/squad/v1
$id: entity/squad/tam
$type: squad
$version: 1
$created: '2026-01-22T08:31:01.317465Z'
$updated: '2026-01-22T08:31:01.317465Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/squad/cma
  confidence: 0.8677
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/crm-team
  confidence: 0.8576
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/new-ventures-systems-squad
  confidence: 0.8522
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/new-ventures-systems-squad-nvs
  confidence: 0.8481
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/good-chop-squad
  confidence: 0.8454
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/goodchop-squad
  confidence: 0.8407
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.317465Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/squad/v1
  message: Migrated from v1 to v2 schema
name: Tam
---

# Tam

**Type:** squad
**Created:** 2026-01-02
**Source:** slack extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Team working on Big Rocks including Good Chop, TPT, Factor Form, Cross-Selling, Programs (#tribe-new-ventures-product)

## Related Entities

[To be filled]

## Notes

- Created automatically from slack analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
