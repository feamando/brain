# Inbox

Transient storage for raw data dumps from `daily_context_updater.py`.

## Status

**Current:** Empty (all items processed)

## Workflow

1. Raw data arrives here from `daily_context_updater.py` output
2. Agent synthesizes raw data into `Core_Context/YYYY-MM-DD-NN-context.md`
3. `brain_updater.py` appends changelog entries to relevant Brain files
4. Inbox files are moved to `Archive/` after processing

## Archive

Processed inbox files are stored in `Archive/` for historical reference.
These files contain raw email/document dumps that have been synthesized.

| Date | Files | Size | Status |
|------|-------|------|--------|
| 2025-12-05 | 4 files | 2.4MB | Archived |

## Cleanup Policy

- Archive files older than 30 days may be deleted
- Keep at least one week of archives for debugging
