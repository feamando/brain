---
$schema: brain://entity/project/v1
$id: entity/project/good-chop
$type: project
$version: 1
$created: '2026-01-22T08:31:01.070907Z'
$updated: '2026-01-30T10:22:46.190472'
$confidence: 0.43
$source: unknown
$status: Active
$relationships:
- type: related_to
  target: entity/project/otp
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/owl
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/sameer-doda
  confidence: 1.0
  last_verified: '2026-01-30'
- type: related_to
  target: entity/project/deo
  confidence: 1.0
  last_verified: '2026-01-30'
- type: related_to
  target: entity/project/team-new-ventures
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.070907Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.040930+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 5
- timestamp: '2026-01-22T10:41:57.447279+00:00'
  type: orphan_cleanup
  actor: system/orphan_cleaner
  changes:
  - field: $relationships
    operation: cleanup
    count: 1
name: Good Chop
id: project-good-chop
title: Good Chop
last_updated: 2025-12-08
related:
- '[[Projects/OTP.md]]'
- '[[Architecture/OWL.md]]'
---

# Good Chop

## Executive Summary

Good Chop is a premium meat subscription service within the HelloFresh Group portfolio. Current focus is on operational improvements, pricing experiments, and enabling one-time purchase (OTP) capabilities.

## Current Initiatives

### OTP Launch
- **Target:** W02 2026 (Jan) for Prospects
- **Status:** In Progress (Actives launching W51 Dec 2025)
- **Related:** [[Projects/OTP.md]]

### Charge at Checkout (C@C)
- **Status:** Incremental rollout in progress
- **Blocker:** Refunds via OWL not triggering for C@C customers (Jira: SE-22404)
- **Related:** [[Architecture/OWL.md]]

### Good Chop Shopify Migration
- **Complexity:** Higher than Factor Form due to customer journey changes
- **Immediate Steps:**
  - Strategy document
  - Customer journey mapping
  - Edge cases (account duplication, redirects)
  - Third-party integrations (Recharge, Elevar)

### Price Value Experiment
- **Status:** Planned for H1 2026

## H1 2026 Focus

1. Close 2025 gaps (OTP for Prospects, Price Value Experiment, Seamless v2, Referrals)
2. Q2: Drive AOR through Engagement (Menu experimentation, rich PDPs)

## Current Blockers

- **Trial Box Profitability Dashboard:** Broken due to data pipeline changes - critical for Referrals structure decision
- **C@C Refunds:** Not processing via OWL (works via Bob)

## Key Stakeholders

- **PM:** Deo
- **Leadership:** Yury
- **Engineering:** Alex Matlin

## Metrics

- AOR (Average Order Rate)
- Menu assortment test results
- Search experiment conversion

## Technical Context
*Auto-synced from GitHub: 2025-12-16*

## Technical Context

*   **Tech Stack:** Built with **React** and **Next.js** within a **Yarn Workspaces** monorepo. Requires Node.js (LTS) and utilizes **Jest** for unit testing and **Cypress** for end-to-end testing.
*   **Architecture:** Follows a strict **Module System** layered architecture. Features a custom **Config System** and **Toolbox** (CLI/scripts) to manage multi-brand support (HelloFresh, WhiteLabel) and internal automation.
*   **Deployment:** Hosted on **Vercel**, utilizing automatic Preview Environments for PRs and Vercel/Grafana for monitoring. Secrets and credentials are secured via **Vault** and a private NPM registry.
*   **Core Capabilities:** 
    *   Dynamic brand and country configuration.
    *   **Spec-machine** integration for AI-assisted workflows (Claude/Cursor).
    *   Contentful draft content preview integration.
    *   Critical review governance system for code ownership.
## Technical Context
*Auto-synced from GitHub: 2025-12-16*

## Technical Context

*   **Tech Stack:** Built with **React** and **Next.js** within a **Yarn Workspaces** monorepo. Requires Node.js (LTS) and utilizes **Jest** for unit testing and **Cypress** for end-to-end testing.
*   **Architecture:** Follows a strict **Module System** layered architecture. Features a custom **Config System** and **Toolbox** (CLI/scripts) to manage multi-brand support (HelloFresh, WhiteLabel) and internal automation.
*   **Deployment:** Hosted on **Vercel**, utilizing automatic Preview Environments for PRs and Vercel/Grafana for monitoring. Secrets and credentials are secured via **Vault** and a private NPM registry.
*   **Core Capabilities:** 
    *   Dynamic brand and country configuration.
    *   **Spec-machine** integration for AI-assisted workflows (Claude/Cursor).
    *   Contentful draft content preview integration.
    *   Critical review governance system for code ownership.
## Changelog
- **2025-12-16:** Context update: **Good Chop Hiring:** Opening mid-level designer role immediately (replace David). Focus on systematic design execution.
- **2025-12-11:** Context update: **Contractor Updates:** Good Chop has one contractor until June; Yury committed to 2 FE + 1 BE for Good Chop (Alex opening). One GPD contractor kept f
- **2025-12-09:** Context update: **Alignment:** Meeting to align on next year's plans across various teams (Maria, Prateek, Factor, Good Chop, Alison Ryan, Nikita).
- **2025-12-08:** Context update: **Good Chop "Charge at Checkout"**: Refunds not processing via OWL (Jira SE-22404). (From 12/05)

- **2025-12-08:** Stub created from daily context synthesis

## Gdocs Context

- [2026-01-02] Digital butcher experience delivering premium, locally sourced proteins to US consumers (from: 2026 Yearly Plan - Consumer Mega-Allianc)

---
*Last updated: 2026-01-02 16:51*


- [2026-01-02] Digital butcher experience delivering premium, locally sourced proteins to US consumers (from: 2026 Yearly Plan - Consumer Mega-Allianc)

- [2026-01-02] Brand supported by client TRE in New Ventures (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] Brand supported by client TRE (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] Brand using client TRE supported by L2 - New Ventures (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] Brand supported by client TRE in L2 - New Ventures rotation (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] Brand supported by client TRE in New Ventures (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] Brand supported by client TRE (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] Brand using client TRE supported by L2 - New Ventures (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] Product with H1 roadmap focusing on OTP launch and price value experiments (from: NVE Product Roadmap Sharing - 2025/12/09)

- [2026-01-02] Product with H1 roadmap prioritizing OTP launch and price value experiments (from: NVE Product Roadmap Sharing - 2025/12/09)

- [2026-01-02] Marina backfill needed, search improvements in Q1 roadmap (from: Notes - Shopping & NV Team Leads Weekly)

- [2026-01-02] Main project being discussed in tech sync meetings (from: Good Chop tech sync up)

- [2026-01-02] Brand with existing precheckout meal selection implementation using static weekly menus (from: Spike - Precheckout Meal Selection FJ)

- [2026-01-02] Main project being discussed in tech sync meetings (from: Good Chop tech sync up)

- [2026-01-02] System being discussed with voucher and menu configuration issues (from: Tech Sync Good Chop - 2025/12/17 21:00 C)

- [2026-01-02] Subject of technical sync meeting (from: Tech Sync Good Chop - 2025/12/17 19:34 C)

- [2026-01-02] Good Chop - H1 2026 Product Prioritization and 2026 OKRs (from: Beatrice <> Nikita Weekly 1:1 Notes)

- [2026-01-02] Shopify migration project, more complex than Factor Form with potential customer journey changes (from: Sameer:Nikita 1:1 - 2025/12/05 15:29 CET)

- [2026-01-02] Shopify migration project, more complex than Factor Form with customer journey changes (from: Sameer:Nikita 1:1 - 2025/12/05 15:29 CET)

- [2026-01-02] Team/project needing mid-level designer replacement (from: Jenna:Nikita 1:1 - 2025/12/15 17:00 CET )

- [2026-01-02] Team/project needing mid-level designer replacement (from: Jenna:Nikita 1:1 - 2025/12/15 17:00 CET )

- [2026-01-02] Upcoming project with strategy, design, and contract considerations; target launch early March (from: Ali:Nikita 1:1 - 2025/12/16 17:45 CET - )

- [2026-01-02] Future project that will benefit from Shopify VMS learnings, contracts under legal review (from: Ali:Nikita 1:1 - 2025/12/09 17:47 CET - )

- [2026-01-02] Brand remaining in TAM Alliance, not included in Growth Alliance scope (from: LEGO: Unified Prospects Checkout Feature)

- [2026-01-02] HelloFresh brand launching OTP in US, September 2025, targeting $180m ARR (from: One Time Purchase - Analytical Data Brie)

- [2026-01-02] HelloFresh brand launching OTP in US, September 2025, targeting $180M ARR (from: One Time Purchase - Analytical Data Brie)

- [2026-01-02] HelloFresh brand launching OTP in US, September 2025, targeting $180M ARR (from: One Time Purchase - Analytical Data Brie)

- [2026-01-02] HelloFresh brand launching OTP in US market September 2025, targeting $180M ARR (from: One Time Purchase - Analytical Data Brie)

- [2026-01-02] HelloFresh brand launching OTP in US, September 2025, targeting $180M ARR (from: One Time Purchase - Analytical Data Brie)

- [2026-01-02] Hiring initiative with three positions pending approval (from: Alexander Matlin - Handover - Vacation C)

- [2026-01-02] Brand remaining in TAM Alliance, not included in current scope (from: LEGO: Unified Prospects Checkout Feature)

- [2026-01-02] Brand remaining in TAM Alliance, not transferred to Growth Alliance (from: LEGO: Unified Prospects Checkout Feature)

- [2026-01-02] Brand remaining in TAM Alliance, not transferred to Growth Alliance (from: LEGO: Unified Prospects Checkout Feature)

- [2026-01-02] Brand remaining with TAM Alliance, not in Growth Alliance scope (from: LEGO: Unified Prospects Checkout Feature)

- [2026-01-02] Brand remaining in TAM Alliance, not transferred to Growth Alliance (from: LEGO: Unified Prospects Checkout Feature)

- [2026-01-02] Premium meat and seafood brand implementing OTP for prospects and actives (from: PRD: Enabling One-Time-Purchase (OTP) Ca)

- [2026-01-02] Target brand for unified funnel (from: PRD: Cancellation Funnel Unification)

- [2026-01-02] Premium meat and seafood OTP offering use case (from: PRD: Enabling One-Time-Purchase (OTP) Ca)

- [2026-01-02] Premium meat and seafood offering for OTP purchase (from: PRD: Enabling One-Time-Purchase (OTP) Ca)

- [2026-01-02] Premium meat and seafood offering for OTP purchases (from: PRD: Enabling One-Time-Purchase (OTP) Ca)

- [2026-01-02] Premium meat and seafood offering for OTP purchase (from: PRD: Enabling One-Time-Purchase (OTP) Ca)

- [2026-01-02] Primary brand launching the Shopify storefront (from: DRAFT - Good Chop - Shopify Storefront)

- [2026-01-02] Primary brand/product being developed (from: DRAFT - Good Chop - Shopify Storefront)

- [2026-01-02] Reference system for add-ons store implementation (from: PRD: Dashboard Simplification and Excite)

- [2026-01-02] Mentioned as comparison for session percentages to address page (from: PRD: TPT Sign-up Page Revamp)

- [2026-01-02] Mentioned as comparison for session percentages to Address page (from: Memo: TPT Sign-up Page Revamp)

- [2026-01-02] Comparison benchmark mentioned for session percentages (from: Memo: TPT Sign-up Page Revamp)

- [2026-01-02] Target brand for unified funnel (from: PRD: Cancellation Funnel Unification)

- [2026-01-02] New venture tracked by Net Revenue KPI, website at goodchop.com (from: CMA Squad overview)

- [2026-01-02] New Ventures squad tracking Net Revenue, managed by Beatrice Dimarucut (PM) and Alexander Matlin (EM) (from: CMA Squad overview)

- [2026-01-02] New Ventures squad tracking net revenue at goodchop.com (from: CMA Squad overview)

- [2026-01-02] New venture brand tracked for net revenue (from: CMA Squad overview)

- [2026-01-02] New venture with Net Revenue KPI at goodchop.com (from: CMA Squad overview)

- [2026-01-02] New Ventures squad tracking net revenue for goodchop.com (from: CMA Squad overview)

- [2026-01-02] New venture tracking net revenue (from: CMA Squad overview)

- [2026-01-02] New Ventures squad tracking Net Revenue at goodchop.com (from: CMA Squad overview)

- [2026-01-02] New venture tracking Net Revenue (from: CMA Squad overview)

- [2026-01-02] New venture brand at goodchop.com tracking net revenue (from: CMA Squad overview)

- [2026-01-02] Separate product with GOC prefix in JIRA tickets (from: Sprint Tracking)

- [2026-01-02] Brand working on one-time-deliveries page and OTP detection (from: The Pets Table - 2026 BP v1 (Internal))

- [2026-01-02] Meat and seafood subscription service offering promotional vouchers for free products (from: Good Chop Marketing Vouchers)

- [2026-01-02] Squad needing 3 roles (1 filled FE transfer, 2 pending: Senior PM and Senior Designer) due to team expansion to 10 people (from: Open roles EPD New ventures - 2026)

- [2026-01-02] Squad expanding to 10 people, needs Product Owner and Designer backfills (from: Open roles EPD New ventures - 2026)

- [2026-01-02] Squad expanding to 10 people, needs 3 roles: 1 filled FE transfer, 1 pending PO, 1 pending designer to replace Marina Guthmann (from: Open roles EPD New ventures - 2026)

- [2026-01-02] Meat subscription service running promotional tests across multiple marketing channels (from: Good Chop: Tests Control Center (TCC))

- [2026-01-02] Major expansion with 5 roles (1 filled, 1 pending designer, 3 pending new engineering roles) funded by Good Chop P&L (from: Open roles EPD New ventures - 2026)

- [2026-01-02] Company being tracked in the marketing performance spreadsheet (from: Good Chop - iTracker (Internal Tracker -)

- [2026-01-02] Secondary brand with 10 requests - subscription service with OTP and cadence experiments (from: New Ventures: PA Backlog)

- [2026-01-02] Secondary brand with 10 requests - subscription service with OTP and cadence experiments (from: New Ventures: PA Backlog)

- [2026-01-02] Company for which roadmap is created (from: Roadmap - Good Chop 2025/2026)

- [2026-01-02] Company for which the roadmap is created (from: Roadmap - Good Chop 2025/2026)

- [2026-01-02] Pilot team with Alexander Matlin as PoC, has DORA metrics (from: AI-Native Pilot Teams)

- [2026-01-02] Company for which roadmap is created (from: Roadmap - Good Chop 2025/2026)

- [2026-01-02] Company for which roadmap is created (from: Roadmap - Good Chop 2025/2026)

- [2026-01-02] Company for which the roadmap is created (from: Roadmap - Good Chop 2025/2026)

- [2026-01-02] Company for which the roadmap is created (from: Roadmap - Good Chop 2025/2026)

- [2026-01-02] Main company/product being developed (from: Roadmap - Good Chop 2025/2026)

- [2026-01-02] Company for which the roadmap is created (from: Roadmap - Good Chop 2025/2026)

- [2026-01-02] Pilot team with complete DORA metrics, PoC: Alexander Matlin (from: AI-Native Pilot Teams)

- [2026-01-02] Company for which the roadmap is created (from: Roadmap - Good Chop 2025/2026)

- [2026-01-02] Product brand being worked on, multiple references to brand guidelines and reviews (from: Product - Onboarding Checklist (Deo/Beat)

- [2026-01-02] Company for which this roadmap is created (from: Roadmap - Good Chop 2026)

- [2026-01-02] Company for which roadmap is created (from: Roadmap - Good Chop 2026)

- [2026-01-02] Primary company/product being tracked (from: Roadmap - Good Chop 2026)

- [2026-01-02] Primary company/product being tracked (from: Roadmap - Good Chop 2026)

- [2026-01-02] Food delivery/subscription service company (from: Roadmap - Good Chop 2026)

- [2026-01-02] Company for which the roadmap is created (from: Roadmap - Good Chop 2026)

- [2026-01-02] Main company/product being tracked in roadmap (from: Roadmap - Good Chop 2026)

- [2026-01-02] Main company/product being tracked (from: Roadmap - Good Chop 2026)

- [2026-01-02] Meat delivery/subscription service running promotional tests (from: Good Chop: Tests Control Center (TCC))

- [2026-01-02] Meat subscription/delivery service running marketing tests (from: Good Chop: Tests Control Center (TCC))

- [2026-01-02] Meat delivery/subscription service running promotional campaigns and A/B tests (from: Good Chop: Tests Control Center (TCC))

- [2026-01-02] Meat subscription service conducting marketing tests, appears to be owned by or affiliated with HelloFresh (from: Good Chop: Tests Control Center (TCC))

- [2026-01-02] Meat delivery/subscription service running promotional tests across multiple marketing channels (from: Good Chop: Tests Control Center (TCC))

- [2026-01-02] Meat subscription/delivery service running promotional test campaigns (from: Good Chop: Tests Control Center (TCC))

- [2026-01-02] Meat delivery service running marketing tests (from: Good Chop: Tests Control Center (TCC))

- [2026-01-02] Meat delivery/subscription service running promotional test campaigns (from: Good Chop: Tests Control Center (TCC))

- [2026-01-02] Company offering meat and food subscription service with promotional vouchers (from: Good Chop Marketing Vouchers)

- [2026-01-02] Company being tracked - appears to be a food/meal delivery service based on name (from: Good Chop - iTracker (Internal Tracker -)

- [2026-01-02] Company being tracked - likely a food/meal delivery service based on name (from: Good Chop - iTracker (Internal Tracker -)

- [2026-01-02] Company being tracked - likely a food/meal delivery service based on name (from: Good Chop - iTracker (Internal Tracker -)

- [2026-01-02] Company offering meat and food subscription service with promotional vouchers (from: Good Chop Marketing Vouchers)

- [2026-01-02] Company being tracked - likely a food/meal delivery service based on name (from: Good Chop - iTracker (Internal Tracker -)

- [2026-01-02] Company being tracked - likely a food/meal delivery service based on name (from: Good Chop - iTracker (Internal Tracker -)

- [2026-01-02] Company being tracked - likely a food/meal delivery service based on name (from: Good Chop - iTracker (Internal Tracker -)

- [2026-01-02] Company being tracked - likely a food/meal delivery service based on name (from: Good Chop - iTracker (Internal Tracker -)

- [2026-01-02] Company being tracked - likely a food/meal delivery service based on name (from: Good Chop - iTracker (Internal Tracker -)

- [2026-01-02] Meat and seafood subscription service offering promotional vouchers (from: Good Chop Marketing Vouchers)

- [2026-01-02] Company being tracked - likely a food/meal delivery service based on name (from: Good Chop - iTracker (Internal Tracker -)

- [2026-01-02] Main company offering meat and food subscription service with promotional vouchers (from: Good Chop Marketing Vouchers)

- [2026-01-02] Company being tracked - likely a food/meal delivery service based on name (from: Good Chop - iTracker (Internal Tracker -)

- [2026-01-02] Company being tracked - likely a food/meal delivery service based on name (from: Good Chop - iTracker (Internal Tracker -)

- [2026-01-02] Food delivery company offering meat and seafood products with promotional vouchers (from: Good Chop Marketing Vouchers)

- [2026-01-02] Company being tracked - likely a food/meal delivery service based on name (from: Good Chop - iTracker (Internal Tracker -)

- [2026-01-02] Food delivery company offering meat and seafood subscriptions with promotional vouchers (from: Good Chop Marketing Vouchers)

- [2026-01-02] Food delivery company offering meat and seafood subscriptions with promotional vouchers (from: Good Chop Marketing Vouchers)

- [2026-01-02] Company being tracked - likely a food/meal delivery service based on name (from: Good Chop - iTracker (Internal Tracker -)

- [2026-01-02] Company being tracked - likely a food/meal delivery service based on name (from: Good Chop - iTracker (Internal Tracker -)

- [2026-01-02] Food delivery company offering meat and seafood subscriptions with promotional vouchers (from: Good Chop Marketing Vouchers)

- [2026-01-02] Company being tracked; likely a food/meal delivery service based on name (from: Good Chop - iTracker (Internal Tracker -)

- [2026-01-02] Meat and food subscription/delivery service offering promotional vouchers (from: Good Chop Marketing Vouchers)

- [2026-01-02] Company being tracked - likely a food/meal delivery service based on name (from: Good Chop - iTracker (Internal Tracker -)

- [2026-01-02] Company being tracked - likely a food/meal delivery service based on name (from: Good Chop - iTracker (Internal Tracker -)

- [2026-01-02] Company being tracked - likely a food/meal delivery service based on name (from: Good Chop - iTracker (Internal Tracker -)

- [2026-01-02] Company working with Anatta delivery team (from: [Active] 2025 Consumer Core Operating Mo)

- [2026-01-02] Good Chop - product team planning H1 2026 strategy (from: GoC H1 2026 Product Prioritization - WIP)

- [2026-01-02] Meat subscription service with marketing campaigns and pricing experiments (from: GoC H1 2026 Product Prioritization - WIP)

- [2026-01-02] Brand driven to new heights, TAM expansion (from: Closing Email: 2026)

- [2026-01-02] New venture squad with 2025/2026 roadmap (from: Consumer Mega-Alliance: Q1 2026 Planning)

- [2026-01-02] Good Chop - main product/brand for H1 2026 strategy (from: GoC H1 2026 Product Prioritization - WIP)

- [2026-01-02] Team owning H1 2026 product prioritization (from: GoC H1 2026 Product Prioritization - WIP)

- [2026-01-02] Team responsible for H1 2026 product prioritization (from: GoC H1 2026 Product Prioritization - WIP)

- [2026-01-02] Team/product name for H1 2026 strategy (from: GoC H1 2026 Product Prioritization - WIP)

- [2026-01-02] Team responsible for H1 2026 product prioritization (from: GoC H1 2026 Product Prioritization - WIP)

- [2026-01-02] Team responsible for H1 2026 product prioritization (from: GoC H1 2026 Product Prioritization - WIP)

- [2026-01-02] Product team responsible for H1 2026 strategy (from: GoC H1 2026 Product Prioritization - WIP)

## Slack Context

- [2026-01-02] Primary squad/brand being supported in this channel (#squad-nv-good-chop)


- [2026-01-02] Primary brand context for the squad, mentioned in discount communication and sub-brand work (#squad-nv-good-chop)

- [2026-01-02] White-label brand with weekly menu, checkout flows, and cut selection features (#squad-nv-good-chop)

- [2026-01-02] E-Commerce platform worked on by team members (#tribe-new-ventures-internal)

- [2026-01-02] Experiencing same subscription SKU update issues as TPT, investigating Select Cuts page performance optimization (#tribe-new-ventures-internal)

- [2026-01-02] Team within New Ventures tribe, discussed legal confirmation checkbox and payments page improvements (#tribe-new-ventures-leads-internal)

- [2026-01-02] Demoing Multi-SKU free cut selection on Reactivation page (#tribe-new-ventures-leads-internal)

- [2026-01-02] Brand considering implementing California checkbox logic and charge at checkout (#tribe-new-ventures-product)

- [2026-01-02] Digital butcher brand needing funnel dashboard, operating on legacy Whitelabel dashboard, planning Q2 2026 dashboard release with Future Boxes feature (#tribe-new-ventures-product)

## Github Context

- [2026-01-02] OTP cart creation and banner copy updates (GitHub commits)


- [2026-01-02] Unified payments feature flag removal, free-addon styling, checkout test fixes (GitHub commits)

- [2026-01-02] Price migration, shipping discount logic, and voucher display improvements (GitHub commits)

- [2026-01-02] Brand-specific gift redemption and reactivation e2e configuration (GitHub commits)

- [2026-01-02] Reactivation flow enhancements including free cuts popup, OTP data attributes, and test updates (GitHub commits)

- [2026-01-02] Secondary project with reactivation and voucher-related work (GitHub commits)