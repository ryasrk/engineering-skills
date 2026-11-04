> Sumber: ISO/IEC/IEEE 29119-3:2021 — https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf
> Catatan: Dipakai saat menyusun rencana pengujian proyek atau rilis lengkap dengan strategi, spesifikasi test case, laporan status, dan laporan penyelesaian dalam satu dokumen.
# {{PRODUCT_NAME}} — Test Plan, Test Strategy & Test Reports
> Mode konformasi: {{FULL_OR_TAILORED_CONFORMANCE}} terhadap ISO/IEC/IEEE 29119-3:2021
> Subset dokumentasi yang diklaim: {{CLAIMED_DOCUMENT_SUBSET}}
> Justifikasi tailoring: {{TAILORING_JUSTIFICATION}}

## 0. Document control — Klausul 5.2
| Field | Nilai |
| --- | --- |
| Unique identifier | {{DOC_ID}} |
| Issuing organization | {{ISSUING_ORG}} |
| Approval authority | {{APPROVER_ROLE}} |
| Change history | {{VERSION}} / {{CHANGE_DATE}} / {{CHANGED_BY}} / {{CHANGE_SUMMARY}} |
| Status | {{DRAFT_OR_APPROVED_OR_RETIRED}} |
| Introduction | {{DOC_PURPOSE}} |
| Scope | {{IN_SCOPE}} / {{OUT_OF_SCOPE}} |
| References | {{TEST_BASIS_REFS}} / {{POLICY_REF}} / {{STANDARDS_LIST}} |
| Glossary | {{GLOSSARY_LINK}} |

## 1. Referensi ke Test Policy — Klausul 6.2
| Item kebijakan | Isi kebijakan | Deviasi proyek ini |
| --- | --- | --- |
| Objectives of testing | {{POLICY_TESTING_OBJECTIVES}} | {{POLICY_DEVIATION_OR_NONE}} |
| Test process | {{POLICY_PROCESS_REF}} | {{DEVIATION}} |
| Test organization structure | {{POLICY_ORG_STRUCTURE}} | {{DEVIATION}} |
| Tester training | {{POLICY_TRAINING}} | {{DEVIATION}} |
| Tester ethics | {{POLICY_ETHICS}} | {{DEVIATION}} |
| Standards | {{POLICY_STANDARDS}} | {{DEVIATION}} |
| Other relevant policies | {{POLICY_RELATED}} | {{DEVIATION}} |
| Measuring the value of testing | {{POLICY_METRICS}} | {{DEVIATION}} |
| Test asset archiving and reuse | {{POLICY_ARCHIVING}} | {{DEVIATION}} |
| Test process improvement | {{POLICY_IMPROVEMENT}} | {{DEVIATION}} |

## 2. Context of testing — Klausul 7.2.2
- Test item / build: {{TEST_ITEM}} @ {{BUILD_SHA}}
- Test objectives: {{TEST_OBJECTIVES}}
- Test basis (cukup ID, tanpa isi dokumen): {{TEST_BASIS_IDS}}
- Lingkungan target: {{TARGET_ENVIRONMENTS}}
- Batas waktu & jendela rilis: {{RELEASE_WINDOW}}
- Constraint: {{CONSTRAINTS}}

## 3. Assumptions and constraints — Klausul 7.2.3
| ID | Asumsi / constraint | Dampak jika meleset | Owner |
| --- | --- | --- | --- |
| {{ASSUMPTION_ID}} | {{ASSUMPTION_TEXT}} | {{IMPACT}} | {{OWNER}} |

## 4. Stakeholders — Klausul 7.2.4
| Peran | Nama/tim | Tanggung jawab pengujian | Kebutuhan training |
| --- | --- | --- | --- |
| {{ROLE}} | {{PERSON_OR_TEAM}} | {{TEST_RESPONSIBILITY}} | {{TRAINING_NEED}} |

## 5. Testing communication — Klausul 7.2.5
- Kanal: {{CHANNELS}} (dashboard CI/CD, task board, formal report)
- Periode pelaporan: {{REPORTING_PERIOD}}
- Template & audiens: {{REPORT_TEMPLATE_AND_AUDIENCE}}
- Eskalasi blocker: {{ESCALATION_PATH}}

## 6. Risk register — Klausul 7.2.6 (risk-based testing)
| risk_id | Kategori (project/product) | Deskripsi | Likelihood | Impact | risk_level | Mitigasi via test | Linked test_case_ids | Owner | Residual risk | Keputusan |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| {{RISK_ID}} | {{RISK_CATEGORY}} | {{RISK_DESC}} | {{LIKELIHOOD}} | {{IMPACT}} | {{RISK_LEVEL}} | {{MITIGATION_TEST_TYPE}} | {{TEST_CASE_IDS}} | {{RISK_OWNER}} | {{RESIDUAL_RISK}} | {{ACCEPT_OR_MITIGATE_OR_TRANSFER}} |

## 7. Test strategy — Klausul 7.2.7
| test_level / test_type | Teknik desain (29119-4) | Completion / exit criteria | Tool resmi | Test data | Environment | Deliverable | Prioritas dari risiko |
| --- | --- | --- | --- | --- | --- | --- | --- |
| {{LEVEL_TYPE}} | {{DESIGN_TECHNIQUE}} | {{EXIT_CRITERIA}} | {{TOOL_AND_DOCS_URL}} | {{TEST_DATA_ID}} | {{ENV_ID}} | {{DELIVERABLE}} | {{RISK_IDS}} |

- Retesting & regression: {{RETEST_REGRESSION_SCOPE}} / {{REGRESSION_SUITE_ID}}
- Komposisi suite (heuristic, bukan norma): unit {{UNIT_SHARE}}, integration {{INTEGRATION_SHARE}}, contract {{CONTRACT_SHARE}}, E2E {{E2E_SHARE}}
- Model yang dipakai: {{PYRAMID_OR_TROPHY_OR_HYBRID}}; alasan SMURF: {{SMURF_TRADEOFF_NOTE}}
- Shift-left practices: {{SPEC_REVIEW}}, {{TESTS_BEFORE_CODE}}, {{CI_FEEDBACK}}, {{STATIC_ANALYSIS}}, {{EARLY_NFR}}
- Deviasi dari Organizational Test Practices: {{PRACTICE_DEVIATIONS}}

## 8. Testing activities, estimates, staffing, schedule — Klausul 7.2.8–7.2.10
| Aktivitas | Estimasi | Owner | Mulai | Selesai | Dependensi |
| --- | --- | --- | --- | --- | --- |
| {{ACTIVITY}} | {{EFFORT_ESTIMATE}} | {{OWNER}} | {{START_DATE}} | {{END_DATE}} | {{DEPENDENCY}} |

## 9. Entry / exit criteria & Definition of Done — ISTQB CTFL v4.0 §5.1.3
| Gate | Entry criteria | Exit criteria | Bukti | Approver |
| --- | --- | --- | --- | --- |
| {{GATE_ID}} | {{ENTRY_CRITERIA}} | {{EXIT_CRITERIA}} | {{EVIDENCE_LINK}} | {{APPROVER}} |
| Definition of Ready | {{DOR_CRITERIA}} | — | {{DOR_EVIDENCE}} | {{APPROVER}} |
| Definition of Done | — | {{DOD_CRITERIA}} | {{DOD_EVIDENCE}} | {{APPROVER}} |

- Coverage target: diff/per-commit {{NEW_CODE_COVERAGE_THRESHOLD}}, branch coverage {{BRANCH_COVERAGE_THRESHOLD}} untuk modul {{CRITICAL_MODULES}}, requirement coverage {{REQUIREMENT_COVERAGE_TARGET}}, mutation testing {{MUTATION_SCOPE}}
- Exit karena waktu/budget: {{TIME_BUDGET_EXIT_ALLOWED}}; persetujuan risiko oleh {{RISK_ACCEPTER}} pada {{RISK_ACCEPTANCE_DATE}}

## 10. Quality gates CI/CD
| Stage | Perintah / check | Fail-closed? | Required status check | Artefak bukti |
| --- | --- | --- | --- | --- |
| {{STAGE_UNIT}} | {{UNIT_COMMAND}} | {{YES_NO}} | {{CHECK_NAME_UNIT}} | {{JUNIT_XML_PATH}} |
| {{STAGE_INTEGRATION}} | {{INTEGRATION_COMMAND}} | {{YES_NO}} | {{CHECK_NAME_INTEGRATION}} | {{REPORT_PATH}} |
| {{STAGE_CONTRACT}} | {{CAN_I_MERGE_COMMAND}} | {{YES_NO}} | {{CHECK_NAME_CONTRACT}} | {{PACT_BROKER_URL}} |
| {{STAGE_E2E}} | {{PLAYWRIGHT_COMMAND}} | {{YES_NO}} | {{CHECK_NAME_E2E}} | {{TRACE_PATH}} |
| {{STAGE_SECURITY}} | {{SECURITY_SCAN_COMMAND}} | {{YES_NO}} | {{CHECK_NAME_SECURITY}} | {{SCAN_ARTIFACT_PATH}} |
| {{STAGE_PERF}} | {{K6_COMMAND}} | {{YES_NO}} | {{CHECK_NAME_PERF}} | {{K6_SUMMARY_PATH}} |
| {{PRE_DEPLOY}} | {{CAN_I_DEPLOY_COMMAND}} | {{YES_NO}} | {{CHECK_NAME_DEPLOY}} | {{DEPLOY_MATRIX_URL}} |
| {{POST_DEPLOY}} | {{SYNTHETIC_CHECK_COMMAND}} | {{YES_NO}} | {{CHECK_NAME_PROD}} | {{OBSERVABILITY_DASHBOARD}} |

- Flake budget: {{FLAKE_BUDGET}}; quarantine suite: {{QUARANTINE_SUITE}}; SLA perbaikan: {{FLAKE_FIX_SLA}}
- Kebijakan fallback policy keamanan: {{FAIL_CLOSED_OR_APPROVED_EXCEPTION}}

## 11. Traceability matrix — definisi 3.26
| requirement_id | risk_id | test_model_id | coverage_item | test_case_id | test_result | incident_id | residual_risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| {{REQUIREMENT_ID}} | {{RISK_ID}} | {{TEST_MODEL_ID}} | {{COVERAGE_ITEM}} | {{TEST_CASE_ID}} | {{PASS_FAIL_BLOCKED}} | {{INCIDENT_ID_OR_NONE}} | {{RESIDUAL_RISK}} |

## 12. Test data & environment readiness — Klausul 8.5–8.8
| ID | Deskripsi | Sumber / masking | Responsibility | Period needed | Resetting needs | Archiving / disposal | Status readiness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| {{TEST_DATA_ID}} | {{DATA_DESC}} | {{DATA_SOURCE_AND_MASKING}} | {{DATA_OWNER}} | {{PERIOD_NEEDED}} | {{RESET_PROCEDURE}} | {{RETENTION_POLICY}} | {{READY_OR_BLOCKED}} |
| {{ENV_ID}} | {{ENV_DESC}} | {{ENV_PROVISIONING}} | {{ENV_OWNER}} | {{PERIOD_NEEDED}} | {{ENV_RESET_PROCEDURE}} | {{ENV_DISPOSAL}} | {{READY_OR_BLOCKED}} |

## 13. Test case specification — Klausul 8.3
| test_case_id | Objective | requirement_id | risk_id | Priority | Preconditions | test_data_id | Langkah | Expected results | Postconditions / cleanup |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| {{TEST_CASE_ID}} | {{OBJECTIVE}} | {{REQUIREMENT_ID}} | {{RISK_ID}} | {{PRIORITY}} | {{PRECONDITIONS}} | {{TEST_DATA_ID}} | {{STEP_1}}; {{STEP_2}}; {{STEP_N}} | {{EXPECTED_RESULTS}} | {{CLEANUP}} |

## 14. Actual results, test result & execution log — Klausul 8.9–8.10
| test_case_id | build_sha | environment_id | Waktu eksekusi | Actual results | Result (pass/fail/blocked) | Log / bukti | incident_id |
| --- | --- | --- | --- | --- | --- | --- | --- |
| {{TEST_CASE_ID}} | {{BUILD_SHA}} | {{ENV_ID}} | {{EXECUTED_AT}} | {{ACTUAL_RESULTS}} | {{RESULT}} | {{EVIDENCE_LINKS}} | {{INCIDENT_ID_OR_NONE}} |

## 15. Test incident report — Klausul 8.11 / ISTQB §5.5
| Field | Nilai |
| --- | --- |
| incident_id | {{INCIDENT_ID}} |
| Title | {{SHORT_SUMMARY}} |
| Timing / tanggal ditemukan | {{OBSERVED_AT}} |
| Originator & peran | {{AUTHOR_AND_ROLE}} |
| Test object & environment | {{TEST_OBJECT}} / {{ENV_ID}} / {{BUILD_SHA}} |
| Context | {{TEST_CASE_ID}} / {{TEST_ACTIVITY}} / {{SDLC_PHASE}} / {{TEST_DATA_ID}} |
| Repro steps | {{REPRO_STEP_1}}; {{REPRO_STEP_2}}; {{REPRO_STEP_N}} |
| Expected results | {{EXPECTED_RESULTS}} |
| Actual results | {{ACTUAL_RESULTS}} |
| Severity | {{SEVERITY_SCALE_AND_VALUE}} |
| Priority to fix | {{PRIORITY_SCALE_AND_VALUE}} |
| Risk | {{LINKED_RISK_ID}} |
| Status | {{OPEN_DEFERRED_DUPLICATE_REOPENED_CLOSED_REJECTED}} |
| Bukti | {{LOG_DUMP}} / {{SCREENSHOT}} / {{TRACE_ZIP}} / {{RECORDING}} |
| References | {{TEST_CASE_ID}} / {{REQUIREMENT_ID}} / {{CI_RUN_URL}} |

## 16. Test status report — Klausul 7.3
| Field | Nilai |
| --- | --- |
| Reporting period | {{PERIOD_START}} – {{PERIOD_END}} |
| Test status | {{AHEAD_ON_TRACK_BEHIND}} |
| Progress against test plan | {{PLANNED_VS_ACTUAL}} |
| Factors blocking progress | {{BLOCKERS}} / {{WORKAROUNDS}} |
| Test measures | {{PASS_RATE}} / {{FLAKY_RATE}} / {{COVERAGE}} / {{DEFECT_METRICS}} / {{RESIDUAL_RISK_LEVEL}} |
| New and changed risks | {{NEW_OR_CHANGED_RISKS}} |
| Planned testing | {{NEXT_PERIOD_PLAN}} |

## 17. Test Completion Report / Test Summary Report — Klausul 7.4
| Field | Nilai |
| --- | --- |
| Summary of testing performed | {{TESTING_SUMMARY}} |
| Deviations from planned testing | {{DEVIATIONS}} |
| Test completion evaluation | {{EXIT_CRITERIA_MET_YES_NO}} / {{EVALUATION_NOTE}} |
| Factors that blocked progress | {{BLOCKERS}} |
| Test measures | {{DDP_OR_ESCAPE_RATE}} / {{PASS_RATE}} / {{COVERAGE}} / {{CHANGE_FAIL_RATE}} / {{FAILED_DEPLOYMENT_RECOVERY_TIME}} |
| Residual risks | {{UNMITIGATED_RISKS}} / {{DEFECTS_NOT_FIXED}} |
| Test deliverables | {{DELIVERABLE_LINKS}} |
| Reusable test assets | {{REUSABLE_ASSETS}} |
| Lessons learned | {{LESSONS_LEARNED}} |
| Keputusan rilis | {{GO_NO_GO}} oleh {{RELEASE_APPROVER}} pada {{DECISION_DATE}} |
| Penerimaan risiko (bila exit karena waktu/budget) | {{RISK_ACCEPTER}} / {{RISK_ACCEPTANCE_REF}} |

## 18. Approval & sign-off
| Peran | Nama | Tanggal | Tanda tangan / referensi approval |
| --- | --- | --- | --- |
| {{APPROVER_ROLE}} | {{APPROVER_NAME}} | {{APPROVAL_DATE}} | {{APPROVAL_REF}} |
