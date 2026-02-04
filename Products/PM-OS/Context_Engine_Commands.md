# Context Creation Engine Commands

**Version**: 1.0
**Created**: 2026-02-04
**Related PRD**: [[PRD_Context_Creation_Engine_v2]]

## Overview

The Context Creation Engine provides slash commands to guide features from initial signals through to approved PRDs. This document covers all available commands, their arguments, and usage patterns.

## Quick Reference

| Command | Purpose | Phase |
|---------|---------|-------|
| `/start-feature` | Initialize a new feature | Initialization |
| `/attach-artifact` | Link Figma, Jira, etc. | Any phase |
| `/check-feature` | View status and blockers | Any phase |
| `/resume-feature` | Resume paused feature work | Any phase |
| `/validate-feature` | Check quality gates | Parallel Tracks+ |
| `/decision-gate` | Final GO/NO-GO review | Decision Gate |
| `/generate-outputs` | Create PRD and summary | Output Generation |

---

## Workflow Diagram

```
                    +-------------------+
                    |  /start-feature   |
                    +-------------------+
                            |
                            v
                    +-------------------+
                    |  INITIALIZATION   |
                    |  - Alias check    |
                    |  - Folder create  |
                    |  - Brain entity   |
                    +-------------------+
                            |
                            v
                    +-------------------+
                    |  CONTEXT DOC      |
                    |  v1 -> v2 -> v3   |
                    | (challenge loops) |
                    +-------------------+
                            |
        +-------------------+-------------------+
        |                   |                   |
        v                   v                   v
+---------------+   +---------------+   +---------------+
| DESIGN TRACK  |   | BC TRACK      |   | ENG TRACK     |
| /attach-      |   | Assumptions   |   | ADRs          |
|  artifact     |   | Approvals     |   | Estimates     |
+---------------+   +---------------+   +---------------+
        |                   |                   |
        +-------------------+-------------------+
                            |
                            v
                    +-------------------+
                    | /validate-feature |
                    |  Quality gates    |
                    +-------------------+
                            |
                            v
                    +-------------------+
                    |  /decision-gate   |
                    |  GO / NO-GO       |
                    +-------------------+
                            |
                            v
                    +-------------------+
                    | /generate-outputs |
                    |  PRD creation     |
                    +-------------------+
```

---

## Commands

### /start-feature

Initialize a new feature for the Context Creation Engine workflow.

**Purpose**: Entry point for all new features. Creates folder structure, initializes state, checks for duplicates.

**Arguments**:
| Argument | Required | Description |
|----------|----------|-------------|
| `<title>` | Yes | Feature title (in quotes if spaces) |
| `--product <id>` | No | Product ID or name |
| `--from-insight <id>` | No | Link to existing insight |
| `--priority <level>` | No | P0, P1, or P2 (default: P2) |

**Examples**:
```bash
/start-feature "OTP Checkout Recovery"
/start-feature "Improve Login Flow" --product good-chop
/start-feature "Push Notifications" --product tpt --priority P1
```

**What it does**:
1. Identifies target product (explicit flag > Master Sheet > recent context > user selection)
2. Checks for existing features with similar names (alias detection)
3. Creates folder at `user/products/{org}/{product}/{feature-slug}/`
4. Creates `feature-state.yaml` for engine state
5. Creates Brain entity at `Entities/{Feature_Name}.md`
6. Reports next steps

**Output**:
```
FEATURE INITIALIZED
-------------------
Title: OTP Checkout Recovery
Product: Good Chop (GOC)
Priority: P2

Created:
  Folder: user/products/new-ventures/good-chop/goc-otp-recovery/
  Context: goc-otp-recovery-context.md
  State: feature-state.yaml
  Brain: Entities/Goc_Otp_Recovery.md

Next Steps:
  1. Add to Master Sheet
  2. Run /analyze-signals to gather insights
```

---

### /attach-artifact

Link external artifacts (Figma, Jira, Confluence, etc.) to a feature.

**Purpose**: Connect design files, tickets, and documentation to the feature context.

**Arguments**:
| Argument | Required | Description |
|----------|----------|-------------|
| `<type>` | Yes | Artifact type: `figma`, `wireframes`, `jira`, `confluence`, `gdocs` |
| `<url_or_value>` | Yes | Full URL or ticket key (e.g., `GOC-1234`) |
| `--feature <slug>` | No | Feature slug (uses current directory if omitted) |

**Examples**:
```bash
/attach-artifact figma https://figma.com/file/abc123/Design-v1
/attach-artifact jira GOC-1234
/attach-artifact wireframes https://figma.com/file/xyz789/Wireframes
/attach-artifact confluence https://hellofresh.atlassian.net/wiki/spaces/GOC/pages/123456
```

**Artifact Types**:
| Type | Description | URL Pattern |
|------|-------------|-------------|
| `figma` | Figma design files | `figma.com/file/<id>` |
| `wireframes` | Wireframe designs | Same as figma |
| `jira` | Jira tickets/epics | `atlassian.net/browse/<KEY>` or just `GOC-1234` |
| `confluence` | Confluence pages | `atlassian.net/wiki/spaces/<SPACE>/pages/<id>` |
| `gdocs` | Google Docs | `docs.google.com/document/d/<id>` |

**What it does**:
1. Validates URL format for the artifact type
2. Converts Jira ticket keys to full URLs
3. Updates `feature-state.yaml` artifacts section
4. Updates `{feature}-context.md` References section

---

### /check-feature

Display status, progress, pending items, and blockers for a feature.

**Purpose**: Get a comprehensive view of where a feature stands and what needs attention.

**Arguments**:
| Argument | Required | Description |
|----------|----------|-------------|
| `<slug>` | No | Feature slug (uses current directory if omitted) |
| `--verbose` | No | Show detailed track information |

**Examples**:
```bash
/check-feature
/check-feature goc-otp-recovery
/check-feature goc-otp-recovery --verbose
```

**Output includes**:
- Overall progress percentage
- Track status (Context, Design, BC, Engineering)
- Pending items requiring action
- Blockers preventing progress
- Linked artifacts
- Last activity timestamp

**Sample Output**:
```
FEATURE STATUS: OTP Checkout Recovery
=====================================
Slug: goc-otp-recovery
Product: good-chop
Phase: parallel_tracks
Status: In Progress

Progress: [========          ] 45%

TRACKS
------
Context:       [DONE]
Design:        [WORKING]
Business Case: [REVIEW]
Engineering:   [TODO]

PENDING ITEMS (3)
-----------------
- [Design] Figma URL not attached
- [Business Case] Awaiting approval from: john.doe
- [Engineering] Track not started

BLOCKERS (0)
------------
No blockers!
```

---

### /resume-feature

Resume work on a paused or inactive feature with state restoration.

**Purpose**: Pick up where you left off, detecting changes since last session.

**Arguments**:
| Argument | Required | Description |
|----------|----------|-------------|
| `<slug>` | No | Feature slug (uses current directory if omitted) |
| `--sync` | No | Force sync with Master Sheet before resuming |
| `--verbose` | No | Show detailed change detection |

**Examples**:
```bash
/resume-feature
/resume-feature goc-otp-recovery
/resume-feature goc-otp-recovery --sync
/resume-feature --verbose
```

**What it does**:
1. Loads feature state from `feature-state.yaml`
2. Detects file modifications since last session
3. Optionally syncs with Master Sheet for external updates
4. Shows time since last activity
5. Provides suggested next actions based on current phase

**Output includes**:
- Last activity timestamp
- Changes detected since last session
- Current track status
- Pending items
- Suggested next actions

---

### /validate-feature

Run validation checks against quality gates for each phase.

**Purpose**: Verify feature meets requirements before advancing to decision gate.

**Arguments**:
| Argument | Required | Description |
|----------|----------|-------------|
| `<slug>` | No | Feature slug (uses current directory if omitted) |
| `--phase <phase>` | No | Validate specific phase only |
| `--verbose` | No | Show detailed gate criteria |

**Phase Options**: `context`, `design`, `business_case`, `engineering`, `decision_gate`

**Examples**:
```bash
/validate-feature
/validate-feature goc-otp-recovery
/validate-feature goc-otp-recovery --phase design
/validate-feature --verbose
```

**Quality Gates Checked**:

| Phase | Gate | Blocking? |
|-------|------|-----------|
| Context | Problem statement present | Yes |
| Context | Stakeholders defined | No |
| Context | Orthogonal challenge run (v2+) | Yes |
| Design | Design spec present | Yes |
| Design | Wireframes provided | No |
| Design | Figma provided | Yes |
| BC | Baseline metrics provided | Yes |
| BC | Assumptions documented | Yes |
| BC | Stakeholder approval | Yes |
| Engineering | Engineering estimate | Yes |
| Engineering | ADRs decided | Yes |
| Engineering | High-impact risks mitigated | Yes |

**Output**:
```
VALIDATION RESULTS: OTP Checkout Recovery
=========================================

Context                                    [DONE]
-------------------------------------------------
[PASS]         Context document exists
[PASS]         Problem statement present
[PASS]         Stakeholders section present

Design                                     [IN PROGRESS]
-------------------------------------------------
[INCOMPLETE]   Design spec not created
               -> Create design specification document
[PASS]         Wireframes attached
[INCOMPLETE]   Figma design not attached
               -> Run /attach-artifact figma <url>

DECISION GATE READINESS
-----------------------
Ready for Decision Gate: NO (2 blocker(s))
```

---

### /decision-gate

Final review command that validates readiness and records GO/NO-GO decisions.

**Purpose**: Formal checkpoint before PRD generation with full validation.

**Arguments**:
| Argument | Required | Description |
|----------|----------|-------------|
| `<slug>` | No | Feature slug (uses current directory if omitted) |
| `--approve` | No | Directly approve (skip interactive) |
| `--reject` | No | Directly reject |
| `--reason "<text>"` | No | Reason for decision |
| `--verbose` | No | Show detailed validation |

**Examples**:
```bash
/decision-gate
/decision-gate goc-otp-recovery
/decision-gate goc-otp-recovery --approve --reason "All tracks complete, BC approved"
/decision-gate goc-otp-recovery --reject --reason "Missing engineering estimate"
```

**Decision Gate Requirements** (all required for GO):
- Context document v3 complete
- Business case approved by stakeholders
- Figma design attached
- Engineering estimate provided
- All ADRs decided (accepted or rejected)
- No blocking dependencies
- High-impact risks have mitigation plans

**What it does**:
1. Runs all validation hooks
2. Checks quality gates across all tracks
3. Detects blockers
4. Generates GO/NO-GO recommendation
5. Records decision in `feature-state.yaml`
6. Creates audit report in `reports/` folder
7. Transitions to OUTPUT_GENERATION phase if approved

**Output**:
```
DECISION GATE REVIEW: OTP Checkout Recovery
===========================================

QUALITY GATES
-------------
Context Track:
  [PASS]         Context document complete

Business Case Track:
  [PASS]         Approved by: john.doe, jane.smith

Design Track:
  [PASS]         Figma attached
  [PASS]         Wireframes attached

Engineering Track:
  [PASS]         Estimate: 3-4 weeks
  [PASS]         2 ADRs accepted

RECOMMENDATION
--------------
Decision: GO
Summary: All decision gate requirements met
```

---

### /generate-outputs

Generate PRD and feature summary from completed tracks.

**Purpose**: Create final deliverables after decision gate approval.

**Arguments**:
| Argument | Required | Description |
|----------|----------|-------------|
| `<slug>` | No | Feature slug (uses current directory if omitted) |
| `--force` | No | Generate even if decision gate not passed |
| `--verbose` | No | Show detailed generation progress |
| `--product-folder <name>` | No | Override product folder name |

**Examples**:
```bash
/generate-outputs
/generate-outputs goc-otp-recovery
/generate-outputs goc-otp-recovery --verbose
/generate-outputs goc-otp-recovery --force
```

**What it does**:
1. Validates decision gate status (unless `--force`)
2. Extracts content from context document
3. Gathers business case metrics and approvals
4. Gathers engineering estimates and ADRs
5. Generates PRD at `user/brain/Products/{Product}/PRD_{Feature}.md`
6. Generates feature summary at `{feature}/feature-summary.md`
7. Updates feature state to COMPLETE

**PRD Contents**:
- Executive Summary
- Problem Statement
- Business Case Summary (metrics, impact, ROI)
- Engineering Approach (estimate, ADRs, risks, dependencies)
- Stakeholder Approvals
- References & Artifacts
- Source Document Links

**Output Locations**:
| File | Location |
|------|----------|
| PRD | `user/brain/Products/{Product}/PRD_{Feature_Name}.md` |
| Summary | `user/products/{org}/{product}/{feature}/feature-summary.md` |

---

## Common Workflows

### New Feature from Scratch

```bash
# 1. Initialize feature
/start-feature "My New Feature" --product my-product

# 2. Create context document (iterative)
# Engine guides through v1 -> challenge -> v2 -> v3

# 3. Attach design artifacts
/attach-artifact figma https://figma.com/file/...
/attach-artifact wireframes https://figma.com/file/...

# 4. Complete business case
# Engine guides through assumptions and approval

# 5. Complete engineering
# Engine captures ADRs and estimates

# 6. Check status periodically
/check-feature

# 7. Validate before decision
/validate-feature

# 8. Decision gate
/decision-gate --approve --reason "Ready for development"

# 9. Generate outputs
/generate-outputs
```

### Resuming Stale Feature

```bash
# 1. Resume with sync
/resume-feature my-feature --sync

# 2. Review detected changes
# 3. Address pending items shown

# 4. Validate current state
/validate-feature --verbose

# 5. Continue from suggested actions
```

---

## Troubleshooting

### "Feature not found"

**Cause**: Feature slug doesn't match any existing feature folder.

**Fix**:
- Check slug spelling
- Navigate to feature directory and omit the slug argument
- List features: `ls user/products/*/*/`

### "Not in a feature directory"

**Cause**: Current directory has no `feature-state.yaml`.

**Fix**:
- Navigate to feature folder: `cd user/products/{org}/{product}/{feature}/`
- Or provide explicit slug: `/check-feature my-feature`

### "Decision gate not passed"

**Cause**: Attempting `/generate-outputs` before approval.

**Fix**:
- Run `/validate-feature` to see blockers
- Address all blocking issues
- Run `/decision-gate --approve --reason "..."`

### "Business case not approved"

**Cause**: BC track missing required approvals.

**Fix**:
- Check pending approvers: `/check-feature --verbose`
- Follow up with approvers
- Record approval when received

### "High-impact risks need mitigation"

**Cause**: Engineering risks flagged as high-impact without mitigation plans.

**Fix**:
- Review risks in engineering track
- Add mitigation strategy for each high-impact risk
- Re-run `/validate-feature`

---

## Related Documentation

- [[PRD_Context_Creation_Engine_v2]] - Full PRD with implementation details
- `common/tools/context_engine/` - Python implementation
- `common/.claude/commands/` - Command source files

---

*Generated by Context Creation Engine - Iteration 39*
