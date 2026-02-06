"""
PM-OS Brain - Semantic Knowledge Graph with Graph Analytics & AI Enrichment

A structured knowledge management system that stores entities (people, projects,
teams) as markdown files with YAML frontmatter, connected through typed relationships.

Features:
- Entity management (CRUD operations)
- Graph traversal and analytics
- Quality scoring (TKS κ scoring)
- Enrichment pipeline
- Relationship management
- Temporal queries and event sourcing

Quick Start:
    from pmos_brain import Brain

    # Initialize brain
    brain = Brain("./my-brain")

    # Search entities
    results = brain.search("project manager")

    # Load specific entity
    entity = brain.get("Entities/Jane_Smith")

    # Graph operations
    neighbors = brain.graph.expand(["entity/person/jane"])
    health = brain.health_report()

    # Quality scoring
    score = brain.quality.score_entity(entity_path)

For more information, see: https://github.com/feamando/brain
"""

__version__ = "2.0.0"
__author__ = "PM-OS Team"

# Core
from pmos_brain.core.brain import Brain
from pmos_brain.core.entity import Entity
from pmos_brain.core.loader import BrainLoader
from pmos_brain.core.search import BrainSearch

# LLM
from pmos_brain.llm.client import LLMClient, get_llm_client

# Graph
from pmos_brain.graph.brain_graph import BrainGraph, GraphNode, TraversalResult
from pmos_brain.graph.graph_health import GraphHealth, GraphHealthReport
from pmos_brain.graph.temporal_query import TemporalQuery, EntitySnapshot

# Quality
from pmos_brain.quality.scorer import QualityScorer, QualityScore

# Enrichment
from pmos_brain.enrichers.pipeline import EnrichmentPipeline, EnrichmentResult
from pmos_brain.enrichers.base_enricher import BaseEnricher

# Relationships
from pmos_brain.relationships.builder import RelationshipBuilder, RelationshipResult

# Maintenance
from pmos_brain.maintenance.orphan_analyzer import OrphanAnalyzer, OrphanAnalysis

# Storage
from pmos_brain.storage.event_store import EventStore, Event

__all__ = [
    # Core
    "Brain",
    "Entity",
    "BrainLoader",
    "BrainSearch",

    # LLM
    "LLMClient",
    "get_llm_client",

    # Graph
    "BrainGraph",
    "GraphNode",
    "TraversalResult",
    "GraphHealth",
    "GraphHealthReport",
    "TemporalQuery",
    "EntitySnapshot",

    # Quality
    "QualityScorer",
    "QualityScore",

    # Enrichment
    "EnrichmentPipeline",
    "EnrichmentResult",
    "BaseEnricher",

    # Relationships
    "RelationshipBuilder",
    "RelationshipResult",

    # Maintenance
    "OrphanAnalyzer",
    "OrphanAnalysis",

    # Storage
    "EventStore",
    "Event",

    # Meta
    "__version__",
]
