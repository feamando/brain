---
type: hellotech_sprint_report
squad: Search Optimization
tribe: AdTech
mega_alliance: Growth
synced_at: 2026-02-04T13:55:23.907665
source: HelloTech Every Other Week Squad Sprint Report
---

## Search Optimization
**Tribe:** AdTech
**Mega-Alliance:** Growth
**Squad Lead:** EM: Michael Mayer
PM: Şevki Argalioğlu

### Squad KPI
% Paid Search CAC deviation (guardrailed by BP planned volume)

Secondary:
- Autopilot uptime (%)
- SEA spend covered (%)

### KPI Movement
No movement due to autopilot was off during the previous sprint

### Delivered (This Sprint)
1. Prototype for the campaign level bidding has been released for testing in the next sprint
If the test result proves success, the default bidding layer for NB markets will be set to campaign level. This unlocks scaling AGE for 10 markets.

2. Laid out the foundation of monitoring and alerting system
This allows to start implementing the monitoring aspects which influences the autopilot uptime (%)

### Planned (Next Sprint)
1. Run the campaign level bidding test in at least one market (DE / GB)
2. Start tracking the CAC achievement through monitoring & alerting and disengage trigger for the autopilot
3. RFC for Global config that enables configuring activation of AGE for the new markets

### Key Learnings
When Google Ads updates a dimension, it creates a new record & persist the old one. This affects the one to one relationship in the pipeline & corrupt the data (e.g., AGE targets wrong campaign). The solution is streamlining the metadata workflow that includes a validation of the required dimensions.

The failing google ads resources underscored the critical need for environment parity and robust unit testing, as dependency mismatches between local dev and Databricks runtimes caused the outage. While a multi-version compatible test structure was implemented as an immediate fix, the long-term solution requires migrating production pipelines out of notebooks to ensure consistent reliability and testability.

Migration of artifacts involves Spark usage and there are several critical schema changes in artifacts. These changes break the reading and writing process, so the latest schema has to be enforced. The solution is pipeline versioning which allows to read and migrate between different folder structures without schema errors.