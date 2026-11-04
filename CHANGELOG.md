# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.1] - 2026-11-04

### Added
- Complete end-to-end worked example (`docs/examples/instant-settlement-feature/`) demonstrating unbroken bidirectional traceability: `BR-SETTLE-001..003` ➔ `FR-SETTLE-001..003` (with Gherkin AC & DMN decision table) ➔ `ADR-0042` (Outbox Pattern) ➔ `TC-SETTLE-01..09` (Pact contract, SLA timer, fail-closed gate) ➔ Daily Report.
- Automated bidirectional traceability audit in `scripts/validate_skills.py` ensuring zero orphan requirements in worked examples.
- Comprehensive evaluation suite (`evals/evals.json` and `scripts/run_evals.py`) testing 80 trigger queries and 19 output rubrics (100% pass rate).
- Overwrite protection in `scripts/install.sh` prompting on existing destination skills in interactive shells and failing safely without `--force` in non-interactive scripts.

### Fixed
- Pinned exact release commit SHAs in `.github/workflows/ci.yml`: `actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683` (`v4.2.2`) and `actions/setup-python@82c7e631bb3cdc910f68e0081d67478d79c6982d` (`v5.1.0`).
- Fixed multi-inner nested placeholder `{{... {{UNIT}} ...}}` in `skills/brd-writing/assets/01-BRD.md:54`.
- Upgraded nested placeholder parser in `scripts/validate_skills.py` to use depth-tracking token parser to eliminate false negatives.
- Unified RTM into master template `skills/engineering-docs/assets/rtm.md` and unified ADR into `skills/design-docs/assets/03-ADR.md`.
- Deduplicated `06-Checklist-Release.md` from `api-versioning` assets.
- Cleaned up legacy `research_notes/` references in `docs/RISET-BEST-PRACTICES.md`.

## [1.1.0] - 2026-11-04

### Added
- Comprehensive repository validator `scripts/validate_skills.py` with multi-level path resolution and broken link detection.
- Unit test suite `tests/test_validate_skills.py` covering passing cases, negative controls, and router skill resolution.
- Command-line flags to `scripts/install.sh`: `--dry-run`, `--uninstall`, and `--force`.
- Python dependency specification `requirements.txt` (`pyyaml>=6.0.1`).
- GitHub Actions CI workflow `.github/workflows/ci.yml` testing validation and installation.
- Repository hygiene files: `CONTRIBUTING.md`, issue templates, and pull request template.
- Language policy documentation explicitly separating English runtime instructions from Indonesian domain templates.

### Changed
- Refactored `skills/qa-docs/assets/04-Quality-Gate-GitHub-Actions.md` to enforce fail-closed branch protection (`if: always()` with explicit non-zero exit on any upstream failure or cancellation).
- Pinned all actions in workflow templates using immutable commit SHAs with semantic version comments.
- Added least-privilege `permissions: contents: read` and concurrency groups to GitHub Actions template.
- Upgraded `skills/api-versioning/assets/06-Routing-Gateway-Nginx.md` with weighted traffic splitting via `split_clients` and TLS certificate directives.
- Streamlined skill references to under 400 lines each to ensure strict progressive disclosure and prevent context overload.
- Made `skills/` the single source of truth for all templates and references, removing redundant root `assets/` copies.
- Unnested ADR status placeholders in `06-ADR.md` and `03-ADR.md` for clean find-and-replace tool compatibility.

### Fixed
- Fixed router `engineering-docs/SKILL.md` to reference self-contained skills rather than nonexistent root paths.
- Removed broken links referencing `catatan-riset-internal` and legacy `research_notes/` paths.
- Clarified that the 500-character description limit is enforced for DeepSeek Harness skill catalog compatibility.

## [1.0.0] - 2026-11-04

### Added
- Initial suite of 8 engineering skills (`engineering-docs`, `brd-writing`, `fsd-writing`, `design-docs`, `qa-docs`, `daily-reporting`, `project-structure`, `api-versioning`).
- 40 production-ready templates with `{{...}}` placeholders and standard citation metadata.
- Comprehensive research synthesis `docs/RISET-BEST-PRACTICES.md` (2,360 lines) and template index `docs/TEMPLATE-INDEX.md`.
- Automated installer script `scripts/install.sh`.
- MIT License.

[Unreleased]: https://github.com/ryasrk/engineering-skills/compare/v1.1.1...HEAD
[1.1.1]: https://github.com/ryasrk/engineering-skills/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/ryasrk/engineering-skills/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/ryasrk/engineering-skills/releases/tag/v1.0.0
