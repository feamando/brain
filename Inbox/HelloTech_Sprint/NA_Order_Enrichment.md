---
type: hellotech_sprint_report
squad: NA Order Enrichment
tribe: Order Enrichment
mega_alliance: Ops
synced_at: 2026-02-04T13:55:23.907550
source: HelloTech Every Other Week Squad Sprint Report
---

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