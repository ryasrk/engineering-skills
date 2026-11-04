> Sumber: GitHub Docs — About protected branches — https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
> Catatan: Dipakai saat menyiapkan quality gate pull request di GitHub Actions dengan required status checks dan artefak bukti pengujian.
# Template quality gate CI — GitHub Actions

name: {{WORKFLOW_NAME}}
on:
  pull_request:
    branches: [{{PROTECTED_BRANCH}}]
  push:
    branches: [{{PROTECTED_BRANCH}}]

jobs:
  {{JOB_UNIT}}:
    name: {{UNIQUE_CHECK_NAME_UNIT}}
    runs-on: {{RUNNER}}
    steps:
      - uses: actions/checkout@v4
      - name: Unit tests
        run: {{UNIT_TEST_COMMAND}}
      - name: Upload JUnit XML
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: {{JUNIT_ARTIFACT_NAME}}
          path: {{JUNIT_XML_PATH}}

  {{JOB_CONTRACT}}:
    name: {{UNIQUE_CHECK_NAME_CONTRACT}}
    runs-on: {{RUNNER}}
    steps:
      - uses: actions/checkout@v4
      - name: Publish pact + provider verification
        run: {{PACT_PUBLISH_COMMAND}}
      - name: can-i-merge
        run: {{CAN_I_MERGE_COMMAND}}

  {{JOB_E2E}}:
    name: {{UNIQUE_CHECK_NAME_E2E}}
    runs-on: {{RUNNER}}
    steps:
      - uses: actions/checkout@v4
      - name: E2E critical journeys
        run: {{PLAYWRIGHT_COMMAND}}
      - name: Upload traces
        if: failure()
        uses: actions/upload-artifact@v4
        with:
          name: {{TRACE_ARTIFACT_NAME}}
          path: {{TRACE_PATH}}

  {{JOB_PERF}}:
    name: {{UNIQUE_CHECK_NAME_PERF}}
    runs-on: {{RUNNER}}
    steps:
      - uses: actions/checkout@v4
      - name: Load test with thresholds
        run: {{K6_RUN_COMMAND}}
        # k6 mengembalikan exit code non-zero saat threshold gagal

  {{JOB_GATE}}:
    name: {{UNIQUE_CHECK_NAME_GATE}}
    needs: [{{JOB_UNIT}}, {{JOB_CONTRACT}}, {{JOB_E2E}}, {{JOB_PERF}}]
    runs-on: {{RUNNER}}
    steps:
      - name: Aggregate gate
        run: {{GATE_AGGREGATION_COMMAND}}
