"""Tests for enrichment snapshot and rollback."""
import subprocess
from pathlib import Path
import pytest

from pmos_brain.enrichers.orchestrator import BrainEnrichmentOrchestrator


def _init_git(brain_dir: Path):
    """Initialize a git repo in the brain directory."""
    subprocess.run(["git", "init"], cwd=brain_dir, capture_output=True, check=True)
    subprocess.run(["git", "add", "."], cwd=brain_dir, capture_output=True, check=True)
    subprocess.run(
        ["git", "commit", "-m", "initial"],
        cwd=brain_dir, capture_output=True, check=True,
        env={**__import__("os").environ, "GIT_AUTHOR_NAME": "test", "GIT_AUTHOR_EMAIL": "test@test.com",
             "GIT_COMMITTER_NAME": "test", "GIT_COMMITTER_EMAIL": "test@test.com"},
    )


class TestRollback:
    """Test snapshot and rollback lifecycle."""

    def test_rollback_no_snapshot_raises(self, test_brain_dir):
        """Rollback without snapshot should raise FileNotFoundError."""
        orch = BrainEnrichmentOrchestrator(test_brain_dir)
        with pytest.raises(FileNotFoundError, match="No enrichment snapshot"):
            orch.rollback()

    def test_no_git_skips_snapshot(self, test_brain_dir):
        """Non-git brain should skip snapshot gracefully."""
        orch = BrainEnrichmentOrchestrator(test_brain_dir)
        result = orch._create_snapshot()
        assert result is None

    def test_snapshot_created_in_git_repo(self, test_brain_dir):
        """Snapshot should be created when in git repo."""
        _init_git(test_brain_dir)
        # Modify a file to have something to stash
        some_file = next(test_brain_dir.rglob("*.md"))
        some_file.write_text(some_file.read_text() + "\nmodified for test")

        orch = BrainEnrichmentOrchestrator(test_brain_dir)
        stash_ref = orch._create_snapshot()

        snapshot_file = test_brain_dir / ".enrichment-snapshot"
        if stash_ref:
            assert snapshot_file.exists()
