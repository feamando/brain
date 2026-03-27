"""Tests for atomic write crash safety."""
import pytest
from pathlib import Path
import yaml


def _validate_all_entities(brain_dir: Path) -> bool:
    """Check all entity files have valid YAML frontmatter."""
    for f in brain_dir.rglob("*.md"):
        if f.name.lower() in ("readme.md", "_index.md"):
            continue
        if ".snapshots" in str(f):
            continue
        content = f.read_text(encoding="utf-8")
        if not content.startswith("---"):
            continue
        parts = content.split("---", 2)
        if len(parts) < 3:
            return False
        try:
            yaml.safe_load(parts[1])
        except yaml.YAMLError:
            return False
    return True


def _find_tmp_files(brain_dir: Path) -> list:
    """Find leftover .tmp. files."""
    return list(brain_dir.rglob("*.tmp.*"))


class TestCrashResilience:
    """Test atomic write guarantees."""

    def test_all_entities_valid_yaml(self, test_brain_dir):
        """All entity files should have valid YAML frontmatter."""
        assert _validate_all_entities(test_brain_dir)

    def test_no_tmp_files_in_fresh_brain(self, test_brain_dir):
        """Fresh brain should have no leftover temp files."""
        assert _find_tmp_files(test_brain_dir) == []

    def test_entity_count_consistent(self, test_brain_dir):
        """Entity count should be consistent."""
        entities = [
            f for f in test_brain_dir.rglob("*.md")
            if f.name.lower() not in ("readme.md", "_index.md")
            and ".snapshots" not in str(f)
        ]
        assert len(entities) == 50  # 15+10+8+7+5+5 from conftest
