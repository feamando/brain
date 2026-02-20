# PM-OS Brain

```
                        ╭────╮
                   ╭────┤ ●  ├────╮
                   │    ╰──┬─╯    │
                ╭──┴─╮    │   ╭──┴─╮
           ╭────┤ ●  ├────┼───┤ ●  ├────╮
           │    ╰──┬─╯    │   ╰──┬─╯    │
        ╭──┴─╮    │   ╭──┴─╮    │   ╭──┴─╮
        │ ●  ├────┼───┤ ●  ├────┼───┤ ●  │
        ╰──┬─╯    │   ╰──┬─╯    │   ╰──┬─╯
           │    ╭──┴─╮    │   ╭──┴─╮    │
           ╰────┤ ●  ├────┼───┤ ●  ├────╯
                ╰──┬─╯    │   ╰──┬─╯
                   │    ╭──┴─╮    │
                   ╰────┤ ●  ├────╯
                        ╰────╯

        ██████╗ ██████╗  █████╗ ██╗███╗   ██╗
        ██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║
        ██████╔╝██████╔╝███████║██║██╔██╗ ██║
        ██╔══██╗██╔══██╗██╔══██║██║██║╚██╗██║
        ██████╔╝██║  ██║██║  ██║██║██║ ╚████║
        ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝

         Semantic Knowledge Graph for AI Agents
```

[![PyPI version](https://badge.fury.io/py/pmos-brain.svg)](https://badge.fury.io/py/pmos-brain)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A structured knowledge management system that stores entities (people, projects, teams) as markdown files with YAML frontmatter, connected through typed relationships. Includes event sourcing, a compressed entity index generator, vector search, MCP server, and graph analytics. Part of the [PM-OS](https://github.com/feamando/pm-os) ecosystem.

## What's New in v3.2.0

- **Entity Cache** — Shared in-memory cache (`EntityCache`) with single filesystem scan, O(1) access by ID/type, and SHA-256 content hashing for incremental change detection
- **Atomic Writes** — `atomic_write()` and `atomic_write_json()` utilities using temp + fsync + rename for crash-safe entity updates
- **ANN Edge Inference** — ChromaDB-backed approximate nearest neighbor search for O(k·log(n)) edge inference on large entity types, with automatic brute-force fallback
- **Cache-Integrated Graph Health** — `GraphHealth` accepts optional `EntityCache` to eliminate redundant filesystem scans during enrichment
- **CLI Improvements** — `pmos-brain enrich --dry-run` to preview changes, `--verbose` for detailed progress, enrichment summary output

```bash
# Install with vector search (includes ANN support)
pip install pmos-brain[vector]==3.2.0

# Enrichment with new flags
pmos-brain enrich --mode full --dry-run --verbose

# Use EntityCache in Python
from pmos_brain import EntityCache
cache = EntityCache(brain_path).load()
persons = cache.get_by_type("person")
```

### v3.1.0

- **MCP Server** — Expose your knowledge graph to any MCP-compatible AI client (Cursor, Windsurf, Claude Code) with 5 built-in tools
- **Vector Search** — ChromaDB + sentence-transformers semantic search across all entities with embedding-based edge inference
- **Canonical Resolver** — Multi-format entity resolution (`$id`, slug, path, alias) with fuzzy matching
- **Enhanced Search** — Inverted index with Porter stemming, O(1) alias lookup, query expansion, and optional semantic fallback
- **Brain Query** — Combined BRAIN (keyword) + GRAPH (traversal) query interface with relevance scoring
- **Enrichment Orchestrator** — Multi-mode enrichment (full/quick/report/boot/orphan) with pluggable external enrichers
- **PM Frameworks** — 35 product management framework documents for reference and agent context
- **Enhanced Orphan Analyzer** — Standalone marking, pending enrichment tracking, event audit trails

### v3.0.0

- **Event Helpers** — Pydantic-validated event creation with factory methods and automatic compaction
- **Event Query CLI** — Query entity timelines, recent activity, and event statistics
- **Brain Index Generator** — Compressed `BRAIN.md` entity index for passive agent context
- **Retrieval-Led Reasoning** — Recommended usage pattern for AI agent integration

## Installation

```bash
# Basic installation
pip install pmos-brain

# With specific LLM provider
pip install pmos-brain[anthropic]    # Claude
pip install pmos-brain[openai]       # GPT-4
pip install pmos-brain[gemini]       # Gemini
pip install pmos-brain[mistral]      # Mistral
pip install pmos-brain[ollama]       # Local models

# With all LLM providers
pip install pmos-brain[llm]

# With vector search (ChromaDB + sentence-transformers)
pip install pmos-brain[vector]

# With MCP server
pip install pmos-brain[mcp]

# With integrations
pip install pmos-brain[slack]
pip install pmos-brain[jira]
pip install pmos-brain[github]
pip install pmos-brain[integrations]  # All integrations

# Everything
pip install pmos-brain[all]
```

## Quick Start

### Python API

```python
from pmos_brain import Brain, LLMClient

# Initialize brain
brain = Brain("./my-brain")

# Search entities
results = brain.search("product manager")
for entity in results:
    print(f"{entity.name} ({entity.entity_type})")

# Get specific entity
person = brain.get("Entities/Jane_Smith")
print(person.relationships)

# Create new entity
project = brain.create(
    name="Mobile App v2",
    entity_type="project",
    content="# Mobile App v2\n\nRedesign project...",
    metadata={"status": "in_progress", "priority": "P1"}
)

# Use LLM for entity extraction
llm = LLMClient()  # Uses ANTHROPIC_API_KEY by default
response = llm.complete(
    "Extract all person names from this text: ...",
    system="Return names as a JSON array."
)
```

### CLI

```bash
# Initialize a new brain
pmos-brain setup ./my-brain

# Search entities
pmos-brain search "product manager" --brain ./my-brain

# List all entities
pmos-brain list --type person

# Get entity details
pmos-brain get Entities/Jane_Smith

# Validate brain structure
pmos-brain validate

# Query entity events
pmos-brain events timeline Entities/Jane_Smith.md
pmos-brain events recent --days 7
pmos-brain events stats --since 2026-01-01

# Generate compressed entity index
pmos-brain index --config team.yaml --output BRAIN.md

# Combined BRAIN+GRAPH query (v3.1.0)
pmos-brain query "mobile app" --limit 5
pmos-brain query "project launch" --no-graph --format json

# Semantic search (v3.1.0, requires pmos-brain[vector])
pmos-brain search "checkout flow redesign" --semantic
pmos-brain vector build                   # Build vector index
pmos-brain vector query "onboarding"      # Query vector index
pmos-brain vector stats                   # Index statistics

# Resolve entity references (v3.1.0)
pmos-brain resolve "jane-smith"
pmos-brain resolve "entity/person/jane-smith"

# Run enrichment (v3.1.0)
pmos-brain enrich --mode quick
pmos-brain enrich --mode report

# Start MCP server (v3.1.0, requires pmos-brain[mcp])
pmos-brain mcp
```

## Event Sourcing

Brain v3.0.0 introduces a structured event sourcing system. Every entity change is tracked as an immutable event in the entity's YAML frontmatter.

### Event Helpers API

```python
from pmos_brain import EventHelper

# Create a field update event
event = EventHelper.create_field_update(
    actor="system/enricher",
    field="role",
    new_value="Director",
    old_value="Senior Manager",
)

# Create a relationship event
event = EventHelper.create_relationship_event(
    actor="user/jane",
    target="entity/team/platform",
    rel_type="member_of",
    operation="add",
)

# Create a status change event
event = EventHelper.create_status_change(
    actor="system/workflow",
    old_status="active",
    new_status="archived",
)

# Append event to entity frontmatter (auto-increments version, compacts at threshold)
frontmatter = {"$version": 1, "$events": []}
EventHelper.append_to_frontmatter(frontmatter, event)
```

### Event Types

| Type | Description |
|------|-------------|
| `entity_create` | Entity was created |
| `entity_delete` | Entity was deleted |
| `field_update` | A field value changed |
| `relationship_add` | A relationship was added |
| `relationship_remove` | A relationship was removed |
| `status_change` | Entity status changed |
| `enrichment` | Data enriched from external source |
| `compacted_summary` | Summarized event group (from compaction) |

### Event Compaction

When an entity accumulates more than 10 events, automatic compaction runs: the first event (creation) and the most recent events are preserved, while middle events are summarized into a `compacted_summary` event. This keeps frontmatter lean without losing history.

### Event Query

```python
from pmos_brain import EventQuery
from pathlib import Path
from datetime import datetime, timedelta, timezone

query = EventQuery(brain_path=Path("./my-brain"))

# Get entity timeline
timeline = query.get_timeline("Entities/Jane_Smith.md")

# Recent events across all entities
since = datetime.now(timezone.utc) - timedelta(days=7)
events = query.get_recent(since=since, limit=50)

# Event statistics
stats = query.get_stats(since=since)
print(f"Total: {stats['total']}, By type: {stats['by_type']}")
```

## Brain Index Generator

The `BrainIndexGenerator` creates a compressed `BRAIN.md` file — a pipe-delimited entity index designed for loading into AI agent context windows.

### Two-Tier Architecture

- **Tier 1 (Team)**: Manager, direct reports, stakeholders — includes full relationship data
- **Tier 2 (Connected)**: One-hop relationship targets from Tier 1 + hot topics — compact format

### Usage

```python
from pmos_brain import BrainIndexGenerator
from pathlib import Path

generator = BrainIndexGenerator(
    brain_path=Path("./my-brain"),
    team_config={
        "user": {"name": "Jane Smith", "position": "Director"},
        "manager": {"id": "john-doe", "name": "John Doe", "role": "VP"},
        "reports": [
            {"id": "alice-b", "name": "Alice B", "role": "PM", "squad": "Alpha"},
        ],
        "stakeholders": [
            {"id": "bob-c", "name": "Bob C", "role": "CTO"},
        ],
    }
)

# Optional: include hot topic entities in Tier 2
generator.set_hot_topics(["mobile-app-v2", "quarterly-planning"])

content = generator.generate()
Path("BRAIN.md").write_text(content)
```

### CLI

```bash
# Generate with team config
brain-index --brain-path ./my-brain --config team.yaml --output BRAIN.md

# Or via the main CLI
pmos-brain index --brain ./my-brain --config team.yaml
```

### Output Format

```markdown
# BRAIN.md — Entity Index
<!-- Generated: 2026-02-11T12:00:00Z | Entities: 45 | Tier1: 8 | Tier2: 37 -->

## Team (Tier 1)
id|type|role|squad|status|relationships
jane-smith|person|Director||active|manages:alice-b,member_of:leadership
alice-b|person|PM|Alpha|active|reports_to:jane-smith,owns:mobile-app

## Connected Entities (Tier 2)
id|type|name|status
mobile-app|project|Mobile App|active
platform-team|team|Platform Team|active
```

## MCP Server

The Brain MCP server exposes your knowledge graph to any MCP-compatible AI client (Cursor, Windsurf, Claude Code, etc.).

### Tools

| Tool | Description |
|------|-------------|
| `search_entities` | Keyword + semantic search across entities |
| `get_entity` | Retrieve full entity content by path |
| `query_knowledge` | Combined BRAIN+GRAPH query |
| `get_relationships` | Get entity relationships |
| `list_entities` | List entities by type |

### Usage

```bash
# Start the MCP server
pmos-brain mcp --brain ./my-brain

# Or set brain path via environment variable
export BRAIN_PATH=./my-brain
python -m pmos_brain.mcp.server
```

### MCP Client Configuration

Add to your MCP client config (e.g., Cursor `mcp.json`):

```json
{
  "brain": {
    "command": "brain-mcp",
    "env": {
      "BRAIN_PATH": "/path/to/your/brain"
    }
  }
}
```

## Vector Search

ChromaDB-powered semantic search using sentence-transformers embeddings. Enables fuzzy, meaning-based entity discovery.

```python
from pmos_brain.vector import BrainVectorIndex, VECTOR_AVAILABLE

if VECTOR_AVAILABLE:
    vi = BrainVectorIndex(brain_path=Path("./my-brain"))

    # Build/rebuild the index
    vi.build()

    # Semantic search
    results = vi.query("checkout flow redesign", n_results=10)
    for r in results:
        print(f"{r['id']} (distance: {r['distance']:.3f})")
```

### Embedding Edge Inference

Automatically discover potential relationships between entities based on embedding similarity:

```python
from pmos_brain.vector.edge_inferrer import EmbeddingEdgeInferrer

inferrer = EmbeddingEdgeInferrer(brain_path=Path("./my-brain"))
report = inferrer.infer_edges(entity_type="person", threshold=0.7)

for edge in report.edges:
    print(f"{edge.source} → {edge.target} (confidence: {edge.confidence:.2f})")
```

## Canonical Resolver

Resolve entity references in any format to their canonical path:

```python
from pmos_brain import CanonicalResolver

resolver = CanonicalResolver(brain_path=Path("./my-brain"))

# All of these resolve to the same entity
resolver.resolve("jane-smith")                    # slug
resolver.resolve("entity/person/jane-smith")      # $id
resolver.resolve("Entities/Jane_Smith.md")        # file path
resolver.resolve("Jane")                          # alias

# Find similar entities (fuzzy matching)
resolver.find_similar("jne-smith", limit=5)
```

## Enrichment Orchestrator

Multi-mode enrichment pipeline for improving graph density and data quality:

```python
from pmos_brain.enrichers.orchestrator import BrainEnrichmentOrchestrator

orchestrator = BrainEnrichmentOrchestrator(brain_path=Path("./my-brain"))

# Full enrichment: health → soft edges → decay scan → hints → health comparison
result = orchestrator.run(mode="full")

# Quick mode: only soft edge inference
result = orchestrator.run(mode="quick")

# Report mode: analysis only, no changes
result = orchestrator.run(mode="report")

# Orphan cleanup: 4-phase orphan resolution
result = orchestrator.run(mode="orphan")
```

### Pluggable External Enrichers

Register custom enrichers for your data sources:

```python
from pmos_brain.enrichers.orchestrator import BrainEnrichmentOrchestrator, ExternalEnricher

class MySlackEnricher:
    """Implements ExternalEnricher protocol."""
    def enrich_entity(self, entity_path, brain_path) -> dict:
        # Your enrichment logic here
        return {"relationships_added": 3}

orchestrator = BrainEnrichmentOrchestrator(brain_path=Path("./my-brain"))
orchestrator.register_enricher(MySlackEnricher())
result = orchestrator.run(mode="full")
```

## PM Frameworks

Brain v3.1.0 includes 35 product management framework documents in the `frameworks/` directory. These can be loaded into agent context or used as reference material:

- Competitive Analysis
- Conducting User Interviews
- Designing Growth Loops
- Evaluating Trade-offs
- Planning Under Uncertainty
- Prioritization Frameworks
- Writing Product Specs
- ...and 28 more

## Retrieval-Led Reasoning

Research on AI agent architectures (Vercel, 2025) shows that **passive context** — loading relevant knowledge into an agent's context window at session start — significantly outperforms tool-based retrieval for structured knowledge tasks. In benchmarks, agents with pre-loaded context achieved 100% task pass rates versus 53% for agents relying on tool calls to retrieve information on demand.

### Why This Matters

Tool-based retrieval (e.g., "search for person X, then read their file") introduces latency, costs tokens on tool orchestration, and creates failure modes when the agent doesn't know what to search for. Passive context gives the agent immediate access to the knowledge graph structure without any tool calls.

### Recommended Pattern

1. **Generate** `BRAIN.md` at session start (or after enrichment runs)
2. **Load** `BRAIN.md` into the agent's system prompt or initial context
3. **Instruct** the agent to consult the index before referencing entities

Example system prompt snippet:

```
You have access to the entity index in BRAIN.md. Before referencing any person,
team, project, or system, check BRAIN.md first. For entities not in the index,
use the brain_loader tool or read the entity file directly.
```

### When to Regenerate

- After enrichment pipeline runs (new data ingested)
- At the start of each agent session
- After significant entity changes (new team members, project status updates)

The compressed pipe-delimited format keeps the index under ~8KB, small enough for any context window while covering 100+ entities.

## Entity Structure

Entities are markdown files with YAML frontmatter:

```markdown
---
$type: person
$version: 3
$status: active
$updated: "2026-02-11T10:00:00Z"
name: Jane Smith
aliases: [Jane, J. Smith]
role: Senior Product Manager
$relationships:
  - type: member_of
    target: "entity/team/consumer"
  - type: owns
    target: "entity/project/mobile-app"
$events:
  - event_id: evt-abc123
    type: entity_create
    actor: system/setup
    timestamp: "2026-01-15T09:00:00Z"
    changes:
      - field: $schema
        operation: set
        value: brain://entity/person/v1
    message: Created entity
---

# Jane Smith

Senior Product Manager on the Consumer team.

## Current Focus
- Mobile App v2 redesign
- Push notification strategy
```

## LLM Providers

Brain supports multiple LLM providers with automatic fallback:

| Provider | Models (Latest) | Best For |
|----------|-----------------|----------|
| **Anthropic** | claude-sonnet-4-20250514, claude-opus-4-20250514 | Entity extraction, reasoning |
| **OpenAI** | gpt-4o, o1, o3-mini | General purpose, embeddings |
| **Gemini** | gemini-2.0-flash-exp, gemini-2.0-pro-exp | Fast summarization |
| **Mistral** | mistral-large-2411, codestral-2405 | Balanced cost/quality |
| **Ollama** | llama3.2, qwen2.5, deepseek-r1, phi4 | Local/offline, privacy |
| **Groq** | llama-3.3-70b-versatile | Ultra-fast inference |
| **Bedrock** | claude-3-5-sonnet, amazon.nova-pro | Enterprise AWS |

```python
from pmos_brain import LLMClient

# Uses config/env for provider selection
client = LLMClient()

# Or specify provider
client = LLMClient(provider="anthropic")

# With fallback
client = LLMClient(
    provider="anthropic",
    fallback=["openai", "ollama"]
)

# Generate completion
response = client.complete("What is 2+2?")
print(response.content)

# Generate embeddings
embeddings = client.embed(["text to embed"])
print(embeddings.dimensions)
```

## Configuration

Create `config.yaml` in your brain directory:

```yaml
llm:
  provider: anthropic
  fallback: [openai, gemini, ollama]
  providers:
    anthropic:
      model: claude-sonnet-4-20250514
    openai:
      model: gpt-4o
      embedding_model: text-embedding-3-large

# Team config for Brain Index Generator
user:
  name: "Jane Smith"
  position: "Director of Product"

team:
  manager:
    id: john-doe
    name: "John Doe"
    role: "VP of Product"
  reports:
    - id: alice-engineer
      name: "Alice Engineer"
      role: "Staff Engineer"
      squad: "Platform"
  stakeholders:
    - id: bob-designer
      name: "Bob Designer"
      role: "Head of Design"
```

Or use environment variables:

```bash
export LLM_PROVIDER=anthropic
export ANTHROPIC_API_KEY=sk-ant-...
export LLM_FALLBACK_ORDER=openai,ollama
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
├── Inbox/              # Unprocessed data
├── .schema/            # Entity schemas
├── .chroma/            # Vector index (generated by pmos-brain vector build)
├── frameworks/         # PM framework reference docs
├── registry.yaml       # Entity index
├── BRAIN.md            # Compressed entity index (generated)
└── config.yaml         # Configuration
```

## Development

```bash
# Clone repo
git clone https://github.com/feamando/brain.git
cd brain

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Run specific tests
pytest tools/tests/test_event_helpers.py -v

# Format code
black src/
ruff check src/
```

## License

MIT License - see [LICENSE](LICENSE) for details.

---

*Part of [PM-OS](https://github.com/feamando/pm-os) - Product Management Operating System*
