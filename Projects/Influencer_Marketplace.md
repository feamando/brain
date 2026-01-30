---
$schema: brain://entity/project/v1
$id: entity/project/influencer-marketplace
$type: project
$version: 1
$created: '2026-01-22T08:31:00.995770Z'
$updated: '2026-01-30T10:22:46.185914'
$confidence: 0.43
$source: unknown
$status: Active - Phase 3 (Prototype & Validate)
$relationships:
- type: mentioned_in
  target: nikita
  confidence: 0.65
  source: body_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: otp
  confidence: 0.65
  source: body_extraction
  last_verified: '2026-01-30'
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
  timestamp: '2026-01-22T08:31:00.995770Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:57.445300+00:00'
  type: orphan_cleanup
  actor: system/orphan_cleaner
  changes:
  - field: $relationships
    operation: cleanup
    count: 1
name: Influencer Marketplace
id: project-influencer-marketplace
title: Influencer Marketplace
last_updated: 2025-12-08
related:
- '[[Projects/OTP.md]]'
- '[[Architecture/SCM.md]]'
---

# Project: Influencer Marketplace

> **Status:** Phase 3: Prototype & Validate (MVP Blueprint)
> **Last Updated:** 2025-12-08
> **Sprint:** Sprint 3 (Nov 24 – Dec 5, 2025)

## 1. Executive Summary
The **Influencer Marketplace** is a strategic initiative to transform HelloFresh from a traditional meal-kit provider into a "Spotify for food" fulfillment platform. The core concept enables food creators (influencers, chefs) to sell their recipes as shoppable, HelloFresh-fulfilled meal kits directly to their followers.

*   **Key Goal:** Bridge the "Inspiration-Execution Gap" where users save social content but rarely cook it.
*   **Target Launch:** Q1 2026 (Pilot in Canada).

## 2. Value Proposition

### For Creators (B2B)
*   **Monetization:** A new stream of "passive income" from existing assets (cookbooks, viral videos) without the need for constant new content creation.
*   **Legitimacy:** A physical product extension of their brand, backed by HelloFresh's operational reliability.
*   **Reach:** Access to HelloFresh's customer base and fulfillment network without handling logistics.

### For Consumers (B2C)
*   **Frictionless Execution:** Instantly shop viral or aspirational recipes seen on social media.
*   **Trust:** Confidence derived from the creator's relatability combined with HelloFresh's quality assurance and delivery reliability.

## 3. Strategy: The "Managed" MVP
The team has shifted from an initial "Open Marketplace" vision to a **Managed/Curated MVP** to de-risk the launch and protect the brand.

*   **MVP Scope:** HelloFresh will do the "heavy lifting" (creating kits from videos, setting up store pages) for a small, curated cohort of creators.
*   **Cohort Target:** 3-5 "Whale" influencers or Cookbook Authors with evergreen content.
*   **Technical Path:** Build internally using existing **"Christmas Box"** frontend code (store-like feel) and reuse the **"Cookbook" scraper tool** (from Project DAU) to automate recipe ingestion. **Decision:** Do NOT use Shopify (too complex/overwhelming).

## 4. Key Decisions & Critical Debates

### Pricing Model
*   **Conflict:**
    *   *Market-Led (Ian Brooks/Linnea Siersma):* Creator sets their own margin; HF takes a service/fulfillment fee. Aligns incentives (sell more = earn more).
    *   *Tiered Cost-Plus (Sameer Doda):* HF sets the base price; creator gets a standardized margin based on tiers. Offers stability but limits upside.
*   **Status:** Open. Needs final decision in Sprint 4.

### Vetting & Quality
*   **Conflict:** Creators expect HF to vet recipes to protect *their* brand. HF wants a scalable marketplace without manual test-kitchen bottlenecks.
*   **Potential Solution:** "Vetted by HelloFresh" as a premium service or badge that creators can pay for or earn.

### Recruitment Ownership
*   **Blocker:** There is currently no clear owner for B2B creator recruitment and contracting for the MVP.
*   **Mitigation:** Marketing (Cole Banning) can support, but requires senior direction (Ian Brooks) to commit resources.

## 5. Research Insights (Sprint 3 Review - Dec 4, 2025)

### Creator Feedback
*   **Monetization:** Mixed preference between flat-fee (low risk) and commission (high upside).
*   **Data:** Strong demand for analytics (traffic, sales, trending ingredients) to optimize content.
*   **Vetting:** High expectation of quality assurance from HF.

### Operational Constraints
*   **Ingredients:** Niche ingredients (e.g., pistachio paste for viral trends) pose fulfillment challenges. MVP may require influencers to design recipes *for* HF's existing assortment.

### Customer Interviews (Dec 2025)
Detailed feedback from 4 participants (Connie, Barinder, Shima, Ashley) on the marketplace concept.

**Key Themes:**
*   **Value Prop:** Solves **Menu Fatigue** and **Ingredient Waste** (buying full bottles for 1 tsp). Not seen as "special occasion" only—strong desire for daily meal rotation solutions.
*   **Pricing Sensitivity:**
    *   Expectation: Comparable to or slightly *lower* than standard HF meal kits.
    *   Willingness to Pay: Minor premium acceptable for creator collaboration, but significant hikes (>30%) are prohibitive.
    *   Model: Strong preference for **Transactional / One-Time Purchase** (no subscription obligation).
*   **Trust & Vetting:**
    *   **"Vetted by HelloFresh"** is a critical trust signal. Users want a visual indicator (e.g., Green Checkmark) distinguishing HF-tested recipes from unvetted ones.
    *   **Reviews:** Unfiltered ratings/reviews are essential for social validation ("hit or miss").
*   **Desired Features:**
    *   **"Digital Cookbook":** Save/organize recipes (Rolodex style, alphabetical).
    *   **Creator Filters:** "Mute/Block" creators (like Facebook ad preferences) and "Follow" favorites.
    *   **Smart Search:** Filter by *Cuisine/Diet* first, Creator second (users care about food > influencer fame).
    *   **Video Integration:** QR codes on recipe cards linking to original social videos.
    *   **Skill Level:** Tags for difficulty (Beginner/Intermediate) and ingredient swaps.

**Barriers to Adoption:**
*   **Complexity:** Videos make recipes look easier/faster than reality.
*   **Subscription Fatigue:** Fear of "skipping weeks" or accidental charges.
*   **Quality:** Risk of recipe failure if not professionally tested.

## 6. Roadmap & Next Steps

### Immediate (Dec 8 - 19, 2025)
*   **MVP Definition:** Finalize decisions on Pricing Model and Vetting workflow.
*   **Recruitment:** Assign dedicated owner to sign 3-5 pilot creators.
*   **Tech Specs:** Validate code reuse (Christmas Box + Cookbook Scraper).

### Q1 2026
*   **Handover:** Transition leadership from Strategy (Annette MvdE) to Execution Squad (Wanderley Teixeira/Sameer Doda).
*   **Launch:** Pilot launch in Canada (CA).

## 7. Key Stakeholders
*   **Strategy Driver:** Annette MvdE
*   **Research:** Katheryn Eckles
*   **MVP Squad Lead:** Sameer Doda
*   **Tech Execution:** Wanderley Teixeira (Incoming Squad Lead - Jan 2026)
*   **Operations Strategy:** Melanie Schwindt
*   **Key Approver:** Ian Brooks
*   **Marketing Support:** Cole Banning, Marina Kramer

## Changelog
- **2025-12-16:** Context update: ### Influencer Marketplace (Strategy Update)
- **2025-12-11:** Context update: **Influencer Marketplace Strategy:** Sprint 4 Week 1 - "Prototype & Validate: MVP Blueprint". Canada first launch. Handover Jan/Feb 2026 to Wanderley 
- **2025-12-09:** Context update: ### Influencer Marketplace (Strategy Update) - *Retained from previous context*
- **2025-12-08:** Context update: **Influencer Marketplace**:

## Gdocs Context

- [2026-01-02] MVP focused on one-time purchase boxes through influencer channels; Q2 launch target (from: Sameer:Nikita 1:1 - 2025/12/05 15:29 CET)

---
*Last updated: 2026-01-02 16:51*


- [2026-01-02] Needs MVP path forward, has varied stakeholder views, design progress with Shay (from: Sameer:Nikita 1:1 - 2025/12/05 15:29 CET)

- [2026-01-02] Mirror board with customer journeys and wireframes being developed (from: Sameer:Nikita 1:1 - 2025/12/09 17:27 CET)

- [2026-01-02] Upcoming presentation with Ed, involves customer journey and creator portals (from: Sameer:Nikita 1:1 - 2025/12/22 15:31 CET)

- [2026-01-02] Creator marketplace concept being researched for turning social media recipes into purchasable meal kits (from: IXI Results: Creator Marketplace Custome)

- [2026-01-02] Creator marketplace concept being researched for turning social media food inspiration into home cooking (from: IXI Results: Creator Marketplace Custome)

- [2026-01-02] Strategic vision for 'Shopify for Food' platform (from: Research Roadmap & Project Tracking (GCI)

- [2026-01-02] Strategic project to create 'Shopify for Food' platform (from: Research Roadmap & Project Tracking (GCI)

- [2026-01-02] Strategic initiative to create 'Shopify for Food' platform (from: Research Roadmap & Project Tracking (GCI)

- [2026-01-02] Strategic initiative to create 'Shopify for Food' platform (from: Research Roadmap & Project Tracking (GCI)

- [2026-01-02] Strategic initiative described as 'Shopify for Food' - in flight (from: Research Roadmap & Project Tracking (GCI)

- [2026-01-02] Strategic initiative to create 'Shopify for Food' platform for influencers (from: Research Roadmap & Project Tracking (GCI)

- [2026-01-02] Strategic initiative to create 'Shopify for Food' platform (from: Research Roadmap & Project Tracking (GCI)

- [2026-01-02] Strategic initiative to create 'Shopify for Food' platform (from: Research Roadmap & Project Tracking (GCI)

- [2026-01-02] Strategic initiative to create 'Shopify for Food' platform (from: Research Roadmap & Project Tracking (GCI)

- [2026-01-02] Strategic initiative to create 'Shopify for Food' platform (from: Research Roadmap & Project Tracking (GCI)

- [2026-01-02] Working title for the marketplace connecting influencers with meal kit fulfillment (from: Influencer Marketplace – Strategy)

- [2026-01-02] Strategy initiative to create shoppable meal kits from influencer recipes (from: Influencer Marketplace – Strategy)

- [2026-01-02] Strategy initiative to create curated recipe creator marketplace (from: Influencer Marketplace – Strategy)