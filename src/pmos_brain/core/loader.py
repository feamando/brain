"""Brain loader - load and save entities."""

from pathlib import Path
from typing import Optional, List, Dict, Any
from datetime import datetime

from pmos_brain.core.entity import Entity


class BrainLoader:
    """Load and save Brain entities."""
    
    DIRECTORIES = ["Entities", "Projects", "Architecture", "Strategy", "Decisions"]
    
    def __init__(self, brain_path: Path):
        self.brain_path = brain_path
    
    def load(self, entity_path: str) -> Optional[Entity]:
        """Load entity by relative path."""
        # Add .md extension if missing
        if not entity_path.endswith(".md"):
            entity_path = f"{entity_path}.md"
        
        full_path = self.brain_path / entity_path
        if not full_path.exists():
            return None
        
        content = full_path.read_text(encoding="utf-8")
        return Entity.from_markdown(full_path, content)
    
    def list_all(
        self,
        entity_type: Optional[str] = None,
        directory: Optional[str] = None,
    ) -> List[Entity]:
        """List all entities."""
        entities = []
        
        dirs_to_search = [directory] if directory else self.DIRECTORIES
        
        for dir_name in dirs_to_search:
            dir_path = self.brain_path / dir_name
            if not dir_path.exists():
                continue
            
            for md_file in dir_path.rglob("*.md"):
                if md_file.name.startswith("."):
                    continue
                
                try:
                    content = md_file.read_text(encoding="utf-8")
                    entity = Entity.from_markdown(md_file, content)
                    
                    if entity_type and entity.entity_type != entity_type:
                        continue
                    
                    entities.append(entity)
                except Exception:
                    continue
        
        return entities
    
    def create(
        self,
        name: str,
        entity_type: str,
        content: str = "",
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Entity:
        """Create a new entity."""
        metadata = metadata or {}
        metadata["type"] = entity_type
        metadata["name"] = name
        metadata["created"] = datetime.now().isoformat()
        metadata["updated"] = datetime.now().isoformat()
        
        # Determine directory
        dir_map = {
            "person": "Entities",
            "team": "Entities", 
            "squad": "Entities",
            "project": "Projects",
            "architecture": "Architecture",
            "decision": "Decisions",
        }
        directory = dir_map.get(entity_type, "Entities")
        
        # Generate filename
        slug = name.replace(" ", "_").replace("-", "_")
        filename = f"{slug}.md"
        path = self.brain_path / directory / filename
        
        # Create entity
        entity = Entity(
            path=path,
            name=name,
            entity_type=entity_type,
            content=content,
            metadata=metadata,
        )
        
        # Save to disk
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(entity.to_markdown(), encoding="utf-8")
        
        return entity
    
    def save(self, entity: Entity) -> bool:
        """Save entity to disk."""
        try:
            entity.metadata["updated"] = datetime.now().isoformat()
            entity.path.write_text(entity.to_markdown(), encoding="utf-8")
            return True
        except Exception:
            return False
    
    def delete(self, entity_path: str) -> bool:
        """Delete entity."""
        if not entity_path.endswith(".md"):
            entity_path = f"{entity_path}.md"
        
        full_path = self.brain_path / entity_path
        if full_path.exists():
            full_path.unlink()
            return True
        return False
    
    def resolve_alias(self, alias: str) -> Optional[Entity]:
        """Resolve alias to entity."""
        alias_lower = alias.lower()
        
        for entity in self.list_all():
            if entity.name.lower() == alias_lower:
                return entity
            if alias_lower in [a.lower() for a in entity.aliases]:
                return entity
        
        return None
