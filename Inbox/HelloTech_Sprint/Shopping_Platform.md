---
type: hellotech_sprint_report
squad: Shopping Platform
tribe: Shopping Foundation
mega_alliance: Consumer
synced_at: 2026-02-04T13:55:23.907500
source: HelloTech Every Other Week Squad Sprint Report
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