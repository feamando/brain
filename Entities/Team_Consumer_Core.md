---
$schema: brain://entity/project/v1
$id: entity/project/team-consumer-core
$type: project
$version: 1
$created: '2026-01-22T08:31:01.151257Z'
$updated: '2026-01-22T10:41:35.173500+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/jama
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/otp
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/scm
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.151257Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.173502+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 13
name: Team Consumer Core
id: entity-team-consumer-core
type: team
last_updated: 2025-12-08
related:
- '[[Projects/OTP.md]]'
- '[[Architecture/SCM.md]]'
---

# Team: Consumer Core

## Overview

Consumer Core (also known as Consumer Mega-Alliance) is responsible for the core consumer experience across HelloFresh Group brands, including checkout, home screen, and user journeys.

## Responsibilities

- Monolith deprecation and decoupling
- User journey ownership (checkout, reactivate, home screen)
- Add-ons and surcharges support
- React Native migration

## Q1 2026 Focus (from Planning Workshop)

### Key Initiatives

- **React Native Migration:** AI-first approach for faster migration (starting with Profile page)
- **Project 500 (P500):** Multi-region readiness - high priority dependency
- **Snowplow:** Personalization signals infrastructure
- **Seamless Downgrade:** Quick fix deployed, long-term solution pending
- **Elusium:** Finalize rollout to remove old native code (must-do)
- **Monolith Deprecation:** Likely to spill over from Q1

### OTP Support

- Add-ons/surcharges resolution for OTP flow
- Cart consolidation (global cart service)

## Key Contacts

- **Platform:** [[Entities/Jama.md|Jama]]

## Related Projects

- [[Projects/OTP.md]] - Add-on/surcharge support
- [[Architecture/SCM.md]] - Logistics integration

## Aliases

- Consumer Core
- Consumer Mega-Alliance

## Changelog
- **2025-12-09:** Mentioned in daily context (2x)

- **2025-12-08:** Entity created from daily context synthesis