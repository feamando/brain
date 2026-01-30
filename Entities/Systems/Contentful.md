---
$schema: brain://entity/system/v1
$id: entity/system/contentful
$type: system
$version: 1
$created: '2026-01-22T08:31:01.694770Z'
$updated: '2026-01-30T10:28:12.969944'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/discount-communication
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/portion-percentage
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/reactivation
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/feeding-plan
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/reactivation-page
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.694770Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Contentful
$orphan_reason: pending_enrichment
---

# Contentful

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Potential location for footer links (from: Weekly Prod/Des/Eng/PA)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Gdocs Context

- [2026-01-02] Content management system with shared modules (from: Discount Communication Presets)


- [2026-01-02] CMS for managing editable content entries (from: Scope Proposal: External Engineering Aug)

- [2026-01-02] Content management dependency (from: PRD: Cancellation Funnel Unification)

- [2026-01-02] CMS for managing copy and assets (from: Scope Proposal: External Engineering Aug)

## Slack Context

- [2026-01-02] Content management system, possibly used for Landing Pages (#tribe-new-ventures-internal)

## Github Context

- [2026-01-02] Integration for recipe CTA content management (GitHub commits)


- [2026-01-02] Keys added for plan card images (GitHub commits)

- [2026-01-02] Integration for recipe carousel content management (GitHub commits)

- [2026-01-02] Added key for invalid payment message management (GitHub commits)

- [2026-01-02] Content management system receiving new keys for nutrition and other content (GitHub commits)

- [2026-01-02] Added key for storage and preps title (GitHub commits)

- [2026-01-02] Multiple updates for content keys including entry names, portion percentages, key ingredients, and descriptions (GitHub commits)

- [2026-01-02] Asset key format standardization to markdown (GitHub commits)

- [2026-01-02] New keys added for feeding plan quiz step (GitHub commits)

- [2026-01-02] Added keys for delivery details component and payment fraud error entry (GitHub commits)

- [2026-01-02] CMS integration for managing UI text and content keys (GitHub commits)

- [2026-01-02] CMS used for managing content keys for reactivation page (GitHub commits)