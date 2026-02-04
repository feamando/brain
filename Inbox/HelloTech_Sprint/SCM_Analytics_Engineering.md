---
type: hellotech_sprint_report
squad: SCM Analytics Engineering
tribe: Operations Data & Decisions
mega_alliance: Ops
synced_at: 2026-02-04T13:55:23.907592
source: HelloTech Every Other Week Squad Sprint Report
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