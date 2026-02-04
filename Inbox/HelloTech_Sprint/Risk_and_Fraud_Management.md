---
type: hellotech_sprint_report
squad: Risk and Fraud Management
tribe: Payments
mega_alliance: Growth
synced_at: 2026-02-04T13:55:23.907689
source: HelloTech Every Other Week Squad Sprint Report
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