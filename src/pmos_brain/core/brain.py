"""
Brain - Main interface for the knowledge graph.

Enhanced with graph operations, quality scoring, and enrichment.

Usage:
    from pmos_brain import Brain

    brain = Brain("./my-brain")

    # Search
    results = brain.search("product manager")

    # Get entity
    entity = brain.get("Entities/Jane_Smith")

    # Graph operations
    neighbors = brain.traverse("Entities/Jane_Smith", depth=2)
    health = brain.health_report()

    # Quality scoring
    score = brain.score_entity(entity.path)

    # List all
    entities = brain.list_entities()
"""

from pathlib import Path
from typing import Optional, List, Dict, Any, Union

from pmos_brain.core.entity import Entity
from pmos_brain.core.loader import BrainLoader
from pmos_brain.core.search import BrainSearch


class Brain:
    """
    Main interface for interacting with the Brain knowledge graph.

    The Brain stores entities as markdown files with YAML frontmatter,
    organized in directories by type (Entities, Projects, etc.).

    Enhanced with:
    - Graph traversal and analytics
    - Quality scoring
    - Enrichment pipeline
    - Maintenance tools
    """

    def __init__(self, path: Union[str, Path], config: Optional[Dict[str, Any]] = None):
        """
        Initialize Brain instance.

        Args:
            path: Path to brain directory
            config: Optional configuration dict
        """
        self.path = Path(path).resolve()
        self.config = config or {}

        self._loader = BrainLoader(self.path)
        self._search = BrainSearch(self.path)

        # Lazy-loaded components
        self._graph = None
        self._health = None
        self._quality = None
        self._relationships = None
        self._orphans = None
        self._temporal = None
        self._events = None
        self._pipeline = None

        if not self.path.exists():
            raise FileNotFoundError(f"Brain directory not found: {self.path}")

    # ==========================================================================
    # Core Operations (existing)
    # ==========================================================================

    def get(self, entity_path: str) -> Optional[Entity]:
        """
        Get an entity by path.

        Args:
            entity_path: Relative path like "Entities/Jane_Smith" or "Projects/Mobile_App"

        Returns:
            Entity object or None if not found
        """
        return self._loader.load(entity_path)

    def search(
        self,
        query: str,
        entity_type: Optional[str] = None,
        limit: int = 50,
    ) -> List[Entity]:
        """
        Search for entities matching query.

        Args:
            query: Search query
            entity_type: Filter by type (person, project, team, etc.)
            limit: Maximum results

        Returns:
            List of matching entities
        """
        return self._search.search(query, entity_type=entity_type, limit=limit)

    def list_entities(
        self,
        entity_type: Optional[str] = None,
        directory: Optional[str] = None,
    ) -> List[Entity]:
        """
        List all entities.

        Args:
            entity_type: Filter by type
            directory: Filter by directory (Entities, Projects, etc.)

        Returns:
            List of entities
        """
        return self._loader.list_all(entity_type=entity_type, directory=directory)

    def create(
        self,
        name: str,
        entity_type: str,
        content: str = "",
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Entity:
        """
        Create a new entity.

        Args:
            name: Entity name
            entity_type: Type (person, project, team, etc.)
            content: Markdown content
            metadata: YAML frontmatter data

        Returns:
            Created entity
        """
        return self._loader.create(name, entity_type, content, metadata)

    def update(self, entity: Entity) -> bool:
        """
        Update an existing entity.

        Args:
            entity: Entity to update

        Returns:
            True if successful
        """
        return self._loader.save(entity)

    def delete(self, entity_path: str) -> bool:
        """
        Delete an entity.

        Args:
            entity_path: Path to entity

        Returns:
            True if successful
        """
        return self._loader.delete(entity_path)

    def resolve(self, alias: str) -> Optional[Entity]:
        """
        Resolve an alias to an entity.

        Args:
            alias: Alias or name to resolve

        Returns:
            Resolved entity or None
        """
        return self._loader.resolve_alias(alias)

    @property
    def stats(self) -> Dict[str, int]:
        """Get brain statistics."""
        return {
            "total_entities": len(self.list_entities()),
            "persons": len(self.list_entities(entity_type="person")),
            "projects": len(self.list_entities(entity_type="project")),
            "teams": len(self.list_entities(entity_type="team")),
        }

    # ==========================================================================
    # Graph Operations (NEW)
    # ==========================================================================

    @property
    def graph(self):
        """
        Get the BrainGraph component for graph traversal.

        Returns:
            BrainGraph instance
        """
        if self._graph is None:
            from pmos_brain.graph.brain_graph import BrainGraph
            self._graph = BrainGraph(self.path)
        return self._graph

    def traverse(
        self,
        start: str,
        depth: int = 2,
        decay: float = 0.5,
        relationship_types: Optional[List[str]] = None,
    ) -> List[Entity]:
        """
        Traverse the graph from a starting entity.

        Args:
            start: Starting entity ID
            depth: Traversal depth (1 = neighbors only)
            decay: Score decay factor for neighbors
            relationship_types: Filter to specific relationship types

        Returns:
            List of entities found via traversal
        """
        result = self.graph.expand(
            seeds=[start],
            depth=depth,
            decay=decay,
            relationship_types=relationship_types,
        )

        entities = []
        for node in result.neighbors:
            entity = self.get(node.entity_id)
            if entity:
                entities.append(entity)

        return entities

    def shortest_path(
        self,
        from_entity: str,
        to_entity: str,
        max_depth: int = 5,
    ) -> Optional[List[str]]:
        """
        Find shortest path between two entities.

        Args:
            from_entity: Starting entity ID
            to_entity: Target entity ID
            max_depth: Maximum search depth

        Returns:
            List of entity IDs in path, or None if not found
        """
        return self.graph.shortest_path(from_entity, to_entity, max_depth)

    def connected_components(self) -> List[List[str]]:
        """
        Find connected components in the graph.

        Returns:
            List of components, each a list of entity IDs
        """
        return self.graph.connected_components()

    # ==========================================================================
    # Health & Quality Operations (NEW)
    # ==========================================================================

    @property
    def health(self):
        """
        Get the GraphHealth component for health monitoring.

        Returns:
            GraphHealth instance
        """
        if self._health is None:
            from pmos_brain.graph.graph_health import GraphHealth
            self._health = GraphHealth(self.path)
        return self._health

    @property
    def quality(self):
        """
        Get the QualityScorer component for quality scoring.

        Returns:
            QualityScorer instance
        """
        if self._quality is None:
            from pmos_brain.quality.scorer import QualityScorer
            self._quality = QualityScorer(self.path)
        return self._quality

    def health_report(self) -> Dict[str, Any]:
        """
        Generate a comprehensive health report.

        Returns:
            Dictionary with health metrics
        """
        report = self.health.analyze()
        return {
            "total_entities": report.total_entities,
            "orphan_entities": report.orphan_entities,
            "relationship_coverage": report.relationship_coverage,
            "density_score": report.density_score,
            "avg_relationships": report.avg_relationships_per_entity,
            "most_connected": report.most_connected[:5],
            "orphans": report.orphans[:10],
        }

    def score_entity(self, entity_path: Union[str, Path]) -> Dict[str, Any]:
        """
        Calculate quality score for an entity.

        Args:
            entity_path: Path to entity file

        Returns:
            Quality score breakdown
        """
        entity_path = Path(entity_path) if isinstance(entity_path, str) else entity_path
        if not entity_path.is_absolute():
            entity_path = self.path / entity_path

        score = self.quality.score_entity(entity_path)
        return {
            "entity_id": score.entity_id,
            "overall_score": score.overall_score,
            "completeness": score.completeness_score,
            "freshness": score.freshness_score,
            "relationships": score.relationship_score,
            "kappa": score.kappa_score,
            "issues": score.issues,
            "recommendations": score.recommendations,
        }

    def find_orphans(self) -> List[Dict[str, Any]]:
        """
        Find orphan entities (entities with no relationships).

        Returns:
            List of orphan entity details
        """
        return self.health.get_orphans()

    def quality_summary(self) -> Dict[str, Any]:
        """
        Get summary of quality scores across all entities.

        Returns:
            Quality summary statistics
        """
        return self.quality.get_summary()

    # ==========================================================================
    # Enrichment Operations (NEW)
    # ==========================================================================

    @property
    def pipeline(self):
        """
        Get the EnrichmentPipeline component.

        Returns:
            EnrichmentPipeline instance
        """
        if self._pipeline is None:
            from pmos_brain.enrichers.pipeline import EnrichmentPipeline
            self._pipeline = EnrichmentPipeline(self.path)
        return self._pipeline

    def enrich(
        self,
        sources: Optional[List[str]] = None,
        dry_run: bool = False,
    ) -> Dict[str, Any]:
        """
        Run enrichment pipeline.

        Args:
            sources: List of sources to process (default: all)
            dry_run: Preview without making changes

        Returns:
            Enrichment results summary
        """
        return self.pipeline.run(sources=sources, dry_run=dry_run)

    # ==========================================================================
    # Relationship Operations (NEW)
    # ==========================================================================

    @property
    def relationships(self):
        """
        Get the RelationshipBuilder component.

        Returns:
            RelationshipBuilder instance
        """
        if self._relationships is None:
            from pmos_brain.relationships.builder import RelationshipBuilder
            self._relationships = RelationshipBuilder(self.path)
        return self._relationships

    def create_relationship(
        self,
        source_id: str,
        target_id: str,
        relationship_type: str,
        confidence: float = 1.0,
        dry_run: bool = False,
    ) -> Dict[str, Any]:
        """
        Create a bidirectional relationship between entities.

        Args:
            source_id: Source entity $id
            target_id: Target entity $id
            relationship_type: Forward relationship type
            confidence: Confidence score
            dry_run: If True, don't write changes

        Returns:
            Result of relationship creation
        """
        result = self.relationships.create_bidirectional(
            source_id=source_id,
            target_id=target_id,
            relationship_type=relationship_type,
            confidence=confidence,
            dry_run=dry_run,
        )
        return {
            "source_id": result.source_id,
            "target_id": result.target_id,
            "forward_type": result.forward_type,
            "inverse_type": result.inverse_type,
            "forward_created": result.forward_created,
            "inverse_created": result.inverse_created,
        }

    def fix_inverse_relationships(
        self,
        dry_run: bool = False,
        limit: int = 1000,
    ) -> Dict[str, int]:
        """
        Fix missing inverse relationships.

        Args:
            dry_run: If True, don't write changes
            limit: Maximum inverses to create

        Returns:
            Stats dict with counts
        """
        return self.relationships.fix_all_inverses(dry_run=dry_run, limit=limit)

    # ==========================================================================
    # Maintenance Operations (NEW)
    # ==========================================================================

    @property
    def orphans(self):
        """
        Get the OrphanAnalyzer component.

        Returns:
            OrphanAnalyzer instance
        """
        if self._orphans is None:
            from pmos_brain.maintenance.orphan_analyzer import OrphanAnalyzer
            self._orphans = OrphanAnalyzer(self.path)
        return self._orphans

    def analyze_orphans(self) -> Dict[str, Any]:
        """
        Analyze orphan entities.

        Returns:
            Orphan analysis report
        """
        analysis = self.orphans.analyze()
        return {
            "total_entities": analysis.total_entities,
            "total_orphans": analysis.total_orphans,
            "orphan_rate": round(analysis.total_orphans / max(1, analysis.total_entities) * 100, 1),
            "by_type": analysis.orphans_by_type,
            "by_reason": analysis.orphans_by_reason,
            "samples": analysis.orphan_details[:20],
        }

    def cleanup_orphans(
        self,
        dry_run: bool = True,
    ) -> Dict[str, int]:
        """
        Mark orphans as pending enrichment.

        Args:
            dry_run: If True, preview without changes

        Returns:
            Stats dict with counts
        """
        pending = self.orphans.mark_pending_enrichment(dry_run=dry_run)
        standalone = self.orphans.mark_standalone(dry_run=dry_run)
        cleared = self.orphans.clear_reason_for_connected(dry_run=dry_run)

        return {
            "marked_pending": pending,
            "marked_standalone": standalone,
            "cleared_reason": cleared,
        }

    # ==========================================================================
    # Temporal Operations (NEW)
    # ==========================================================================

    @property
    def temporal(self):
        """
        Get the TemporalQuery component.

        Returns:
            TemporalQuery instance
        """
        if self._temporal is None:
            from pmos_brain.graph.temporal_query import TemporalQuery
            self._temporal = TemporalQuery(self.path)
        return self._temporal

    @property
    def events(self):
        """
        Get the EventStore component.

        Returns:
            EventStore instance
        """
        if self._events is None:
            from pmos_brain.storage.event_store import EventStore
            self._events = EventStore(self.path)
        return self._events
