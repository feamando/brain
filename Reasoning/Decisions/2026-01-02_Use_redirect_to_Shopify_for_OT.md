---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-use-redirect-to-shopify-for-ot
$type: project
$version: 1
$created: '2026-01-22T08:31:01.831195Z'
$updated: '2026-01-30T15:14:17.151611'
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
  timestamp: '2026-01-22T08:31:01.831195Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Use Redirect To Shopify For Ot
---

# Decision: Use redirect to Shopify for OTP implementation if it's faster/cheaper than building a proper endpoint

**Date:** 2026-01-02
**Source:** GDocs - Nikita / Beatrice - 2025/12/08 17:31 CET - Notes b
**Confidence:** medium


## Decision

Use redirect to Shopify for OTP implementation if it's faster/cheaper than building a proper endpoint

## Participants

Beatrice Dimarucut, Nikita Gorshkov

## Context

Weighing technical implementation options for one-time purchases, considering that redirect would be significantly cheaper (20% of cost) and faster

---
*Extracted from GDocs on 2026-01-02*
