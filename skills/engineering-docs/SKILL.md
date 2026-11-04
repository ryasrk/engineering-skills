---
name: engineering-docs
description: "Use when setting up or auditing engineering documentation end to end — BRD, FSD, design docs, test plans, daily reports, folder/project layout, and API lifecycle — and when the user asks which artefact comes next, how artefacts trace to each other, or how to organize a docs tree. Routes to focused skills and bundled templates; not for writing a single isolated document."
---

# Engineering documentation playbook

Turn a request into the smallest set of artefacts that can actually be traced, reviewed, and shipped. This skill is the router for a six-part documentation system; load a focused skill when the request has already narrowed to one artefact.

## Choose the working mode

| Request | Read next |
| --- | --- |
| Business goals, scope, KPI, stakeholder sign-off | `brd-writing` |
| Use cases, acceptance criteria, business rules, OpenAPI contract | `fsd-writing` |
| Architecture decision, design doc, C4, UI spec, accessibility DoD | `design-docs` |
| Test strategy, test plan, quality gate, exit criteria, metrics | `qa-docs` |
| Standup, daily status, blocker escalation, audience-specific reporting | `daily-reporting` |
| Docs/project tree, monorepo, SemVer, CODEOWNERS, CHANGELOG | `project-structure` |
| V1/V2/V3 coexistence, deprecation, zero-downtime migration | `api-versioning` |

For a full programme, work in this order: BRD → FSD → design/ADR → test plan → release artefacts → daily evidence. Keep stable IDs (`BR-...`, `FR-...`, `AC-...`, `TC-...`, `ADR-...`, `api_version`) so a requirements traceability matrix can connect them. Avoid copying requirement prose between artefacts; reference IDs instead.

## Shared assets

The repository root contains reusable material:

- `assets/templates/` — 40 Markdown templates with `{{...}}` placeholders and source metadata. Copy the relevant template into the target project, fill every placeholder, and remove the two metadata lines if the target repository does not use that convention.
- `assets/standards/` — six cited research notes and eight report sections. Read only the note relevant to the current question; they carry the source URLs, conflicts, and explicit limitations.
- `docs/TEMPLATE-INDEX.md` — when to use each template and how phases depend on each other.
- `docs/RISET-BEST-PRACTICES.md` — complete narrative report and correction table.

Do not load the whole research corpus into context for a single document. Read the focused note, then the template.

## Non-obvious rules that change decisions

1. **Standards rarely mandate document templates.** ISO/IEC/IEEE 29148 does not require an artefact named "BRD" or "FSD"; ISO/IEC/IEEE 42010:2022 explicitly leaves architecture-description format and notation to the organisation. Treat section lists as governance decisions, and say so when asked whether a template is mandatory.
2. **Separate five different claims:** standard, first-party documentation, community convention, team recommendation, and unverified inference. The bundled notes mark these explicitly; preserve the markers when rewriting.
3. **Verify the correction table before quoting a standard.** See `references/standard-corrections.md`. The most expensive mistakes in this corpus are reversed RFC attributions and treating WCAG AAA guidance as AA conformance.
4. **Traceability is bidirectional.** A BRD row must reach a test case, and every test case must resolve back to a requirement or explicit risk decision. Orphan rows are defects, not optional rows.
5. **A template is not evidence of completion.** Shipped artefacts need dated status, owner, review decision, and — for changes claimed as done — command-backed evidence.

## Deep reference

- Read `references/standard-corrections.md` when citing ISO/IEC/IEEE, RFC, W3C, OWASP, or when a reviewer disputes a standard claim.
- Read `references/artefact-map.md` when designing a docs tree or an RTM across more than two phases.
