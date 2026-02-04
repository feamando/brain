---
type: hellotech_sprint_report
squad: Menu to Content
tribe: Top 6 volume regions for all brands where we predict demand: Wk03 Vs Wk 05
UK - 4.1 PPTs reduction
DACH - 1 PPTs increment
CA - 2.5 PPTs reduction
BENELUX - 0.3 PPTs reduction
FR - 1 PPTs Increment
AUNZ - 4.4 PPTs reduction
mega_alliance: Ops
synced_at: 2026-02-04T12:25:20.949517
source: HelloTech Every Other Week Squad Sprint Report
---

## Menu to Content
**Tribe:** Top 6 volume regions for all brands where we predict demand: Wk03 Vs Wk 05
UK - 4.1 PPTs reduction
DACH - 1 PPTs increment
CA - 2.5 PPTs reduction
BENELUX - 0.3 PPTs reduction
FR - 1 PPTs Increment
AUNZ - 4.4 PPTs reduction
**Mega-Alliance:** Ops

### KPI Movement
Demand Forecasting & Planning

### Delivered (Last Sprint)
DS: Zlata Tanovic
PM: Shahab Syed

### Planned (Next Sprint)
SKU forecast variance from actuals measured as Weighted Absolute Percentage Error (WAPE)  at 1 Week Out from target week

### Key Learnings
[Forecasting Model Improvements]
1. Club NDD & BOLT orders forecast into one logical unit when sharing with downstream teams, to enable improvement in SCO projections (reported for UK, valid for UK+IE+DACH, scoping validity for all INTL markets).
2. Replace MBT targets with new conversions data in swap ratio calculations and splitting tool logic (All INTL markets).
3. Improve swap ratio predictions by switching to actual customer selections every Wednesday (all INTL markets).
4. Identify structural changes in the model as well as additional features, that will improve F4L model predictions (All INTL markets)
5. Identify optimal solution for incorporating  the launch of exclusive slots for Savers Plan (AUNZ)

**MBL Initiative:** [Forecasting Model Improvements]
1. [Box Forecast] Completed development & testing of model for predicting total conversions (new customers) for all markets.
2. [Recipe Uptake Forecast] Personalization integration in INTL: Identified 12/13 sources needed for creating historical defaults and raised request with Atlan team for support on 1/13.

[KTLO & Continuous Improvements]
1. Updated code to ingest real recipe_family values instead of hard coded strings which were causing occasional empty/low forecasts (all INTL markets)
2. Improved F4L prediction model by eliminating data constraints that were leading to suboptimal handling of the existing conversions (all INTL markets)
3. Identified root cause for under forecasting of modular slots (duplicate slot index mapping in upstream data sources ). Deployed fix that successfully improved forecast for W09 & beyond (AUNZ).
4. Investigated & resolved the issue of F4L predictions being the same as customer selections. (reported for FR, solved for all INTL markets)
5. Resolved issue of failing API calls due to empty zip codes in SFS table (All INTL markets).
6. Resolved DC encoding misalignment in source tables that caused non eligible slots to be forecasted for a DC (AUNZ)

**Sprint Health:** - We introduced a weekly firefighter program, where every week 1 team member will dedicatedly man the support requests channel. This new  setup is working well and has helped increase productivity: it allows one person to work fully on KTLO & tech debt , while the rest of the team can concentrate on new developments

- Free For Life under forecasting caused by proxy data on F4L conversions. We learned that more precise high quality data existed and were able to improve the forecast by around 5pp WAPE in all markets

- An ensemble of two independent total conversions models outperformed either of the two in almost all markets, by around 2pp WAPE (for the new conversions). This is an input to our total box demand model.  We should continue exploring ensembles for model improvements.

- Code changes deployed near to the weekend require additional focus on impact evaluation: Inventory Planner tool faced a downtime due to unavailability of forecast, reported on Friday 4:55 PM. While we aligned with team to deploy a solution on Monday as they had a workaround, we learnt that in future this could lead to huge impact if the issue is unreported over the weekend.