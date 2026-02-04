---
type: hellotech_sprint_report
squad: Labor Management
tribe: Labor Planning, Management, and Analytics
mega_alliance: Ops
synced_at: 2026-02-04T13:55:23.907565
source: HelloTech Every Other Week Squad Sprint Report
---

## Labor Management
**Tribe:** Labor Planning, Management, and Analytics
**Mega-Alliance:** Ops
**Squad Lead:** SL: Niharika Aggarwal
PM: Nikhil Ranka

### Squad KPI
Worked Minutes Per Box (Worked MPB)

### KPI Movement
Production MBP HF/GC [US]: 13.9% increase (14.1 -> 16.1)
Worked MPB [BARN]: 4.6% decrease (18.2 -> 17.4)
Worked MPB [WM]: 9.8% decrease (15.5 -> 14)

(We are working with Product Analytics to track Worked MPB for the US to accurately report KPI movement in all markets with our Labor Tracking toolkit)

### Delivered (This Sprint)
Reducing Labor Cost and Labor Minutes per Box (60%)
- Evaluated Dematic (Warehouse Picking System) integration readiness for Scan2Job in BARN DC to enable improvement in labor productivity - 20%
- Improved Attendance Forecasting Model reliability by resolving data quality issues to enable UAT for accurate labor shift staffing - 40%

Launch Factor Verden Facility (10%)
- Scoped out work required to rollout Scan2Job for Factor Verden launch to enable improvement in labor productivity and planning accuracy - 10%

KTLO - Security, Support & Maintenance (30%)
- Secured access to our S3 buckets to be compliant with HelloFresh Secuity guidelines
- Added alerts for operational excellence
- Reduced vulnerabilities in Github repos

### Planned (Next Sprint)
1. Enable Verden data on Scan2Job to support the Verden Launch
2. Successful UAT for improved Attendance Forecasting integration with Short Term Planning Toolkit [MK] 
3. Integrate Scan2Job with Dematic in BARN and enable UAT

### Key Learnings
We are getting slowed down on multiple fronts due to data unavailability from upstream teams. For eg:
1. INTL Opex team is still working on providing a full list of associate_id to Dematic RFID mapping (missing mapping for 19 RFIDs) - we've escalated it and the responsible team is prioritizing it.
2. US Asset Protection team hasn't been able to provide required data in the Lenel dataset for us to identify day labor to effectively track the ~10-20% day labor across Factor and Meal Kit sites - US Opex has escalated the issue but no progress has been made yet.
3. FreshField Project (3010 to Workday Migration) is yet to provide us with a complete data set of employees for a day and shift. We have escalated the issue but no progress so far.

**Demo:** Demo - Jan 29th '26