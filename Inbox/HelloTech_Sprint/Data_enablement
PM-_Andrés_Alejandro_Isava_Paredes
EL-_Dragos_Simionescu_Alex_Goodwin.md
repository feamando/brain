---
type: hellotech_sprint_report
squad: Data enablement
PM- Andrés Alejandro Isava Paredes
EL- Dragos Simionescu Alex Goodwin
tribe: OpsTech Auto Cluster
mega_alliance: Ops
synced_at: 2026-02-04T13:55:23.907628
source: HelloTech Every Other Week Squad Sprint Report
---

## Data enablement
PM- Andrés Alejandro Isava Paredes
EL- Dragos Simionescu Alex Goodwin
**Tribe:** OpsTech Auto Cluster
**Mega-Alliance:** Ops
**Squad Lead:** Ed Dunger

### Squad KPI
-% Features delivered that contribute to standardisation (in local tools & Hellotech code base)

*Features = stories, tasks are not counted within this KPI

### KPI Movement
33%

### Delivered (This Sprint)
- Extended TIS Business Marts to AU/NZ to enable standardised Logistics Exceptions management
- Extended Physical box pipelines (ODIN) to Nordics
- Completed 30% Wave 1 Deprecation of UK_OPS_ANALYTICS
- Evaluated usage of Atlan API for automatic README completion in order to streamline assets certification
- Migrate all Airflow DAGs to dbt orchestration (Snowflake tasks)
- Repoint UK date_dimension SF consumers to global date_dimension

### Planned (Next Sprint)
N/A

### Key Learnings
- Snowflake dbt projects offer limited observability that we had to overcome with custom solutions. These required significant more effort than the migration itself.
- ODIN data outputs structure differs by business_division, which requires additional modeling for standartization
- Physical box price and costs calculation logic needed to  be refactored to reflect the actual numbers from сustomer basket and shopping experience