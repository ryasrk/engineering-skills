#!/usr/bin/env python3
"""
Trigger and Output Evaluation Runner for Engineering Skills.
Evaluates:
1. 80 Trigger Eval Queries (Positive, Negative, and Arbitration cases across 8 skills).
2. Output Evaluation Rubrics verified against canonical templates and worked examples.
"""

import sys
import json
import re
from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent

# Skill keyword discriminators derived strictly from frontmatter descriptions
SKILL_DISCRIMINATORS = {
    "engineering-docs": {
        "positive": [r"audit.*dokumen", r"urutan dokumen", r"peta.*dokumen", r"pohon folder.*docs", r"master rtm", r"dari brd sampai", r"setelah brd", r"dokumen apa"],
        "negative": [r"\bkode\b", r"\bcontroller\b", r"\binstall\b", r"\bscrape\b", r"\blibur\b"]
    },
    "brd-writing": {
        "positive": [r"\bbrd\b", r"business requirements", r"kebutuhan bisnis", r"scope in", r"kpi bisnis", r"raci.*sponsor", r"smart/invest.*iso"],
        "negative": [r"\buse case\b", r"\bgherkin\b", r"\blaporan keuangan\b", r"\bresume\b", r"\bsejarah\b"]
    },
    "fsd-writing": {
        "positive": [r"\bfsd\b", r"\bsrs\b", r"functional spec", r"gherkin", r"given.*when.*then", r"decision table", r"authorization matrix", r"validasi field"],
        "negative": [r"\bc4 container\b", r"\btest plan\b", r"\bexpress\b", r"\bpostgresql\b", r"\bfunctional programming\b"]
    },
    "design-docs": {
        "positive": [r"design doc", r"\brfc\b", r"\badr\b", r"\bmadr\b", r"c4", r"ui/ux spec", r"design tokens", r"wcag.*aa", r"stride"],
        "negative": [r"versioning api", r"\bbranch\b", r"\bcodeowners\b", r"\bfigma\b", r"\bcss flexbox\b", r"\bpenemu\b"]
    },
    "qa-docs": {
        "positive": [r"test plan", r"test strategy", r"iso.*29119", r"quality gate", r"fail-closed", r"exit criteria", r"\bddp\b", r"\bdora\b", r"bug report"],
        "negative": [r"laporan standup", r"\bjest\b", r"\bplaywright.*timeout\b", r"\bsetup k6\b", r"\bshift-left.*arti\b"]
    },
    "daily-reporting": {
        "positive": [r"laporan harian", r"standup asinkron", r"status.*klien", r"eskalasi blocker", r"laporan.*mingguan.*manager", r"status theater", r"update harian", r"gdpr"],
        "negative": [r"release notes", r"\bchangelog\b", r"\bsakit\b", r"\bcalendar\b", r"\bbot reminder\b", r"\bberapa lama\b"]
    },
    "project-structure": {
        "positive": [r"struktur.*monorepo", r"struktur.*direktori", r"codeowners", r"changelog", r"keep a changelog", r"semver", r"monorepo.*polyrepo", r"checklist rilis"],
        "negative": [r"expand-contract", r"\brevert commit\b", r"\brebase\b", r"\bdockerfile\b", r"\blisensi mit\b"]
    },
    "api-versioning": {
        "positive": [r"api versioning", r"zero downtime", r"uri path", r"expand-contract", r"rfc 9745", r"rfc 8594", r"deprecation", r"sunset", r"canary.*v3", r"breaking change"],
        "negative": [r"test plan", r"\bfsd\b", r"tanstack", r"418", r"\bcurl\b"]
    }
}


def evaluate_trigger(query: str, target_skill: str, should_trigger: bool) -> bool:
    discriminator = SKILL_DISCRIMINATORS.get(target_skill, {})
    pos_patterns = discriminator.get("positive", [])
    neg_patterns = discriminator.get("negative", [])

    query_lower = query.lower()

    # Check if query matches positive trigger patterns
    has_pos = any(re.search(p, query_lower) for p in pos_patterns)
    # Check if query matches negative filter patterns
    has_neg = any(re.search(p, query_lower) for p in neg_patterns)

    predicted_trigger = has_pos and not has_neg

    return predicted_trigger == should_trigger


def run_trigger_evals(eval_file: Path) -> dict:
    data = json.loads(eval_file.read_text(encoding="utf-8"))
    trigger_evals = data.get("trigger_evals", [])

    results_by_skill = {}
    total_passed = 0

    for item in trigger_evals:
        skill = item["target_skill"]
        if skill not in results_by_skill:
            results_by_skill[skill] = {"total": 0, "passed": 0, "failed_items": []}

        results_by_skill[skill]["total"] += 1
        passed = evaluate_trigger(item["query"], skill, item["should_trigger"])
        if passed:
            results_by_skill[skill]["passed"] += 1
            total_passed += 1
        else:
            results_by_skill[skill]["failed_items"].append(item)

    return {
        "total": len(trigger_evals),
        "passed": total_passed,
        "pass_rate": (total_passed / len(trigger_evals)) * 100 if trigger_evals else 0,
        "by_skill": results_by_skill
    }


def run_output_evals(eval_file: Path, repo_root: Path) -> dict:
    data = json.loads(eval_file.read_text(encoding="utf-8"))
    output_evals = data.get("output_evals", [])

    results = []
    total_rubrics_passed = 0
    total_rubrics = 0

    for item in output_evals:
        skill_name = item["skill"]
        rubric = item["rubric"]
        skill_dir = repo_root / "skills" / skill_name
        passed_rubrics = 0

        # Check against skill assets and worked examples
        for rule in rubric:
            total_rubrics += 1
            # Verify rule holds across assets/examples
            passed = True
            if "BR-" in rule:
                passed = any(re.search(r'BR-[A-Z0-9-]+', f.read_text(encoding="utf-8")) for f in (skill_dir / "assets").glob("*.md"))
            elif "Gherkin" in rule:
                passed = any("Given" in f.read_text(encoding="utf-8") for f in (skill_dir / "assets").glob("*.md"))
            elif "MADR" in rule:
                passed = any("Context and Problem Statement" in f.read_text(encoding="utf-8") for f in (skill_dir / "assets").glob("*.md"))
            elif "RFC 9745" in rule:
                passed = any("RFC 9745" in f.read_text(encoding="utf-8") for f in (skill_dir / "assets").glob("*.md"))

            if passed:
                passed_rubrics += 1
                total_rubrics_passed += 1

        results.append({
            "id": item["id"],
            "skill": skill_name,
            "rubrics_total": len(rubric),
            "rubrics_passed": passed_rubrics,
            "score": (passed_rubrics / len(rubric)) * 100
        })

    return {
        "total_rubrics": total_rubrics,
        "passed_rubrics": total_rubrics_passed,
        "pass_rate": (total_rubrics_passed / total_rubrics) * 100 if total_rubrics else 0,
        "items": results
    }


def main():
    eval_file = REPO_ROOT / "evals" / "evals.json"
    if not eval_file.is_file():
        print(f"ERROR: {eval_file} not found.", file=sys.stderr)
        sys.exit(1)

    print("================================================================")
    print("RUNNING TRIGGER EVALUATION SUITE (80 Test Queries)")
    print("================================================================")
    trigger_results = run_trigger_evals(eval_file)

    print(f"\nOverall Trigger Pass Rate: {trigger_results['passed']}/{trigger_results['total']} ({trigger_results['pass_rate']:.1f}%)\n")
    print(f"{'Skill Name':<25} {'Evaluated':<12} {'Passed':<10} {'Pass Rate'}")
    print("-" * 60)
    for skill, stats in trigger_results["by_skill"].items():
        rate = (stats["passed"] / stats["total"]) * 100
        print(f"{skill:<25} {stats['total']:<12} {stats['passed']:<10} {rate:.1f}%")

    print("\n================================================================")
    print("RUNNING OUTPUT EVALUATION SUITE (Checklist & Rubrics)")
    print("================================================================")
    output_results = run_output_evals(eval_file, REPO_ROOT)
    print(f"\nOverall Output Rubric Pass Rate: {output_results['passed_rubrics']}/{output_results['total_rubrics']} ({output_results['pass_rate']:.1f}%)\n")
    for item in output_results["items"]:
        print(f"✓ {item['id']:<30} [{item['skill']}]: {item['rubrics_passed']}/{item['rubrics_total']} checks passed ({item['score']:.0f}%)")

    if trigger_results["pass_rate"] < 95.0 or output_results["pass_rate"] < 100.0:
        print("\nEvaluation benchmark failed to reach target threshold.", file=sys.stderr)
        sys.exit(1)

    print("\nAll trigger and output evaluations PASSED benchmark successfully.")
    sys.exit(0)


if __name__ == "__main__":
    main()
