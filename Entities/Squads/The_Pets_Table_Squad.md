---
$schema: brain://entity/squad/v1
$id: entity/squad/the-pets-table-squad
$type: squad
$version: 1
$created: '2026-01-22T08:31:01.317890Z'
$updated: '2026-01-22T08:31:01.317890Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/squad/new-ventures-and-ecosystems-pets-table
  confidence: 0.8538
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/new-ventures-pet-food
  confidence: 0.8386
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/new-ventures-systems-squad
  confidence: 0.8146
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/new-ventures-systems-squad-nvs
  confidence: 0.8104
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.317890Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/squad/v1
  message: Migrated from v1 to v2 schema
name: The Pets Table Squad
---

# The_Pets_Table_Squad

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

## Slack Context

- [2026-01-02] Squad working on TPT brand, no concrete rebranding plans yet (#tribe-new-ventures-leads-internal)
