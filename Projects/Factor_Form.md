---
$schema: brain://entity/project/v1
$id: entity/project/factor-form
$type: project
$version: 1
$created: '2026-01-22T08:31:01.042658Z'
$updated: '2026-01-30T10:22:46.198341'
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
- type: owned_by
  target: entity/person/allison
  since: null
  until: null
  role: null
  metadata: null
- type: related_to
  target: entity/project/sameer-doda
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
  timestamp: '2026-01-22T08:31:01.042658Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.005718+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 6
name: Factor Form
id: project-factor-form
title: Factor Form
last_updated: 2025-12-08
related:
- '[[Projects/OTP.md]]'
---

# Factor Form

## Executive Summary

Factor Form is a ready-to-eat meal service brand. Current focus includes multi-cadence options, OTP capabilities, and Shopify migration.

## Current Initiatives

### Multi-Cadence Project
- **Status:** Live (launched Dec 2, 2025)
- **Feature:** Active users can choose 4/6/8 week cadences

### OTP (One-Time Purchase)
- **Status:** In progress, targeting W51 launch
- **Work Items:**
  - Cart implementation
  - Mutually exclusive checkouts
  - Dashboard updates
- **Related:** [[Projects/OTP.md]]

### Factor Form Shopify Migration
- **Status:** In progress
- **Complexity:** Lower than Good Chop (customer journey already defined)
- **Integrations:** Recharge, Elevar

## Key Stakeholders

- **PM:** Allison
- **Support:** Sameer Doda

## Technical Context
*Auto-synced from GitHub: 2025-12-16*

## Technical Context

The `hellofresh/web` repository serves as the central front-end monorepo for HelloTech, supporting multiple brands including HelloFresh and WhiteLabel.

*   **Tech Stack:** Built using **React** and **Next.js**, managed via **Yarn Workspaces**. The environment requires Node.js (LTS) and integrates with a private NPM registry.
*   **Architecture:** Utilizes a layered **Module System** for dependency structure and a flexible **Config System** for application settings. A custom **Toolbox CLI** streamlines local development and automation.
*   **Deployment & Infrastructure:** Deploys to **Vercel** (production and preview environments) via GitHub Actions. **HashiCorp Vault** is used for secure credential and secret management.
*   **Quality & Capabilities:**
    *   **Testing:** Comprehensive strategy using **Jest** for unit tests and **Cypress** for end-to-end testing.
    *   **Governance:** Enforces code ownership via `.claim.json` files and a **Critical Review** system for sensitive code paths.
    *   **AI Integration:** Includes `spec-machine` to standardize AI-assisted feature development.

## Changelog
- **2025-12-16:** Context update: **Factor Form UX:** Michael to conduct UX audit. Integration into Factor app planned if Shopify store fails.
- **2025-12-11:** Context update: **Factor Form Dev Team Evolution:** Developer concerns about team's future post-Shopify launch. Strategy: use Shopify as experiment tool, integrate su
- **2025-12-09:** Context update: Session end: Updated Influencer Marketplace and Factor Form statuses, refactored README.md, created PM-OS distribution package, and updated Jira API t
- **2025-12-08:** Mentioned in daily context (3x)

- **2025-12-08:** Stub created from daily context synthesis

## Gdocs Context

- [2026-01-02] Factor sub-brand supporting customers on holistic wellness and health goals (from: 2026 Yearly Plan - Consumer Mega-Allianc)

---
*Last updated: 2026-01-02 16:51*


- [2026-01-02] Factor sub-brand supporting customers on holistic wellness and health goals (from: 2026 Yearly Plan - Consumer Mega-Allianc)

- [2026-01-02] Brand supported by client TRE in New Ventures (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] Brand supported by client TRE (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] Platform experiencing CC errors in W49, main product system (from: Factor Form Weekly Tech - Business Sync)

- [2026-01-02] User journey optimization project, retesting cart functionality (from: Factor Form Weekly Tech - Business Sync)

- [2026-01-02] Brand using client TRE supported by L2 - New Ventures (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] Brand supported by client TRE in L2 - New Ventures rotation (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] Brand supported by client TRE in New Ventures (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] Brand supported by client TRE (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] Brand using client TRE supported by L2 - New Ventures (from: New Ventures Tribe - Weekly Standup Note)

- [2026-01-02] Platform experiencing CC errors and hosting OTP functionality (from: Factor Form Weekly Tech - Business Sync)

- [2026-01-02] User journey optimization project, retesting cart and checkout flows (from: Factor Form Weekly Tech - Business Sync)

- [2026-01-02] Main platform experiencing CC errors and hosting OTP feature (from: Factor Form Weekly Tech - Business Sync)

- [2026-01-02] User journey optimization project testing cart functionality and CVR impact (from: Factor Form Weekly Tech - Business Sync)

- [2026-01-02] Launch project for OTP that is being blocked by technical issues (from: OTP Topics - 2025/12/29 16:00 CET - Note)

- [2026-01-02] Launch project for OTP (from: OTP Topics - 2025/12/29 16:00 CET - Note)

- [2026-01-02] Shopify migration project, simpler than Good Chop (from: Sameer:Nikita 1:1 - 2025/12/05 15:29 CET)

- [2026-01-02] Dev team shouldn't be affected by Shopify experiment (from: Notes: Hamed <> Nikita 1:1)

- [2026-01-02] Shopify project, used as comparison point for Good Chop complexity (from: Sameer:Nikita 1:1 - 2025/12/05 15:29 CET)

- [2026-01-02] Has UX issues; strategy to integrate into Factor if Shopify store fails (from: Jenna:Nikita 1:1 - 2025/12/15 17:00 CET )

- [2026-01-02] Product with UX issues needing fixes; strategy to integrate into Factor if Shopify store fails (from: Jenna:Nikita 1:1 - 2025/12/15 17:00 CET )

- [2026-01-02] Development team and system discussed in context of Shopify experiment impact and general feedback (from: Notes: Hamed <> Nikita 1:1)

- [2026-01-02] Existing templates that Goodchop design should not mirror (from: Ali:Nikita 1:1 - 2025/12/16 17:45 CET - )

- [2026-01-02] Shopify store developed by Allison, to be shared with Yuri as reference (from: Sameer:Nikita 1:1 - 2025/12/16 17:32 CET)

- [2026-01-02] Current project that provides opportunity to try new design approaches without the restrictions of other products (from: Hamed:Nikita 1:1 - 2025/12/18 17:25 CET )

- [2026-01-02] Project that provides opportunity to try new design approaches without the constraints of other products (from: Hamed:Nikita 1:1 - 2025/12/18 17:25 CET )

- [2026-01-02] One of three projects Tishia would be dedicated to if hired (from: Maria:Nikita 1:1 - 2025/12/09 15:17 CET )

- [2026-01-02] One of three projects Tishia would be dedicated to if hired (from: Maria:Nikita 1:1 - 2025/12/09 15:17 CET )

- [2026-01-02] Simon's initial onboarding focus before scope expansion (from: Eva:Nikita 1:1 - 2025/12/09 15:02 CET - )

- [2026-01-02] Previous project referenced as comparison for involvement level (from: Sameer:Nikita 1:1 - 2025/12/22 15:31 CET)

- [2026-01-02] Launching OTP in US, November 2025, targeting 15,690 net conversions for Factor Form (from: One Time Purchase - Analytical Data Brie)

- [2026-01-02] Launching OTP in US, November 2025, targeting 15,690 net conversions for Factor Form (from: One Time Purchase - Analytical Data Brie)

- [2026-01-02] Launching OTP in US, November 2025 (from: One Time Purchase - Analytical Data Brie)

- [2026-01-02] Launching OTP in US November 2025, targeting 15,690 net conversions for Factor Form (from: One Time Purchase - Analytical Data Brie)

- [2026-01-02] HelloFresh brand launching OTP in US, November 2025 (from: One Time Purchase - Analytical Data Brie)

- [2026-01-02] Supplement brand currently operating on subscription-only model, introducing OTP option (from: Factor Form | One Time Purchase)

- [2026-01-02] Target brand for unified funnel (from: PRD: Cancellation Funnel Unification)

- [2026-01-02] Referenced brand in messaging section (appears to be template content) (from: DRAFT - Good Chop - Shopify Storefront)

- [2026-01-02] Testing ground for e-commerce capabilities (from: DRAFT - Good Chop - Shopify Storefront)

- [2026-01-02] Reference project that cost $400k USD (from: Ian:Nikita 1:1 (2w) - 2025/12/19 17:01 C)

- [2026-01-02] Target brand for unified funnel (from: PRD: Cancellation Funnel Unification)

- [2026-01-02] New venture with dedicated squad, website at factor75.com/factorform (from: CMA Squad overview)

- [2026-01-02] New Ventures squad with Factor Penetration % KPI, managed by Hamed Karimian (PM) and Pantelis Chatzinikolis (EM) (from: CMA Squad overview)

- [2026-01-02] New Ventures squad focused on Factor75.com penetration (from: CMA Squad overview)

- [2026-01-02] New venture tracked by Factor Penetration % KPI, managed by Hamed Karimian and Pantelis Chatzinikolis (from: CMA Squad overview)

- [2026-01-02] New Ventures squad focused on Factor75.com penetration (from: CMA Squad overview)

- [2026-01-02] New Ventures squad tracking Factor Penetration % at factor75.com (from: CMA Squad overview)

- [2026-01-02] New venture brand at factor75.com with penetration KPI (from: CMA Squad overview)

- [2026-01-02] Sub-brand with OTP order history and discount communications work (from: The Pets Table - 2026 BP v1 (Internal))

- [2026-01-02] Squad with 2 open engineering roles (CS4 FE, CS6 Staff FE) in Toronto, experiencing hiring challenges (from: Open roles EPD New ventures - 2026)

- [2026-01-02] Squad with 2 open engineering roles (CS4 and CS6) in Toronto, facing recruitment challenges (from: Open roles EPD New ventures - 2026)

- [2026-01-02] Squad with 2 open engineering roles (CS4 FE, CS6 Staff FE) in Toronto, experiencing offer rejections (from: Open roles EPD New ventures - 2026)

- [2026-01-02] Squad with 2 open backfill roles in Toronto for frontend developers (CS4 and CS6) (from: Open roles EPD New ventures - 2026)

- [2026-01-02] Main product line with multiple flavors (chocolate, vanilla, greens, lemonlime, bloodorangeyuzu, passionfruitguava, variety, bulk) (from: Pricing OTP vs. SNS)

- [2026-01-02] Main product line with various flavor combinations and box quantities (1-4 boxes) (from: Pricing OTP vs. SNS)

- [2026-01-02] Product line being launched on new Shopify storefront, positioned as food-first wellness system (from: DRAFT [HelloTech Launch Announcement] - )

- [2026-01-02] Product line being launched on new Shopify storefront, positioned as food-first wellness system (from: DRAFT [HelloTech Launch Announcement] - )

- [2026-01-02] Brand driven to new heights, TAM expansion (from: Closing Email: 2026)

- [2026-01-02] New venture squad with roadmap (from: Consumer Mega-Alliance: Q1 2026 Planning)

- [2026-01-02] Product system requiring ratings, favoriting, and catalog integration (from: Proposal & Tech Breakdown for Launching )

## Slack Context

- [2026-01-02] System handling meal selection differently than TPT and GoC for reactivation flow (#squad-nv-good-chop)


- [2026-01-02] Working on Multi Box Discounts implementation, refactoring GoodChop's discount communication components (#squad-nv-good-chop)

- [2026-01-02] Planning introduction of delivery cadence to actives experience, learning from GoodChop approach (#squad-nv-good-chop)

- [2026-01-02] Team within New Ventures tribe, planning demos for OTP and Shopify launches (#tribe-new-ventures-leads-internal)

- [2026-01-02] Mentioned by Ed at all-hands as challenging subscription model (#tribe-new-ventures-product)

- [2026-01-02] Has data backlog spreadsheet, Q1 2026 roadmap, and OKR tracker being updated (#tribe-new-ventures-product)

## Github Context

- [2026-01-02] Multiple GTM tracking updates and OTP flow enhancements (GitHub commits)


- [2026-01-02] UI improvements including sticky CTAs and SnS discount integration (GitHub commits)

- [2026-01-02] Multiple updates for OTP copy, discount communication, and SKU calculation (GitHub commits)

- [2026-01-02] Multiple updates including OTP checkout pricing, VMSU family SKU, endless pause cleanup, and order summary fixes (GitHub commits)

- [2026-01-02] Major updates for OTP support including order summary, address forms, cart creation, and canonical URLs (GitHub commits)

- [2026-01-02] Major updates for OTP checkout implementation, feature gating, and invalid product type handling (GitHub commits)

- [2026-01-02] Major OTP implementation, two-step login, and legacy to Shopify migration (GitHub commits)

- [2026-01-02] OTP order summary logic implementation (GitHub commits)

- [2026-01-02] Enhanced with multi-cadence support, toolbox commands, and localization (GitHub commits)

- [2026-01-02] Major development area for OTP functionality and multi-cadence support (GitHub commits)

- [2026-01-02] OTP implementation, cart service migration, and multi-cadence account settings (GitHub commits)

- [2026-01-02] VMS spans fixed, multi-cadence Lokalise keys added (GitHub commits)

- [2026-01-02] Checkout page refactoring pattern being applied across multiple components (GitHub commits)

- [2026-01-02] Major feature receiving multiple updates for OTP, cadence, cart-service migration, and filtering (GitHub commits)

- [2026-01-02] Receiving bundles frequency selector functionality for OTP (GitHub commits)

- [2026-01-02] Undergoing price calculation migration across cart, checkout, and leads capture (GitHub commits)

- [2026-01-02] Part of cart-service migration effort (GitHub commits)

- [2026-01-02] Undergoing cart-service migration with multiple commits for OTP flow and calculate endpoint changes (GitHub commits)