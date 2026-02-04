# HelloTech Sprint Summary

**Synced:** 2026-02-04T12:55:23.918256
**Source:** [HelloTech Every Other Week Squad Sprint Report](https://docs.google.com/spreadsheets/d/1TFvUQFbFKG4k5Y819UqVpxIVN9ebXJFkiMXTvzcb8ak)
**Squads:** 98

---

# AdTech

## Ad Data Platform
**Tribe:** AdTech
**Mega-Alliance:** Growth
**Squad Lead:** EM: Eshwar Prasad Vidhyasankar
PM: Oluboni Agbaniyaka

### Squad KPI
Marketing Data Freshness

Secondary:
- MAC uptime
- Semantic Layer uptime
- P0 incidents

### KPI Movement
N/A

### Delivered (This Sprint)
N/A

### Planned (Next Sprint)
N/A

---

## Planning & Reporting
**Tribe:** AdTech
**Mega-Alliance:** Growth
**Squad Lead:** EM: Valentina Ical
PM: Oluboni Agbaniyaka

### Squad KPI
% Global adoption rate of marketing reporting and forecasting tools.

Secondary:
- % of manual spend automated
- GMR/SSA uptime (%)
- Reporting freshness

### KPI Movement
% Global adoption rate of marketing reporting and forecasting tools. N/A

### Delivered (This Sprint)
1. Globalize Clarisights/SSA tool: Validation and mapping of Meta s data entries in Clarisights is finalized & Meta & Google Ads accounts are set up.
2. Reduce data assets: 60% of KitKat active components are now available in GMR. 
3. Expend FreshCost to NA : All MEL spend distribution methodologies (4/4) have been fully implemented in FreshCost NA.
3. Others (2025 leftovers) : CCV/discounts updated in MEL

### Planned (Next Sprint)
1. Globalize Clarisights/SSA tool: Validation and mapping of Google Ads data entries in Clarisights will be completed.
2. Globalize Clarisights/SSA tool & automate spend reporting: Cost reporting for Google Ads and Meta will be automated via API connections in Clarisights.
3. Reduce data assets:  Findings from the investigation into consolidating former MISO conversion dashboards (Empty Conversions, Daily Scorecard, Intraday) into a single data asset/dashboard will be shared.
4. Reduce data assets: 90% of KitKat active components are now available in GMR. (MaxCAC in next sprint)

### Key Learnings
Learning: Assign a primary and backup owner for larger tasks. Define responsibilities between main and backup assignees 

Time-box stakeholders feedback cycle

---

## Tracking & Targeting
**Tribe:** AdTech
**Mega-Alliance:** Growth
**Squad Lead:** EM: Jason Studstill
PM: Varsha Lalwani

### Squad KPI
Settled model accuracy

Secondary:
- Conversion pixel coverage
- Weighted match rates (EQM)

### KPI Movement
N/A

### Delivered (This Sprint)
N/A

### Planned (Next Sprint)
N/A

---

## Measurement
**Tribe:** AdTech
**Mega-Alliance:** Growth
**Squad Lead:** EM: Michael Mayer
PM: Dinesh Dacharaju

### Squad KPI
% of media spend covered by incrementality (weighted by model accuracy)

Secondary:
- % of media spend lift tested
- Time to launch a lift test

### KPI Movement
N/A

### Delivered (This Sprint)
N/A

### Planned (Next Sprint)
N/A

---

## Search Optimization
**Tribe:** AdTech
**Mega-Alliance:** Growth
**Squad Lead:** EM: Michael Mayer
PM: Şevki Argalioğlu

### Squad KPI
% Paid Search CAC deviation (guardrailed by BP planned volume)

Secondary:
- Autopilot uptime (%)
- SEA spend covered (%)

### KPI Movement
No movement due to autopilot was off during the previous sprint

### Delivered (This Sprint)
1. Prototype for the campaign level bidding has been released for testing in the next sprint
If the test result proves success, the default bidding layer for NB markets will be set to campaign level. This unlocks scaling AGE for 10 markets.

2. Laid out the foundation of monitoring and alerting system
This allows to start implementing the monitoring aspects which influences the autopilot uptime (%)

### Planned (Next Sprint)
1. Run the campaign level bidding test in at least one market (DE / GB)
2. Start tracking the CAC achievement through monitoring & alerting and disengage trigger for the autopilot
3. RFC for Global config that enables configuring activation of AGE for the new markets

### Key Learnings
When Google Ads updates a dimension, it creates a new record & persist the old one. This affects the one to one relationship in the pipeline & corrupt the data (e.g., AGE targets wrong campaign). The solution is streamlining the metadata workflow that includes a validation of the required dimensions.

The failing google ads resources underscored the critical need for environment parity and robust unit testing, as dependency mismatches between local dev and Databricks runtimes caused the outage. While a multi-version compatible test structure was implemented as an immediate fix, the long-term solution requires migrating production pipelines out of notebooks to ensure consistent reliability and testability.

Migration of artifacts involves Spark usage and there are several critical schema changes in artifacts. These changes break the reading and writing process, so the latest schema has to be enforced. The solution is pipeline versioning which allows to read and migrate between different folder structures without schema errors.

---

## Social Optimization
**Tribe:** AdTech
**Mega-Alliance:** Growth
**Squad Lead:** EM: Alan Khalil
PM: Amanda Wong

### Squad KPI
IA Conversions at a target IA CAC (HF-US)

Secondary: Creative Throughput (Factor-EU)

### KPI Movement
N/A
HF-US Budget Optimization tool will be adopted post-peak in order to not disrupt peak operations 
Creative Throughput has depdencency on Paid Social Creative Governance Framework (in progress)

### Delivered (This Sprint)
1. Shipped the multi-agent framework for SousChef (replacing MCP); lending to greater app stability and accuracy in responses.

### Planned (Next Sprint)
1. Performance metrics and analysis output - provided with HF-US budget recommendations

---

# Communications

## Campaign Composition
**Tribe:** Communications
**Mega-Alliance:** Growth
**Squad Lead:** Aamish Baluch, Emmanuel S.D

### Squad KPI
% of campaigns migrated to Iterable

### KPI Movement
0%/100%

### Delivered (This Sprint)
- CRM can now launch campaigns in Iterable with all foundational work done, including code snippets (merge tags) and Knak templates sync, soft login, and discount communication.

### Planned (Next Sprint)
- Launch RAF Cart Abandonment campaign for HF in Iterable.
- Complete and test the Forgot Password transactional campaign setup so it is ready to launch.

### Key Learnings
- Owning delivery from foundations and configuration through campaign creation and testing enabled the squad to ship launch-ready outcomes within a single sprint, avoiding handoffs and delays.
- Testing foundations through real, launch-ready campaigns surfaced gaps early and ensured solutions directly support business-critical use cases.
- Early, focused collaboration with the Consumer Core team (owner of CIPS) via a lightweight RFC and dev-to-dev sync enabled fast validation and allowed Comms to deliver end-to-end without handoff delays.
- AI support helped engineers work effectively in unfamiliar codebases, reducing ramp-up time and maintaining delivery speed across team boundaries.

**Demo:** [Bi-Weekly] Communication Demos  - 2026/01/30 16:10 CET – Recording

---

## Customer Profile Platform
**Tribe:** Communications
**Mega-Alliance:** Growth
**Squad Lead:** Gaganpreet Singh Duggal, Emmanuel S.D

### Squad KPI
% of campaigns migrated to Iterable

### KPI Movement
N/A

### Delivered (This Sprint)
N/A

### Planned (Next Sprint)
N/A

---

## Send Decisioning
**Tribe:** Communications
**Mega-Alliance:** Growth
**Squad Lead:** Francesco Virotta, Patrick Muntzinger

### Squad KPI
Communications delivered to actions

### KPI Movement
N/A

### Delivered (This Sprint)
N/A

### Planned (Next Sprint)
N/A

---

## CRM Engine
**Tribe:** Communications
**Mega-Alliance:** Growth
**Squad Lead:** Yawar Rizvi, Patrick Muntzinger

### Squad KPI
% of campaigns migrated to Iterable

### KPI Movement
N/A

### Delivered (This Sprint)
N/A

### Planned (Next Sprint)
N/A

---

## Creative Tech
**Tribe:** Communications
**Mega-Alliance:** Growth
**Squad Lead:** Patrick Gunia, Emmanuel S.D

### Squad KPI
Time-to-market for campaign content generation

### KPI Movement
N/A

### Delivered (This Sprint)
N/A

### Planned (Next Sprint)
N/A

---

# Consumer Core

## Monolith
**Tribe:** Consumer Core
**Mega-Alliance:** Consumer

### Squad KPI
No of critical user journies dependant on the monoliths (API-v2/Intfood)

### KPI Movement
Target: 7/7
Actual: 0/7
Compared to last month: no movement. 3 additional journeys added into scope of Q1, however Q4 user journeys still not completely rolled out in all entities
Link to detailed progress report

### Delivered (This Sprint)
- Rolled out Recurring order processing outside the monoliths for first entity - HF LU 
- Rolled out Deprecation of Initial Order Creation (part of the Checkout journey) in two additional entities - HF BE and NL

### Planned (Next Sprint)
- Rollout Checkout user journey without monoliths in HF Nordics (DK, NO)
             - Deprecate initial order creation (part of the checkout journey) in all remaining entities
- Rollout Recurring order processing without monoliths in HF (BE, NL)
- Rollout one-off user journey without monoliths in HF LU

**Demo:** Consumer Core Tribe - Demo [L4-A-Situation room] - 2026/01/30 13:55 CET - Recording

---

# Consumer Foundation

## Client Platform
**Tribe:** Consumer Foundation
**Mega-Alliance:** Consumer
**Squad Lead:** EM: Wellington Lima Freire
PM: Priscila Koeck Machado

### Squad KPI
The Platform Unification Ratio (PUR) is a metric that tracks progress toward completing the migration to a fully React Native codebase. It is a ratio calculated by dividing the number of React Native Pull Requests (PRs) by the total number of mobile PRs (Android + iOS + RN).

### KPI Movement
Target by end of Q1: 80%
Target by end of Q2: 95%
Actual: 68.87%
Compared to Last Month: +15.2 pp (from 53.71% to 68.87%)

We saw a big increase due to the use of AI and expect this number to keep increasing until the end of Q2.
Link for report containing auxiliar metrics

### Delivered (This Sprint)
Around. 30% of our team's capacity was spent in managing the mobile releases due to lack of e2e automation:

1. Ensured the mobile releases for our core brands were successful, including auditing changes that were introduced after the release's cutoff.
2. Investigated and identified possible causes for the apps submission rejection in ChefsPlate/GreenChef/EveryPlate.
3. Identified and corrected the skipped releases on Youfoodz.

Beyond that, we made significant progress in migrating the Cash Credit Balance History and Account Details screens to RN. However, we didn't get to a production-ready state with them.

More info about this sprint can be found here.

### Planned (Next Sprint)
1. Make the mobile releases hands-free again: finish the planned improvements, create and share a runbook with the teams about how  to handle hotfixes, and udpated documentation for the e2e process.

2. Cash Credits Balance History screen migrated to RN is enabled in production

3. Profile Tab + Account Details/Personal Info migrated to RN is enabled in production

(Pending: decision on whether we will prioritise RAF and what we plan to accomplish)

### Key Learnings
1. GenAI with spec-machine is very promising. We will adopt it in our SDLC to bring consistency to how we use AI for development, and increase the team's productivity (refer to the last segment of the linked demo to see the achieved results).

2. We have a significant "Bus/Truck Factor" in the mobile releases process: Although we were already prioritizing and working to fix and improve the process, the absence of one team member in this sprint showed us how much the knowledge is siloed. We will double down on our effort in the next sprint to complete the changes required to make the mobile releases hands-free again, and also improve our documentation to support with offloading parts of the process from our team.

**Demo:** The recording was not processed an IT ticket was created for investigation.

---

## Consumer Acceleration
**Tribe:** Consumer Foundation
**Mega-Alliance:** Consumer
**Squad Lead:** EM: Kutlu Kartal
PM: Meggie Bouchard

### Squad KPI
Definition of Done First-Pass Success Rate

### KPI Movement
KPI Still in Development

### Delivered (This Sprint)
1. [Lokalisation] Enabled React Native Over-the-Air (OTA) updates (as part of v26.06). This allows instant copy updates without full app store releases. We have initiated a safe 5% rollout to validate localization stability starting by week 6 release.
2. [Accessibility] Deployed the Accessibility PR Bot for Web to automate compliance. To ensure smooth adoption, we established a 2-week grace period before the bot begins strictly blocking non-compliant code.

### Planned (Next Sprint)
1. Release: Launch Chefsplate UI2 for all mobile users (iOS and Android).
2. [Lokalisation] Prototype a new Localization architecture to cut engineering overhead by ~70% (reducing steps from 10 to 3 with minimum human activity).
3.[Accessibility] Address 113 Web Accessibility (A11Y) violations in Menu and Storefront areas to align with pending regulatory reviews (NL Authorities).

### Key Learnings
1.[Localisation] We encountered a 1-week delay in the RN OTA rollout. While the feature passed initial checks, E2E testing on real devices revealed complex issues that were difficult to trace within large blocks of AI-generated code (spec-machine). To maintain development speed while ensuring maintainability, we are adjusting our protocols. Future AI-generated implementations will be restricted to smaller, modular Pull Requests (PRs) to allow for more granular human review and faster debugging.

**Demo:** The recording was not processed an IT ticket was created for investigation.

---

# Conversions

## Organic Growth
**Tribe:** Conversions
**Mega-Alliance:** Growth
**Squad Lead:** EM: Sushma Sharma
PM: Srishti Shah

### Squad KPI
Impressions or Clicks

### KPI Movement
n/a

### Delivered (This Sprint)
1. Improving URLs for Multilingual Markets – Launched in CA
 2.  Recipe Collection Pages – Routing, components, and payload integration; 25% complete
 3.  AI Review Summary for English-Speaking Markets – UX review completed and copy improved based on feedback
 4.   Display 10 User Reviews on the US Recipe Page – Ready to deploy

### Planned (Next Sprint)
1. Launch Review Summary – Available in English-speaking markets
2. Recipe Collection Page – Migrate collections and tags from Contentful to Food Content Hub and implement the new UI
3. Real-Time Chef Mapping on Recipe Detail Page in US – Integrate Matilda into the Sync service for live updates
4. Display 10 User Reviews on US Recipe Pages – Launch and go live

### Key Learnings
Removing duplicate recipe pages across Phase 2 markets (US, GB, DE, CA, NZ) using 301 redirects and canonical/noindex consolidation can meaningfully improve organic performance. By comparing pre- and post-deduplication results and benchmarking against last year’s seasonal trends and control pages, we learned that cleaning up duplicate content drives measurable gains in traffic and efficiency. Careful testing against non-recipe pages helps confirm that the improvements are real and not seasonal.

**Demo:** Jan 23, 2026 - Organic Growth Bi-weekly Demo & Sprint Review

---

## Conversion Platform
**Tribe:** Conversions
**Mega-Alliance:** Growth
**Squad Lead:** EM: Gabriel Zanin
PM: Harneet Singh

### Squad KPI
% of legacy Quiz logic replicated in the new modular architecture

### KPI Movement
1. Two functionalities already moved : Step order and Goals question. Exact % to be calculated

### Delivered (This Sprint)
1. Step order is CMS driven
2. Goal question is CMS driven
3. Moment of Assurannce is CMS driven

### Planned (Next Sprint)
1. Ship A/A test for  server side experiment with server allocation
2. Integrate funnel-selector in HelloFresh US
3. Launch value prop funnels in HelloFresh US

### Key Learnings
1. Experiment predictions on server side cause SRM issue on funnel-selector experiment, we decided to move to real exposure on the server. Will launch A/A test on week 6

---

## Reactivation
**Tribe:** Conversions
**Mega-Alliance:** Growth
**Squad Lead:** EM: Steve Costa
PM: Shay Ben Yacov

### Squad KPI
Incremental Gross Conversions (Formers)

### KPI Movement
n/a

### Delivered (This Sprint)
1. Unification (gradual) rollout
2. App Redesigned Homepage - 30%
3. Peak - Final changes

### Planned (Next Sprint)
N/A

### Key Learnings
Onsite UX is missing on Factor INTL and UX in general is inconsistent across multiple markets and brands.
Unification rollout will enable us to unify the experience and test the new Onsite UX we launched in Hellofresh across different flows.

---

## Onboarding
**Tribe:** Conversions
**Mega-Alliance:** Growth
**Squad Lead:** EM: Ashwin Samtani
PM: Ana Sollitto

### Squad KPI
Incremental Settled Customers

### KPI Movement
n/a

### Delivered (This Sprint)
1. Updated HF INTL Welcome flow to reintroduce Welcome page
2. Built Redesigned Welcome page features usable for both HF and Factor
3. Completed ENG spike on App Deeplinking flow for new customers

### Planned (Next Sprint)
1. Welcome page redirect experiment - HF Global (had to add Welcome page back in INTL before we could go live)
2. Continue shared feature building for Welcome page redesign - experiment ETA end of Feb
3. Launch updated HF App login UI to align with new visual design across site (e.g. visually rich HF funnel)
4. 40% of Eng resources on loan to other teams - Snowplow Migration Events + Actives

### Key Learnings
Welcome page was accidentally removed from HF INTL Onboarding flow in June 2025, which was not discovered until new squad took over in January. It is important to regularly QA full experience (checkout --> onboarding steps) for all markets, our new tool Spur should help with this.

---

## Activations RTE
**Tribe:** Conversions
**Mega-Alliance:** Growth
**Squad Lead:** EM: Ashwin Samtani
PM: Tommaso Cremonini

### Squad KPI
Incremental Gross Conversions (RTE)

### KPI Movement
n/a

### Delivered (This Sprint)
1. FJ redesigned flow test - 40%
2. P500 extension to HF US desktop - 30%
3. KTLO - 25%
4. HF Register page unification completion - 5%

### Planned (Next Sprint)
1. Go live of two experiments: (i) new redesigned FJ mobile Quiz expriment, (ii) P500 extension to HF US desktop
2. Kick off the work on the new dynamic FJ Quiz controlled by ML model
3. DIY for meal selection in activation funnel

### Key Learnings
The funnel is a highly stateful, experiment-heavy system where small UI or logic changes ripple across validation, tracking, pricing, and compliance. Changes like the Factor redesign and P500 desktop initiatives need to be handled patiently and deliberately to avoid cross-brand bleed or negative impacts in this highly sensitive TRE.

**Demo:** New redesign FJ funnel
P500 on desktop

---

## Reachable Audience
**Tribe:** Conversions
**Mega-Alliance:** Growth
**Squad Lead:** EM: Gabriel Zanin
PM: Ioanna Politi

### Squad KPI
% leads captured per session

### KPI Movement
N/A

### Delivered (This Sprint)
1. Wunderkind tactical fixes (drop in performance solved)
2. Fix for missing campaign customisation due to regional pricing changes  
3. Mapped all wunderkind customisation capabilities
4. Added missing catch-all rule + Rolled out Micro-tags v2 in IT + Rollout Web Performance Dashboard

### Planned (Next Sprint)
1. Spike: Wunderkind vs Internal solution 
2. Implement automated QA tests in Spur for Wunderkind flows 
3. Rollout of Micro Tags 2.0 in rest of INTL markets 
4. Clean up micro tags v1 and measure web performance impact
5. Continue the end-to-end user flow mapping

### Key Learnings
1. Lack of transparency and clarity on how Wunderkind campaigns are triggered. We have asked Wunderkindfor detailed information on the triggers and url params needed to properly QA the end-to-end experience 
2. We discovered that Campaign Customisation was disabled in September 2025 when changes to support regional pricing were merged on landing pages. Team implemented a fix

**Demo:** Conversions Tribe AHM Bi-Weekly Review - Jan29

---

## Activations Mealkits
**Tribe:** Conversions
**Mega-Alliance:** Growth
**Squad Lead:** EM: Vitaliy Shvarz
PM: Kate Zimina

### Squad KPI
Incremental Gross Conversions (Mealkits)

### KPI Movement
n/a

### Delivered (This Sprint)
1. Progressed on First Intelligent Funnel Flows - Product values customized - 55%
2. Completed AddressId migration to LEGO - 15% 
3. Merged initial version of 1-line address on prod - 15%
4. Completed Playwright MCP - 15%

### Planned (Next Sprint)
1. Intelligent Funnels: Launch intelligent funnel custom flows: product values
2. Intelligent Funnels: Prepare ML model to be ready to incorporate custom flows: household-adapted flows
3. Start work on Quiz in HF INT & WL updated to UX/UI of P500
4. Launch one-line address A/B test
5. Start work on single page checkout

### Key Learnings
1. Intelligent funnels model - Understanding how the model works right now, current limitations and future possible capacinilities and adapted the custom flows development prioritisation accordingly
2. Cart service cross-cluster communication - Since cart service is deployed on FTCP, fetching data from services on the legacy cluster requires additional configuration

---

# Customer Engagement

## Inspire
**Tribe:** Customer Engagement
**Mega-Alliance:** Consumer
**Squad Lead:** EM: Edu Morôni
PM: Lisa Trueblood

### Squad KPI
Users that have successfully saved at least 3 recipes to their Cookbook

### KPI Movement
Target: 1M (Q1)
Actual: 6.7K
Compared to Last Month: +5.2k (from 1.5k to 6.7k)

### Delivered (This Sprint)
1. Launched a video-based awareness and activation flow that includes a full-screen takeover on app open and an onboarding video that plays when a user visits the Cookbook for the first time
2. Redesigned the empty version of the Cookbook screen to prompt users to save their first recipe and added a link to a picture-in-picture tutorial that runs in social media apps and teaches them how to save a recipe

### Planned (Next Sprint)
1. Allow app users to share the Cookbook feature and/or saved recipes, creating a new viral growth loop
2. Improve the experience of saving recipes to the Cookbook by providing clearer error communication during the import process for external recipes and allowing users to save HelloFresh recipes to their Cookbook from any entry point in the app, as-is

### Key Learnings
1. In UXR, we continue seeing signals that users connect with the problem of saving recipes across platforms. For example, “I need this so badly because I have so many recipes saved under every single social media.” (src)
2. However, very few app users are saving recipes to their Cookbook (dashboard). Total daily imports are decreasing, and the number of users who saved 3+ recipes is still below 10k. This is why we focused on awareness and onboarding the past 2 weeks. Starting from the next sprint, we will also swarm both squads in the tribe on driving Cookbook adoption.
3. We see an upward trend in the percentage of external recipes saved relative to HelloFresh recipes, but HelloFresh recipes still account for the vast majority (c.90%)

**Demo:** Engagement Tribe-Level Demo - 2026/01/30 10:52 CET - Recording

---

## Act
**Tribe:** Customer Engagement
**Mega-Alliance:** Consumer
**Squad Lead:** EM: Wladimir Gaus
PM: Remy Aldasoro

### Squad KPI
Users that have successfully saved at least 3 recipes to their Cookbook

(swarming with Inspire squad on a Q1 MBL item)

### KPI Movement
Target: 1M (Q1)
Actual: 6.7K
Compared to Last Month: +5.2k (from 1.5k to 6.7k)

### Delivered (This Sprint)
1. Aisle-Based Grocery View: Organizes recipe ingredients by store aisle to create a more intuitive, streamlined "grocery" shopping experience.
2. Dynamic Serving Adjustments: Enables users to scale serving sizes before adding ingredients to their grocery list, ensuring accurate quantities.

### Planned (Next Sprint)
1. [swarming with Inspire squad] Allow app users to share the Cookbook feature and/or saved recipes, creating a new viral growth loop
2. Finish work in progress to launch an A/B test of the Post-Cutoff Meal Planner, which allows subscribers to schedule which days they're going to cook each of their meal kits on during the upcoming week.

### Key Learnings
- Strong Initial Interest vs. Low Utility: While the feature successfully attracted 37K users (top-of-funnel), only 10% converted to active users (adding items), indicating a significant gap between "interest" and "functional value."
- The "View-Only" Barrier: A 90% drop-off from viewing to adding items suggests the current UI/UX feels more like a static reference page than an interactive tool.
- Low Feature "Ownership": With <1% manual additions, customers view this strictly as a "HelloFresh Ingredient Summary" rather than a personal shopping list. This limits the feature’s stickiness and daily relevance.
- Broken Feedback Loop: The 2.87% check-off rate is the primary concern. It indicates that even active users are not using the list during the "action" phase (shopping ), meaning the tool currently fails to provide its main utility.
- Content Drivers: Growth is driven by the Recipe Hub (66%) rather than the Cookbook, suggesting users are using the list to "shortlist" or "bookmark" future meals they desire.

**Demo:** Engagement Tribe-Level Demo - 2026/01/30 10:52 CET - Recording

---

# EXAMPLE: Shopping Journey

## EXAMPLE: Feedback
**Tribe:** EXAMPLE: Shopping Journey
**Mega-Alliance:** Consumer

### Squad KPI
EXAMPLE: Recipe Response Rate

### KPI Movement
EXAMPLE: 
Target: 16.0%
Actual: 17.5%
Compared to Last Month: + 2.5% (from 15.0% to 17.5%)

### Delivered (This Sprint)
EXAMPLE: 
1. Launched v2 of the in-app micro-survey for recipe rating/feedback on the post-cook screen. 
2. Integrated feedback data stream with the Core Product database.

### Planned (Next Sprint)
EXAMPLE: 
1. Implement personalized push notifications to prompt feedback 30 minutes after the estimated meal completion time. 
2. Begin A/B testing different visual styles for the feedback UI.

### Key Learnings
1. The new micro-survey placement significantly boosted response rate (17.5% vs. 15.0% baseline), validating the shift away from email prompts.

2. The new data stream integration confirmed that 70% of responses occur within 15 minutes of app session re-entry, suggesting we can optimize push notification timing.

**Demo:** Link to the Squad or Tribe demo recording for this sprint. Multiple squads may reference the same demo.

---

# Global People Technology

## People Tech Operations
**Tribe:** Global People Technology
**Mega-Alliance:** Ops

### Squad KPI
SLA Adherence & Reduction of KTLO Workload

### KPI Movement
People Tech Operations: No material KPI movement versus last sprint; SLA, TTR, TFR, and NPS remain broadly stable

### Delivered (This Sprint)
People Tech Operations BAU delivery continued; steady-state case handling and monitoring; no scope or operating-model change introduced this sprint

### Planned (Next Sprint)
Maintain BAU delivery model; continue SLA and NPS monitoring, risk-based prioritisation, and control execution

### Key Learnings
BAU performance is most sensitive to data quality and stakeholder responsiveness rather than system throughput

---

## People Tech Development - HCM
**Tribe:** Global People Technology
**Mega-Alliance:** Ops

### Squad KPI
% of Global Worker Data Quality & Completeness in Workday

### KPI Movement
HelloConnect (Philippines) rollout: Schedule RAG remains Amber; readiness improved versus last sprint following resolution of critical integration blocker

### Delivered (This Sprint)
HelloConnect (Philippines) Workday rollout progressed through late unit testing into E2E testing; 98% unit testing completed; E2E testing launched 26 Jan; critical Hire API issue resolved; ZKTeco clocks delivered; org structure and data strategy aligned; change management campaign launched

### Planned (Next Sprint)
Formal unit test sign-off; complete E2E testing cycle 1; commence physical clock testing and training; progress final data gathering toward go-live

### Key Learnings
SME capacity and late-stage scope changes are now the dominant risks, not configuration completeness

---

## People Tech Development - PATTB
**Tribe:** Global People Technology
**Mega-Alliance:** Ops

### Squad KPI
# of Distribution Centres using Workday Absence & Time Tracking

### KPI Movement
Fresh Field programme: Readiness improved versus last sprint, but overall delivery risk increased due to late-breaking requirements

### Delivered (This Sprint)
Fresh Field programme advanced across testing and operational readiness; ORT mobilisation initiated with onsite sessions confirmed; clock testing progressed with logistics unblocked; 16/17 SSC SOPs completed; Wave 2 kick-off initiated

### Planned (Next Sprint)
Execute ORT and DACH onsite testing; close open configuration items; stabilise readiness for UK and DACH go-lives; continue Wave 2 discovery

### Key Learnings
Operational readiness, not build progress, is now the critical path; late scope additions materially compress stabilisation time

---

## People Tech Development - Integrations
**Tribe:** Global People Technology
**Mega-Alliance:** Ops

### Squad KPI
# of Hours of Manual Work Eliminated

### KPI Movement
Integrations (cross-programme): Integration readiness improved versus last sprint, but end-to-end sign-off remains constrained

### Delivered (This Sprint)
Integration delivery across HelloConnect and Fresh Field progressed; Workday–Sprout Hire integration stabilised; Scan2Job testing advanced; 3010 SFTP connection established; Tableau development completed

### Planned (Next Sprint)
Close remaining integration test cycles; resolve data ownership and reporting decisions; support ORT and E2E testing with sufficient test data

### Key Learnings
Integration risk is now driven by data ownership decisions and test data sufficiency rather than technical defects

---

# Ingredient to Product

## Strategic Procurement
**Tribe:** Ingredient to Product
**Mega-Alliance:** Ops
**Squad Lead:** PO : Imran Uddin
EM : Maykol Saavedra

### Squad KPI
Menu Risk (% of at-fault recipes flagged and resolved before T-3)

### KPI Movement
KPI definition and data completeness needs to be updated [part of sprint 3 goal]

### Delivered (This Sprint)
[P500 Substitutions Pre-Approved Ingridient Selection Flow]
1. Prepare AI SKU Substitution options for HF & EP - WK06/07/08/09 to reduce the friction for recipe developers to manually click on "generate AI recommendation" for each recipe.
2. Update Manual Substitution Edit Reasons to ensure we capture the reasons accurately for manually replacing an AI sub suggestion. In the long term this will help us improve the AI suggested
3. Removed all AI generated and/or manual subs after the ship without/pack without selection. The helps in ensuring the pack without/ ship without options serve as the ultimate rider in the sub decision log and all options generated thereof hold no importance for downstream services/users.

[KTLO & Continuous Improvements]
1. Improvements to the search and filter in the sku catalog. This increases the ease of navigation and filtering out the relevant jobs to be done for a recipe developer.

### Planned (Next Sprint)
[P500 Substitutions Pre-Approved Ingridient Selection Flow]
1. Enable "copy from" functionality for pre-approved SKU Subs between base, variants and versions of a recipe.
2. Complete one time migration of pre-approved SKU subs between identifed base, variants and versions of recipes.
3. Improved the subs UX by grouping base, variants and versions of a recipe in the UI.

[KTLO & Continuous Improvements]
1. Authenticate (3P FSQA tool that collects & store information) <> internal Supplier SKU integration improvements
2. Menu Risk Ratio (squad KPI) calculation improvements

---

## Assortment Development
**Tribe:** Ingredient to Product
**Mega-Alliance:** Ops
**Squad Lead:** PO: Manizeh Dossa
EM: Nikhil Khurana

### Squad KPI
% of mealkit products consumed in the Global Recipe Pool with 100% standardized recipe attributes

### KPI Movement
N/A

### Delivered (This Sprint)
P500 Hypercare
1. Solution to identify the discrepency of Variant grouping and Customised Ingredient in Live Menus. 
2. Solution to fix the discrepency of Variant grouping and Customised Ingredient in Live Menus. 
3. Identified the root cause of discrepency between ingredients sku between CPS and PKG. Executed a systematic fix of feature flag based solution to remove bulk sku sub option from the Tool. 
[KTLO & Continuous Improvements]
1. Fixed PDF exports from CPS.
2. CPS relationship display bugs (“undefined” base recipes).
3. Mapping global cuisines to multiple markets.
Discovery for Next Sprint:
1. Set up for a new Asynchronous File Processing Module epic.
2. Refinement of Pork Compliance automation solution for P500 Support

### Planned (Next Sprint)
[CPS]
1. Implement the Asynchronous file processing module
[P500]
1. Finalise the technical discovery of Pork Compliance recipes content automation and kickoff the implementation
[Product Catalogue]
1. Full nutrition breakdown automatically fills in nutrition information
[KTLO & Continuous Improvements]
1. Continuous support in our public channel and provide the resolutions to the stakeholders.

---

# Insights

## Upstream Operations
Etienne Leconte
**Tribe:** Insights
**Mega-Alliance:** Ops
**Squad Lead:** Virgil Brown

### Squad KPI
Complete 6 insights projects guiding operational improvements

### KPI Movement
Upstream Q1 Insights completed: 1
Est. Impact TBD

### Delivered (This Sprint)
1. Kicked off inventory demand simulation project
2. Kicked off 3PW Total Cost of Ownership Project
3. Finalized Recipie Recommendation Engine Analysis

### Planned (Next Sprint)
1. Conclude Vendor Forecast Analysis
2. Kick off CC Operations Cost Simulator
3. Finalize Ingredient Delta Analysis

### Key Learnings
-Confirmed that Harp is best well-positioned for tenured customers, particularly those with a history of sixteen or more boxes. 
-Penguin remains the most effective engine for driving menu engagement through the first fifteen boxes, an analysis of secondary "Food Ordered" metrics suggests a significant performance opportunity

**Demo:** -3PW Explorator Analysis
-Menu Recommendation Engine Analysis

---

## Conventional Operations
Corné Heijnen
**Tribe:** Insights
**Mega-Alliance:** Ops
**Squad Lead:** Virgil Brown

### Squad KPI
Complete 6 insights projects guiding operational improvements

### KPI Movement
Conventional Q1 Insights completed: 1
Est. Impact €187K

### Delivered (This Sprint)
1. Kicked off Formula Fresh analysis
2. Completed Monopallets analysis

### Planned (Next Sprint)
1. Kick off Ingredient Buffer Analysis
2. Kick off menu expansion impact anlaysis

### Key Learnings
-Changes in the middle mile planning setup and production batches have been implemented based on our findings, having led to an improved MPR and a strong negotiation position when it comes to contract renewal

**Demo:** -Monopallets Analysis

---

## Automated Operations
Leonie Gablier
**Tribe:** Insights
**Mega-Alliance:** Ops
**Squad Lead:** Virgil Brown

### Squad KPI
Complete 6 insights projects guiding operational improvements

### KPI Movement
Automated Q1 Insights completed: 1
Est. Impact TBD

### Delivered (This Sprint)
1. Completed Cool Chain Analysis
2. Conducted maintenance for legacy reports

### Planned (Next Sprint)
1. Finalize Safety Stock Analysis
2. Kick off Production Capacity Analysis - Barn
3. Kick off HFDN Drop Analysis

### Key Learnings
-Cool Chain analysis identified positive effect on cancellations due to packaging reasons (-0.11 p.p.) On the other hand, the negative impact on error rate appears more substantial, with the compensation per box rising 0.31 €/box (0.08€ due to last mile errors). Given these considerations, further expansion of CoolChain does not appear favorable.

**Demo:** -Cold Chain Analysis

---

# Inventory Management

## Finance Tech
**Tribe:** Inventory Management
**Mega-Alliance:** Ops
**Squad Lead:** EM: Roberto Gritti
PO: Mark Holohan

### Squad KPI
Global Cost Reporting Tool

### KPI Movement
Automate Cost Report generation

### Delivered (This Sprint)
1. Requirements gathering
2. Workshop with relevant stakeholders to bootstrap the project and set expectations and deadlines

### Planned (Next Sprint)
Continue Requirements gathering

### Key Learnings
Insights on how the report is currently build
New requirements from stakeholders

---

## WMS Integrations/ AIP
**Tribe:** Inventory Management
**Mega-Alliance:** Ops
**Squad Lead:** EM: Aleksandar Petrovski
PO: Piotr Jastrzębski Integrations

### Squad KPI
Global roll-out of the Advanced Inventory Platform (AIP) removing SaaS costs and make features like HA, monitoring, automated deployments and tests globally available

Consolidate into one global WMS replacing FCMS in automated sites

WMS2.0 integration with downstream systems

### KPI Movement
Deprecation of installation of HighJump in Oracle cloud in two DC's in Canada, migrated to AWS

### Delivered (This Sprint)
Successful roll out of AIP to 4 distribution centers in Canada:
- HelloFresh Edmonton
- Factor Laird DC
- HelloFresh Timberlea
- HelloFresh Summerlea

### Planned (Next Sprint)
Rollout in HelloFresh Abbotsford in Canada, preparation for the rollouts of AIP in US and AU/NZ.

### Key Learnings
Refinement of runbooks for futher deployments in CA and US created, onboarding of US Fulfilment Analysts onto the migration process

---

## WMS- Product & Engineering
**Tribe:** Inventory Management
**Mega-Alliance:** Ops
**Squad Lead:** Eng: Ashraf Ali
PO:  Piotr Jastrzębski FCMS 
 Edwin Chung WMS2.0  
Owen Cascante-Rovira WMS-NA

### Squad KPI
WMS SCOS Compliance, P500 expansion/ AZ Pilot, Factor_, Inventory Accuracy/Cost

### KPI Movement
SCOS: Factor_EU Inbound operations launched on WMS-NA product in Verden, Germany 
P500: Several software deliveries around integration and WMS Workflow

### Delivered (This Sprint)
WMS2.0
1.UAT completed for Jan 21 product release
2. Demo held for partial pallet replen
WMS-NA
1.RF Translations for words in architect.(2h)
2.Prevent Partial Pallet move with different UOM EA/CS.(35h)
3. Remove additional screen during the Kit Receipt RF Process(4h)
4.Factor EU Weight sampling from LBS to KG(35h)
5.Performance tuning on WO import process(15h)
6.Changes to CPT workflow to display item description during dropoff(6h)
7.RF and web profile updates for LDL scan to slot(5h)
8.Slotting replens based on Proc subs tool Import(60h)
9.Item status validation for factor scanned item(2h)
10.International date format - Factor EU(9h)
11.Enhancements(filters) autostore Inventory Summary page(1h)
12. System Translation from English to German(27h)
13.PIO Inventory Dashboard and Return pages(26h)
14.Fix Item slot description filter - Autostore replens page(1h)
15.Kit Misc LP having both MLK and R sku code(8.5h)
16.Create tran log linking autostore import(21.5h)
17.Import and Process RPD data(61h)
18.Display correct UOM on Kit Replen Page(cs vs PL)-25.5h
FCMS
1.Continued design feedback on FCMS-WMS2.0 integration requirements to DAI
2. Improved UX flow of manual loc stock audit
3. Decoupled trolley trip generation from replen generation in background process to increase the  efficiency of multishuttle trolley trips
4. Functionality to adjust # of cases in Pallet Replen before deletion
5. Cleardown: show a list of the pallets with an SKU that can be scanned
6. Cleardown: UX adjustment of manual pallet creation flow
7. Cleardown: prevent mix of a stock with different BBD on the same pallet
8. Cleardown: allow to  search by SKU name or code within picking stations cleardown flow
9. Allow Picking Station Cleardown when there is picking activity ongoing on onther station belonging to the same line

### Planned (Next Sprint)
WMS2.0
1.Auto-populate BBD for undated PHF skus(IT)
2.Pre-Populateed list of allergens(IT)
3.BBD vs MLOR validation at palletisation(Bjuv)
4.Add Print LP button on Add LP page(Bjuv)
5.Make weight QC optional for all categories(Bjuv)
6.ICS-Create new transaction type for faild skus during QC(Bjuv)
7.Add questions on logo and control code for Organic products(Bjuv)
8.Sort Alphabetically on empty crates page.
9.Rename 'Yes' to 'Confirm' buttons in inbound.
WMS-NA
1.Return from Manufacturing partial LP's to include PO# and lot code.
2.PIO Message integration-wms integration service
3.Item sub forklift wo integration
4.Slotting & Replen process change for PIO.
5.Prevent dropping non-pio tasks into PIO staging locations.
6.Job to delete cycle log.
7.WO Picking - tune pick path sequence.
8.Putaway allergen violation- prevent items with allergens placed in adjacent locations.
9.Increase allergen attribute.
10.PIO Message Integration.
11.Cart Building for PIO kits and cart putaway.
12.Add item no to Case replens RF
13. Fix replen process for Autostore.
FCMS
1.Internal testing kickoff for thawing workflow enhancements

### Key Learnings
Streamling deployments for sprints, need for a checklist for migrations to sync objects ,test migrations.

**Demo:** Partial Pallet Replen

---

# Labor Planning, Management, and Analytics

## Labor Management
**Tribe:** Labor Planning, Management, and Analytics
**Mega-Alliance:** Ops
**Squad Lead:** SL: Niharika Aggarwal
PM: Nikhil Ranka

### Squad KPI
Worked Minutes Per Box (Worked MPB)

### KPI Movement
Production MBP HF/GC [US]: 13.9% increase (14.1 -> 16.1)
Worked MPB [BARN]: 4.6% decrease (18.2 -> 17.4)
Worked MPB [WM]: 9.8% decrease (15.5 -> 14)

(We are working with Product Analytics to track Worked MPB for the US to accurately report KPI movement in all markets with our Labor Tracking toolkit)

### Delivered (This Sprint)
Reducing Labor Cost and Labor Minutes per Box (60%)
- Evaluated Dematic (Warehouse Picking System) integration readiness for Scan2Job in BARN DC to enable improvement in labor productivity - 20%
- Improved Attendance Forecasting Model reliability by resolving data quality issues to enable UAT for accurate labor shift staffing - 40%

Launch Factor Verden Facility (10%)
- Scoped out work required to rollout Scan2Job for Factor Verden launch to enable improvement in labor productivity and planning accuracy - 10%

KTLO - Security, Support & Maintenance (30%)
- Secured access to our S3 buckets to be compliant with HelloFresh Secuity guidelines
- Added alerts for operational excellence
- Reduced vulnerabilities in Github repos

### Planned (Next Sprint)
1. Enable Verden data on Scan2Job to support the Verden Launch
2. Successful UAT for improved Attendance Forecasting integration with Short Term Planning Toolkit [MK] 
3. Integrate Scan2Job with Dematic in BARN and enable UAT

### Key Learnings
We are getting slowed down on multiple fronts due to data unavailability from upstream teams. For eg:
1. INTL Opex team is still working on providing a full list of associate_id to Dematic RFID mapping (missing mapping for 19 RFIDs) - we've escalated it and the responsible team is prioritizing it.
2. US Asset Protection team hasn't been able to provide required data in the Lenel dataset for us to identify day labor to effectively track the ~10-20% day labor across Factor and Meal Kit sites - US Opex has escalated the issue but no progress has been made yet.
3. FreshField Project (3010 to Workday Migration) is yet to provide us with a complete data set of employees for a day and shift. We have escalated the issue but no progress so far.

**Demo:** Demo - Jan 29th '26

---

## Global Field HR Data Products
**Tribe:** Labor Planning, Management, and Analytics
**Mega-Alliance:** Ops
**Squad Lead:** PM - Benjamin Feder

### Squad KPI
# of standardized global field HR data products

### KPI Movement
Domo Deprecation --> $250K contract up for renewal in May 2026 (decided to discontinue) + eliminating tech debt blocking global scaling

# business processes still in Domo: 2

### Delivered (This Sprint)
1. Domo Deprecation: VER app ready for UAT and MAT is passing 40% of internal testing metrics - 73%
2. Data pipeline improvement initiative propsals - 10%
3. KTLO tool support - 10%
4. Post-Domo scoping with People + Tech leadership - 5%
5. New ways of working documentation in post-Domo world with partner teams  - 2%

### Planned (Next Sprint)
1. Complete VER UAT
2. Begin MAT UAT
3. Develop Squad meta backlog with People team leadership input
4. Align on ways of working with more respective partner and stakeholder teams
5. Begin Lenel data quality improvement

### Key Learnings
Need agile-style issues tracker for apps in development to ease coordination across teams

**Demo:** GOAT Bi Weekly: Punch Data Modernization

---

# Logistics

## Delivery Network
**Tribe:** Logistics
**Mega-Alliance:** Ops
**Squad Lead:** PM - Iria Maron Lopez
Interim SL - Abhishek Ash Boris Blinov

### Squad KPI
% of global business onboarded to DNET product portfolio (TADA,  Central Network Planner, Logistics Configurator)

### KPI Movement
TADA: In terms of boxes shipped globally, 35.77% of the business use TADA. In terms of markets, it's currently available in DACH, Nordics, Benelux, France, Australia, Ireland, for HelloFresh brand.
UK, CA, NZ TADA rollouts are planned for Q2 (which would bring the metric to 54%), although this needs to be revised due to DNET squad onboarding into CNP.

### Delivered (This Sprint)
1. Remaining high-priority issues for Zipmap-LC integration have been addressed. Last round of E2E testing and UAT is in progress. Go Live date: 9th Feb
2. BE changes for switching service label configuration to be managed at area level are done (required to address operational complexities and workarounds across multiple TADA markets).
3. Aligned with OR team on solution and plan to enable capping fast deliveries through TADA (required for DACH and the UK). Implementation is scheduled to start next sprint.
4. Address correction improvement for the US to flag cases where flat number is missing is in progress.
5. Testing of Statsig integration for active customer using Mobile is in progress (Android works as expected but issues have been reported for iOS)

### Planned (Next Sprint)
1. Go Live with Zipmap-LC integration in the US
2. Finish remaining FE change for area-level configuration of Service Labels
3. Start "Actual Uptake" Implementation (= capping of fast deliveries)
4. Continue CNP onboarding
5. Scope a solution to incorporate Delivery Exception Lists in TADA (required for CA rollout, they are used for emergencies)

### Key Learnings
Alignment meetings with OR team helped to redesign the "Fast deliveries capping" solution to better achieve the business requirements.

**Demo:** DACH Label Issue Post-Mortem


RFI - Final Mile Tooling final (1).docx

---

## Shipping and Tracking
**Tribe:** Logistics
**Mega-Alliance:** Ops
**Squad Lead:** PM- (Interim)Christopher DeStefano
SL - Boris Blinov Martina Dümcke

### Squad KPI
% of global business onboarded to Shipping and Tracking product portfolio (Lassy, Exceptions Tooling,

### KPI Movement
0% - development work continues on Lassy AUS and US deployment (Q1 Targets: AUS = +0.36% // US = +5.57%  Squad KPI)

### Delivered (This Sprint)
1) Released auto-generation feature for Lassy - DACH
2) Predictive Failure ML model result analysis completed - parity achieved with current exception tooling in U.S.
3) MAO Mapping for Lassy AUS integration. completed

### Planned (Next Sprint)
1) AUS Lassy pilot using EveryPlate brand
2) FedEx Canada direct carrier integration
3) U.S. ML failure prediction soft launch

### Key Learnings
- Additional validation needed between ODIN and Lassy  systems
- Lack of upstream CPT within the Central Network Planner config prevents closure of boxes in PCS

---

## Transportation Tech
**Tribe:** Logistics
**Mega-Alliance:** Ops
**Squad Lead:** PM - Allegra Friedman
SL - N/A

### Squad KPI
% of all global freight spend going through TMS

### KPI Movement
Vendor decision in Q1 for future onboarding.  CA Inbound to be completed in Sprint 4 for KPI progression

### Delivered (This Sprint)
1) CA IB TMS build - 45% - Began working through UAT scenarios with CA team. Continued to work through a few integration layer snags that came up. Onboarded most carriers into the E2Open production environment, and completed bulk of production environment build.
2) TMS Market Analysis - 45% - Scoped next demo-scenario requirements with vendors & pushed for client referrals. Received pricing and implementation info from one more vendor 
3) KTLO (TMS) - 10%

### Planned (Next Sprint)
CA IB TMS: TMI (integration layer) should be fully ready by end of this week at the latest. Production build to be complete next week and ready for 3PW/Carrier testing and training. Preparing for TO pilot launch on 2/16

TMS Market Analysis (Highlander): schedule final demo scenarios with vendor partners and shore up client referrals. Get pricing and implementation proposals from remaining vendor

### Key Learnings
CA IB TMS: Crossdock PO infrastructure/process will need special attention - scheduling a call with US IB team to understand their current process

TMS Market Analysis (Highlander): need to address specific integration capabilities across vendor solutions in further detail to ensure alignment with full tech stack

---

## Last Mile Tech
**Tribe:** Logistics
**Mega-Alliance:** Ops
**Squad Lead:** PM - Lauren Tersaga
SL - N/A

### Squad KPI
% of all global markets onboarded to Final Mile & Routing platform

### KPI Movement
n/a, RFI phase

### Delivered (This Sprint)
1. Distributed Highlander Final Mile Tooling RFI to vendors and began Q&A (20%)
2. TIS KTLO and data cleanup (20%)
3. Evaluated additional Final Mile Tooling vendors in response to RFI (10%)
4. Supported Amazon Key launch in US HFDN (10%)
5. Supported integration of US HFDN and Dropoff DSP (10%)
6. Solutioned TIS sideloading build for failures in response to winter storm (10%)
6. FarEye KTLO, enhancements, change requests (10%)
7. Revenue recognition logic refinement in partnership with Global Finance (10%)

### Planned (Next Sprint)
1. Begin structured Q&A cycles with vendors; consolidate questions and responses
2. Hold vendor clarification calls as required (routing + execution)
3. Build shared FAQ tracking for all vendors (internal + external)
4. Start preparing for evaluation rubric customization based on vendor responses
5. Continue TIS KTLO as needed

### Key Learnings
1. Early vendor outreach requires strict gating and consistent messaging to avoid unmanaged pre-screening conversations.
2. We need full visibility into vendor communications from IP to properly manage Q&A and timelines.
3. Contributors and informed parties are highly engaged, so a centralized FAQ and communication protocol reduces noise and ensures fairness in the process.

---

# Loyalty & Virality

## Share
**Tribe:** Loyalty & Virality
**Mega-Alliance:** Consumer
**Squad Lead:** EM: Travis Provick
PM: Rachna Ravi

### Squad KPI
Referral Take Rate upon landing (% referral invites/referral page sessions)

### KPI Movement
Target: +5%  
Actual: -3.6% YoY

Compared to same week last year:
- Invites 2025 W4: 177742 | Take rate: 7.48%
- Invites 2026 W4: 141785 | Take Rate: 7.21%

Change: 
- Invites:-20.23% YoY | Take Rate: -3.6% YoY

Note: A fix to session data reporting went live in W4, so the accuracy of that data for the week is uncertain. For this review we have included invite rate as an additional metric.  This should be resolved for future weeks.

### Delivered (This Sprint)
1. Added fallback logic to ensure customers are presented the correct referral offer when CDP is unavailable or slow.  Approximately 5% of users were presented with the wrong offer terms.
2. Allocated 41k additional freebie invites to Factor Canada customers to drive additional conversions
3. Referral page migration for Pets Table and Goodchop to reduce code complexity and improve speed to test. We have 2 more markets to migrate

### Planned (Next Sprint)
1. New welcome page referral entry point on multiple HF markets targeting new users after a moment of joy [link]
2. Bring parity to Sharing options on mobile web to improve seamless sharing / invites. Mobile web is our highest traffic platform for referrals, and does not have all options to allow users to share referrals through the messaging platform of their choice
3. Launch contest module in additional markets (GB, DE, FR) to incentivize users to share more referrals in a limited time window, with an opportunity to win greater rewards

### Key Learnings
- Final approvals on plan to add additional target platforms for sharing referrals on mobile web delayed the start of work
- Use of Iterable integration for quick win new referral touchpoints (recipe rating) requires additional groundwork from CRM Engine squad and was not ready for integration in this sprint as planned
- With two target initiatives delayed, the split of work for this sprint was skewed heavily - 75/25 - to technical/platform improvements which will improve delivery velocity and reduce error rates. In the upcoming sprint, bottlenecks around decision making have been resolved and planned work is focused on deliveries with immediate impact to squad KPIs

**Demo:** Loyalty & Virality - Sprint Demos - 2026_01_30 15_56 CET - Recording.mp4

---

## Missions
**Tribe:** Loyalty & Virality
**Mega-Alliance:** Consumer
**Squad Lead:** EM : Aleksei Akireikin
PM: Anshal Anand

### Squad KPI
Weekly Loyalty Engaged User Rate

### KPI Movement
Target : 12%
Actual : 5.83% (src)*
Compared to Last Month : +0.09% (5.83% to 5.74%)

* We are currently reporting this data for Loyalty 1.0 from US, as Loyalty 2.0 is still under development

### Delivered (This Sprint)
We are working toward launching the MVP test of  our "Loyalty 2.0" program for HelloFresh US in March. The below deliverables are slated for release in February as a part of milestone 1 (Internal Launch - Friends & Family) of the new program.

1. Established the connection between internal systems (CAS) and the points engine (Talon One), enabling core point processing.
2. Integrated frontend clients with Loyalty API v3 to enable program opt-in and checking a customer's enrolment status and program version.
3. Delivered the new "Rewards Cards" UI, allowing customers to view available rewards in the Loyalty Program.

### Planned (Next Sprint)
1. Enable customers enrolled in the Loyalty 2.0 program to earn points based on their spend via Talon One and view their points balance in the Loyalty Dashboard.

### Key Learnings
1. In the ongoing Factor Rewards experiment in the US, both variants of the experiment are showing a lower weekly cancellation rate. Food-based rewards are leading with a 2.6% lower cancellation rate, versus monetary rewards showing a 2.4% lower cancellation rate when compared to the control group. Based on these early directional trends, we are diving deeper into the data to check if it’s feasible to make an early decision on the rollout of the Factor Rewards Program in the US.

**Demo:** Loyalty & Virality - Sprint Demos - 2026_01_30 15_56 CET - Recording.mp4

---

## Rewards
**Tribe:** Loyalty & Virality
**Mega-Alliance:** Consumer
**Squad Lead:** EM: Bruno Klarin
PM: Thomas Gamper Feitoza

### Squad KPI
Percent of earned rewards redeemed, in the Loyalty 2.0 program*

### KPI Movement
Target: 50%
Actual: 30% (src)*
Compared to Last Month: + 2% (from 28% to 30%)

*Loyalty 2.0 not released yet, so we report on current loyalty 1.0 numbers

### Delivered (This Sprint)
We are working toward launching the MVP test of  our "Loyalty 2.0" program for HelloFresh US in March. The below deliverables are slated for release in February as a part of milestone 1 (Internal Launch - Friends & Family) of the new program.

1. Loyalty 2.0 Rewards Store connected to real rewards and points data, allowing users to: see their points, see their available rewards, and see rewards details.

### Planned (Next Sprint)
1. Loyalty 2.0 Rewards store complete with purchasing capabilities (connected to talon.one). Users will be able to purchase rewards and the points balance will be adjusted accordingly.
2. Introduction of loyalty 2.0 entrypoints in the end-to-end experience (Store, HomePage) to expand loyalty 2.0 presence.

### Key Learnings
As part of FJ Loyalty experiment, we are observing that food related  rewards (e.g. 'Free breakfast reward') have a higher reward take rate (~23% on food related versus ~13% on comparable value discount voucher). We will use this learning to prioritise getting Food-based rewards as part of the Rewards store for Loyalty 2.0 as fast follow, as users demonstrated higher levels of interest.

**Demo:** Loyalty & Virality - Sprint Demos - 2026_01_30 15_56 CET - Recording.mp4

---

# Menu to Content

## Product Content Ready
**Tribe:** Menu to Content
**Mega-Alliance:** Ops
**Squad Lead:** PM: Pretty Yakoub
Engineering and ML: Benjamin Bertincourt

### Squad KPI
Touchless Product Content Rate (% of individual product content assets generated and published without human interaction)

### KPI Movement
Updated KPI Definition
baseline will be provided with new measurement next sprint

### Delivered (This Sprint)
[P500 Concorde]
1. 5 Recipe heroes image-generation model fine-tuning experiments
2. Accuracy & Realism image evaluation framework (offline for now)
3. Curation structure for reference images in Olympus (Concorde DAM)

[PDF Creation Automation] 
1. Allowing different user  choice of templates on tooling. 
2. Launching ingredient supply tips for INTL markets for PDF automations

[KTLO & Continuous Improvements]
1. P500 hypercare for HF and EP data issues.

### Planned (Next Sprint)
[P500 Concorde]
1. [ML] Production ready inference infra for fine-tuned models
2. [ML] MVP of Automated image evaluation
3. [ML] Meaningful improvements on the quality of generated Heroes (measured by photo team feedback and acceptance rate)
4. [Data] KPI measurement pipeline
5. [Refinement] Selective enrichment and Variants iteration, upon approval from teams and stakeholders. 

[KTLO & Continuous Improvements]
1. P500 hypercare for HF and EP data issues.

### Key Learnings
1. Fine-tuning allows us to address some of the shortcomings of foundation image-generation models for HelloFresh image generation, especially SKU and Style accuracy

---

## Food Planning
**Tribe:** Menu to Content
**Mega-Alliance:** Ops
**Squad Lead:** EM: Teresa Chavez Payam Mo
PM: Raghul Babu

### Squad KPI
Weekly Offering (Menu) Task Automation Rate (%)

### KPI Movement
KPI Target still being defined, for this new squad.

### Delivered (This Sprint)
[xPS Data Validation that catches errors before it reaches to customers]
1. Laid the foundation for a new validation service to improve data quality at scale
2. Enabled the launch of an automated validation service to catch menu and content issues earlier, reducing manual effort and preventing downstream operational errors as menu volume grows.

[P500 Availability Management System]
1. Enabled SKU caps with automatic “Sold Out” triggering feature for users to do UAT
2. Page load times improved from ~20s to ~2s to support better usability and adoption.

[KTLO & Continuous Improvements]
1. Improved CCM Menu performance by reducing the menu save response times 
2. Introduced performance tracking editor productivity, giving the squad clear KPIs to monitor and optimize performance.

### Planned (Next Sprint)
[xPS Data Validation that catches errors before it reaches to customers]
1. Enable automated and scheduled checks to catch menu and content issues earlier, expand business rule coverage, and reduce manual reviews and downstream operational errors.
2. Improve system observability to speed up issue detection to allow faster, more accurate investigations, minimizing disruption to operational teams.

[P500 Availability Management System]
1. Complete Availability Management for UAT and rollout by finalizing end-to-end readiness of Availability Management, enabling UAT and rollout for W12 to reduce sold-out issues, manual work in managing availability and improve customer experience.

[KTLO & Continuous Improvements]
1. Further reduce CCM response times to improve editor efficiency by delivering targeted performance improvements to make menu creation and updates faster and more reliable.

### Key Learnings
1. Insights on validation enhancements  alerts needed to effectively detect data discrepancies and gaps in proactive manner.
2. Current logging, tracing infrastructure is "leaky" making the investigations more difficult than it should be.
3. Along with functional tests, data tests help in measuring the success of the system behaviour.

---

## Menu Ranking
**Tribe:** Menu to Content
**Mega-Alliance:** Ops
**Squad Lead:** EM: Michael Johnson
PM: Alejandra Garcia

### Squad KPI
% of All Ordering Customers with at Least 2 Meals from the Top Ranked 15

### KPI Movement
W3: '+0.6pp (wow difference on rolling average last 4w)

### Delivered (This Sprint)
1. Released Week Over Week Variety for Menu-Ranker which improves variety for P500 customers who have a profile
2. Released high performance version of menu ranking API which moves P99 for P500 menu size from 250ms to 90ms and improves throughput by 3x
3. Cleaning up Harp alerts to decrease cognitive load (stating clear actions required, removing unnecessary alerts, adjusting triggers). We had so many alerts that we were starting to ignore them.
4. Improved backtesting so we can now test ~100 different sets of hyperparameters in one day
5. Discovery about backtesting metrics to get a ranking metric that we trust that we can use in offline experiments to compare ranking models. The new metric, which will substitute “recall at K”, is “worst choice score”, which checks what’s the lowest recipe in our ranking, from the recipes that the customer chose.

### Planned (Next Sprint)
1. Including Menu-Ranker recommendations during non-live weeks, enabling full visibility for forecasting purposes
2. Enable applying exclusions and dislikes from the customer profile for all customers (including actives)
3. Enable A/B testing for menu-ranking configurations
4. Finish up backtesting setup, to enable quick offline comparisons of ranking models. This will enable future improvements for Harp.

### Key Learnings
- Found a bug in the production data pipeline (menu_enriched) which didn’t have proper allergens. Fixed bug before direct exposure to customers
- We were treating versions of the same recipe, as the same recipe, which led to us recommending the same item in defaults in consecutive weeks; we have fixed that
- Discovery of more stable embeddings approach to stabilise recommendations

---

## Demand Forecasting & Planning
**Tribe:** Menu to Content
**Mega-Alliance:** Ops
**Squad Lead:** DS: Zlata Tanovic
PM: Shahab Syed

### Squad KPI
SKU forecast variance from actuals measured as Weighted Absolute Percentage Error (WAPE)  at 1 Week Out from target week

### KPI Movement
Top 6 volume regions for all brands where we predict demand: Wk03 Vs Wk 05
UK - 4.1 PPTs reduction
DACH - 1 PPTs increment
CA - 2.5 PPTs reduction
BENELUX - 0.3 PPTs reduction
FR - 1 PPTs Increment
AUNZ - 4.4 PPTs reduction

### Delivered (This Sprint)
[Forecasting Model Improvements]
1. [Box Forecast] Completed development & testing of model for predicting total conversions (new customers) for all markets.
2. [Recipe Uptake Forecast] Personalization integration in INTL: Identified 12/13 sources needed for creating historical defaults and raised request with Atlan team for support on 1/13.

[KTLO & Continuous Improvements]
1. Updated code to ingest real recipe_family values instead of hard coded strings which were causing occasional empty/low forecasts (all INTL markets)
2. Improved F4L prediction model by eliminating data constraints that were leading to suboptimal handling of the existing conversions (all INTL markets)
3. Identified root cause for under forecasting of modular slots (duplicate slot index mapping in upstream data sources ). Deployed fix that successfully improved forecast for W09 & beyond (AUNZ).
4. Investigated & resolved the issue of F4L predictions being the same as customer selections. (reported for FR, solved for all INTL markets)
5. Resolved issue of failing API calls due to empty zip codes in SFS table (All INTL markets).
6. Resolved DC encoding misalignment in source tables that caused non eligible slots to be forecasted for a DC (AUNZ)

### Planned (Next Sprint)
[Forecasting Model Improvements]
1. Club NDD & BOLT orders forecast into one logical unit when sharing with downstream teams, to enable improvement in SCO projections (reported for UK, valid for UK+IE+DACH, scoping validity for all INTL markets).
2. Replace MBT targets with new conversions data in swap ratio calculations and splitting tool logic (All INTL markets).
3. Improve swap ratio predictions by switching to actual customer selections every Wednesday (all INTL markets).
4. Identify structural changes in the model as well as additional features, that will improve F4L model predictions (All INTL markets)
5. Identify optimal solution for incorporating  the launch of exclusive slots for Savers Plan (AUNZ)

### Key Learnings
- We introduced a weekly firefighter program, where every week 1 team member will dedicatedly man the support requests channel. This new  setup is working well and has helped increase productivity: it allows one person to work fully on KTLO & tech debt , while the rest of the team can concentrate on new developments

- Free For Life under forecasting caused by proxy data on F4L conversions. We learned that more precise high quality data existed and were able to improve the forecast by around 5pp WAPE in all markets

- An ensemble of two independent total conversions models outperformed either of the two in almost all markets, by around 2pp WAPE (for the new conversions). This is an input to our total box demand model.  We should continue exploring ensembles for model improvements.

- Code changes deployed near to the weekend require additional focus on impact evaluation: Inventory Planner tool faced a downtime due to unavailability of forecast, reported on Friday 4:55 PM. While we aligned with team to deploy a solution on Monday as they had a workaround, we learnt that in future this could lead to huge impact if the issue is unreported over the weekend.

---

# New Ventures

## Market Innovation
**Tribe:** New Ventures
**Mega-Alliance:** Consumer
**Squad Lead:** PO: Sameer Doda
EM: Wanderley Teixeira

### Squad KPI
Orders Confirmed

### KPI Movement
N/A

### Delivered (This Sprint)
1. GC NL -> HF Migration: Migration foundation (backend)
- Built and validated core migration tooling to move active GC customers to HF, including payment tokens, subscription preferences, and entitlements.
- Prepared production-ready migration branches to support phased rollout.

2. GC NL -> HF Migration: Communicaiton ((FE web/mobile)
- Shipped customer-facing CTAs across web and mobile to inform customers of:
  - GC closure
  - HF as the new destination
  - The new HF premium plan offering
- Ensured customers are guided through the transition at key decision points.

3. Initial rollout readiness
Finalized the first migration batch scheduled for Feb 5, targeting ~27% of GC customers, as a planned initial rollout.

### Planned (Next Sprint)
1. Execute remaining (NL) GC → HF migration batches in W7, completing the planned rollout beyond the initial Feb 5 branch.

2. Launch price comparison experience for GC customers to clearly communicate value and pricing differences, improving conversion and confidence.

3. Scale migration tooling to support remaining 4,260 GC NL customers (73%).

### Key Learnings
1. Migration tooling is foundational infrastructure, not a one-off task
- Investing early enables safer market transitions, faster rollouts, and reduced customer and revenue risk.

2. Customer-facing clarity is as critical as backend correctness
- Migration success depends on aligned backend logic and frontend/mobile UX, especially during product sunsets.

3. Phased rollouts reduce risk and increase confidence
- Starting with a meaningful first batch (27%) provides strong signal before scaling remaining migrations, and ensures customer communication (eg email) is delivered.

**Demo:** New Ventures Tribe Bi-Weekly Demos - 2026/01/30 15:12 CET - Recording

---

## Factor Form
**Tribe:** New Ventures
**Mega-Alliance:** Consumer
**Squad Lead:** PO: Hamed Karimian
EM: Pantelis Chatzinikolis

### Squad KPI
Factor Penetration Rate

### KPI Movement
0.33%
+0.01%
action: accelerating work on entry points & CRM comms

### Delivered (This Sprint)
1. SKU Expansion 
Meal Shake and Creatine+ product lines experience launched, expanding the product assortment for customers and TAM for Factor Form
- Homepage display
- Navigation addition
- Ordering experience for new SKUs 

2. Funnel Improvements
- Improved discount logic
- Improved dicount communicaitons and additional 
 - Order summary improvements

### Planned (Next Sprint)
1. SKU Expansion: 
Updated Product Detail Page (PDP) for Creatine and Meal Shake lines will include
- dynamic flavor selectors
- subscription options and SNS logic
- Nutritional and educational content

2. OTP Expansion: 
- OTP in Order History display

### Key Learnings
1. New product launches require full-funnel visibility updates. 
- Create new product launch checklist: homepage, nav, PDP, dashboard, order history - ensure no touchpoint missed.

2. OTP integration spans multiple product areas. 
- Map OTP touchpoints across all product areas before implementation to prevent scope creep.

**Demo:** New Ventures Tribe Bi-Weekly Demos - 2026/01/30 15:12 CET - Recording

---

## Good Chop
**Tribe:** New Ventures
**Mega-Alliance:** Consumer
**Squad Lead:** PO: Alexander Matlin
EM: Beatrice Dimarucut

### Squad KPI
Net Revenue

### KPI Movement
$10,000,825
+$2,673,825
action: in-line w/ targets.

### Delivered (This Sprint)
1. OTP Launch: 
Post Checkout experience for the One Time Purchase MVP, 
- dashboard funcitonality to display upcoming deliveries
- reordering logic for active customers 
- CRM flows and confirmaitons
- Post-purchase visibility of ordered items

### Planned (Next Sprint)
1. Dashboard Improvements: 
Benefits communicaiton across the conversion funnel, improving the vallue perception of Good Chop, especially in comparison with competitor offers, retail, clear information and guidance of benefits captured with subscription to Good Chop. 

2. Funnel: 
- Deeplinking from customer-facing marketing/pages to benefits communication in funnel, dring conversion rate through greater connection between marketing comms & on-site offer.

3. Seamless Funnel Prep (BE)
Work on infrastrucutre to enable seamless plan management for customers (Q1 priority)

### Key Learnings
1. UI micro-interactions impact conversion significantly. 
- Include UX polish pass as explicit sprint task, not afterthought - small UI fixes compound into conversion gains.

2. Free Cuts TR drop was caused by skipping subscribable addon by Meal Addons Selection (MAS) service (#in-60958-22-01-26). 
- The found MAS issue fixed on 2026-01-30. Patch for impacted customers (~35K) to be done on W06.

3. Observability investment pays dividends for maintaing insight into key performance KPIs.
We ill include tracing/observability tickets in MVP scope, not post-launch.

**Demo:** New Ventures Tribe Bi-Weekly Demos - 2026/01/30 15:12 CET - Recording

---

## The Pets Table
**Tribe:** New Ventures
**Mega-Alliance:** Consumer
**Squad Lead:** PO: Ahmed Wagdi
EM: Maria Chelminska

### Squad KPI
Net Revenue

### KPI Movement
$3,917,368
+$926,368
action: in-line w/ targets.

### Delivered (This Sprint)
1. Digital feeding guideline launch: 
- Entry points 
- Customization of content  based on plan/profile of customer
- Multi[pet support 

2. CVR Program: 
- Improved benefit communication throughout funnel
- Product statistics for customer engagement throughout the conversion funnel.

### Planned (Next Sprint)
1. Dashboard Improvements: 
Entry points aimed at increasing the discoverability of services and products offered by TPT:
- Add-ons Store and easy add-on addition
- Refer-a-Friend visibility improvements and benefit communication 

2. CVR Program: 
Social proofing and engagement content strategy within the funnel, including statistics, reviews and testimonials to build customer trust in the TPT brand.

### Key Learnings
1. Social proof accelerates trust-building in signup. 
- Prioritize social proof components early in signup optimization work - they compound conversion gains.

2. Recipe content requires data validation layer. 
- Build automated content validation for recipe data before shipping new recipe features.

**Demo:** New Ventures Tribe Bi-Weekly Demos - 2026/01/30 15:12 CET - Recording

---

# Operations Data & Decisions

## Data Engineering
**Tribe:** Operations Data & Decisions
**Mega-Alliance:** Ops
**Squad Lead:** Mahendra Chandrakar

### Squad KPI
# of global supply chain data sources

### KPI Movement
N/A

### Delivered (This Sprint)
Global Pick2Light Data Solution:
 - Implemented a solution to enable photon users to consume data from Snowflake tables, as a poilet project we enabled few highjump data tables from snowflake to photon for ops analytics team  
 Logistic last mile cost analytics:
- Implemented data pipeline and assets for Last mile carrier invoice data. This ETL automates the invoice data feed from carriers to analytics plaform for logistics team to analyze and optimize last mile cost

### Planned (Next Sprint)
P500 Forecasting data for international: 
  Extend the solution implemented for NA P500 to international customer menu default and  ranking data history for forecasting.
GLobal Pick2Light data solution: 
  Use flink for data formatting, filering and enrichment to Unify data feed for downstream systems and unified Snowfkake and photon tables.
Workday strategic sourcing data: 
 implementing an automated solution to unlock data from Workday Strategic Sourcing, enabling enterprise visibility and truly data-driven sourcing decisions informed by historical performance, bid competitiveness.
Fedex last mile invoice data: 
  This is continuation from previous sprint (G) ,  We are waiting on fedex to provide data feed, once they provide the data we will add data assets for invoice data from them.
Global ICS data solution:
  Unify ICS ticketing data into common data assets into snowflake and photon

---

## SCM Analytics Engineering
**Tribe:** Operations Data & Decisions
**Mega-Alliance:** Ops
**Squad Lead:** Sharif Abdel-Halim

### Squad KPI
% of All Ordering Customers with at Least 2 Meals from the Top Ranked 15

### KPI Movement
W3: '+0.6pp (wow difference on rolling average last 4w)

### Delivered (This Sprint)
Personalization: 
Enhanded DQ checks for inelibility flags in order to make sure we have enough eligible recipes for each preset
Created a separate Menu Pipeline for US MPS with DQ checks to compare MPS US data with ISP US data to ensure that the new MPS source as the same DQ before we make the switch  

GOAT:
- We build the first rudimentary GOAT Trigger API endpoint to trigger optimization jobs 

Upstream:
- Wrapped up all the changes for the PO Base Grain table in order to deprecate the old Purchase Order Table from the Ordering Tool (Tapioca)

### Planned (Next Sprint)
Personalization
- During the hackathon we want to assess the effort to embed Factor data into personalization data assets
- Creation of a shadow pipeline to collect US data from MPS instead of ISP in order to have the same source for US and intl Menu Data 

Upstream
- Deprecation of all remaining procurement data assets that source the data from Tapioca in order to fully deprecate Tapioca

---

## Operations Research
**Tribe:** Operations Data & Decisions
**Mega-Alliance:** Ops
**Squad Lead:** EM: Robert Dochow

### Squad KPI
# Models in production

### KPI Movement
+1 model in DKSE

### Delivered (This Sprint)
Personalization: New optimization based approach was shown which shows superior performance to Kenobi
Production: DKSE Kitting Matching Optimization launched
Menu Planning: GAMP'26 roll-out kick-off in UK

### Planned (Next Sprint)
Personalization: Alignment with current personalization teams, how to improve/replace Kenobi
Logistics: Review of autoamted demand steering (TADA) in order to enable a more granular steering above just utilization driven steering (i.e., utilization & remaining-time-to-cut-off steering)

---

## Data Science
**Tribe:** Operations Data & Decisions
**Mega-Alliance:** Ops
**Squad Lead:** EM: Andrew Kim

### Squad KPI
Forecast accuracy

### KPI Movement
Normal Menu | High Loyalty 6WO WAPE: 46% (-3%)
Normal Menu | Low Loyalty 6WO WAPE: 68% (-0%)

### Delivered (This Sprint)
- Created / tested new LLM based features for the model that can tell us whether certain recipes might be more/less polarizing for the american taste palate. Very minor to no change for high loyalty accuracy.
- Updating model run modes to include a new accuracy mode that will more consistently track model accuracy over time, while removing noise like region / menu changes.

### Planned (Next Sprint)
- Further testing around LLM based features to see if we can create some features that suggest why certain recipes don't do well despite being highly recommended (Like Greek Feta Meatloaf with Veggie Jumble)
- Discussions with personalization on potentially locking Penguin / Profile ranker 6 weeks out to minimize volatility from non-live --> live week
- Check on volatility of profile-ranker recommendations from 6WO --> 5WO once data starts publishing in non-live weeks

### Key Learnings
- We will be splitting up our run modes in ML Flow for better tracking and saving as we've aggregated too much into the same experiments / model names.

---

# Ops BI

## Sourcing and Planning
Christian Lannefranque
**Tribe:** Ops BI
**Mega-Alliance:** Ops
**Squad Lead:** Cem Erenguc

### Squad KPI
# of Sourcing and Planing metrics that are globalised and cover at least 50% of the MK order count

### KPI Movement
+1

### Delivered (This Sprint)
Process/Area | KPI 
- PROC DO3 | Procurement | Spend Coverage Metric for Int. 
- CS2 | Menu Expansion: Demand Planning | WAPE Target 

Others: 
- DO2 | NIDEID Dashboard Training
- DO3 | Statics Collection Analysis Support
- DO3 | COGS Late Forecast Alert
- DO1 | OTIF Emails Support
- Demand Planning Knowledge Transfer 

Capacity Allocation 
- NID/EID: 20% 
- Demand Planning Consolidation: 20% 
- Int. Procurement: 20% 
- Supplier Performance: 20% 
- COGS Bridge: 20%

### Planned (Next Sprint)
Process/Area | KPI Delivered
- PROC DO3 | Procurement | Savings: SKU Replacement Logic
- PROC DO2 | EID Count by Steps

Others:
- PROC DO3 | Consolidating COGS Requests & Discussion w/ local markets
- PROC DO1 | SPICER Ownership Transfer

Capacity Allocation:
- NIDEID: 25%
- Demand Planning Consolidation: 12%
- Int. Procurement: 25%
- Supplier Performance: 25%
- COGS Bridge: 12%

### Key Learnings
We can't forget about documenting and training when finishing a workbook / dashboard.

**Demo:** For links to products to review metrics, please refer to our Internal Roadmap

---

## Fulfilment
Chad Aoun
**Tribe:** Ops BI
**Mega-Alliance:** Ops
**Squad Lead:** Cem Erenguc

### Squad KPI
# of Fulfilment performance metrics that are globalised and cover at least 50% of the MK order count

### KPI Movement
+6

### Delivered (This Sprint)
Process/Area | KPI 

- Companys Stategy 1: Dwell Time US integration - data being validated, squad KPI movement next round
- FULF DO 2, POR: Logistics US integration - 6 TIS and Errors metrics delivered. Final presentation to stakeholders is planned.
- FULF DO 4, MK CPB: Production S2J efficiency metrics - Phase 1 metrics complete (not included in Squad KPI, due to only being relevant for Automated cluster = < 50%)

Capacity Allocation
- Carrier Performance: 40%
- Production Errors: 20%
- Farm-To-Fork Time: 20%
- KTLO: 20%

### Planned (Next Sprint)
Process/Area | KPI Planned w/ Global coverage

- Company Strategy 1: Farm-to-Fork/ Dwell Time metrics - US rollout: Metrics (5+)

### Key Learnings
International scope makes for a lot more alignment and planning, due to diverging market expectations

**Demo:** For links to products to review metrics, please refer to our Internal Roadmap

---

## Executive and E2E
Bishnu Panda
**Tribe:** Ops BI
**Mega-Alliance:** Ops
**Squad Lead:** PO/EM: Cem Erenguc

### Squad KPI
# metrics reported globally as part of global business reviews and executive reports

### KPI Movement
+5

### Delivered (This Sprint)
Process/Area | KPI Delivered
- P500: P&P and Proc Error Rate for baseline and P500 customers
- Executive: 4 New metrics for the Global BU WBR

Process/Area | KPI Delivered with Non Global Scope (Int Only)
- CSRD I 9 metrics: Technical Material Weight (g),  Biological Material Weight (g). Total Material Weight (g)% of Technical Materials used, % of Biological Materials used, Recycled Weight (g), Recyclable Weight (g), % of Recycled, % of Recyclable

Capacity Allocation
- Executive: 40%
- Menu Expansion: 20%
- Errors: 20% 
- KTLO: 20%

### Planned (Next Sprint)
Process/Area | KPI Delivered
- Global Business Review: People BR Metrics will be delivered to NA sites

(Global BR: alignment, consolidation, and discovery activities with 60% of team bandwidth)

### Key Learnings
- Ingredient Family–level Quality Error 2026 targets are now included in dashboards
- Executive dashboard for the CEO’s office has been shared with all MDs; updates are underway based on received feedback
- Ops Complexity and Menu Expansion metrics consolidation is in scoping, with the goal of reducing 5+ dashboards into a single Single Source of Truth

**Demo:** For links to products to review metrics, please refer to our Internal Roadmap

---

## Customer Care
Ming Jin Siew
**Tribe:** Ops BI
**Mega-Alliance:** Ops
**Squad Lead:** PO/EM: Cem Erenguc

### Squad KPI
# of Customer Care Operations Metrics with Global coverage

### KPI Movement
+3

### Delivered (This Sprint)
Process/Area | KPI Delivered
- Executive | Chatbot Self-Service Rate
- Executive | Interaction Ratio Budgets 2026
- Executive | Customer Care Cost Budgets 2026

Capacity Allocation
- Datagamz: 50%
- Executive Reporting: 20%- Workforce Management: 10%
- KTLO: 20%

### Planned (Next Sprint)
Process/Area | KPI Planned

- Customer Care | Agent Compliant Compensation (continued)
- Internal FCR

### Key Learnings
2026 Exec Reporting budgets complete. DataGamz issues resolved; back to focusing on roadmap (Agent Compliance, Internal FCR and WFM)

**Demo:** For links to products to review metrics, please refer to our Internal Roadmap

---

# Ops Enablement

## eProcurement
**Tribe:** Ops Enablement
**Mega-Alliance:** Ops
**Squad Lead:** Sara Felcher

### Squad KPI
eProcurement Suite launched in all markets

### KPI Movement
Continued focus on stronger adoption of Workday Procurement for users and planned for additional markets to onboard in Q2

### Delivered (This Sprint)
1. Signed IronClad SOW / Immediately began working on enabling SSO to allow for legal teams to leverage the Jurist AI feature on Ironclad even before being live on tool for contract management 
2. Kicked off phase 2 workday procurement (ANZ/CA/Factor Verden) with Kainos team 
3. Further aligned on Marketing conversation and the need for Freshcost vs. MEL, working to streamline process for Marketing spend
4. Kicked off Ironclad implemenation with team and started planning for the HR and Procurement launch timing
5. Continued adoption and CI tasks and leveraged an existing implementation partner (Strada) to help with backlog and move faster

### Planned (Next Sprint)
1. Enable SSO on Ironclad to enable Jurist AI feature  
2. ANZ Workday Procurement Kickoff 2/2
3. CA Workday Procurement Kickoff week of 2/9 (to be scheduled) 
4. Enable CAPEX categories in Workday Procurement 
5. Align on approach and timline for Ironclad implementation

### Key Learnings
Workday Procurement adoption is being hindered when users feel the tool takes longer than the previous process (lacking tooling) and better change management focus needed to onboard these groups and make sure concerns are heard and addressed. Meetings in progress to manage.

---

# Ops Tech Conventional

## OpsTech Benelux
PM - Anaïs van den Hengel
EL - Jeroen Entjes
**Tribe:** Ops Tech Conventional
**Mega-Alliance:** Ops
**Squad Lead:** PO/EM:Thomas Saaby

### Squad KPI
-% Features delivered that contribute to standardisation (in local tools & Hellotech code base)

*Features = stories, tasks are not counted within this KPI

### KPI Movement
No movement 
(0% vs. 0% last sprint)

### Delivered (This Sprint)
The required features to go live with project Mosaic (deprecating GC, launching premium preference) has been delivered, including enabling more than 1 sorting line and allowing marketing to target premium customers for their marketing campaigns. This will drive value for our customers (launching a premium preference) and value for operations (simplification of not handling two seperate brands, giving more space for additional HelloFresh recipes)

### Planned (Next Sprint)
- End to end test run of the full tooling landscape with Mosaic test data (Before go-live in W09) 
- Enable core menu recipes to be planned on slots >10.000 to enable recipe variants (and thereby menu expansion) - removing legacy hard-coded rules

**Demo:** Folder with demos

---

## OpsTech Nordics
PM - Marine Gautier
EL - Domingo Gomes
**Tribe:** Ops Tech Conventional
**Mega-Alliance:** Ops
**Squad Lead:** Thomas Saaby

### Squad KPI
-% Features delivered that contribute to standardisation (in local tools & Hellotech code base)

*Features = stories, tasks are not counted within this KPI

### KPI Movement
-6ppt
(44% vs. 50% last sprint)

### Delivered (This Sprint)
- Wrap Q4 opened topic
- Continue on standardisation of conv cluster forecasting set-up and define new standards - working towards one shared forecasting set-up across the conventional clsuter (as the first step) and data sharing to global systems (IP) 
- Go-live with recipe booklets - Driving value for customers though a better customer experience and for operations (not having to pick +150 recipe different recipe cards seperatly, but just 1 unique booklet per customer)
- Kick-off data preparation for WMS 2.0 replenishment module

### Planned (Next Sprint)
- Recipe booklets ramp-up & hypercare
- WMS 2.0 replenishment module kafka topic creation 
- Update conv cluster pure forecasting pilelines up to new standards post BNL findings
- Set-up foundations for app with Django (better / more scalable set-up than current Streamlit applicaiton and more in line with global standards)

### Key Learnings
Q3/Q4 work on automatic handling of partial actuals & get rid of cut-off structure (rely on LC instead of local/manual cut-off table/mapping) paid off and lead to a smooth holiday period with minimal disruption.

**Demo:** N/A

---

## OpsTech France
PM & EL - Andreas Jakobsson
**Tribe:** Ops Tech Conventional
**Mega-Alliance:** Ops
**Squad Lead:** Thomas Saaby

### Squad KPI
-% Features delivered that contribute to standardisation (in local tools & Hellotech code base)

*Features = stories, tasks are not counted within this KPI

### KPI Movement
No Movement
(39% vs. 39% last sprint)

### Delivered (This Sprint)
- Local setup of DPC to evaluate performance in preparation for Project Odin rollout starting in Feb. Key point is that we are missing quite a few SKU volumes, which we are discussing with operations
- Completed script for harmonized approach for data sharing to IP within Conventional Cluster, where France deciated. Testing expected to commence Feb 10 assuming operations is ready. 
- We launched Click & Collect service for our own employees. Next step will be roll out for customers in Paris region.

[FR sprint 101]

### Planned (Next Sprint)
- Next sprint we plan to continue to work on DPC and SKU dimensions
- We also plan to begin our work to improve our bulk compensation tool as it is has not been adapted to certain edge cases that can happen especially since we prepared future of food in production

---

# OpsTech Auto Cluster

## OpsTech UK & DACH
PM - Andrés Alejandro Isava Paredes
EL - Syed Minhaji
**Tribe:** OpsTech Auto Cluster
**Mega-Alliance:** Ops
**Squad Lead:** Ed Dunger

### Squad KPI
-% Features delivered that contribute to standardisation (in local tools & Hellotech code base)

*Features = stories, tasks are not counted within this KPI

### KPI Movement
40%

### Delivered (This Sprint)
- DPC adoption by UK Order Creation now ready for Phase 2 Employee box Tests in WK07
- Supporting UK Jan Ramp with Network capacity for WM / GR and UK snow crisis
- Aligning UK & DACH data pipelines to enable single Auto Cluster approach
- Automated Courier Label flipping service expanded to UK HFDN to enable better emergency response to incdients (e.g. weather)

### Planned (Next Sprint)
N/A

---

## Data enablement
PM- Andrés Alejandro Isava Paredes
EL- Dragos Simionescu Alex Goodwin
**Tribe:** OpsTech Auto Cluster
**Mega-Alliance:** Ops
**Squad Lead:** Ed Dunger

### Squad KPI
-% Features delivered that contribute to standardisation (in local tools & Hellotech code base)

*Features = stories, tasks are not counted within this KPI

### KPI Movement
33%

### Delivered (This Sprint)
- Extended TIS Business Marts to AU/NZ to enable standardised Logistics Exceptions management
- Extended Physical box pipelines (ODIN) to Nordics
- Completed 30% Wave 1 Deprecation of UK_OPS_ANALYTICS
- Evaluated usage of Atlan API for automatic README completion in order to streamline assets certification
- Migrate all Airflow DAGs to dbt orchestration (Snowflake tasks)
- Repoint UK date_dimension SF consumers to global date_dimension

### Planned (Next Sprint)
N/A

### Key Learnings
- Snowflake dbt projects offer limited observability that we had to overcome with custom solutions. These required significant more effort than the migration itself.
- ODIN data outputs structure differs by business_division, which requires additional modeling for standartization
- Physical box price and costs calculation logic needed to  be refactored to reflect the actual numbers from сustomer basket and shopping experience

---

# Order Enrichment

## NA Order Enrichment
**Tribe:** Order Enrichment
**Mega-Alliance:** Ops
**Squad Lead:** PO: Jeff Risdon
EM: Pablo Carbajal Siller

### Squad KPI
P500 expansion

### KPI Movement
Systems successfully processed orders for P300 and P500 without issue

### Delivered (This Sprint)
P500 Features :[80%]
1.Deployed the ingredient subsitutions Kafka consumer to production, added several end to end tests and integration tests (50%)
2.Completed end to end tests in staging for Katana to Pyramid (P2L) Integration in order to automate the data flow and enable substitutions (25%)
3.Improved Snowfake data ingestion to include data required to enable scan2slot (5%)

KTLO: [20%]
1. Added short shiping capability for P500 recipes selected by customers not in P500 regions which resulted from an upstream menu error
2. Recovered 3800 orders across HF, EP, GO and TPT in the US that were mistakenly canceled by upstream systems 
2. Published CC Workbook Orders to Order Database to support tracking of those orders when the Order Database is deployed
3. Various support requests

### Planned (Next Sprint)
1.Handling Edits & deletes in P500 subs process
2.Katana  <>Lassy intergration for generating orders in the exception paths(Remakes,relabels)
3.Katana<>BIS upgrade task breakdown

### Key Learnings
1.Many edge cases exist in the application of subsitutions on the Data Consumer side that we needed to build exception handling for

---

## Global Order Enrichment (ANZ OPS)
**Tribe:** Order Enrichment
**Mega-Alliance:** Ops
**Squad Lead:** PO: Zubeda Shaik
EM: Jeremy Badcock

### Squad KPI
% of order volume processed via Odin

### KPI Movement
No movement. Still at 21%

### Delivered (This Sprint)
Enhancements to enable Highlander: [75%]
1. ODL v1 delivery for CK and CA markets
2. Consume Order of Delivery Events for KSCMX (Order Enrichment Trigger intiative)
2.Implement Odin network allocation DAG changes to allow for on-demand runs in DACH

KTLO: [25%]
1.Added monitoring and alerting to prevent kSCMx generation during periods of high consumer lag
2.Added new schedule for kSCMx Italy
3.Migrate from customer loyalty to box count topics for kSCMx

### Planned (Next Sprint)
1.Implement self-service re-runs for Odin Order validation pipelines
2.Technical design for Odin implementaion in France 
3.ADR for core pipeline change to pass packaging options to CNP
4. Testing of the new order enrichment trigger in kSCMx

### Key Learnings
1. A high number of validation alerts need to be rerouted to the appropriate teams owning metadata.
2. We will pause work on migrating the kSCMx to FTCP until after the Project 500 lauch in the US

**Demo:** https://drive.google.com/file/d/1cM5DLklUqM7U2SZfGGMLoZZklzvKBBjn/view?usp=sharing

---

## Packaging Optimization & Dropshipping
**Tribe:** Order Enrichment
**Mega-Alliance:** Ops
**Squad Lead:** PO: Abie Joseph
EM: Maksym Dykhtiaruk

### Squad KPI
Packaging Costs ; Revenue Growth From Marketing Partnerships

### KPI Movement
No movement since last sprint
We will need to develop a way to measure this across all markets

### Delivered (This Sprint)
Enahancements to enable Highlander: [80%]
1. Highlander (standartizing packaging for all markets) 
1.1 Odin CA Dynamic Packaging Configuration (DPC) Wrapper (Phase 1)
 - Finished remaining packaging features for all 3 brands
 - First round of integration testing finished
1.2 Odin - Native DPC solution for CA, CF and CK (Phase 2)
- Add-on range configuration done

KTLO: [20%]
1. A few small business requests
2. BIS UI test automation (saves manual dev efforts for testing releases): covered new BIS features
3. Fixed 4 Security vulnerabilities in BIS APIs

### Planned (Next Sprint)
1. Highlander - continue Native DPC solution for 3 Canada Brands - 56% market rollout Q1 Target 81%
2. Highlander - DPC UK launch. Physical Box Test (Employee Trial) -  56% market rollout Q1 Target 81%
3. Box Insert Service (Marketing inserts) - Integration with xPS and UI changes - to obtain marketing SKU info directly from source of truth and reduce human errors during campaign creation. - Reduce montly error rates by 60%
4. Box Insert Service - Integration with CDP to automate manual file upload containing audience for specific targeting. - increase revenue by $13m from marketing partnerships.

### Key Learnings
1. Changing business priorities in local markets have impact on launch timelines
2. UI Autotests save efforts for go-live process, but require maintenance

**Demo:** https://drive.google.com/file/d/1Gnvr8pQH16o1ckPdWFm7WbXbym4OEyy9/view?usp=sharing

https://drive.google.com/file/d/1UpoPhLXtuTH9u9SgZ6M01qrjI1BjYVsZ/view?usp=sharing

---

## BeCool
**Tribe:** Order Enrichment
**Mega-Alliance:** Ops
**Squad Lead:** SL: Mark Brady
PM: Tony Tannous

### Squad KPI
Customer Reported Error Rate (<=0.20%)

### KPI Movement
0.19% error rate in W04, down from 0.22% in W03 - need to wait until Monday to get W05 numbers

### Delivered (This Sprint)
Error Reduction Activities [35%]: 
1.Closed 8 customer requests leading to more accurate integration and delivery creation facilitating reduced error rates [10%]
2.Migrated from aws redis 4.0 to valkey before extended support starts reducing operational costs of AWS environment [15%]
3.Migration from Katana to Lassy for HelloFresh delivery management allowing for real time feedback reducing potential for errors due to delayed feedback[10%]

Cost Reduction Activities [45%]:
1. Linehaul optimisation. Increased visibility of depot receive and dispatch orders for all depots along the linehaul journey. More visibility in each box arriving \ departing resulting in less boxes being misplaced from production to last mile depot [15%]
2. Expanded PTV usage for route optimisation to 100% of W05 deliveries. This is toe reduce the number of required trucks and delivering boxes on time reducing error rates and reducing operational costs. [30%]

KTLO [20%]:
-Remediated 4 critical security wiz alerts. Increasing stability and reduced risk potential ensuring smooth system operations. Customers had uninterrupted system access allowing delivery management which reduces error rates.

### Planned (Next Sprint)
1. Optimise PVT integration 
2. Scope phase 3 requirements for Line Haul optimisation project
3. Finance alerting for business insights and agility
4. Launch Lassy integration
5. Upgrade sorter Lebra app. Faster more accurate results will result in less errors

---

# Payments

## Payment Offering
**Tribe:** Payments
**Mega-Alliance:** Growth
**Squad Lead:** Khaled ElSayed Vimarsh Thusu

### Squad KPI
Payment Tokenization Success Rate

### KPI Movement
Actual: 95.41% (W04/05, Activation only)
Compared to 2 sprints ago: -1.34pp (from 96.71% W52/01 to 95.41% for W04/05)
-------
Insights:
Tokenization Success Rate for HF US dropped in W05 to 91.43% (vs. 94.07% in W04) after a change introduced with ProcessOut. Investigation and mitigation is ongoing.

### Delivered (This Sprint)
Sprint Focus: The team prioritized to focus on learnings from the initial Express Checkout test for Factor as well as preparations for implementing the APM flow through our orchestrator ProcessOut which is an enabler for adding additional payment methods through ProcessOut as a technical gateway moving forward.

1. Express Checkout Validation phase for Factor markets including address page modifications
2. Discovery done for implementing the APM flow in ProcessOut

### Planned (Next Sprint)
Sprint Focus:  Ship Charge at Checkout and Reactivation for Direct Sales to improve Acceptance Rate; Have MobilePay ready for testing in sandbox.

1. Release C@C and C@R (DS and Leads) for HF brand. 
2. Finalising APM flow and start testing MobilePay in sandbox. 
3. Implement the FE validation events.

---

## Payments Platform
**Tribe:** Payments
**Mega-Alliance:** Growth
**Squad Lead:** Zeeshan Akram Gangadharan Khoteeswarun

### Squad KPI
Payment Approval Rate

### KPI Movement
Actual: 94.81% (W04/05)
Compared to 2 sprints ago: +1.81pp (from 93.12% W52/01 to 94.81% for W04/05)
-------
Insights:
Recurring charges AR and dunning ship rate outperforming YoY. Fully rolled out markets on ProcessOut from previous sprint performing around 1.5pp higher for recurring AR vs. last year.

### Delivered (This Sprint)
Sprint Focus: Progressing payment-order decoupling thorugh rollout of POPS. Enabling the further rollout of ProcessOut by closing identified feature gaps. 

1. LU has at least one payment run and rerun through POPS
2.Started sending additional customer Data to Processout (email, name, and billing address)  with the goal to improve AR through ProcessOut
3. US & FJ are running 50% of new cards via ProcessOut.
4. POC for frictionless 3DS flow through Processout SDK integration

### Planned (Next Sprint)
Sprint Focus: Progress on Payments-Order Decoupling by moving additional flows to Payment Orchestrator and POPS.

1. Rollout C@C through Payments Orchestrator - This will help to move all flows through PO which reduces our technical complexity
2. Finalize current LU runs in POPS - LU will become independent of Process Orchestrator 
3. Use PTS as a source of truth for tokens in smaller countries - rollout this after the bug fix

### Key Learnings
1. Tasks without estimates like bugs/investigation needs to be tracked differently
2. With 5 different rollouts currently handled within team, we need to better manage and visualize it

---

## Risk and Fraud Management
**Tribe:** Payments
**Mega-Alliance:** Growth
**Squad Lead:** Tessa Rötzmeier Cagdas Ozek

### Squad KPI
Fraud Approval Rate

### KPI Movement
Actual: 92.09% (W04/05)
Compared to 2 sprints ago: -3.78pp (from 95.70% W52/01 to 92.09% for W04/05)
-------
Insights:
Expected seasonality impact due to higher trending global Dupliacte Block Rate compared to first weeks of the year (3.1% vs. 5.5%) + Fraud Attack CG in W05 increases Payment Fraud Block Rate from 0.5% to 56.1%

### Delivered (This Sprint)
Sprint Focus: Improve dunning model accuracy and respond to fraud incidents. The team prioritized enhancing the pre-payment and post-payment dunning models while maintaining fraud prevention. A critical fraud attack on Green Chef US required immediate investigation and response.

1. Identified and implemented postcode features for pre-payment dunning model
2. Designed and implemented Expected Value Transformation pipeline with backfill DAG
3. Investigated Green Chef US payment fraud attack (~6K blocked attempts) and helped security implement preventive measures
4. Updated dunning cancellation times for Italy (800 boxes/week impact) and GB BOLT
5. Resolved Airflow-02 DAG discovery issues and EMR-01 task failures

### Planned (Next Sprint)
Sprint Focus: Operationalize dunning improvements and shift fraud prevention earlier. Based on Sprint 2 learnings, the team will deploy EVT scoring to production, explore proactive fraud prevention at registration (vs. checkout), and address infrastructure cost concerns through EMR migration exploration.

1. Complete Expected Value Transformation pipeline and enrich Dunning dashboard with EVT scores
2. Implement chargeback traffic split logic (Justt 80%, Forter 20% with 30% minimum)
3. Implement fraud prevention measures in NL (disposable emails) and GB (address blacklist)
4. Explore EMR EC2-to-EKS migration and Unity Catalog migration steps
5. Continue dunning model improvements: voucher features and backfill score pipeline

---

# Plan & Procurement

## Touchless Ordering
**Tribe:** Plan & Procurement
**Mega-Alliance:** Ops
**Squad Lead:** PO: Oliver Gilliland
EM: Mamta Yadav

### Squad KPI
Percent of purchase orders placed via touchless ordering

17% end of 2025 to
56% end of Q2 2026

### KPI Movement
Currently at 18.1%. Increased by 0.3% from just-in-time pilot expansion in US.

### Delivered (This Sprint)
[North America stock SKU touchless ordering - 11% KPI impact]
1. Final inputs for TOPO order recommendation collected in Order Planning database; transfer data integrated via weekly Supply Quantity Recommendation (SQR) Kafka topic
2. Initial skeleton created for new page where supply planners will review network-level order recommendations

[US just-in-time recommendations - 13% KPI impact]
1. Next batch of SKUs enabled, increasing from 10 SKUs in 1 DC to 31 SKUs in 2 DCs. On track to enable all just-in-time SKUs for all US DCs by end of March

[KTLO & Continuous Improvements]
1. Supplier split integration enabled for orders placed by INTL supply chain planning team for delivery to EU third-party warehouses (3PWs)

### Planned (Next Sprint)
[NA stock SKU touchless ordering - 11% KPI impact]
1. Add category and region filters to supply planner review page
2. Display closing stock, recommendations, and planned stock on supply planner review page

[Recommendation Engine - 3.3% KPI impact]
3. Integrate DC master data to match against order recommendations

[KTLO & Continuous Improvements]
4. Separate cleardown support for Kititng and assembly SKU's to improve kitting SKU stock rollover accuracy for just-in-time touchless ordering

**Demo:** Bi-Weekly Demo : Ordering - 2026/02/02 13:25 GMT - Recording

---

## Purchase Order Lifecycle
**Tribe:** Plan & Procurement
**Mega-Alliance:** Ops
**Squad Lead:** PO: Trishul Venkata Reddy
EM: Serghei Bleih

### Squad KPI
Total number of touchpoints after purchase order recommendation

### KPI Movement
N/A

### Delivered (This Sprint)
[Transfer Order and Transport Management Rollout]
1. Rolled out TO for US packaging. Implemented showing available inventory when adding new SKUs to eliminate a manual calculation and removed pick-up dates when the shipment method is set to vendor delivered to simplify the UI.
2. Updated the temperature range and currency  mapping to support the CA rollout. We are scheduling UAT next week.

[Legacy Ordering Tool Deprecation]
Disabled unused order reasons for the US market, enabled new comment field for POs to unlock deprecating legacy spreadhseets used for logistics communication. Added the temperature ranges to the PO status view for the EU team to deprecate one of the legacy OT exports. With support from platform team, exposed new PO accept / reject replacement endpoint (used by suppliers) thus eliminating another blocker for OT deprecation. Deprecated GSync usage in US. 

[KTLO & Continuous Improvements]
1. We rolled out "ready-by-date" for the US and CA markets, an initiative that simplfies the process to communicate the "pick-up date" to suppliers for non Vendor Delivered POs.

### Planned (Next Sprint)
[Transfer Order and Transport Management Rollout]
Canada TMS rollout and hyper care (global tooling standarization). 

[Legacy Ordering Tool Deprecation] 
Implement email customization for multi template/language markets to provide a replacement for onr of the remaning OT features in use. Investigate "Ice Safety Stock" management replacement for the US market, an edge case business use case that's one of the last blockers for OT deprecation.

[KTLO & Continuous Improvements]
Prepration for Ready-to-Ship rollout to automate "SIMing process" by putting a PO on load using the data suppliers provide via E2Open.

### Key Learnings
We have uncovered some of the legacy DWH assets are still using OT (tapioca) APIs  and have  usecases that need to be deprecaeted. We are preparing a wide communication together with Data Analytics team to remind about the upcomming dprecation and provide some recomendation on alternative data assets.

**Demo:** Bi-Weekly Demo : Ordering - 2026/02/02 13:25 GMT - Recording

---

## Globalization of Procurement Tooling
**Tribe:** Plan & Procurement
**Mega-Alliance:** Ops
**Squad Lead:** PO: Ouessanne Dobe 
EM: Alireza Saadat

### Squad KPI
% of substitutions entered through the system

### KPI Movement
W05: 1/1 in Arizona
W06: 1/1 in Arizona

### Delivered (This Sprint)
[P500 Substitutions Execution Flow]
We officially rolled out the in-week subs platform for Arizona and we created the first substitutions live. We also worked on some UX improvements to ease and fasten the ability for procurement to submit a sub. By the end of the sprint, we will consider the first version of the platform done.

### Planned (Next Sprint)
[P500 Substitutions Execution Flow]
We will focus on hypercare, continuous improvements tasks such as creating runbooks. We will  evaluate the team capacity and probably send 1 FE to support touchless ordering.

**Demo:** In-week sku substitution procurement platform final demo - 2026/02/02 16:20 CET - Recording

---

# Production

## 3P
**Tribe:** Production
**Mega-Alliance:** Ops
**Squad Lead:** PO: Avishek Ghosh
EM: Petr Archakov

### Squad KPI
Production Planning Minutes per recipe served (3PMR)

### KPI Movement
None. Movement to be expected next Sprint

### Delivered (This Sprint)
- Completed user acceptance test for freshstart launch in Canada
- Completed go-live in US P500
- Lauched consumption and production strategy selection to allocate recipes to new production methods
- Expanded from 4 combination of production methods across 300 recipes on average to 10 combindation of production methods across 3000 recipes (10X scale)

### Planned (Next Sprint)
- Reduce time spent on production plan change manager by 60%+ -> This entails several tasks connected to improving the menu and sku information consumers, improving the latency of our services, improving the UX of the change manager and removing unnecessary clutter for the end users

### Key Learnings
- Our products need to address several tech challenges internally to provide reliable user experience at this scale. We have detected 1.4 Billion change items lines across just one US market due to menu expansion. Our systems are expected to scale must more over the next months

---

## Network Planning
**Tribe:** Production
**Mega-Alliance:** Ops
**Squad Lead:** Avishek Ghosh

### Squad KPI
Logistics TCO

### KPI Movement
no movement since last sprint

### Delivered (This Sprint)
KTLO

### Planned (Next Sprint)
Continued transfer of the product to DNET

### Key Learnings
KTLO

---

## Fulfillment Demand Planning
**Tribe:** Production
**Mega-Alliance:** Ops
**Squad Lead:** PO: Avishek Ghosh
EM: Petr Archakov

### Squad KPI
Planned vs Actual DC & Production Day Allocation (Measured 4WO)

### KPI Movement
no movement since last sprint

### Delivered (This Sprint)
- Completed the Home Page of FDA as per the UI wireframe handover from the Enterprise UX team. 
- Users can now run the Assembly allocation model with hardcoded constraints/capacity.

### Planned (Next Sprint)
- Continue with the development of FDA as per the final agreed upon UI.

### Key Learnings
- An end to end strategy for integrated flight planning is required along with deligation of POC for all the main capability: Scope, Optimization, Visualization, Integration and Steering. A document in progress to consolidate the strategy.

---

## Deployment & Innovations
**Tribe:** Production
**Mega-Alliance:** Ops
**Squad Lead:** PO: Willem Vandeput

### Squad KPI
LMPB for low runner (kit type demand less than 100 per day)

### KPI Movement
none yet, next impact measurable after FS CA go-live in W7

### Delivered (This Sprint)
1. configuration & UAT of FreshStart Canada
2. FlexSim FS CA analysis complete (Report & Model Description)

### Planned (Next Sprint)
1. FreshStart MVP Edmonton (CA) UAT completion & Go-Live  
2. FreshStart SPAC throughput trial in Moss (NO)
3. FlexSim: FreshStart SPAC AU simulation (comparisson of trolley capacities)

---

## Production
**Tribe:** Production
**Mega-Alliance:** Ops

### Squad KPI
AVG Picks per Person per Hour

### KPI Movement
N/A

### Delivered (This Sprint)
N/A

### Planned (Next Sprint)
N/A

---

## Production
**Tribe:** Production
**Mega-Alliance:** Ops
**Squad Lead:** PO: Abdul Saboor
EM: Sebastian Wilhelm

### Squad KPI
Enabling Build to Order Production

### KPI Movement
none yet, Impact measurable after FS CA go-live in W7

### Delivered (This Sprint)
1. End to End testing of FreshStart development on demo line in Saarbrucken Office
2. Bug Fixes & Enhancements for FreshStart based on internal testing in Saarbrucken Office & UAT in Canada 
2. Enabling setup for UAT of FreshStart in Edmonton (including setting PCS UAT Instance)

### Planned (Next Sprint)
Discovery for development of Booklet Extension for Cluster Picking in Bjuv
Optimisation for ESL Integration to remove unnecessary ESL updates on Flexi Kitting Lines

### Key Learnings
Having a demo setup with all hardware and software components in office allowed thorough testing, identification of flaws . It also allowed us to implement fixes and validate them live in the demo setup, allowing for an operation ready solution to be shipped out from the beginning.

---

## Platform
**Tribe:** Production
**Mega-Alliance:** Ops

### Squad KPI
Ensure 99% SLA adherence

### KPI Movement
None

### Delivered (This Sprint)
1. ESL Integration rollout Spain
2. Reworked SOPs for maintenance technicians for server upgrades based on feedback
3. Rework and reconfig of Saarbrücken testsetup for FreshStart Testing         
4. Injection station setup for SE Market (Booklet CP)
5. Scoped additional namespace for multi service deployment in on-site k3s cluster

### Planned (Next Sprint)
1.UAT testing support and setup for Edmoneton Fresh start 
2.Scales inference system transition to k3s 
3.KTLO Package installation

### Key Learnings
Need to work on backlog refinement as many tickets were poorly defined in their acceptance criteria. Immediate step to enforce atleast 3 criterias per ticket

**Demo:** N/A

---

## Installs
**Tribe:** Production
**Mega-Alliance:** Ops
**Squad Lead:** EM: Patrick Schuh

### Squad KPI
Install Squad keeps the average installation rating 9 out of 10

### KPI Movement
No movement. no feedback from Freshstart Canada yet latest data still from 2025 Overall Installation Rating 2025

### Delivered (This Sprint)
1. Freshstart installation in Canada PT-PI visit report CA, Edmonton 25.01.2026

### Planned (Next Sprint)
1. Preperation work for DeKas

**Demo:** Pictures from Freshstart installation 01.2026 - CA,Edmonton

---

# RTE Manufacturing

## RTE Production
**Tribe:** RTE Manufacturing
**Mega-Alliance:** Ops
**Squad Lead:** SL: Jan McSparin
PM: Melissa Minor

### Squad KPI
Plan Attainment % (plan vs actual deviation) to reduce waste and cost per meal

### KPI Movement
N/A

### Delivered (This Sprint)
Stabilize Factor Operations Cost
- Allow target reductions for certain WMS statuses  - 10%

Factor EU Verden Launch
 - Completed MPT/ET integration with Manufacturing Volume Allocation Service and other EU configurations - 60%

KTLO 
-  resolved an SMP equipment mapping issue, improved expiration data sync reliability, feature flag maintenance - 30%

### Planned (Next Sprint)
Improve Factor Quality
- Transition planning constraint 'Earliest Plating Day' to 'Earliest Cook Day' for granular shelf life planning and scheduling flexibility (when MSKU is ready with shelf life)  -  25%

Stabilize Factor Operations Cost
 - Begin Sub-Recipe Batching, enabling large batches of cooked components to be allocated across multiple meals  -  45%

KTLO 
-  Support EU E2E testing, ET data investigation, update ET runbooks - 30%

### Key Learnings
Streamlining team processes will help us deploy completed code to production more efficiently, and eliminate a bottleneck that was impacting overall squad velocity.

**Demo:** RTEP Internal Sprint Demo - 2026/01/30 12:56 MST - Recording

---

## RTE Services
**Tribe:** RTE Manufacturing
**Mega-Alliance:** Ops
**Squad Lead:** SL - Reid MacTavish
PM - Court Bell

### Squad KPI
# of recipes and sub-recipes supported (for menu expansion)

### KPI Movement
80 recipes on W06 menu (+1 from W04)

### Delivered (This Sprint)
Improve Factor Quality
- NatureIn preservative removed from over 3000 auto-created manufactured SKUs for US culinary team to begin reviewing and testing for a NatureIn free menu  - 50% 

Factor EU Verden Launch
- Fixed bugs found in testing Manufactured Volume Allocation Service integrations with upstream data sources for Factor EU launch readiness - 25%

KTLO 
- Increased service stability and memory cache loading efficiency - 25%

### Planned (Next Sprint)
1. Consuming ODL data for all 5 Factor EU markets to be used as a data source for the manufacturing volume allocation service 
2. Downstream manufacturing volume allocation service integration testing for Factor EU

### Key Learnings
Loading MSKU's cache asynchronously reduced service start up time from 4 minutes to 16 seconds. 

Running NautreIn removal script to duplicate all active MSKUs locally first, along with updated MSKU's DB to be read only optimized saved time and managed risk for such a large bulk data update.

**Demo:** to be added Friday

---

## YouFoodz and Factor B2B
**Tribe:** RTE Manufacturing
**Mega-Alliance:** Ops
**Squad Lead:** Michael Frost

### Squad KPI
Factor B2B growth of 10x YOY

### KPI Movement
- Factor B2B - Week on Week $55k down from $57k 
- Youfoodz B2B - Week on Week $2.1m up from $2.0m
- Youfoodz Care - Week on Week $15k from $14k

### Delivered (This Sprint)
Factor B2B Subscription
- APIs for front end complete - 25%
- Product sync from HF from CCM, PCS, OSCAR ready price integration 20%
- TIS Tracking data sync and APIs - complete at the order level - 20%

Youfoodz EDI
OTR onboarding - product mapping and pricing in testing - 25%

Recipe Life Cycle Management
- Point74 Recipe Professor approval obtained - 10%

### Planned (Next Sprint)
1. Build B2B order creation subscription engine
2. Investigate and integrate item level TIS tracking from HF systems into Shopify
3. Progress Youfoodz EDI for OTR and Metcach
4. Design and commence Point74 Recipe LCM into Youfoodz systems

### Key Learnings
TIS tracking will need to be at a line item level and not at the order level to be able to track when orders have multiple boxes in Shopify

---

# Shopping Foundation

## Search & Personalization
**Tribe:** Shopping Foundation
**Mega-Alliance:** Consumer
**Squad Lead:** EM : Amey Patil Interim 
(Later: Bartosz Raciborski)
PM : Tushar Raina

### Squad KPI
Add to cart rate from top 15 search results

### KPI Movement
No movement

### Delivered (This Sprint)
1. Github repositories were created for HF Integration Layer
2. Github repositories were created for MXP
3. Catalog contract between HF Integration Layer & MXP has been 90% completed
4. Agreement with Reliability Platform team was reached to use the main-it account to deploy MXP services
5. ADR has been updated with latest decisions around integration layer &  MXP

### Planned (Next Sprint)
1. MXP services setup & deployed in HF infrastructure
2. Search-adapter-service setup deployed
3. Catalog consumer & Indexing APIs are integrated
4. Search available through demo UI based on HF Catalog & MXP solution

### Key Learnings
1. Tech Discussions have been helpful
2. Tasks can be divided into smaller tasks
3. Need faster decisions

**Demo:** Shopping Foundation Tribe Demo - 2026/01/30 16:52 CET - Recording

---

## Cart
**Tribe:** Shopping Foundation
**Mega-Alliance:** Consumer
**Squad Lead:** EM: (A-Dos) Arbaaz Dossani (Temp for Tales Padua on Pat. Leave)
PM: Xavier Sinclair Vale-Buisson

### Squad KPI
Cart Service Adoption Rate

### KPI Movement
Target: 100%
Actual: 58.2%
Movement: 23.2%

### Delivered (This Sprint)
Global Cart Service Migration: Continued the architectural migration of the Cart Service to its own authoritative data layer, successfully rolling out across remaining European and AU/NZ markets. This refactor enables faster meal selection and eliminates potential data errors for our customers.

### Planned (Next Sprint)
1. Complete Cart Service roll out to all remaining markets (YE still pending meal-plan handler fix)
2. Release Cart Read API across all markets 
3. Release Post-lock change for P500 use, which will allow local markets to switch recipes without sending manual requests to the Cart squad

### Key Learnings
1. Load testing for save requests not just reading  in the future
2. Support engineer process to be reviewed to deal with high number of requests

**Demo:** Shopping Foundation Tribe Demo - 2026/01/30 16:52 CET - Recording

---

## Shopping Platform
**Tribe:** Shopping Foundation
**Mega-Alliance:** Consumer
**Squad Lead:** EM: Maxime Valy
PM: Priyank Khanna

### Squad KPI
Q1 only: Latency [key customer actions] (Mobile)

### KPI Movement
We are the in process of creating a executive dashboard with all key e2e actions / journey stats but based on a spot analysis using the most up date Honeycomb stats for Jan 2026 for all markets, we get

True mean latency - P95 (all customer actions): 1141 ms (src)
-------------------------------------------------------------- 
Worst: Get_Home_Deliverues: 1803 ms
Best: Get_Delivery_Dates: 394 ms
----------------------------------------------------------
SLOs: In progress

### Delivered (This Sprint)
Although this was a KTLO heavy sprint (~50% bandwidth), we: 
1. [P500] Complete dev for new append feature for CCM Bulk upload to support non US markets 
2. [P500] Completed discovery of next stage latency improvements for P500 and beyond
3. [P500] Groundwork to improve performance observability by market & P500 segment link

### Planned (Next Sprint)
P500
1. Cart State Optimisations: Develop a way to load only selected products and eliminate unnecessary menu fetches.
2. Store latency reduction by X ms by further Shoppable Product optimisations and decoupling BFF-CMS
3. Add country-level latency visibility in Grafana/Honeycomb
---------
Non P500
4. Evaluation of MXP/Grid Dynamics from the POV of catering to Filters / Categories use cases

### Key Learnings
- Figure out a way to eliminate support channel noise in favor of meaningful work. Triage as early as possible and say NO. KTLO took about 50% of the team's bandwidth
- Get visibility on 'validated' observabaility stats by key customer actions asap and set SLOs (we can't improve if we cant measure)

**Demo:** Shopping Foundation Tribe Demo - 2026/01/30 16:52 CET - Recording

---

## Cross Selling and Subscription Flexibility
**Tribe:** Shopping Foundation
**Mega-Alliance:** Consumer
**Squad Lead:** PM: Deo Nathaniel
EM:
(A-Dos) Arbaaz Dossani

### Squad KPI
% Cross-sell & OTP Contributions to Gross Revenue

### KPI Movement
KPI Still in Development

### Delivered (This Sprint)
1. [Xsell] Complete development for Landing page
2. [Xsell] Complete development for Enrollment journey meal selection

### Planned (Next Sprint)
1. [Xsell] Complete development for Enrollment journey checkout
2. [Xsell] Ticket breakdown for Active journey
3. [OTP KTLO] Launch OTP Easter Box Campaign

### Key Learnings
1. AI workflow - Cross-Sell specific context - More issues building UI so we will use and iterating the general context
2. AI workflow - MCP Mobile tool to self validate UI changes with FIGMA
3. OTP Recipe & menu setup can be different per market, and this required more alignment with local team than expected

**Demo:** Shopping Foundation Tribe Demo - 2026/01/30 16:52 CET - Recording

---

## Customer Service Experience
**Tribe:** Shopping Foundation
**Mega-Alliance:** Consumer
**Squad Lead:** EM: Amey Patil
PM: Shishir Mishra

### Squad KPI
Self Service Rate

### KPI Movement
Global Self-service rate: 49.33%
Change from last sprint: +0.78

### Delivered (This Sprint)
Chatbot:
1. Chatbot launch in Factor Germany (50% population)
2. Tech evaluation of Sierra started and aim to conclude it next sprint
3. Ability to experiment new use cases on chatbot is available
CERT:
1. Photo upload feature is built and awaiting translations to go live
2. CERT configuration has been standardized across markets for HF, EP, GChef, and CP

### Planned (Next Sprint)
Chatbot:
1. Sierra Tech evaluation will be complete, paving way for cost comparisons, and POCs with actual integrations 
2. Continuation of customer conversation from chatbot to Genesys is nearly done and will be rolled out in upcoming sprint
3. System prompt optimization to use only necessary tokens and face less 'unexpected error' scenarios due to throttling issues
CERT:
1. Photo upload rollout via an experiment
2. Decision on CERT in GoodChop after reviewing the results of the experiment
3. CERT in Chatbot discovery to begin

### Key Learnings
1. If we continue with AWS bot, we can use a beta feature from Amazon Science Team for model and prompt evaluation.

**Demo:** Shopping Foundation Tribe Demo - 2026/01/30 16:52 CET - Recording

---

## Agent Experience
**Tribe:** Shopping Foundation
**Mega-Alliance:** Consumer
**Squad Lead:** EM: Amey Patil
PM: Shishir Mishra

### Squad KPI
KPI Still in Development

### KPI Movement
KPI Still in Development

### Delivered (This Sprint)
Compensation:
1. Workshop with GCX was done to understand new model for calculation and tasks identified to confirm the feasibility of the model by identifying data sources
Agent Tool:
1. Cancellation for initial order was integrated to fix the broken experience for customers after changes to downstream APIs
2. Added customer name to shipping address to resolve downstream discrepancy of incorrect name being printend on the box-sticker
3. Activity log enhanced to include more information on meal swaps

### Planned (Next Sprint)
Compensation:
1. Investigate and confirm the feasibility of change in compensation calculation proposed by GCX
Agent Tool:
1. Continue resolving service desk issues

**Demo:** Shopping Foundation Tribe Demo - 2026/01/30 16:52 CET - Recording

---

# Shopping Journey

## Customer Profile
**Tribe:** Shopping Journey
**Mega-Alliance:** Consumer
**Squad Lead:** EM: Abbas Ali Awan
PM: Wellney Yarra

### Squad KPI
[HF US] Profile Completion Rate

### KPI Movement
Target: 20%
Actual: 14.97%
Movement: n/a since metric was just established

### Delivered (This Sprint)
1. Tracking events for V1 of Food profile page 
2. Profile completion rate is now available as a metric
3. Gradual rollout of the new address form, starting with Sweden

### Planned (Next Sprint)
1. Bump up rollout traffic of Food Profile v1 to 100% at the start of the sprint
2. Finish development of Food profile v2 at the end of the sprint, allowing customers to add more data points to their profile (cuisine, dish type, flavors, proteins, etc.). Start gradual rollout.
3. Integrate profile completion metric into statsig to unlock experimentation
4. Rollout the new adddress form to more markets

### Key Learnings
14% of customers who were exposed to the Food profile page found and interacted with the page even without being nudged, signaling the strong need for customers to share their preferences (especially hard restrictions) with us.

Out of those interacting with the page, ±35% of them indicated at least one exclusion.

**Demo:** 2026-01-30

---

## Menu Discovery
**Tribe:** Shopping Journey
**Mega-Alliance:** Consumer
**Squad Lead:** EM: Brandon Donato-Long
PM: Elisa Marku

### Squad KPI
Orders Confirmed w/ Meal Selection

### KPI Movement
Target: 65%
Actual: 62%
Movement: n/a (experiments will start this sprint)

### Delivered (This Sprint)
1. Personalized Shopping Experience 'For You' V1.0 - Launching in Week 6
2. Macro nutrient values displayed in RTE small Cards - Launching in Week 6
3. P500 Client side schema updates to reduce latency on graphql requests.
4. 2x Snowplow Events on web for "filter applied' personalization signals

### Planned (Next Sprint)
1.) Chefs Plate Elysium Launch 
2.) Search UI - Categories & Search Bar variants.

### Key Learnings
1. A large amount of KTLO work being done. Of the 31 tickets completed, 8 of them (25%) were bugs. 
Two high priority bugs were present for the last 2 releases and these bugs could have been caught easily by automated testing. 

- Learning: More time needs to be spent working on automated integration testing. This 25% does not include time spent investigating.

**Demo:** 2026-01-30

---

## Merchandising & Shopping Guidance
**Tribe:** Shopping Journey
**Mega-Alliance:** Consumer
**Squad Lead:** EM: Shruti Patil
PM: Laura Mneimneh

### Squad KPI
Net AOV proven from experiments

### KPI Movement
No movement - development on experiment targeting AOV will start this sprint

### Delivered (This Sprint)
1.  Implementation of New Order Cards variation 2
2.  UI2 readiness for ChefsPlate on Android

### Planned (Next Sprint)
1. Homepage Experiment launch
2. Chefsplate Elysium launch 
3. Extra meal price communication in the Shopping Guidance (for AOV)

### Key Learnings
- we discovered issues on small screens with the quick action pills on the homepage variation 2 and updated the logic for them to have a dynamic width so that they don't wrap on 2 lines when the number of characters is long

**Demo:** 2026-01-30

---

## Feedback
**Tribe:** Shopping Journey
**Mega-Alliance:** Consumer
**Squad Lead:** EM: Luis Eduardo Talavera Rios
PM: Sandra Rozario

### Squad KPI
Recipe Response Rate

### KPI Movement
Recipe response rate = No of recipes rated/No of recipes shipped
W01-2026: 6%
W03-2026: 7.0%

### Delivered (This Sprint)
1. Quick comments starters (bubble options) in Past Deliveries completed on iOS and will be launched by 6th Feb. Android work is in progress and the android release will follow next week.
2. Completed the work for UI2 readiness for ChefsPlate
3. The frontend work to surface 'users’ favorite recipes' (highly rated and hearted) via widgets and nested pages in the store is complete. Over the coming weeks, we’ll focus on integrating the backend with the frontend. This is expected to create a positive feedback loop by demonstrating the value of rating, supporting faster meal selection, and ultimately increasing rating engagement over time.
4. Prep work on Backend for showing Users favorite recipe (related to point 3)

### Planned (Next Sprint)
1) Launch quick comments in Past Deliveries for android. 
2) Complete the work to show users recipe ratings and list of favorite items in a widget in storefront. 
3) Start the work for showing quick comment starters/ bubbles on the recipe rating nudge in apps.

### Key Learnings
We discovered some edge cases for why customers do not see the nudge (e.g. they cancel) and updated our logic accordingly

**Demo:** 2026-01-30

---

