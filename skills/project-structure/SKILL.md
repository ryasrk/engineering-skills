---
name: project-structure
description: "Use when designing, scaffolding, or reorganizing code and documentation repositories, choosing between monorepo and polyrepo, setting up CODEOWNERS, branch protection, or trunk-based workflows. Also use when establishing release governance with SemVer, Conventional Commits, Keep a Changelog, and Definition of Done."
---

# Repository layout and engineering project governance

Establish clean repository directory layouts, modular boundary separation, and automated release governance across code and documentation.

## Work from the source artefact

1. Read `references/project-structure-guide.md` for directory breakdown, monorepo trade-off analysis, and governance rules.
2. For repository and docs layout: copy `assets/06-Struktur-Folder.md` (for standard repositories) or `assets/06-Struktur-Folder-Monorepo.md` (for multi-package workspaces with tools like pnpm, Nx, or Turborepo).
3. Use `assets/06-Documentation-Hub.md` to establish the root `docs/README.md` navigation hub.
4. Establish ownership, releases, and changelog governance using:
   - `assets/06-CODEOWNERS.md` — path-based code review ownership.
   - `assets/06-CHANGELOG.md` — Keep a Changelog 1.1.0 and Semantic Versioning 2.0.0 format.
   - `assets/06-Definition-of-Done.md` — multi-stage DoD checklist.
   - `assets/06-RACI.md` — governance and responsibility matrix.
   - `assets/06-Checklist-Release.md` — pre-release, cutover, and rollback readiness checklist.
   - `assets/06-RTM.md` — cross-module traceability matrix.
   - `assets/06-ADR.md` — lightweight MADR template for structural decisions.

## Decisions that materially change the result

- **Documentation as code:** Maintain a single canonical path for each document. The root `README.md` serves as a navigation directory; it must not duplicate content from inner specification files.
- **Monorepo vs polyrepo criteria:** Adopt a monorepo only when cross-package atomic changes, shared tooling, and centralized CI caching provide clear benefits. If chosen, enforce strict package boundary checks and affected-target detection (using Nx, Turborepo, or pnpm workspaces).
- **Trunk-based development:** Prefer trunk-based development with short-lived feature branches, mandatory pull request reviews, automated CI checks, and feature flags. Reserve multi-branch GitFlow exclusively for software requiring concurrent support of multiple long-lived releases.
- **Release tagging and changelog:** Format release tags as `vMAJOR.MINOR.PATCH`. Follow Conventional Commits (`feat:`, `fix:`, `BREAKING CHANGE:`) and Keep a Changelog categories (`Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`).
- **Protected branches and CODEOWNERS:** Configure branch protection requiring review approval by assigned CODEOWNERS, linear commit histories, and all required status checks to pass before merging.

## Review checklist

- Documentation tree separates editable templates from canonical project specs (`docs/`).
- `CODEOWNERS` maps all critical infrastructure, security, and schema paths to specific teams.
- Branch protection prevents direct pushes to `main` and enforces status checks.
- Release checklist includes unambiguous cutover triggers and automated rollback conditions.
