---
$schema: brain://entity/project/v1
$id: entity/project/incomm-integration
$type: project
$version: 8
$created: '2026-01-22T08:31:01.054652Z'
$updated: '2026-01-30T14:32:27.332900+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.054652Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Incomm Integration
---

# Project: InComm Retail Gift Card Integration

**Type:** Integration / Payment Method
**Status:** Active Scope
**Scope Source:** [Google Drive Folder](https://drive.google.com/drive/folders/17BoJBC3hLM9hRT6lN4QUAAcrfK2zk5aK) (ID: `17BoJBC3hLM9hRT6lN4QUAAcrfK2zk5aK`)

## Overview
Integration with **InComm's Retail Transaction Gateway (RTG) V2** to support "Transferred Value" (TV) products, specifically retail gift cards. This allows customers to purchase physical or digital gift cards at third-party retailers (activated by InComm) and redeem them on our platforms (HelloFresh/Good Chop).

## Core Architecture
*   **Product Type:** Transferred Value (TV) / Gift Cards.
*   **Roles:**
    *   **Retailer:** Initiates **Activation** (Real-time request to InComm). Partner is *not* involved.
    *   **InComm:** Database of record for PIN status (Active, Redeemed, Inactive).
    *   **Partner (Us):** Initiates **Redemption** (Real-time request to InComm when customer enters PIN).

## Integration Scope (Redemption Flow)
The primary development scope is the **Redemption Interface**:
1.  **User Interface:** Customer enters PIN on our site/app.
2.  **Backend Logic:**
    *   Call InComm RTG API (`rtg-tv` module).
    *   Action: `redeem` (or `getStatus`).
    *   Handle timeouts (recommended threshold > 7s).
    *   Handle retries (cancel request or exact retry).
3.  **Value Handling:**
    *   **Full Redemption Rule:** InComm requires full value redemption. No partial balances stored on InComm.
    *   **Balance Management:** If we support partial use, *we* must maintain the wallet balance ledger; InComm sees it as fully "spent" once redeemed.

## Technical Specs (from TV Tool Kit V3.0)
*   **API Protocol:** HTTP POST (REST-like).
*   **Format:** JSON or XML.
*   **Authentication:** OAuth 2 (Client ID + Client Secret -> Token valid for 24h).
*   **PIN Format:** Up to 20 chars. Standard InComm PINs are 17 digits (numeric).
*   **Key Fields:**
    *   `AccessID` / `PartnerName` (Provided by InComm).
    *   `InventoryID` (The PIN).
    *   `TransactionID` (UUID, max 50 chars).

## References
*   **Integration Guide:** `TV Tool Kit_TV Integration Guide v3.0 04-23-2024.pdf`
*   **API Spec:** `TV Tool Kit_Retail_Transaction_Gateway_V2_API_Specification_20250501.pdf`
