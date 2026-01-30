---
$schema: brain://entity/project/v1
$id: entity/project/squad-shopping-platform
$type: project
$version: 1
$created: '2026-01-22T08:31:01.097751Z'
$updated: '2026-01-30T10:22:46.116671'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/person/priyank-khanna
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/person/maxime-valy
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/priyank-khanna
  confidence: 1.0
  last_verified: '2026-01-30'
- type: related_to
  target: entity/project/maxime-valy
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.097751Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.077844+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Shopping Platform
---

# Squad: Shopping Platform

## Metadata
- **Type**: Squad
- **Tribe**: Shopping Foundation
- **Slack**: `#squad-shopping-platform`
- **PM**: [[Priyank Khanna]]
- **EM**: [[Maxime Valy]]
- **KPI (Q1 2026)**: Feature GTM Speed and Coverage

## Focus & Scope
Responsible for Shopping Platform within the Shopping Foundation tribe.

## Resources
- [More Information](Shopping Foundation & Customer Care)

## Jira Project
- Key: `SHOP`
- [Backlog Link](https://hellofresh.atlassian.net/jira/software/c/projects/SHOP/boards/1511/backlog?epics=visible&issueParent=3235102 - Can’t find link)

## Active Epics
- [SHOP-4059] FTCP (Status: Backlog, Priority: Normal)
- [SHOP-4041] Product Attribute Based Filtering (Status: Backlog, Priority: Normal)
- [SHOP-4027] CCM Bulk Upload follow ups (Status: Backlog, Priority: Normal)
- [SHOP-3991] Menu Pre live checks and QA (Status: Backlog, Priority: Normal)
- [SHOP-3853] Update web client to use new search endpoint (Status: In Progress, Priority: Normal)
- [SHOP-3847] Menu Search Backend (Status: In Progress, Priority: Normal)
- [SHOP-3761] P500 - Shopping Platform Performance Upgrade and Readiness (Status: In Progress, Priority: High)
- [SHOP-3589] GraphQL Schema Changes/Upgrades - Q4 onwards (Status: In Progress, Priority: High)
- [SHOP-3552] Enable Product Segments for tiered plans (Status: Won't do, Priority: Normal)
- [SHOP-3506] Deprecation of Sections, Collections, Groutype (Status: Backlog, Priority: Normal)
