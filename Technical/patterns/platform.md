---
$schema: brain://entity/project/v1
$id: entity/project/platform
$type: project
$version: 1
$created: '2026-01-22T08:31:01.777605Z'
$updated: '2026-01-30T10:28:13.214726'
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
  target: entity/system/react-native
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/system/native
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.777605Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Platform
$orphan_reason: pending_enrichment
---

# Platform Patterns

*Source: hellofresh/spec-machine/profiles/engagement-dau/standards/platform/*

### android-patterns

# Android Platform Patterns  ## Overview  Standards for Android-specific patterns, native module integration, and platform-specific UI behaviors in React Native applications.  **Why**: Android has unique platform requirements including hardware back button handling, status bar configuration, elevati...
### ios-patterns

# iOS Platform Patterns  ## Overview  Standards for iOS-specific patterns, native module integration, and platform-specific UI behaviors in React Native applications.  **Why**: iOS has unique platform requirements including safe area handling, shadow rendering, status bar configuration, and specific...
### native-development

# Native Development Standards  ## Requirements  Native files in this repo are display-only. All native changes must occur in `../ios` and `../android` directories.  **Why**: Keeps native code organized in dedicated repositories.  ## Verification  Before any native work, verify `../ios` and `../andr...
### platform-detection

# Platform Detection Patterns  ## Overview  Standards for detecting and handling platform differences between iOS and Android in React Native applications.  **Why**: Proper platform detection enables platform-specific implementations while maintaining code clarity and preventing runtime errors. Thes...

---

*Synced from spec-machine. Run `/sync-tech-context` to update.*
