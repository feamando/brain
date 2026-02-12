"""Entity model for Brain knowledge graph."""

import re
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any, List
from dataclasses import dataclass, field

import yaml


@dataclass
class Entity:
    """
    Represents a Brain entity (person, project, team, etc.).
    
    Entities are stored as markdown files with YAML frontmatter.
    """
    
    path: Path
    name: str
    entity_type: str
    content: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    @property
    def slug(self) -> str:
        """URL-safe identifier."""
        return self.path.stem
    
    @property
    def aliases(self) -> List[str]:
        """Get entity aliases."""
        return self.metadata.get("aliases", [])
    
    @property
    def relationships(self) -> Dict[str, List[str]]:
        """Get entity relationships."""
        return self.metadata.get("relationships", {})
    
    @property
    def created(self) -> Optional[datetime]:
        """Get creation timestamp."""
        created = self.metadata.get("created")
        if isinstance(created, datetime):
            return created
        if isinstance(created, str):
            try:
                return datetime.fromisoformat(created)
            except ValueError:
                return None
        return None
    
    @property
    def updated(self) -> Optional[datetime]:
        """Get last update timestamp."""
        updated = self.metadata.get("updated")
        if isinstance(updated, datetime):
            return updated
        if isinstance(updated, str):
            try:
                return datetime.fromisoformat(updated)
            except ValueError:
                return None
        return None
    
    def to_markdown(self) -> str:
        """Serialize entity to markdown with YAML frontmatter."""
        frontmatter = yaml.dump(self.metadata, default_flow_style=False, allow_unicode=True)
        return f"---\n{frontmatter}---\n\n{self.content}"
    
    @classmethod
    def from_markdown(cls, path: Path, content: str) -> "Entity":
        """Parse entity from markdown file content."""
        metadata = {}
        body = content
        
        # Parse YAML frontmatter
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                try:
                    metadata = yaml.safe_load(parts[1]) or {}
                except yaml.YAMLError:
                    pass
                body = parts[2].strip()
        
        # Extract name from first heading or filename
        name = metadata.get("name")
        if not name:
            heading_match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
            if heading_match:
                name = heading_match.group(1).strip()
            else:
                name = path.stem.replace("_", " ")
        
        entity_type = metadata.get("type", "entity")
        
        return cls(
            path=path,
            name=name,
            entity_type=entity_type,
            content=body,
            metadata=metadata,
        )
    
    def __repr__(self) -> str:
        return f"Entity(name='{self.name}', type='{self.entity_type}', path='{self.path}')"
