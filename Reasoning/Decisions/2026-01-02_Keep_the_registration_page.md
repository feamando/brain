---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-keep-the-registration-page
$type: project
$version: 1
$created: '2026-01-22T08:31:01.962566Z'
$updated: '2026-01-30T10:28:13.694197'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.962566Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Keep The Registration Page
$orphan_reason: pending_enrichment
---

# Decision: Keep the registration page

**Date:** 2026-01-02
**Source:** GDocs - PRD: Sign up page revamp
**Confidence:** medium


## Decision

Keep the registration page

## Participants

prateek jajoo

## Context

Registration page is necessary to verify if prospect already has an account, helps redirect existing users to reactivation page, prevents redundant navigation through signup funnel. Data shows minimal drop-off (12.25% visited address vs 11.62% visited registration) compared to HelloFresh (55% drop-off).

---
*Extracted from GDocs on 2026-01-02*
