---
$schema: brain://entity/project/v1
$id: entity/project/squad-the-pets-table
$type: project
$version: 1
$created: '2026-01-22T08:31:01.175847Z'
$updated: '2026-01-30T10:22:46.097830'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/person/maria-chelminska
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/person/ahmed-wagdi
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/ahmed-wagdi
  confidence: 1.0
  last_verified: '2026-01-30'
- type: related_to
  target: entity/project/maria-chelminska
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.175847Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.223319+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad The Pets Table
---

# Squad: The Pets Table

## Metadata
- **Type**: Squad
- **Tribe**: New Ventures
- **Slack**: `#squad-nv-pet-food`
- **PM**: [[Maria Chelminska]]
- **EM**: [[Ahmed Wagdi]]
- **KPI (Q1 2026)**: Net Revenue

## Focus & Scope
Responsible for The Pets Table within the New Ventures tribe.

## Resources
- [Technical Domain / TRE](The Pets Table / https://www.thepetstable.com/)
- [More Information](Page: Squad: Pet Food)

## Jira Project
- Key: `TPT`
- [Backlog Link](https://hellofresh.atlassian.net/jira/software/c/projects/TPT/boards/1836)

## Active Epics
- [TPT-2546] Enable Passwordless Sign up & Login for TPT (Status: Backlog, Priority: High)
- [TPT-2538] Enable passwordless signup on TPT (Status: Backlog, Priority: Normal)
- [TPT-2427] Sku Expansion (Status: Backlog, Priority: Normal)
- [TPT-2379] Digital feeding guide (Status: In Progress, Priority: Normal)
- [TPT-2360] [GEO] Generative Engine Optimization (Status: Backlog, Priority: Normal)
- [TPT-2326] Breed Specific Messages in the funnel  (Status: Backlog, Priority: Normal)
- [TPT-2218] Hide subscriptions of deceased dogs (Status: In Progress, Priority: Normal)
- [TPT-2178]  [GD] Refactor and Locators Migrate (Status: Backlog, Priority: Normal)
- [TPT-2177] [GD] Update Pet profile without retaking the quiz (Status: Backlog, Priority: Normal)
- [TPT-2176]  [GD] One-Click Add-ons (Status: Backlog, Priority: Normal)

## Jira Status
*Auto-updated: 2026-01-30*

- **Active Epics:** 15
- **In Progress:** 15
- **Blockers:** 8

### Current Focus
- [TPT-2603] Add 5 star icons on reviews in the sign up page
- [TPT-2602] Add new section with Product stats & Icons on sign up page
- [TPT-2569] Filter out cadence delivery options from edit address page

### Blockers
- [TPT-2575] Revamp the Signup Page
- [TPT-2546] Enable Passwordless Sign up & Login for TPT
- [TPT-2535] Update tracking events on the plans-selection page for New P
