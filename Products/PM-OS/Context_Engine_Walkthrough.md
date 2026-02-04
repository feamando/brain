# Context Creation Engine - Example Walkthrough

**Version**: 1.0
**Created**: 2026-02-04
**Audience**: Product Managers using PM-OS

---

## Overview

This guide walks through a complete example of using the Context Creation Engine to take a feature from initial signal through to an approved PRD. We'll use a realistic feature: **"OTP Checkout Recovery"** for the Good Chop product.

**What you'll learn:**
- How to initialize a new feature
- Creating and iterating on context documents
- Attaching design artifacts
- Working through business case approval
- Running validation and decision gate
- Generating final PRD outputs

---

## The Scenario

**Product**: Good Chop (subscription meat delivery)
**Feature**: OTP Checkout Recovery
**Problem**: Customers who abandon checkout due to OTP (one-time password) verification failures are lost. We want to recover these customers with a retry mechanism.

**Signal Source**: Customer support tickets + Statsig funnel analysis showing 8% drop-off at OTP step.

---

## Step 1: Initialize the Feature

### Command

```bash
/start-feature "OTP Checkout Recovery" --product good-chop --priority P1
```

### Expected Output

```
================================================================
 FEATURE INITIALIZED
================================================================

 Title: OTP Checkout Recovery
 Product: Good Chop (GOC)
 Priority: P1

 Created:
   Folder: user/products/new-ventures/good-chop/goc-otp-recovery/
   Context: goc-otp-recovery-context.md
   State: feature-state.yaml
   Brain: Entities/Goc_Otp_Recovery.md

 Next Steps:
   1. Add to Master Sheet (if not auto-synced)
   2. Review the generated context document
   3. Iterate on context with /check-feature

================================================================
```

### What Got Created

After running the command, your feature folder contains:

```
user/products/new-ventures/good-chop/goc-otp-recovery/
|-- goc-otp-recovery-context.md    # Initial context document
|-- feature-state.yaml             # Engine state tracking
|-- context-docs/                  # Version history folder
```

### Sample: Initial Context Document

```markdown
# OTP Checkout Recovery Context

**Product**: Good Chop
**Created**: 2026-02-04
**Status**: To Do
**Owner**: nikita.gorshkov

## Description

[Problem statement to be refined]

Customers encountering OTP verification failures during checkout
are dropping off. This feature aims to implement recovery mechanisms
to reduce checkout abandonment.

## Stakeholders

- **nikita.gorshkov** (Owner/PM)
- **[Engineering Lead]** (TBD)
- **[Designer]** (TBD)

## References

- Master Sheet: [Good Chop Features]
- Brain Entity: [[Entities/Goc_Otp_Recovery]]

## Action Log

| Date | Action | Status |
|------|--------|--------|
| 2026-02-04 | Feature initialized | Done |
```

---

## Step 2: Refine the Context Document

The engine guides you through iterating the context document from v1 to v3 using the orthogonal challenge system.

### Context Document v1 (Draft)

Edit your `goc-otp-recovery-context.md` to add detail:

```markdown
# OTP Checkout Recovery Context

**Product**: Good Chop
**Created**: 2026-02-04
**Status**: In Progress
**Owner**: nikita.gorshkov

## Description

### Problem Statement

Customers who fail OTP verification during checkout have no recovery path.
Current data shows:
- 8% of customers fail OTP on first attempt
- 65% of those who fail do not retry
- This represents ~$45K monthly in lost revenue

### Proposed Solution

Implement a multi-pronged OTP recovery system:
1. **Resend OTP** - Allow customers to request new code
2. **Alternative verification** - Email magic link fallback
3. **Skip with risk scoring** - Low-risk orders bypass OTP

### Success Metrics

- Reduce OTP-related checkout abandonment from 8% to 3%
- Recover 50% of currently-lost OTP failures
- No increase in fraud rate

## Stakeholders

- **nikita.gorshkov** (Owner/PM)
- **alex.chen** (Engineering Lead)
- **sarah.kim** (Designer)
- **mike.johnson** (Risk/Fraud)

## Scope

### In Scope
- OTP resend functionality
- Email magic link fallback
- Basic fraud scoring integration

### Out of Scope
- Phone call verification
- Third-party auth providers
- International phone number support (phase 2)

## References

- Master Sheet: [Good Chop Features]
- Brain Entity: [[Entities/Goc_Otp_Recovery]]
- Related: [[Checkout_Flow_Optimization]]

## Action Log

| Date | Action | Status |
|------|--------|--------|
| 2026-02-04 | Feature initialized | Done |
| 2026-02-04 | Context v1 drafted | Done |
```

### Run Orthogonal Challenge

The engine will run an orthogonal challenge to score your context document:

```
================================================================
 ORTHOGONAL CHALLENGE RESULTS: v1
================================================================

 Overall Score: 62/100

 STRENGTHS
 ---------
 [+] Clear problem statement with data
 [+] Defined success metrics
 [+] Stakeholders identified

 CHALLENGES
 ----------
 [!] Fraud risk not fully addressed - what if bad actors exploit
     the "skip with risk scoring" option?
 [!] No timeline or phasing proposed
 [!] Technical feasibility of magic link not validated
 [!] Missing competitive analysis - how do others handle this?

 QUESTIONS TO ADDRESS
 --------------------
 1. What fraud controls exist for risk scoring bypass?
 2. How will you measure fraud impact post-launch?
 3. What is the engineering complexity estimate?
 4. Are there regulatory considerations for OTP changes?

 Recommendation: Address challenges and create v2

================================================================
```

### Context Document v2 (After Challenge)

Update your context to address the challenges:

```markdown
# OTP Checkout Recovery Context

**Product**: Good Chop
**Created**: 2026-02-04
**Status**: In Progress
**Owner**: nikita.gorshkov
**Version**: 2

## Description

### Problem Statement

Customers who fail OTP verification during checkout have no recovery path.
Current data shows:
- 8% of customers fail OTP on first attempt
- 65% of those who fail do not retry
- This represents ~$45K monthly in lost revenue

### Proposed Solution

Implement a multi-pronged OTP recovery system:
1. **Resend OTP** - Allow customers to request new code (max 3 attempts)
2. **Alternative verification** - Email magic link fallback
3. **Skip with risk scoring** - Low-risk orders bypass OTP

### Fraud Mitigation (addressing challenge)

Risk scoring bypass will be controlled by:
- Order value threshold: <$75 only
- Customer history: 3+ previous successful orders
- Device fingerprinting: Known device required
- Velocity limits: Max 1 bypass per 24 hours
- Post-launch monitoring: Daily fraud reports for 30 days

### Timeline & Phasing

| Phase | Scope | Timeline |
|-------|-------|----------|
| Phase 1 | Resend OTP only | Sprint 1 (2 weeks) |
| Phase 2 | Email magic link | Sprint 2 (2 weeks) |
| Phase 3 | Risk scoring bypass | Sprint 3 (3 weeks) |

### Success Metrics

- Reduce OTP-related checkout abandonment from 8% to 3%
- Recover 50% of currently-lost OTP failures
- Fraud rate increase <0.1% (hard constraint)
- No regulatory flags from compliance review

### Competitive Analysis

| Competitor | OTP Recovery Approach |
|------------|----------------------|
| HelloFresh | Resend + email fallback |
| Blue Apron | Resend only |
| ButcherBox | No OTP (uses 3DS) |

Good Chop approach aligns with HelloFresh but adds risk scoring
for trusted customers.

## Stakeholders

- **nikita.gorshkov** (Owner/PM)
- **alex.chen** (Engineering Lead)
- **sarah.kim** (Designer)
- **mike.johnson** (Risk/Fraud) - approval required

## Scope

### In Scope
- OTP resend functionality
- Email magic link fallback
- Basic fraud scoring integration
- Compliance review

### Out of Scope
- Phone call verification
- Third-party auth providers
- International phone number support (phase 2)

## References

- Master Sheet: [Good Chop Features]
- Brain Entity: [[Entities/Goc_Otp_Recovery]]
- Related: [[Checkout_Flow_Optimization]]

## Action Log

| Date | Action | Status |
|------|--------|--------|
| 2026-02-04 | Feature initialized | Done |
| 2026-02-04 | Context v1 drafted | Done |
| 2026-02-04 | Orthogonal challenge v1 | Score: 62 |
| 2026-02-04 | Context v2 drafted | Done |
```

### Second Challenge (v2)

```
================================================================
 ORTHOGONAL CHALLENGE RESULTS: v2
================================================================

 Overall Score: 78/100 (improved from 62)

 IMPROVEMENTS NOTED
 ------------------
 [+] Fraud mitigation strategy added
 [+] Phased timeline included
 [+] Competitive analysis provided
 [+] Compliance consideration added

 REMAINING GAPS
 --------------
 [*] Engineering estimate still needed
 [*] Designer review pending
 [*] Rollback plan not documented

 Recommendation: Ready for parallel tracks (score >= 75)

================================================================
```

---

## Step 3: Attach Design Artifacts

Once designers provide wireframes and Figma files, attach them:

### Commands

```bash
/attach-artifact wireframes https://figma.com/file/abc123/GOC-OTP-Recovery-Wireframes
```

### Expected Output

```
================================================================
 ARTIFACT ATTACHED
================================================================

 Type: Wireframes
 URL: https://figma.com/file/abc123/GOC-OTP-Recovery-Wireframes
 Feature: goc-otp-recovery

 Updated:
   - feature-state.yaml (artifacts.wireframes_url)
   - goc-otp-recovery-context.md (References section)

================================================================
```

### Attach Figma Design

```bash
/attach-artifact figma https://figma.com/file/xyz789/GOC-OTP-Recovery-Final-Design
```

### Output

```
================================================================
 ARTIFACT ATTACHED
================================================================

 Type: Figma Design
 URL: https://figma.com/file/xyz789/GOC-OTP-Recovery-Final-Design
 Feature: goc-otp-recovery

 Updated:
   - feature-state.yaml (artifacts.figma)
   - goc-otp-recovery-context.md (References section)

================================================================
```

### Updated References Section

Your context file's References section now shows:

```markdown
## References

- Master Sheet: [Good Chop Features]
- Brain Entity: [[Entities/Goc_Otp_Recovery]]
- Related: [[Checkout_Flow_Optimization]]
- Wireframes: [GOC-OTP-Recovery-Wireframes](https://figma.com/file/abc123/GOC-OTP-Recovery-Wireframes)
- Figma: [GOC-OTP-Recovery-Final-Design](https://figma.com/file/xyz789/GOC-OTP-Recovery-Final-Design)
```

---

## Step 4: Check Feature Status

At any point, check the feature's progress:

### Command

```bash
/check-feature goc-otp-recovery
```

### Expected Output

```
================================================================
 FEATURE STATUS: OTP Checkout Recovery
================================================================

 Slug: goc-otp-recovery
 Product: good-chop
 Phase: parallel_tracks
 Status: In Progress

 Progress: [==============      ] 70%

================================================================
 TRACKS
================================================================

 Context:       [DONE]
 Design:        [DONE]
 Business Case: [REVIEW]
 Engineering:   [WORKING]

================================================================
 PENDING ITEMS (2)
================================================================

 - [Business Case] Awaiting approval from: mike.johnson
 - [Engineering] Engineering estimate needed

================================================================
 BLOCKERS (0)
================================================================

 No blockers!

================================================================
 ARTIFACTS
================================================================

 figma: https://figma.com/file/xyz789/GOC-OTP-Recovery-Final-Design
 wireframes_url: https://figma.com/file/abc123/GOC-OTP-Recovery-Wireframes
 jira_epic: (not attached)

Last activity: 2026-02-04 15:30

================================================================
```

---

## Step 5: Business Case Approval

The business case track requires stakeholder approval. After creating your BC document with metrics and assumptions:

### Sample Business Case Summary

The engine creates `business-case/bc-v1.md` with:

```markdown
# Business Case: OTP Checkout Recovery

## Baseline Metrics

| Metric | Current Value | Source |
|--------|---------------|--------|
| OTP failure rate | 8% | Statsig |
| Retry rate after failure | 35% | Statsig |
| Monthly lost revenue | $45,000 | Finance |
| Avg order value | $125 | Analytics |

## Impact Assumptions

| Scenario | Recovery Rate | Monthly Revenue |
|----------|---------------|-----------------|
| Conservative | 30% | $13,500 |
| Expected | 50% | $22,500 |
| Optimistic | 70% | $31,500 |

## Investment

- Engineering: 7 weeks (3 sprints)
- Design: 2 weeks (already complete)
- Estimated cost: $35,000

## ROI Analysis

| Scenario | Payback Period | 12-month ROI |
|----------|----------------|--------------|
| Conservative | 2.6 months | 363% |
| Expected | 1.6 months | 671% |
| Optimistic | 1.1 months | 980% |

## Required Approvals

- mike.johnson (Risk/Fraud) - Pending
- nikita.gorshkov (PM) - Approved
```

### Recording Approval

When Mike approves (e.g., via Slack), record it:

```
Business Case Approval Recorded:
  Approver: mike.johnson
  Decision: Approved
  Reference: Slack thread 2026-02-04
  Notes: "Fraud controls look solid. Approved with 30-day monitoring."
```

---

## Step 6: Validate Before Decision Gate

Run validation to ensure everything is ready:

### Command

```bash
/validate-feature goc-otp-recovery
```

### Expected Output

```
================================================================
 VALIDATION RESULTS: OTP Checkout Recovery
================================================================

 Feature: goc-otp-recovery
 Product: good-chop
 Current Phase: parallel_tracks

================================================================

 Context                                   [DONE]
-----------------------------------------------------------------
   [PASS]         Context document exists
   [PASS]         Problem statement present
   [PASS]         Stakeholders section present
   [PASS]         Orthogonal challenge completed

 Design                                    [DONE]
-----------------------------------------------------------------
   [PASS]         Design spec document exists
   [PASS]         Wireframes attached
   [PASS]         Figma design attached

 Business Case                             [DONE]
-----------------------------------------------------------------
   [PASS]         Baseline metrics defined
   [PASS]         Impact assumptions documented
   [PASS]         ROI analysis complete
   [PASS]         Approved by: mike.johnson, nikita.gorshkov

 Engineering                               [DONE]
-----------------------------------------------------------------
   [PASS]         Engineering spec created
   [PASS]         2 ADRs accepted
   [PASS]         Estimate: 7 weeks
   [PASS]         No blocking dependencies
   [PASS]         All risks mitigated

================================================================
 DECISION GATE READINESS
================================================================

   [PASS]         Context document complete
   [PASS]         Business case approved
   [PASS]         Design artifacts attached
   [PASS]         Engineering spec complete
   [PASS]         No blocking risks

================================================================
 SUMMARY
================================================================

 Total Blockers: 0
 Total Warnings: 0

 Ready for Decision Gate: YES

================================================================
```

---

## Step 7: Decision Gate

Now run the formal decision gate:

### Command

```bash
/decision-gate goc-otp-recovery --approve --reason "All tracks complete, BC approved by mike.johnson, eng estimate 7 weeks"
```

### Expected Output

```
================================================================
 DECISION GATE REVIEW: OTP Checkout Recovery
================================================================

 Feature: goc-otp-recovery
 Product: good-chop
 Current Phase: parallel_tracks

================================================================
 VALIDATION HOOKS (12/12 passed)
================================================================

 [No critical failures]

================================================================
 QUALITY GATES
================================================================

 Context Track:
   [PASS]         Context document complete

 Business Case Track:
   [PASS]         Approved by: mike.johnson, nikita.gorshkov

 Design Track:
   [PASS]         Figma attached
   [PASS]         Wireframes attached

 Engineering Track:
   [PASS]         Estimate: 7 weeks
   [PASS]         2 ADRs accepted

================================================================
 DECISION GATE REQUIREMENTS
================================================================

   [PASS]         Context document complete
   [PASS]         Business case approved
   [PASS]         Design artifacts attached
   [PASS]         Engineering spec complete
   [PASS]         No blocking risks

================================================================
 BLOCKERS (0 total)
================================================================

   No blockers detected!

================================================================
 RECOMMENDATION
================================================================

   Decision: GO
   Summary: All decision gate requirements met

 Evidence:
   [PASS] Context document complete
   [PASS] Business case approved
   [PASS] Design artifacts attached
   [PASS] Engineering spec complete
   [PASS] No blocking risks

================================================================
 DECISION RECORDED: APPROVED
================================================================

 Feature has been approved and transitioned to OUTPUT_GENERATION phase.

 Next steps:
   1. Generate PRD: /generate-outputs goc-otp-recovery
   2. Export to spec: /export-to-spec goc-otp-recovery
   3. Create Jira epic (optional)

 Report saved: reports/decision-gate-20260204-153000.md

================================================================
```

---

## Step 8: Generate Final Outputs

Generate the PRD and feature summary:

### Command

```bash
/generate-outputs goc-otp-recovery
```

### Expected Output

```
================================================================
 OUTPUT GENERATION COMPLETE
================================================================

 Feature: OTP Checkout Recovery
 Product: good-chop

 Generated Files:
   PRD: user/brain/Products/Good-Chop/PRD_OTP_Checkout_Recovery.md
   Summary: user/products/new-ventures/good-chop/goc-otp-recovery/feature-summary.md

 PRD Contents:
   - Executive Summary
   - Problem Statement
   - Business Case Summary (metrics, impact, ROI)
   - Engineering Approach (estimate, ADRs, risks)
   - Stakeholder Approvals
   - References & Artifacts

 Feature State Updated:
   - Phase: complete
   - Status: Done

================================================================
 NEXT STEPS
================================================================

 1. Review the generated PRD:
    Read: user/brain/Products/Good-Chop/PRD_OTP_Checkout_Recovery.md

 2. Export to spec machine (if ready):
    /export-to-spec PRD_OTP_Checkout_Recovery.md

 3. Create Jira epic (optional):
    /attach-artifact goc-otp-recovery jira GOC-1234

 4. Mark feature as complete in Master Sheet

================================================================
```

### Sample Generated PRD

The generated PRD at `user/brain/Products/Good-Chop/PRD_OTP_Checkout_Recovery.md`:

```markdown
---
title: "OTP Checkout Recovery"
type: prd
status: approved
author: nikita.gorshkov
created: 2026-02-04
version: 1.0
product: good-chop
organization: new-ventures
tags: [good-chop, feature, prd]
---

# PRD: OTP Checkout Recovery

**Product:** Good Chop
**Status:** Approved
**Owner:** nikita.gorshkov
**Created:** 2026-02-04
**Feature Path:** `user/products/new-ventures/good-chop/goc-otp-recovery/`

## Executive Summary

Implement a multi-pronged OTP recovery system to reduce checkout
abandonment from 8% to 3%, recovering ~$22,500 monthly revenue with
a 1.6 month payback period.

## Problem Statement

Customers who fail OTP verification during checkout have no recovery path.
Current data shows:
- 8% of customers fail OTP on first attempt
- 65% of those who fail do not retry
- This represents ~$45K monthly in lost revenue

## Business Case Summary

### Baseline Metrics

- **OTP failure rate**: 8%
- **Retry rate after failure**: 35%
- **Monthly lost revenue**: $45,000

### Expected Impact

- **Recovery rate**: 50%
- **Monthly revenue recovered**: $22,500
- **Fraud rate increase**: <0.1%

### Investment

7 weeks engineering (3 sprints)

### ROI Analysis

- **Payback period**: 1.6 months
- **12-month ROI**: 671%

## Engineering Approach

### Effort Estimate

- **Overall**: 7 weeks
- **Confidence**: High

**Breakdown:**
- Phase 1 (Resend OTP): 2 weeks
- Phase 2 (Email magic link): 2 weeks
- Phase 3 (Risk scoring bypass): 3 weeks

### Architecture Decision Records

- **ADR-001**: Use existing email service for magic links (accepted)
- **ADR-002**: Implement client-side device fingerprinting (accepted)

*Full ADRs available in `goc-otp-recovery/engineering/adrs/`*

### Technical Risks

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Email deliverability issues | Medium | Low | Use primary email provider with fallback |
| Risk scoring false positives | High | Medium | Conservative thresholds + monitoring |

## Stakeholder Approvals

| Approver | Decision | Date | Type | Reference |
|----------|----------|------|------|-----------|
| mike.johnson | Approved | 2026-02-04 | Risk/Fraud | Slack thread |
| nikita.gorshkov | Approved | 2026-02-04 | PM | Direct |

## References & Artifacts

- **Figma Design**: [GOC-OTP-Recovery-Final-Design](https://figma.com/file/xyz789/GOC-OTP-Recovery-Final-Design)
- **Wireframes**: [Wireframes](https://figma.com/file/abc123/GOC-OTP-Recovery-Wireframes)
- **Context Document**: `goc-otp-recovery-context.md`
- **Business Case**: `business-case/bc-v1-approved.md`

## Brain Entities

- [[Entities/Goc_Otp_Recovery]]

## Source Documents

All source documents are available in the feature folder:

```
user/products/new-ventures/good-chop/goc-otp-recovery/
|-- goc-otp-recovery-context.md       # Primary context document
|-- feature-state.yaml                # Engine state
|-- context-docs/                     # Context doc versions
|-- business-case/                    # BC documents
|-- engineering/
|   |-- adrs/                         # Architecture Decision Records
```

---
*Generated by Context Creation Engine on 2026-02-04T15:30:00*
```

---

## Complete Workflow Timeline

| Time | Action | Command |
|------|--------|---------|
| 9:00 AM | Initialize feature | `/start-feature "OTP Checkout Recovery" --product good-chop --priority P1` |
| 9:15 AM | Draft context v1 | (manual edit) |
| 9:30 AM | Run challenge | (automatic) |
| 10:00 AM | Address challenges, create v2 | (manual edit) |
| 10:30 AM | Challenge v2, score 78 | (automatic) |
| 11:00 AM | Attach wireframes | `/attach-artifact wireframes <url>` |
| 11:05 AM | Attach Figma | `/attach-artifact figma <url>` |
| 11:30 AM | Submit BC for approval | (through engine) |
| 2:00 PM | Receive BC approval | (recorded in engine) |
| 2:30 PM | Validate feature | `/validate-feature goc-otp-recovery` |
| 2:45 PM | Decision gate | `/decision-gate goc-otp-recovery --approve --reason "..."` |
| 3:00 PM | Generate outputs | `/generate-outputs goc-otp-recovery` |
| 3:15 PM | PRD ready | Review generated PRD |

**Total time: ~6 hours** (vs. 5+ days manual process)

---

## Command Quick Reference

| Phase | Command | Purpose |
|-------|---------|---------|
| Start | `/start-feature "<title>" --product <id>` | Initialize new feature |
| Any | `/attach-artifact <type> <url>` | Link Figma, Jira, etc. |
| Any | `/check-feature [slug]` | View status & blockers |
| Any | `/resume-feature [slug]` | Resume paused feature |
| Pre-gate | `/validate-feature [slug]` | Check quality gates |
| Gate | `/decision-gate [slug] --approve` | Final GO/NO-GO |
| Final | `/generate-outputs [slug]` | Create PRD |

---

## Tips for Success

1. **Front-load the context document** - The more detail you add in v1, the fewer iterations needed
2. **Run challenges early** - Don't wait; the orthogonal challenge helps identify gaps
3. **Attach artifacts as soon as available** - Keeps progress visible
4. **Use `/check-feature` frequently** - Catches blockers early
5. **Get BC approval in parallel** - Start the approval process while working on engineering
6. **Document decisions** - The engine tracks everything for audit trail

---

## Troubleshooting

### "Feature not found"
- Check the slug spelling
- Use `/check-feature` without arguments in the feature directory
- List all features: `ls user/products/*/*/`

### "Decision gate not passed"
- Run `/validate-feature` to see all blockers
- Address each blocking item
- Re-run `/decision-gate`

### "Business case not approved"
- Check `/check-feature --verbose` for pending approvers
- Follow up with stakeholders directly
- Record approval when received

### "Stale feature warning"
- Feature inactive >3 days triggers reminder
- Use `/resume-feature --sync` to see changes
- Update if source data is outdated

---

## Related Documentation

- **Command Reference**: [[Context_Engine_Commands]]
- **Confluence Guide**: [[Context_Engine_Confluence]]
- **Full PRD**: [[PRD_Context_Creation_Engine_v2]]

---

*Document generated by Context Creation Engine - Iteration 41*
