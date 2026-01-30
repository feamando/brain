# Brain/Reasoning

Structured reasoning knowledge integrated with Quint Code (FPF - First Principles Framework).

## Directory Structure

```
Reasoning/
├── Active/       # Current FPF reasoning cycles (synced from .quint/sessions/)
├── Decisions/    # Design Rationale Records (DRRs) - final decisions with audit trail
├── Hypotheses/   # Historical claims at L0/L1/L2 levels
└── Evidence/     # Validated evidence archive with expiry tracking
```

## Knowledge Assurance Levels

| Level | Name | Meaning | Source |
|-------|------|---------|--------|
| **L0** | Conjecture | Unverified hypothesis | `/q1-hypothesize` |
| **L1** | Substantiated | Logically verified | `/q2-verify` |
| **L2** | Corroborated | Empirically validated | `/q3-validate` |
| **Invalid** | Falsified | Failed verification | Kept for learning |

## Key Concepts

- **WLNK (Weakest Link):** `R_eff = min(evidence)`, never average
- **Congruence (CL):** How well external evidence matches our context
- **DRR:** Design Rationale Record - persisted decision with full audit trail
- **Transformer Mandate:** AI generates options, human decides

## Sync with .quint/

This directory mirrors `.quint/` for Brain integration:

```
.quint/decisions/  →  Brain/Reasoning/Decisions/
.quint/knowledge/  →  Brain/Reasoning/Hypotheses/
.quint/evidence/   →  Brain/Reasoning/Evidence/
.quint/sessions/   →  Brain/Reasoning/Active/
```

Run `python3 AI_Guidance/Tools/quint_brain_sync.py` to synchronize.

## Related

- [[Projects/OTP.md]] - Example project using FPF
- `/q-status` - Check current reasoning state
- `/q-query` - Search knowledge base
