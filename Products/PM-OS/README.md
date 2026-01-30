# PM-OS: Product Management Operating System

**Version:** 2.5
**Last Updated:** 2026-01-12

PM-OS is an AI-powered operating system for product managers that automates context management, document generation, meeting preparation, and career planning.

---

## Feature Index

### Core Systems

| Feature | Command | Status | Description |
|---------|---------|--------|-------------|
| Boot Agent | `/boot` | Active | Initialize agent with full operational knowledge |
| Daily Context | `/update-context` | Active | Sync Google Docs, Jira, GitHub, Slack |
| Brain Loader | `/brain-load` | Active | Load semantic knowledge from Brain entities |
| Session Manager | `/session-save`, `/session-load` | Active | Persist conversation context across sessions |

### Document Generation (All with FPF)

| Feature | Command | FPF | Orthogonal | Description |
|---------|---------|-----|------------|-------------|
| PRD Generator | `/prd` | Mandatory | Optional | Product Requirements Document |
| 4CQ | `/4cq` | Mandatory | Optional | Four Critical Questions alignment |
| ADR | `/adr` | Mandatory | Optional | Architecture Decision Record |
| RFC | `/rfc` | Mandatory | Optional | Request for Comments |
| PRFAQ | `/prfaq` | Mandatory | Optional | Amazon-style Press Release FAQ |
| Sprint Report | `/sprint-report` | Lightweight | N/A | Bi-weekly sprint reports |
| Tribe Update | `/tribe-update` | Mandatory | Optional | Quarterly planning update |

### Reasoning Framework (FPF)

| Feature | Command | Description |
|---------|---------|-------------|
| Initialize | `/q0-init` | Set bounded context |
| Hypothesize | `/q1-hypothesize` | Generate hypotheses (abduction) |
| Verify | `/q2-verify` | Verify logic (deduction) |
| Validate | `/q3-validate` | Gather evidence (induction) |
| Audit | `/q4-audit` | Audit for bias |
| Decide | `/q5-decide` | Create Design Rationale Record |
| Status | `/q-status` | Show FPF state |
| Confucius | `/confucius-status` | Show captured session notes |

### People & Meetings

| Feature | Command | Status | Description |
|---------|---------|--------|-------------|
| Meeting Prep | `/meeting-prep` | Active | Generate pre-reads for calendar events |
| Career Planning | `/career-planning` | **NEW** | Track projects/feedback for promotion cases |
| Meeting Notes | `/meeting-notes` | Active | Create structured meeting notes |

### Integrations

| Feature | Command | Description |
|---------|---------|-------------|
| Jira Sync | `/jira-sync` | Fetch squad epics, blockers |
| GitHub Sync | `/github-sync` | Fetch PRs, commits |
| Confluence Sync | `/confluence-sync` | Fetch documentation |
| Statsig Sync | `/statsig-sync` | Fetch experiment data |
| Slack Bot | `/slackbot` | Process @mentions for tasks |

---

## New Features (2026-01-12)

### 1. Confucius Note-Taker Agent

**Location:** `AI_Guidance/Tools/confucius_agent.py`
**Command:** `/confucius-status`

Lightweight context capture during conversations without full FPF overhead:
- **Decisions** - Choices made with rationale
- **Assumptions** - Implicit assumptions to validate
- **Observations** - Facts worth preserving
- **Blockers** - Issues identified
- **Actions** - Tasks and follow-ups

Notes are automatically injected into FPF context during document generation.

### 2. Career Planning System

**Location:** `Planning/Career/{NAME}/`
**Command:** `/career-planning`
**Template:** `AI_Guidance/Frameworks/Career_Plan_Template.md`

Track projects and feedback for promotion cases:
- `-create {NAME}` - Initialize career plan
- `-WHAT {NAME} {CYCLE}` - Generate Body of Work section
- `-HOW {NAME} {CYCLE}` - Generate Behavioral Evidence section
- `-status {NAME}` - Show tracking status
- `-sync {NAME}` - Force sync from all sources

**Current Tracked:**
- Daniel Arias (S2026)
- Hamed Karimian (S2026)

### 3. Meeting Prep with Career Integration

**Enhanced:** `.claude/commands/meeting-prep.md`

For 1:1 meetings, automatically includes:
- Career plan status and cycle
- Recent project highlights
- Feedback summary by DNA value
- Evidence gaps to discuss

**Meeting Series Files:**
- `Planning/Meeting_Prep/Series/Series-{slug}.md` - Recurring meetings with history

### 4. Mandatory FPF in Document Commands

All document generation commands now run FPF silently:
- No `--fpf` flag needed (always on)
- Confucius context loaded automatically
- Decision Rationale section appended
- DRR stored in `Brain/Reasoning/Decisions/`

### 5. Orthogonal Challenge FPF Enhancement

**Updated:** `AI_Guidance/Tools/orthogonal_challenge.py`

Round 2 (Gemini) now challenges both document AND FPF reasoning:
- Hypothesis quality critique
- Evidence chain weakness detection
- Unvalidated assumption identification
- Assurance level audit
- Trust calculus gap detection

DRR includes FPF challenge resolutions and adjusted assurance level.

### 6. Structured Slack Mentions

**Updated:** `AI_Guidance/Tools/slack_mention_classifier.py`

New mention formats:
- `ngo-task dl-YYYYMMDD` - High-priority task for Nikita
- `task e-NAME dl-YYYYMMDD` - Task for colleague with deadline
- `info d-YYYYMMDD` - Information for Brain storage
- `question` - Questions for Nikita
- `feature` / `bug` - PM-OS feature requests

---

## Directory Structure

```
Documents/
├── .claude/
│   └── commands/           # Slash commands
├── AI_Guidance/
│   ├── Brain/
│   │   ├── Confucius/      # Session notes (NEW)
│   │   ├── Entities/       # People, squads, projects
│   │   ├── Inbox/          # Raw sync data
│   │   ├── Reasoning/      # FPF state, DRRs
│   │   └── Caches/         # Slack user cache
│   ├── Core_Context/       # Daily context files
│   ├── Frameworks/         # Templates
│   ├── Rules/              # Agent behavior
│   ├── Sessions/           # Session persistence
│   └── Tools/              # Python scripts
├── Brain/
│   └── Products/PM-OS/     # This file
├── Planning/
│   ├── Career/             # Career plans (NEW)
│   │   ├── Daniel_Arias/
│   │   └── Hamed_Karimian/
│   └── Meeting_Prep/
│       ├── Series/         # Recurring meeting pre-reads
│       ├── AdHoc/          # One-time meetings
│       └── Archive/        # Past meetings
└── Reporting/
    └── Sprint_Reports/     # Generated reports
```

---

## Configuration

| Config | Location | Purpose |
|--------|----------|---------|
| Google OAuth | `AI_Guidance/Tools/token.json` | GDrive/Calendar access |
| Squad Registry | `AI_Guidance/Tools/squad_registry.yaml` | Squad definitions |
| Slack User Cache | `AI_Guidance/Brain/Caches/slack_user_cache.json` | Name → ID mapping |

---

## Backlog

See: `Brain/Products/PM-OS/mention_backlog.md`

---

*PM-OS: Human-in-the-Loop, AI-in-the-Flow*
