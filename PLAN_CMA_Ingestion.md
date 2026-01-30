---
$schema: brain://entity/project/v1
$id: entity/project/plan-cma-ingestion
$type: project
$version: 10
$created: '2026-01-22T08:31:00.694069Z'
$updated: '2026-01-30T14:50:43.005555+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.694069Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Plan Cma Ingestion
$orphan_reason: no_external_data
---

# PLAN: CMA Knowledge Ingestion

**Objective:** Index and add "Consumer Mega Alliance" (CMA) knowledge to the Brain from the source Google Sheet.

**Source:** `1q55kO1Nku3iw5y1G2XfNX2O1bDXiRaJ8vYWEHoRkBlY` (CMA Squad overview)

## 1. Environment Setup
- [x] **Verify Jira Access:** Check if `jira_mcp` is usable to fetch Epics.
- [x] **Parse Source Data:** Extract the CSV structure from `AI_Guidance/Brain/Inbox/INBOX_2025-12-08-.md`.

## 2. Execution Loop (Per Tribe/Squad)

### Shopping Journey
- [x] Customer Profile (Wellney Yarra, Abbas Ali Awan)
- [x] Menu Discovery (Elisa Marku, Brandon Donato-Long)
- [x] Merchandising (Laura Mneimneh, Shruti Patil)
- [x] Feedback (Sandra Rozario, Luis Eduardo Talavera Rios)

### Shopping Foundation
- [x] Personalization (Tushar Raina, Bartosz Raciborski)
- [x] Cart (Xavier Sinclair Vale-Buisson, Tales Padua)
- [x] Shopping Platform (Priyank Khanna, Maxime Valy)
- [x] Customer Service Experience (Shishir Mishra, Amey Patil)
- [x] Cross Selling (Deo Nathaniel, Arbaaz Dossani)

### New Ventures
- [x] Factor Form (Hamed Karimian, Pantelis Chatzinikolis)
- [x] Good Chop (Beatrice Dimarucut, Alexander Matlin)
- [x] The Pets Table (Maria Chelminska, Ahmed Wagdi)
- [x] Market Innovation (Sameer Doda, Wanderley Teixeira)

### Consumer Core
- [x] Customers (Fiona Lucas, Vinay Mohan)
- [x] Plans (Fiona Lucas, Ekaterina Shemerey)
- [x] Deliveries & Orders (Fiona Lucas, Ahmed ElSebaei)
- [x] Monoliths (Fiona Lucas, Damian Tylczyński)

### Consumer Foundations
- [x] Consumer Acceleration (Meggie Bouchard, Kutlu Kartal)
- [x] Client Platform (Priscila Koeck Machado, Wellington Lima Freire)

### Engagement
- [x] Inspire (Lisa Trueblood, Edu Morôni)
- [x] Act (Remy Aldasoro, Wladimir Gaus)

### Loyalty & Virality
- [x] Share (Rachna Ravi, Paul Andrews)
- [x] Missions (Anshal Anand, Aleksei Akireikin)
- [x] Rewards (Thomas Gamper Feitoza, Bruno Klarin)

## 3. Knowledge Base Updates
- [x] **Create Squad Files:** `Brain/Entities/Squad_*.md`
- [x] **Create Person Files:** `Brain/Entities/*.md`
- [x] **Update Registry:** `Brain/registry.yaml`

## 4. Completion
- [x] Validate all links and references.
