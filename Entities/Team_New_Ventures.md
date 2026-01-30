---
$schema: brain://entity/project/v1
$id: entity/project/team-new-ventures
$type: project
$version: 1
$created: '2026-01-22T08:31:01.247589Z'
$updated: '2026-01-30T10:22:39.222050'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/person/sameer-doda
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/deo
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/beatrice
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/person/prateek-jajoo
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/alex-matlin
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/daniel
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
  target: entity/project/influencer-marketplace
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/good-chop
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/the-pets-table
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/factor-form
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/yury
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/ian-brooks
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/jama
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/sameer-doda
  confidence: 1.0
  last_verified: '2026-01-30'
- type: related_to
  target: entity/project/prateek-jajoo
  confidence: 1.0
  last_verified: '2026-01-30'
- type: related_to
  target: entity/project/beatrice-dimarucut
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.247589Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.353899+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 18
name: Team New Ventures
id: entity-team-new-ventures
type: team
last_updated: 2025-12-08
related:
- '[[Projects/Influencer_Marketplace.md]]'
- '[[Projects/Good_Chop.md]]'
- '[[Projects/The_Pets_Table.md]]'
- '[[Projects/Factor_Form.md]]'
- '[[Projects/OTP.md]]'
---

# Team: New Ventures & Ecosystems

## Overview

New Ventures & Ecosystems (also known as TAM Expansion) is responsible for expanding HelloFresh Group's total addressable market through new products, brands, and business models.

## Team Members

| Name | Role | Focus Area |
|------|------|------------|
| Nikita Gorshkov | Product Leader | Strategy, team management |
| [[Entities/Sameer_Doda.md\|Sameer Doda]] | PM | Influencer Marketplace, Good Chop Shopify |
| [[Entities/Deo.md\|Deo]] | PM | Good Chop |
| [[Entities/Beatrice.md\|Beatrice]] | PM | TBD |
| [[Entities/Prateek_Jajoo.md\|Prateek Jajoo]] | Staff PM | The Pets Table |
| Allison | PM | Platform, Factor Form Shopify |
| [[Entities/Alex_Matlin.md\|Alex Matlin]] | Engineering Lead | Technical feasibility |
| [[Entities/Daniel.md\|Daniel]] | Engineering Lead | Implementation |

## Current Projects

| Project | Status | Lead |
|---------|--------|------|
| [[Projects/OTP.md\|OTP Capabilities]] | Active | Cross-team |
| [[Projects/Influencer_Marketplace.md]] | Phase 3 | Sameer |
| [[Projects/Good_Chop.md]] | Active | Deo |
| [[Projects/The_Pets_Table.md]] | Active | Prateek |
| [[Projects/Factor_Form.md]] | Active | Allison |

## Resource Constraints

- **Frontend Development:** Need FE developer to replace Deborah
- **Open Roles:** 3 positions being filled
- **Design:** Shay supporting, but bandwidth limited

## Key Stakeholders

- **Leadership:** [[Entities/Yury.md|Yury]], [[Entities/Ian_Brooks.md|Ian Brooks]]
- **Platform:** [[Entities/Jama.md|Jama]]

## Aliases

- New Ventures
- New Ventures & Ecosystems
- TAM Expansion

## Changelog

- **2025-12-08:** Entity created from daily context synthesis