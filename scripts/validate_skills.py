#!/usr/bin/env python3
"""
Comprehensive integrity validator for engineering-skills repository.
Checks:
1. Valid SKILL.md frontmatter (name, description, kebab-case).
2. Description under 500 characters (DeepSeek Harness catalog truncation limit;
   Claude Code allows up to 1024, but 500 ensures universal cross-platform compatibility).
3. No unresolved TODO placeholders or angle brackets in metadata.
4. All relative paths and Markdown links in SKILL.md and references/ resolve on disk.
5. Router skills reference only valid, existing skill directories.
6. No machine-local absolute paths or broken research_notes references.
7. Assets contain valid {{...}} placeholders without broken nested placeholders.
8. Correct RFC mapping (RFC 8594 = Sunset, RFC 9745 = Deprecation).
"""

import sys
import re
from pathlib import Path
import yaml


def check_skill_links_and_references(skill_dir: Path, repo_root: Path) -> list:
    errors = []

    # Check SKILL.md and files in references/
    docs_to_check = [skill_dir / "SKILL.md"]
    ref_dir = skill_dir / "references"
    if ref_dir.is_dir():
        docs_to_check.extend(ref_dir.glob("*.md"))

    for doc in docs_to_check:
        if not doc.is_file():
            continue
        content = doc.read_text(encoding="utf-8")

        # 1. Check markdown links [label](path)
        link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
        for match in link_pattern.finditer(content):
            target = match.group(2).strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean_target = target.split("#")[0]
            if not clean_target:
                continue
            resolved = (doc.parent / clean_target).resolve()
            if not resolved.exists():
                errors.append(f"Broken markdown link '{target}' in {doc.relative_to(repo_root)}")

        # 2. Check explicitly referenced assets/ and references/ paths in backticks
        ref_pattern = re.compile(r'`((?:\.\./)?(?:assets|references)/[A-Za-z0-9._-]+)`')
        for match in ref_pattern.finditer(content):
            rel_path = match.group(1).strip()
            resolved = (doc.parent / rel_path).resolve()
            if not resolved.exists():
                errors.append(f"Broken referenced path `{rel_path}` in {doc.relative_to(repo_root)}")

        # 3. Check for broken legacy references
        if "catatan-riset-internal" in content:
            errors.append(f"Unresolved 'catatan-riset-internal' placeholder in {doc.relative_to(repo_root)}")
        if "research_notes/" in content:
            errors.append(f"Unresolved 'research_notes/' path reference in {doc.relative_to(repo_root)}")

    return errors


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
    skill_names = {f.name for f in skill_folders}

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
            print(f"[{skill_name}] FAIL: Description exceeds 500 characters ({len(desc)}). "
                  f"Enforced to prevent truncation in DeepSeek Harness skill catalog (Claude allows 1024).", file=sys.stderr)
            all_ok = False

        if "<" in desc or ">" in desc:
            print(f"[{skill_name}] FAIL: Description contains angle brackets (< or >)", file=sys.stderr)
            all_ok = False

        if "[TODO:" in desc or "[TODO:" in content:
            print(f"[{skill_name}] FAIL: Contains unfinished [TODO: ...]", file=sys.stderr)
            all_ok = False

        # Router skill check: verify that skills mentioned in the router table exist
        if skill_name == "engineering-docs":
            router_targets = re.findall(r"\|\s*`([a-z0-9-]+)`\s*\|", content)
            for target_skill in router_targets:
                if target_skill != "engineering-docs" and target_skill not in skill_names:
                    print(f"[{skill_name}] FAIL: Router mentions non-existent skill '{target_skill}'", file=sys.stderr)
                    all_ok = False

        # Check markdown links and path references in SKILL.md and references/
        link_errors = check_skill_links_and_references(folder, repo_root)
        for err in link_errors:
            print(f"[{skill_name}] FAIL: {err}", file=sys.stderr)
            all_ok = False

        # Validate assets
        assets_dir = folder / "assets"
        if assets_dir.is_dir():
            for asset in assets_dir.glob("*.md"):
                text = asset.read_text(encoding="utf-8")
                if "{{" not in text:
                    print(f"[{skill_name}] WARNING: Asset {asset.name} does not contain {{{{...}}}} placeholder", file=sys.stderr)
                # Check for broken nested placeholder (depth > 1)
                for line_no, line in enumerate(text.splitlines(), start=1):
                    tokens = [m.group() for m in re.finditer(r"(\{\{|\}\})", line)]
                    depth = 0
                    for tok in tokens:
                        if tok == "{{":
                            depth += 1
                            if depth > 1:
                                print(f"[{skill_name}] FAIL: Asset {asset.name}:{line_no} contains nested {{{{...}}}} placeholder: {line.strip()}", file=sys.stderr)
                                all_ok = False
                                break
                        elif tok == "}}":
                            depth = max(0, depth - 1)

        # Standard correction checks for api-versioning and engineering-docs
        if skill_name in ("api-versioning", "engineering-docs"):
            if "RFC 8594" in content and "Sunset" not in content:
                print(f"[{skill_name}] FAIL: RFC 8594 must be identified as Sunset", file=sys.stderr)
                all_ok = False
            if "RFC 9745" in content and "Deprecation" not in content:
                print(f"[{skill_name}] FAIL: RFC 9745 must be identified as Deprecation", file=sys.stderr)
                all_ok = False

        print(f"[{skill_name}] PASS")

    # Validate worked examples traceability (docs/examples/)
    examples_dir = repo_root / "docs" / "examples"
    if examples_dir.is_dir():
        for example_folder in examples_dir.iterdir():
            if not example_folder.is_dir():
                continue
            brd_file = example_folder / "01-BRD.md"
            fsd_file = example_folder / "02-FSD.md"
            tp_file = example_folder / "04-Test-Plan.md"

            if brd_file.is_file() and fsd_file.is_file() and tp_file.is_file():
                brd_txt = brd_file.read_text(encoding="utf-8")
                fsd_txt = fsd_file.read_text(encoding="utf-8")
                tp_txt = tp_file.read_text(encoding="utf-8")

                br_ids = set(re.findall(r'`(BR-[A-Z0-9-]+)`', brd_txt))
                kpi_ids = set(re.findall(r'`(KPI-[A-Z0-9-]+)`', brd_txt))
                fr_ids = set(re.findall(r'`(FR-[A-Z0-9-]+)`', fsd_txt))

                # Check every BR has downstream FR
                for br in br_ids:
                    if br not in fsd_txt:
                        print(f"[examples/{example_folder.name}] FAIL: Orphan requirement {br} not mapped in FSD", file=sys.stderr)
                        all_ok = False

                # Check every FR has downstream TC
                for fr in fr_ids:
                    if fr not in tp_txt:
                        print(f"[examples/{example_folder.name}] FAIL: Orphan functional requirement {fr} not mapped in Test Plan", file=sys.stderr)
                        all_ok = False

                # Check every KPI has downstream TC or measurement in Test Plan
                for kpi in kpi_ids:
                    if kpi not in tp_txt:
                        print(f"[examples/{example_folder.name}] FAIL: Business KPI {kpi} not traced in Test Plan", file=sys.stderr)
                        all_ok = False

    # Global check: no machine-local paths in repository markdown or scripts
    local_machine_pattern = "/home/" + "ryasr"
    for path in repo_root.glob("**/*"):
        if path.is_file() and path.suffix in (".md", ".py", ".sh", ".yml", ".yaml"):
            if ".git" in path.parts or path.name == "validate_skills.py":
                continue
            try:
                txt = path.read_text(encoding="utf-8")
                if local_machine_pattern in txt:
                    print(f"FAIL: Local machine path '{local_machine_pattern}' found in {path.relative_to(repo_root)}", file=sys.stderr)
                    all_ok = False
            except Exception:
                pass

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
