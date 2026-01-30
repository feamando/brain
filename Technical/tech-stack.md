---
$schema: brain://entity/project/v1
$id: entity/project/tech-stack
$type: project
$version: 7
$created: '2026-01-22T08:31:01.096543Z'
$updated: '2026-01-30T14:33:14.690237+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.096543Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Tech Stack
---

# HelloFresh Tech Stack Overview

## Frontend (Consumer)

| Layer | Technology | Notes |
|-------|------------|-------|
| Framework | Next.js 14 | App Router |
| Language | TypeScript 5.x | Strict mode |
| State | Zustand | Lightweight stores |
| Styling | CSS Modules + Zest tokens | Design system |
| Testing | Jest + RTL + Playwright | Unit + E2E |

## Mobile (Consumer)

| Layer | Technology | Notes |
|-------|------------|-------|
| Framework | React Native | Shared components with web |
| Navigation | React Navigation | Deep linking support |
| State | Zustand | Same patterns as web |
| Testing | Jest + Detox | Unit + E2E |

## Backend Services

| Service | Language | Framework |
|---------|----------|-----------|
| Consumer BFF | TypeScript | NestJS |
| Engagement | Go | Standard library |
| Logistics | Go | gRPC services |

## Infrastructure

| Component | Technology |
|-----------|------------|
| Hosting | Vercel (frontend), AWS (backend) |
| Feature Flags | Statsig |
| Monitoring | Grafana, Datadog |
| CI/CD | GitHub Actions |

## Key Libraries

| Purpose | Library |
|---------|---------|
| Data Fetching | Apollo Client (GraphQL), fetch (REST) |
| Forms | React Hook Form |
| Validation | Zod |
| Dates | date-fns |
| Analytics | Segment |

---

*Run `/sync-tech-context` to update from spec-machine*
