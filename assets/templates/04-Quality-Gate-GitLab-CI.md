> Sumber: GitLab Docs — Unit test reports — https://docs.gitlab.com/ci/testing/unit_test_reports/
> Catatan: Dipakai saat menyusun pipeline quality gate merge request di GitLab CI dengan JUnit report, security scan, trace, dan can-i-deploy.
# Template quality gate CI — GitLab CI

stages:
  - {{STAGE_TEST}}
  - {{STAGE_SECURITY}}
  - {{STAGE_GATE}}

{{JOB_UNIT}}:
  stage: {{STAGE_TEST}}
  script:
    - {{UNIT_TEST_COMMAND}}
  artifacts:
    when: always
    reports:
      junit: {{JUNIT_XML_PATH}}
    paths:
      - {{COVERAGE_REPORT_PATH}}

{{JOB_E2E}}:
  stage: {{STAGE_TEST}}
  script:
    - {{PLAYWRIGHT_COMMAND}}
  artifacts:
    when: on_failure
    paths:
      - {{TRACE_PATH}}

{{JOB_SECURITY_SCAN}}:
  stage: {{STAGE_SECURITY}}
  script:
    - {{SECURITY_SCAN_COMMAND}}
  artifacts:
    reports:
      sast: {{SAST_REPORT_PATH}}
      dependency_scanning: {{DS_REPORT_PATH}}

{{JOB_CONTRACT_GATE}}:
  stage: {{STAGE_GATE}}
  script:
    - {{CAN_I_DEPLOY_COMMAND}} --to-environment {{TARGET_ENVIRONMENT}}
