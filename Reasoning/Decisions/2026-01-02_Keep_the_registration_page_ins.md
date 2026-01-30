---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-keep-the-registration-page-ins
$type: project
$version: 1
$created: '2026-01-22T08:31:02.140868Z'
$updated: '2026-01-30T10:28:14.140486'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:02.140868Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Keep The Registration Page Ins
$orphan_reason: pending_enrichment
---

# Decision: Keep the registration page instead of removing it

**Date:** 2026-01-02
**Source:** GDocs - PRD: TPT Sign-up Page Revamp
**Confidence:** medium


## Decision

Keep the registration page instead of removing it

## Participants

Product team

## Context

Registration page is necessary to verify whether a prospect already has an account, helps redirect existing users to reactivation page, prevents redundant navigation through signup funnel. Data shows registration page adds little friction (12.25% visited Address vs 11.62% visited Registration).

---
*Extracted from GDocs on 2026-01-02*
