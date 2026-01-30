---
$schema: brain://entity/project/v1
$id: entity/project/glossary
$type: project
$version: 1
$created: '2026-01-22T08:31:00.692124Z'
$updated: '2026-01-30T10:07:21.146206'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: otp
  confidence: 0.65
  source: body_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:00.692124Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Glossary
id: glossary
title: Acronym & Term Glossary
last_updated: 2026-01-02
purpose: Disambiguation of acronyms and terms used across HelloFresh/New Ventures
  documentation
---

# Glossary

## Brand & Product Acronyms

| Acronym | Full Name | Description |
|---------|-----------|-------------|
| **HF** | HelloFresh | Parent company and primary meal kit brand |
| **GoC / GOC** | Good Chop | Premium meat subscription service (New Ventures) |
| **TPT** | The Pets Table | Premium pet food subscription (New Ventures) |
| **VMS** | Vitamins, Minerals & Supplements | Product category; also refers to Factor Form sub-brand |
| **Factor 4** | Factor Form | VMS sub-brand of Factor (same as Factor Form) |
| **Factor Form** | Factor Form | VMS wellness products under Factor brand |
| **RTE** | Ready to Eat | Pre-prepared meal category (Factor's core product) |
| **MIO** | Market Innovation & Optimization | New Ventures squad focused on innovation |
| **CMA** | Consumer Mega-Alliance | Cross-brand product organization |
| **NV** | New Ventures | Portfolio: Good Chop, Pets Table, Factor Form, Market Innovation |

## Geographic Acronyms

| Acronym | Full Name | Description |
|---------|-----------|-------------|
| **NA** | North America | US + Canada region |
| **DACH** | Deutschland, Austria, Confoederatio Helvetica | Germany, Austria, Switzerland region |
| **BNL** | Benelux | Belgium, Netherlands, Luxembourg region |
| **ANZ** | Australia & New Zealand | Pacific region |
| **UK** | United Kingdom | British market |
| **US** | United States | American market |
| **CA** | Canada | Canadian market |
| **DE** | Germany (Deutschland) | German market |
| **FR** | France | French market |
| **NL** | Netherlands | Dutch market |

## Business Metrics

| Acronym | Full Name | Description |
|---------|-----------|-------------|
| **TCVA / CVA** | (Total) Customer Value Added | Primary metric for customer lifetime value contribution |
| **AOR** | Average Order Rate | Orders per customer per time period |
| **CVR** | Conversion Rate | Percentage of visitors who convert |
| **CAC** | Customer Acquisition Cost | Cost to acquire a new customer |
| **AOV** | Average Order Value | Average revenue per order |
| **CLV / LTV** | Customer Lifetime Value | Total value from a customer relationship |
| **ARR** | Annual Recurring Revenue | Annualized subscription revenue |
| **P&L** | Profit and Loss | Financial statement |
| **WoW** | Week-over-Week | Comparison to previous week |
| **YoY** | Year-over-Year | Comparison to same period last year |
| **MoM** | Month-over-Month | Comparison to previous month |

## Product & Feature Acronyms

| Acronym | Full Name | Description |
|---------|-----------|-------------|
| **OTP** | One-Time Purchase | Transactional e-commerce (NOT One-Time Password) |
| **SNS** | Subscribe & Save | Subscription model with recurring discount |
| **C@C** | Charge at Checkout | Payment model where charge happens at order, not delivery |
| **RAF** | Refer-a-Friend | Referral program |
| **PDP** | Product Detail Page | Individual product information page |
| **CTA** | Call to Action | Button/link prompting user action |
| **SKU** | Stock Keeping Unit | Unique product identifier |

## Technical & Engineering

| Acronym | Full Name | Description |
|---------|-----------|-------------|
| **FE** | Frontend | Client-side/UI development |
| **BE** | Backend | Server-side development |
| **E2E** | End-to-End | Full flow testing |
| **UAT** | User Acceptance Testing | Pre-launch testing phase |
| **MVP** | Minimum Viable Product | Smallest shippable feature set |
| **POC** | Proof of Concept | Technical validation prototype |
| **API** | Application Programming Interface | System integration interface |
| **GTM** | Google Tag Manager | Analytics tagging system (also: Go-To-Market) |
| **SSR** | Server-Side Rendering | Web rendering approach |
| **CLI** | Command Line Interface | Terminal-based tool |
| **MCP** | Model Context Protocol | AI tool integration standard |

## Internal Systems

| Acronym | Full Name | Description |
|---------|-----------|-------------|
| **OWL** | OWL | Payment/refund processing system |
| **Bob** | Bob | Alternative admin tool for refunds |
| **Demeter** | Demeter | UK local logistics system |
| **Odin** | Odin | Global logistics integration |
| **Katana** | Katana | Fulfillment/order management system |
| **ABBA** | ABBA | App launch initiative (Elysium) |

## Organizational

| Acronym | Full Name | Description |
|---------|-----------|-------------|
| **PM** | Product Manager | Product role |
| **EM** | Engineering Manager | Engineering leadership role |
| **PA** | Product Analytics | Analytics team/function |
| **HC** | Headcount | Team size/staffing |
| **CS4/CS5/CS6** | Career Stage 4/5/6 | HelloFresh job levels (CS4=mid, CS5=senior, CS6=staff) |
| **FT** | Full-Time | Employment type |

## Frameworks & Methodology

| Acronym | Full Name | Description |
|---------|-----------|-------------|
| **OKR** | Objectives & Key Results | Goal-setting framework |
| **PRD** | Product Requirements Document | Feature specification |
| **WBD** | Working Backwards Document | Amazon-style product brief |
| **4CQ** | Four Critical Questions | Customer/problem/solution/benefit framework |
| **BAU** | Business As Usual | Routine operations |
| **KTLO** | Keep The Lights On | Maintenance work |
| **SCM** | Supply Chain Management | Operations/logistics |
| **CRM** | Customer Relationship Management | Customer communication systems |
| **CDP** | Customer Data Platform | Unified customer data system |

## FPF (First Principles Framework)

| Acronym | Full Name | Description |
|---------|-----------|-------------|
| **FPF** | First Principles Framework | Structured reasoning methodology |
| **DRR** | Design Rationale Record | Persisted decision with context |
| **WLNK** | Weakest Link | Trust calculation: R_eff = min(evidence) |
| **CL** | Congruence Level | Evidence context matching (CL1-CL3) |
| **L0/L1/L2** | Knowledge Layers | Conjecture → Substantiated → Corroborated |

## Compliance & Standards

| Acronym | Full Name | Description |
|---------|-----------|-------------|
| **WCAG** | Web Content Accessibility Guidelines | Accessibility standard |
| **EAA** | European Accessibility Act | EU accessibility regulation |
| **GDPR** | General Data Protection Regulation | EU privacy regulation |
| **DORA** | DevOps Research and Assessment | Engineering metrics framework |

---

## Usage Notes

1. **Factor 4 = Factor Form = VMS brand** - These are interchangeable references to the same sub-brand
2. **OTP always means One-Time Purchase** in this codebase (not authentication)
3. **Career Stages (CS)** follow HelloFresh leveling: CS4 (mid), CS5 (senior), CS6 (staff), CS7+ (principal/director)
4. **CVA vs TCVA** - Often used interchangeably; TCVA is the "total" variant

---
*Last updated: 2026-01-02*