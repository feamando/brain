---
$schema: brain://entity/system/v1
$id: entity/system/ftcp-cluster
$type: system
$version: 1
$created: '2026-01-22T08:31:01.652232Z'
$updated: '2026-01-22T08:31:01.652232Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/system/ftcp
  confidence: 0.9003
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.652232Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Ftcp Cluster
---

# Ftcp_Cluster

**Type:** system
**Created:** 2026-01-02
**Source:** slack extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] 30% of live PCS traffic being switched to this cluster (#squad-nv-good-chop)

## Related Entities

[To be filled]

## Notes

- Created automatically from slack analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
