"""Brain search functionality."""
from pathlib import Path
from typing import List, Optional
from pmos_brain.core.entity import Entity
from pmos_brain.core.loader import BrainLoader

class BrainSearch:
    """Search Brain entities."""
    def __init__(self, brain_path: Path):
        self.brain_path = brain_path
        self._loader = BrainLoader(brain_path)
    
    def search(self, query: str, entity_type: Optional[str] = None, limit: int = 50) -> List[Entity]:
        """Search entities by query."""
        query_lower = query.lower()
        results = []
        for entity in self._loader.list_all(entity_type=entity_type):
            score = self._score(entity, query_lower)
            if score > 0:
                results.append((score, entity))
        results.sort(key=lambda x: x[0], reverse=True)
        return [e for _, e in results[:limit]]
    
    def _score(self, entity: Entity, query: str) -> int:
        score = 0
        if query in entity.name.lower(): score += 10
        if query in entity.content.lower(): score += 5
        for alias in entity.aliases:
            if query in alias.lower(): score += 8
        return score
