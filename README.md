# PM-OS Brain

[![PyPI version](https://badge.fury.io/py/pmos-brain.svg)](https://badge.fury.io/py/pmos-brain)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Semantic Knowledge Graph with Graph Analytics & AI Enrichment**

A structured knowledge management system that stores entities (people, projects, teams) as markdown files with YAML frontmatter, connected through typed relationships. Designed for AI agents to create, manage, retrieve, and reason over organizational knowledge.

## Philosophy & Approach

### Knowledge as a Graph

Brain treats organizational knowledge as a **connected graph** rather than isolated documents:

- **Entities** are nodes (people, teams, projects, systems, decisions)
- **Relationships** are typed edges (reports_to, owns, member_of, depends_on)
- **Traversal** enables contextual retrieval (find all people connected to a project)
- **Density** measures knowledge completeness (orphan detection, relationship coverage)

### Knowledge Lifecycle

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   CREATE    │────▶│   ENRICH    │────▶│  RETRIEVE   │────▶│  MAINTAIN   │
│             │     │             │     │             │     │             │
│ • Entities  │     │ • From APIs │     │ • Search    │     │ • Quality   │
│ • Relations │     │ • From docs │     │ • Traverse  │     │ • Orphans   │
│ • Metadata  │     │ • Inference │     │ • Path find │     │ • Freshness │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

1. **Create**: Define entities with structured frontmatter and markdown content
2. **Enrich**: Pull data from external sources (Slack, Jira, GitHub, Google Docs)
3. **Retrieve**: Search, traverse relationships, find paths between entities
4. **Maintain**: Score quality, detect orphans, ensure freshness

## Installation

```bash
# Basic installation
pip install pmos-brain

# With graph analytics (networkx)
pip install pmos-brain[graph]

# With LLM providers
pip install pmos-brain[anthropic]    # Claude
pip install pmos-brain[openai]       # GPT-4
pip install pmos-brain[llm]          # All LLM providers

# With integrations
pip install pmos-brain[integrations]  # Slack, Jira, GitHub, Google

# Full installation (all features)
pip install pmos-brain[full]
```

## Quick Start

```python
from pmos_brain import Brain

brain = Brain("./my-brain")

# Search entities
results = brain.search("product manager")

# Get specific entity
person = brain.get("Entities/Jane_Smith")

# Traverse relationships (find connected entities)
neighbors = brain.traverse("Entities/Jane_Smith", depth=2)

# Get health report
report = brain.health_report()
print(f"Density: {report['density_score']}, Orphans: {report['orphan_entities']}")
```

## Core Modules

### 1. Entity Management (Core)

Store and manage entities as markdown files with YAML frontmatter:

```python
from pmos_brain import Brain

brain = Brain("./my-brain")

# CRUD operations
entity = brain.get("Entities/Jane_Smith")
results = brain.search("mobile app", entity_type="project")
entities = brain.list_entities(entity_type="person")

# Create new entity
project = brain.create(
    name="Mobile App v2",
    entity_type="project",
    metadata={"status": "active", "owner": "entity/person/jane"}
)

# Update and delete
brain.update(entity)
brain.delete("Entities/Old_Project")
```

**Entity Structure:**
```markdown
---
$id: entity/person/jane-smith
$type: person
$schema: entity-v2
name: Jane Smith
role: Senior Product Manager
$relationships:
  - type: member_of
    target: entity/team/consumer
    confidence: 1.0
  - type: owns
    target: entity/project/mobile-app
    since: "2024-01-15"
---

# Jane Smith

Senior Product Manager leading the Mobile App initiative.
```

### 2. Graph Traversal & Analytics

Navigate the knowledge graph to find connected information:

```python
from pmos_brain import Brain, BrainGraph

brain = Brain("./my-brain")

# Expand from seed entities (TKS-based traversal)
result = brain.graph.expand(
    seeds=["entity/person/jane"],
    depth=2,           # How far to traverse
    decay=0.5,         # Score decay per hop
    relationship_types=["member_of", "owns"]  # Filter relationships
)

for node in result.neighbors:
    print(f"{node.entity_id}: score={node.score}, via={node.via_relationship}")

# Find shortest path between entities
path = brain.shortest_path(
    from_entity="entity/person/jane",
    to_entity="entity/project/mobile-app"
)
# Returns: ["entity/person/jane", "entity/team/consumer", "entity/project/mobile-app"]

# Find connected components (isolated subgraphs)
components = brain.connected_components()
```

### 3. Graph Health & Metrics

Monitor knowledge graph density and completeness:

```python
from pmos_brain import Brain, GraphHealth

brain = Brain("./my-brain")

# Full health report
report = brain.health_report()
print(f"""
Total entities: {report['total_entities']}
Relationship coverage: {report['relationship_coverage']*100:.1f}%
Density score: {report['density_score']:.2f} (1.0 = healthy)
Orphan entities: {report['orphan_entities']}
""")

# Get detailed orphan list
orphans = brain.find_orphans()
for orphan in orphans:
    print(f"[{orphan['type']}] {orphan['id']} - {orphan['name']}")

# Most/least connected entities
print("Most connected:", report['most_connected'][:5])
```

### 4. Quality Scoring (TKS κ)

Assess entity completeness and data quality:

```python
from pmos_brain import Brain, QualityScorer

brain = Brain("./my-brain")

# Score single entity
score = brain.score_entity("Entities/Jane_Smith.md")
print(f"""
Overall: {score['overall_score']:.2f}
Completeness: {score['completeness']:.2f}
Freshness: {score['freshness']:.2f}
Relationships: {score['relationships']:.2f}
κ (kappa): {score['kappa']:.3f}

Issues: {score['issues']}
Recommendations: {score['recommendations']}
""")

# Quality summary across all entities
summary = brain.quality_summary()
print(f"Average quality: {summary['average_overall']:.2f}")
print(f"Distribution: {summary['distribution']}")
print(f"Top issues: {summary['top_issues'][:5]}")
```

**Scoring Formula:**
- **Completeness (40%)**: Required + optional field coverage (κ-weighted)
- **Source Reliability (40%)**: Based on data source (HR system > Jira > Slack > manual)
- **Freshness (20%)**: Decay 0.01/week from last update

### 5. Enrichment Pipeline

Automatically enrich entities from external data sources:

```python
from pmos_brain import Brain, EnrichmentPipeline

brain = Brain("./my-brain")

# Run enrichment from specific sources
results = brain.enrich(
    sources=["gdocs", "slack", "jira"],
    dry_run=False  # Set True to preview
)

print(f"""
Processed: {results['processed']}
Successful: {results['successful']}
Failed: {results['failed']}
""")

# Or use pipeline directly for more control
pipeline = EnrichmentPipeline(
    brain_path="./my-brain",
    max_workers=4,      # Parallel execution
    batch_size=10,      # Items per batch
    rate_limit=60,      # Requests/minute
)

pipeline.run(sources=["slack"], resume=True)
```

**Supported Sources:**
- `gdocs` - Google Docs mentions and references
- `slack` - Slack messages and channel activity
- `jira` - Jira tickets, assignments, comments
- `github` - GitHub PRs, issues, commits
- `context` - Daily context files

### 6. Relationship Management

Build and maintain bidirectional relationships:

```python
from pmos_brain import Brain, RelationshipBuilder

brain = Brain("./my-brain")

# Create bidirectional relationship (automatically creates inverse)
result = brain.create_relationship(
    source_id="entity/person/jane",
    target_id="entity/team/consumer",
    relationship_type="member_of",  # Inverse: has_member
    confidence=1.0
)

print(f"Forward ({result['forward_type']}): created={result['forward_created']}")
print(f"Inverse ({result['inverse_type']}): created={result['inverse_created']}")

# Fix missing inverse relationships across entire brain
stats = brain.fix_inverse_relationships(dry_run=False, limit=1000)
print(f"Created {stats['inverses_created']} missing inverses")
```

**Relationship Type Inverses:**
| Forward | Inverse |
|---------|---------|
| `reports_to` | `manages` |
| `member_of` | `has_member` |
| `owns` | `owned_by` |
| `depends_on` | `depended_on_by` |
| `works_with` | `works_with` (symmetric) |

### 7. Maintenance & Cleanup

Keep the knowledge graph healthy:

```python
from pmos_brain import Brain, OrphanAnalyzer

brain = Brain("./my-brain")

# Analyze orphan entities
analysis = brain.analyze_orphans()
print(f"""
Total orphans: {analysis['total_orphans']}
Orphan rate: {analysis['orphan_rate']:.1f}%
By type: {analysis['by_type']}
By reason: {analysis['by_reason']}
""")

# Mark orphans for enrichment
stats = brain.cleanup_orphans(dry_run=False)
print(f"Marked pending: {stats['marked_pending']}")
print(f"Marked standalone: {stats['marked_standalone']}")
```

**Orphan Reasons:**
- `pending_enrichment` - Not yet processed by enrichers
- `no_external_data` - Enrichers found no matching data
- `standalone` - Legitimately independent (templates, glossary)
- `enrichment_failed` - Processing error occurred

### 8. Temporal Queries & Event Sourcing

Track changes over time:

```python
from pmos_brain import Brain
from datetime import datetime, timedelta

brain = Brain("./my-brain")

# Get entity state at a point in time
snapshot = brain.temporal.get_entity_at(
    entity_path=brain.path / "Entities/Jane_Smith.md",
    point_in_time=datetime(2024, 1, 1)
)

# Compare states between two times
diff = brain.temporal.compare_states(
    entity_path=brain.path / "Entities/Jane_Smith.md",
    time_a=datetime(2024, 1, 1),
    time_b=datetime.now()
)
print(f"Field changes: {diff['field_changes']}")

# Get changes in a time period
changes = brain.temporal.get_changes_in_period(
    start=datetime.now() - timedelta(days=30),
    end=datetime.now()
)
print(f"Entities changed: {changes['entities_changed']}")

# Query events
events = brain.events.query_events(
    since=datetime.now() - timedelta(days=7),
    event_types=["field_updated", "relationship_added"]
)
```

## CLI Commands

```bash
# Basic operations
pmos-brain search "product manager"
pmos-brain get Entities/Jane_Smith
pmos-brain list --type person

# Graph operations
brain-graph health              # Health report
brain-graph traverse Jane_Smith --depth 2
brain-graph path Jane_Smith --to Mobile_App

# Quality operations
brain-quality score Entities/Jane_Smith.md
brain-quality report            # Full quality report
brain-quality orphans --fix     # Find/fix orphans

# Enrichment
brain-enrich --sources gdocs slack
brain-enrich --dry-run          # Preview mode

# Setup and validation
pmos-brain setup ./my-brain
pmos-brain validate
```

## LLM Providers

Brain supports multiple LLM providers for entity extraction and enrichment:

| Provider | Models | Best For |
|----------|--------|----------|
| **Anthropic** | claude-sonnet-4, claude-opus-4 | Entity extraction, reasoning |
| **OpenAI** | gpt-4o, o1, o3-mini | General purpose, embeddings |
| **Gemini** | gemini-2.0-flash, gemini-2.0-pro | Fast summarization |
| **Ollama** | llama3.2, qwen2.5, deepseek-r1 | Local/offline, privacy |

```python
from pmos_brain import LLMClient

client = LLMClient(provider="anthropic")
response = client.complete("Extract person names from: ...")
```

## Directory Structure

```
my-brain/
├── Entities/           # People, teams, companies
│   ├── Jane_Smith.md
│   └── Team_Consumer.md
├── Projects/           # Active projects
│   └── Mobile_App.md
├── Architecture/       # Technical documentation
├── Strategy/           # Strategic documents
├── Decisions/          # ADRs and decisions
├── Inbox/              # Unprocessed data from integrations
│   ├── Slack/
│   ├── Jira/
│   └── GDocs/
├── .schema/            # Entity schemas (JSON Schema)
├── .snapshots/         # Point-in-time snapshots
└── registry.yaml       # Entity index
```

## Configuration

Create `config.yaml` in your brain directory:

```yaml
llm:
  provider: anthropic
  fallback: [openai, ollama]

enrichment:
  sources: [gdocs, slack, jira]
  rate_limit: 60  # requests/minute

quality:
  min_score: 0.6
  required_fields:
    person: [name, role, team]
    project: [owner, status]
```

## Development

```bash
git clone https://github.com/feamando/brain.git
cd brain
pip install -e ".[dev]"
pytest
```

## License

MIT License - see [LICENSE](LICENSE) for details.

---

*Part of [PM-OS](https://github.com/hellofresh/hf-pm-os) - Product Management Operating System*
