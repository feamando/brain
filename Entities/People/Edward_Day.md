---
$schema: brain://entity/person/v1
$id: entity/person/edward-day
$type: person
$version: 1
$created: '2026-01-22T08:31:01.495204Z'
$updated: '2026-01-30T15:14:16.360113'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: works_on
  target: entity/project/cancel-deflection
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: works_on
  target: entity/project/homepage-redesign
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: works_on
  target: entity/project/click-collect-cc
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: related_to
  target: entity/person/emmanuelle-hazeaux
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: related_to
  target: entity/person/karolina-zak
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.495204Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/person/v1
  message: Migrated from v1 to v2 schema
name: Edward Day
---

# Edward_Day

**Type:** person
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Decision maker for rollout scenario (from: PRD: Cancellation Funnel Unification)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Gdocs Context

- [2026-01-02] Project decision maker and owner (from: PRD: Cancellation Funnel Unification)
