# DRR Templates

Design Rationale Record (DRR) templates for common decision types.

## Available Templates

| Template | Use Case | Typical Duration |
|----------|----------|------------------|
| [Architecture Decision](drr-architecture.md) | Technical architecture choices | 6-12 months |
| [Build vs Buy](drr-build-vs-buy.md) | Make or acquire decisions | 12-24 months |
| [Technology Selection](drr-technology.md) | Framework, language, tool choices | 12-18 months |
| [Process Change](drr-process.md) | Workflow or methodology changes | 6-12 months |
| [Strategic Decision](drr-strategic.md) | Business strategy decisions | 6-18 months |

## How to Use

1. Copy the appropriate template to `Brain/Reasoning/Decisions/`
2. Rename to `drr-YYYY-MM-DD-topic.md`
3. Fill in all sections
4. Update frontmatter with actual values
5. Link to related Brain entities

## Template Sections

All templates include:
- **Frontmatter** - Metadata for indexing
- **Context** - Situation requiring decision
- **Options Evaluated** - Hypotheses with scores
- **Selected Option** - The decision
- **Evidence Chain** - Supporting data
- **Bias Audit** - Cognitive bias review
- **Revisit Conditions** - When to reconsider

## Evidence Expiry Guidelines

| Decision Type | Typical Validity |
|---------------|------------------|
| Architecture | 12-18 months |
| Technology | 12-24 months |
| Process | 6-12 months |
| Strategic | 6-12 months |
| Tactical | 3-6 months |

## Best Practices

1. **Always set expiry dates** - No evidence is forever valid
2. **Link to Brain entities** - Build knowledge graph
3. **Document rejected options** - Future you will thank you
4. **Include bias audit** - Even brief review helps
5. **Define revisit conditions** - What would change your mind?
