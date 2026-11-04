---
name: brd-writing
description: "Use when drafting, reviewing, or baselining a Business Requirements Document (BRD), business case, stakeholder requirements, business KPI/OKR, scope in/out, RACI sign-off, or a BRD requirements traceability matrix. Also use when someone asks whether BRD section lists or SMART/INVEST are mandated by ISO 29148."
---

# BRD writing

Produce business-level requirements that a sponsor can approve and downstream teams can trace — not a disguised solution specification.

## Work from the source artefact

1. Read `references/brd-guide.md` for standards context, source conflicts, and condensed best practices.
2. Copy `assets/01-BRD.md` into the target project. Fill every `{{...}}` placeholder; use `assets/01-Checklist-Review-BRD.md` and `assets/01-Pola-Kalimat-Kebutuhan-Bisnis.md` for review and requirement phrasing. For cross-phase requirements tracing, use the canonical Master RTM from `engineering-docs`.
3. Keep a stable `BR-...` ID for each requirement and a matching RTM row. If the user only asks for a review, check the existing document against the checklist instead of replacing it with a fresh template.

## Decisions that materially change the result

- **Boundary:** a business case evaluates value, a charter authorises work, a BRD states business needs and outcomes, and PRD/SRS/FSD describe the solution. Do not move solution elements into the BRD unless the organisation has explicitly chosen the broader Atlassian-style template. The bundled research records this as a real conflict between IIBA guidance and an Atlassian template; name the choice in the document's governance section.
- **Normative status:** ISO/IEC/IEEE 29148:2018 is the nearest formal anchor (BRS/SRS information items). It does not mandate an artefact called BRD, a fixed chapter list, SMART/INVEST, or a `Draft/Review/Approved/Baselined` state machine. Mark those as team conventions where used.
- **Requirement quality:** prefer atomic, unambiguous, measurable statements with an owner and a verification method. `"fast enough"` and `"a mobile app"` are not business acceptance criteria without a threshold or an explicit out-of-scope decision.
- **Traceability:** RTM rows should point downstream by ID only. Orphan business requirements and untraceable KPIs are review defects.

## Review before sign-off

- Scope in/out, assumptions, constraints, dependencies, risks, and value/cost confidence are explicit.
- Stakeholder RACI names an accountable approver, not only a contributor list.
- KPIs have a baseline, target, measurement source, and review date.
- Every requirement has an ID, acceptance statement, and RTM row.
- Document status, version, change-control route, and sign-off are recorded.
- Claims are labelled as standard, first-party practice, or team decision; no claim that a template is ISO-mandated.

Do not write FSD use cases, detailed UI, or test cases here; hand the approved BRD to `fsd-writing` with intact IDs.
