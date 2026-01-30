---
$schema: brain://entity/project/v1
$id: entity/project/squad-cross-selling-and-subscription-flexibility
$type: project
$version: 1
$created: '2026-01-22T08:31:01.214143Z'
$updated: '2026-01-30T10:22:43.368535'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/person/deo-nathaniel
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/a-dos-arbaaz-dossani
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/deo-nathaniel
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.214143Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.285950+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Cross Selling And Subscription Flexibility
---

# Squad: Cross Selling and Subscription Flexibility

## Metadata
- **Type**: Squad
- **Tribe**: Shopping Foundation
- **Slack**: `#squad-cross-selling-and-subscription-flexibility`
- **PM**: [[Deo Nathaniel]]
- **EM**: [[(A-Dos) Arbaaz Dossani]]
- **KPI (Q1 2026)**: Incremental Gross Revenue per Customer

## Focus & Scope
Responsible for Cross Selling and Subscription Flexibility within the Shopping Foundation tribe.

## Resources
- [More Information](Shopping Foundation & Customer Care)

## Jira Project
- Key: `XSELL`
- [Backlog Link](https://hellofresh.atlassian.net/jira/software/c/projects/XSELL/boards/4012/backlog - Can’t find link)

## Active Epics
- [XSELL-421] [Q1] XSELL MVP on React Native Home (Status: In Progress, Priority: Normal)
- [XSELL-406] Occasion Boxes Post Launch Q4 2025 (Status: Open, Priority: Normal)
- [XSELL-390] ChatGPT Recommender App + MCP POC (Status: Open, Priority: Normal)
- [XSELL-223] [MVP] X-sell UAT Issues (Status: Resolved, Priority: Normal)
- [XSELL-164] Cross Selling Post Launch Optimization Backlog (Status: Open, Priority: Normal)
- [XSELL-163] [Opt-Out] Cross Selling Post (Status: Open, Priority: Normal)
- [XSELL-33] [MVP] Cross Selling v1.0 (Status: Resolved, Priority: Normal)
- [XSELL-19] XSell Team setup (Status: Resolved, Priority: Normal)
- [XSELL-2] Cross Selling discovery (Status: Closed, Priority: Normal)
