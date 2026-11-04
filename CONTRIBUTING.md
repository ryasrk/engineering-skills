# Contributing to Engineering Skills

Thank you for your interest in improving the engineering skills suite.

## Core Design Principles

1. **Self-Contained Skills:** Each skill in `skills/<name>/` must contain its own `SKILL.md`, `references/`, and `assets/`. Never reference relative paths outside the skill directory from runtime instructions.
2. **Progressive Disclosure:** Keep `SKILL.md` concise (< 200 lines). Specialized background knowledge goes into `references/` (< 400 lines each, < 5,000 tokens) and executable templates go into `assets/`.
3. **Language Policy:**
   - **Skill Metadata & Runtime Instructions:** Written in clear English for maximum LLM instruction following across Claude Code, Codex, and DeepSeek Harness.
   - **Templates & Domain References:** Written in Indonesian with standard English technical terms (e.g. *pull request*, *fail-closed*, *canary*, *upstream*), matching target engineering delivery standards.
4. **Description Limits:** Frontmatter `description` must not exceed **500 characters** (to prevent truncation in the DeepSeek Harness skill catalog) and must not contain angle brackets (`<` or `>`).
5. **No Nested Placeholders:** Template placeholders must use single-level `{{PLACEHOLDER}}` syntax (e.g. `{{STATUS: proposed | accepted}}`) to allow clean find-and-replace automation.

## Verification Checklist

Before submitting a pull request, run the test and validation suite:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run unit tests
python3 -m unittest discover -s tests -v

# 3. Run repository validator
python3 scripts/validate_skills.py

# 4. Test installation script
./scripts/install.sh --dry-run /tmp/test-skills
```
