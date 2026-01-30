---
$schema: brain://entity/project/v1
$id: entity/project/deo
$type: project
$version: 1
$created: '2026-01-22T08:31:01.158571Z'
$updated: '2026-01-22T10:41:35.191520+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/team-new-ventures
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
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.158571Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.191525+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Deo
id: entity-deo
type: person
role: PM - Good Chop
last_updated: 2025-12-08
related:
- '[[Projects/Good_Chop.md]]'
- '[[Entities/Team_New_Ventures.md]]'
---

# Deo

## Role & Responsibilities

- **Title:** Product Manager - Good Chop
- **Team:** [[Entities/Team_New_Ventures.md|New Ventures & Ecosystems]]

### Primary Responsibilities

- Good Chop product strategy and execution
- OTP implementation for Good Chop
- Charge at Checkout rollout

## Current Projects

| Project | Role | Status |
|---------|------|--------|
| [[Projects/Good_Chop.md]] | Lead PM | Active |
| Good Chop OTP | Lead | W02 2026 Launch |

## Working Style (from NGO.md)

- **Strengths:** Execution
- **Development Area:** Strategic framing, conciseness in communication

## Key Relationships

- **Leadership:** Yury
- **Collaborators:** Alex Matlin (Engineering)

## Meeting Notes Format

Uses "Deo Format" for meeting notes:
- Header: Date | Topic | Attendees
- Notes/Project Updates: Bulleted list
- Action Items: Explicit list at bottom

## Changelog

- **2025-12-08:** Entity created from daily context synthesis