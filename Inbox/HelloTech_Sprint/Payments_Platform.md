---
type: hellotech_sprint_report
squad: Payments Platform
tribe: Payments
mega_alliance: Growth
synced_at: 2026-02-04T13:55:23.907686
source: HelloTech Every Other Week Squad Sprint Report
---

## Payments Platform
**Tribe:** Payments
**Mega-Alliance:** Growth
**Squad Lead:** Zeeshan Akram Gangadharan Khoteeswarun

### Squad KPI
Payment Approval Rate

### KPI Movement
Actual: 94.81% (W04/05)
Compared to 2 sprints ago: +1.81pp (from 93.12% W52/01 to 94.81% for W04/05)
-------
Insights:
Recurring charges AR and dunning ship rate outperforming YoY. Fully rolled out markets on ProcessOut from previous sprint performing around 1.5pp higher for recurring AR vs. last year.

### Delivered (This Sprint)
Sprint Focus: Progressing payment-order decoupling thorugh rollout of POPS. Enabling the further rollout of ProcessOut by closing identified feature gaps. 

1. LU has at least one payment run and rerun through POPS
2.Started sending additional customer Data to Processout (email, name, and billing address)  with the goal to improve AR through ProcessOut
3. US & FJ are running 50% of new cards via ProcessOut.
4. POC for frictionless 3DS flow through Processout SDK integration

### Planned (Next Sprint)
Sprint Focus: Progress on Payments-Order Decoupling by moving additional flows to Payment Orchestrator and POPS.

1. Rollout C@C through Payments Orchestrator - This will help to move all flows through PO which reduces our technical complexity
2. Finalize current LU runs in POPS - LU will become independent of Process Orchestrator 
3. Use PTS as a source of truth for tokens in smaller countries - rollout this after the bug fix

### Key Learnings
1. Tasks without estimates like bugs/investigation needs to be tracked differently
2. With 5 different rollouts currently handled within team, we need to better manage and visualize it