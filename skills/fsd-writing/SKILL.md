---
name: fsd-writing
description: "Use when drafting, reviewing, or updating a Functional Specification Document (FSD) or Software Requirements Specification (SRS), user stories with Given/When/Then acceptance criteria, business rules, decision tables, or authorization matrices. Also use when establishing bidirectional traceability from business requirements to test cases."
---

# FSD writing

Bridge business requirements into verifiable, testable system behaviors and contracts without jumping into implementation-specific code.

## Work from the source artefact

1. Read `references/fsd-guide.md` for standards context, acceptance criteria conventions, and condensed best practices.
2. Copy `assets/02-FSD.md` into the target project. Fill each `{{...}}` placeholder.
3. Use `assets/02-RTM.md` to map upstream `BR-...` to functional requirements (`FR-...`), acceptance criteria (`AC-...`), and downstream test cases (`TC-...`).
4. Validate the draft using `assets/02-Checklist-Review.md` before requesting technical and product sign-off.

## Decisions that materially change the result

- **Normative status:** FSD is an industry convention; the formal anchor is SRS under ISO/IEC/IEEE 29148:2018. IEEE 830-1998 is formally superseded.
- **Verifiable acceptance criteria:** Every user story must include acceptance criteria in Gherkin (`Given / When / Then`) format covering at least 3 distinct scenarios:
  1. Happy path (normal flow).
  2. Edge cases (boundary conditions, inclusive limits).
  3. Error/failure paths (invalid inputs, timeouts, authorization rejections).
- **Business rules:** Document rules with numbered constraints, decision tables with an explicit default/fallback row, and role-based authorization matrices rather than ambiguous prose paragraphs.
- **Interface boundaries:** Embed data models, field validation rules, and OpenAPI 3.1/3.2 schema contracts directly or by explicit reference.
- **Traceability:** Maintain bidirectional traceability. Every `FR-...` must map back to a `BR-...` and forward to acceptance criteria and test cases. Flag orphan requirements immediately.

## Review before sign-off

- System actors, personas, and preconditions are explicitly stated.
- All non-functional requirements (performance SLA, security, audit logging) have measurable thresholds.
- Error codes, fallback behaviors, and edge cases are documented with expected status and payloads.
- RTM links every functional requirement to upstream business goals and downstream QA plans.
- Sign-off matrix includes Product Owner, Tech Lead, and QA Lead.
