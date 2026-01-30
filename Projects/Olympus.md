---
$schema: brain://entity/project/v1
$id: entity/project/olympus
$type: project
$version: 8
$created: '2026-01-22T08:31:01.038216Z'
$updated: '2026-01-30T14:32:05.106459+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/person/ally
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/system/concord
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.038216Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Olympus
$orphan_reason: no_external_data
---

# Olympus

**Type:** project
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Image RAG solution for Concorde (from: Demo Session Sign-Up Sheet)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Gdocs Context

- [2026-01-02] Image RAG system for Concorde (from: Demo Session Sign-Up Sheet)
