# Artefact map and traceability

Use this when a request spans more than two phases or when restructuring a documentation tree.

## Flow

```text
business case / charter
  → BRD (BR-..., KPI-...)
  → FSD (FR-..., AC-..., RULE-...)
  → design doc + ADR (DD-..., ADR-...)
  → OpenAPI contract per api_version
  → test plan + test cases (TC-..., DEF-...)
  → quality gate + release/CHANGELOG
  → daily report with PR/issue evidence
  ↺ change requests return through RTM
```

## Minimum RTM columns

| Requirement ID | Source artefact | Design / ADR | Contract / api_version | Test case(s) | Release evidence | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `{{BR-001}}` | `{{BRD_SECTION}}` | `{{ADR_OR_DESIGN_SECTION}}` | `{{API_VERSION_OR_NA}}` | `{{TC_IDS}}` | `{{PR_OR_RELEASE_ID}}` | `{{COVERED_OR_ORPHAN}}` |

Treat `orphan` on either side as a review blocker. A stable ID is more important than identical prose: downstream artefacts should reference upstream IDs, not duplicate upstream text.

## Recommended canonical tree

```text
docs/
├── README.md                 # navigation hub, not a dump of all content
├── requirements/
│   ├── BRD.md
│   └── FSD.md
├── design/
│   ├── design-docs/
│   └── adr/
├── api/
│   └── openapi/              # one description per major version
├── testing/
│   ├── test-plan.md
│   └── reports/
├── reports/
│   └── daily/
├── templates/                # placeholders only; filled copies go to canonical paths
└── CHANGELOG.md
```

Keep one canonical path per artefact. `README.md` links to artefacts; it does not become a second copy. Templates stay separate from filled artefacts so placeholders can be audited mechanically.

## Phase exit decisions

| From | To | Exit decision |
| --- | --- | --- |
| BRD | FSD | Business owner signs off on scope, KPI, assumptions, and `.Baselined` status. |
| FSD | Design | Every functional requirement has testable acceptance criteria and an RTM row. |
| Design | Test plan | Decisions, rejected alternatives, migration, security, observability, and rollback are recorded. |
| FSD/design | Test plan | Contract and AC exist; test cases can reference IDs rather than guess intent. |
| Test plan | Release | Entry/exit criteria met, fail-closed CI gate green, residual risk accepted. |
| Release | Daily operation | Release evidence and per-version metrics are queryable. |

For the full tree variants and release artefacts, read `../../assets/standards/07-skema-folder-project.md` and `../../docs/TEMPLATE-INDEX.md`.
