# Standard corrections and evidence boundaries

Use this table before asserting conformance or quoting a standard in a review.

| Topic | Correct statement | Why it matters | Source |
| --- | --- | --- | --- |
| HTTP lifecycle headers | **RFC 8594 defines `Sunset`; RFC 9745 defines `Deprecation`.** Both are hints; `Sunset` must not be earlier than `Deprecation`. | Reversing them produces invalid migration notices. | [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html), [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html) |
| ISO/IEC/IEEE 29119-3:2021 | Test Strategy is **part of Test Plan**, clause 7.2.7; Test Summary Report maps to Test Completion Report, clause 7.4. Tailored conformance is allowed. | Prevents six unnecessary documents and false conformance claims. | [ISO/IEC/IEEE 29119-3:2021 preview](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf) |
| WCAG 2.2 | Level AA means **all A and AA criteria**. 2.3.3 Animation from Interactions is **AAA**; `prefers-reduced-motion` is not an AA requirement and remains a Media Queries Level 5 Working Draft construct. | Avoids overclaiming accessibility conformance. Reduced motion can still be an internal product rule. | [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [Media Queries Level 5](https://www.w3.org/TR/mediaqueries-5/#prefers-reduced-motion) |
| BRD/FSD | ISO/IEC/IEEE 29148:2018 uses **BRS/SRS** information-item language; "BRD" and "FSD" are industry conventions, not mandatory standard names. IEEE 830-1998 is superseded. | Do not claim a section list is ISO-mandated. | [ISO/IEC/IEEE 29148:2018 catalogue](https://www.iso.org/standard/72086.html) |
| ISO/IEC/IEEE 42010:2022 | It specifies what an architecture description must address, but **does not prescribe format, notation, process, or chapter order**. | C4, arc42, and ADR are compatible choices, not standard compliance proofs. | [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html) |
| MADR | Version 4.0.0 is dated 2024-09-17. Supersede an ADR by adding a linked new record rather than rewriting history. | Keeps an append-only decision log. | [MADR](https://adr.github.io/madr/) |
| Design Tokens | DTCG Format Module 2025.10 is a stable **Community Group Final Specification**, not a W3C Standard or Standards Track document. | Do not cite it as a W3C standard. | [DTCG Format Module 2025.10](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/) |
| OWASP ASVS | Stable release cited by the research is 5.0.0 (2025). | Version security requirements explicitly. | [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) |
| OpenAPI versioning | `openapi`, `info.version`, `/api/vN`, and SDK version are four distinct values. | Prevents contradictory release metadata. | [OpenAPI Specification](https://spec.openapis.org/oas/v3.2.0.html) |

## Evidence boundaries recorded by the research

- Full text of several ISO/IEEE/PMI standards is paywalled; verification used official catalogues, abstracts, tables of contents, and official previews. Do not invent clause wording from those sources.
- Some secondary links were unavailable during research (for example Google re:Work, parts of DORA flow metrics, and certain PayPal/ASP.NET pages). State this rather than silently treating them as verified.
- Ratios between unit/integration/E2E tests, escalation SLAs, deprecation notice periods, and N-1 versus N-2 support are organisation decisions. No standard in the corpus fixes those numbers.
- SMART/INVEST and Draft/Review/Approved/Baselined are useful heuristics and workflow conventions, not ISO/IEC/IEEE 29148 clauses.

When a new source contradicts this table, update the table and the affected focused skill in the same change, and cite the primary source that resolves the conflict.
