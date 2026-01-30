---
$schema: brain://entity/system/v1
$id: entity/system/statsig
$type: system
$version: 1
$created: '2026-01-22T08:31:01.644246Z'
$updated: '2026-01-22T08:31:01.644246Z'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: similar_to
  target: entity/system/experimentation-core
  confidence: 0.9172
  source: auto_embedding
  last_verified: '2026-01-30'
  metadata:
    model: all-MiniLM-L6-v2
    threshold: 0.85
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.644246Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Statsig
---

# Statsig

**Type:** system
**Created:** 2026-01-02
**Source:** gdocs extraction

## Overview

[Auto-generated - needs manual review]

## Context

- [2026-01-02] Experimentation platform experiencing group assignment health issues (from: Alexander Matlin - Handover - Vacation C)

## Related Entities

[To be filled]

## Notes

- Created automatically from gdocs analysis
- Review and enrich manually

---
*Last updated: 2026-01-02 16:51*

## Gdocs Context

- [2026-01-02] Experimentation platform (not integrated) (from: DRAFT - Good Chop - Shopify Storefront)


- [2026-01-02] Experimentation platform referenced for passwordless sign up (from: PRD: Sign up page revamp)

- [2026-01-02] A/B testing platform referenced for HelloFresh social login experiment (from: PRD: TPT Sign-up Page Revamp)

- [2026-01-02] Experimentation platform for A/B testing (from: PRD: Beam Integration for The Pets Table)

- [2026-01-02] Experimentation platform for A/B testing (from: PRD: Beam Integration for The Pets Table)

- [2026-01-02] Experimentation platform used for HelloFresh social login testing (from: PRD: TPT Sign-up Page Revamp)

- [2026-01-02] Experimentation platform used by HelloFresh for social login testing (from: Memo: TPT Sign-up Page Revamp)

- [2026-01-02] Experimentation platform used by HelloFresh for social login testing (from: Memo: TPT Sign-up Page Revamp)

- [2026-01-02] Used as starting point for price test analysis (from: New Ventures: PA Backlog)

- [2026-01-02] Used as starting point for price test analysis (from: New Ventures: PA Backlog)

- [2026-01-02] Analytics/experimentation platform used for tracking experiment results (from: New Ventures: Cumulative KRs tracker 202)

- [2026-01-02] Analytics/experimentation platform used for tracking experiment results (from: New Ventures: Cumulative KRs tracker 202)

- [2026-01-02] Analytics/experimentation platform used for tracking experiment results (from: New Ventures: Cumulative KRs tracker 202)

- [2026-01-02] Platform used for A/B testing integration and CLV model deployment (from: Demo Session Sign-Up Sheet)

- [2026-01-02] Platform used for A/B testing integration and CLV model deployment (from: Demo Session Sign-Up Sheet)

- [2026-01-02] Platform used for A/B testing integration and CLV model deployment (from: Demo Session Sign-Up Sheet)

## Slack Context

- [2026-01-02] Experimentation platform providing actual results for CVA calculations (#tribe-new-ventures-product)


- [2026-01-02] Experimentation platform hosting Venmo experiment results (#tribe-new-ventures-product)

- [2026-01-02] Experimentation platform with delayed gross_activations metric causing CVR calculation issues (#tribe-new-ventures-product)

## Github Context

- [2026-01-02] Analytics tracking for OTP checkout submissions (GitHub commits)


- [2026-01-02] Experiment mapping and event tracking for OTP (GitHub commits)

- [2026-01-02] Used for feature flagging (HFNL plan switcher) and event tracking (OTP success) (GitHub commits)

- [2026-01-02] Feature flag management system integrated for OTP rollout control (GitHub commits)

- [2026-01-02] Enhanced with OTP attributes for checkout success tracking (GitHub commits)

- [2026-01-02] Event tracking integration for OTP checkout success (GitHub commits)

- [2026-01-02] Being removed from Factor Form OTP configuration (GitHub commits)

- [2026-01-02] Analytics tracking system that required fixes (GitHub commits)