---
type: person
name: Jane Smith
aliases:
  - Jane
  - J. Smith
  - jsmith
role: Senior Product Manager
team: Consumer Products
email: jane.smith@example.com
slack_id: U0123456789
$version: 3
$status: active
$updated: "2026-02-10T14:30:00Z"
relationships:
  member_of:
    - "[[Entities/Team_Consumer]]"
  owns:
    - "[[Projects/Mobile_App_v2]]"
  reports_to:
    - "[[Entities/John_Director]]"
$events:
  - event_id: "evt-a1b2c3d4e5f6"
    timestamp: "2026-01-15T09:00:00Z"
    type: entity_create
    actor: system/unified_writer
    changes:
      - field: "$schema"
        operation: set
        value: "brain://entity/person/v1"
    message: "Created entity from onboarding sync"
  - event_id: "evt-f6e5d4c3b2a1"
    timestamp: "2026-02-01T11:00:00Z"
    type: relationship_add
    actor: system/relationship_builder
    changes:
      - field: "$relationships"
        operation: append
        value:
          type: owns
          target: "entity/project/mobile-app-v2"
    message: "Relationship add: owns -> entity/project/mobile-app-v2"
  - event_id: "evt-c3d4e5f6a1b2"
    timestamp: "2026-02-10T14:30:00Z"
    type: field_update
    actor: system/jira_enricher
    changes:
      - field: role
        operation: set
        value: "Senior Product Manager"
        old_value: "Product Manager"
    message: "Updated role from Jira sync"
    source: "jira:PM-456"
created: 2026-01-15
updated: 2026-02-10
---

# Jane Smith

Senior Product Manager on the Consumer Products team.

## Background

- Joined: January 2025
- Previous: Product Lead at TechCorp
- Focus: Mobile experiences and user engagement

## Current Focus

- Mobile App v2 redesign
- Push notification strategy
- User onboarding optimization

## Communication Preferences

- Prefers Slack for quick questions
- Email for formal requests
- Available 9am-6pm CET

## Notes

Key stakeholder for all mobile-related initiatives.
