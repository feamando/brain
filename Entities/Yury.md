---
$schema: brain://entity/project/v1
$id: entity/project/yury
$type: project
$version: 1
$created: '2026-01-22T08:31:01.163437Z'
$updated: '2026-01-22T10:41:35.200120+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/team-new-ventures
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.163437Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.200122+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 5
name: Yury
id: entity-yury
type: person
role: Senior Leadership
last_updated: 2025-12-08
related:
- '[[Projects/Good_Chop.md]]'
- '[[Entities/Team_New_Ventures.md]]'
---

# Yury

## Role & Responsibilities

- **Title:** Senior Stakeholder / Leadership
- **Scope:** Sets high-level priorities for New Ventures

### Primary Responsibilities

- Strategic direction for Good Chop and New Ventures
- H1 2026 product prioritization
- Resource allocation decisions

## Current Focus

- Good Chop H1 2026 strategy
- OTP rollout prioritization

## Action Items (Current)

- [ ] Finalize H1 2026 product prioritization for Good Chop

## Key Relationships

- **Direct Reports:** Deo (Good Chop PM)
- **Collaborators:** Nikita Gorshkov

## Changelog

- **2025-12-08:** Entity created from daily context synthesis