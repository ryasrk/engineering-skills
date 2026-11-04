---
name: design-docs
description: "Use when authoring or reviewing software design documents, High-Level / Low-Level Design (HLD/LLD), Architecture Decision Records (ADR/MADR), C4 model diagrams, UI/UX handoff specifications with design tokens, or accessibility Definition of Done. Also use when conducting architectural design reviews and STRIDE threat modeling."
---

# Design docs and architecture decisions

Produce actionable system design documents, decision records, and interface specifications that guide engineering implementation and pass rigorous technical reviews.

## Work from the source artefact

1. Read `references/design-guide.md` for architectural decision patterns, C4 model guidance, and condensed design best practices.
2. For system architecture or RFCs: copy `assets/03-Design-Doc.md` and complete all sections including goals, non-goals, structural design, STRIDE security analysis, observability, and rollback plans.
3. For discrete architectural decisions: copy `assets/03-ADR.md` (MADR 4.0.0 format). Maintain an immutable, append-only decision record.
4. For UI/UX component handoffs: use `assets/03-UI-UX-Spec.md` with explicit design tokens and complete state matrices (idle, loading, error, empty, disabled).
5. For accessibility compliance: verify against `assets/03-DoD-Aksesibilitas.md`.

## Decisions that materially change the result

- **Standard boundaries:** ISO/IEC/IEEE 42010:2022 sets architecture description requirements, but explicitly does *not* prescribe document templates, diagram notation, or chapter order. C4 model and arc42 are practical architectural patterns, not formal ISO standards.
- **ADR lifecycle:** MADR 4.0.0 (released 2024-09-17) uses `Proposed`, `Accepted`, `Deprecated`, and `Superseded`. When superseding a decision, create a new ADR linking back to the old one rather than editing historical records.
- **Accessibility conformance truth:** WCAG 2.2 Level AA requires satisfying *all* Level A and Level AA success criteria. Criterion 2.3.3 (Animation from Interactions) is **Level AAA**; `prefers-reduced-motion` is a Media Queries Level 5 Working Draft. Support reduced motion as an internal product quality rule without misrepresenting it as an AA legal requirement.
- **Design tokens status:** Design Tokens Format Module (DTCG 2025.10) is a Community Group Final Specification; it is **not** on the formal W3C Standards Track.
- **Failure modes and rollbacks:** Every design doc must feature non-goals, rejected alternatives with explicit rationale, data migration compatibility, and automated rollback triggers before review approval.

## Review before sign-off

- C4 diagrams include clear system context and container boundaries with defined protocols.
- Security section includes threat modeling (e.g. STRIDE) and data privacy controls.
- Observability specifies metrics, structured logging context, and latency/error SLIs.
- Rollback criteria specify automated thresholds (error rate, latency spike) and data rollback strategy.
