"""
Brain - Main interface for the knowledge graph.

Usage:
    from pmos_brain import Brain
    
    brain = Brain("./my-brain")
    
    # Search
    results = brain.search("product manager")
    
    # Get entity
    entity = brain.get("Entities/Jane_Smith")
    
    # List all
    entities = brain.list_entities()
"""

import os
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
        
        if not self.path.exists():
            raise FileNotFoundError(f"Brain directory not found: {self.path}")
    
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
