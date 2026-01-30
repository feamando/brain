---
$schema: brain://entity/project/v1
$id: entity/project/observability
$type: project
$version: 1
$created: '2026-01-22T08:31:01.781424Z'
$updated: '2026-01-30T10:28:13.224486'
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
  target: entity/project/decisions
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/fresh
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.781424Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Observability
$orphan_reason: pending_enrichment
---

# Observability Patterns

*Source: hellofresh/spec-machine/profiles/engagement-dau/standards/observability/*

### analytics

# Analytics & Event Tracking Standards  ## Overview  Use custom analytics hooks with useCallback for consistent event tracking. Always specify destinations and provide complete event context.  **Why**: Structured analytics enable data-driven decisions and product insights.  ## Analytics Hook Pattern...
### error-handling

# Error Handling Standards  ## Overview  Use ErrorBoundary components to catch and handle React errors gracefully. Integrate OpenTelemetry for distributed tracing and error monitoring.  **Why**: Proper error handling prevents app crashes, provides better UX, and enables debugging in production.  ##...
### performance-monitoring

# Performance Monitoring Standards  ## Overview  Standards for monitoring and measuring application performance in React Native using native performance tracking and OpenTelemetry integration.  **Why**: Performance monitoring identifies bottlenecks, tracks user experience metrics, and enables proact...
### tracing

# OpenTelemetry Tracing Standards  ## Overview  Standards for distributed tracing with OpenTelemetry to enable debugging, performance analysis, and observability across the React Native application.  **Why**: Tracing provides visibility into application behavior, helps identify performance bottlenec...

---

*Synced from spec-machine. Run `/sync-tech-context` to update.*
