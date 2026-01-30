---
$schema: brain://entity/project/v1
$id: entity/project/2026-01-02-active-customers-can-buy-small
$type: project
$version: 1
$created: '2026-01-22T08:31:01.947884Z'
$updated: '2026-01-30T15:14:17.397586'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: nikita
  confidence: 0.65
  source: body_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: otp
  confidence: 0.65
  source: body_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.947884Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: 2026 01 02 Active Customers Can Buy Small
---

# Decision: Active customers can buy small kits (like dinner for two) as one-time purchase

**Date:** 2026-01-02
**Source:** GDocs - Sameer:Nikita 1:1 - 2025/12/05 15:29 CET - Notes b
**Confidence:** medium


## Decision

Active customers can buy small kits (like dinner for two) as one-time purchase

## Participants

Unknown

## Context

Simplifies front-end by avoiding need to enforce minimum rules

---
*Extracted from GDocs on 2026-01-02*
