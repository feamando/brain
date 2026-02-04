---
$schema: brain://entity/project/v1
$id: entity/project/snowplow-migration
$type: project
$version: 1
$created: '2026-02-02T13:08:50.627046Z'
$updated: '2026-02-02T13:08:50.627046Z'
$confidence: 0.5
$source: master_sheet
$status: active
$relationships:
- type: part_of
  target: entity/brand/nv-general
  since: '2026-02-02'
$tags:
- master_sheet
- p0
$aliases:
- snowplow migration
$events:
- event_id: evt-master-sheet-20260202130850
  timestamp: '2026-02-02T13:08:50.627046Z'
  type: entity_create
  actor: system/master_sheet_sync
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Created from Master Sheet sync
name: Snowplow Migration
---

# Snowplow Migration

**Type:** project
**Product:** NV General
**Created:** 2026-02-02
**Source:** Master Sheet

## Overview

Migration Strategy

## Status

- **Current Status:** In Progress
- **Priority:** P0
- **Deadline:** 2026-02-15
- **Owner:** Daniel Arias

## Context

- [2026-02-02] Created from Master Sheet (Product: NV General, Feature: Snowplow Migration)

## Related Entities

- [[nv-general]] (Product)
- [[Daniel_Arias]] (Owner)

## References

- [Snowplow - 2026/01/26 10:02 CET - Notes by Gemini](Snowplow - 2026/01/26 10:02 CET - Notes by Gemini)

## Notes

- Created automatically from Master Sheet sync
- Review and enrich manually

---
*Last updated: 2026-02-02*
