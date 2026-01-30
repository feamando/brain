---
$schema: brain://entity/project/v1
$id: entity/project/squad-customer-service-experience
$type: project
$version: 1
$created: '2026-01-22T08:31:01.155208Z'
$updated: '2026-01-30T10:22:41.271150'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/person/shishir-mishra
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/person/amey-patil
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/amey-patil
  confidence: 1.0
  last_verified: '2026-01-30'
- type: related_to
  target: entity/project/shishir-mishra
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.155208Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.186321+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Customer Service Experience
---

# Squad: Customer Service Experience

## Metadata
- **Type**: Squad
- **Tribe**: Shopping Foundation
- **Slack**: `#squad-customer-service-experience`
- **PM**: [[Shishir Mishra]]
- **EM**: [[Amey Patil]]
- **KPI (Q1 2026)**: Self Service Rate

## Focus & Scope
Responsible for Customer Service Experience within the Shopping Foundation tribe.

## Resources
- [More Information](Shopping Foundation & Customer Care)

## Jira Project
- Key: `AGNTX`
- [Backlog Link](https://hellofresh.atlassian.net/jira/software/c/projects/AGNTX/boards/1315)

## Active Epics
- [AGNTX-4316] Owl Enhancements (Status: Open, Priority: Normal)
- [AGNTX-4124] Logistics Errors in CERT V2  (Status: Open, Priority: Normal)
- [AGNTX-4099] Photo uploads in CERT (Status: Open, Priority: Normal)
- [AGNTX-4028] Voicebot : Use case 2 (Status: Closed, Priority: Normal)
- [AGNTX-4027] Voicebot : Use case 1 (Status: Closed, Priority: Normal)
- [AGNTX-4026] Voicebot : Create Foundation (Status: Closed, Priority: Normal)
- [AGNTX-3974] Migrate to FTCP (Status: Open, Priority: Normal)
- [AGNTX-3730] [CBS] Migrate ChatBot Admin UI to SCM Customer Care Module (Status: Closed, Priority: High)
- [AGNTX-3686] Chatbot : Service Desk & Requests (Status: Open, Priority: Normal)
- [AGNTX-3674] M3 - Model Result Ingestion -Global Fraud Policy (Status: Open, Priority: Normal)
