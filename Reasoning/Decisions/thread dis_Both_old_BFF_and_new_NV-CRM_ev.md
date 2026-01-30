---
$schema: brain://entity/project/v1
$id: entity/project/thread-dis-both-old-bff-and-new-nv-crm-ev
$type: project
$version: 1
$created: '2026-01-22T08:31:01.887243Z'
$updated: '2026-01-30T10:28:13.498672'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.887243Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Thread Dis Both Old Bff And New Nv Crm Ev
$orphan_reason: pending_enrichment
---

# Decision: Both old (BFF) and new (NV-CRM) event systems will coexist during migration without interfering with each other

**Date:** thread dis
**Source:** Slack - #squad-market-io
**Confidence:** high


## Decision

Both old (BFF) and new (NV-CRM) event systems will coexist during migration without interfering with each other

## Participants

U047SAC2PPV

## Context

To avoid migrating multiple clients simultaneously and allow gradual rollout of the new NV-CRM approach for subscribable addon email notifications

---
*Extracted from Slack on 2026-01-02*
