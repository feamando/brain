---
$schema: brain://entity/project/v1
$id: entity/project/global
$type: project
$version: 1
$created: '2026-01-22T08:31:01.780307Z'
$updated: '2026-01-30T10:28:13.222193'
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
  target: entity/project/decisions
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/tech-stack
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
  timestamp: '2026-01-22T08:31:01.780307Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Global
$orphan_reason: pending_enrichment
---

# Global Patterns

*Source: hellofresh/spec-machine/profiles/engagement-dau/standards/global/*

### cli-tools

# CLI Tools and Commands  ## Overview  This document lists all available CLI commands in the project. Use these commands for common development tasks instead of running underlying tools directly.  **Why**: Using the defined yarn scripts ensures consistent behavior across the team, handles environmen...
### tech-stack

# Tech Stack (MASTER REFERENCE)  ## Context and Usage  This is the authoritative tech stack reference for the Shared Mobile Modules React Native project. All development decisions must align with these technology choices and versions.  ## Application Framework  - **React Native:** 0.75.4 (Cross-plat...

---

*Synced from spec-machine. Run `/sync-tech-context` to update.*
