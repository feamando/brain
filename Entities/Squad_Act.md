---
$schema: brain://entity/project/v1
$id: entity/project/squad-act
$type: project
$version: 1
$created: '2026-01-22T08:31:01.143632Z'
$updated: '2026-01-30T10:22:41.220894'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/remy-aldasoro
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/person/wladimir-gaus
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/wladimir-gaus
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.143632Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.158521+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Act
---

# Squad: Act

## Metadata
- **Type**: Squad
- **Tribe**: Engagement
- **Slack**: `#squad-act`
- **PM**: [[Remy Aldasoro]]
- **EM**: [[Wladimir Gaus]]
- **KPI (Q1 2026)**: Daily active users to monthly active users ratio for the HelloFresh app

## Focus & Scope
Responsible for Act within the Engagement tribe.

## Resources

## Jira Project
- Key: `ACT`
- [Backlog Link](https://hellofresh.atlassian.net/jira/software/c/projects/ACT/boards/9008/timeline)

## Active Epics
- [ACT-204] Planner - Post cut-off (Status: In Progress, Priority: High)
- [ACT-158] Smart Auto-Planner (Status: Open, Priority: Normal)
- [ACT-157] Physical-Digital Bridge (Status: Open, Priority: Normal)
- [ACT-156] Planner - Subscription Pre-Cutoff (Status: Open, Priority: Normal)
- [ACT-67] Planner - Orders Management (Status: Open, Priority: Normal)
- [ACT-66] Planner - Profile & Automation (Status: Open, Priority: Normal)
- [ACT-65] Planner - Integrations (iCal, GoogleCalendar) (Status: Open, Priority: Normal)
- [ACT-64] Planner - Week & Calendar views (Status: Open, Priority: Normal)
- [ACT-61] 🧑🏼‍🍳 Cooking - Ratings & Review  (Status: Closed, Priority: Normal)
- [ACT-58] Peak Readiness (Status: Closed, Priority: Normal)
