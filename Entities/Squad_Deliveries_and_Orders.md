---
$schema: brain://entity/project/v1
$id: entity/project/squad-deliveries-and-orders
$type: project
$version: 1
$created: '2026-01-22T08:31:01.194435Z'
$updated: '2026-01-30T10:22:37.146092'
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
  target: entity/person/ahmed-elsebaei
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/ahmed-elsebaei
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.194435Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.251209+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Deliveries And Orders
---

# Squad: Deliveries & Orders

## Metadata
- **Type**: Squad
- **Tribe**: Consumer Core
- **Slack**: `#squad-deliveries-platform
#squad-customer-orders`
- **PM**: [[Fiona Lucas]]
- **EM**: [[Ahmed ElSebaei]]
- **KPI (Q1 2026)**: No of API-v2 endpoints with live traffic - deliveries domain

## Focus & Scope
Responsible for Deliveries & Orders within the Consumer Core tribe.

## Resources

## Jira Project
- Key: `DPLAT`
- [Backlog Link](Deliveries https://hellofresh.atlassian.net/jira/software/c/projects/DPLAT/boards/1749 
Orders https://hellofresh.atlassian.net/jira/software/c/projects/CO/boards/821)

## Active Epics
- [DPLAT-2621] Deliveries Count API Implementation (Status: Open, Priority: Normal)
- [DPLAT-2620] Order Enrichment Trigger: CDPS API (Status: Open, Priority: Normal)
- [DPLAT-2615] [M10] Cleanup (Status: Grooming, Priority: Normal)
- [DPLAT-2398] [M8] Source of Truth Rollout (Status: In Development, Priority: Normal)
- [DPLAT-2346] Unify the delivery cadence systems (Status: Open, Priority: Normal)
- [DPLAT-2278] [M9] Intfood backfills decommissioned  (Status: In Development, Priority: Normal)
- [DPLAT-2273] [M9] Use CDPSv2 as source for APIv2 Read API (Status: In Development, Priority: Normal)
- [DPLAT-2269] [M4] Complete Delivery & Delivery Plan Write API (Status: In Development, Priority: Normal)
- [DPLAT-2253] [M7] Implement Data Syncing & Backfill (Status: In Development, Priority: Normal)
- [DPLAT-2098] CDPS cutoff observability fix (Status: Open, Priority: Normal)
