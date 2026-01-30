---
$schema: brain://entity/project/v1
$id: entity/project/beatrice-dimarucut
$type: project
$version: 1
$created: '2026-01-22T08:31:01.174608Z'
$updated: '2026-01-22T10:41:35.221089+00:00'
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
  target: entity/project/squad-good-chop
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases:
- Beatrice
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.174608Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.221091+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Beatrice Dimarucut
id: entity-beatrice-dimarucut
type: person
role: PM - Good Chop
last_updated: 2025-12-12
related:
- '[[Entities/Team_New_Ventures.md]]'
- '[[Entities/Squad_Good_Chop.md]]'
- '[[Projects/Good_Chop.md]]'
---

# Beatrice Dimarucut

## Role & Responsibilities

- **Title:** Product Manager
- **Team:** [[Entities/Team_New_Ventures.md|New Ventures & Ecosystems]]
- **Squad:** [[Entities/Squad_Good_Chop.md|Good Chop]]
- **Reports to:** Nikita Gorshkov

### Primary Responsibilities

- Good Chop product roadmap and prioritization
- H1 2026 product planning (OTP launch, price value experiments, funnel cleanup)
- Charge at Checkout (C@C) documentation and troubleshooting

## Working Style (from NGO.md)

- **Strengths:** Ownership, attention to detail
- **Development Area:** Communication brevity

## Key Relationships

- **Manager:** Nikita Gorshkov
- **Collaborators:** Daniel Arias (Engineering), Yury Trofimov (Commercial)

## Action Items (Current)

- [ ] Document all charge checkout issues, including AL refund options and pre-cut off order sequences
- [ ] Conduct live test and process via Bob to understand correct sequence for pre-cut off orders
- [ ] Summarize Owl refund issues for Nikita
- [ ] Ask about reusing backend services for HelloFresh

## Career Development

- Nikita planning promo case for new CS5 role
- Candidate for midyear promotion (February)

## Changelog
- **2025-12-12:** Consolidated from duplicate Beatrice.md file
- **2025-12-11:** Context update: **GoC H1 2026 Product Prioritization (WIP):** Beatrice working on Good Chop H1 2026 priorities.
- **2025-12-11:** Context update: [ ] **Beatrice Dimarucut**: Summarize Owl refund issues for Nikita.
- **2025-12-09:** Context update: **Good Chop H1 Roadmap (Beatrice):** Prioritizing OTP launch, price value experiment (CVR/retention), foundational code cleanup in funnel.
- **2025-12-09:** Context update: [ ] **Prateek Jajoo & Maria Chelminska**: Share prototype for tailored cancellation deflection with Beatrice Dimarucut.
- **2025-12-08:** Entity created from daily context synthesis