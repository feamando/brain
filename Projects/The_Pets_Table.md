---
$schema: brain://entity/project/v1
$id: entity/project/the-pets-table
$type: project
$version: 1
$created: '2026-01-22T08:31:00.950796Z'
$updated: '2026-01-30T10:24:59.127670'
$confidence: 0.43
$source: unknown
$status: Active
$relationships:
- type: mentioned_in
  target: nikita
  confidence: 0.65
  source: body_extraction
  last_verified: '2026-01-30'
- type: related_to
  target: entity/project/prateek-jajoo
  confidence: 1.0
  last_verified: '2026-01-30'
- type: related_to
  target: entity/project/team-new-ventures
  confidence: 1.0
  last_verified: '2026-01-30'
- type: related_to
  target: entity/project/v1
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.950796Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:57.443763+00:00'
  type: orphan_cleanup
  actor: system/orphan_cleaner
  changes:
  - field: $relationships
    operation: cleanup
    count: 1
name: The Pets Table
id: project-the-pets-table
title: The Pets Table (TPT)
last_updated: 2025-12-11
related:
- '[[Projects/OTP.md]]'
- '[[Architecture/OWL.md]]'
---

# The Pets Table (TPT)

## Executive Summary

The Pets Table is a premium pet food subscription service within the HelloFresh Group. Focus areas include app development for pet health tracking, terminology updates, and enabling Charge at Checkout.

## Current Initiatives

### App Development (v1)
- **Strategy:** Webview-first "Notification Vehicle" (React Native shell + webviews) to drive AOR.
- **Phasing:**
  - **v0 (POC):** Web Parity (Webview wrapper, persistent login, dashboard face).
  - **v1 (Unlock):** Engagement & Revenue (Native biometric login, **Push Notifications**, native dashboard).
- **Business Impact:** Projected ~$1.5M incremental revenue via +5% AOR lift from notifications.
- **Key Docs:**
  - [TPT App v1 Proposal](../../../Products/The_Pets_Table/TPT_App_v1_Proposal.md)
  - [TPT App 2026 - NV <> Client Platform Sync](https://docs.google.com/document/d/1y-4spjzKmW1QMF-dtEWtm6e2UGdLOv-vZeTYgaWn4rs/edit)
  - [2026 HFG Domain Objectives - TPT](https://docs.google.com/document/d/1NUSJBAi6-mxAVqEjJHkxDWRKX5KvuNdYtro2qZ0VGk8/edit)

### Copy Change: "Meal" → "Recipe"
- **Status:** In progress
- **Owner:** Maria, Prateek

### Charge at Checkout (C@C)
- **Status:** Allocation increase blocked by OWL refund question
- **Owner:** Ahmed (confirm enablement for reactivation)

### Staffing
- Prateek Jajoo joined as Staff Product Manager
- Proposal: Convert Tishi (freelancer) to permanent/contract, funded by GC/TPT

## Key Stakeholders

- **Staff PM:** Prateek Jajoo
- **Designer:** Katrina
- **Commercial Contact:** Lindsay

## Blockers

- **C@C:** Allocation increase blocked by open question on OWL refunds
- **App:** Need to define smallest viable product

## Technical Context
*Auto-synced from GitHub: 2025-12-16*

## Technical Context

*   **Tech Stack:** Built on **React** and **Next.js**, organized as a monorepo using **Yarn Workspaces**. Requires Node.js v22+ and connects to private NPM registries.
*   **Architecture:** Follows a layered **Module System** for structural dependency management. Features a scalable **Config System** to handle multi-brand (HelloFresh, WhiteLabel) and multi-country configurations dynamically.
*   **Core Capabilities:**
    *   **Toolbox:** A proprietary suite of automation scripts and CLI tools.
    *   **Spec-Machine:** Integrated workflows for AI-assisted development (Claude/Cursor).
    *   **Governance:** Enforces code ownership via `.claim.json` files and a "Critical Review" system for high-impact changes.
*   **Testing:** Utilizes **Jest** for unit testing and **Cypress** for end-to-end (E2E) testing.
*   **Deployment:** Hosted on **Vercel**, providing automatic preview environments for Pull Requests (including Contentful draft support) and observability via Grafana.

## Changelog
- **2025-12-16:** Context update: ### The Pets Table (TPT) App
- **2025-12-11:** Context update: **The Pets Table 2026 BP v1 (Internal):** Laurent Guillemain's business plan updated.
- **2025-12-09:** Context update: [ ] **The Pets Table**: Prateek to start app login page/one-pager.
- **2025-12-08:** Context update: ### The Pets Table

- **2025-12-08:** Stub created from daily context synthesis

## Gdocs Context

- [2026-01-02] Human-grade pet food for pet parents, includes loyalty program and app launch plans (from: 2026 Yearly Plan - Consumer Mega-Allianc)

---
*Last updated: 2026-01-02 16:51*


- [2026-01-02] Human-grade pet food for pet parents, with planned loyalty program in Q3 and contingent app launch (from: 2026 Yearly Plan - Consumer Mega-Allianc)

- [2026-01-02] Brand supported by client TRE in New Ventures (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] Brand supported by client TRE (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] Brand using client TRE supported by L2 - New Ventures (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] Brand supported by client TRE in L2 - New Ventures rotation (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] Brand supported by client TRE in New Ventures (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] Brand supported by client TRE (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] Brand using client TRE supported by L2 - New Ventures (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] System handling legal checkbox approval based on zip code (from: Beatrice <> Nikita Weekly 1:1 Notes)

- [2026-01-02] Handling legal checkbox approval based on zip code (from: Beatrice <> Nikita Weekly 1:1 Notes)

- [2026-01-02] Project Katrina is working on successfully (from: Jenna:Nikita 1:1 - 2025/12/15 17:00 CET )

- [2026-01-02] Project Katrina is working on successfully (from: Jenna:Nikita 1:1 - 2025/12/15 17:00 CET )

- [2026-01-02] Previous project where Nikita is happy with the design outcomes (from: Hamed:Nikita 1:1 - 2025/12/18 17:25 CET )

- [2026-01-02] Product where Nikita is happy with the design; has certain constraints about upsetting balance (from: Hamed:Nikita 1:1 - 2025/12/18 17:25 CET )

- [2026-01-02] One of three projects Tishia would be dedicated to if hired (from: Maria:Nikita 1:1 - 2025/12/09 15:17 CET )

- [2026-01-02] One of three projects Tishia would be dedicated to if hired (from: Maria:Nikita 1:1 - 2025/12/09 15:17 CET )

- [2026-01-02] Project requiring bandwidth support and potential funding source for Tishi headcount conversion (from: Series-evanikita-11.md)

- [2026-01-02] Project with bandwidth needs, potential funding source for Tishi conversion, to be included in VMS error metric report (from: Series-evanikita-11.md)

- [2026-01-02] Brand remaining in TAM Alliance, not included in Growth Alliance scope (from: LEGO: Unified Prospects Checkout Feature)

- [2026-01-02] Brand remaining in TAM Alliance, not included in current scope (from: LEGO: Unified Prospects Checkout Feature)

- [2026-01-02] Brand remaining in TAM Alliance, not transferred to Growth Alliance (from: LEGO: Unified Prospects Checkout Feature)

- [2026-01-02] Brand remaining in TAM Alliance, not transferred to Growth Alliance (from: LEGO: Unified Prospects Checkout Feature)

- [2026-01-02] Brand remaining with TAM Alliance, not in Growth Alliance scope (from: LEGO: Unified Prospects Checkout Feature)

- [2026-01-02] Brand remaining in TAM Alliance, not transferred to Growth Alliance (from: LEGO: Unified Prospects Checkout Feature)

- [2026-01-02] Company making promotion decisions for contractors (from: Offshore Contractor Agencies)

- [2026-01-02] Product/service being improved (from: PRD: Dashboard Simplification and Excite)

- [2026-01-02] Dog food product brand being enhanced with portion percentages (from: PRD for different portion percentages in)

- [2026-01-02] Abbreviated name for ThePetsTable (from: PRD: TPT Sign-up Page Revamp)

- [2026-01-02] Pet food subscription company implementing Beam integration (from: PRD: Beam Integration for The Pets Table)

- [2026-01-02] Product/service being improved (from: PRD: Dashboard Simplification and Excite)

- [2026-01-02] Pet food subscription company implementing Beam integration (from: PRD: Beam Integration for The Pets Table)

- [2026-01-02] Pet food subscription company implementing Beam integration (from: PRD: Beam Integration for The Pets Table)

- [2026-01-02] Pet food venture tracked by Net Revenue, website at thepetstable.com (from: CMA Squad overview)

- [2026-01-02] New Ventures pet food squad tracking Net Revenue, managed by Maria Chelminska (PM) and Ahmed Wagdi (EM) (from: CMA Squad overview)

- [2026-01-02] New Ventures squad for pet food business at thepetstable.com (from: CMA Squad overview)

- [2026-01-02] New venture pet food brand tracked for net revenue (from: CMA Squad overview)

- [2026-01-02] Pet food venture with Net Revenue KPI at thepetstable.com (from: CMA Squad overview)

- [2026-01-02] New Ventures squad tracking net revenue for thepetstable.com (from: CMA Squad overview)

- [2026-01-02] New venture for pet food tracking net revenue (from: CMA Squad overview)

- [2026-01-02] New Ventures squad tracking Net Revenue at thepetstable.com (from: CMA Squad overview)

- [2026-01-02] Pet food venture tracking Net Revenue (from: CMA Squad overview)

- [2026-01-02] New venture pet food brand at thepetstable.com tracking net revenue (from: CMA Squad overview)

- [2026-01-02] Primary brand being analyzed for conversion performance (from: Conversion Tool - TPT)

- [2026-01-02] Main product being developed, referenced in JIRA tickets (TPT prefix) (from: Sprint Tracking)

- [2026-01-02] SKU Complexity Calculator tool that requires date mapping functionality (from: TPT SKU Complexity Calculator)

- [2026-01-02] Primary brand with 33 requests - appears to be a pet food subscription service (from: New Ventures: PA Backlog)

- [2026-01-02] Primary brand with 33 requests - appears to be a pet food subscription service (from: New Ventures: PA Backlog)

- [2026-01-02] Primary brand being analyzed for conversion performance (from: Conversion Tool - TPT)

- [2026-01-02] Company/platform developing this pricing model (from: TPT_Pricing Model_vFinal (Live))

- [2026-01-02] Primary business entity for which the 2026 business plan is being created (from: The Pets Table - 2026 BP v1 (Internal))

- [2026-01-02] Primary subject of the business plan document (from: The Pets Table - 2026 BP v1 (Internal))

- [2026-01-02] Company developing this pricing model (likely The Pet Table or similar) (from: TPT_Pricing Model_vFinal (Live))

- [2026-01-02] Primary subject of the business plan document (from: The Pets Table - 2026 BP v1 (Internal))

- [2026-01-02] Pet food product line with trial box offering for new customers (from: KN - Reset To Trial Customers)

- [2026-01-02] Primary brand being analyzed for conversion performance (from: Conversion Tool - TPT)

- [2026-01-02] Primary subject of the business plan document (from: The Pets Table - 2026 BP v1 (Internal))

- [2026-01-02] Primary subject of the business plan document (from: The Pets Table - 2026 BP v1 (Internal))

- [2026-01-02] Primary subject of the business plan document (from: The Pets Table - 2026 BP v1 (Internal))

- [2026-01-02] Company creating this pricing model (likely The Pet Table or similar) (from: TPT_Pricing Model_vFinal (Live))

- [2026-01-02] Primary subject of the business plan document (from: The Pets Table - 2026 BP v1 (Internal))

- [2026-01-02] Company creating this pricing model (likely The Pet Table or similar) (from: TPT_Pricing Model_vFinal (Live))

- [2026-01-02] Primary subject of the business plan document (from: The Pets Table - 2026 BP v1 (Internal))

- [2026-01-02] Company developing this pricing model (likely The Pet Table or similar) (from: TPT_Pricing Model_vFinal (Live))

- [2026-01-02] Primary subject of the business plan document (from: The Pets Table - 2026 BP v1 (Internal))

- [2026-01-02] Primary subject of the business plan document (from: The Pets Table - 2026 BP v1 (Internal))

- [2026-01-02] Primary subject of the business plan document (from: The Pets Table - 2026 BP v1 (Internal))

- [2026-01-02] New customers signing up for trial boxes (from: KN - Reset To Trial Customers)

- [2026-01-02] Company/brand being analyzed in the business case (from: Business Cases - TPT)

- [2026-01-02] Company/brand being analyzed in the business case (from: Business Cases - TPT)

- [2026-01-02] Pet food subscription service developing mobile app (from: TPT App: Discovery)

- [2026-01-02] Pet food subscription service company whose mobile app is being planned (from: TPT App: Discovery)

- [2026-01-02] Referenced in title as 'TPT SKU Complexity Calculator' - likely a product or inventory management system (from: TPT SKU Complexity Calculator)

- [2026-01-02] Team that received one transfer in September-October (from: GoC H1 2026 Product Prioritization - WIP)

- [2026-01-02] Brand driven to new heights, TAM expansion (from: Closing Email: 2026)

- [2026-01-02] New venture squad with draft 2026 roadmap (from: Consumer Mega-Alliance: Q1 2026 Planning)

- [2026-01-02] Team that received one transfer, impacting capacity (from: GoC H1 2026 Product Prioritization - WIP)

- [2026-01-02] Team that received transfer from GoC (from: GoC H1 2026 Product Prioritization - WIP)

- [2026-01-02] Team that received one transfer from GoC (from: GoC H1 2026 Product Prioritization - WIP)

- [2026-01-02] Team that received transfer (from: GoC H1 2026 Product Prioritization - WIP)

- [2026-01-02] Team that received one transfer from GoC (from: GoC H1 2026 Product Prioritization - WIP)

- [2026-01-02] Team that received a transfer from GoC (from: GoC H1 2026 Product Prioritization - WIP)

- [2026-01-02] Team that received a transfer from GoC (from: GoC H1 2026 Product Prioritization - WIP)

- [2026-01-02] Team that received one transfer from GoC (from: GoC H1 2026 Product Prioritization - WIP)

## Slack Context

- [2026-01-02] Brand asking about reactivation meal selection flow, doesn't have reactivation page (#squad-nv-good-chop)


- [2026-01-02] Project with Maria as key contributor (#tribe-new-ventures-internal)

- [2026-01-02] Pet food service offering across US, experiencing subscription SKU update issues (#tribe-new-ventures-internal)

- [2026-01-02] Team within New Ventures tribe, discussed for demo participation (#tribe-new-ventures-leads-internal)

- [2026-01-02] The Pets Table - brand working on preference deprecation and meal selection (#tribe-new-ventures-product)

## Github Context

- [2026-01-02] Product line receiving multiple updates including MSS flag, test refactoring, and UI enhancements (GitHub commits)


- [2026-01-02] Primary project with most commits, likely pet food subscription platform (GitHub commits)