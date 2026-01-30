---
$schema: brain://entity/project/v1
$id: entity/project/squad-plans
$type: project
$version: 1
$created: '2026-01-22T08:31:01.161275Z'
$updated: '2026-01-22T10:41:35.195680+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/person/fiona-lucas
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/ekaterina-shemerey
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.161275Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.195683+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Plans
---

# Squad: Plans

## Metadata
- **Type**: Squad
- **Tribe**: Consumer Core
- **Slack**: `#squad-plans`
- **PM**: [[Fiona Lucas]]
- **EM**: [[Ekaterina Shemerey]]
- **KPI (Q1 2026)**: No of API-v2 endpoints with live traffic - subscription domain

## Focus & Scope
Responsible for Plans within the Consumer Core tribe.

## Resources

## Jira Project
- Key: `PLANS`
- [Backlog Link](https://hellofresh.atlassian.net/jira/software/c/projects/PLANS/boards/382)

## Active Epics
- [PLANS-4933] Unit Price migration to Plans Domain from subscription (Status: Backlog, Priority: Normal)
- [PLANS-4880] [UI] API-v2: Checkout deprecation (Status: In Progress, Priority: Normal)
- [PLANS-4764] Backend Services migration from Subscription call (Status: Backlog, Priority: Normal)
- [PLANS-4763] Payments domain not using subscriptions call (Status: Backlog, Priority: Normal)
- [PLANS-4762] Owl tool without Subscriptions call (Status: Backlog, Priority: Normal)
- [PLANS-4761] Reactivations funnel without Subscriptions call (Status: Backlog, Priority: Normal)
- [PLANS-4760] Referrals without GET Subscriptions call (Status: Backlog, Priority: Normal)
- [PLANS-4759] Loyalty and Rewards Funnel without GET Subscriptions call (Status: Backlog, Priority: Normal)
- [PLANS-4758] Cancellations Funnel without Subscriptions call (Status: Backlog, Priority: Normal)
- [PLANS-4881] [UI] API-v2: One-Off Flow deprecation (Status: In Progress, Priority: Normal)
