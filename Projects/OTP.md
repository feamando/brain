---
$schema: brain://entity/project/v1
$id: entity/project/otp
$type: project
$version: 1
$created: '2026-01-22T08:31:01.084345Z'
$updated: '2026-01-30T10:22:46.181719'
$confidence: 0.43
$source: unknown
$status: active
$relationships:
- type: related_to
  target: entity/project/factor-form
- type: related_to
  target: entity/project/good-chop
- type: related_to
  target: entity/project/confluence-consumercore
- type: related_to
  target: entity/project/confluence-monoliths
- type: related_to
  target: entity/project/team-consumer-core
- type: related_to
  target: entity/project/team-new-ventures
  confidence: 1.0
  last_verified: '2026-01-30'
$tags:
- project
- active
- high-priority
$aliases:
- One-Time-Purchase
- one-time purchase
- one time purchase
- OTP Capabilities
- seasonal boxes
- guest ordering
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.084345Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.057938+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 19
name: Otp
relationships:
  owner:
  - '[[Entities/Nikita.md]]'
  relates_to:
  - '[[Entities/Squad_Good_Chop.md]]'
---

# One-Time-Purchase (OTP) Capabilities

## Executive Summary
**Definition:** OTP refers strictly to **One-Time Purchase** capabilities, enabling transactional e-commerce flows alongside subscriptions. It is unrelated to One-Time Passwords (authentication).

OTP enables HelloFresh Group brands to address customer demand for flexibility, reducing subscription commitment barriers. It opens avenues for seasonal offerings, product trials, and cross-selling (e.g., Factor meals) to both active and former customers.

**Projected Value:** €24.7M - €28.8M incremental TCVA.

## Roadmap & Milestones

### 2025 Rollouts (Active/Upcoming)
*   **Good Chop OTP:** Offerings for prospects and actives.
    *   *Status:* **100% Live** (Launch declared complete Dec 25).
*   **VMS (Factor Form) OTP:**
    *   *Status:* Pilot Live (W51). Full Rollout planned W02 (Jan 2026).
*   **Factor Form OTP:** Item-based OTP purchase.
    *   *Status:* Planned W02 (Jan 2026). Feature flag ready.
*   **Seasonal Boxes (HelloFresh):** Integrating seasonal boxes into the core experience.
    *   *Status:* Live/In-Progress (Target: €16.5M-€21.5M net revenue).
*   **Formers (UK):** MVP launch for UK market.
    *   *Status:* Planned W50 (Dec 2025).

### 2026 Targets
*   **Intent-Based Routing:** New homepage for canceled customers (Early Q1).
*   **Guest Ordering/Trial Box:** For prospects (Early Q1).
*   **Occasional Boxes:** HF DACH & FR (Easter Launch - Feb/Mar).
*   **New Brands:** Chefs Plate or Youfoodz OTP (Late Q1).
*   **OTP for Actives:** Foundational work (Q2/Q3).
*   **2-Way Marketplace:** Potential PoC.

## Strategic Focus (Q4 2025 / Q1 2026)

### Critical Tech & Data
*   **Marketing Attribution (CRITICAL):** Fixing `plan_id` dependency which loses CAC/CVA tracking for OTP. *Owner: Platform/Marketing Tech.*
*   **CRM Templates:** Developing non-subscription email templates to avoid customer confusion. *Owner: CRM.*
*   **CDP Integration:** Implementing a "New Customer" status for OTP users. *Owner: Consumer Data.*
*   **Cart Consolidation:** Prioritizing use of the global cart service. *Owner: Shopping Foundations.*

### Operational
*   **SCM/Logistics:** Updating local systems (e.g., Demeter in UK) to recognize "order grouping ID". Global scaling requires Odin integration.
*   **Add-ons/Surcharges:** resolving support for add-ons in OTP flow. *Owner: Consumer Core.*

## Current Blockers & Risks
*   **Attribution Blind Spot:** Inability to track CAC/CVA accurately due to legacy `plan_id` architecture (P0).
*   **Communications Risk:** Sending subscription-style emails to OTP customers (P0).
*   **Scaling Blocker:** Local logistics systems (legacy) blocking global rollout (P0).
*   **Voucher Limitations:** Vouchers currently require a subscription link; cannot be applied to OTP orders (P1).
*   **RESOLVED: Good Chop C@C Refunds:** Payment state bug fixed; auto-refund at cutoff working (Dec 25).

## Metrics
*   **TCVA (Total Customer Value Added)**
*   **Net Revenue**
*   **AOV (Average Order Value) Increase**
*   **AOR (Average Order Rate) Increase**
*   **CAC/CVA Tracking Accuracy**

## Changelog
- **2025-12-25:** Context update: **Good Chop OTP:** Launch 100% Live. **C@C Refunds:** Resolved. **Factor Form:** Shopify Storefront Live, OTP W02.
- **2025-12-23:** Context update: **Factor Form:** Shopify Storefront LIVE.
- **2025-12-19:** Context update: **VMS OTP:** Pilot live.
- **2025-12-16:** Mentioned in daily context (3x)
- **2025-12-11:** Context update: **VMS/OTP Launch:** Successfully moved to second week of calendar year to mitigate peak traffic risks.
- **2025-12-09:** Context update: **OTP/Subscribe & Save:** Factor 4 OTP + Subscribe & Save launching **January 5th**.
- **2025-12-08:** Context update: **OTP Capabilities (P0)**: Marketing `plan_id` attribution, CRM email templates, logistics order grouping ID.

## Gdocs Context

- [2026-01-02] One Time Purchase feature being launched, with production demo and pricing structure discussions (from: Factor Form Weekly Tech - Business Sync)

---
*Last updated: 2026-01-02 16:51*


- [2026-01-02] One Time Purchase feature being launched, with specific pricing and discount structures (from: Factor Form Weekly Tech - Business Sync)

- [2026-01-02] One Time Purchase feature being launched on Factor Form with specific pricing and discount structures (from: Factor Form Weekly Tech - Business Sync)

- [2026-01-02] One-time purchase feature being launched by both Factor and Good Chop (from: NVE Product Roadmap Sharing - 2025/12/09)

- [2026-01-02] One-time purchase launch initiative for both Factor and Good Chop (from: NVE Product Roadmap Sharing - 2025/12/09)

- [2026-01-02] One-time purchase feature in development, targeting W3/4 launch with live order testing (from: Good Chop tech sync up)

- [2026-01-02] One-Time Purchase implementation, major project with multiple milestones (from: Good Chop tech sync up)

- [2026-01-02] One-time purchase system being launched for VMS (from: OTP Topics - 2025/12/29 16:00 CET - Note)

- [2026-01-02] System being launched for VMS, experiencing blocker issues (from: OTP Topics - 2025/12/29 16:00 CET - Note)

- [2026-01-02] Running e2e testing, launch date decision for W02, separate OTP/SNS checkout flows (from: Notes: Hamed <> Nikita 1:1)

- [2026-01-02] Main project being launched, went through UAT, ready for production testing, launch decision made for W02 (from: Notes: Hamed <> Nikita 1:1)

- [2026-01-02] Major launch project with UAT testing, e2e testing, and launch date planning for W02 (from: Notes: Hamed <> Nikita 1:1)

- [2026-01-02] Ready to test on live, UAT completed, e2e testing running, launch decision made for W02 (from: Notes: Hamed <> Nikita 1:1)

- [2026-01-02] Ready to test on live, UAT completed, launch decision made for W02 with feature flag (from: Notes: Hamed <> Nikita 1:1)

- [2026-01-02] Ready to test on live, UAT completed, launch decision made for W02 with feature flag (from: Notes: Hamed <> Nikita 1:1)

- [2026-01-02] Ready to test on live, UAT went well, launch decision made for W02 (from: Notes: Hamed <> Nikita 1:1)

- [2026-01-02] One-Time Purchase feature being tested and launched, ready for production testing, UAT completed, launch delayed to W02 (from: Notes: Hamed <> Nikita 1:1)

- [2026-01-02] Launch targeted for January 5th with full UAT scheduled for December 30th (from: Laura:Nikita 1:1 (2w) - 2025/12/19 16:05)

- [2026-01-02] Project requiring ticket updates for new API endpoint approach (from: Alexander Matlin - Handover - Vacation C)

- [2026-01-02] One-time purchase system discussed as alternative approach (from: IXI Results: Creator Marketplace Custome)

- [2026-01-02] One-Time Purchase pricing model introduced as new purchasing option (from: Pricing OTP vs. SNS)

- [2026-01-02] One-Time Purchase pricing model with $65 minimum for free shipping (from: Pricing OTP vs. SNS)

## Slack Context

- [2026-01-02] One-time purchase system being rolled out across multiple teams (#tribe-new-ventures-leads-internal)

## Github Context

- [2026-01-02] Multiple enhancements including e-commerce tracking, product family config, and discount functionality (GitHub commits)