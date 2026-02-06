"""
Brain Graph - Graph Traversal Component

Expands seed entities via relationship traversal.
Based on TKS research findings for knowledge graph retrieval.

Features:
- 1-hop and multi-hop relationship traversal
- Configurable decay factor for neighbor scoring
- Relationship-specific strength support
- Cycle prevention via visited tracking
"""

import re
from pathlib import Path
from typing import Dict, List, Set, Optional, Any, Tuple, Union
from dataclasses import dataclass, field

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

try:
    import networkx as nx
    HAS_NETWORKX = True
except ImportError:
    HAS_NETWORKX = False


@dataclass
class GraphNode:
    """Represents a node in the graph traversal."""
    entity_id: str
    score: float = 1.0
    depth: int = 0
    via_entity: Optional[str] = None
    via_relationship: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TraversalResult:
    """Result of a graph traversal operation."""
    seeds: List[GraphNode]
    neighbors: List[GraphNode]
    warnings: List[str]
    stats: Dict[str, Any]


class BrainGraph:
    """
    Graph traversal component for the Brain knowledge graph.

    Expands seed entities by following relationships to find neighbors.
    Implements TKS research findings: 1-hop traversal with decay.

    Example:
        graph = BrainGraph(brain_path)
        result = graph.expand(seed_ids, depth=2)
        for node in result.neighbors:
            print(f"{node.entity_id}: {node.score}")
    """

    DEFAULT_DECAY = 0.5

    def __init__(self, brain_path: Union[str, Path]):
        """
        Initialize graph component.

        Args:
            brain_path: Path to brain directory
        """
        self.brain_path = Path(brain_path)
        self.warnings: List[str] = []
        self._entity_cache: Dict[str, Dict] = {}
        self._nx_graph: Optional[Any] = None

    def expand(
        self,
        seeds: List[Union[str, GraphNode]],
        decay: float = DEFAULT_DECAY,
        depth: int = 1,
        relationship_types: Optional[List[str]] = None,
    ) -> TraversalResult:
        """
        Expand seed entities via relationship traversal.

        Args:
            seeds: List of seed entity IDs or GraphNodes
            decay: Score decay factor for neighbors (default 0.5)
            depth: Traversal depth (1 = neighbors only)
            relationship_types: Filter to specific relationship types

        Returns:
            TraversalResult with neighbors and metadata
        """
        self.warnings = []

        # Normalize seeds to GraphNodes
        seed_nodes = []
        for s in seeds:
            if isinstance(s, str):
                seed_nodes.append(GraphNode(entity_id=s, score=1.0, depth=0))
            else:
                seed_nodes.append(s)

        if not seed_nodes:
            return TraversalResult(
                seeds=[],
                neighbors=[],
                warnings=[],
                stats={"seeds": 0, "neighbors": 0, "depth": depth}
            )

        # Track visited entities
        visited: Set[str] = {n.entity_id for n in seed_nodes}
        neighbors: Dict[str, GraphNode] = {}

        # Current frontier
        current_frontier = [
            (n.entity_id, n.score, None) for n in seed_nodes
        ]

        for d in range(depth):
            next_frontier = []
            current_decay = decay ** (d + 1)

            for entity_id, parent_score, parent_id in current_frontier:
                # Load entity and get relationships
                entity_data = self._load_entity(entity_id)
                if entity_data is None:
                    continue

                relationships = entity_data.get('$relationships', [])
                if not relationships:
                    continue

                for rel in relationships:
                    target = rel.get('target')
                    rel_type = rel.get('type', 'related_to')

                    if not target:
                        continue

                    # Filter by relationship type if specified
                    if relationship_types and rel_type not in relationship_types:
                        continue

                    # Resolve target
                    canonical_target = self._resolve_target(target)
                    if canonical_target is None:
                        self.warnings.append(f"Unresolved: '{target}' in {entity_id}")
                        continue

                    # Skip if already visited
                    if canonical_target in visited:
                        continue

                    # Calculate score with decay
                    rel_strength = self._get_relationship_strength(rel, current_decay)
                    score = parent_score * rel_strength

                    via_entity = parent_id if parent_id else entity_id

                    # Create or update (max score wins)
                    if canonical_target not in neighbors or score > neighbors[canonical_target].score:
                        neighbors[canonical_target] = GraphNode(
                            entity_id=canonical_target,
                            score=score,
                            depth=d + 1,
                            via_entity=via_entity,
                            via_relationship=rel_type,
                        )

                    visited.add(canonical_target)
                    next_frontier.append((canonical_target, score, via_entity))

            current_frontier = next_frontier

        neighbor_list = sorted(
            neighbors.values(),
            key=lambda x: x.score,
            reverse=True
        )

        return TraversalResult(
            seeds=seed_nodes,
            neighbors=neighbor_list,
            warnings=self.warnings,
            stats={
                "seeds": len(seed_nodes),
                "neighbors": len(neighbor_list),
                "depth": depth,
                "decay": decay,
            }
        )

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
        if not HAS_NETWORKX:
            # Fallback to BFS
            return self._bfs_path(from_entity, to_entity, max_depth)

        # Use NetworkX for efficient pathfinding
        G = self._build_networkx_graph()
        try:
            return nx.shortest_path(G, from_entity, to_entity)
        except (nx.NetworkXNoPath, nx.NodeNotFound):
            return None

    def connected_components(self) -> List[List[str]]:
        """
        Find connected components in the graph.

        Returns:
            List of components, each a list of entity IDs
        """
        if not HAS_NETWORKX:
            self.warnings.append("NetworkX not installed, connected_components unavailable")
            return []

        G = self._build_networkx_graph()
        return [list(c) for c in nx.connected_components(G.to_undirected())]

    def get_neighbors(
        self,
        entity_id: str,
        relationship_type: Optional[str] = None,
    ) -> List[GraphNode]:
        """
        Get direct neighbors of an entity.

        Args:
            entity_id: Entity to get neighbors for
            relationship_type: Filter by relationship type

        Returns:
            List of neighbor GraphNodes
        """
        result = self.expand(
            [entity_id],
            decay=1.0,  # No decay for direct neighbors
            depth=1,
            relationship_types=[relationship_type] if relationship_type else None,
        )
        return result.neighbors

    def _load_entity(self, entity_id: str) -> Optional[Dict]:
        """Load entity data from file or cache."""
        if entity_id in self._entity_cache:
            return self._entity_cache[entity_id]

        # Try various path patterns
        possible_paths = [
            self.brain_path / f"{entity_id}.md",
            self.brain_path / entity_id / "index.md",
        ]

        # Handle IDs like "Entities/Jane_Smith"
        if "/" in entity_id:
            possible_paths.insert(0, self.brain_path / f"{entity_id}.md")

        for path in possible_paths:
            if path.exists():
                data = self._parse_frontmatter(path)
                if data:
                    self._entity_cache[entity_id] = data
                    return data

        return None

    def _parse_frontmatter(self, path: Path) -> Optional[Dict]:
        """Parse YAML frontmatter from markdown file."""
        if not HAS_YAML:
            return None

        try:
            content = path.read_text(encoding='utf-8')
        except Exception:
            return None

        if not content.startswith('---'):
            return {}

        parts = content.split('---', 2)
        if len(parts) < 3:
            return {}

        try:
            return yaml.safe_load(parts[1]) or {}
        except yaml.YAMLError:
            return {}

    def _resolve_target(self, target: str) -> Optional[str]:
        """
        Resolve a relationship target to canonical ID.

        Handles:
        - [[Entity]] wiki links
        - Direct paths like "Entities/Name"
        - Plain names
        """
        # Strip wiki link syntax
        if target.startswith('[[') and target.endswith(']]'):
            target = target[2:-2]

        # If it looks like a path, use it directly
        if '/' in target:
            # Verify entity exists
            if self._load_entity(target) is not None:
                return target

        # Try common patterns
        patterns = [
            f"Entities/{target.replace(' ', '_')}",
            f"Projects/{target.replace(' ', '_')}",
            f"Teams/{target.replace(' ', '_')}",
            target.replace(' ', '_'),
        ]

        for pattern in patterns:
            if self._load_entity(pattern) is not None:
                return pattern

        return None

    def _get_relationship_strength(self, rel: Dict, default: float) -> float:
        """Extract relationship strength from relationship dict."""
        strength = rel.get('strength', default)
        if isinstance(strength, str):
            try:
                return float(strength)
            except ValueError:
                return default
        return float(strength) if strength else default

    def _build_networkx_graph(self) -> Any:
        """Build NetworkX graph from brain entities."""
        if self._nx_graph is not None:
            return self._nx_graph

        if not HAS_NETWORKX:
            raise ImportError("NetworkX required for graph operations")

        G = nx.DiGraph()

        # Find all entity files
        for entity_file in self.brain_path.rglob("*.md"):
            rel_path = entity_file.relative_to(self.brain_path)
            entity_id = str(rel_path.with_suffix(''))

            data = self._load_entity(entity_id)
            if data is None:
                continue

            G.add_node(entity_id, **data)

            for rel in data.get('$relationships', []):
                target = rel.get('target')
                if target:
                    canonical = self._resolve_target(target)
                    if canonical:
                        G.add_edge(
                            entity_id,
                            canonical,
                            type=rel.get('type', 'related_to'),
                            strength=self._get_relationship_strength(rel, 0.5),
                        )

        self._nx_graph = G
        return G

    def _bfs_path(
        self,
        from_entity: str,
        to_entity: str,
        max_depth: int,
    ) -> Optional[List[str]]:
        """BFS pathfinding fallback when NetworkX unavailable."""
        from collections import deque

        if from_entity == to_entity:
            return [from_entity]

        visited = {from_entity}
        queue = deque([(from_entity, [from_entity])])

        while queue:
            current, path = queue.popleft()

            if len(path) > max_depth:
                continue

            result = self.expand([current], depth=1, decay=1.0)
            for neighbor in result.neighbors:
                if neighbor.entity_id == to_entity:
                    return path + [to_entity]

                if neighbor.entity_id not in visited:
                    visited.add(neighbor.entity_id)
                    queue.append((neighbor.entity_id, path + [neighbor.entity_id]))

        return None
