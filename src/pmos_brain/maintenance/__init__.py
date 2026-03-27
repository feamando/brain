"""
Maintenance module for Brain knowledge graph.

Provides orphan analysis, cleanup, and graph maintenance tools.
"""

from pmos_brain.maintenance.orphan_analyzer import OrphanAnalyzer, OrphanAnalysis
from pmos_brain.maintenance.stale_detector import StaleEntityDetector, StaleEntity
from pmos_brain.maintenance.orphan_cleaner import OrphanCleaner, OrphanTarget, CleanupResult
from pmos_brain.maintenance.snapshot_manager import SnapshotManager
from pmos_brain.maintenance.extraction_hints import (
    ExtractionHintsGenerator,
    ExtractionHintsReport,
    ExtractionHint,
    FIELD_SOURCES,
    FIELD_PRIORITY,
)

__all__ = [
    "OrphanAnalyzer",
    "OrphanAnalysis",
    "StaleEntityDetector",
    "StaleEntity",
    "OrphanCleaner",
    "OrphanTarget",
    "CleanupResult",
    "SnapshotManager",
    "ExtractionHintsGenerator",
    "ExtractionHintsReport",
    "ExtractionHint",
    "FIELD_SOURCES",
    "FIELD_PRIORITY",
]
