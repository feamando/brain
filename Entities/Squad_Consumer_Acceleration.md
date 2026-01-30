---
$schema: brain://entity/project/v1
$id: entity/project/squad-consumer-acceleration
$type: project
$version: 1
$created: '2026-01-22T08:31:01.106340Z'
$updated: '2026-01-22T10:41:35.091631+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/meggie-bouchard
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/kutlu-kartal
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.106340Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.091633+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Squad Consumer Acceleration
---

# Squad: Consumer Acceleration

## Metadata
- **Type**: Squad
- **Tribe**: Consumer Foundations
- **Slack**: `#squad-consumer-acceleration`
- **PM**: [[Meggie Bouchard]]
- **EM**: [[Kutlu Kartal]]
- **KPI (Q1 2026)**: Average number of production deployed features per mobile engineer

## Focus & Scope
Responsible for Consumer Acceleration within the Consumer Foundations tribe.

## Resources

## Jira Project
- Key: `ACCEL`
- [Backlog Link](https://hellofresh.atlassian.net/jira/software/c/projects/ACCEL/boards/7243 
Consumer Acceleration - Q4 2025 Roadmap)

## Active Epics
- [ACCEL-336] [Mobile] UI2 Migration for Chefsplate (Status: Open, Priority: Normal)
- [ACCEL-328] Localisation - Refactor Business Logic Keys (Status: Open, Priority: Normal)
- [ACCEL-327] ZEST - Figma-to-Code (Status: Open, Priority: Normal)
- [ACCEL-326] A11Y -  Document Best Practices (Status: Open, Priority: Normal)
- [ACCEL-325] ZEST - AI powered contribution model (Status: Open, Priority: Normal)
- [ACCEL-323] ZEST - Introduce composite layouts (Status: Open, Priority: Normal)
- [ACCEL-322] Lokalise - Automate the localization request process (Status: Open, Priority: Normal)
- [ACCEL-321] ZEST - Token Automation (Status: Open, Priority: Normal)
- [ACCEL-320] A11Y - Product teams own their compliance (Status: Open, Priority: Normal)
- [ACCEL-311] A11Y - ARIA & Tooling Improvements (RN: +25 rules, Web: +10 rules) (Status: Open, Priority: Normal)
