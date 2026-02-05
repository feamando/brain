# PM-OS Brain

[![PyPI version](https://badge.fury.io/py/pmos-brain.svg)](https://badge.fury.io/py/pmos-brain)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Semantic Knowledge Graph for AI Agents**

A structured knowledge management system that stores entities (people, projects, teams) as markdown files with YAML frontmatter, connected through typed relationships. Part of the [PM-OS](https://github.com/hellofresh/hf-pm-os) ecosystem.

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
```

## Entity Structure

Entities are markdown files with YAML frontmatter:

```markdown
---
type: person
name: Jane Smith
aliases: [Jane, J. Smith]
role: Senior Product Manager
relationships:
  member_of:
    - "[[Entities/Team_Consumer]]"
  owns:
    - "[[Projects/Mobile_App]]"
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
└── registry.yaml       # Entity index
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

# Format code
black src/
ruff check src/
```

## License

MIT License - see [LICENSE](LICENSE) for details.

---

*Part of [PM-OS](https://github.com/hellofresh/hf-pm-os) - Product Management Operating System*
