---
$schema: brain://entity/project/v1
$id: entity/project/scm
$type: project
$version: 1
$created: '2026-01-22T08:31:01.089397Z'
$updated: '2026-01-22T10:41:35.065209+00:00'
$confidence: 0.43
$source: unknown
$status: Active
$relationships:
- type: related_to
  target: entity/project/team-consumer-core
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.089397Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.065217+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 5
name: Scm
id: arch-scm
title: Supply Chain Management (SCM)
type: system
last_updated: 2025-12-08
related:
- '[[Projects/OTP.md]]'
---

# Supply Chain Management (SCM)

## Overview

SCM encompasses the logistics and fulfillment systems that power HelloFresh Group's delivery operations. Key systems include Demeter (UK legacy) and Odin (global).

## Key Systems

### Demeter (UK)
- **Type:** Legacy logistics system
- **Status:** Active but requires updates for OTP
- **Issue:** Needs "order grouping ID" update to recognize OTP orders

### Odin
- **Type:** Global logistics platform
- **Status:** Target for OTP scaling
- **Requirement:** Integration needed for global OTP rollout

## OTP Dependencies

For OTP to scale globally, local SCM systems need updates:
- **Order Grouping ID:** Local systems must recognize this field
- **Non-subscription handling:** Systems designed for subscription orders need adaptation

## Key Contacts

- **Operations/SCM:** Seb

## Blockers

- **Scaling Blocker (P0):** Legacy local logistics systems blocking global OTP rollout

## Changelog
- **2025-12-08:** Mentioned in daily context (4x)

- **2025-12-08:** Stub created from daily context synthesis