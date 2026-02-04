---
title: "Project/Feature Context Creation Engine"
type: prd
status: draft
author: PM-OS
created: 2026-02-02
version: 1.0
tags: [pm-os, automation, context-engine, feature-development]
---

# PRD: Project/Feature Context Creation Engine

## Executive Summary

The Context Creation Engine transforms PM-OS from a passive knowledge assistant into an active feature development partner. It automates the journey from raw signals (Slack discussions, Jira tickets, experiment results) through validated context documents, business cases, and design specs—ultimately producing spec-machine-ready inputs for engineering handoff.

**Key Value:** Reduce the PM cognitive load of synthesizing information from 10+ sources into coherent feature proposals, while maintaining rigorous validation through orthogonal challenges at each stage.

---

## 1. Problem Statement

### Current State

PMs spend 60-70% of their time on information synthesis:
- Manually scanning Slack channels for feature requests and issues
- Cross-referencing Jira tickets with experiment results
- Writing context documents from scratch
- Iterating business cases in isolation
- Duplicating effort across design specs and PRDs

### Pain Points

| Pain Point | Impact | Frequency |
|------------|--------|-----------|
| Context scattered across 10+ sources | 4-6 hours/week searching | Daily |
| No systematic validation of assumptions | Features built on weak foundations | Weekly |
| Business case disconnected from technical spec | Misaligned priorities | Per feature |
| Design decisions made without full context | Rework cycles | Per feature |
| Manual PRD creation | 8-16 hours per feature | Bi-weekly |

### Opportunity

Automate 80% of the synthesis work while improving quality through:
- Continuous signal monitoring and insight extraction
- Structured validation gates (orthogonal challenges)
- Parallel workstreams (design, business case, engineering)
- Direct integration with spec-machine for engineering handoff

---

## 2. Solution Overview

### Core Concept

A **pipeline-based engine** that:
1. **Ingests** signals from all configured sources
2. **Analyzes** and extracts actionable insights
3. **Guides** the PM through progressive context refinement
4. **Validates** at each stage via orthogonal challenges
5. **Produces** spec-machine-ready outputs

### User Mental Model

```
"I notice a pattern in Slack discussions about checkout friction.
 PM-OS, investigate this and build me a feature proposal."

PM-OS then:
- Gathers all related signals
- Presents synthesized insights for review
- Guides through context document iterations
- Runs orthogonal challenges automatically
- Produces PRD + spec-machine input
```

---

## 3. Detailed User Flow

### 3.1 Phase 1: Signal Ingestion (Automated)

**Trigger:** Continuous background process during `/boot` or `/create-context`

**Sources → PM-OS Mapping:**

| Source | Current Tool | Data Extracted |
|--------|--------------|----------------|
| GDrive reports & plans | `gdocs_processor.py` | Strategic context, OKRs, decisions |
| Slack product channels | `slack_mention_handler.py` | Feature requests, pain points, sentiment |
| Statsig experiments | `statsig_brain_sync.py` | Experiment results, metric movements |
| Confluence docs | `confluence_brain_sync.py` | Existing specs, documentation |
| Jira tickets | `jira_brain_sync.py` | Bugs, feature requests, priorities |
| GitHub issues | `github_brain_sync.py` | Technical debt, found bugs |
| Spur UAT (future) | New integration | User testing feedback |
| Chattermill (future) | New integration | Customer feedback themes |

**User Interface:** None required (background). Status visible via `/create-context status`.

**Output:** `user/brain/inbox/signals/` - Raw signal files with metadata.

---

### 3.2 Phase 2: Signal Analysis (Semi-Automated)

**Trigger:** `/analyze-signals` or automatic after ingestion

**Process:**
1. LLM analyzes all new signals
2. Clusters related signals into themes
3. Scores themes by: frequency, severity, strategic alignment
4. Generates **Insights List**

**User Interface - Insight Review:**

```
/analyze-signals

PM-OS analyzes 47 new signals from last 7 days...

┌─────────────────────────────────────────────────────────────┐
│ INSIGHTS IDENTIFIED (5)                                      │
├─────────────────────────────────────────────────────────────┤
│ 1. [HIGH] Checkout abandonment spike after OTP rollout       │
│    Sources: Slack (12), Statsig (2), Jira (3)               │
│    Confidence: 0.87                                          │
│                                                              │
│ 2. [MEDIUM] Mobile app navigation confusion                  │
│    Sources: Slack (8), GitHub (2), Jira (5)                 │
│    Confidence: 0.72                                          │
│                                                              │
│ 3. [MEDIUM] Recipe personalization requests                  │
│    Sources: Slack (15), GDocs (1)                           │
│    Confidence: 0.68                                          │
│                                                              │
│ 4. [LOW] Dark mode requests                                  │
│    Sources: Slack (6)                                        │
│    Confidence: 0.45                                          │
│                                                              │
│ 5. [LOW] Subscription pause feature gaps                     │
│    Sources: Jira (4), Confluence (1)                        │
│    Confidence: 0.52                                          │
└─────────────────────────────────────────────────────────────┘

Select insight to explore (1-5), or 'enrich' to add context:
```

**User Actions:**
- Select an insight to explore → proceeds to enrichment
- `enrich` → adds more context to all insights
- `dismiss [n]` → removes insight from consideration
- `merge [n] [m]` → combines related insights

**Output:** `user/brain/inbox/insights/insight-{date}-{slug}.yaml`

---

### 3.3 Phase 3: Insight Enrichment (Interactive)

**Trigger:** User selects insight for exploration

**Process:**
1. Pull all related Brain entities (people, teams, projects)
2. Fetch historical context (previous attempts, related features)
3. Generate **metric assumptions** for business case track
4. Present enriched insight for user refinement

**User Interface - Enrichment:**

```
/explore-insight 1

Enriching: "Checkout abandonment spike after OTP rollout"

Loading related context...
  ✓ Good Chop OTP experiment data
  ✓ Checkout funnel metrics (last 90 days)
  ✓ Related Slack threads (23)
  ✓ Team context: Beatrice (PM), Marina (leaving Feb 12)
  ✓ Previous work: OTP Phase 1 PRD

┌─────────────────────────────────────────────────────────────┐
│ ENRICHED INSIGHT                                             │
├─────────────────────────────────────────────────────────────┤
│ Problem: OTP verification causing 12% checkout drop          │
│                                                              │
│ Evidence:                                                    │
│ - Statsig: OTP variant shows -12.3% conversion (p<0.01)     │
│ - Slack: 23 complaints about "code never arrives"           │
│ - Jira: 3 P1 bugs filed for OTP timeout issues              │
│                                                              │
│ Stakeholders:                                                │
│ - Beatrice Scibilia (Good Chop PM)                          │
│ - Platform team (owns OTP infra)                            │
│                                                              │
│ Historical Context:                                          │
│ - OTP was 5% rollout, expanded to 20% on Jan 31             │
│ - Phase 2 planned for "remember device" feature             │
│                                                              │
│ Metric Assumptions (for business case):                      │
│ - Current checkout CVR: 45%                                  │
│ - OTP impact: -12.3%                                         │
│ - Potential recovery: 8-10% with fixes                       │
│ - Revenue at risk: ~$2.3M/month at 100% rollout             │
└─────────────────────────────────────────────────────────────┘

Actions:
  [C] Create context document v1
  [E] Edit enriched insight
  [A] Add more sources
  [B] Start business case track
```

**Output:**
- Enriched insight file
- Initial metric assumptions for business case

---

### 3.4 Phase 4: Context Document Creation (Guided)

**Trigger:** User selects "Create context document"

**Process:**
1. Generate Context Document v1 from enriched insight
2. **Automatic Orthogonal Challenge** runs
3. Present challenge results and refinements
4. User approves/modifies → Context Document v2
5. Second orthogonal challenge
6. Final Context Document v3

**User Interface - Context Document v1:**

```
/create-context-doc

Generating Context Document v1...

┌─────────────────────────────────────────────────────────────┐
│ CONTEXT DOCUMENT v1: OTP Checkout Recovery                   │
├─────────────────────────────────────────────────────────────┤
│ ## Problem                                                   │
│ OTP verification is causing 12% checkout abandonment due to: │
│ 1. SMS delivery delays (avg 45s, some >2min)                │
│ 2. No "remember this device" option                          │
│ 3. Confusing error states when code expires                  │
│                                                              │
│ ## Hypothesis                                                │
│ Implementing "remember device" + fallback auth will recover  │
│ 8-10% of lost conversions while maintaining fraud protection.│
│                                                              │
│ ## Success Metrics                                           │
│ - Primary: Checkout CVR returns to baseline (45%)           │
│ - Secondary: OTP completion rate >90%                        │
│ - Guardrail: Fraud rate stays <0.1%                         │
│                                                              │
│ ## Scope                                                     │
│ - In: Remember device, resend flow, better error states     │
│ - Out: Alternative auth methods, biometrics                  │
└─────────────────────────────────────────────────────────────┘

Running Orthogonal Challenge...
```

**User Interface - Orthogonal Challenge Results:**

```
┌─────────────────────────────────────────────────────────────┐
│ ORTHOGONAL CHALLENGE: Context Document v1                    │
├─────────────────────────────────────────────────────────────┤
│ Challenge Score: 72/100 (Needs Refinement)                   │
│                                                              │
│ CHALLENGES IDENTIFIED:                                       │
│                                                              │
│ 1. [CRITICAL] Assumption Gap                                 │
│    "8-10% recovery" has no supporting evidence               │
│    → Need: A/B test data or competitor benchmarks           │
│                                                              │
│ 2. [IMPORTANT] Missing Stakeholder                           │
│    Fraud/Risk team not consulted                             │
│    → Need: Fraud team sign-off on "remember device"         │
│                                                              │
│ 3. [MODERATE] Scope Creep Risk                               │
│    "Better error states" is vague                            │
│    → Need: Specific error scenarios defined                  │
│                                                              │
│ COUNTER-ARGUMENTS TO ADDRESS:                                │
│ - What if SMS delays are carrier-specific? (regional issue) │
│ - What if "remember device" increases fraud surface?        │
│ - Why not email OTP as alternative?                          │
└─────────────────────────────────────────────────────────────┘

Actions:
  [R] Refine and generate v2
  [D] Dismiss challenge (with reason)
  [I] Investigate challenge points
```

**Output:**
- `user/brain/Products/{product}/context-doc-v1.md`
- `user/brain/Reasoning/Orthogonal/context-doc-v1/challenge-results.md`

---

### 3.5 Phase 5: Parallel Workstreams

After Context Document v2 is approved, three parallel tracks begin:

#### 5a. Design Track

**Trigger:** Automatic after v2 approval (if design-required flag set)

```
/design-track start

Design Track: OTP Checkout Recovery

Step 1: Design Spec
  Generating design requirements from context doc...

  ┌───────────────────────────────────────────────────────────┐
  │ DESIGN SPEC                                                │
  ├───────────────────────────────────────────────────────────┤
  │ Screens Required:                                          │
  │ 1. OTP entry with "Remember this device" checkbox         │
  │ 2. Resend flow with countdown timer                        │
  │ 3. Error states: expired, invalid, max attempts           │
  │ 4. Device management in account settings                   │
  │                                                            │
  │ User Flows:                                                │
  │ - Happy path: Enter code → Remember → Complete            │
  │ - Resend path: Didn't receive → Resend → Enter            │
  │ - Error path: Wrong code → Retry → Success/Lockout        │
  └───────────────────────────────────────────────────────────┘

Step 2: Flow Creation
  [Auto-generate flow diagram? Y/n]

Step 3: Low-Fidelity Design
  Generate wireframe descriptions for Figma handoff...

Step 4: Figma Design
  Handoff to designer with full context...
```

**Output:**
- `user/planning/Design/{feature}/design-spec.md`
- `user/planning/Design/{feature}/flows.md`
- `user/planning/Design/{feature}/wireframes.md`

#### 5b. Business Case Track

**Trigger:** Parallel with context doc refinement

```
/business-case start

Business Case Track: OTP Checkout Recovery

Using metric assumptions from enrichment phase...

┌─────────────────────────────────────────────────────────────┐
│ BUSINESS CASE v1                                             │
├─────────────────────────────────────────────────────────────┤
│ Investment:                                                  │
│ - Engineering: 3 sprints (6 weeks)                          │
│ - Design: 1 sprint                                           │
│ - QA: Included                                               │
│ - Total: ~$180K fully loaded                                │
│                                                              │
│ Return:                                                      │
│ - CVR recovery: 8% (conservative) to 12% (optimistic)       │
│ - Monthly revenue impact: $1.8M - $2.7M                     │
│ - Payback period: <1 month                                  │
│                                                              │
│ Confidence: MEDIUM                                           │
│ - Strong on problem (p<0.01 experiment data)                │
│ - Weak on solution (no "remember device" benchmarks)        │
└─────────────────────────────────────────────────────────────┘

Refine assumptions? [Y/n]
```

**Business Case Refinement Loop:**
```
/business-case refine

What would you like to refine?
1. Investment estimates (get engineering input)
2. Return assumptions (run sensitivity analysis)
3. Confidence scoring (add more evidence)
4. Risk factors (identify failure modes)

> 2

Running sensitivity analysis...

┌─────────────────────────────────────────────────────────────┐
│ SENSITIVITY ANALYSIS                                         │
├─────────────────────────────────────────────────────────────┤
│ Scenario      │ CVR Recovery │ Monthly Impact │ Payback     │
│───────────────┼──────────────┼────────────────┼─────────────│
│ Pessimistic   │ 4%           │ $920K          │ 2 months    │
│ Conservative  │ 8%           │ $1.8M          │ <1 month    │
│ Expected      │ 10%          │ $2.3M          │ <1 month    │
│ Optimistic    │ 14%          │ $3.2M          │ <1 month    │
└─────────────────────────────────────────────────────────────┘

Even pessimistic scenario shows positive ROI.
Business Case v2 updated.
```

**Output:**
- `user/planning/BusinessCases/{feature}/bc-v1.md`
- `user/planning/BusinessCases/{feature}/bc-v2.md`

#### 5c. Engineering Track

**Trigger:** After Context Document v3 approved

```
/engineering-spec start

Engineering Specification: OTP Checkout Recovery

Analyzing technical requirements...

┌─────────────────────────────────────────────────────────────┐
│ ENGINEERING SPEC v0                                          │
├─────────────────────────────────────────────────────────────┤
│ Components Affected:                                         │
│ - checkout-service (OTP verification)                       │
│ - device-fingerprint-service (new)                          │
│ - user-preferences-api (remember device storage)            │
│ - mobile-app (UI changes)                                    │
│ - web-app (UI changes)                                       │
│                                                              │
│ Technical Decisions Required:                                │
│ 1. Device fingerprinting approach (native vs library)       │
│ 2. Token storage (secure enclave vs encrypted storage)      │
│ 3. Expiration policy (30 days vs never vs configurable)     │
│                                                              │
│ Dependencies:                                                │
│ - Platform team for device-fingerprint-service              │
│ - Security review for token storage                          │
│ - Mobile release cycle alignment                             │
└─────────────────────────────────────────────────────────────┘

Generate ADRs for technical decisions? [Y/n]
```

**ADR Generation:**
```
Generating ADR: Device Fingerprinting Approach

┌─────────────────────────────────────────────────────────────┐
│ ADR-001: Device Fingerprinting Approach                      │
├─────────────────────────────────────────────────────────────┤
│ Status: Proposed                                             │
│                                                              │
│ Context:                                                     │
│ Need to identify returning devices for "remember me" feature │
│                                                              │
│ Options:                                                     │
│ 1. Native implementation (custom)                            │
│    + Full control, no dependencies                           │
│    - 4-6 weeks development, maintenance burden              │
│                                                              │
│ 2. FingerprintJS library                                     │
│    + Battle-tested, 1 week integration                       │
│    - License cost, third-party dependency                   │
│                                                              │
│ 3. Platform-provided solution                                │
│    + Shared infrastructure, no per-team maintenance         │
│    - May not exist yet, timeline dependency                 │
│                                                              │
│ Recommendation: Option 2 (FingerprintJS)                     │
│ Rationale: Fastest to market, proven accuracy               │
└─────────────────────────────────────────────────────────────┘
```

**Code Analysis (if codebase connected):**
```
/code-analysis

Analyzing codebase for OTP-related code...

Found 12 relevant files:
- checkout-service/src/otp/verifier.ts (main logic)
- checkout-service/src/otp/sender.ts (SMS dispatch)
- mobile-app/src/screens/OTPScreen.tsx (UI)
...

Complexity Assessment:
- OTP verifier: Medium complexity, well-tested
- Adding device check: Low complexity, clear injection point
- UI changes: Medium complexity, needs design handoff
```

**Output:**
- `user/planning/Engineering/{feature}/spec-v0.md`
- `user/planning/Engineering/{feature}/ADR-001-*.md`
- `user/planning/Engineering/{feature}/code-analysis.md`

---

### 3.6 Phase 6: Decision Gate

**Trigger:** All three tracks complete

```
/decision-gate

┌─────────────────────────────────────────────────────────────┐
│ DECISION GATE: OTP Checkout Recovery                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ CONTEXT DOCUMENT v3                          ✓ Complete     │
│   Orthogonal challenges: 2 passed                           │
│   Confidence: HIGH                                           │
│                                                              │
│ DESIGN TRACK                                  ✓ Complete     │
│   Design spec: Approved                                      │
│   Figma: In progress (ETA: Feb 5)                           │
│                                                              │
│ BUSINESS CASE v2                              ✓ Complete     │
│   ROI: Positive in all scenarios                            │
│   Confidence: MEDIUM-HIGH                                    │
│                                                              │
│ ENGINEERING SPEC v0                           ✓ Complete     │
│   ADRs: 3 proposed, 0 decided                               │
│   Dependencies: 1 (Platform team)                           │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│ RECOMMENDATION: PROCEED TO BUILD                             │
│                                                              │
│ Blockers to resolve:                                         │
│ - [ ] ADR decisions needed (schedule tech review)           │
│ - [ ] Platform team capacity confirmation                    │
│ - [ ] Figma completion                                       │
└─────────────────────────────────────────────────────────────┘

Actions:
  [P] Proceed - Generate PRD and spec-machine input
  [H] Hold - Save state, revisit later
  [R] Reject - Archive with reason
```

---

### 3.7 Phase 7: Output Generation

**Trigger:** User selects "Proceed" at decision gate

```
/generate-outputs

Generating final outputs...

1. PM-OS PRD
   Using /prd with full context...
   ✓ Generated: Products/Good_Chop/PRD_OTP_Recovery.md

2. Spec Machine Input
   Using /export-to-spec...
   ✓ Generated: spec-machine/specs/2026-02-02-otp-recovery/

3. Spur UAT Test Plan (future)
   ✓ Generated: QA/otp-recovery-uat-plan.md

All outputs ready!

PRD: /Users/.../PRD_OTP_Recovery.md
Spec: /Users/.../spec-machine/specs/2026-02-02-otp-recovery/

Next: Run spec-machine to generate implementation plan
```

---

## 4. Technical Architecture

### 4.1 New Commands

| Command | Purpose | Phase |
|---------|---------|-------|
| `/analyze-signals` | Analyze ingested signals, generate insights | 2 |
| `/explore-insight [n]` | Enrich selected insight | 3 |
| `/create-context-doc` | Generate context document with challenges | 4 |
| `/design-track` | Manage design workstream | 5a |
| `/business-case` | Manage business case workstream | 5b |
| `/engineering-spec` | Manage engineering workstream | 5c |
| `/decision-gate` | Review all tracks, make build decision | 6 |
| `/generate-outputs` | Create PRD + spec-machine input | 7 |

### 4.2 New Tools

```
common/tools/
├── context_engine/
│   ├── __init__.py
│   ├── signal_analyzer.py      # LLM-powered signal analysis
│   ├── insight_generator.py    # Clustering and scoring
│   ├── context_doc_builder.py  # Document generation
│   ├── orthogonal_runner.py    # Automatic challenges
│   └── decision_gate.py        # Track aggregation
├── design_track/
│   ├── design_spec_generator.py
│   ├── flow_generator.py
│   └── wireframe_generator.py
├── business_case/
│   ├── bc_generator.py
│   ├── metric_analyzer.py
│   └── sensitivity_runner.py
└── engineering_track/
    ├── eng_spec_generator.py
    ├── adr_generator.py
    └── code_analyzer.py
```

### 4.3 Data Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    PM-OS Brain                               │
├─────────────────────────────────────────────────────────────┤
│ inbox/signals/          ← Raw signals from integrations     │
│ inbox/insights/         ← Analyzed insights                 │
│ Products/{product}/                                          │
│   ├── context-doc-v1.md                                     │
│   ├── context-doc-v2.md                                     │
│   ├── context-doc-v3.md                                     │
│   └── PRD_*.md          → Final PRD                         │
│ Reasoning/Orthogonal/   ← Challenge results                 │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    PM-OS Planning                            │
├─────────────────────────────────────────────────────────────┤
│ Design/{feature}/       ← Design track outputs              │
│ BusinessCases/{feature}/ ← Business case versions           │
│ Engineering/{feature}/  ← Specs, ADRs, analysis             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    Spec Machine                              │
├─────────────────────────────────────────────────────────────┤
│ specs/{date}-{feature}/ → Engineering handoff               │
└─────────────────────────────────────────────────────────────┘
```

### 4.4 State Management

Each feature in progress maintains state in:
```yaml
# user/planning/active/{feature-slug}/state.yaml
feature_id: otp-checkout-recovery
created: 2026-02-02T10:30:00Z
current_phase: decision_gate
tracks:
  context:
    version: 3
    status: complete
    challenges_passed: 2
  design:
    status: in_progress
    completion: 75%
  business_case:
    version: 2
    status: complete
  engineering:
    version: 0
    status: complete
    adrs_pending: 3
decision: pending
```

---

## 5. Implementation Phases

### Phase 1: Foundation (2-3 weeks)
- [ ] Signal analyzer tool (LLM-based)
- [ ] Insight generator with clustering
- [ ] Basic `/analyze-signals` command
- [ ] State management infrastructure

### Phase 2: Context Pipeline (2-3 weeks)
- [ ] Context document builder
- [ ] Integration with existing orthogonal challenge
- [ ] `/create-context-doc` command
- [ ] Automatic challenge triggering

### Phase 3: Parallel Tracks (3-4 weeks)
- [ ] Design track tools and command
- [ ] Business case generator and refinement
- [ ] Engineering spec generator
- [ ] ADR auto-generation

### Phase 4: Decision & Output (2 weeks)
- [ ] Decision gate aggregator
- [ ] Integration with existing `/prd` and `/export-to-spec`
- [ ] Full pipeline testing

### Phase 5: Future Integrations (Ongoing)
- [ ] Spur UAT integration
- [ ] Chattermill integration
- [ ] Competitor analysis integration
- [ ] Flow benchmarking integration

---

## 6. Success Metrics

| Metric | Current | Target | Measurement |
|--------|---------|--------|-------------|
| Time to PRD | 8-16 hours | 2-4 hours | Tracked in state |
| Context doc iterations | 5-10 | 2-3 | Version count |
| Assumption validation | Ad-hoc | 100% challenged | Challenge logs |
| Signal-to-insight time | Days | Hours | Timestamp diff |
| Spec-machine adoption | 20% | 80% | Output tracking |

---

## 7. Risks and Mitigations

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| LLM hallucination in analysis | Medium | Medium | Human review gates, confidence scoring |
| Over-automation reduces PM judgment | High | Low | Design for guidance, not replacement |
| Integration complexity | Medium | Medium | Phased rollout, existing tool reuse |
| User adoption resistance | Medium | Low | Gradual feature introduction |

---

## 8. Open Questions

1. **Insight threshold:** What confidence score should trigger user notification?
2. **Challenge strictness:** Should orthogonal challenges block progress or just warn?
3. **Design handoff:** How to integrate with actual Figma (API or manual)?
4. **Multi-feature:** How to handle multiple features in parallel?
5. **Team collaboration:** Should other PMs see/contribute to context docs?

---

## 9. Appendix: Command Reference

### Full Command Flow

```bash
# Daily signal monitoring (automatic with /boot)
/boot

# Weekly insight review
/analyze-signals
/analyze-signals --since "7 days"

# Feature exploration
/explore-insight 1
/explore-insight --topic "checkout friction"

# Context document creation
/create-context-doc
/create-context-doc --from-insight insight-2026-02-02-otp.yaml

# Parallel tracks
/design-track start
/design-track status
/business-case start
/business-case refine
/engineering-spec start

# Decision and output
/decision-gate
/decision-gate --feature otp-recovery
/generate-outputs
```

---

*Generated: 2026-02-02*
*Status: Draft - Ready for Review*
