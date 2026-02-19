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

__version__ = "3.1.0"
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
from pmos_brain.storage.event_helpers import EventHelper, EventType
from pmos_brain.storage.event_query import EventQuery

# Vector (optional — requires chromadb + sentence-transformers)
try:
    from pmos_brain.vector import BrainVectorIndex, VECTOR_AVAILABLE
except ImportError:
    BrainVectorIndex = None
    VECTOR_AVAILABLE = False

try:
    from pmos_brain.vector.edge_inferrer import EmbeddingEdgeInferrer
except ImportError:
    EmbeddingEdgeInferrer = None

# Resolver
from pmos_brain.resolver.canonical import CanonicalResolver

# Query
from pmos_brain.core.query import BrainQuery, QueryResult

# Enrichment Orchestrator
from pmos_brain.enrichers.orchestrator import BrainEnrichmentOrchestrator

# Index
from pmos_brain.core.index_generator import BrainIndexGenerator

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
    "EventHelper",
    "EventType",
    "EventQuery",

    # Vector
    "BrainVectorIndex",
    "VECTOR_AVAILABLE",
    "EmbeddingEdgeInferrer",

    # Resolver
    "CanonicalResolver",

    # Query
    "BrainQuery",
    "QueryResult",

    # Enrichment Orchestrator
    "BrainEnrichmentOrchestrator",

    # Index
    "BrainIndexGenerator",

    # Meta
    "__version__",
]
