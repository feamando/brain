---
$schema: brain://entity/project/v1
$id: entity/project/squad-customers
$type: project
$version: 1
$created: '2026-01-22T08:31:01.130764Z'
$updated: '2026-01-30T10:22:35.032415'
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
  target: entity/project/vinay-mohan
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/fiona-lucas
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.130764Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.131424+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Customers
---

# Squad: Customers

## Metadata
- **Type**: Squad
- **Tribe**: Consumer Core
- **Slack**: `#squad-customers`
- **PM**: [[Fiona Lucas]]
- **EM**: [[Vinay Mohan]]
- **KPI (Q1 2026)**: No of API-v2 endpoints with live traffic - customer domain

## Focus & Scope
Responsible for Customers within the Consumer Core tribe.

## Resources

## Jira Project
- Key: `CUST`
- [Backlog Link](https://hellofresh.atlassian.net/jira/software/c/projects/CUST/boards/808)

## Active Epics
- [CUST-4164] Order Processing Service to not have any dependency on legacy customers API / Monolith (Status: Backlog, Priority: Normal)
- [CUST-4162] [CAS][M3]: Data Sync to CAS (Status: Backlog, Priority: Normal)
- [CUST-4161] [CAS][M4]: Make CAS the source of truth (Status: Backlog, Priority: Normal)
- [CUST-4151] [CAS][M2]: Read & Write Operations via CAS Proxy (Status: Backlog, Priority: Normal)
- [CUST-3996] Provision public.customer.v1beta5 Topic Without Default Locale Values (Status: Backlog, Priority: Normal)
- [CUST-3974] Verification over email of customer login & active journeys for malicious account access (Status: In Progress, Priority: High)
- [CUST-3969] Customer Address Modernization - Placeholder for Execution (Status: Backlog, Priority: Normal)
- [CUST-3962] Decommission Customers Intfood Sinkers via Consumer Migration (Status: Backlog, Priority: Normal)
- [CUST-3912] FTCP Program Customers Squad (Status: Backlog, Priority: Normal)
- [CUST-3731] Customer Address POST endpoint changes to unblock POC, Subscription extraction and Voucher attachment rollouts (Status: In Progress, Priority: Normal)
