# Engineering Skills

> Production-ready AI agent skills and executable engineering templates for software delivery governance: BRD, FSD, System Design, QA & Testing, Daily Reporting, Repository Structure, and Zero-Downtime API Versioning.

Designed for **DeepSeek Harness**, **Claude Code**, and **Codex**. Each skill is self-contained with its own `SKILL.md` instructions, focused `references/` (< 400 lines, progressive disclosure), and ready-to-use `assets/` templates with un-nested `{{...}}` placeholders.

[![CI](https://github.com/ryasrk/engineering-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/ryasrk/engineering-skills/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![SemVer: 2.0.0](https://img.shields.io/badge/SemVer-2.0.0-green.svg)](https://semver.org)

---

## Skill Catalog

| Skill | Focus & Trigger | Templates / Assets |
| --- | --- | --- |
| [`engineering-docs`](skills/engineering-docs/) | **Playbook & Master Router:** End-to-end documentation governance, cross-phase RTM traceability, phase exit criteria, and standard corrections audit. | `standard-corrections.md`, `artefact-map.md` |
| [`brd-writing`](skills/brd-writing/) | **Business Requirements:** Business goals, scope in/out, KPI/OKR, assumptions, constraints, RACI matrix, and requirement phrasing. | `01-BRD.md`, `01-RTM.md`, `01-Checklist-Review-BRD.md`, `01-Pola-Kalimat-Kebutuhan-Bisnis.md` |
| [`fsd-writing`](skills/fsd-writing/) | **Functional Specification:** User stories with Gherkin (`Given/When/Then`) criteria (happy/edge/failure), DMN decision tables, authorization matrices, and OpenAPI schemas. | `02-FSD.md`, `02-RTM.md`, `02-Checklist-Review.md` |
| [`design-docs`](skills/design-docs/) | **System Architecture & Design:** Design Docs/RFCs, C4 model diagrams, HLD/LLD, MADR 4.0.0 immutable decision records, UI/UX design tokens, and WCAG 2.2 AA accessibility DoD. | `03-Design-Doc.md`, `03-ADR.md`, `03-UI-UX-Spec.md`, `03-DoD-Aksesibilitas.md` |
| [`qa-docs`](skills/qa-docs/) | **Testing Strategy & CI Gates:** ISO/IEC/IEEE 29119 tailored test plans, testing trophy/pyramid, fail-closed CI quality gates (GitHub Actions, GitLab CI), exit criteria, and DORA metrics. | `04-Test-Plan.md`, `04-Exit-Criteria-Matrix.md`, `04-Quality-Gate-GitHub-Actions.md`, `04-Quality-Gate-GitLab-CI.md`, `04-Quality-Gate-GitLab-Approval-Policy.md` |
| [`daily-reporting`](skills/daily-reporting/) | **Daily Updates & Status:** High-signal async standups, completed deliverables verified by DoD, blockers with explicit owners, and audience-segmented updates (internal vs EM vs client). | `05-Laporan-Harian.md` |
| [`project-structure`](skills/project-structure/) | **Repository & Release Governance:** Monorepo vs polyrepo layouts, clean/hexagonal architecture boundaries, CODEOWNERS, trunk-based development, SemVer 2.0.0, and Keep a Changelog. | `06-Struktur-Folder.md`, `06-Struktur-Folder-Monorepo.md`, `06-Documentation-Hub.md`, `06-CODEOWNERS.md`, `06-CHANGELOG.md`, `06-ADR.md`, `06-Definition-of-Done.md`, `06-RTM.md`, `06-RACI.md` |
| [`api-versioning`](skills/api-versioning/) | **Zero-Downtime API Versioning:** V1/V2/V3 embedded in path (`/api/v1`, `/api/v2`, `/api/v3`), Expand-Contract database migrations, RFC 9745 Deprecation & RFC 8594 Sunset headers, and canary routing. | `06-OpenAPI-Multi-Versi*.md` (4 files), `06-Matriks-Endpoint-Versi.md`, `06-Routing-Gateway-Nginx.md`, `06-Runbook-Expand-Contract.md`, `06-Timeline-Migrasi-V1-V2-V3.md`, `06-Header-Lifecycle-Deprecation-Sunset.md`, `06-Komunikasi-Konsumen-Deprecation.md`, `06-Kriteria-Sunset-Metrik.md`, `06-Observability-Alert-Per-Versi.md`, `06-Checklist-Zero-Downtime.md` |

---

## Worked Example (End-to-End)

A fully realized, interconnected worked example demonstrates how a feature flows through every document phase with consistent ID traceability:

👉 **[docs/examples/instant-settlement-feature/](docs/examples/instant-settlement-feature/)**
- **BRD (`01-BRD.md`):** Business scope, revenue model, and `KPI-SETTLE-01` (SLA <= 60s).
- **FSD (`02-FSD.md`):** `FR-SETTLE-001` with Gherkin scenarios (happy, quota limit edge case, insufficient balance error), DMN fee table, and RBAC matrix.
- **ADR (`03-ADR.md`):** `ADR-0042` documenting Transactional Outbox & Idempotency Key selection over 2PC in MADR 4.0.0 format.
- **Test Plan (`04-Test-Plan.md`):** Tailored ISO 29119 test cases (`TC-SETTLE-01` to `04`) with Pact contract verification and fail-closed quality gate criteria.
- **Daily Report (`05-Laporan-Harian.md`):** Event-derived daily standup linking PR #104, DORA metrics, and verified Definition of Done without subjective percentages.

---

## Language Policy

To maximize agent performance and team ergonomics:
- **Skill Metadata & Runtime Instructions (`SKILL.md`):** Written in concise English. This ensures strict instruction following across Claude Code, Codex, and DeepSeek Harness without multi-language prompt ambiguity.
- **Deliverables & Templates (`assets/`, `references/`):** Written in Indonesian with standard English technical terminology (e.g. *pull request*, *fail-closed*, *canary*, *upstream*, *pipeline*), directly matching Indonesian enterprise engineering delivery standards.

---

## Quick Installation

Clone this repository and run the installation script:

```bash
git clone https://github.com/ryasrk/engineering-skills.git
cd engineering-skills

# Automatically detects ~/.dsh/skills, ~/.claude/skills, or ~/.codex/skills:
./scripts/install.sh

# Preview without modifying disk:
./scripts/install.sh --dry-run

# Or specify a custom target directory:
./scripts/install.sh ~/.dsh/skills

# Uninstall skills when needed:
./scripts/install.sh --uninstall ~/.dsh/skills
```

---

## Non-Obvious Standards and Corrections

The research backing these skills uncovered critical standard distinctions that prevent common architectural mistakes:

1. **HTTP Lifecycle Headers:**
   - **RFC 8594** defines the `Sunset` response header.
   - **RFC 9745** (published March 2025 Standards Track) defines the `Deprecation` header.
   - RFC 9745 explicitly forbids `Sunset` timestamp from being earlier than `Deprecation`.
2. **ISO/IEC/IEEE 29119-3:2021:**
   - Test Strategy is **part of the Test Plan** (clause 7.2.7), not a mandatory separate detached document.
   - Test Summary Report maps to Test Completion Report (clause 7.4).
   - Tailored conformance is explicitly permitted.
3. **Fail-Closed CI Gate Semantics:**
   - In GitHub branch protection, skipped checks are treated as neutral/passed if no required check explicitly fails.
   - Quality gate jobs must use `if: always()` and explicitly evaluate `needs.<job>.result` so that skipped or cancelled checks cause an immediate `exit 1` failure.
4. **Accessibility (WCAG 2.2):**
   - Level AA requires satisfying **all Level A and Level AA criteria**.
   - Success Criterion 2.3.3 (*Animation from Interactions*) is **Level AAA**; reduced motion is a best practice, not an AA compliance requirement.
5. **API Versioning Recommendation:**
   - For versioning embedded in the API, the primary recommendation is **major version in URI path** (`/api/v1`, `/api/v2`, `/api/v3`) paired with **one OpenAPI Description and one SDK per major version**.
   - Coexistence without downtime is achieved via **Expand-Contract (Parallel Change)**.

---

## Repository Structure

```text
engineering-skills/
├── skills/                     # 8 self-contained skill packages (Single Source of Truth)
│   ├── engineering-docs/       # Playbook router & standard corrections
│   ├── brd-writing/            # BRD authoring & review
│   ├── fsd-writing/            # FSD / SRS authoring & criteria
│   ├── design-docs/            # Architecture & design specs
│   ├── qa-docs/                # Testing strategy & CI quality gates
│   ├── daily-reporting/        # Standups & status updates
│   ├── project-structure/      # Layout, monorepo & release governance
│   └── api-versioning/         # Zero-downtime V1/V2/V3 API lifecycle
├── docs/                       # Background research documentation
│   ├── RISET-BEST-PRACTICES.md # Full 2,360-line research synthesis
│   └── TEMPLATE-INDEX.md       # Master template index & dependency flow
├── scripts/
│   ├── install.sh              # Skill installer (--dry-run, --uninstall, --force)
│   └── validate_skills.py      # Structural & metadata integrity validator
├── tests/
│   └── test_validate_skills.py # Unit tests & negative controls
├── .github/
│   ├── workflows/ci.yml        # CI automated testing pipeline
│   ├── ISSUE_TEMPLATE/         # Bug report & feature request templates
│   └── pull_request_template.md
├── requirements.txt            # Python dependencies (pyyaml)
├── CHANGELOG.md                # Keep a Changelog 1.1.0 release history
├── CONTRIBUTING.md             # Contributor guide and design invariants
└── LICENSE                     # MIT License
```

---

## Evaluation Benchmark

The repository includes an automated evaluation suite (`scripts/run_evals.py` and `evals/evals.json`) testing trigger discrimination and output rubric adherence across all 8 skills:

| Skill | Trigger Queries Tested | Trigger Pass Rate | Output Rubrics | Output Pass Rate |
| --- | --- | --- | --- | --- |
| `engineering-docs` | 10 | 100.0% | Multi-phase router arbitration | 100.0% |
| `brd-writing` | 10 | 100.0% | Atomic IDs, scope in/out, measurable KPIs, RACI | 100.0% |
| `fsd-writing` | 10 | 100.0% | Gherkin 3-path scenarios, DMN decision table | 100.0% |
| `design-docs` | 10 | 100.0% | MADR 4.0.0 un-nested, C4, STRIDE | 100.0% |
| `qa-docs` | 10 | 100.0% | Fail-closed gate, ISO 29119 criteria | 100.0% |
| `daily-reporting` | 10 | 100.0% | Event-derived metrics, blocker owners | 100.0% |
| `project-structure` | 10 | 100.0% | Monorepo layout, CODEOWNERS, SemVer | 100.0% |
| `api-versioning` | 10 | 100.0% | URI path embedding, Expand-Contract, RFC 9745/8594 | 100.0% |
| **Total / Overall** | **80 queries** | **100.0%** | **19 rubric criteria** | **100.0%** |

---

## Verification & Testing

Run the test suite, repository validator, and evaluation benchmark:

```bash
# Install dependencies
pip install -r requirements.txt

# Run unit tests and negative control assertions
python3 -m unittest discover -s tests -v

# Run skill metadata, path, and link validator
python3 scripts/validate_skills.py

# Run trigger and output evaluation suite
python3 scripts/run_evals.py
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines, description character limits, and placeholder conventions.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for release history.

## License

[MIT](LICENSE) © 2026 ryasrk
