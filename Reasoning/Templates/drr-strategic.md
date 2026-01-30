---
$schema: brain://entity/project/v1
$id: entity/project/drr-strategic
$type: project
$version: 1
$created: YYYY-MM-DD
$updated: '2026-01-30T10:28:14.215926'
$confidence: 0.49
$source: unknown
$status: draft
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:02.173731Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Drr Strategic
id: drr-YYYY-MM-DD-[topic-slug]
type: strategic
valid_until: YYYY-MM-DD
assurance: L2
r_eff: 0.XX
related_project: '[[Projects/PROJECT_NAME.md]]'
stakeholders:
- '[[Entities/STAKEHOLDER.md]]'
board_approved: false
$orphan_reason: pending_enrichment
---

# Strategic Decision: [INITIATIVE NAME]

## Executive Summary

**Decision:** [One-line summary of the decision]

**Impact:** [High/Medium/Low]

**Investment:** [Budget range]

**Timeline:** [Implementation period]

## Strategic Context

### Business Situation
[Market conditions, competitive landscape, internal context]

### Strategic Alignment
- **Company mission:** [How this aligns]
- **Annual objectives:** [Which OKRs this supports]
- **Portfolio fit:** [Where this fits in overall strategy]

### Opportunity / Threat
[What happens if we do/don't act]

## Options Evaluated

| Option | Assurance | R_eff | NPV/ROI | Risk | Status |
|--------|-----------|-------|---------|------|--------|
| [Option A] | L2 | 0.XX | $XX / XX% | Med | **Selected** |
| [Option B] | L1 | 0.XX | $XX / XX% | High | Alternative |
| [Option C] | Invalid | - | - | - | Rejected |
| Do Nothing | L1 | 0.XX | $XX / XX% | High | Baseline |

### Option A: [Strategic Initiative Name]

**Description:**
[What this strategic option entails]

**Financial Analysis:**
| Metric | Year 1 | Year 2 | Year 3 | Total |
|--------|--------|--------|--------|-------|
| Revenue | $XX | $XX | $XX | $XX |
| Cost | $XX | $XX | $XX | $XX |
| Net | $XX | $XX | $XX | $XX |

**NPV:** $XX (at X% discount)
**IRR:** XX%
**Payback:** X months

**Strategic Benefits:**
- [Benefit 1]
- [Benefit 2]

**Risks:**
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk 1] | [H/M/L] | [H/M/L] | [Plan] |
| [Risk 2] | [H/M/L] | [H/M/L] | [Plan] |

### Option B: [Alternative]
[Similar structure]

### Option C: [Rejected Option]
**Rejection reason:** [Strategic rationale]

### Do Nothing Analysis
**Projected outcome:**
- [What happens without action]
- [Opportunity cost]
- [Competitive risk]

## Decision Criteria

| Criterion | Weight | Opt A | Opt B | Do Nothing |
|-----------|--------|-------|-------|------------|
| Strategic fit | 0.25 | X | X | X |
| Financial return | 0.25 | X | X | X |
| Risk profile | 0.20 | X | X | X |
| Execution feasibility | 0.15 | X | X | X |
| Competitive advantage | 0.15 | X | X | X |
| **Weighted Score** | | **X.X** | **X.X** | **X.X** |

## Selected Option

**Decision:** Option A - [Name]

**Rationale:**
[Strategic justification linking evidence to decision]

### WLNK Analysis
```
Evidence chain:
- Market analysis: 0.XX (CL2 - external research)
- Financial model: 0.XX (CL3 - internal analysis)
- Competitive intel: 0.XX (CL2 - industry sources)
- Pilot results: 0.XX (CL3 - internal validation)

R_eff = min(all) = 0.XX
```

## Evidence Chain

| Evidence | Type | CL | Weight | Expires | Source |
|----------|------|-----|--------|---------|--------|
| TAM analysis | research | CL2 | 0.XX | YYYY-MM-DD | [Report] |
| Financial model | analysis | CL3 | 0.XX | YYYY-MM-DD | Finance |
| Customer research | validation | CL3 | 0.XX | YYYY-MM-DD | [Study] |
| Competitor analysis | research | CL2 | 0.XX | YYYY-MM-DD | [Source] |

## Bias Audit

| Bias | Risk | Evidence | Mitigation |
|------|------|----------|------------|
| Confirmation | High | [Signs observed] | Red team exercise |
| Overconfidence | Med | [Optimistic projections] | Conservative scenarios |
| Groupthink | Med | [Leadership alignment] | External advisory |
| Sunk cost | Low/Med | [Prior investments] | Fresh analysis |
| Anchoring | Med | [Initial estimates] | Multiple scenarios |

**Red Team Findings:**
- [Challenge 1 and response]
- [Challenge 2 and response]

## Implementation Roadmap

### Phase 1: [Name] - QX YYYY
- [Key milestone 1]
- [Key milestone 2]
- **Go/No-Go criteria:** [Metrics]

### Phase 2: [Name] - QX YYYY
- [Key milestone 3]
- [Key milestone 4]
- **Go/No-Go criteria:** [Metrics]

### Phase 3: [Name] - QX YYYY
- [Scale/optimize]
- **Success criteria:** [Metrics]

## Resource Requirements

| Resource | Year 1 | Year 2 | Year 3 |
|----------|--------|--------|--------|
| Headcount | X FTE | X FTE | X FTE |
| CapEx | $XX | $XX | $XX |
| OpEx | $XX | $XX | $XX |
| External | $XX | $XX | $XX |

## Success Metrics

| Metric | Baseline | Y1 Target | Y2 Target | Y3 Target |
|--------|----------|-----------|-----------|-----------|
| [Revenue] | $XX | $XX | $XX | $XX |
| [Market share] | X% | X% | X% | X% |
| [Customer metric] | X | X | X | X |

## Governance

**Decision authority:** [Who approved]
**Review cadence:** [Quarterly/Monthly]
**Escalation path:** [If metrics miss]

## Conditions for Revisiting

This decision should be revisited if:
- [ ] Y1 metrics miss by >20%
- [ ] Market conditions change significantly
- [ ] Competitor makes major move
- [ ] Key assumptions prove false
- [ ] New strategic opportunity emerges
- [ ] Evidence expires (see chain)

## Appendices

- Financial model: [link]
- Market research: [link]
- Competitive analysis: [link]
- Risk register: [link]

---
*Created: YYYY-MM-DD | Author: [Name] | Status: Draft*
*Board Approval: Pending*
*Generated with FPF | R_eff: 0.XX*