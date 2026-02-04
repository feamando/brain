---
$schema: brain://entity/system/v1
$id: entity/system/vmsvmsu
$type: system
$version: 2
$created: '2026-01-22T08:31:01.773622Z'
$updated: '2026-02-04T10:35:00.000000Z'
$confidence: 0.85
$source: manual_enrichment
$status: active
$relationships:
- type: mentioned_in
  target: entity/person/ally
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: has_component
  target: entity/system/factor-form-vms-sku-schema
  confidence: 1.0
  source: manual
  last_verified: '2026-02-04'
- type: part_of
  target: entity/project/factor-form-rtevms
  confidence: 0.9
  source: manual
  last_verified: '2026-02-04'
$tags:
- factor-form
- voucher-management
- sku
- subscription
- otp
$aliases:
- VMS
- VMSU
- Voucher Management System
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.773622Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
- event_id: evt-enrichment-20260204
  timestamp: '2026-02-04T10:35:00.000000Z'
  type: entity_update
  actor: user/nikita
  changes:
  - field: content
    operation: update
    value: Added full system documentation and SKU schema linkage
  message: Manual enrichment with VMS/VMSU system details
name: VMS/VMSU Voucher Management System
---

# VMS/VMSU Voucher Management System

**Type:** system
**Created:** 2026-01-02
**Source:** GitHub extraction + Manual enrichment (2026-02-04)

## Overview

The Voucher Management System (VMS/VMSU) is Factor Form's backend system for managing product SKUs, vouchers, subscriptions, and one-time purchases. It handles the full lifecycle of customer orders from cart to fulfillment.

## Key Components

### Product Families

| Family | Code | Use Case |
|--------|------|----------|
| **VMS** | `FJ-VMS` | Subscription-based orders |
| **VMSU** | `FJ-VMSU` | One-Time Purchase (OTP) orders |

### SKU Encoding

See: [[Factor_Form_VMS_SKU_Schema]] for detailed SKU structure documentation.

**Format:** `FJ-[FAMILY]-[BOX_COUNT]-[VARIANT_CODE]-0`

### Key Features

1. **SKU Normalization** - Converts between VMS ↔ VMSU families based on customer context
2. **Dynamic Pricing** - Applies SNS discounts (40%/20%) vs OTP full price
3. **Cart Integration** - Validates and applies appropriate SKU family during checkout
4. **Feature Gating** - `rtevms-2256_vmsu_family` flag controls VMSU activation

## Context

- [2026-01-02] Added normalization helper for SKU family mapping (GitHub commits)
- [2025-12-15] RTEVMS-2256: VMSU product family implementation completed
- [2025-12] TAM-T-53: De-couple Product SKU business logic (in progress)

## Related Tickets

- **RTEVMS-2256:** VMSU product family - Added normalized SKU for VMSU family
- **RTEVMS-2186/2362:** Create new product family for OTP support
- **RTEVMS-1323:** [TAM-A-14] One Time Purchase epic
- **TAM-T-53:** De-couple Product SKU business logic

## Related Entities

- [[Factor_Form_VMS_SKU_Schema]] - SKU encoding documentation
- [[Factor_Form_Rtevms]] - Parent project
- RTE Actives integration

## Technical Details

### GitHub Commits (RTEVMS-2256)
- `2884f19` - Added normalized sku for vmsu family
- `d53cbcc` - Added feature gate to enable vmsu family usage
- `7fd8b9d` - Added changes to normalized vms to vmsu in flows
- `f9a4589` - Removed hard coded logic that calculates the sku

### Feature Flags
- `rtevms-2256_vmsu_family` - Statsig gate for VMSU family activation

---
*Last updated: 2026-02-04 10:35*
