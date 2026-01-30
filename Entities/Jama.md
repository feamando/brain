---
$schema: brain://entity/project/v1
$id: entity/project/jama
$type: project
$version: 1
$created: '2026-01-22T08:31:01.152898Z'
$updated: '2026-01-22T10:41:35.177632+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/team-consumer-core
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/team-new-ventures
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.152898Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.177637+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 10
name: Jama
id: entity-jama
type: person
role: VP of Product
last_updated: 2025-12-10
related:
- '[[Projects/OTP.md]]'
- '[[Projects/Good_Chop.md]]'
- '[[Projects/Factor_Form.md]]'
- '[[Entities/Team_Consumer_Core.md]]'
---

# Jama Musse

## Role & Responsibilities

- **Title:** VP of Product
- **Team:** [[Entities/Team_Consumer_Core.md|Consumer Core]]
- **Reports to:** Ed Boyes (CPO)

### Primary Responsibilities

- Product strategy and roadmap for Consumer Core
- OTP platform capabilities ownership
- Voucher and add-on functionality decisions
- Staffing and budget approvals
- Roadmap review meetings

## Key Topics

- **Voucher Application:** Key contact for OTP voucher limitations
- **Add-on Sales:** Discussions on enabling add-ons in OTP flow
- **Roadmap Reviews:** Monthly reviews for visibility

## Current Discussions

- Voucher application for one-time purchases (limitation)
- Add-on sales on OTP flow (limitation)
- Programs revival (capacity dependent, needs full funding)

## Key Relationships

- **Collaborators:** Sameer Doda, Nikita Gorshkov, Allison
- **Reports:** DACH Juices support project originated from Jama

## Action Items (Current)

- [ ] Roadmap review meeting coordination (with Sameer/Nikita)
- [ ] Discuss voucher and add-on limitations for OTP

## Changelog
- **2025-12-11:** Context update: [ ] **Jama Musse & Nikita Gorshkov**: Sit down with B2B team on HIPPA compliance needs.
- **2025-12-09:** Context update: ### Jama & Nikita 1:1 (Dec 9)

- **2025-12-08:** Entity created from daily context synthesis