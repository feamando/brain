---
$schema: brain://entity/project/v1
$id: entity/project/drr-process
$type: project
$version: 1
$created: YYYY-MM-DD
$updated: '2026-01-30T10:28:14.212524'
$confidence: 0.49
$source: unknown
$status: draft
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:02.171900Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Drr Process
id: drr-YYYY-MM-DD-[topic-slug]
type: process
valid_until: YYYY-MM-DD
assurance: L2
r_eff: 0.XX
related_project: '[[Projects/PROJECT_NAME.md]]'
stakeholders:
- '[[Entities/STAKEHOLDER.md]]'
$orphan_reason: pending_enrichment
---

# Process Change: [PROCESS NAME]

## Context

### Current Process
[Describe the existing workflow]

```
[Current State Diagram - optional]
Step 1 → Step 2 → Step 3 → Outcome
```

### Pain Points
- [Pain point 1 - with metrics if available]
- [Pain point 2]
- [Pain point 3]

### Trigger for Change
[What prompted this evaluation]

## Options Evaluated

| Option | Assurance | R_eff | Impact | Status |
|--------|-----------|-------|--------|--------|
| [Option A] | L2 | 0.XX | High | **Selected** |
| [Option B] | L1 | 0.XX | Medium | Alternative |
| Status Quo | L1 | 0.XX | None | Baseline |

### Option A: [Process Change Name]

**Description:**
[What changes in the new process]

```
[Proposed State Diagram]
Step 1 → New Step → Step 3 → Better Outcome
```

**Expected Improvements:**
| Metric | Current | Expected | Improvement |
|--------|---------|----------|-------------|
| Cycle time | X days | Y days | Z% reduction |
| Error rate | X% | Y% | Z% reduction |
| Cost/unit | $X | $Y | Z% savings |

**Implementation Effort:**
- Team training: [X hours/days]
- Tool changes: [Description]
- Transition period: [X weeks]

### Option B: [Alternative]
[Similar structure]

### Status Quo Analysis
**Why change is needed:**
- [Reason 1 with evidence]
- [Reason 2 with evidence]

**Cost of inaction:**
- [Quantified cost/risk]

## Selected Option

**Decision:** Option A - [Name]

**Rationale:**
[Why this process change was selected]

### WLNK Analysis
```
Evidence:
- Pilot results: 0.XX (CL3)
- Industry benchmark: 0.XX (CL2)
- Team feedback: 0.XX (CL3)

R_eff = 0.XX
```

## Evidence Chain

| Evidence | Type | CL | Weight | Expires |
|----------|------|-----|--------|---------|
| Pilot program results | validation | CL3 | 0.XX | YYYY-MM-DD |
| Team survey | research | CL3 | 0.XX | YYYY-MM-DD |
| Industry case study | research | CL2 | 0.XX | YYYY-MM-DD |

## Bias Audit

| Bias | Risk | Mitigation |
|------|------|------------|
| Status quo | [Resistance to change] | Quantified pain points |
| Novelty | [Excitement for new] | Pilot before rollout |
| Authority | [Management preference] | Team input gathered |

## Change Management Plan

### Communication
1. [Announcement to stakeholders]
2. [Training schedule]
3. [Support channels]

### Rollout Phases
1. **Pilot:** [Team/timeframe]
2. **Expand:** [Groups/timeframe]
3. **Full rollout:** [Date]

### Success Metrics
| Metric | Baseline | Target | Measure Date |
|--------|----------|--------|--------------|
| [Metric 1] | X | Y | YYYY-MM-DD |
| [Metric 2] | X | Y | YYYY-MM-DD |

### Rollback Criteria
Process will be rolled back if:
- [Criterion 1]
- [Criterion 2]

## Conditions for Revisiting

- [ ] Success metrics not met after [X] months
- [ ] Team size changes significantly
- [ ] New tools become available
- [ ] Business context shifts
- [ ] Evidence expires

---
*Created: YYYY-MM-DD | Author: [Name] | Status: Draft*
*Generated with FPF | R_eff: 0.XX*