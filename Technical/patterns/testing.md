---
$schema: brain://entity/project/v1
$id: entity/project/testing
$type: project
$version: 1
$created: '2026-01-22T08:31:01.779851Z'
$updated: '2026-01-30T10:28:13.220814'
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
  target: entity/person/ally
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
  timestamp: '2026-01-22T08:31:01.779851Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Testing
$orphan_reason: pending_enrichment
---

# Testing Patterns

*Source: hellofresh/spec-machine/profiles/engagement-dau/standards/testing/*

### mocking-strategies

# Mocking Strategies  ## Overview  Comprehensive patterns for mocking dependencies in React Native tests, including TanStack Query, Apollo Client, navigation, Zustand stores, and native modules.  **Why**: Proper mocking enables isolated, fast, and reliable tests by replacing external dependencies wi...
### test-ids

# Test IDs Standards  ## Overview  Define test IDs as constants grouped by feature. Use descriptive, hierarchical naming for test IDs.  **Why**: Consistent test IDs enable reliable automated testing and prevent duplication.  ## Test ID Constants  ### Feature-Level Organization  Define test IDs in fe...
### test-patterns

# Testing Standards  ## Test Environment Setup  Mock native modules globally in jest.setup.ts.  ```typescript // jest.setup.ts import '@testing-library/jest-native/extend-expect';  jest.mock('@libs/native-modules/events', () => ({   sendEvent: jest.fn(),   SharedModulesEventEmitter: {     addListene...

---

*Synced from spec-machine. Run `/sync-tech-context` to update.*
