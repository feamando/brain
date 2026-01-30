---
$schema: brain://entity/system/v1
$id: entity/system/hellofresh-github-rules
$type: system
$version: 7
$created: '2026-01-22T08:31:01.095558Z'
$updated: '2026-01-30T14:33:13.180652+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.095558Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/system/v1
  message: Migrated from v1 to v2 schema
name: Hellofresh Github Rules
---

# HelloFresh GitHub Repository Rules

Reference for all PRs to hellofresh/* repositories. Enforced via [Mergeable](https://github.com/mergeability/mergeable).

## Branch Naming (Private Repos)

**Required format:** `<prefix>/<JIRA-TICKET>[-description]`

Valid prefixes:
- `major/`, `release/`, `minor/`, `feature/` - Feature branches
- `patch/`, `issue/`, `hotfix/` - Fix branches
- `dependabot/`, `whitesource/` - Dependency updates

**Jira ticket rules:**
- Must be UPPERCASE (e.g., `PEP-263`, not `pep-263`)
- Must exist in Jira and be accessible by `jira-users-hellofresh`
- Regex: `[A-Z][A-Z0-9]+-\d+`

**Examples:**
```
feature/PEP-263-pm-os-v2.3          # Good
PEP-263/feat-pm-os-distribution     # Good
patch/EES-2021                       # Good
feature/add-new-tool                 # BAD - no Jira ticket
feature/pep-263-lowercase            # BAD - lowercase ticket
```

## Pull Request Requirements

| Rule | Requirement |
|------|-------------|
| **Title** | Cannot contain `WIP` or `wip` |
| **Labels** | Cannot have a `WIP` label |
| **Description** | Cannot be empty |
| **Approvals** | Minimum 1 developer review |

## Special Cases

### AI-Generated PRs (Cursor bot)
- Requires **2 approvals** instead of 1
- Use `Co-Authored-By: Claude <noreply@anthropic.com>` for Claude-assisted PRs

### Security Repos (`mergeable-security` topic)
- Requires approval from `@hellofresh/security` team

### Ownership Labels (`mergeable-ownership-labels` topic)
- Requires `squad: <name>` and `tribe: <name>` labels

### Dependabot
- Exempt from all rules (auto-approved)

### Public Repos
- Branch naming (Jira ticket) NOT required
- Still require non-WIP title/labels and non-empty description

## Workflow

1. Create branch with Jira ticket: `feature/TICKET-123-description`
2. Make changes and push
3. Create PR with meaningful title (no WIP) and description
4. Wait for checks to pass
5. Get 1 developer approval
6. Merge

## Troubleshooting

**"Branch name must match regex definition"**
- Add Jira ticket to branch name: `git checkout -b TICKET-123/your-branch`

**"Jira ticket does not exist"**
- Verify ticket exists in Jira
- Ensure ticket is UPPERCASE
- Check project is accessible by `jira-users-hellofresh`

**Mergeable stuck**
- Check [GitHub Status](https://www.githubstatus.com/) for webhook issues
- Re-trigger by: adding label, editing title, or editing description
- Contact #tribe-platform if persistent

## Reference

- [User Guide](https://github.com/hellofresh/.github/tree/master/docs)
- [Mergeable Config](https://github.com/hellofresh/.github/blob/master/.github/mergeable.yml)
- [Code Risk Management](https://github.com/hellofresh/engineering-playbook/blob/master/docs/code-risk-management.md)
