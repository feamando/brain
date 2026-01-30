---
$schema: brain://entity/project/v1
$id: entity/project/sameer-doda
$type: project
$version: 1
$created: '2026-01-22T08:31:01.099939Z'
$updated: '2026-01-22T10:41:35.081646+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/team-new-ventures
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/influencer-marketplace
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/good-chop
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/factor-form
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.099939Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.081649+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 4
name: Sameer Doda
id: entity-sameer-doda
type: person
role: PM - New Ventures
last_updated: 2025-12-08
related:
- '[[Projects/Influencer_Marketplace.md]]'
- '[[Projects/Good_Chop.md]]'
- '[[Projects/Factor_Form.md]]'
- '[[Entities/Team_New_Ventures.md]]'
---

# Sameer Doda

## Role & Responsibilities

- **Title:** Product Manager - New Ventures
- **Team:** [[Entities/Team_New_Ventures.md|New Ventures & Ecosystems]]
- **Reports to:** Nikita Gorshkov

### Primary Responsibilities

- **Influencer Marketplace:** MVP Squad Lead, driving prototype & validate phase
- **Good Chop Shopify:** Leading migration project (more complex than Factor Form)
- **Factor Form Shopify:** Supporting Allison on platform work
- **DACH Juices Support:** Nordic markets Pfand implementation

## Current Projects

| Project | Role | Status |
|---------|------|--------|
| [[Projects/Influencer_Marketplace.md]] | MVP Squad Lead | Active - Phase 3 |
| [[Projects/Good_Chop.md]] | Lead PM | Active |
| [[Projects/Factor_Form.md]] | Support | Active |
| DACH Juices (Pfand) | Lead | Planning |

## Working Style

- **Strengths:** Execution, detail-oriented, multi-project management
- **Collaboration:** Works closely with Allison on Shopify projects, Shay on design

## Key Relationships

- **Manager:** Nikita Gorshkov
- **Collaborators:** Allison (platform), Shay (design), Jama (roadmap)
- **Stakeholders:** Ian Brooks, Annette MvdE

## Action Items (Current)

- [ ] Set up session with physical product team for HelloFresh Canada (Q1 alignment)
- [ ] Create requirements document for DACH Juices Pfand implementation
- [ ] Review low-fidelity designs with Nikita and Shay for Influencer Marketplace
- [ ] Connect with Jama on roadmap review meeting

## Notes

- Manages workload well, Allison assists on platform projects
- Concerned about frontend resource constraints for multiple projects
- Prefers visual roadmap view for presentations

## Changelog
- **2025-12-11:** Context update: [ ] **Sameer Doda**: Contact payments team to finalize migration of credits approach.

- **2025-12-08:** Entity created from daily context synthesis