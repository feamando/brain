---
$schema: brain://entity/project/v1
$id: entity/project/squad-monoliths
$type: project
$version: 1
$created: '2026-01-22T08:31:01.204924Z'
$updated: '2026-01-22T10:41:35.269470+00:00'
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
  target: entity/project/damian-tylczyski
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.204924Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.269474+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Monoliths
---

# Squad: Monoliths

## Metadata
- **Type**: Squad
- **Tribe**: Consumer Core
- **Slack**: `#monoliths`
- **PM**: [[Fiona Lucas]]
- **EM**: [[Damian Tylczyński]]
- **KPI (Q1 2026)**: 

## Focus & Scope
Responsible for Monoliths within the Consumer Core tribe.

## Resources

## Jira Project
- Key: `MNLTH`
- [Backlog Link](https://hellofresh.atlassian.net/jira/software/c/projects/MNLTH/boards/6124)

## Active Epics
- [MNLTH-1115] [UI] API-v2: Reactivation deprecation (Status: Backlog, Priority: Normal)
- [MNLTH-1114] [UI] API-v2: Customer Orders Flow deprecation (Status: Backlog, Priority: Normal)
- [MNLTH-1113] [UI] API-v2: Account Settings Flow deprecation (Status: Backlog, Priority: Normal)
- [MNLTH-1095] Support migration of Customer endpoints out of monolith (Status: In Progress, Priority: Normal)
- [MNLTH-1052] APIv2 Deprecation: Legacy ID Mapper (Status: Won't do, Priority: Normal)
- [MNLTH-1041] Deprecate Job Orchestrator (Status: Backlog, Priority: Normal)
- [MNLTH-1003] API-v2: Recurring Orders deprecation (Status: Backlog, Priority: Normal)
- [MNLTH-1001] API-v2: One Off deprecation (Status: In Discovery, Priority: Normal)
- [MNLTH-898] Migrate Legacy Subscription API Calls to Modern Domain APIs (Status: Backlog, Priority: Normal)
- [MNLTH-889] Complete the leftovers of - Meal preference extraction from BOB to Profile service (Status: Backlog, Priority: Normal)
