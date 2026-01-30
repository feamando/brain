---
$schema: brain://entity/system/v1
$id: entity/system/v0-by-vercel
$type: system
$version: 1
$created: '2026-01-22T08:31:01.649936Z'
$updated: '2026-01-30T10:24:58.209628'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/system/spec-machine
  confidence: 0.8726
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/system/figma
  confidence: 0.8502
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.649936Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: V0 By Vercel
---

# V0_By_Vercel

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] AI prototyping tool being evaluated for enabling designers/PMs to create interactive prototypes (from: 2025: AI Bytes - Operating Model & Core )

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
