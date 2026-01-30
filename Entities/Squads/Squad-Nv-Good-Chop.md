---
$schema: brain://entity/squad/v1
$id: entity/squad/squad-nv-good-chop
$type: squad
$version: 1
$created: '2026-01-22T08:31:01.321569Z'
$updated: '2026-01-30T10:22:52.489156'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/squad/good-chop-squad
  confidence: 0.8467
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.8
- type: similar_to
  target: entity/squad/goodchop-squad
  confidence: 0.8063
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.321569Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/squad/v1
  message: Migrated from v1 to v2 schema
name: Squad Nv Good Chop
---

# Squad-Nv-Good-Chop

**Type:** squad
**Created:** 2026-01-02
**Source:** slack extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Team handling GoodChop support requests, bug fixes, and code reviews (#squad-nv-good-chop)

## Related Entities

[To be filled]

## Notes

- Created automatically from slack analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Slack Context

- [2026-01-02] Support channel receiving requests for code reviews, test failures, and QA (#squad-nv-good-chop)


- [2026-01-02] Support channel for Good Chop brand issues including E2E tests, menu configuration, and code reviews (#squad-nv-good-chop)