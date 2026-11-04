#!/usr/bin/env python3
"""
Comprehensive integrity validator for engineering-skills repository.
Checks:
1. Valid SKILL.md frontmatter (name, description).
2. Name matches directory and follows kebab-case.
3. Description under 500 characters (DSH and Claude catalog limit).
4. No unresolved TODO placeholders or angle brackets in metadata.
5. All references/ and assets/ links in SKILL.md resolve to existing files.
6. Assets contain valid {{...}} placeholders.
7. Correct RFC mapping (RFC 8594 = Sunset, RFC 9745 = Deprecation).
"""

import sys
import re
from pathlib import Path
import yaml

def validate_repo(repo_root: Path) -> bool:
    all_ok = True
    skills_dir = repo_root / "skills"

    if not skills_dir.is_dir():
        print(f"ERROR: skills directory not found at {skills_dir}", file=sys.stderr)
        return False

    skill_folders = sorted([d for d in skills_dir.iterdir() if d.is_dir()])
    if not skill_folders:
        print("ERROR: No skill folders found in skills/", file=sys.stderr)
        return False

    print(f"Validating {len(skill_folders)} skills in {skills_dir}...")

    for folder in skill_folders:
        skill_name = folder.name
        skill_md = folder / "SKILL.md"

        if not skill_md.is_file():
            print(f"[{skill_name}] FAIL: SKILL.md is missing", file=sys.stderr)
            all_ok = False
            continue

        content = skill_md.read_text(encoding="utf-8")
        if not content.startswith("---"):
            print(f"[{skill_name}] FAIL: No YAML frontmatter found", file=sys.stderr)
            all_ok = False
            continue

        match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        if not match:
            print(f"[{skill_name}] FAIL: Invalid YAML frontmatter delimiter", file=sys.stderr)
            all_ok = False
            continue

        try:
            fm = yaml.safe_load(match.group(1))
        except yaml.YAMLError as e:
            print(f"[{skill_name}] FAIL: YAML parsing error: {e}", file=sys.stderr)
            all_ok = False
            continue

        if not isinstance(fm, dict):
            print(f"[{skill_name}] FAIL: Frontmatter is not a dictionary", file=sys.stderr)
            all_ok = False
            continue

        name = fm.get("name", "")
        if name != skill_name:
            print(f"[{skill_name}] FAIL: Name '{name}' does not match directory '{skill_name}'", file=sys.stderr)
            all_ok = False

        if not re.match(r"^[a-z0-9-]+$", name):
            print(f"[{skill_name}] FAIL: Name must be kebab-case", file=sys.stderr)
            all_ok = False

        desc = fm.get("description", "")
        if not desc:
            print(f"[{skill_name}] FAIL: Missing description", file=sys.stderr)
            all_ok = False
        elif len(desc) > 500:
            print(f"[{skill_name}] FAIL: Description exceeds 500 characters ({len(desc)})", file=sys.stderr)
            all_ok = False

        if "<" in desc or ">" in desc:
            print(f"[{skill_name}] FAIL: Description contains angle brackets", file=sys.stderr)
            all_ok = False

        if "[TODO:" in desc or "[TODO:" in content:
            print(f"[{skill_name}] FAIL: Contains unfinished [TODO: ...]", file=sys.stderr)
            all_ok = False

        # Check that referenced assets/ and references/ files exist
        ref_matches = re.findall(r"`((?:assets|references)/[A-Za-z0-9._-]+)`", content)
        for rel in ref_matches:
            target = folder / rel
            if not target.exists():
                print(f"[{skill_name}] FAIL: Referenced path does not exist: {rel}", file=sys.stderr)
                all_ok = False

        # Validate assets
        assets_dir = folder / "assets"
        if assets_dir.is_dir():
            for asset in assets_dir.glob("*.md"):
                text = asset.read_text(encoding="utf-8")
                if "{{" not in text:
                    print(f"[{skill_name}] WARNING: Asset {asset.name} does not contain {{{{...}}}} placeholder", file=sys.stderr)

        # Standard correction checks for api-versioning and engineering-docs
        if skill_name in ("api-versioning", "engineering-docs"):
            if "RFC 8594" in content and "Sunset" not in content:
                print(f"[{skill_name}] FAIL: RFC 8594 must be identified as Sunset", file=sys.stderr)
                all_ok = False
            if "RFC 9745" in content and "Deprecation" not in content:
                print(f"[{skill_name}] FAIL: RFC 9745 must be identified as Deprecation", file=sys.stderr)
                all_ok = False

        print(f"[{skill_name}] PASS")

    return all_ok


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    if len(sys.argv) > 1:
        root = Path(sys.argv[1]).resolve()

    success = validate_repo(root)
    if not success:
        print("\nRepository validation FAILED.", file=sys.stderr)
        sys.exit(1)
    else:
        print("\nAll skills passed repository validation successfully.")
        sys.exit(0)
