---
$schema: brain://entity/project/v1
$id: entity/project/localization
$type: project
$version: 1
$created: '2026-01-22T08:31:01.777171Z'
$updated: '2026-01-30T10:28:13.213617'
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
  target: entity/project/mobile-app
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/fresh
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/system/react-native
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.777171Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Localization
$orphan_reason: pending_enrichment
---

# Localization Patterns

*Source: hellofresh/spec-machine/profiles/engagement-dau/standards/localization/*

### content-rendering

# Content Rendering Standards  ## Overview  Standards for rendering dynamic HTML content safely in React Native using react-native-render-html and sanitize-html.  **Why**: Proper content rendering prevents XSS attacks, ensures consistent formatting, and provides safe HTML display in mobile apps.  ##...
### localization

# Localization & Internationalization Standards  ## Overview  Use useT9n hook with namespace-based translations for all user-facing text. Never hardcode user-facing strings.  **Why**: Localization enables global reach and provides consistent translation patterns across the app.  ## useT9n Hook  ###...

---

*Synced from spec-machine. Run `/sync-tech-context` to update.*
