---
$schema: brain://entity/project/v1
$id: entity/project/feature-flags
$type: project
$version: 1
$created: '2026-01-22T08:31:01.778517Z'
$updated: '2026-01-30T10:28:13.217174'
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
  target: entity/project/fresh
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/testing
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.778517Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Feature Flags
$orphan_reason: pending_enrichment
---

# Feature Flags Patterns

*Source: hellofresh/spec-machine/profiles/engagement-dau/standards/feature-flags/*

### feature-flags

# Feature Flags Standards  ## Overview  Use useFeatureIsEnabled hook for conditional feature rendering. Always provide feature flag keys as constants.  **Why**: Feature flags enable gradual rollouts, A/B testing, and quick feature toggles without deployments.  ## useFeatureIsEnabled Hook  ### Basic...

---

*Synced from spec-machine. Run `/sync-tech-context` to update.*
