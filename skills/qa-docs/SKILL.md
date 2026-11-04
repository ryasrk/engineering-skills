---
name: qa-docs
description: "Use when creating or evaluating test strategies, test plans, test case specifications, bug reports, or test completion reports under ISO/IEC/IEEE 29119 and ISTQB. Also use when configuring fail-closed CI/CD quality gates (GitHub Actions, GitLab CI), defining test exit criteria, or auditing testing metrics like DORA and defect escape rate."
---

# QA strategy and test documentation

Design risk-based test plans and fail-closed quality gates that verify requirements, prevent defects from escaping to production, and maintain continuous delivery speed.

## Work from the source artefact

1. Read `references/testing-guide.md` for ISO/IEC/IEEE 29119 standards context, quality gate mechanisms, and condensed testing best practices.
2. Copy `assets/04-Test-Plan.md` into the project repository. It combines Test Plan (clause 7.2), Test Strategy (7.2.7), Test Case Specification (8.3), Incident Reporting (8.11), and Test Completion Report (7.4) under tailored conformance.
3. Establish exit criteria for every test level using `assets/04-Exit-Criteria-Matrix.md`.
4. Configure automated CI gates using `assets/04-Quality-Gate-GitHub-Actions.md` or `assets/04-Quality-Gate-GitLab-CI.md` along with `assets/04-Quality-Gate-GitLab-Approval-Policy.md`.

## Decisions that materially change the result

- **Active standard edition:** The governing standard is ISO/IEC/IEEE 29119 (Part 1:2022, Parts 2/3/4:2021, Part 5:2024). Edisi 2013 is superseded.
- **Test Strategy placement:** Under ISO/IEC/IEEE 29119-3:2021 clause 7.2.7, Test Strategy is a *component section within the Test Plan*, not a mandatory separate document. Tailored conformance allows combining planning, execution, and reporting assets into unified project documents.
- **Fail-closed CI quality gates:** Automate quality checks so pipelines fail closed. Required status checks, security approval policies, Pact `can-i-deploy` verification, and k6 performance thresholds must produce non-zero exit codes on breach. The aggregation gate job must use `if: always()` and explicitly check each required check result to prevent skipped jobs from masquerading as passed checks.
- **Test pyramid vs trophy:** Choose composition based on architecture:
  - Backend services/APIs: emphasize unit + contract testing + component integration.
  - Web/Mobile frontends: emphasize integration/component tests and critical-path E2E smoke journeys.
- **Meaningful vs vanity metrics:** Target Defect Detection Percentage (DDP), defect escape rate, and DORA change failure rate. Never enforce a dogmatic 100% line coverage target or report test pass rates without an unambiguous denominator.
- **Security baseline:** Target OWASP Application Security Verification Standard (ASVS) version 5.0.0 (2025).

## Review before sign-off

- Traceability connects all test cases to upstream `FR-...` and `AC-...` identifiers.
- Test environments, test data management, and isolation strategies are documented.
- Entry and exit criteria specify quantifiable criteria (zero Sev-1/Sev-2 defects, performance latency SLA).
- Flaky tests are quarantined in an automated pipeline rather than ignored.
