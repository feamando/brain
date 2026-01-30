---
$schema: brain://entity/system/v1
$id: entity/system/hc-likely-hellochef-or-hello-content-team
$type: system
$version: 1
$created: '2026-01-22T08:31:01.616641Z'
$updated: '2026-01-22T08:31:01.616641Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/system/hc-hellochef
  confidence: 0.9215
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
- type: similar_to
  target: entity/system/ccm-contentcampaign-management-system
  confidence: 0.856
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.616641Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Hc Likely Hellochef Or Hello Content Team
---

# Hc_Likely_Hellochef_Or_Hello_Content_Team

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Team responsible for uploading menu weeks into CCM (from: HFCA - CCM Recipes)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
