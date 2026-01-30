---
$schema: brain://entity/project/v1
$id: entity/project/squad-cart
$type: project
$version: 1
$created: '2026-01-22T08:31:01.139735Z'
$updated: '2026-01-30T10:22:46.130529'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/xavier-sinclair-vale-buisson
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/person/tales-padua
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/tales-padua
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.139735Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.152598+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Cart
---

# Squad: Cart

## Metadata
- **Type**: Squad
- **Tribe**: Shopping Foundation
- **Slack**: `#squad-cart-foundation`
- **PM**: [[Xavier Sinclair Vale-Buisson]]
- **EM**: [[Tales Padua]]
- **KPI (Q1 2026)**: Meal Selection Data Consistency

## Focus & Scope
Responsible for Cart within the Shopping Foundation tribe.

## Resources
- [More Information](Shopping Foundation & Customer Care)

## Jira Project
- Key: `MPC`
- [Backlog Link](https://hellofresh.atlassian.net/jira/software/c/projects/MPC/boards/1666/backlog - Can’t find link)

## Active Epics
- [MPC-2286] Stop relying on data from APIv2 in Cart Domain (Status: Backlog, Priority: Normal)
- [MPC-2217] Post-lock change improvements (Status: In Progress, Priority: Normal)
- [MPC-2108] [incident_response_action][MAS] Split save API into 3 distinct operations (Status: Backlog, Priority: Normal)
- [MPC-2077] Fix customer selection functionality (Status: In Progress, Priority: Normal)
- [MPC-2019] Automated Customer Selection Handling for Menu Modifications (Status: Backlog, Priority: Normal)
- [MPC-1982] Cart TA Milestone #3 - Switch Source of Truth for Addon Selections (Status: Backlog, Priority: Normal)
- [MPC-1981] Support Shift Left in Data Strategy  (Status: Backlog, Priority: Normal)
- [MPC-1980] Publish Cart events to Cart Kafka (Status: Backlog, Priority: Normal)
- [MPC-1979] Migrate Shopping Platform Kubernetes services to FTCP (Status: Backlog, Priority: Normal)
- [MPC-1978] Discovery for selection reset issues and use-cases (Status: Backlog, Priority: Normal)
