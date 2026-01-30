---
$schema: brain://entity/project/v1
$id: entity/project/drr-architecture
$type: project
$version: 1
$created: YYYY-MM-DD
$updated: '2026-01-30T10:28:14.217650'
$confidence: 0.49
$source: unknown
$status: draft
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:02.174728Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Drr Architecture
id: drr-YYYY-MM-DD-[topic-slug]
type: architecture
valid_until: YYYY-MM-DD
assurance: L2
r_eff: 0.XX
related_project: '[[Projects/PROJECT_NAME.md]]'
stakeholders:
- '[[Entities/STAKEHOLDER.md]]'
relationships:
  decides:
  - '[[Reasoning/Hypotheses/hypothesis-name.md]]'
  supersedes:
  - '[[Reasoning/Decisions/old-drr.md]]'
$orphan_reason: pending_enrichment
---

# Architecture Decision: [TITLE]

## Context

### Situation
[Describe the current state and why a decision is needed]

### Constraints
- **Performance:** [e.g., <100ms latency]
- **Scalability:** [e.g., 10K concurrent users]
- **Security:** [e.g., SOC2 compliance]
- **Budget:** [e.g., <$50K infrastructure]
- **Timeline:** [e.g., Q1 delivery]

### Stakeholders
- **Decision maker:** [Name]
- **Implementers:** [Team]
- **Affected parties:** [Users, other teams]

## Options Evaluated

| Option | Assurance | R_eff | Status |
|--------|-----------|-------|--------|
| [Option A] | L2 | 0.XX | **Selected** |
| [Option B] | L1 | 0.XX | Viable alternative |
| [Option C] | Invalid | - | Rejected: [reason] |

### Option A: [Name]
**Description:** [What this option entails]

**Pros:**
- [Pro 1]
- [Pro 2]

**Cons:**
- [Con 1]
- [Con 2]

**Evidence:**
- [Evidence 1] (CL3, 0.XX)
- [Evidence 2] (CL2, 0.XX)

### Option B: [Name]
[Similar structure]

### Option C: [Name] - REJECTED
**Rejection reason:** [Why this option was invalid]

## Selected Option

**Decision:** Option A - [Name]

**Rationale:**
[Explain why this option won based on evidence and WLNK analysis]

### WLNK Analysis
```
Evidence scores:
- [Evidence 1]: 0.XX
- [Evidence 2]: 0.XX
- [Evidence 3]: 0.XX

R_eff = min(0.XX, 0.XX, 0.XX) = 0.XX
```

## Evidence Chain

| Evidence | Type | CL | Weight | Expires | Source |
|----------|------|-----|--------|---------|--------|
| [Evidence 1] | validation | CL3 | 0.XX | YYYY-MM-DD | [link] |
| [Evidence 2] | research | CL2 | 0.XX | YYYY-MM-DD | [link] |
| [Evidence 3] | benchmark | CL3 | 0.XX | YYYY-MM-DD | [link] |

## Bias Audit

| Bias | Risk | Mitigation |
|------|------|------------|
| Confirmation | [Low/Med/High] | [What was done] |
| Anchoring | [Low/Med/High] | [What was done] |
| Availability | [Low/Med/High] | [What was done] |
| Authority | [Low/Med/High] | [What was done] |

## Consequences

### Positive
- [Consequence 1]
- [Consequence 2]

### Negative / Trade-offs
- [Trade-off 1]
- [Trade-off 2]

### Technical Debt
- [Any debt incurred]

## Implementation Notes

### Key Actions
1. [Action 1]
2. [Action 2]
3. [Action 3]

### Dependencies
- [Dependency 1]
- [Dependency 2]

## Conditions for Revisiting

This decision should be revisited if:
- [ ] Evidence expires (see chain above)
- [ ] [Specific condition 1]
- [ ] [Specific condition 2]
- [ ] Performance requirements change significantly

---
*Created: YYYY-MM-DD | Author: [Name] | Status: Draft*
*Generated with FPF | R_eff: 0.XX*