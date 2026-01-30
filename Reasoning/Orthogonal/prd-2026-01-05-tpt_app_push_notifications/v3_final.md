---
$schema: brain://entity/project/v1
$id: entity/project/v3-final
$type: project
$version: 1
$created: '2026-01-22T08:31:02.176222Z'
$updated: '2026-01-30T15:14:18.389325'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: nikita
  confidence: 0.65
  source: body_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:02.176222Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: V3 Final
---

# PRD: TPT Mobile App - Push Notifications and Engagement Features

*Final Version (v3) - Orthogonal Challenge Complete*
*Generated: 2026-01-05T13:45:00*

---

## Metadata

| Field | Value |
|-------|-------|
| **PRD ID** | PRD-2026-01-TPT-PUSH |
| **Product** | The Pets Table Mobile App |
| **Status** | Draft (Orthogonal Validated) |
| **Author** | Nikita Gorshkov |
| **Owner** | Prateek Jajoo (Staff PM) |
| **Date** | 2026-01-05 |
| **Orthogonal Status** | Complete (3 rounds) |
| **Assurance Level** | L1 Substantiated |

---

## 1. Purpose

### What This Document Proposes

This PRD defines the push notification and engagement features for The Pets Table (TPT) mobile app v1, designed to drive Active Order Rate (AOR) lift through timely, personalized notifications.

### Why It Matters Now

1. **Revenue Opportunity**: Projected $500K-$2M incremental revenue (range accounts for uncertainty)
2. **App v1 Milestone**: Push notifications are a core unlock for "Engagement & Revenue" phase
3. **Competitive Gap**: Farmer's Dog, Ollie have mature mobile experiences
4. **Customer Pain Point**: "When is my delivery?" is a top support inquiry

### Key Changes from Orthogonal Challenge

- Added sensitivity analysis for revenue projections
- Added customer research requirement before Phase 2
- Defined explicit platform strategy (iOS-first)
- Added frequency capping rules
- Included SMS as complementary channel

---

## 2. Problem Statement

### The Core Problem

> TPT customers lack proactive communication about their pet food deliveries, resulting in missed engagement opportunities, support overhead, and preventable churn.

### Evidence

| Source | Finding | Confidence | From Challenge |
|--------|---------|------------|----------------|
| Customer Support | "When is my delivery?" is top inquiry | High | Validated |
| Email Analytics | Delivery emails have 35% open rate (higher than industry) | High | Added R2 |
| Competitor Analysis | Farmer's Dog, Ollie have push-enabled apps | Medium | Validated |
| 2026 BP | App launch identified as key growth lever | High | Validated |
| **Gap Identified** | No TPT-specific customer research on notification preferences | - | Added R2 |

### Validation Requirement (from Challenge)

**Before Phase 2**, conduct 10-15 customer interviews to validate:
- Notification type preferences
- Acceptable frequency
- Channel preferences (push vs SMS vs email)

---

## 3. Solution

### Hypothesis (Updated)

> If we implement push notifications for delivery reminders and order updates, then we will see measurable AOR improvement (target: 2-5%) and reduced support inquiries, **contingent on** achieving >50% opt-in rate and maintaining <5% opt-out rate.

### Proposed Approach

**Three-tier notification system with validation gates:**

1. **Transactional Notifications** (Phase 1 - Must Have)
   - Delivery scheduled
   - Delivery out for delivery
   - Delivery completed
   - Payment processed

2. **Engagement Notifications** (Phase 2 - Gated)
   - Skip deadline reminder (24h before)
   - Menu selection available
   - *Requires: Phase 1 metrics met + customer research complete*

3. **Personalization Notifications** (Phase 3 - Contingent)
   - Pet birthday reminders
   - Feeding tips
   - *Requires: Phase 2 success*

### Key Features (MVP)

| Feature | Description | Priority | Challenge Response |
|---------|-------------|----------|-------------------|
| Push Permission Flow | In-app prompt with value prop | Must | Enhanced per R2 |
| Delivery Notifications | Order status updates | Must | Validated |
| Notification Preferences | Granular settings screen | Must | Enhanced per R2 |
| Deep Linking | Tap → relevant screen | Must | Tech spike added |
| **Frequency Capping** | Max 3/week, 1/day | Must | **Added from R2** |
| Analytics Integration | Sent, opened, converted tracking | Should | Validated |
| Skip/Edit Reminder | 24h deadline notification | Should | Gated to Phase 2 |
| **SMS Fallback** | For users without app | Should | **Added from R2** |

### Platform Strategy (Resolved from Challenge)

**Decision: iOS-First Launch**

| Factor | iOS | Android | Winner |
|--------|-----|---------|--------|
| TPT Web Traffic | 62% | 38% | iOS |
| Avg Order Value | $85 | $72 | iOS |
| Push Implementation | Native, stable | Fragmented | iOS |
| Timeline Impact | Baseline | +2 weeks | iOS |

**Rationale:** iOS users represent higher-value segment and faster implementation path. Android follows in Phase 2.

### Notification Frequency Rules (Added from Challenge)

| Rule | Specification |
|------|---------------|
| Max per day | 1 notification |
| Max per week | 3 notifications |
| Quiet hours | 9 PM - 9 AM local time |
| Fatigue detection | >2 dismissals without open → reduce frequency |
| Opt-out recovery | 30-day cooldown before re-prompt |

### What This Is NOT

- Not a chat/messaging system
- Not replacing email campaigns (complementary)
- Not a marketing automation tool
- Not Android-first (iOS first, then Android)

---

## 4. Investment Required (Added from Challenge)

### Development Costs

| Phase | Effort (Person-Weeks) | Team |
|-------|----------------------|------|
| Phase 1: Foundation | 6 PW | Mobile + Backend |
| Phase 2: Engagement | 4 PW | Mobile |
| Phase 3: Personalization | 3 PW | Mobile |
| **Total** | **13 PW** | - |

### Infrastructure Costs

| Item | Monthly Cost | Annual Cost |
|------|--------------|-------------|
| Firebase (FCM) | $0 (free tier) | $0 |
| APNs | $99 (Apple Dev) | $99 |
| Analytics (Amplitude) | Existing | $0 incremental |
| **Total** | - | **~$100/year** |

### ROI Analysis (with Sensitivity)

| Scenario | AOR Lift | Revenue Impact | ROI |
|----------|----------|----------------|-----|
| Pessimistic | 2% | $500K | 3.8x |
| Expected | 5% | $1.2M | 9.2x |
| Optimistic | 8% | $2.0M | 15.4x |

**Assumptions:** 13 PW × $10K/PW = $130K development cost

---

## 5. Success Metrics (Enhanced from Challenge)

### Primary Metrics

| Metric | Baseline | Target | Measurement Method |
|--------|----------|--------|-------------------|
| **AOR Lift** | 0% | +2-5% | A/B test with holdout group |
| Push Opt-in Rate | N/A | >50% | In-app analytics |
| Notification Open Rate | N/A | >15% | FCM/APNs reporting |

### Guardrail Metrics

| Metric | Threshold | Action if Breached |
|--------|-----------|-------------------|
| Opt-out Rate | <5% monthly | Reduce frequency |
| Support Tickets (Push) | <10/week | Investigate UX |
| App Uninstalls | <2% lift | Pause notifications |

### Measurement Plan (Added from Challenge)

1. **Holdout Group**: 10% of eligible users receive no push notifications
2. **Attribution Window**: 7 days from notification to conversion
3. **Statistical Power**: 80% power to detect 2% lift with n=5,000 per group
4. **Duration**: 8 weeks minimum for statistical significance
5. **Reporting**: Weekly metrics review, monthly deep-dive

---

## 6. Validation Gates (Added from Challenge)

### Phase 1 → Phase 2 Gate

| Metric | Threshold | Source |
|--------|-----------|--------|
| Push Opt-in Rate | >50% | Analytics |
| Notification Open Rate | >10% | FCM |
| Customer Research Complete | Yes | UXR team |
| No increase in support tickets | <10% increase | Zendesk |

**If gate not met:** Pause Phase 2, investigate, iterate on Phase 1.

### Phase 2 → Phase 3 Gate

| Metric | Threshold | Source |
|--------|-----------|--------|
| Measurable AOR lift | >1% (statistically significant) | A/B test |
| Engagement notification CTR | >8% | Analytics |
| Customer satisfaction | >4/5 stars | In-app survey |

---

## 7. Alternatives Considered (Added from Challenge)

### SMS-First Approach

| Pros | Cons |
|------|------|
| Higher open rates (98%) | Ongoing cost ($0.01-0.05/message) |
| No app required | Less rich experience |
| Faster implementation | Doesn't drive app adoption |

**Decision:** Implement as **complementary channel** for delivery confirmations only. Push remains primary for engagement.

### SMS + Push Hybrid Strategy

| Notification Type | Primary Channel | Fallback |
|-------------------|-----------------|----------|
| Delivery Confirmed | SMS | Push |
| Delivery Reminder | Push | Email |
| Skip Deadline | Push | Email |
| Engagement | Push only | None |

---

## 8. Technical Strategy

### Dependencies

| Dependency | Owner | Status | Risk |
|------------|-------|--------|------|
| React Native shell | Client Platform | Complete | Low |
| FCM integration | Mobile Team | Not Started | Medium |
| APNs integration | Mobile Team | Not Started | Low |
| Backend event system | NV Backend | Partial | Medium |
| **Deep link spike** | Mobile Team | **Required** | **Added R2** |

### Implementation Phases (Updated)

**Phase 1: Foundation (6 weeks)**
- Week 1-2: Deep linking technical spike
- Week 2-4: FCM/APNs integration
- Week 4-5: Permission flow + transactional notifications
- Week 5-6: Analytics + frequency capping

**Phase 2: Engagement (4 weeks) - Gated**
- Requires: Phase 1 gate + customer research
- Skip deadline + menu selection notifications
- Android platform launch

**Phase 3: Personalization (3 weeks) - Contingent**
- Requires: Phase 2 gate
- Pet birthday + feeding tips
- Advanced personalization

---

## 9. Stakeholders

| Stakeholder | Role | Sign-off Required |
|-------------|------|-------------------|
| Prateek Jajoo | Staff PM, TPT | Yes |
| Ahmed Wagdi | EM, NV | Yes (technical) |
| Maria Chelminska | PM, NV | No (inform) |
| Katrina | Designer | Yes (UX) |
| Lindsay | Commercial | Yes (business) |
| Client Platform | Engineering | Yes (technical) |

---

## 10. Challenge FAQ

*Generated from Orthogonal Challenge Process*

### Q: Why is the revenue projection so uncertain ($500K-$2M)?
**A:** The original $1.5M projection lacked TPT-specific validation. We've added sensitivity analysis showing pessimistic (2% lift = $500K) to optimistic (8% lift = $2M) scenarios. The expected case remains $1.2M at 5% lift. We'll validate with A/B testing before claiming specific impact.

### Q: Why don't you have customer research yet?
**A:** This gap was identified in the challenge process. We've added customer research as a **hard gate** before Phase 2. Phase 1 (transactional notifications) proceeds based on industry best practices while we gather TPT-specific insights.

### Q: Why iOS-first instead of both platforms?
**A:** TPT web traffic shows 62% iOS users with higher average order value ($85 vs $72). iOS push implementation is also more straightforward. Android follows in Phase 2, approximately 4 weeks after iOS launch.

### Q: What prevents notification fatigue?
**A:** We've added specific rules: max 3 notifications/week, max 1/day, quiet hours (9PM-9AM), and fatigue detection (reduce frequency after 2+ dismissals). Users have granular control in settings.

### Q: Why not just use SMS instead of building push?
**A:** SMS has higher open rates but ongoing costs and doesn't drive app adoption. We've adopted a **hybrid approach**: SMS for delivery confirmations (high urgency), push for engagement (richer experience). This gives us best of both channels.

### Q: How will you know if this is actually working?
**A:** We're implementing a holdout group (10% receive no push) for proper A/B testing. We need 8 weeks and 5,000 users per group to detect a 2% lift with 80% statistical power. Weekly metrics reviews will catch issues early.

### Q: What if Phase 1 metrics don't meet the gate?
**A:** If opt-in <50% or open rate <10%, we pause Phase 2 investment, investigate root causes (permission flow UX? notification content? timing?), iterate, and re-test. We won't blindly proceed if fundamentals aren't working.

### Q: Why wasn't the development cost in the original PRD?
**A:** Oversight corrected. At ~$130K development cost and expected $1.2M revenue impact, ROI is approximately 9x. Even pessimistic scenario ($500K) yields 3.8x return.

---

## 11. Decision Rationale (FPF)

### DRR Reference
- **DRR Link:** `Brain/Reasoning/Decisions/prd-2026-01-05-tpt_app_push_notifications_drr.md`
- **Assurance Level:** L1 Substantiated

### Key Decisions Made

| Decision | Rationale | Alternatives Rejected |
|----------|-----------|----------------------|
| iOS-first launch | Higher-value users, faster implementation | Both platforms (resource constrained) |
| Hybrid SMS+Push | Best of both channels | SMS-only (doesn't drive app), Push-only (lower reach) |
| Validation gates | Reduce risk of building unused features | Ship everything at once |
| Frequency capping | Prevent notification fatigue | User-controlled only |

### Evidence Chain (Updated)

1. **2026 Business Plan** - App launch priority - CL: 0.9, Weight: 0.25
2. **Customer Support Data** - Delivery inquiry volume - CL: 0.8, Weight: 0.25
3. **iOS Traffic Analysis** - Platform distribution - CL: 0.9, Weight: 0.2
4. **Competitor Analysis** - Market standards - CL: 0.7, Weight: 0.15
5. **Industry Benchmarks** - Push effectiveness - CL: 0.6, Weight: 0.15

### Confidence Assessment by Section

| Section | Confidence | Notes |
|---------|------------|-------|
| Problem Statement | High | Validated by support data |
| Solution Approach | Medium | Pending customer research |
| Revenue Projection | Low-Medium | Range reflects uncertainty |
| Technical Strategy | High | Standard implementation |
| Success Metrics | High | Rigorous measurement plan |

### Conditions for Revisiting

- Phase 1 gate not met after 8 weeks
- Customer research reveals different preferences
- Competitor launches significantly different approach
- Technical blockers emerge from deep link spike

---

## 12. Next Steps

| Action | Owner | Due | Status |
|--------|-------|-----|--------|
| Stakeholder review of v3 PRD | Nikita | 2026-01-08 | Pending |
| Deep linking technical spike | Mobile Team | 2026-01-12 | Not Started |
| Customer research plan | UXR/Prateek | 2026-01-10 | Not Started |
| Design notification permission flow | Katrina | 2026-01-15 | Not Started |
| Define notification content | Prateek | 2026-01-10 | Not Started |
| Engineering estimation | Ahmed | 2026-01-12 | Not Started |

---

## 13. Appendix

### A. Orthogonal Challenge Summary

| Round | Model | Key Contribution |
|-------|-------|------------------|
| 1 | Claude (Originator) | Initial PRD with research + FPF reasoning |
| 2 | Gemini (Challenger) | 8 challenges, 2 alternatives proposed |
| 3 | Claude (Resolver) | All challenges addressed, final PRD |

### B. Challenges Resolution Summary

| # | Challenge | Resolution |
|---|-----------|------------|
| 1 | Revenue projection lacks validation | Added sensitivity analysis |
| 2 | Missing customer research | Added as Phase 2 gate requirement |
| 3 | No cost estimate | Added Investment Required section |
| 4 | Platform not decided | iOS-first decision documented |
| 5 | Notification fatigue risk | Added specific frequency caps |
| 6 | Deep linking complexity | Added technical spike as pre-req |
| 7 | Metrics lack rigor | Added measurement plan with holdout |
| 8 | SMS not considered | Added hybrid SMS+Push strategy |

---

*Orthogonal Challenge Complete | Ready for Stakeholder Review*
