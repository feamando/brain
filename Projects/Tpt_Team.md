---
$schema: brain://entity/project/v1
$id: entity/project/tpt-team
$type: project
$version: 1
$created: '2026-01-22T08:31:00.973168Z'
$updated: '2026-01-30T10:19:58.665318'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: nikita
  confidence: 0.7
  source: body_extraction
  last_verified: '2026-01-30'
- type: similar_to
  target: entity/project/commercial-team
  confidence: 0.9444
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.973168Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Tpt Team
---

# Tpt_Team

**Type:** project
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Team that manages customer surveys and research (from: Nikita / Prateek (Deep Dive) - 2025/12/0)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:50*

## Gdocs Context

- [2026-01-02] Team that runs customer surveys (from: Nikita / Prateek (Deep Dive) - 2025/12/0)
