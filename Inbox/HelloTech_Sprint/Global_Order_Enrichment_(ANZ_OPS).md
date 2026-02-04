---
type: hellotech_sprint_report
squad: Global Order Enrichment (ANZ OPS)
tribe: Order Enrichment
mega_alliance: Ops
synced_at: 2026-02-04T13:55:23.907553
source: HelloTech Every Other Week Squad Sprint Report
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