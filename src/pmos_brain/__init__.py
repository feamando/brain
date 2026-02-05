"""
PM-OS Brain - Semantic Knowledge Graph for AI Agents

A structured knowledge management system that stores entities (people, projects,
teams) as markdown files with YAML frontmatter, connected through typed relationships.

Quick Start:
    from pmos_brain import Brain, LLMClient
    
    # Initialize brain
    brain = Brain("./my-brain")
    
    # Search entities
    results = brain.search("project manager")
    
    # Load specific entity
    entity = brain.get("Entities/Jane_Smith")
    
    # Use LLM for enrichment
    llm = LLMClient()
    response = llm.complete("Extract entities from: ...")

For more information, see: https://github.com/feamando/brain
"""

__version__ = "1.0.0"
__author__ = "PM-OS Team"

from pmos_brain.core.brain import Brain
from pmos_brain.core.entity import Entity
from pmos_brain.core.loader import BrainLoader
from pmos_brain.core.search import BrainSearch
from pmos_brain.llm.client import LLMClient, get_llm_client

__all__ = [
    "Brain",
    "Entity",
    "BrainLoader",
    "BrainSearch",
    "LLMClient",
    "get_llm_client",
    "__version__",
]
