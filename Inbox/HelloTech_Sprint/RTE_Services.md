---
type: hellotech_sprint_report
squad: RTE Services
tribe: RTE Manufacturing
mega_alliance: Ops
synced_at: 2026-02-04T13:55:23.907561
source: HelloTech Every Other Week Squad Sprint Report
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