---
$schema: brain://entity/project/v1
$id: entity/project/during-con-remove-honeycomb-span-use-free
$type: project
$version: 1
$created: '2026-01-22T08:31:02.103593Z'
$updated: '2026-01-30T10:28:14.058742'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:02.103593Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: During Con Remove Honeycomb Span Use Free
$orphan_reason: pending_enrichment
---

# Decision: Remove honeycomb span 'use-free-addons-by-voucher-code' due to spam

**Date:** during con
**Source:** Slack - #squad-nv-good-chop
**Confidence:** high


## Decision

Remove honeycomb span 'use-free-addons-by-voucher-code' due to spam

## Participants

U0MBX09UZ, U03UCPY6MHQ

## Context

Span was 9th most collected with 6.3M spans/day and 100 spans per session, creating inaccurate data

---
*Extracted from Slack on 2026-01-02*
