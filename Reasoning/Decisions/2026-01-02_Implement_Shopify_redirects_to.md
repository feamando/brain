---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-implement-shopify-redirects-to
$type: project
$version: 1
$created: '2026-01-22T08:31:01.983698Z'
$updated: '2026-01-30T15:14:17.936150'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: nikita
  confidence: 0.65
  source: body_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.983698Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Implement Shopify Redirects To
---

# Decision: Implement Shopify redirects to prevent multiple accounts across websites

**Date:** 2026-01-02
**Source:** GDocs - Hamed:Nikita 1:1 - 2025/12/05 17:41 CET - Notes by
**Confidence:** medium


## Decision

Implement Shopify redirects to prevent multiple accounts across websites

## Participants

Unknown

## Context

Decision by Samir and Allison. Net new users from legacy pages redirected to Shopify; existing Factor account users landing on Shopify redirected back to legacy page to see their subscriptions and past orders. Expected to affect only small percentage (5% or less) of users.

---
*Extracted from GDocs on 2026-01-02*
