---
$schema: brain://entity/project/v1
$id: entity/project/week-29-j-prioritize-patch-subscriptions
$type: project
$version: 1
$created: '2026-01-22T08:31:01.785710Z'
$updated: '2026-01-30T10:28:13.233033'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/consumer-core
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/u8f7zdapm
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/u027201fqsv
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/pants
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/uez4prfkm
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.785710Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Week 29 (J Prioritize Patch Subscriptions
$orphan_reason: pending_enrichment
---

# Decision: Prioritize PATCH /subscriptions deprecation for CDPS migration in next sprint (mid-August deadline)

**Date:** Week 29 (J
**Source:** Slack - #tribe-new-ventures-leads-internal
**Confidence:** medium


## Decision

Prioritize PATCH /subscriptions deprecation for CDPS migration in next sprint (mid-August deadline)

## Participants

UEZ4PRFKM, U027201FQSV, U8F7ZDAPM

## Context

Consumer Core rolling out CDPS and deprecating old endpoint; originally requested end of July but negotiated to mid-August

---
*Extracted from Slack on 2026-01-02*
