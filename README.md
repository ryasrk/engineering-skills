# Engineering Skills

> Production-ready AI agent skills and executable engineering templates for software delivery governance: BRD, FSD, System Design, QA & Testing, Daily Reporting, Repository Structure, and Zero-Downtime API Versioning.

Designed and verified for **DeepSeek Harness**, **Claude Code**, and **Codex**. Each skill is self-contained with its own `SKILL.md` instructions, cited `references/`, and ready-to-use `assets/` templates containing `{{...}}` placeholders.

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
| [`project-structure`](skills/project-structure/) | **Repository & Release Governance:** Monorepo vs polyrepo layouts, clean/hexagonal architecture boundaries, CODEOWNERS, trunk-based development, SemVer 2.0.0, and Keep a Changelog. | `06-Struktur-Folder.md`, `06-Struktur-Folder-Monorepo.md`, `06-Documentation-Hub.md`, `06-CODEOWNERS.md`, `06-CHANGELOG.md`, `06-ADR.md`, `06-Definition-of-Done.md`, `06-RTM.md`, `06-RACI.md`, `06-Checklist-Release.md` |
| [`api-versioning`](skills/api-versioning/) | **Zero-Downtime API Versioning:** V1/V2/V3 embedded in path (`/api/v1`, `/api/v2`, `/api/v3`), Expand-Contract database migrations, RFC 9745 Deprecation & RFC 8594 Sunset headers, and canary routing. | `06-OpenAPI-Multi-Versi*.md` (4 files), `06-Matriks-Endpoint-Versi.md`, `06-Routing-Gateway-Nginx.md`, `06-Runbook-Expand-Contract.md`, `06-Timeline-Migrasi-V1-V2-V3.md`, `06-Header-Lifecycle-Deprecation-Sunset.md`, `06-Komunikasi-Konsumen-Deprecation.md`, `06-Kriteria-Sunset-Metrik.md`, `06-Observability-Alert-Per-Versi.md`, `06-Checklist-Zero-Downtime.md` |

---

## Quick Installation

Clone this repository and run the installation script:

```bash
git clone https://github.com/ryasrk/engineering-skills.git
cd engineering-skills

# Automatically detects ~/.dsh/skills, ~/.claude/skills, or ~/.codex/skills:
./scripts/install.sh

# Or specify a custom target directory:
./scripts/install.sh ~/.dsh/skills
```

Or copy individual skills manually into your agent environment:

```bash
# Example: Install only api-versioning into DeepSeek Harness
cp -R skills/api-versioning ~/.dsh/skills/

# Example: Install brd-writing into Claude Code
cp -R skills/brd-writing ~/.claude/skills/
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
3. **Accessibility (WCAG 2.2):**
   - Level AA requires satisfying **all Level A and Level AA criteria**.
   - Success Criterion 2.3.3 (*Animation from Interactions*) is **Level AAA**; reduced motion is a best practice, not an AA compliance requirement.
4. **API Versioning Recommendation:**
   - For versioning embedded in the API, the primary recommendation is **major version in URI path** (`/api/v1`, `/api/v2`, `/api/v3`) paired with **one OpenAPI Description and one SDK per major version**.
   - Coexistence without downtime is achieved via **Expand-Contract (Parallel Change)**.

---

## Repository Structure

```text
engineering-skills/
├── skills/                     # 8 self-contained skill packages
│   ├── engineering-docs/       # Playbook router & standard corrections
│   ├── brd-writing/            # BRD authoring & review
│   ├── fsd-writing/            # FSD / SRS authoring & criteria
│   ├── design-docs/            # Architecture & design specs
│   ├── qa-docs/                # Testing strategy & CI quality gates
│   ├── daily-reporting/        # Standups & status updates
│   ├── project-structure/      # Layout, monorepo & release governance
│   └── api-versioning/         # Zero-downtime V1/V2/V3 API lifecycle
├── assets/                     # Shared canonical assets
│   ├── templates/              # 40 original production-ready templates
│   └── standards/              # Research notes & cited references
├── docs/                       # Comprehensive documentation
│   ├── RISET-BEST-PRACTICES.md # Full 2,360-line research synthesis
│   └── TEMPLATE-INDEX.md       # Master template index & dependency flow
├── scripts/
│   ├── install.sh              # Skill installer for dsh, claude, codex
│   └── validate_skills.py      # Structural & metadata integrity validator
└── LICENSE                     # MIT License
```

---

## Validation

Verify that all skills meet metadata and frontmatter constraints:

```bash
python3 scripts/validate_skills.py
```

---

## License

[MIT](LICENSE) © 2026 ryasrk
