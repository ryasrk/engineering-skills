# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
- Streamlined skill references to under 400 lines each (~3k-5k tokens) to ensure strict progressive disclosure and prevent context overload.
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
