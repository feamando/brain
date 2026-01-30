---
$schema: brain://entity/project/v1
$id: entity/project/code-quality
$type: project
$version: 1
$created: '2026-01-22T08:31:01.776242Z'
$updated: '2026-01-30T10:28:13.211191'
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
  target: entity/person/eric
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/ally
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.776242Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Code Quality
$orphan_reason: pending_enrichment
---

# Code Quality Patterns

*Source: hellofresh/spec-machine/profiles/engagement-dau/standards/code-quality/*

### documentation

# Documentation Standards  ## Overview  Use JSDoc comments with @description, @context, and @example tags for complex functions and components. Document the "why" not the "what".  **Why**: Good documentation helps future developers understand intent and usage.  ## JSDoc Patterns  ### Component Docum...
### file-organization

# File Organization Standards  ## Overview  Standards for organizing files and folders in the React Native Shared Modules (RNSM) repository using a 6-tier module system architecture. This architecture ensures scalability, maintainability, and clear boundaries as the codebase grows.  **Why**: Structu...
### imports-exports

# Import and Export Standards  ## Overview  Standards for organizing imports and exports in TypeScript/React Native files. Proper import organization improves readability and is automatically enforced by ESLint.  **Why**: Consistent import ordering makes dependencies clear, enables tree-shaking, and...
### typescript-patterns

# TypeScript Patterns  ## Overview  Standards for TypeScript type definitions, interfaces, generics, and type safety patterns. This project uses TypeScript strict mode with zero tolerance for `any` types.  **Why**: TypeScript's type system catches errors at compile time, enables better IDE support,...

---

*Synced from spec-machine. Run `/sync-tech-context` to update.*
