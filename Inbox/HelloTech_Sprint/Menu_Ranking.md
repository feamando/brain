---
type: hellotech_sprint_report
squad: Menu Ranking
tribe: Menu to Content
mega_alliance: Ops
synced_at: 2026-02-04T13:55:23.907539
source: HelloTech Every Other Week Squad Sprint Report
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