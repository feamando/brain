---
type: hellotech_sprint_report
squad: Client Platform
tribe: Consumer Foundation
mega_alliance: Consumer
synced_at: 2026-02-04T13:55:23.907470
source: HelloTech Every Other Week Squad Sprint Report
---

## Client Platform
**Tribe:** Consumer Foundation
**Mega-Alliance:** Consumer
**Squad Lead:** EM: Wellington Lima Freire
PM: Priscila Koeck Machado

### Squad KPI
The Platform Unification Ratio (PUR) is a metric that tracks progress toward completing the migration to a fully React Native codebase. It is a ratio calculated by dividing the number of React Native Pull Requests (PRs) by the total number of mobile PRs (Android + iOS + RN).

### KPI Movement
Target by end of Q1: 80%
Target by end of Q2: 95%
Actual: 68.87%
Compared to Last Month: +15.2 pp (from 53.71% to 68.87%)

We saw a big increase due to the use of AI and expect this number to keep increasing until the end of Q2.
Link for report containing auxiliar metrics

### Delivered (This Sprint)
Around. 30% of our team's capacity was spent in managing the mobile releases due to lack of e2e automation:

1. Ensured the mobile releases for our core brands were successful, including auditing changes that were introduced after the release's cutoff.
2. Investigated and identified possible causes for the apps submission rejection in ChefsPlate/GreenChef/EveryPlate.
3. Identified and corrected the skipped releases on Youfoodz.

Beyond that, we made significant progress in migrating the Cash Credit Balance History and Account Details screens to RN. However, we didn't get to a production-ready state with them.

More info about this sprint can be found here.

### Planned (Next Sprint)
1. Make the mobile releases hands-free again: finish the planned improvements, create and share a runbook with the teams about how  to handle hotfixes, and udpated documentation for the e2e process.

2. Cash Credits Balance History screen migrated to RN is enabled in production

3. Profile Tab + Account Details/Personal Info migrated to RN is enabled in production

(Pending: decision on whether we will prioritise RAF and what we plan to accomplish)

### Key Learnings
1. GenAI with spec-machine is very promising. We will adopt it in our SDLC to bring consistency to how we use AI for development, and increase the team's productivity (refer to the last segment of the linked demo to see the achieved results).

2. We have a significant "Bus/Truck Factor" in the mobile releases process: Although we were already prioritizing and working to fix and improve the process, the absence of one team member in this sprint showed us how much the knowledge is siloed. We will double down on our effort in the next sprint to complete the changes required to make the mobile releases hands-free again, and also improve our documentation to support with offloading parts of the process from our team.

**Demo:** The recording was not processed an IT ticket was created for investigation.