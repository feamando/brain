---
$schema: brain://entity/project/v1
$id: entity/project/daniel
$type: project
$version: 1
$created: '2026-01-22T08:31:01.149758Z'
$updated: '2026-01-30T10:22:46.178466'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: nikita
  confidence: 0.7
  source: body_extraction
  last_verified: '2026-01-30'
- type: related_to
  target: entity/project/team-new-ventures
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.149758Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Daniel
id: entity-daniel
type: person
role: Engineering Lead
last_updated: 2025-12-08
related:
- '[[Entities/Team_New_Ventures.md]]'
---

# Daniel

## Role & Responsibilities

- **Title:** Engineering Lead
- **Scope:** Technical feasibility, implementation

### Primary Responsibilities

- Technical leadership
- "T-Shirt Sizing" estimates (with Alex)
- Implementation guidance

## Key Relationships

- **Collaborators:** Alex Matlin (Engineering Lead)
- **Team:** Engineering

## Changelog
- **2025-12-11:** Context update: **Daniel & Nikita:**

- **2025-12-08:** Entity created from daily context synthesis