"""Tests for enrichment orchestrator modes."""
import os
from pathlib import Path
import pytest

from pmos_brain.enrichers.orchestrator import BrainEnrichmentOrchestrator, EnrichmentResult


class TestBrainEnrichModes:
    """Test enrichment modes."""

    def _collect_mtimes(self, brain_dir: Path) -> dict:
        """Collect modification times for all entity files."""
        mtimes = {}
        for f in brain_dir.rglob("*.md"):
            if f.name.lower() not in ("readme.md", "_index.md"):
                mtimes[str(f)] = f.stat().st_mtime
        return mtimes

    def test_mode_report_no_modifications(self, test_brain_dir):
        """Report mode should not modify any files."""
        before = self._collect_mtimes(test_brain_dir)
        orch = BrainEnrichmentOrchestrator(test_brain_dir)
        result = orch.run(mode="report")
        after = self._collect_mtimes(test_brain_dir)

        assert result.mode == "report"
        assert before == after, "Report mode modified files"

    def test_mode_boot_limited_types(self, test_brain_dir):
        """Boot mode should only process BOOT_ENTITY_TYPES."""
        orch = BrainEnrichmentOrchestrator(test_brain_dir)
        result = orch.run(mode="boot", dry_run=True)

        assert result.mode == "boot"
        # Boot should only scan brand, squad, team
        for scanned_type in result.soft_edges_by_type.keys():
            assert scanned_type in orch.BOOT_ENTITY_TYPES

    def test_dry_run_no_modifications(self, test_brain_dir):
        """Dry run should not modify any files."""
        before = self._collect_mtimes(test_brain_dir)
        orch = BrainEnrichmentOrchestrator(test_brain_dir)
        result = orch.run(mode="full", dry_run=True)
        after = self._collect_mtimes(test_brain_dir)

        assert before == after, "Dry run modified files"

    def test_result_dataclass_fields(self, test_brain_dir):
        """EnrichmentResult should have all expected fields with correct types."""
        orch = BrainEnrichmentOrchestrator(test_brain_dir)
        result = orch.run(mode="report")

        assert isinstance(result.timestamp, str)
        assert isinstance(result.mode, str)
        assert isinstance(result.baseline_entities, int)
        assert isinstance(result.baseline_relationships, int)
        assert isinstance(result.baseline_density, float)
        assert isinstance(result.soft_edges_by_type, dict)
        assert isinstance(result.cache_entities_loaded, int)
        assert isinstance(result.parallel_enabled, bool)
        assert isinstance(result.incremental_enabled, bool)

    def test_empty_brain(self, empty_brain_dir):
        """Should handle empty brain gracefully."""
        orch = BrainEnrichmentOrchestrator(empty_brain_dir)
        result = orch.run(mode="report")

        assert result.baseline_entities == 0
        assert result.mode == "report"
