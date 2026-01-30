---
$schema: brain://entity/person/v1
$id: entity/person/dsire-lima
$type: person
$version: 1
$created: '2026-01-22T08:31:01.482305Z'
$updated: '2026-01-30T15:14:16.317478'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: works_on
  target: entity/project/my-deliveries
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
- type: maintains
  target: entity/system/tpt-checkout
  confidence: 0.7
  last_verified: '2026-01-30'
  source: gdocs
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.482305Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/person/v1
  message: Migrated from v1 to v2 schema
name: Désirée Lima
---

# Désirée_Lima

**Type:** person
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Attendee leading free items and two step loading page initiatives (from: Weekly Prod/Des/Eng/PA)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:50*
