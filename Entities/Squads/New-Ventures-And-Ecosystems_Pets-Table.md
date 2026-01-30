---
$schema: brain://entity/squad/v1
$id: entity/squad/new-ventures-and-ecosystems-pets-table
$type: squad
$version: 1
$created: '2026-01-22T08:31:01.323350Z'
$updated: '2026-01-30T10:22:52.419454'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/squad/the-pets-table-squad
  confidence: 0.8538
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/squad/new-ventures-pet-food
  confidence: 0.9289
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.323350Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/squad/v1
  message: Migrated from v1 to v2 schema
name: New Ventures And Ecosystems Pets Table
---

# New-Ventures-And-Ecosystems_Pets-Table

**Type:** squad
**Created:** 2026-01-02
**Source:** slack extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Team/squad being monitored by Inspector (#squad-nv-pet-food)

## Related Entities

[To be filled]

## Notes

- Created automatically from slack analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
