---
$schema: brain://entity/system/v1
$id: entity/system/hello-connect
$type: system
$version: 1
$created: '2026-01-22T08:31:01.671672Z'
$updated: '2026-01-22T08:31:01.671672Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/system/recharge
  confidence: 0.8586
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/system/shopify
  confidence: 0.8707
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/system/elevar
  confidence: 0.8512
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.671672Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Hello Connect
---

# Hello_Connect

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Alternative tool for uploading products to Shopify, estimated ~1 week (from: Sameer:Nikita 1:1 - 2025/12/22 15:31 CET)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Gdocs Context

- [2026-01-02] Previously attempted offshore partner for menu management (poor quality results) (from: Ian:Nikita 1:1 (2w) - 2025/12/19 17:01 C)
