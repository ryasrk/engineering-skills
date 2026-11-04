---
name: daily-reporting
description: "Use when authoring, structuring, or reviewing daily engineering reports, asynchronous standup updates, project status summaries for clients or management, blocker escalation matrices, or team communication protocols. Also use when eliminating subjective status theater and aligning updates with tangible PR/issue evidence."
---

# Daily reporting and engineering status updates

Deliver high-signal, evidence-backed daily progress reports and asynchronous standups that drive blockers to resolution without bureaucratic overhead.

## Work from the source artefact

1. Read `references/05-laporan-harian.md` for foundational research and cited guidelines. Read `references/06-laporan-harian.md` for condensed reporting practices.
2. Copy `assets/05-Laporan-Harian.md` into your documentation or operational repository.
3. Complete the ten standard sections: TL;DR, completed deliverables (meeting Definition of Done), WIP, blockers with assigned owners, scope/risk changes, event-derived metrics, decisions needed, tomorrow's plan, audience-specific view, and audit trail.

## Decisions that materially change the result

- **Scrum Guide vs Atlassian origin:** The 2020 Scrum Guide specifies a 15-minute inspection-and-adaptation event for Developers focused on the Sprint Goal. The popular "yesterday / today / blockers" triad is an Atlassian industry pattern, not a formal Scrum Guide requirement. Adapt format to team mode (synchronous verbal vs asynchronous written).
- **Eliminate status theater:** Ban subjective percentages (e.g. "feature is 85% done"). Progress must be grounded in tangible, event-derived work items: merged pull requests, closed issues, completed test suites, or passing deployment checks.
- **Blocker escalation discipline:** Every listed blocker must name a single responsible owner, an escalation level (L1/L2/L3), an expected resolution time, and an actionable next step. Never report a blocker without ownership.
- **Audience-segmented communication:**
  - *Internal engineering:* code diffs, branch names, technical blockers, test logs.
  - *Engineering managers:* delivery velocity, systemic blockers, inter-team dependencies, scope changes.
  - *Clients and executive sponsors:* milestone progress, business impact, risks, decisions required, and target delivery dates (omitting internal friction and unvetted bugs).
- **Privacy compliance:** Protect personal and sensitive operational data under GDPR 2016/679 and organizational confidentiality guidelines. Avoid pasting credentials, customer PII, or internal tokens into status logs.

## Quality checklist for daily updates

- TL;DR summarizes status in 3 concise sentences.
- Every completed item links directly to an issue or pull request and meets the team's Definition of Done.
- Blockers state owner, duration, and target resolution time.
- Decisions requested are explicit and highlight the consequence of inaction.
