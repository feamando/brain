---
$schema: brain://entity/project/v1
$id: entity/project/react-native-core
$type: project
$version: 1
$created: '2026-01-22T08:31:01.780930Z'
$updated: '2026-01-30T10:28:13.223303'
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
  timestamp: '2026-01-22T08:31:01.780930Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: React Native Core
$orphan_reason: pending_enrichment
---

# React Native Core Patterns

*Source: hellofresh/spec-machine/profiles/engagement-dau/standards/react-native-core/*

### component-patterns

<!-- TODO: Extract only component patterns (Component Structure, JSX Formatting, Conditional Rendering, List Rendering, Event Handling) -->  # React Native Code Style  This document defines code formatting and style patterns for React Native TypeScript projects. All patterns are enforced by ESLint/P...
### constants

# Constants Standards  ## Overview  Organize constants in feature-level files. Group related constants together and export them for reuse.  **Why**: Centralized constants prevent magic numbers, improve maintainability, and enable easy updates.  ## File Organization  ### Feature-Level Constants  Crea...
### hooks-patterns

<!-- TODO: Extract only hooks patterns (useState, useEffect, useMemo, useCallback, custom hooks) -->  # React Native Code Style  This document defines code formatting and style patterns for React Native TypeScript projects. All patterns are enforced by ESLint/Prettier and validated in the codebase....
### performance

# Performance Optimization Standards  ## Overview  Use useRef, useMemo, and useCallback appropriately to prevent unnecessary re-renders and expensive computations. Apply performance optimizations strategically, not universally.  **Why**: Strategic optimization improves app responsiveness without add...

---

*Synced from spec-machine. Run `/sync-tech-context` to update.*
