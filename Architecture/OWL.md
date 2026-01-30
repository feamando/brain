---
$schema: brain://entity/project/v1
$id: entity/project/owl
$type: project
$version: 1
$created: '2026-01-22T08:31:01.093799Z'
$updated: '2026-01-22T10:41:35.072068+00:00'
$confidence: 0.43
$source: unknown
$status: Active
$relationships:
- type: related_to
  target: entity/project/good-chop
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.093799Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:35.072070+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 3
name: Owl
id: arch-owl
title: OWL (Order/Refund Management)
type: system
last_updated: 2025-12-08
related:
- '[[Projects/Good_Chop.md]]'
- '[[Projects/The_Pets_Table.md]]'
---

# OWL

## Overview

OWL is the order and refund management system. Currently experiencing issues with refund processing for Charge at Checkout (C@C) orders.

## Known Issues

### C@C Refund Bug
- **Status:** Active blocker
- **Symptom:** Refunds not triggering for C@C customers
- **Workaround:** Refunds work via Bob (alternative system)
- **Jira:** SE-22404
- **Impact:** Blocking Good Chop and TPT C@C allocation increases

## Integration Points

- Good Chop - Charge at Checkout
- The Pets Table - Charge at Checkout
- Bob (fallback refund system)

## Changelog
- **2025-12-16:** Context update: **Concept:** "Context-Driven Product Management" â€“ automating knowledge curation to feed AI tools.
- **2025-12-11:** Context update: **Good Chop "Charge at Checkout" Refunds:** Not processing via OWL. (Jira SE-22404).
- **2025-12-09:** Context update: **Good Chop "Charge at Checkout"**: Refunds not processing via OWL. (Jira SE-22404).
- **2025-12-08:** Context update: **New Recipes**: Multiple new recipes in pipeline (Greek Isle Caper Salmon, Greek-Style Market Chicken Bowl, Red Pepper Bruschetta Shredded Chicken, G

- **2025-12-08:** Stub created from daily context synthesis - C@C refund bug documented