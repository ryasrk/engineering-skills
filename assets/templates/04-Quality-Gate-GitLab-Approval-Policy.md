> Sumber: GitLab Docs — Merge request approval policies — https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/
> Catatan: Dipakai saat mendefinisikan kebijakan approval fail-closed berbasis temuan scanner keamanan pada merge request GitLab.
# Contoh policy approval (file kebijakan terpisah), fail-closed secara default
approval_policy:
  - name: {{POLICY_NAME}}
    enabled: true
    rules:
      - type: scan_finding
        branches: []
        scanners: [{{SCANNER_LIST}}]
        vulnerabilities_allowed: {{VULNERABILITIES_ALLOWED}}
        severity_levels: [{{SEVERITY_LEVELS}}]
        vulnerability_states: [new_needs_triage]
    actions:
      - type: require_approval
        approvals_required: {{APPROVALS_REQUIRED}}
        user_approvers: [{{APPROVER_GROUP}}]
    fallback_behavior:
      fail: closed
