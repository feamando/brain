---
$schema: brain://entity/project/v1
$id: entity/project/data-access
$type: project
$version: 1
$created: '2026-01-22T08:31:01.776710Z'
$updated: '2026-01-30T10:28:13.212460'
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
  target: entity/system/react-native
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.776710Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Data Access
$orphan_reason: pending_enrichment
---

# Data Access Patterns

*Source: hellofresh/spec-machine/profiles/engagement-dau/standards/data-access/*

### data-transformation

# Data Transformation Standards  ## Overview  Use transformer functions for API response shaping and helper functions for business logic. Organize transformers, helpers, and utils in separate files.  **Why**: Separation of concerns makes data transformation testable, maintainable, and reusable.  ##...
### graphql-api

# GraphQL API Standards  ## When to Use GraphQL  Always verify data availability in GraphQL schema first. If a query exists in the schema, use GraphQL over REST.  **Why**: Reduces over-fetching, provides type safety, and maintains consistency across the app.  ## File Organization  ``` src/data-acces...
### native-data

# Native Data Standards  ## ⚠️ SPECIALIZED PROTOCOL - Only on User Request  **Use only when accessing observables from the native app container.**  This is NOT for regular React Native development. This is a specific API for data that the iOS/Android container exposes through observables.  **For reg...
### repository-loading

# Repository Loading Standards  ## Overview  Use RepositoryLoader to validate critical data is loaded before rendering. Configure requiredRepositories to specify data dependencies.  **Why**: Pre-rendering validation prevents downstream null errors and improves error handling.  ## RepositoryLoader Co...
### rest-api

# REST API Standards  ## When to Use REST API  Use REST API only when data is NOT available in GraphQL schema. Always verify GraphQL schema first.  **Why**: GraphQL provides better type safety and reduces over-fetching, but REST is needed for legacy endpoints and external APIs.  ## File Organization...

---

*Synced from spec-machine. Run `/sync-tech-context` to update.*
