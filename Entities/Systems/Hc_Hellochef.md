---
$schema: brain://entity/system/v1
$id: entity/system/hc-hellochef
$type: system
$version: 1
$created: '2026-01-22T08:31:01.701918Z'
$updated: '2026-01-30T10:24:58.338726'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/system/ccm-customer-choice-menu
  confidence: 0.8547
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/system/hc-likely-hellochef-or-hello-content-team
  confidence: 0.9215
  last_verified: '2026-01-30'
  source: auto_embedding
- type: similar_to
  target: entity/system/ccm-contentcampaign-management-system
  confidence: 0.8887
  last_verified: '2026-01-30'
  source: auto_embedding
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.701918Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Hc Hellochef
---

# Hc_Hellochef

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Team/system responsible for uploading menus into CCM (from: HFCA - CCM Recipes)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Gdocs Context

- [2026-01-02] Team/system responsible for uploading menu weeks into CCM (from: HFCA - CCM Recipes)
