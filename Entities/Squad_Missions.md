---
$schema: brain://entity/project/v1
$id: entity/project/squad-missions
$type: project
$version: 1
$created: '2026-01-22T08:31:01.123441Z'
$updated: '2026-01-22T10:41:35.117909+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/anshal-anand
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/aleksei-akireikin
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.123441Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.117910+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Missions
---

# Squad: Missions

## Metadata
- **Type**: Squad
- **Tribe**: Loyalty & Virality
- **Slack**: `#squad-missions`
- **PM**: [[Anshal Anand]]
- **EM**: [[Aleksei Akireikin]]
- **KPI (Q1 2026)**: Percent of eligible customers who complete a mission

## Focus & Scope
Responsible for Missions within the Loyalty & Virality tribe.

## Resources
- [More Information](Loyalty & Share Introduction)

## Jira Project
- Key: `LCORE`
- [Backlog Link](https://hellofresh.atlassian.net/jira/software/c/projects/LCORE/boards/4497/backlog - Can’t find link)

## Active Epics
- [LCORE-2087] [React Native] Bugs (Status: Open, Priority: Normal)
- [LCORE-2003] [2ew] Data pipeline maintenance (Status: Open, Priority: Normal)
- [LCORE-2002] [2ew] Housekeeping (CAS refactoring) (Status: Open, Priority: Normal)
- [LCORE-2001] [1ew] Reliability (Status: Open, Priority: Normal)
- [LCORE-2000] [1ew] Security (Status: Open, Priority: Normal)
- [LCORE-1999] [5.5ew] Observability (Status: Open, Priority: Normal)
- [LCORE-1998] [0.5ew] Opt-in (manually) (Status: Open, Priority: Normal)
- [LCORE-1997] [2ew] Display the balance (Status: Open, Priority: Normal)
- [LCORE-1996] [4.5ew] Display the touchpoints (Status: Open, Priority: Normal)
- [LCORE-1995] [4.5ew] Progression: Point engine (Status: Open, Priority: Normal)
