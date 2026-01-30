---
$schema: brain://entity/system/v1
$id: entity/system/slack-channels
$type: system
$version: 1
$created: 2026-01-07
$updated: '2026-01-30T10:24:58.633085'
$confidence: 0.56
$source: unknown
$status: Active
$relationships:
- type: related_to
  target: entity/system/slack-user-ids
  confidence: 1.0
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.783603Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Slack Channels Registry
type: system
last_updated: 2026-01-07
---

# Slack Channels Registry

Quick reference for Slack channel IDs. Use channel IDs for programmatic access.

## How to Use

When posting to Slack or referencing channels in code:
```python
from slack_sdk import WebClient
client.chat_postMessage(channel='C08QWJC5ZQE', text='message')
```

## Known Channels

### AI & Technology

| Channel | ID | Type | Description |
|---------|-----|------|-------------|
| #clan-genai | `C08QWJC5ZQE` | public | GenAI community channel |

### New Ventures Tribe

| Channel | ID | Type | Description |
|---------|-----|------|-------------|
| #ngo-slack-private | `C0A6ZAS1MSQ` | private | NGO private channel |

### The Pets Table (TPT)

| Channel | ID | Type | Description |
|---------|-----|------|-------------|
| #tpt_performance_pupdates | TBD | public | TPT performance updates |
| #tpt_team | TBD | public | TPT team channel |

### Good Chop

| Channel | ID | Type | Description |
|---------|-----|------|-------------|
| #good-chop-product | TBD | public | Good Chop product discussions |
| #goodchop-shopify-internal | TBD | private | Shopify internal discussions |
| #cc-goodchop | TBD | public | Good Chop general |
| #growth-updates_goodchop | TBD | public | Good Chop growth updates |

### Factor Form / VMS

| Channel | ID | Type | Description |
|---------|-----|------|-------------|
| #factor-form | TBD | public | Factor Form team |
| #vms | TBD | public | VMS discussions |

### Consumer Mega-Alliance (CMA)

| Channel | ID | Type | Description |
|---------|-----|------|-------------|
| #consumer-mega-alliance | TBD | public | CMA tribe channel |
| #cma-lt | TBD | private | CMA leadership team |

### BNL (Benelux)

| Channel | ID | Type | Description |
|---------|-----|------|-------------|
| #bnl-2-tier-tech-requirements | TBD | public | BNL premium tier tech |

### Incidents

| Channel | ID | Type | Description |
|---------|-----|------|-------------|
| Payment Status Incident | `C0A56M4L96J` | public | Payment issues investigation |

## Channel Naming Conventions

- **Tribe channels**: `#tribe-name` or `#tribe-name-lt` (leadership)
- **Squad channels**: `#squad-name` or product-specific
- **Performance channels**: `#product_performance_pupdates`
- **Internal/private**: suffix `-internal` or `-private`
- **Clan channels**: `#clan-topic` (community of practice)

## Adding New Channels

To look up a channel ID:
1. Open Slack
2. Right-click on channel name
3. Select "Copy link"
4. Channel ID is in the URL: `slack.com/archives/CHANNEL_ID`

Or use the Slack API:
```python
response = client.conversations_list(types='public_channel,private_channel')
for ch in response['channels']:
    if 'search-term' in ch['name'].lower():
        print(f"{ch['name']}: {ch['id']}")
```

## Related

- [[../Entities/]] - People entities (add slack_id field)
- [[../../Rules/NGO.md]] - Team structure with Slack channels