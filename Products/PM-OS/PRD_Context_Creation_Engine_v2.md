---
title: "Project/Feature Context Creation Engine"
type: prd
status: draft
author: PM-OS
created: 2026-02-02
version: 2.1
tags: [pm-os, automation, context-engine, feature-development]
changelog:
  - v2.1: Revised folder structure to align with actual PM-OS v3.3 structure (products/{org}/{product}/{feature}/)
  - v2.0: Added user input gates, external artifact handling, validation framework
---

# PRD: Project/Feature Context Creation Engine (v2)

## Addendum: Implementation Reality Check

Before the main PRD content, this section addresses critical questions about how this system works in practice.

---

## A. User Input Gates

### A.1 Where Human Decisions Are Required

| Phase | Input Type | Why Human Required | Blocking? |
|-------|-----------|-------------------|-----------|
| **Insight Selection** | Choice | PM decides which insight is worth pursuing | Yes |
| **Enrichment Review** | Approval | Validate that context is accurate/complete | Yes |
| **Context Doc v1→v2** | Decision | Accept/reject orthogonal challenge findings | Yes |
| **Business Case Assumptions** | Input | Provide/validate metric assumptions | Yes |
| **Business Case Approval** | Approval | Stakeholder sign-off (may be external) | Yes |
| **Design Spec Review** | Approval | Validate requirements before design starts | Yes |
| **Wireframe/Figma Link** | Input | Provide external artifact URL | Yes |
| **Engineering Complexity** | Input | Validate effort estimates with eng lead | No (advisory) |
| **ADR Decisions** | Decision | Choose between technical options | Yes |
| **Decision Gate** | Approval | Final go/no-go | Yes |

### A.2 Input Gate Interface Design

Each input gate follows a consistent pattern:

```
┌─────────────────────────────────────────────────────────────┐
│ INPUT REQUIRED: [Gate Name]                                  │
│ Feature: OTP Checkout Recovery                               │
│ Phase: Business Case Approval                                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ [Content requiring review/input]                             │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│ Required Action:                                             │
│   ○ Approve - proceed to next phase                         │
│   ○ Request Changes - specify what needs updating           │
│   ○ Reject - archive feature with reason                    │
│   ○ Defer - pause, set reminder date                        │
│                                                              │
│ Optional:                                                    │
│   □ Add stakeholder approval (name, date)                   │
│   □ Attach external artifact (URL)                          │
│   □ Add notes for next phase                                │
└─────────────────────────────────────────────────────────────┘
```

### A.3 State Transitions

```
                    ┌──────────┐
                    │  DRAFT   │
                    └────┬─────┘
                         │ User initiates
                         ▼
                    ┌──────────┐
              ┌─────│ PENDING  │─────┐
              │     │  INPUT   │     │
              │     └────┬─────┘     │
         Defer│          │Approve    │Reject
              │          ▼           │
              │     ┌──────────┐     │
              │     │PROCESSING│     │
              │     └────┬─────┘     │
              │          │           │
              ▼          ▼           ▼
        ┌──────────┐┌──────────┐┌──────────┐
        │ DEFERRED ││  NEXT    ││ ARCHIVED │
        │          ││  PHASE   ││          │
        └──────────┘└──────────┘└──────────┘
```

---

## B. External Artifact Handling

### B.1 Types of External Artifacts

| Artifact | Source | When Needed | How Captured |
|----------|--------|-------------|--------------|
| **Figma Design** | Designer | After wireframe approval | URL input |
| **Wireframes** | Designer/PM | During design track | URL or file upload |
| **Stakeholder Approval** | Email/Slack/Meeting | BC approval, Decision gate | Manual record or Slack link |
| **Engineering Estimate** | Eng Lead | Engineering spec phase | Manual input or Jira link |
| **Experiment Data** | Statsig | Enrichment, BC | Auto-fetched if configured |
| **Meeting Notes** | GDocs | Various | Auto-linked from calendar |
| **Jira Epic** | Jira | After decision gate | Auto-created or manual link |

### B.2 Artifact Attachment Interface

```
/attach-artifact

Feature: OTP Checkout Recovery
Phase: Design Track

What type of artifact?
  1. Figma design URL
  2. Wireframe URL/file
  3. Stakeholder approval
  4. Engineering estimate
  5. Other document

> 1

Enter Figma URL: https://figma.com/file/abc123...

Validating URL... ✓ Valid Figma file
Fetching metadata... ✓ "OTP Recovery - Mobile Screens"

Artifact attached to Design Track.
Design phase status: Figma Complete ✓
```

### B.3 Artifact Validation Rules

| Artifact | Validation | On Failure |
|----------|------------|------------|
| Figma URL | Check URL pattern, fetch title | Warn, allow override |
| Jira link | Verify ticket exists via API | Block until valid |
| Stakeholder approval | Check name in Brain | Warn if unknown person |
| GDocs link | Verify accessible | Warn, allow override |

---

## C. Project/Feature Folder Structure

> **IMPORTANT:** This section has been revised to align with actual PM-OS folder structure as of v3.3

### C.1 Existing PM-OS Structure

PM-OS already has a well-defined folder hierarchy:

```
user/
├── config.yaml                    # Central configuration (products, team, integrations)
├── products/
│   └── {organization}/            # e.g., new-ventures/
│       ├── {product}/             # e.g., good-chop/
│       │   ├── {product}-context.md       # Product-level context
│       │   ├── discovery/         # Standard subfolder
│       │   ├── planning/          # Standard subfolder
│       │   ├── execution/         # Standard subfolder
│       │   ├── reporting/         # Standard subfolder
│       │   ├── presentations/     # Standard subfolder
│       │   ├── discussions/       # Standard subfolder
│       │   └── {feature-slug}/    # Feature folders
│       │       └── {feature-slug}-context.md
│       └── {organization}-context.md
├── personal/
│   └── context/                   # Daily context files (YYYY-MM-DD-context.md)
├── brain/
│   ├── Entities/                  # Brain entities (people, teams, features)
│   └── Products/                  # Product-level docs (PRDs, etc.)
└── team/                          # Team member folders
```

### C.2 Integration with Existing Structure

The Context Creation Engine integrates with (not replaces) the existing structure:

**Feature Location:**
```
user/products/{org}/{product}/{feature-slug}/
├── {feature-slug}-context.md     # EXISTING: Auto-generated from Master Sheet
├── feature-state.yaml            # NEW: Engine state tracking
├── context-docs/                  # NEW: Context doc versions
│   ├── v1-draft.md
│   ├── v1-challenge.md
│   ├── v2-revised.md
│   └── v3-final.md
├── business-case/                 # NEW: BC artifacts
│   ├── bc-v1.md
│   └── bc-v2-approved.md
├── engineering/                   # NEW: Engineering artifacts
│   ├── spec.md
│   └── adrs/
└── artifacts.yaml                 # NEW: External artifact links
```

**Brain Integration:**
```
user/brain/Products/{Product-Name}/
├── PRD_{Feature_Name}.md         # Final PRD output
└── ...other product docs
```

### C.3 Initialization Flow

```
/start-feature "OTP Checkout Recovery" --product "Good Chop"

Checking existing structure...
✓ Product found: user/products/new-ventures/good-chop/
✓ Config entry: products.items[good-chop]

Creating feature workspace...

┌─────────────────────────────────────────────────────────────┐
│ NEW FEATURE INITIALIZED                                      │
├─────────────────────────────────────────────────────────────┤
│ Feature Slug: goc-otp-recovery                              │
│ Product: Good Chop (good-chop)                              │
│ Organization: New Ventures                                   │
│                                                              │
│ Location:                                                    │
│ user/products/new-ventures/good-chop/goc-otp-recovery/      │
│                                                              │
│ Created:                                                     │
│ ├── goc-otp-recovery-context.md  (from template)            │
│ ├── feature-state.yaml           (engine state)             │
│ └── context-docs/                (for context iterations)   │
│                                                              │
│ Master Sheet:                                                │
│ → Added entry to "topics" tab                               │
│                                                              │
│ Brain:                                                       │
│ → Entity created: Entities/Goc_Otp_Recovery                 │
└─────────────────────────────────────────────────────────────┘

Next: Run /analyze-signals to gather related insights
```

### C.4 Feature State File

The `feature-state.yaml` tracks engine-specific state without modifying the existing context file format:

```yaml
# user/products/new-ventures/good-chop/goc-otp-recovery/feature-state.yaml
slug: goc-otp-recovery
title: "OTP Checkout Recovery"
product_id: good-chop
organization: new-ventures

# Links to existing PM-OS structure
context_file: goc-otp-recovery-context.md
brain_entity: "[[Entities/Goc_Otp_Recovery]]"
master_sheet_row: 15  # Row in "topics" tab

created: 2026-02-02T10:30:00Z
created_by: nikita.gorshkov

# Engine state (separate from context.md status)
engine:
  current_phase: design_track
  phase_history:
    - phase: initialization
      entered: 2026-02-02T10:30:00Z
      completed: 2026-02-02T10:30:15Z
    - phase: signal_analysis
      entered: 2026-02-02T10:30:15Z
      completed: 2026-02-02T11:45:00Z
      insights_reviewed: 5
      insight_selected: insight-otp-abandonment
    - phase: context_doc
      entered: 2026-02-02T11:45:00Z
      completed: 2026-02-02T14:30:00Z
      versions: 3
      challenges_passed: 2
    - phase: design_track
      entered: 2026-02-02T14:30:00Z
      status: in_progress

  tracks:
    context:
      status: complete
      current_version: 3
      file: context-docs/v3-final.md
    design:
      status: in_progress
      current_step: wireframes
      artifacts:
        design_spec: context-docs/design-spec.md
        wireframes: null
        figma: null
    business_case:
      status: complete
      current_version: 2
      file: business-case/bc-v2-approved.md
      approvals:
        - name: Laurent Ades
          date: 2026-02-02
          type: verbal
          reference: "Slack thread #good-chop-planning"
    engineering:
      status: not_started

# External artifacts (URLs, references)
artifacts:
  jira_epic: null
  figma: null
  confluence_page: null
  wireframes_url: null

# Decisions made during engine flow
decisions:
  - date: 2026-02-02T12:00:00Z
    phase: context_doc
    decision: Proceed with "remember device" approach
    rationale: Best balance of UX and security
    decided_by: nikita.gorshkov
```

### C.5 Syncing with Context File

The engine keeps `{feature-slug}-context.md` in sync with `feature-state.yaml`:

```yaml
# Context file updates triggered by engine state changes:
sync_rules:
  status:
    source: engine.tracks  # Derive from track completion
    mapping:
      all_complete: "Done"
      any_in_progress: "In Progress"
      all_pending: "To Do"

  action_log:
    source: engine.phase_history
    append: true  # Add new entries, don't overwrite

  references:
    source: artifacts
    filter: non_null  # Only add when artifact provided

  changelog:
    source: engine.phase_history
    format: "**{date}**: {phase} completed"
```

### C.6 Product Identification

**How we identify the product:**

1. **From config.yaml:** Products defined in `products.items[]`
2. **From Master Sheet:** Product mapping in `master_sheet.product_mapping`
3. **From context:** Recent daily context files mention products

```
Priority Order:
1. Explicit flag: /start-feature "Title" --product "Good Chop"
2. Master Sheet lookup: If topic already exists, use its product
3. Current daily context: What product appeared in today's context?
4. Signal source: If insight from #good-chop channel → Good Chop
5. Ask user: Present list from config.yaml products.items[]
```

**User Interface when ambiguous:**

```
/start-feature "Improve checkout conversion"

Product not specified. Which product is this for?

From config.yaml:
  1. Good Chop (GOC) - recent activity: 2 hours ago
  2. The Pets Table (TPT)
  3. Factor Form (RTEVMS)
  4. Market Innovation (MIO)

> 1

Product set to: Good Chop
Feature will be created at: user/products/new-ventures/good-chop/
```

### C.7 Master Sheet Integration

The Master Sheet (Google Sheets) is the source of truth for feature/topic tracking in PM-OS. The Context Creation Engine integrates bidirectionally:

**Master Sheet Configuration (from config.yaml):**
```yaml
master_sheet:
  enabled: true
  spreadsheet_id: "15roio2__Ow9nDsOOjeeWE4-Y1TEmJnRD-TkoLSe897s"
  tabs:
    instructions: "how-to"
    topics: "topics"        # Feature/topic tracking
    recurring: "recurring"  # Recurring items
  product_mapping:
    "FF": "factor-form"
    "GOC": "good-chop"
    "TPT": "the-pets-table"
    "MIO": "market-innovation"
```

**When a feature is created:**
1. Engine scans "Feature" column in "topics" tab for potential matches
2. If potential match found (fuzzy matching):
   - **High confidence match:** Auto-consolidate as alias, notify user
   - **Uncertain match:** Bubble up question to user: "Is this the same as [existing feature]?"
3. If no match or user confirms new: Add row to "topics" tab
4. Engine creates feature folder and context file
5. Context file is auto-generated with data from Master Sheet row

**Alias Detection Logic:**
```python
def find_existing_feature(new_title: str, product: str) -> MatchResult:
    """Check if feature already exists with different name."""

    existing = get_topics_for_product(product)

    for row in existing:
        similarity = fuzzy_match(new_title, row.feature_name)

        if similarity > 0.9:  # Very high match
            return MatchResult(
                type="auto_consolidate",
                existing=row,
                message=f"Auto-linked to existing: {row.feature_name}"
            )
        elif similarity > 0.7:  # Possible match
            return MatchResult(
                type="ask_user",
                existing=row,
                question=f"Is '{new_title}' the same as '{row.feature_name}'?"
            )

    return MatchResult(type="new_feature")
```

**User Prompt for Uncertain Matches:**
```
/start-feature "OTP Checkout Recovery" --product "Good Chop"

⚠ Potential duplicate detected:

Existing feature in Master Sheet:
  "GOC OTP Flow Improvements" (Row 12, Status: To Do, Owner: Beatrice)

Is "OTP Checkout Recovery" the same feature?
  1. Yes, link to existing (consolidate names)
  2. No, create as new feature
  3. Show me more details about the existing feature

> 1

Linked to existing feature. Updated aliases:
  - Primary: "GOC OTP Flow Improvements"
  - Alias: "OTP Checkout Recovery"
```

**Alias Storage (in feature-state.yaml):**
```yaml
# Aliases are stored for future matching
aliases:
  primary_name: "GOC OTP Flow Improvements"  # From Master Sheet
  known_aliases:
    - "OTP Checkout Recovery"
    - "OTP Recovery"
    - "checkout otp fix"  # From Slack mention
  auto_detected: true  # Whether aliases were auto-consolidated
```

**Alias sources:**
- Manual consolidation (user confirmed)
- Slack mentions with similar keywords
- Jira ticket titles referencing same epic
- Brain entity aliases (from `entity_aliases.json`)

**When feature state changes:**
1. Engine updates Master Sheet row (Status, Priority, etc.)
2. Engine syncs changes to `{feature}-context.md`
3. Action Log in context file is updated with new entries

**Bidirectional sync flow:**
```
Master Sheet ←→ Context File ←→ Engine State
     ↑               ↑               ↑
     └───────────────┴───────────────┘
            All stay in sync
```

**Example: Context file auto-generated from Master Sheet**
```markdown
# GOC OTP Recovery Context

**Product:** GOC
**Status:** In Progress
**Owner:** Nikita Gorshkov
**Priority:** P0
**Deadline:** 2026-02-15
**Last Updated:** 2026-02-02

## Description
*Feature context auto-generated from Master Sheet*

## Action Log
| Date | Action | Status | Priority | Deadline |
|------|--------|--------|----------|----------|
| 2026-02-02 | Context doc v3 complete | Done | P0 | 2026-02-02 |
| 2026-02-02 | Business case approved | Done | P0 | 2026-02-02 |
| 2026-02-02 | Awaiting Figma designs | In Progress | P0 | 2026-02-05 |

## References
- Wireframes: https://figma.com/file/wireframes...
- *Figma: Pending*

## Brain Entities
- [[Entities/Goc_Otp_Recovery]]

## Changelog
- **2026-02-02**: Context file created from Master Sheet
- **2026-02-02**: Engine initialized, signal analysis complete
- **2026-02-02**: Context doc v3 approved
```

---

## D. Initial Inputs Required

### D.1 Feature Initialization Inputs

| Input | Required? | Source | Default |
|-------|-----------|--------|---------|
| **Feature title** | Yes | User | - |
| **Product** | Yes | User or inferred | Prompt if ambiguous |
| **Starting point** | No | User | `signals` (start fresh) |
| **Related insight** | No | From `/analyze-signals` | None |
| **Priority** | No | User | `medium` |
| **Target date** | No | User | None |
| **Stakeholders** | No | Auto from Brain | Editable |

### D.2 Phase-Specific Inputs

**Signal Analysis Phase:**
```yaml
inputs:
  - time_range: "How far back to look for signals?"
    default: "7 days"
    options: ["24 hours", "7 days", "30 days", "custom"]
  - sources: "Which sources to include?"
    default: "all configured"
    options: [slack, jira, github, statsig, gdocs, confluence]
  - keywords: "Additional keywords to filter?"
    default: null
```

**Context Document Phase:**
```yaml
inputs:
  - problem_statement: "What problem are we solving?"
    source: enriched_insight
    editable: true
  - success_metrics: "How will we measure success?"
    source: auto_suggested
    editable: true
  - scope_in: "What's in scope?"
    source: user
    required: true
  - scope_out: "What's explicitly out of scope?"
    source: user
    required: true
```

**Business Case Phase:**
```yaml
inputs:
  - baseline_metrics: "Current state metrics"
    source: statsig_or_manual
    required: true
  - impact_assumptions: "Expected improvement"
    source: user_or_benchmark
    required: true
  - investment_estimate: "Rough effort estimate"
    source: user_or_jira
    required: false  # Can defer to engineering phase
  - approver: "Who needs to approve BC?"
    source: brain_or_user
    required: true
```

**Design Phase:**
```yaml
inputs:
  - design_requirements: "Auto-generated from context doc"
    source: context_doc_v3
    editable: true
  - wireframe_url: "Link to wireframes"
    source: user
    required: true
    validation: url_pattern
  - figma_url: "Link to Figma designs"
    source: user
    required: true
    validation: figma_url_pattern
  - design_approval: "Designer sign-off"
    source: user
    required: true
```

**Engineering Phase:**
```yaml
inputs:
  - complexity_estimate: "T-shirt size or story points"
    source: user_or_eng_lead
    required: false
  - technical_constraints: "Any known constraints?"
    source: user
    required: false
  - adr_decisions: "Resolution of technical options"
    source: user
    required: true  # Per ADR
```

---

## E. Automations

### E.1 Proactive Automations

| Automation | Trigger | Action |
|------------|---------|--------|
| **Signal digest** | Daily at 9am | Summarize new signals, notify if high-priority |
| **Stale feature alert** | Feature inactive >3 days | Slack reminder to user |
| **Stakeholder reminder** | Approval pending >24h | Notify stakeholder |
| **Artifact reminder** | Phase blocked on artifact | Daily reminder until provided |
| **Meeting prep integration** | Meeting with stakeholder | Include feature status in pre-read |
| **Context decay check** | Weekly | Flag if source data is stale |

### E.2 Auto-Population

```yaml
auto_populate:
  stakeholders:
    source: brain_entities
    trigger: insight_selection
    logic: "Find people/teams mentioned in insight sources"

  related_features:
    source: brain_products
    trigger: feature_initialization
    logic: "Find features in same product with similar keywords"

  baseline_metrics:
    source: statsig
    trigger: business_case_start
    logic: "Fetch current metrics for product area"

  meeting_notes:
    source: gdocs
    trigger: any_phase
    logic: "Link recent meeting notes mentioning feature topic"

  jira_context:
    source: jira
    trigger: engineering_phase
    logic: "Find related tickets, estimate from similar work"
```

### E.3 Auto-Transitions

```yaml
auto_transitions:
  # When all required inputs provided, auto-advance
  - from: pending_input
    to: processing
    condition: all_required_inputs_provided

  # When orthogonal challenge passes, suggest advancement
  - from: context_doc_v1
    to: context_doc_v2_ready
    condition: challenge_score >= 80
    action: notify_user  # Don't auto-advance without approval

  # When all tracks complete, trigger decision gate
  - from: parallel_tracks
    to: decision_gate_ready
    condition: all_tracks_complete
    action: notify_user
```

### E.4 Integration Automations

```yaml
integrations:
  slack:
    - event: phase_complete
      action: post_to_channel
      channel: from_config_or_product_channel

    - event: approval_needed
      action: dm_approver

    - event: feature_decision
      action: post_announcement

  jira:
    - event: decision_gate_approved
      action: create_epic
      auto: false  # Prompt user first

    - event: engineering_spec_complete
      action: create_stories_from_spec
      auto: false

  calendar:
    - event: approval_pending > 24h
      action: suggest_meeting

  confluence:
    - event: feature_complete
      action: create_or_update_page
      template: feature_summary
```

---

## F. Validation Framework

### F.1 Validation Types

| Type | When | What | Automated? |
|------|------|------|------------|
| **Input validation** | On entry | Format, required fields | Yes |
| **Content validation** | Pre-phase-complete | Completeness, quality | Partial |
| **Cross-reference** | Throughout | Brain entity links valid | Yes |
| **Challenge validation** | Context doc phases | Orthogonal challenge | Yes |
| **Stakeholder validation** | BC, Decision gate | Human approval | No |
| **Artifact validation** | When attached | URL valid, accessible | Yes |
| **Output validation** | Pre-output | All requirements met | Yes |

### F.2 Quality Gates

Each phase has explicit quality criteria:

```yaml
quality_gates:
  insight_selection:
    criteria:
      - insight_has_multiple_sources: true
      - confidence_score: ">= 0.6"
      - not_duplicate_of_existing_feature: true
    blocking: true

  context_doc_v1:
    criteria:
      - problem_statement_present: true
      - success_metrics_defined: true
      - scope_defined: true
    blocking: true

  context_doc_v2:
    criteria:
      - orthogonal_challenge_run: true
      - challenge_score: ">= 60"
      - critical_challenges_addressed: true
    blocking: true

  context_doc_v3:
    criteria:
      - orthogonal_challenge_run: true
      - challenge_score: ">= 75"
      - all_challenges_addressed: true
    blocking: true

  business_case:
    criteria:
      - baseline_metrics_provided: true
      - assumptions_documented: true
      - roi_positive_in_conservative_case: true  # Warning if not
      - stakeholder_approval: true
    blocking: [stakeholder_approval]  # Only this blocks

  design_track:
    criteria:
      - design_spec_approved: true
      - wireframes_provided: true
      - figma_provided: true  # Can be "in_progress"
    blocking: [design_spec_approved]

  engineering_spec:
    criteria:
      - components_identified: true
      - adrs_decided: true
      - dependencies_listed: true
    blocking: [adrs_decided]

  decision_gate:
    criteria:
      - context_doc_complete: true
      - business_case_approved: true
      - design_track_complete_or_parallel: true
      - engineering_spec_complete: true
      - no_blocking_risks: true
    blocking: all
```

### F.3 Validation Interface

```
/validate-feature

Feature: OTP Checkout Recovery
Current Phase: Design Track

Running validation checks...

┌─────────────────────────────────────────────────────────────┐
│ VALIDATION RESULTS                                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ Context Document                              ✓ PASS        │
│   ✓ Problem statement present                               │
│   ✓ Success metrics defined                                 │
│   ✓ Scope defined                                           │
│   ✓ Orthogonal challenge passed (82/100)                   │
│                                                              │
│ Business Case                                 ✓ PASS        │
│   ✓ Baseline metrics provided                               │
│   ✓ Assumptions documented                                  │
│   ✓ ROI positive in conservative case                       │
│   ✓ Stakeholder approval: Laurent (2026-02-02)             │
│                                                              │
│ Design Track                                  ⚠ INCOMPLETE  │
│   ✓ Design spec approved                                    │
│   ✓ Wireframes provided                                     │
│   ✗ Figma not provided                                      │
│     → Required to proceed to decision gate                  │
│     → Run: /attach-artifact figma                           │
│                                                              │
│ Engineering Spec                              ○ NOT STARTED │
│   Can start in parallel with design completion              │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│ BLOCKERS: 1                                                  │
│   • Figma design URL required                               │
│                                                              │
│ WARNINGS: 0                                                  │
│                                                              │
│ Ready for decision gate: NO (1 blocker)                     │
└─────────────────────────────────────────────────────────────┘
```

### F.4 Continuous Validation

```yaml
continuous_validation:
  # Run on every feature state change
  on_state_change:
    - check: brain_references_valid
      action: warn_if_broken

    - check: source_data_freshness
      action: warn_if_stale
      threshold: 7_days

    - check: stakeholder_still_valid
      action: warn_if_person_left

  # Run daily for active features
  daily:
    - check: approval_sla
      action: remind_if_overdue
      threshold: 24_hours

    - check: phase_duration
      action: warn_if_stuck
      threshold: 3_days

  # Run weekly
  weekly:
    - check: context_relevance
      action: suggest_refresh
      logic: "New signals in same area since context doc?"
```

---

## G. Error Handling & Recovery

### G.1 Common Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| **External URL invalid** | On validation | Prompt for new URL |
| **Stakeholder unavailable** | On reminder failure | Suggest alternate approver |
| **Source data stale** | Age check | Offer to refresh from source |
| **Orthogonal challenge fails hard** | Score < 40 | Suggest major revision or pivot |
| **Feature abandoned** | 14 days inactive | Archive with option to resume |
| **Conflicting features** | Duplicate detection | Merge or differentiate |

### G.2 Resume Capability

```
/resume-feature gc-otp-recovery-2026-02

Resuming feature: OTP Checkout Recovery
Last activity: 3 days ago
Phase: Design Track (waiting for Figma)

┌─────────────────────────────────────────────────────────────┐
│ FEATURE STATE RESTORED                                       │
├─────────────────────────────────────────────────────────────┤
│ What's changed since you left:                              │
│                                                              │
│ • 2 new Slack messages in #good-chop mentioning OTP        │
│ • Statsig experiment updated (now at 25% rollout)          │
│ • Marina's last day is now Feb 12 (was in stakeholder list)│
│                                                              │
│ Pending action: Provide Figma URL                           │
└─────────────────────────────────────────────────────────────┘

Continue where you left off? [Y/n]
```

---

## H. Complete User Journey Example

### Scenario: PM notices checkout issues, builds feature proposal

```bash
# Day 1, Morning - Notice pattern in signals
$ /boot
PM-OS Boot Complete
...
⚠ Signal Alert: 15 new Slack mentions about "OTP" in #good-chop

# Review signals
$ /analyze-signals --filter "otp"

5 insights identified...
[Select insight 1: OTP checkout abandonment]

# Start feature
$ /start-feature "OTP Checkout Recovery" --product "Good Chop" --from-insight 1

Feature initialized: goc-otp-recovery
Location: user/products/new-ventures/good-chop/goc-otp-recovery/
Context file: goc-otp-recovery-context.md
Master Sheet: Row added to "topics" tab (Product: GOC)
Brain entity: [[Entities/Goc_Otp_Recovery]]

# Enrich context
$ /explore-insight

[Review enriched context, edit as needed]
[Approve enrichment]

# Create context document
$ /create-context-doc

Context Document v1 generated at:
  user/products/new-ventures/good-chop/goc-otp-recovery/context-docs/v1-draft.md

Running orthogonal challenge...
Score: 68/100 (3 issues to address)

Challenge output saved to:
  user/products/new-ventures/good-chop/goc-otp-recovery/context-docs/v1-challenge.md

[Address challenge findings]
[Generate v2]

Challenge Score: 78/100 (1 minor issue)
[Accept and proceed]

[Generate v3]
Challenge Score: 85/100 ✓
Context document complete at:
  user/products/new-ventures/good-chop/goc-otp-recovery/context-docs/v3-final.md

# Day 1, Afternoon - Start parallel tracks
$ /business-case start

[Review auto-generated assumptions]
[Refine with actual metrics from Statsig]
[Run sensitivity analysis]

BC v2 ready at:
  user/products/new-ventures/good-chop/goc-otp-recovery/business-case/bc-v2.md

Stakeholder approval required.
Who should approve? [Laurent Ades - from brain entity]

> Laurent

Approval request sent to Laurent via Slack DM.

$ /design-track start

Design spec generated from context doc.
[Review and approve design spec]

Wireframes required. Provide URL:
> https://figma.com/file/wireframes...

Wireframes attached ✓
  → Updated: goc-otp-recovery-context.md (References section)
  → Updated: feature-state.yaml (artifacts.wireframes_url)

Figma designs required. You can proceed to engineering while waiting.

$ /engineering-spec start

Spec generated at:
  user/products/new-ventures/good-chop/goc-otp-recovery/engineering/spec.md

[Review auto-generated spec]
[3 ADRs generated at engineering/adrs/]

# Day 2 - Complete approvals
$ /check-feature goc-otp-recovery

Feature: OTP Checkout Recovery
Location: user/products/new-ventures/good-chop/goc-otp-recovery/

Pending:
- Business Case: Approved by Laurent ✓ (overnight)
    → bc-v2.md renamed to bc-v2-approved.md
- Design: Awaiting Figma URL
- Engineering: 3 ADR decisions needed

# Attach Figma (designer finished)
$ /attach-artifact figma
> https://figma.com/file/final-designs...

Figma attached ✓
  → Updated: goc-otp-recovery-context.md
  → Updated: feature-state.yaml

# Make ADR decisions
$ /adr-decide 1
[Select option 2: FingerprintJS]

$ /adr-decide 2
[Select option 1: 30-day token expiry]

$ /adr-decide 3
[Select option 2: Shared platform service]

All ADRs decided ✓
  → ADRs updated in engineering/adrs/

# Day 2, Afternoon - Decision gate
$ /decision-gate

All tracks complete. Ready for decision.

[Review summary]
Decision: PROCEED

$ /generate-outputs

PRD generated at:
  user/brain/Products/Good_Chop/PRD_Goc_Otp_Recovery.md

Spec machine export ready:
  Run: /export-to-spec --prd PRD_Goc_Otp_Recovery.md

Create Jira epic? [Y/n] > Y
Epic created: GOC-1234
  → Updated: goc-otp-recovery-context.md (References: Jira Epic)
  → Updated: feature-state.yaml (artifacts.jira_epic)

Feature complete!
  Context file status: Done
  Master Sheet status: Done
  All artifacts linked in context file
```

---

## I. Commands Summary

| Command | Purpose | Phase |
|---------|---------|-------|
| `/start-feature` | Initialize new feature | 0 |
| `/analyze-signals` | Review and select insights | 1 |
| `/explore-insight` | Enrich selected insight | 2 |
| `/create-context-doc` | Generate and iterate context doc | 3 |
| `/business-case` | Manage business case track | 4 |
| `/design-track` | Manage design track | 4 |
| `/engineering-spec` | Manage engineering track | 4 |
| `/attach-artifact` | Add external artifact | Any |
| `/validate-feature` | Check quality gates | Any |
| `/check-feature` | View feature status | Any |
| `/resume-feature` | Resume paused feature | Any |
| `/decision-gate` | Final review and decision | 5 |
| `/generate-outputs` | Create PRD + spec input | 6 |
| `/adr-decide` | Make ADR decision | 4 (eng) |

---

*Updated: 2026-02-02*
*Version: 2.1 - Aligned with actual PM-OS v3.3 folder structure*
