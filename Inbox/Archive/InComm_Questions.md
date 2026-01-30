---
$schema: brain://entity/project/v1
$id: entity/project/incomm-questions
$type: project
$version: 1
$created: '2026-01-22T08:31:02.204740Z'
$updated: '2026-01-30T10:28:14.264822'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:02.204740Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Incomm Questions
$orphan_reason: pending_enrichment
---

# Questions for InComm Team (Kickoff / Technical Deep Dive)

## 1. Operational & Logistics
- **PIN Generation:** We see we can either generate PINs or have InComm do it. For a faster launch with major retailers (Walmart, CVS, etc.), which path has fewer friction points?
- **Physical Cards:** If InComm generates the PINs, do you also handle the manufacturing coordination with the card printers, or do we just receive a file to send to our own print vendors?

## 2. Redemption Logic (The "Full Value" Constraint)
- **Error Handling / Reversals:** If we call `redeem` and get a success, but our system fails to credit the user's wallet (database crash), does the `rtg-tv` API support a `void` or `reverse` call to reactivate that PIN immediately?
    - *Context:* The spec mentions "cancel" requests for timeouts, but not explicit reversals for post-redemption internal failures.
- **Balance Inquiries:** Are there commercial costs or rate limits associated with `getStatus` calls? We intend to call this whenever a user enters a code to preview the value before they commit to redeeming.

## 3. Fraud & Security
- **Velocity Controls:** Does InComm implement rate limiting on invalid PIN attempts (brute force protection) at the API level, or is the Partner fully responsible for blocking bad actors?
- **PIN Locking:** If a valid PIN is entered incorrectly multiple times (or targeted), does it enter a "Locked" state? What is the customer service flow to unlock it?

## 4. Testing & Certification
- **Test Data:** Can you provide a set of test PINs representing different states (Active, Inactive, Redeemed, Locked) for our QA automation?
- **Certification:** What is the lead time for certification once we complete coding? Is there a specific "freeze period" before peak trading?

## 5. Reporting
- **Reconciliation:** Could you provide a sample specification for the daily settlement/reconciliation files? We need to confirm that our `TransactionID` will persist through to the finance reports for 1:1 matching.
