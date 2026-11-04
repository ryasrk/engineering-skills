#!/usr/bin/env python3
"""
Unit tests for validate_skills.py.
Verifies both passing conditions and negative controls (deliberate violations).
"""

import sys
import shutil
import tempfile
import unittest
from pathlib import Path

# Add scripts directory to sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_skills import validate_repo, check_skill_links_and_references


class TestValidateSkills(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp(prefix="test_skills_")
        self.mock_root = Path(self.temp_dir)
        self.mock_skills = self.mock_root / "skills"
        self.mock_skills.mkdir(parents=True)

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _create_minimal_skill(self, name="sample-skill", description="Valid description.", extra_md=""):
        skill_dir = self.mock_skills / name
        skill_dir.mkdir(parents=True, exist_ok=True)
        (skill_dir / "assets").mkdir(exist_ok=True)
        (skill_dir / "references").mkdir(exist_ok=True)

        content = f"""---
name: {name}
description: "{description}"
---

# {name}

{extra_md}
"""
        (skill_dir / "SKILL.md").write_text(content, encoding="utf-8")
        return skill_dir

    def test_current_repo_is_valid(self):
        """The actual engineering-skills repository must pass validation."""
        self.assertTrue(validate_repo(REPO_ROOT))

    def test_minimal_valid_skill_passes(self):
        self._create_minimal_skill()
        self.assertTrue(validate_repo(self.mock_root))

    def test_missing_skill_md_fails(self):
        skill_dir = self.mock_skills / "missing-md"
        skill_dir.mkdir(parents=True)
        self.assertFalse(validate_repo(self.mock_root))

    def test_name_mismatch_fails(self):
        self._create_minimal_skill(name="folder-name")
        # Overwrite frontmatter with mismatched name
        skill_dir = self.mock_skills / "folder-name"
        (skill_dir / "SKILL.md").write_text("""---
name: different-name
description: "Mismatch."
---
# Test
""", encoding="utf-8")
        self.assertFalse(validate_repo(self.mock_root))

    def test_broken_markdown_link_fails(self):
        skill_dir = self._create_minimal_skill(extra_md="See [broken](nonexistent_file.md) for details.")
        errors = check_skill_links_and_references(skill_dir, self.mock_root)
        self.assertTrue(any("Broken markdown link 'nonexistent_file.md'" in e for e in errors))

    def test_broken_backtick_path_fails(self):
        skill_dir = self._create_minimal_skill(extra_md="Refer to `references/missing-guide.md`.")
        errors = check_skill_links_and_references(skill_dir, self.mock_root)
        self.assertTrue(any("Broken referenced path `references/missing-guide.md`" in e for e in errors))

    def test_nested_placeholder_fails(self):
        skill_dir = self._create_minimal_skill()
        # Add an asset with broken nested placeholder
        bad_asset = skill_dir / "assets" / "broken.md"
        bad_asset.write_text("Status: {{proposed|superseded by {{NNNN}}}}", encoding="utf-8")
        self.assertFalse(validate_repo(self.mock_root))

    def test_description_too_long_fails(self):
        long_desc = "A" * 501
        self._create_minimal_skill(description=long_desc)
        self.assertFalse(validate_repo(self.mock_root))

    def test_router_target_skill_not_found_fails(self):
        router_dir = self._create_minimal_skill(
            name="engineering-docs",
            description="Router.",
            extra_md="| Target | `nonexistent-skill` |"
        )
        self.assertFalse(validate_repo(self.mock_root))


if __name__ == "__main__":
    unittest.main()
