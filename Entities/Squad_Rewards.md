---
$schema: brain://entity/project/v1
$id: entity/project/squad-rewards
$type: project
$version: 1
$created: '2026-01-22T08:31:01.181659Z'
$updated: '2026-01-30T10:22:35.036889'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/person/thomas-gamper-feitoza
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/bruno-klarin
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/thomas-gamper-feitoza
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.181659Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.231110+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Rewards
---

# Squad: Rewards

## Metadata
- **Type**: Squad
- **Tribe**: Loyalty & Virality
- **Slack**: `#squad-rewards`
- **PM**: [[Thomas Gamper Feitoza]]
- **EM**: [[Bruno Klarin]]
- **KPI (Q1 2026)**: Percent of earned rewards redeemed

## Focus & Scope
Responsible for Rewards within the Loyalty & Virality tribe.

## Resources
- [More Information](Loyalty & Share Introduction)

## Jira Project
- Key: `REW`
- [Backlog Link](https://hellofresh.atlassian.net/jira/software/c/projects/REW/boards/8441/backlog - Can’t find link)

## Active Epics
- [REW-157] Add visual feedback for applied benefits across all touchpoints (Status: Open, Priority: Normal)
- [REW-156] Saving Reassurance on Home (Status: Open, Priority: Normal)
- [REW-155] Fix benefit application logic for selection-required benefits (Status: Open, Priority: Normal)
- [REW-154] Cancellation handover (Status: Open, Priority: Normal)
- [REW-103] Loyalty 2.0 MVP (Status: In Progress, Priority: Normal)
- [REW-94]   Monolith deprecation second part (Status: Open, Priority: Normal)
- [REW-60] Allocation Deprecation (Status: Open, Priority: Normal)
- [REW-35] RN training (Status: In Progress, Priority: Normal)
- [REW-34] RN migration of remaining native TRE (Status: Open, Priority: Normal)
- [REW-33] 2025 Peak preparation (Status: Resolved, Priority: Normal)
