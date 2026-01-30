---
$schema: brain://entity/system/v1
$id: entity/system/cdps-customer-delivery-platform-service
$type: system
$version: 1
$created: '2026-01-22T08:31:01.697121Z'
$updated: '2026-01-30T10:28:12.975489'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/consumer-core
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/ally
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/system/live
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/system/slack
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/system/cdps
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.697121Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Cdps Customer Delivery Platform Service
$orphan_reason: pending_enrichment
---

# Cdps_Customer_Delivery_Platform_Service

**Type:** system
**Created:** 2026-01-02
**Source:** slack extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] New platform being rolled out by Consumer Core requiring API migration (#tribe-new-ventures-leads-internal)

## Related Entities

[To be filled]

## Notes

- Created automatically from slack analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*
