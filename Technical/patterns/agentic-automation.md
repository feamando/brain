---
$schema: brain://entity/project/v1
$id: entity/project/agentic-automation
$type: project
$version: 1
$created: '2026-01-22T08:31:01.781901Z'
$updated: '2026-01-30T10:28:13.225806'
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
  target: entity/system/native
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/platform
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.781901Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Agentic Automation
$orphan_reason: pending_enrichment
---

# Agentic Automation Patterns

*Source: hellofresh/spec-machine/profiles/engagement-dau/standards/agentic-automation/*

### mobile-mcp

# Mobile MCP - Mobile Automation Server  ## Overview  Mobile MCP is a Model Context Protocol server that enables AI agents to automate iOS and Android applications through a platform-agnostic interface. It works with simulators, emulators, and real devices using native accessibility trees and screen...

---

*Synced from spec-machine. Run `/sync-tech-context` to update.*
