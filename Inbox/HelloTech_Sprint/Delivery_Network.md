---
type: hellotech_sprint_report
squad: Delivery Network
tribe: Logistics
mega_alliance: Ops
synced_at: 2026-02-04T13:55:23.907570
source: HelloTech Every Other Week Squad Sprint Report
---

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