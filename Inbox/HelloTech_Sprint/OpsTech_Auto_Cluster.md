---
type: hellotech_sprint_report
squad: OpsTech Auto Cluster
tribe: 33%
mega_alliance: Ops
synced_at: 2026-02-04T12:25:20.949608
source: HelloTech Every Other Week Squad Sprint Report
---

## OpsTech Auto Cluster
**Tribe:** 33%
**Mega-Alliance:** Ops

### KPI Movement
Data enablement
PM- Andrés Alejandro Isava Paredes
EL- Dragos Simionescu Alex Goodwin

### Delivered (Last Sprint)
Ed Dunger

### Planned (Next Sprint)
-% Features delivered that contribute to standardisation (in local tools & Hellotech code base)

*Features = stories, tasks are not counted within this KPI

**MBL Initiative:** - Extended TIS Business Marts to AU/NZ to enable standardised Logistics Exceptions management
- Extended Physical box pipelines (ODIN) to Nordics
- Completed 30% Wave 1 Deprecation of UK_OPS_ANALYTICS
- Evaluated usage of Atlan API for automatic README completion in order to streamline assets certification
- Migrate all Airflow DAGs to dbt orchestration (Snowflake tasks)
- Repoint UK date_dimension SF consumers to global date_dimension

**Sprint Health:** - Snowflake dbt projects offer limited observability that we had to overcome with custom solutions. These required significant more effort than the migration itself.
- ODIN data outputs structure differs by business_division, which requires additional modeling for standartization
- Physical box price and costs calculation logic needed to  be refactored to reflect the actual numbers from сustomer basket and shopping experience