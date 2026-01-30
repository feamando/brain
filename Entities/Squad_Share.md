---
$schema: brain://entity/project/v1
$id: entity/project/squad-share
$type: project
$version: 1
$created: '2026-01-22T08:31:01.147254Z'
$updated: '2026-01-30T10:22:43.292185'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/rachna-ravi
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/person/paul-andrews
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/paul-andrews
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.147254Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.163935+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Share
---

# Squad: Share

## Metadata
- **Type**: Squad
- **Tribe**: Loyalty & Virality
- **Slack**: `#squad-share`
- **PM**: [[Rachna Ravi]]
- **EM**: [[Paul Andrews]]
- **KPI (Q1 2026)**: Organic HelloFresh app downloads from new sharing features

## Focus & Scope
Responsible for Share within the Loyalty & Virality tribe.

## Resources
- [More Information](Loyalty & Share Introduction)

## Jira Project
- Key: `SHA`
- [Backlog Link](https://hellofresh.atlassian.net/jira/software/c/projects/SHA/boards/8375/backlog - Can’t find link)

## Active Epics
- [SHA-264] Consolidate /referral , /referrals , as well as complete the partial UMK migration. (Status: Backlog, Priority: Normal)
- [SHA-196] Support credit to vouchers migration (Status: Backlog, Priority: Normal)
- [SHA-191] Share Squad Tech Discovery (Status: Backlog, Priority: Normal)
- [SHA-175] RAF to React Native - Supporting the Migration (Status: Backlog, Priority: Normal)
- [SHA-163] Adding kickbox to RAF email inputs (Status: Backlog, Priority: Normal)
- [SHA-162] Turn off RAF Page for Greenchef NL (GQ) (Status: Backlog, Priority: Low)
- [SHA-127] Audit of RAF entry points  (Status: Backlog, Priority: Normal)
- [SHA-126] Streamline translation setup for RAF (Status: Backlog, Priority: Normal)
- [SHA-115] System Improvements Q4: Mobile (Status: Backlog, Priority: Normal)
- [SHA-59] System Improvements Q4: Web (Status: Backlog, Priority: Normal)
