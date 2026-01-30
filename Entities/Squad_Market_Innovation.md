---
$schema: brain://entity/project/v1
$id: entity/project/squad-market-innovation
$type: project
$version: 1
$created: '2026-01-22T08:31:01.210051Z'
$updated: '2026-01-30T10:22:30.912857'
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
  target: entity/person/wanderley-teixeira
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/wanderley-teixeira
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.210051Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.279222+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Market Innovation
---

# Squad: Market Innovation

## Metadata
- **Type**: Squad
- **Tribe**: New Ventures
- **Slack**: `#squad-market-io`
- **PM**: [[Sameer Doda]]
- **EM**: [[Wanderley Teixeira]]
- **KPI (Q1 2026)**: # Orders Confirmed

## Focus & Scope
Responsible for Market Innovation within the New Ventures tribe.

## Resources
- [Technical Domain / TRE](Project-based)
- [More Information](Page: Squad: Market Innovation (WIP))

## Jira Project
- Key: `MIO`
- [Backlog Link](https://hellofresh.atlassian.net/jira/software/c/projects/MIO/boards/8541)

## Active Epics
- [MIO-14] MIO Reteaming transition (Restructuring Tasks) (Status: In Progress, Priority: Normal)
- [MIO-13] Shopify | Factor Form (Status: In Progress, Priority: Normal)
- [MIO-12] On-call support (Status: Open, Priority: Normal)
- [MIO-11] HF CA Occasion Box (Status: Open, Priority: Normal)
- [MIO-10] HF ANZ Occasion Box (Status: Open, Priority: Normal)
- [MIO-9] Variable & Itemized pricing (Status: Open, Priority: Normal)
- [MIO-8] Manage Week Improvements (multi-address, seamless) (Status: Open, Priority: Normal)
- [MIO-7] Handover & Deprecation - TAM BE Services (Status: In Progress, Priority: Normal)
- [MIO-2] Second-Party Recipe Marketplace (Status: In Progress, Priority: Normal)
- [MIO-1] Benelux Premium Pricing (Status: In Progress, Priority: Normal)

## Jira Status
*Auto-updated: 2026-01-30*

- **Active Epics:** 10
- **In Progress:** 15
- **Blockers:** 0

### Current Focus
- [MIO-1] Benelux Premium Pricing
- [MIO-109] [Android][Milestone 0]: Menu Screen: Fix WeeklyNav UI for mi
- [MIO-119] Plan type switch does not send productType.family when Plans
