---
$schema: brain://entity/project/v1
$id: entity/project/squad-factor-form
$type: project
$version: 1
$created: '2026-01-22T08:31:01.163981Z'
$updated: '2026-01-30T10:22:35.041203'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/person/hamed-karimian
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/pantelis-chatzinikolis
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/hamed-karimian
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.163981Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.201729+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Factor Form
---

# Squad: Factor Form

## Metadata
- **Type**: Squad
- **Tribe**: New Ventures
- **Slack**: `#squad-rte-vms-factor-form`
- **PM**: [[Hamed Karimian]]
- **EM**: [[Pantelis Chatzinikolis]]
- **KPI (Q1 2026)**: Factor Penetration %

## Focus & Scope
Responsible for Factor Form within the New Ventures tribe.

## Resources
- [Technical Domain / TRE](Factor Form / https://www.factor75.com/factorform)
- [More Information](Page: Squad: Factor Form)

## Jira Project
- Key: `RTEVMS`
- [Backlog Link](https://hellofresh.atlassian.net/jira/software/c/projects/RTEVMS/boards/3398)

## Active Epics
- [RTEVMS-2471] [Q1/26] Escaped Defects (Status: Backlog, Priority: Normal)
- [RTEVMS-2451] [Delivery] Quick Wins - Q1 2026 (Status: In Progress, Priority: Normal)
- [RTEVMS-2412] Introduce Meal Shake & Creatine to VMS assortment (Status: In Progress, Priority: Normal)
- [RTEVMS-2341] Shopify || Factor Form (Status: Backlog, Priority: Normal)
- [RTEVMS-2297] Possible Features (Status: Backlog, Priority: Normal)
- [RTEVMS-2296] [Bugs] Escaped Defects (Status: In Progress, Priority: Normal)
- [RTEVMS-2295] [Long Term] Product / Design Debt (Status: Backlog, Priority: Normal)
- [RTEVMS-2294] [Long Term] Action Items & Process Improvements (Status: In Progress, Priority: Normal)
- [RTEVMS-2283] [Q4/25] - Factor Form Peak Prep (Status: In Progress, Priority: Normal)
- [RTEVMS-2252] [KTLO] Keep The Lights On (Status: In Progress, Priority: Normal)

## Jira Status
*Auto-updated: 2026-01-30*

- **Active Epics:** 15
- **In Progress:** 15
- **Blockers:** 15

### Current Focus
- [RTEVMS-2423] [OTP][UAT] Dashboard shows past OTP orders in "shipping" sta
- [RTEVMS-2412] [NPD] Meal Shake & Creatine+ Products
- [RTEVMS-2471] [Q1/26] Escaped Defects

### Blockers
- [RTEVMS-2366] [Peak] Add new RTE XSELL voucher to fallback peak voucher se
- [RTEVMS-2371] [OTP][UAT] SnS Discount Should Show
- [RTEVMS-1117] [Retro] Audit SSR-able pages/components in FactorForm
