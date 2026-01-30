---
$schema: brain://entity/project/v1
$id: entity/project/current-st-crm-team-completely-migrated-f
$type: project
$version: 1
$created: '2026-01-22T08:31:01.891814Z'
$updated: '2026-01-30T10:28:13.510887'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.891814Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Current St Crm Team Completely Migrated F
$orphan_reason: pending_enrichment
---

# Decision: CRM team completely migrated Factor emails to NV-CRM events, no longer using BFF events

**Date:** current st
**Source:** Slack - #squad-market-io
**Confidence:** high


## Decision

CRM team completely migrated Factor emails to NV-CRM events, no longer using BFF events

## Participants

U047SAC2PPV, CRM team

## Context

Part of phased migration from old BFF-based email triggering to new NV-CRM event system

---
*Extracted from Slack on 2026-01-02*
