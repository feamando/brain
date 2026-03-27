"""Tests for incremental enrichment processing."""
import json
import os
from pathlib import Path
import pytest

from pmos_brain.enrichers.orchestrator import BrainEnrichmentOrchestrator


class TestIncrementalEnrichment:
    """Test incremental enrichment state tracking."""

    def test_state_file_not_created_on_dry_run(self, test_brain_dir):
        """Dry run should not create state file."""
        os.environ["PMOS_ENRICH_INCREMENTAL"] = "1"
        try:
            orch = BrainEnrichmentOrchestrator(test_brain_dir)
            orch.run(mode="full", dry_run=True)
            state_path = test_brain_dir / ".enrichment-state.json"
            assert not state_path.exists(), "State file created on dry run"
        finally:
            os.environ.pop("PMOS_ENRICH_INCREMENTAL", None)

    def test_incremental_disabled_by_default(self, test_brain_dir):
        """Incremental should be disabled when env var not set."""
        os.environ.pop("PMOS_ENRICH_INCREMENTAL", None)
        orch = BrainEnrichmentOrchestrator(test_brain_dir)
        result = orch.run(mode="report")
        assert result.incremental_enabled is False

    def test_incremental_enabled_by_env(self, test_brain_dir):
        """Incremental should be enabled when env var is set."""
        os.environ["PMOS_ENRICH_INCREMENTAL"] = "1"
        try:
            orch = BrainEnrichmentOrchestrator(test_brain_dir)
            result = orch.run(mode="boot", dry_run=True)
            assert result.incremental_enabled is True
        finally:
            os.environ.pop("PMOS_ENRICH_INCREMENTAL", None)

    def test_corrupt_state_does_not_crash(self, test_brain_dir):
        """Corrupt state file should not crash enrichment."""
        os.environ["PMOS_ENRICH_INCREMENTAL"] = "1"
        try:
            state_path = test_brain_dir / ".enrichment-state.json"
            state_path.write_text("{{invalid json!!")
            orch = BrainEnrichmentOrchestrator(test_brain_dir)
            result = orch.run(mode="boot", dry_run=True)
            assert result is not None
        finally:
            os.environ.pop("PMOS_ENRICH_INCREMENTAL", None)
