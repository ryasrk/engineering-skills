> Sumber: GitHub Docs — About protected branches — https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
> Catatan: Dipakai saat menyiapkan quality gate pull request di GitHub Actions dengan required status checks dan artefak bukti pengujian.
# Template quality gate CI — GitHub Actions

# PERHATIAN KEAMANAN & INTEGRITAS GATE:
# 1. Actions di-pin menggunakan commit SHA penuh untuk mencegah supply-chain attacks.
# 2. Permissions dibatasi secara ketat (least privilege): contents: read.
# 3. Concurrency disetel untuk membatalkan build redundan saat ada commit baru.
# 4. FAIL-CLOSED GATE: GitHub branch protection memperlakukan skipped check sebagai lolos.
#    Oleh karena itu, job 'gate' WAJIB menggunakan 'if: always()' dan mengevaluasi status
#    setiap job prasyarat secara eksplisit agar build gagal jika ada test yang gagal/dibatalkan.

name: {{WORKFLOW_NAME}}
on:
  pull_request:
    branches: [{{PROTECTED_BRANCH}}]
  push:
    branches: [{{PROTECTED_BRANCH}}]

permissions:
  contents: read

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  unit_test:
    name: {{UNIQUE_CHECK_NAME_UNIT}}
    runs-on: {{RUNNER}}
    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
      - name: Unit tests
        run: {{UNIT_TEST_COMMAND}}
      - name: Upload JUnit XML
        if: always()
        uses: actions/upload-artifact@5d5d22a31266ced268874388b861e4b58bb5c2f3 # v4.3.1
        with:
          name: {{JUNIT_ARTIFACT_NAME}}
          path: {{JUNIT_XML_PATH}}

  contract_test:
    name: {{UNIQUE_CHECK_NAME_CONTRACT}}
    runs-on: {{RUNNER}}
    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
      - name: Publish pact + provider verification
        run: {{PACT_PUBLISH_COMMAND}}
      - name: can-i-merge
        run: {{CAN_I_MERGE_COMMAND}}

  e2e_test:
    name: {{UNIQUE_CHECK_NAME_E2E}}
    runs-on: {{RUNNER}}
    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
      - name: E2E critical journeys
        run: {{PLAYWRIGHT_COMMAND}}
      - name: Upload traces
        if: failure()
        uses: actions/upload-artifact@5d5d22a31266ced268874388b861e4b58bb5c2f3 # v4.3.1
        with:
          name: {{TRACE_ARTIFACT_NAME}}
          path: {{TRACE_PATH}}

  perf_test:
    name: {{UNIQUE_CHECK_NAME_PERF}}
    runs-on: {{RUNNER}}
    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
      - name: Load test with thresholds
        run: {{K6_RUN_COMMAND}}
        # k6 mengembalikan exit code non-zero saat threshold performa terlampaui

  gate:
    name: {{UNIQUE_CHECK_NAME_GATE}}
    needs: [unit_test, contract_test, e2e_test, perf_test]
    runs-on: {{RUNNER}}
    if: always()
    steps:
      - name: Evaluate quality gates (fail-closed enforcement)
        shell: bash
        run: |
          echo "=== Quality Gate Evaluation (Fail-Closed) ==="
          results=(
            "${{ needs.unit_test.result }}"
            "${{ needs.contract_test.result }}"
            "${{ needs.e2e_test.result }}"
            "${{ needs.perf_test.result }}"
          )
          
          has_failure=0
          for res in "${results[@]}"; do
            echo "Upstream check result: $res"
            if [ "$res" != "success" ]; then
              echo "::error::Quality gate failure: upstream check finished with status '$res' (required: 'success')"
              has_failure=1
            fi
          done

          if [ $has_failure -ne 0 ]; then
            echo "--------------------------------------------------------"
            echo "FAIL-CLOSED GATE TRIGGERED: One or more required checks"
            echo "did not complete successfully. Branch merge is blocked."
            echo "--------------------------------------------------------"
            exit 1
          fi

          echo "All required quality gates completed successfully."
