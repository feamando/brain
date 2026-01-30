---
$schema: brain://entity/project/v1
$id: entity/project/drr-build-vs-buy
$type: project
$version: 1
$created: YYYY-MM-DD
$updated: '2026-01-30T10:28:14.214191'
$confidence: 0.49
$source: unknown
$status: draft
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:02.172784Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Drr Build Vs Buy
id: drr-YYYY-MM-DD-[topic-slug]
type: build-vs-buy
valid_until: YYYY-MM-DD
assurance: L2
r_eff: 0.XX
related_project: '[[Projects/PROJECT_NAME.md]]'
stakeholders:
- '[[Entities/STAKEHOLDER.md]]'
$orphan_reason: pending_enrichment
---

# Build vs Buy Decision: [CAPABILITY/SYSTEM NAME]

## Context

### Business Need
[What capability is needed and why]

### Current State
[How is this handled today, if at all]

### Urgency
- **Time to value:** [When is this needed]
- **Competitive pressure:** [Market context]

## Options Evaluated

| Option | Type | Assurance | R_eff | TCO (3yr) | Status |
|--------|------|-----------|-------|-----------|--------|
| Build in-house | Build | LX | 0.XX | $XXX | [Status] |
| Vendor A | Buy | LX | 0.XX | $XXX | [Status] |
| Vendor B | Buy | LX | 0.XX | $XXX | [Status] |
| Hybrid | Both | LX | 0.XX | $XXX | [Status] |

### Option 1: Build In-House

**Description:** [What building entails]

**Cost Analysis:**
| Item | Year 1 | Year 2 | Year 3 | Total |
|------|--------|--------|--------|-------|
| Development | $XX | $XX | $XX | $XX |
| Maintenance | $XX | $XX | $XX | $XX |
| Infrastructure | $XX | $XX | $XX | $XX |
| **Total** | $XX | $XX | $XX | **$XX** |

**Pros:**
- Full control over roadmap
- No vendor lock-in
- Custom to our needs
- IP ownership

**Cons:**
- Longer time to market
- Requires specialized talent
- Ongoing maintenance burden
- Opportunity cost

**Risk Factors:**
- Team availability: [Low/Med/High]
- Technical complexity: [Low/Med/High]
- Scope creep: [Low/Med/High]

### Option 2: Buy (Vendor A)

**Vendor:** [Name]
**Product:** [Product name]

**Cost Analysis:**
| Item | Year 1 | Year 2 | Year 3 | Total |
|------|--------|--------|--------|-------|
| License | $XX | $XX | $XX | $XX |
| Implementation | $XX | - | - | $XX |
| Integration | $XX | $XX | $XX | $XX |
| Support | $XX | $XX | $XX | $XX |
| **Total** | $XX | $XX | $XX | **$XX** |

**Pros:**
- Faster time to market
- Proven solution
- Vendor handles maintenance
- Lower initial investment

**Cons:**
- Vendor dependency
- Limited customization
- Recurring costs
- Feature roadmap not in our control

**Risk Factors:**
- Vendor stability: [Low/Med/High]
- Lock-in risk: [Low/Med/High]
- Integration complexity: [Low/Med/High]

### Option 3: Hybrid Approach

**Description:** [What hybrid entails - e.g., buy core, build integrations]

[Similar structure]

## Decision Criteria

| Criterion | Weight | Build | Vendor A | Vendor B |
|-----------|--------|-------|----------|----------|
| Time to market | 0.25 | 2/5 | 4/5 | 4/5 |
| Total cost (3yr) | 0.20 | 3/5 | 4/5 | 3/5 |
| Customization | 0.15 | 5/5 | 2/5 | 3/5 |
| Maintenance burden | 0.15 | 2/5 | 4/5 | 4/5 |
| Strategic alignment | 0.15 | 4/5 | 3/5 | 3/5 |
| Risk profile | 0.10 | 3/5 | 4/5 | 3/5 |
| **Weighted Score** | | **X.X** | **X.X** | **X.X** |

## Selected Option

**Decision:** [Build / Buy Vendor X / Hybrid]

**Rationale:**
[Explain the decision based on evidence and criteria]

### WLNK Analysis
```
Evidence scores:
- Cost analysis: 0.XX (CL3 - internal data)
- Vendor evaluation: 0.XX (CL2 - demos + references)
- Market research: 0.XX (CL2 - Gartner/Forrester)

R_eff = min(scores) = 0.XX
```

## Evidence Chain

| Evidence | CL | Weight | Expires | Source |
|----------|-----|--------|---------|--------|
| TCO model | CL3 | 0.XX | YYYY-MM-DD | Finance analysis |
| Vendor demos | CL2 | 0.XX | YYYY-MM-DD | [dates] |
| Reference calls | CL2 | 0.XX | YYYY-MM-DD | [customers] |
| Market analysis | CL2 | 0.XX | YYYY-MM-DD | [report] |

## Bias Audit

| Bias | Risk | Mitigation |
|------|------|------------|
| NIH (Not Invented Here) | [Med/High for Build bias] | [Mitigation] |
| Vendor influence | [Med/High for Buy bias] | [Mitigation] |
| Sunk cost | [If prior investment] | [Mitigation] |
| Recency | [Recent success/failure influence] | [Mitigation] |

## Implementation Plan

### If Build:
1. [Phase 1: Design]
2. [Phase 2: MVP]
3. [Phase 3: Full implementation]

### If Buy:
1. [Procurement]
2. [Implementation]
3. [Integration]
4. [Training]

## Exit Strategy

**If Build fails:**
- [Contingency plan]
- [Pivot criteria]

**If Buy fails:**
- [Data export capabilities]
- [Alternative vendors]
- [Rebuild timeline]

## Conditions for Revisiting

- [ ] Vendor pricing changes >20%
- [ ] Our requirements change significantly
- [ ] New market entrants emerge
- [ ] Build team becomes available
- [ ] Evidence expires (see chain)

---
*Created: YYYY-MM-DD | Author: [Name] | Status: Draft*
*Generated with FPF | R_eff: 0.XX*