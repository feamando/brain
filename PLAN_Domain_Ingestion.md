---
$schema: brain://entity/project/v1
$id: entity/project/plan-domain-ingestion
$type: project
$version: 8
$created: '2026-01-22T08:31:00.692989Z'
$updated: '2026-01-30T15:22:31.429765'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: has_contributor
  target: entity/person/nikita-gorshkov
  confidence: 0.7
  last_verified: '2026-01-30'
  source: test
- type: similar_to
  target: entity/project/plan-cma-ingestion
  confidence: 0.7064
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.65
- type: similar_to
  target: entity/project/plan-strategy-indexing
  confidence: 0.6823
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.65
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.692989Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Plan Domain Ingestion
---

# PLAN: Domain Strategy Ingestion

**Objective:** Ingest high-level strategy (Domain Objectives, Yearly Plans, Leadership) from "DOs & YPs Configuration".

**Source:** `1DwsNzmbIYucZ65ehMZ74KDo_wMTX03yPfq4JNyZcrto`

## 1. Data Acquisition
- [x] **Fetch Sheet Content:** Use `gdrive_mcp` to read the specific sheet ID.
- [x] **Archive:** Save raw content to `AI_Guidance/Brain/Inbox/RAW_Strategy_Config.md`.

## 2. Ingestion Logic (Script)
- [x] **Parse Tab 2 (DOs & YPs):**
    - Columns: Domain, Alliance, Commercial Leader, Tech Leader, Approver, Domain Objective Doc (Link), Yearly Plan Doc (Link).
    - **Action:** Create `Brain/Entities/Domain_[Name].md`.
    - **Action:** Create `Brain/Strategy/[Alliance]_YP_2026.md` (stub/link).
    - **Action:** Create/Update Person entities for Leaders/Approvers.
- [x] **Parse Tab 5 (Projects):**
    - Map Projects to Domains/Alliances if possible.

## 3. Brain Updates
- [x] **Register Domains:** Add to `registry.yaml`.
- [x] **Linkage:** Ensure Tribes/Squads (from previous task) can ideally be linked to these Alliances (manual or fuzzy match).

## 4. Execution
- [x] Run `AI_Guidance/Tools/domain_brain_ingest.py`.
