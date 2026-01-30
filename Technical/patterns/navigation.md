---
$schema: brain://entity/project/v1
$id: entity/project/navigation
$type: project
$version: 1
$created: '2026-01-22T08:31:01.779420Z'
$updated: '2026-01-30T10:28:13.219719'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/hellofresh
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/engagement
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/data
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/fresh
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/desi
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.779420Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Navigation
$orphan_reason: pending_enrichment
---

# Navigation Patterns

*Source: hellofresh/spec-machine/profiles/engagement-dau/standards/navigation/*

### deep-linking

# Deep Linking Standards  ## Overview  Standards for implementing deep links using the project's `createModuleLinking` architecture, enabling navigation from external sources while handling cold start race conditions.  **Why**: Deep linking improves user experience by allowing direct navigation to s...
### navigation-patterns

# Navigation Standards  ## Overview  Standards for configuring navigation headers and navigation behavior using React Navigation with the project's `useNavigationHeader` hook and route enum patterns.  **Why**: Consistent navigation patterns improve UX, ensure design system compliance, and provide ty...
### providers

# Provider Architecture Standards  ## Overview  Use entry providers to set up the application context hierarchy. Providers wrap components with necessary context like navigation, theming, data access, and error boundaries.  **Why**: Providers establish the runtime environment and ensure all componen...

---

*Synced from spec-machine. Run `/sync-tech-context` to update.*
