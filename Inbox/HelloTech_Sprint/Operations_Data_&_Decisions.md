---
type: hellotech_sprint_report
squad: Operations Data & Decisions
tribe: Normal Menu | High Loyalty 6WO WAPE: 46% (-3%)
Normal Menu | Low Loyalty 6WO WAPE: 68% (-0%)
mega_alliance: Ops
synced_at: 2026-02-04T12:25:20.949577
source: HelloTech Every Other Week Squad Sprint Report
---

## Operations Data & Decisions
**Tribe:** Normal Menu | High Loyalty 6WO WAPE: 46% (-3%)
Normal Menu | Low Loyalty 6WO WAPE: 68% (-0%)
**Mega-Alliance:** Ops

### KPI Movement
Data Science

### Delivered (Last Sprint)
EM: Andrew Kim

### Planned (Next Sprint)
Forecast accuracy

### Key Learnings
- Further testing around LLM based features to see if we can create some features that suggest why certain recipes don't do well despite being highly recommended (Like Greek Feta Meatloaf with Veggie Jumble)
- Discussions with personalization on potentially locking Penguin / Profile ranker 6 weeks out to minimize volatility from non-live --> live week
- Check on volatility of profile-ranker recommendations from 6WO --> 5WO once data starts publishing in non-live weeks

**MBL Initiative:** - Created / tested new LLM based features for the model that can tell us whether certain recipes might be more/less polarizing for the american taste palate. Very minor to no change for high loyalty accuracy.
- Updating model run modes to include a new accuracy mode that will more consistently track model accuracy over time, while removing noise like region / menu changes.

**Sprint Health:** - We will be splitting up our run modes in ML Flow for better tracking and saving as we've aggregated too much into the same experiments / model names.