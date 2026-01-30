---
$schema: brain://entity/project/v1
$id: entity/project/prateek-jajoo
$type: project
$version: 1
$created: '2026-01-22T08:31:01.134380Z'
$updated: '2026-01-22T10:41:35.138780+00:00'
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
  target: entity/project/the-pets-table
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.134380Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.138784+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 2
name: Prateek Jajoo
id: entity-prateek-jajoo
type: person
role: Staff PM - The Pets Table
last_updated: 2025-12-08
related:
- '[[Projects/The_Pets_Table.md]]'
- '[[Entities/Team_New_Ventures.md]]'
---

# Prateek Jajoo

## Role & Responsibilities

- **Title:** Staff Product Manager - The Pets Table (TPT)
- **Team:** [[Entities/Team_New_Ventures.md|New Ventures & Ecosystems]]
- **Joined:** Recently (as of Dec 2025)

### Primary Responsibilities

- TPT product strategy
- App development for pet health tracking
- Copy/terminology updates ("Meal" → "Recipe")

## Current Projects

| Project | Role | Status |
|---------|------|--------|
| [[Projects/The_Pets_Table.md]] | Lead PM | Active |
| TPT App | Lead | Discovery |

## Current Focus

- **App Development:** Defining smallest viable product for pet health tracking
- **Target Users:** "DINKs" (Dual Income No Kids) in metro areas
- **Key Initiative:** Login page and one-pager for TPT app

## Action Items (Current)

- [ ] Start work on login page and one-pager for TPT app
- [ ] Change copy "meal" → "recipe" (with Maria)

## Key Relationships

- **Manager:** Nikita Gorshkov
- **Collaborators:** Maria, Katrina (designer), Lindsay (commercial/surveys)

## Changelog
- **2025-12-11:** Context update: [ ] **Prateek Jajoo**: Start app login page/one-pager for TPT.
- **2025-12-09:** Context update: [ ] **Prateek Jajoo & Maria Chelminska**: Share prototype for tailored cancellation deflection with Beatrice Dimarucut.

- **2025-12-08:** Entity created from daily context synthesis