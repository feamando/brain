---
$schema: brain://entity/project/v1
$id: entity/project/squad-good-chop
$type: project
$version: 1
$created: '2026-01-22T08:31:01.201981Z'
$updated: '2026-01-30T10:22:43.356002'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/person/beatrice-dimarucut
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/person/alexander-matlin
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/beatrice-dimarucut
  confidence: 1.0
  last_verified: '2026-01-30'
- type: related_to
  target: entity/project/alexander-matlin
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.201981Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.263529+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Good Chop
---

# Squad: Good Chop

## Metadata
- **Type**: Squad
- **Tribe**: New Ventures
- **Slack**: `#squad-nv-good-chop`
- **PM**: [[Beatrice Dimarucut]]
- **EM**: [[Alexander Matlin]]
- **KPI (Q1 2026)**: Net Revenue

## Focus & Scope
Responsible for Good Chop within the New Ventures tribe.

## Resources
- [Technical Domain / TRE](Good Chop / https://www.goodchop.com/)
- [More Information](Page: Squad: Good Chop)

## Jira Project
- Key: `GOC`
- [Backlog Link](https://hellofresh.atlassian.net/jira/software/c/projects/GOC/boards/4046)

## Active Epics
- [GOC-3437] Price-Menu Experiment (Status: Backlog, Priority: Normal)
- [GOC-3434] Improve Value Communication (Status: Design, Priority: Normal)
- [GOC-3334] [P0] Honeycomb Monitoring & Alerting (Status: Backlog, Priority: Normal)
- [GOC-3255] Databricks alerts kick off (Status: Backlog, Priority: Normal)
- [GOC-3183] [Milestone 2] Improve Reactivations page (Status: Backlog, Priority: Normal)
- [GOC-3177] [MVP] One Time Purchase - Funnel (Status: In Development, Priority: Normal)
- [GOC-3139] [Milestone 2] One Time Purchase (Status: Design, Priority: Normal)
- [GOC-3118] Search V2 Pre-checkout (Status: Backlog, Priority: Normal)
- [GOC-3077] Menu experimentation (Status: Backlog, Priority: Normal)
- [GOC-3071] New Product card on Post-checkout (Status: Backlog, Priority: Normal)

## Jira Status
*Auto-updated: 2026-01-30*

- **Active Epics:** 15
- **In Progress:** 11
- **Blockers:** 15

### Current Focus
- [GOC-3477] Box benefits banner does not load at login
- [GOC-3489] Investigate issue with TR drop for repeat orders
- [GOC-3370] Add trace for discount banner component rendering

### Blockers
- [GOC-2122] [Runbook] Create one-off 4xx and 5xx runbook
- [GOC-3056] Post-Mortem for #in-52003-2508
- [GOC-2804] Post-mortem for INC-21897 (#in-48710-2505)
