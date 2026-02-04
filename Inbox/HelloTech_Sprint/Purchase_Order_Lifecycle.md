---
type: hellotech_sprint_report
squad: Purchase Order Lifecycle
tribe: Plan & Procurement
mega_alliance: Ops
synced_at: 2026-02-04T13:55:23.907521
source: HelloTech Every Other Week Squad Sprint Report
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