---
$schema: brain://entity/system/v1
$id: entity/system/slack-user-ids
$type: system
$version: 1
$created: 2026-01-07
$updated: '2026-01-22T10:41:36.044839+00:00'
$confidence: 0.56
$source: unknown
$status: Active
$relationships:
- type: related_to
  target: entity/system/slack-channels
  since: null
  until: null
  role: null
  metadata: null
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.784477Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
- timestamp: '2026-01-22T10:41:36.044849+00:00'
  type: normalization
  actor: system/relationship_normalizer
  changes:
  - field: $relationships
    operation: normalize
    count: 1
name: Slack User IDs Registry
type: system
last_updated: 2026-01-07
---

# Slack User IDs Registry

Quick reference for Slack user IDs. Use user IDs for mentions and DMs.

## How to Use

When mentioning users in Slack messages:
```python
# Mention user
message = f"Hey <@U0R6LPVDF>, can you review this?"

# DM user
client.chat_postMessage(channel='U0R6LPVDF', text='Direct message')
```

## New Ventures Team

| Name | Slack ID | Role |
|------|----------|------|
| Nikita Gorshkov | `U03TY4YJU4X` | Group Product Manager |
| Ian Brooks | `U0R6LPVDF` | Engineering Manager |
| Jama Musse | `UHSH4MF5M` | Director, Market Innovation |
| Sameer Doda | `U02CRDYF2NL` | Product Manager |
| Daniel Arias | `UEZ4PRFKM` | Engineering |
| Ahmed Wagdi | `U8F7ZDAPM` | Engineering |
| Alison Ryan | `U1GA9435H` | Product Manager (Good Chop) |
| Maria Chelminska | `U03UMPD2NNS` | Product Manager (TPT) |

## The Pets Table (TPT)

| Name | Slack ID | Role |
|------|----------|------|
| Laurent Guillemain | `UFC7CRXMZ` | GM, The Pets Table |
| Dovas Zakas | `U3XBWJ3ND` | Product |
| Jordan Einhorn | `U0139TY5FDF` | Growth |
| Cade Kelly | `U022DLAHBUY` | Growth |
| Ceren Hapoglu | `U064HHX7ZFE` | CRM |

## Good Chop

| Name | Slack ID | Role |
|------|----------|------|
| Beatrice Dimarucut | `U01AKGWGLC8` | Product Manager |
| Yury Trofimov | `UAAJRNY8G` | Engineering |
| Seb Tron | `U01B2LBUPND` | Engineering |
| Rohan Choksi | `U01HAJCP17B` | Growth |

## Manual Lookup Needed

These team members weren't found in automated search (may use different name spellings):
- Prateek Jajoo (TPT) - try searching "prateek" in Slack
- Hamed Karimian (VMS) - try searching "hamed" in Slack
- Wellney Yarra (VMS) - try searching "wellney" in Slack

To find manually: Click profile → "..." → "Copy member ID"

## How to Find a User ID

1. **In Slack Desktop**: Click on user profile → "..." menu → "Copy member ID"
2. **Via API**:
```python
response = client.users_list()
for user in response['members']:
    if 'search_name' in user.get('real_name', '').lower():
        print(f"{user['real_name']}: {user['id']}")
```

## Related

- [[Slack_Channels.md]] - Channel IDs
- [[../../Entities/]] - Person entities with slack_id field