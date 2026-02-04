# Context Creation Engine - Confluence Documentation

**Version**: 1.0
**Last Updated**: 2026-02-04
**Status**: Production Ready
**Audience**: PMs, Engineers, Stakeholders

---

## Executive Summary

The Context Creation Engine is a PM-OS feature that automates the journey from initial feature signals through to approved PRDs. It provides a structured, repeatable workflow that ensures features are thoroughly validated before development begins.

**Key Benefits:**
- Reduces time from insight to PRD by 60%
- Ensures consistent quality through automated validation gates
- Tracks decisions, approvals, and artifacts in one place
- Integrates with existing tools (Master Sheet, Jira, Figma)

---

## How It Works

### High-Level Flow

```
Signal Detection -> Context Creation -> Parallel Tracks -> Decision Gate -> PRD Output
```

The engine guides PMs through six phases, each with clear inputs, outputs, and quality gates.

### Workflow Diagram

```
+-------------------+     +-------------------+     +-------------------+
|  1. INITIALIZE    | --> |  2. CONTEXT DOC   | --> |  3. PARALLEL      |
|  /start-feature   |     |  v1 -> v2 -> v3   |     |     TRACKS        |
+-------------------+     +-------------------+     +-------------------+
                                                           |
                                                    +------+------+
                                                    |      |      |
                                                    v      v      v
                                              +-------+ +----+ +-----+
                                              |Design | | BC | | Eng |
                                              +-------+ +----+ +-----+
                                                    |      |      |
                                                    +------+------+
                                                           |
                                                           v
+-------------------+     +-------------------+     +-------------------+
|  6. PRD OUTPUT    | <-- |  5. DECISION GATE | <-- |  4. VALIDATION    |
|  /generate-outputs|     |  /decision-gate   |     |  /validate-feature|
+-------------------+     +-------------------+     +-------------------+
```

---

## Phase-by-Phase Breakdown

### Phase 1: Initialization

**Command**: `/start-feature "Feature Name" --product product-name`

**What Happens:**
1. Engine checks for duplicate/similar features (alias detection)
2. Creates feature folder at `user/products/{org}/{product}/{feature-slug}/`
3. Creates feature-state.yaml for tracking
4. Creates Brain entity for knowledge graph
5. Optionally adds row to Master Sheet

**Outputs:**
- Feature folder with initial structure
- Brain entity `Entities/{Feature_Name}.md`
- Master Sheet entry (if enabled)

**Who's Involved:** PM (initiator)

---

### Phase 2: Context Document

The context document goes through 3 iterations with automated "orthogonal challenge" validation.

| Version | Purpose | Quality Gate |
|---------|---------|--------------|
| v1 | Initial draft | Problem statement, scope defined |
| v2 | Challenge response | Score >= 60, critical issues addressed |
| v3 | Final | Score >= 75, ready for tracks |

**Challenge System:**
The orthogonal challenge runs an AI-powered devil's advocate review that scores the context document and identifies gaps, risks, and assumptions that need addressing.

**Who's Involved:** PM (author), potentially stakeholders for review

---

### Phase 3: Parallel Tracks

Three tracks run in parallel after context doc is finalized:

#### Design Track
- Design spec auto-generated from context
- Wireframes required (URL attachment)
- Figma designs required (URL attachment)
- Designer sign-off needed

#### Business Case Track
- Baseline metrics (from Statsig or manual)
- Assumptions documented
- ROI analysis
- **Stakeholder approval required** (blocking)

#### Engineering Track
- Technical spec generation
- ADRs (Architecture Decision Records) created
- Complexity estimate
- Dependencies identified
- All ADRs must be decided (accepted/rejected)

**Who's Involved:** PM, Designer, Engineering Lead, Business Stakeholders

---

### Phase 4: Validation

**Command**: `/validate-feature`

Runs quality gate checks across all tracks:

| Track | Check | Blocking? |
|-------|-------|-----------|
| Context | Document complete | Yes |
| Design | Figma attached | Yes |
| Design | Wireframes attached | No |
| BC | Stakeholder approval | Yes |
| Engineering | ADRs decided | Yes |
| Engineering | Estimate provided | Yes |

**Output:** Validation report showing PASS/INCOMPLETE/FAIL for each gate

---

### Phase 5: Decision Gate

**Command**: `/decision-gate`

Final checkpoint before PRD generation:

**Requirements for GO:**
- Context document v3 complete
- Business case approved by stakeholders
- Figma design attached
- Engineering estimate provided
- All ADRs decided
- No blocking dependencies
- High-impact risks have mitigation plans

**Outcomes:**
- **GO**: Proceed to PRD generation
- **NO-GO**: List of blockers to resolve
- **DEFER**: Pause with documented reason

**Who's Involved:** PM (facilitator), key stakeholders for final approval

---

### Phase 6: Output Generation

**Command**: `/generate-outputs`

**What Gets Created:**
1. **PRD** at `user/brain/Products/{Product}/PRD_{Feature}.md`
   - Executive Summary
   - Problem Statement
   - Business Case Summary
   - Engineering Approach
   - Stakeholder Approvals
   - All artifact links

2. **Feature Summary** at `{feature-folder}/feature-summary.md`

**Optional Integrations:**
- Export to spec machine: `/export-to-spec`
- Create Jira epic: Prompted at end

---

## Integration Points

### Master Sheet (Google Sheets)

| Direction | Data Flow |
|-----------|-----------|
| Sheet -> Engine | Feature list, product mapping, existing status |
| Engine -> Sheet | New features, status updates, completion |

**Sync triggers:**
- Feature initialization
- Phase completion
- Status changes
- Decision gate outcome

### Brain (Knowledge Graph)

- Creates feature entities with bidirectional links
- Links to related features, people, products
- Searchable in `/deep-search`

### Jira

- Optional epic creation after decision gate
- Links stored in feature-state.yaml
- Updates context file References section

### Figma

- URL validation on attachment
- Metadata fetch (file name)
- Stored in feature-state.yaml and context file

---

## Team Responsibilities

### Product Manager

| Phase | Responsibility |
|-------|----------------|
| Initialize | Start feature, select product |
| Context Doc | Author v1, address challenges, finalize v3 |
| Business Case | Provide assumptions, request approvals |
| Validation | Review blockers, ensure completion |
| Decision Gate | Facilitate GO/NO-GO decision |
| Output | Review PRD, initiate Jira epic |

### Designer

| Phase | Responsibility |
|-------|----------------|
| Parallel Tracks | Provide wireframes URL |
| Parallel Tracks | Provide Figma URL |
| Design Track | Sign off on design spec |

### Engineering Lead

| Phase | Responsibility |
|-------|----------------|
| Engineering Track | Review technical spec |
| Engineering Track | Decide ADRs |
| Engineering Track | Provide complexity estimate |
| Engineering Track | Identify dependencies |

### Business Stakeholder

| Phase | Responsibility |
|-------|----------------|
| Business Case | Review ROI analysis |
| Business Case | Approve business case (blocking) |
| Decision Gate | Participate in GO/NO-GO |

---

## Command Reference

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/start-feature` | Initialize new feature | Starting a new feature |
| `/attach-artifact` | Link Figma, Jira, etc. | When external artifact ready |
| `/check-feature` | View status & blockers | Anytime for progress check |
| `/resume-feature` | Resume paused feature | Returning to stale feature |
| `/validate-feature` | Run quality gates | Before decision gate |
| `/decision-gate` | Final GO/NO-GO | All tracks complete |
| `/generate-outputs` | Create PRD | After decision gate approval |

For detailed command documentation including all arguments and examples, see:
**[[Context_Engine_Commands]]**

---

## Quality Gates Summary

### Context Document Gates

| Gate | Threshold | Blocking |
|------|-----------|----------|
| Problem statement present | Required | Yes |
| Success metrics defined | Required | Yes |
| Orthogonal challenge v2 | Score >= 60 | Yes |
| Orthogonal challenge v3 | Score >= 75 | Yes |

### Business Case Gates

| Gate | Threshold | Blocking |
|------|-----------|----------|
| Baseline metrics | Required | Yes |
| Assumptions documented | Required | Yes |
| Stakeholder approval | Required | Yes |
| ROI positive (conservative) | Advisory | No |

### Engineering Gates

| Gate | Threshold | Blocking |
|------|-----------|----------|
| ADRs decided | All | Yes |
| Estimate provided | Required | Yes |
| High-impact risks mitigated | Required | Yes |

---

## Example Timeline

A typical feature journey through the Context Creation Engine:

| Day | Activity | Phase |
|-----|----------|-------|
| Day 1 AM | `/start-feature`, signal analysis | Init |
| Day 1 PM | Context doc v1 -> challenge -> v2 -> v3 | Context |
| Day 1 PM | Start business case, request approval | Parallel |
| Day 1 PM | Share design spec with designer | Parallel |
| Day 2 AM | Receive BC approval, attach wireframes | Parallel |
| Day 2 PM | Attach Figma, decide ADRs | Parallel |
| Day 2 PM | `/validate-feature` | Validation |
| Day 2 PM | `/decision-gate` GO | Decision |
| Day 2 PM | `/generate-outputs` | Output |

**Total time: ~2 days** (vs. 5+ days manual process)

---

## Troubleshooting

### "Feature not found"
- Check feature slug spelling
- Navigate to feature directory
- Use `/check-feature` to list active features

### "Decision gate not passed"
- Run `/validate-feature` to see all blockers
- Address each blocking item
- Re-run `/decision-gate`

### "Business case not approved"
- Check pending approvers with `/check-feature --verbose`
- Follow up with stakeholders
- Record approval when received

### "Stale feature" warning
- Feature inactive >3 days triggers reminder
- Use `/resume-feature --sync` to see what changed
- Update context if source data is stale

---

## Related Documentation

- **Command Details**: [[Context_Engine_Commands]]
- **Full PRD**: [[PRD_Context_Creation_Engine_v2]]
- **PM-OS User Guide**: [[README]]

---

## Getting Help

- Slack: #pm-os-support
- Documentation: PM-OS brain/Products/PM-OS/
- Issues: Submit via `/feedback`

---

*Document generated by Context Creation Engine - Iteration 40*
