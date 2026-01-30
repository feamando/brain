---
$schema: brain://entity/project/v1
$id: entity/project/state-management
$type: project
$version: 1
$created: '2026-01-22T08:31:01.778980Z'
$updated: '2026-01-30T10:28:13.218501'
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
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.778980Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: State Management
$orphan_reason: pending_enrichment
---

# State Management Patterns

*Source: hellofresh/spec-machine/profiles/engagement-dau/standards/state-management/*

### state-machines

# State Machine Patterns with Zustand  ## Overview  Patterns for implementing type-safe state machines using Zustand with discriminated unions, enabling complex UI flows with predictable state transitions.  **Why**: State machines prevent invalid state combinations (e.g., loading + error simultaneou...
### zustand-patterns

# State Management Standards  ## Use Zustand for Client State Only  **Never** use Zustand for server data. Use TanStack Query (REST) or Apollo Client (GraphQL) for server state.  **Why**: Separating client and server state prevents sync issues and enables optimistic updates.  ## When to Use Zustand...

---

*Synced from spec-machine. Run `/sync-tech-context` to update.*
