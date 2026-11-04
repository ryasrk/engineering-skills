## 4. Testing / QA

> Konvensi penanda: **[Standar resmi]** = ISO/IEC/IEEE, W3C, serta katalog badan standardisasi IEEE SA/ISO. **[Praktik industri]** = dokumentasi resmi vendor/proyek, riset DORA/Google, dan tulisan praktisi pada situs resminya (sub-penanda asli `[Dokumentasi resmi vendor/proyek]` / `[Praktik industri / opini]` tetap disebut). **[Rekomendasi peneliti/tim]** = turunan/inferensi (`[Inferensi]`) dari rujukan di atas, bukan klaim normatif. Penanda asli **[Sertifikasi/resmi badan]** untuk syllabus/badan resmi ISTQB dipertahankan terpisah karena bukan standar normatif; label turunan seperti **[Standar resmi — masih draft]** untuk DIS 29119-14 juga dipertahankan. Nomor edisi disebut eksplisit; rentang norma yang dibahas adalah 2024–2026.

> Template terkait: `templates/04-Test-Plan.md`, `templates/04-Exit-Criteria-Matrix.md`, `templates/04-Quality-Gate-GitHub-Actions.md`, `templates/04-Quality-Gate-GitLab-CI.md`, `templates/04-Quality-Gate-GitLab-Approval-Policy.md`.

Kelima berkas tersebut adalah artefak mandiri; bagian ini tidak menyalinnya, hanya memetakan section kuncinya.
- `templates/04-Test-Plan.md` — document control (Klausul 5.2), referensi Test Policy (6.2), context hingga schedule (7.2.1–7.2.10), **Risk register 7.2.6**, **Test Strategy 7.2.7**, entry/exit criteria dan Definition of Done, quality gates, traceability (definisi 3.26), test data/environment readiness (8.5–8.8).
- `templates/04-Test-Plan.md` (lanjutan) — Test Case Specification (8.3), actual results/execution log (8.9–8.10), Test Incident Report (8.11), **Test Status Report 7.3**, **Test Completion Report / Test Summary Report 7.4**, approval & sign-off; memuat `{{FULL_OR_TAILORED_CONFORMANCE}}` beserta justifikasi tailoring.
- `templates/04-Exit-Criteria-Matrix.md` — matriks jenis × tujuan × tools/docs resmi × contoh exit criteria: unit, integration, API/contract, E2E, regression, smoke, performance, security, accessibility, compatibility, data migration, UAT, chaos/resilience, observability produksi.
- `templates/04-Quality-Gate-GitHub-Actions.md` — job unit/contract/E2E/performance, nama check unik lintas workflow, unggah JUnit XML dan trace sebagai artifact, job agregasi gate; dipasangkan dengan required status checks serta strict/merge queue.
- `templates/04-Quality-Gate-GitLab-CI.md` — stages test/security/gate, JUnit report, artifact SAST/dependency scanning, `can-i-deploy --to-environment {{env}}`; `templates/04-Quality-Gate-GitLab-Approval-Policy.md` — aturan `scan_finding`, `severity_levels`, `vulnerabilities_allowed`, `require_approval`, `fallback_behavior.fail: closed`.

Sumber peta template: **[Standar resmi]** [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); **[Praktik industri]** [GitHub Docs — About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), [GitLab Docs — Merge request approval policies](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/), [Pact Docs — Pact Nirvana Step 6: can-i-deploy](https://docs.pact.io/pact_nirvana/step_6), [Grafana k6 Docs — Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/).

### 4.1 Ringkasan best practices

1. **[Standar resmi]** Kunci seri aktif: **ISO/IEC/IEEE 29119-1:2022, 29119-2:2021, 29119-3:2021, 29119-4:2021, 29119-5:2024**; 29119-3:2013 sudah *superseded* dan 29119-1:2013 berstatus *Withdrawn*. — [IEEE SA — seri 29119 aktif](https://standards.ieee.org/ieee/29119-3/7499/); [ISO — ISO/IEC/IEEE 29119-1:2013 (Withdrawn)](https://www.iso.org/standard/45142.html)
2. **[Standar resmi]** Dokumen tingkat organisasi adalah **Test Policy (6.2)** yang menjelaskan *purpose, goals, principles, scope* tanpa merinci cara pengujian, dan **Organizational Test Practices (6.3)**; Test Policy tidak boleh dipakai sebagai pengganti rencana proyek. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, definisi 3.20 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
3. **[Standar resmi]** Setiap dokumen pengujian memuat *common information elements* Klausul 5.2: unique identifier, issuing organization, approval authority, change history, status, introduction, scope, references, glossary. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, Klausul 5.2 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
4. **[Standar resmi]** Susun strategi dari **Risk register (7.2.6)**: risiko hadir pula di *New and changed risks* (7.3.7), *Residual risks* (7.4.7), dan *Risk* pada incident report (8.11.8). — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
5. **[Sertifikasi/resmi badan]** Definisikan entry/exit criteria **per test level**; di Agile exit criteria sering disebut Definition of Done dan entry criteria Definition of Ready. Exit karena habis waktu/budget sah hanya dengan peninjauan dan penerimaan risiko oleh pemangku kepentingan. — [ISTQB TBOK — CTFL Syllabus v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
6. **[Rekomendasi peneliti/tim · Inferensi]** Pyramid, trophy, shift-left, dan SMURF menjawab pertanyaan berbeda (seberapa banyak, kapan, kriteria trade-off) sehingga **boleh dipakai bersamaan**; tidak ada yang saling menggantikan. — [Google Testing Blog 2024](https://testing.googleblog.com/2024/10/?m=0); [ISTQB TBOK — CTFL Syllabus v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
7. **[Sertifikasi/resmi badan]** Shift-left berarti review spesifikasi, test sebelum kode, CI/CD ber-feedback cepat, static analysis sebelum dynamic testing, dan non-functional testing sejak component level; **bukan** meniadakan pengujian akhir. — [ISTQB TBOK — CTFL Syllabus v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
8. **[Praktik industri · Dokumentasi resmi vendor/proyek]** Gate harus berbasis artefak yang tidak bisa dilewati: required status checks dengan nama job unik (GitHub), approval policy default `fail: closed` (GitLab), threshold k6 dengan exit code non-zero, dan `can-i-deploy` menjelang deploy (Pact). — [GitHub Docs — About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches); [GitLab Docs — Merge request approval policies](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/); [Grafana k6 Docs — Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/); [Pact Docs — Pact Nirvana Step 6: can-i-deploy](https://docs.pact.io/pact_nirvana/step_6)
9. **[Praktik industri · Praktik industri / opini]** **100% line coverage menyesatkan**: tidak ada angka coverage ideal universal, 100% memberi *false sense of security* dan utang pemeliharaan test bernilai rendah; 100% statement coverage pun tidak menjamin decision logic maupun defect data-dependent. — [Google Testing Blog — Code Coverage Best Practices](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html); [ISTQB TBOK — CTFL Syllabus v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
10. **[Praktik industri · Dokumentasi resmi vendor/proyek]** Kunci versi standar keamanan: **OWASP ASVS 5.0.0 (Mei 2025)** dengan format `v5.0.0-1.2.5`; WSTG harus mengunci `Latest` atau `Stable v4.2`; WCAG 2.2 diuji dengan automated testing **dan** human evaluation. — [OWASP/ASVS v5.0.0 README (repositori resmi)](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/README.md); [OWASP WSTG — Latest / About](https://wstg.owasp.org/latest/1-About/); [W3C — WCAG 2.2 Recommendation](https://www.w3.org/TR/WCAG22/)
11. **[Praktik industri · Praktik industri / opini]** DORA per 2026 memakai **lima metrik**, bukan "four keys"; ukur per aplikasi/service, pasangkan speed dan stability, dan jangan jadikan metrik sebagai target tunggal. — [DORA — Software delivery performance metrics](https://dora.dev/guides/dora-metrics/)
12. **[Sertifikasi/resmi badan]** Pisahkan **spesifikasi** (prekondisi, data uji, langkah, expected result) dari **hasil eksekusi** (actual result, pass/fail, log); pisahkan **severity** (dampak) dari **priority** (urutan perbaikan); version-control semua configuration item. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, definisi 3.1/3.2/3.22 dan daftar isi (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [ISTQB TBOK — CTFL Syllabus v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
13. **[Rekomendasi peneliti/tim · Inferensi]** Flaky test adalah defect: catat `flaky` terpisah dari `passed`, karantina dengan tiket dan SLA, retry hanya penyerap sementara, dan tetapkan `flake_budget = 0` untuk gate rilis. — [Playwright Docs — Retries](https://playwright.dev/docs/test-retries); [Google Testing Blog — SMURF](https://testing.googleblog.com/2024/10/?m=0)
14. **[Sertifikasi/resmi badan]** Pisahkan *Test Status Report* (periode tertentu, untuk test control) dari *Test Completion Report* (penutupan, untuk keputusan rilis); quality adalah tanggung jawab whole team, bukan gerbang QA di akhir. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [ISTQB TBOK — CTFL Syllabus v4.0.1](https://tbok.istqb.org/view-pdf/id/2)

### 4.2 Koreksi yang wajib dipakai

| No | Koreksi | Status bukti | Rujukan |
| --- | --- | --- | --- |
| K1 | Seri aktif adalah **ISO/IEC/IEEE 29119-1:2022, -2:2021, -3:2021, -4:2021, -5:2024**; edisi 2013 sudah digantikan, 29119-3:2013 tidak lagi dipakai. | **[Standar resmi]** | [IEEE SA — seri 29119 aktif](https://standards.ieee.org/ieee/29119-3/7499/); [ISO Online Browsing Platform — ISO/IEC/IEEE 29119-1:2022](https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso-iec-ieee%3A29119%3A-1%3Aed-2%3Av1%3Aen) |
| K2 | Dalam 29119-3:2021 **Test Strategy ADALAH bagian dari Test Plan, Klausul 7.2.7** — bukan dokumen organisasi berdiri sendiri. Istilah "Organizational Test Strategy" bukan entitas kanonik edisi 2021. | **[Standar resmi]** + **[Rekomendasi peneliti/tim]** | [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, daftar isi (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf) |
| K3 | **Test Summary Report = Test Completion Report, Klausul 7.4**; *Test Status Report* (7.3) adalah entitas terpisah dengan periode pelaporan. | **[Standar resmi]** | [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, definisi 3.9 dan 3.24 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf) |
| K4 | **Tailored conformance diizinkan** (Klausul 4.1): heading boleh diubah, dokumen boleh digabung/dipisah; organisasi *shall* menyatakan *full* atau *tailored* dan *shall* memberi justifikasi. Annex A (normative) memetakan `shall/should/may`. | **[Standar resmi]** | [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, Klausul 4.1 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf) |
| K5 | **Tidak ada rasio pyramid yang distandardisasi**: tidak satu pun standar ISO/IEC/IEEE maupun ISTQB menetapkan persentase unit:integration:contract:E2E; angka komposisi adalah keputusan tim berbasis analisis risiko, bukan KPI audit. | **[Standar resmi]** + **[Rekomendasi peneliti/tim]** | [ISTQB TBOK — CTFL Syllabus v4.0.1](https://tbok.istqb.org/view-pdf/id/2); [Google Testing Blog — SMURF](https://testing.googleblog.com/2024/10/?m=0) |
| K6 | **Quality gate fail-closed**: kebijakan approval GitLab memblokir MR saat aturan invalid/tidak dapat dievaluasi (default `fail: closed`); `fail: open` hanya exception terdokumentasi dengan persetujuan risiko. | **[Praktik industri]** + **[Rekomendasi peneliti/tim]** | [GitLab Docs — Merge request approval policies](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/); [GitHub Docs — About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) |
| K7 | **OWASP ASVS 5.0.0 (Mei 2025)** adalah versi stabil terkini, menggantikan 4.0.3 (2021); identifier requirement dapat berubah, jadi selalu sertakan versi. | **[Praktik industri]** | [OWASP/ASVS v5.0.0 README (repositori resmi)](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/README.md); [OWASP ASVS 5.0.0 English PDF](https://github.com/OWASP/ASVS/raw/v5.0.0/5.0/OWASP_Application_Security_Verification_Standard_5.0.0_en.pdf) |
| K8 | **DORA lima metrik** (bukan "four keys"; MTTR diposisikan ulang menjadi *failed deployment recovery time*) dan **100% line coverage menyesatkan**; gate pada kode yang berubah, bukan mandat 100% repositori. | **[Praktik industri]** + **[Rekomendasi peneliti/tim]** | [DORA — Software delivery performance metrics](https://dora.dev/guides/dora-metrics/); [Google Testing Blog — Code Coverage Best Practices](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html) |

Konsekuensi praktis K1–K4: template lama bertajuk "Organizational Test Strategy" dipetakan ke **Organizational Test Practices (6.3)** + **Test Strategy (7.2.7)**, dan "Test Summary Report" dipetakan ke **Test Completion Report (7.4)** agar audit tidak ambigu. **[Rekomendasi peneliti/tim · Inferensi]** — [ISO/IEC/IEEE 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf).

Perubahan teknis edisi 2021 terhadap 2013: konsep *test conditions* **digantikan** oleh *test models*; Annex T menjelaskan alasannya, Annex S memetakan ke IEEE 829:2008 yang sudah *superseded*. **[Standar resmi]** — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, Foreword dan Annex S/T (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf).

29119-3:2021 mendukung dynamic/non-dynamic, functional/non-functional, manual/otomatis, scripted/unscripted, seluruh model lifecycle termasuk agile dan DevOps; dokumentasi boleh berupa records di test tool, spreadsheet, mind map, atau foto whiteboard. **[Standar resmi]** — [IEEE SA — IEEE/ISO/IEC 29119-3-2021](https://standards.ieee.org/ieee/29119-3/7499/); [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, Introduction (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf).

29119-4:2021 (teknik desain) dan 29119-5:2024 (keyword-driven testing) melengkapi 29119-3:2021: yang pertama mengisi 7.2.7, yang kedua menstandarisasi test case modular dan pertukaran artefak antar-tool. **[Rekomendasi peneliti/tim · Inferensi]** — [IEEE SA — seri 29119 aktif](https://standards.ieee.org/ieee/29119-3/7499/).

### 4.3 Konvensi dan tabel penting

#### 4.3.1 Hierarki artefak dokumentasi

| Artefak | Klausul | Fungsi / isi kunci | Status |
| --- | --- | --- | --- |
| Test Policy | 6.2 | Organisasi; *why/what*: objectives, process, struktur, training, etika, standards, measuring value, archiving, improvement; tidak merinci cara pengujian | **[Standar resmi]** |
| Organizational Test Practices | 6.3 | Organisasi; pendekatan yang direkomendasikan, selaras dengan Test Policy, boleh banyak dokumen per konteks | **[Standar resmi]** |
| Test Plan | 7.2 | Proyek/rilis; tujuan, sarana, jadwal; boleh lebih dari satu (master/level/type plan); 7.2.1–7.2.10 | **[Standar resmi]** |
| **Test Strategy** | **7.2.7** | **Bagian dari Test Plan**: levels/types, retesting & regression, teknik desain + completion criteria, test data, environment, tool, deliverable | **[Standar resmi]** |
| Test Model / Test Case Specification | 8.2 / 8.3 | Model memuat objective, priority, strategy extract, test model, traceability; 8.3 memuat coverage items dan test cases | **[Standar resmi]** |
| Test Data & Environment Requirements | 8.5–8.8 | Description, responsibility, period needed, **resetting needs**, **archiving or disposal**; dua readiness report | **[Standar resmi]** |
| Actual Results, Test Result, Execution Log | 8.9 / 8.10 | Pass/fail dari kesesuaian actual vs expected; log eksekusi | **[Standar resmi]** |
| Test Incident Report | 8.11 | Timing, originator, context, description, severity, priority, risk, status; disebut pula bug/defect report | **[Standar resmi]** |
| Test Status Report | 7.3 | Reporting period, progress against plan, blocker, test measures, new/changed risks, planned testing | **[Standar resmi]** |
| **Test Completion Report / Test Summary Report** | **7.4** | Summary, deviations, completion evaluation, blocker, measures, **residual risks**, deliverables, reusable assets, lessons learned | **[Standar resmi]** |
| Test Traceability Matrix | definisi 3.26 | Dokumen/spreadsheet/tool penghubung requirement dengan test-nya; format dan detail boleh berbeda | **[Standar resmi]** |

Sumber tabel: **[Standar resmi]** [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); **[Rekomendasi peneliti/tim]** hierarki aman tim (Test Policy → Organizational Test Practices → Test Plan → Test Model/Case/Procedure → Status/Completion Report) diturunkan dari [ISO/IEC/IEEE 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf) dan [ISTQB CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2).

#### 4.3.2 Komposisi suite: model dan konvensi

| Model | Menjawab | Isi / trade-off | Penanda |
| --- | --- | --- | --- |
| Test pyramid | Seberapa banyak tiap lapisan | Heuristik: lebih banyak unit daripada integration, lebih banyak integration daripada E2E; jumlah/penamaan lapisan boleh berbeda (Cohn 2009: unit/service/UI; populer: unit/component integration/E2E) | **[Sertifikasi/resmi badan]** [ISTQB TBOK — CTFL Syllabus v4.0.1](https://tbok.istqb.org/view-pdf/id/2) |
| SMURF (Google, 2024-10-15) | Kriteria trade-off | Speed, Maintainability, Utilization, Reliability, Fidelity; unit unggul speed/utilization, integration dan E2E unggul fidelity; reliable test hanya gagal saat masalah nyata | **[Praktik industri]** [Google Testing Blog — SMURF: Beyond the Test Pyramid](https://testing.googleblog.com/2024/10/?m=0) |
| Test Sizes (Google, 2010) | Kosakata ukuran | Small ≈ unit, Medium ≈ integration (dua tier berkomunikasi), Large ≈ end-to-end/system | **[Praktik industri]** [Google Testing Blog — Test Sizes](https://testing.googleblog.com/2010/12/test-sizes.html) |
| Testing Trophy | Seberapa banyak, khusus UI | Integration sebagai lapisan terbesar; opini satu praktisi (2021-06-02), bukan standar dan tanpa nomor rilis resmi | **[Praktik industri]** [Kent C. Dodds — The Testing Trophy and Testing Classifications](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications) |
| Shift-left | Kapan | Review spesifikasi, test sebelum kode, CI/CD feedback cepat, static analysis, NFR sejak component level; tidak meniadakan pengujian akhir | **[Sertifikasi/resmi badan]** [ISTQB TBOK — CTFL Syllabus v4.0.1](https://tbok.istqb.org/view-pdf/id/2) |
| Testing Quadrants | Penempatan jenis | Q1 component/component integration (CI); Q2 functional, contoh, user story, API; Q3 exploratory, usability, UAT; Q4 smoke dan non-functional | **[Sertifikasi/resmi badan]** [ISTQB TBOK — CTFL Syllabus v4.0.1](https://tbok.istqb.org/view-pdf/id/2) |
| Consumer-driven contract | Kompatibilitas pesan | Consumer test memakai mock provider menghasilkan pact file; provider verification membandingkan respons aktual dengan minimal expected response; fokus pada request/response dan **data-independent** | **[Praktik industri]** [Pact Docs — How Pact works](https://docs.pact.io/getting_started/how_pact_works) |

**[Rekomendasi peneliti/tim · Inferensi]** Komposisi awal untuk diskusi tim (bukan target audit): service/backend murni unit ≈ 60–70%, integration ≈ 20–30%, contract ≈ 5–10% per pasangan consumer–provider, E2E ≈ 5% untuk critical journeys; UI-heavy mengikuti trophy; microservices dengan deploy independen mewajibkan contract test per pasangan dan `can-i-deploy` sebagai gate; safety-critical/regulasi menaikkan integration/E2E serta teknik coverage formal. Semua angka ditetapkan ulang lewat analisis risiko produk. — [ISTQB CTFL v4.0 §5.2.3](https://tbok.istqb.org/view-pdf/id/2); [Google SMURF](https://testing.googleblog.com/2024/10/?m=0); [Pact Docs](https://docs.pact.io/pact_nirvana/step_6).

**[Rekomendasi peneliti/tim · Inferensi]** Pilih pyramid bila biaya CI, kecepatan feedback, dan maintainability menjadi kendala; pilih trophy bila defect terkonsentrasi di batas komponen/UI; shift-left tetap dipakai di semua kasus. Contract test bukan pengganti integration test karena Pact memverifikasi bentuk pesan, bukan perilaku end-to-end. — [Google SMURF](https://testing.googleblog.com/2024/10/?m=0); [Kent C. Dodds](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications); [Pact Docs — How Pact works](https://docs.pact.io/getting_started/how_pact_works).

#### 4.3.3 Konvensi field minimum dan keterlacakan

| Konteks | Field / konvensi | Penanda |
| --- | --- | --- |
| Test case (spesifikasi) | `{{test_case_id}}`, `{{objective}}`, `{{requirement_id}}`, `{{risk_id}}`, `{{priority}}`, `{{preconditions}}`, `{{test_data_id}}`, `{{steps}}`, `{{expected_results}}`, `{{postconditions_cleanup}}` | **[Rekomendasi peneliti/tim]** |
| Hasil eksekusi | `{{actual_results}}`, `{{result_pass_fail}}`, `{{build_sha}}`, `{{environment_id}}`, `{{evidence_links}}`, `{{incident_id}}` | **[Rekomendasi peneliti/tim]** |
| Incident / defect report | unique identifier, title ringkas, tanggal/organisasi/penulis+peran, test object & environment, konteks, repro steps, expected vs actual, **severity**, **priority to fix**, status, referensi, bukti | **[Sertifikasi/resmi badan]** |
| Risk register | `{{risk_id}}`, kategori project/product, `{{likelihood}}`, `{{impact}}`, `{{risk_level}}`, `{{mitigation_test_type}}`, `{{linked_test_case_ids}}`, `{{owner}}`, `{{residual_risk_after_testing}}`, `{{acceptance_decision}}` | **[Rekomendasi peneliti/tim]** |
| Test data | Sintetik/ter-masking, `{{test_data_id}}` unik, fixture dengan teardown, resetting needs, archiving/disposal, readiness report, **tanpa data acak di kontrak Pact** | **[Rekomendasi peneliti/tim]** |
| Severity vs priority | Severity = dampak bagi pemangku kepentingan/requirement; priority = kapan diperbaiki; keduanya boleh berbeda dan skalanya ditetapkan lokal | **[Rekomendasi peneliti/tim]** |
| Configuration management | Semua configuration item (plan, strategy, cases, scripts, results, logs, reports) unik, version-controlled, saling direlasikan; baseline hanya berubah lewat change control | **[Sertifikasi/resmi badan]** |

Rantai keterlacakan yang berguna bukan sekadar tabel requirement↔test case: `{{requirement_id}} → {{risk_id}} → {{test_model_id}} → {{test_case_id}} → {{test_result}} → {{incident_id}} → {{residual_risk}}`. **[Rekomendasi peneliti/tim · Inferensi]** — [ISTQB CTFL v4.0 §1.4.4](https://tbok.istqb.org/view-pdf/id/2); [ISO 29119-3:2021 Klausul 7.4.7](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf).

Bukti (log, screenshot, trace, database dump) diunggah sebagai artifact CI tertaut ke `{{build_sha}}`, bukan ditempel sebagai teks bebas, agar konfigurasi dapat direproduksi. **[Rekomendasi peneliti/tim · Inferensi]** — [GitHub Docs — workflow artifacts](https://docs.github.com/zh/actions/tutorials/store-and-share-data); [GitLab Docs — Unit test reports](https://docs.gitlab.com/ci/testing/unit_test_reports/); [ISTQB §5.4](https://tbok.istqb.org/view-pdf/id/2).

Sumber konvensi: **[Standar resmi]** [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); **[Sertifikasi/resmi badan]** [ISTQB TBOK — CTFL Syllabus v4.0.1, halaman 55–56](https://tbok.istqb.org/view-pdf/id/2?page=56&search=defect%20report&highlight=5.5).

#### 4.3.4 Exit criteria dan quality gate

| Gate / jenis | Mekanisme yang dapat diotomasi | Contoh exit criteria | Penanda rujukan |
| --- | --- | --- | --- |
| Unit / component | JUnit `@Tag`/`@DisplayName` untuk grouping suite | Seluruh test pada diff pass; coverage kode baru ≥ `{{new_code_coverage_threshold}}`; tidak ada assertion dikosongkan | **[Praktik industri]** [JUnit User Guide 6.1.3 — Overview](https://docs.junit.org/6.1.3/overview.html) |
| API / contract | `can-i-merge` untuk PR; `can-i-deploy --to-environment {{env}}` menjelang deploy | Hasil provider verification terpublikasi ke broker; pengecekan ulang bila jeda verifikasi–deploy lama; pact bebas data acak | **[Praktik industri]** [Pact Docs — Pact Nirvana Step 6: can-i-deploy](https://docs.pact.io/pact_nirvana/step_6); [Pact Docs — Provider verification badges](https://docs.pact.io/pact_broker/advanced_topics/provider_verification_badges) |
| E2E / UI | Auto-waiting, auto-retrying assertions, Trace Viewer, kategori `passed`/`flaky`/`failed` | `{{critical_journeys}}` pass pada run pertama; `flaky` = `{{flake_budget}}`; trace tersimpan tiap failure | **[Praktik industri]** [Playwright Docs — Actionability](https://playwright.dev/docs/actionability); [Playwright Docs — Trace viewer](https://playwright.dev/docs/trace-viewer-intro); [Playwright Docs — Retries](https://playwright.dev/docs/test-retries) |
| Performance / load | k6 **thresholds** sebagai pass/fail; threshold gagal ⇒ exit code non-zero | `http_req_failed: ['rate<0.01']`, `http_req_duration: ['p(95)<200']`; `checks` **tidak** memengaruhi exit status sehingga wajib dipasangkan threshold | **[Praktik industri]** [Grafana k6 Docs — Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/) |
| Security | Policy `scan_finding`, `severity_levels`, `vulnerabilities_allowed`, `vulnerability_states`; artifact report di source **dan** target branch | Tidak ada temuan baru critical/high dengan `fix_available: true` pada `{{asvs_level}}`; policy terverifikasi, bukan `fail: open` tanpa persetujuan risiko | **[Praktik industri]** [GitLab Docs — Merge request approval policies](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/) |
| Branch protection | Required status checks harus successful/skipped/neutral; mode strict; merge queue menjalankan ulang checks; nama job unik lintas workflow | Semua required checks hijau pada artefak `{{build_sha}}`; "require deployments to succeed before merging" bila relevan | **[Praktik industri]** [GitHub Docs — About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) |
| Accessibility | WCAG 2.2 success criteria teruji, level A/AA/AAA | Seluruh success criteria `{{wcag_target_level}}` untuk `{{scope_pages}}` terpenuhi; automated = 0 **dan** evaluasi manusia terdokumentasi | **[Standar resmi]** [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/) |
| Smoke / regression / UAT | Smoke sebagai entry criteria (Q4); regression 100% dieksekusi; UAT Q3 | Smoke pass sebelum tahap berikutnya; tidak ada defect baru di atas `{{severity_threshold}}`; sign-off `{{business_owner}}` + residual risk diterima | **[Sertifikasi/resmi badan]** [ISTQB TBOK — CTFL Syllabus v4.0.1](https://tbok.istqb.org/view-pdf/id/2) |
| Chaos / resilience | Steady state, metrik steady state, observability, alarm/log/MTTR, rencana & hasil eksperimen | Metrik steady state dalam `{{slo}}`; MTTR terukur; eksperimen dapat di-abort; dampak terbatas `{{blast_radius}}` | **[Praktik industri]** [AWS — Chaos Engineering on AWS (PDF)](https://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/chaos-engineering-on-aws.pdf) |

**[Rekomendasi peneliti/tim · Inferensi]** Urutan gate PR: static analysis/unit → integration + contract (`can-i-merge`) → E2E smoke → security/accessibility scan → required status checks → review/approval; sebelum deploy: `can-i-deploy` + k6 threshold + post-deploy synthetic/observability check. — [GitHub Docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), [GitLab Docs](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/), [Pact Docs](https://docs.pact.io/pact_nirvana/step_6), [k6 Docs](https://grafana.com/docs/k6/latest/using-k6/thresholds/).

**[Rekomendasi peneliti/tim · Inferensi]** Terapkan **fail-closed** pada seluruh gate; `fallback_behavior: fail: open` tersedia di GitLab tetapi tidak ada panduan resmi yang menetapkan kapan boleh dipakai untuk sistem regulasi, sehingga harus menjadi exception dengan persetujuan risiko. — [GitLab Docs — Merge request approval policies](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/).

**[Rekomendasi peneliti/tim · Inferensi]** Coverage target yang tidak menyesatkan: gate pada **kode yang berubah** (diff/per-commit) dengan `{{new_code_coverage_threshold}}`, tambahkan requirement coverage dan risk coverage, serta mutation testing pada modul kritikal; branch coverage menyubsume statement coverage (100% branch ⇒ 100% statement, tidak berlaku sebaliknya). — [Google Testing Blog 2020](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html); [ISTQB §4.3.1–4.3.2](https://tbok.istqb.org/view-pdf/id/2).

#### 4.3.5 Metrik: DORA lima dan sinyal bermakna

| Kelompok | Metrik DORA (guide diperbarui 2026-01-05) | Catatan |
| --- | --- | --- |
| Throughput | *change lead time*, *deployment frequency*, *failed deployment recovery time* | Lead time for changes = code committed → code successfully running in production ([DORA — Quick Check 2019 results](https://dora.dev/quickcheck/2019/results/)) |
| Instability | *change fail rate*, *deployment rework rate* | Change fail rate = rasio deployment yang memerlukan intervensi segera (rollback/hotfix); rework rate = rasio deployment tidak terencana akibat insiden produksi |
| Prinsip pemakaian | Speed dan stability bukan trade-off; ukur per aplikasi/service; leading indicator bagi organisasi, lagging indicator bagi praktik delivery | Terminologi "four keys" adalah sebutan lama; MTTR kini *failed deployment recovery time* |

Sumber tabel: **[Praktik industri · Praktik industri / opini]** [DORA — Software delivery performance metrics](https://dora.dev/guides/dora-metrics/); [DORA — A history of DORA's software delivery metrics](https://dora.dev/insights/dora-metrics-history/); [DORA — Quick Check 2019 results](https://dora.dev/quickcheck/2019/results/).

| Bermakna (pasangkan minimal satu per kelompok) | Menyesatkan bila dijadikan target |
| --- | --- |
| Outcome produksi: change fail rate, deployment rework rate, failed deployment recovery time | Pass rate 100% tanpa denominator test yang diskip |
| Efektivitas pengujian: DDP / defect escape rate, defect density area kritikal, residual risk level | Jumlah test case sebagai proxy kualitas; jumlah bug sebagai KPI individu |
| Kecepatan feedback: change lead time, durasi pipeline ke keputusan merge | **100% line coverage sebagai tujuan**; velocity eksekusi tanpa defect escape rate |
| Kesehatan suite: flaky rate, duration p95, test yang diskip | Perbandingan DORA lintas aplikasi sangat berbeda; satu metrik tunggal sebagai target tahunan |
| Cakupan risiko: requirements/acceptance-criteria coverage untuk `{{critical_requirements}}` | Metrik sebagai goal (Goodhart's law), kompetisi antar-tim, ownership tersilo |

**[Rekomendasi peneliti/tim · Inferensi]** — [DORA Guides](https://dora.dev/guides/dora-metrics/); [Google Testing Blog — Code Coverage Best Practices](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html); [ISTQB §5.3.1](https://tbok.istqb.org/view-pdf/id/2). *Defect escape rate* bukan istilah normatif pada primer yang diverifikasi; definisi operasional dan denominator wajib ditulis di Test Plan. **[Rekomendasi peneliti/tim · Inferensi]** — [ISTQB — CT-ATLaS BoK v2.0](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CT-ATLaS_Body-of-Knowledge_v2.0.pdf).

ISTQB CTFL v4.0 §5.3.1 mendaftar metrik project/test progress, product quality, defect (jumlah, prioritas, density, **defect detection percentage**), risk, coverage, dan cost; 29119-3:2021 menempatkan *test measures* dan *residual risks* di 7.4.6–7.4.7, serta *measuring the value of testing* di Test Policy 6.2.9. **[Sertifikasi/resmi badan]** — [ISTQB TBOK — CTFL Syllabus v4.0.1](https://tbok.istqb.org/view-pdf/id/2); [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf).

### 4.4 Checklist review

Jalankan dua kali: saat **review Test Plan** sebelum implementasi test, dan saat **review Test Completion Report** sebelum keputusan rilis, dengan bukti `{{CI_RUN_URL}}`, bukan sekadar centang manual. **[Rekomendasi peneliti/tim · Inferensi]** — [ISTQB §5.3.1–5.3.3](https://tbok.istqb.org/view-pdf/id/2); [GitHub Docs](https://docs.github.com/zh/actions/tutorials/store-and-share-data).

**A. Konformasi dan Test Plan** — **[Standar resmi]** [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, Klausul 5.2 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, Klausul 4.1 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, daftar isi (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)

- [ ] Klaim *full* atau *tailored conformance* tercatat, lengkap dengan justifikasi tailoring dan subset dokumentasi yang diklaim.
- [ ] Common information tersedia: unique ID, issuing organization, approval authority, change history, status, introduction, scope, references, glossary.
- [ ] Test Plan memuat context, assumptions/constraints, stakeholders, communication, risk register, test strategy, activities/estimates, staffing, schedule.
- [ ] Test Strategy 7.2.7 mencantumkan levels/types, retesting & regression, teknik desain + completion criteria, test data, environment, tool, dan deliverable.
- [ ] Risiko ditautkan ke scope, urutan eksekusi, estimasi, dan residual risk; prioritas eksekusi mempertimbangkan dependensi serta ketersediaan resource.
- [ ] Readiness report test data & environment sebelum eksekusi, termasuk *resetting needs* dan *archiving/disposal*.
- [ ] Entry/exit criteria per test level, DoD/DoR, dan persetujuan risiko tertulis bila exit karena waktu/budget. **[Sertifikasi/resmi badan]** [ISTQB TBOK — CTFL Syllabus v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- [ ] Target aksesibilitas mengunci WCAG 2.2 dan level konformasi, dengan evaluasi manusia selain automated scan. **[Standar resmi]** [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/)

**B. Test case, incident, dan keterlacakan** — **[Sertifikasi/resmi badan]** [ISTQB TBOK — CTFL Syllabus v4.0.1, halaman 55–56](https://tbok.istqb.org/view-pdf/id/2?page=56&search=defect%20report&highlight=5.5)

- [ ] Setiap test case punya prekondisi, data uji, langkah, expected result, dan cleanup.
- [ ] Setiap eksekusi punya actual result, pass/fail, log, `{{build_sha}}`, dan `{{environment_id}}`.
- [ ] Setiap incident punya severity **dan** priority yang terpisah, repro steps, konteks lingkungan, serta bukti.
- [ ] Traceability `requirement → risk → test case → result → incident → residual risk` lengkap dan version-controlled.
- [ ] Bukti diunggah sebagai artifact CI, bukan teks bebas; baseline perubahan melalui change control.
- [ ] Completion Report memuat residual risks, deviations, test measures, reusable assets, lessons learned—bukan hanya ringkasan pass/fail. **[Standar resmi]** [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, daftar isi Klausul 7.3–7.4 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)

**C. Quality gate CI/CD** — **[Praktik industri · Dokumentasi resmi vendor/proyek]**

- [ ] Required status checks unik lintas workflow, berstatus successful/skipped/neutral; strict/merge queue sesuai risiko integrasi. — [GitHub Docs — About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [ ] Artefak scanner tersedia di source **dan** target branch; scanner tidak dihapus dari MR; fallback tidak sengaja `fail: open`. — [GitLab Docs — Merge request approval policies](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/)
- [ ] `can-i-deploy` dijalankan menjelang deploy (bukan hanya saat verifikasi awal) dan pact bebas data acak. — [Pact Docs — Step 6](https://docs.pact.io/pact_nirvana/step_6)
- [ ] Performance gate memakai **thresholds**, bukan hanya `checks`, agar exit code benar-benar memblokir pipeline. — [Grafana k6 Docs — Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/)
- [ ] Metrik `flaky` dilaporkan terpisah dari `passed` dan trace tersimpan untuk first retry. — [Playwright Docs — Retries](https://playwright.dev/docs/test-retries); [Playwright Docs — Trace viewer](https://playwright.dev/docs/trace-viewer-intro)
- [ ] Requirement keamanan dirujuk dengan format berversi `v5.0.0-...`; WSTG mengunci Latest atau Stable v4.2. — [OWASP ASVS v5.0.0](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/README.md); [OWASP WSTG](https://wstg.owasp.org/latest/1-About/)
- [ ] Metrik tidak dijadikan target tunggal dan diukur per aplikasi/service. **[Praktik industri]** — [DORA — Software delivery performance metrics](https://dora.dev/guides/dora-metrics/)
- [ ] Gate bersifat fail-closed; exception `fail: open` memiliki persetujuan risiko terdokumentasi. **[Rekomendasi peneliti/tim]** — [GitLab Docs — Merge request approval policies](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/)

### 4.5 Anti-pattern

| Anti-pattern | Mengapa cacat | Koreksi | Status bukti |
| --- | --- | --- | --- |
| Tes selalu hijau / assertion kosong | Test dieksekusi belum tentu menguji dengan benar | Mutation testing untuk memeriksa assertion menangkap failure | **[Praktik industri]** [Google Testing Blog — Code Coverage Best Practices](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html) |
| Mengejar 100% line coverage | *False sense of security*, technical debt test bernilai rendah; 100% statement tidak menjamin decision logic | Gate pada diff/per-commit + branch, requirement, risk coverage | **[Praktik industri]** + **[Standar resmi]** [Google Testing Blog 2020](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html); [ISTQB CTFL v4.0 §4.3.1](https://tbok.istqb.org/view-pdf/id/2) |
| E2E berlebih | Menaikkan fidelity tetapi mengorbankan Speed, Maintainability, Utilization, Reliability | Pakai SMURF untuk menimbang ulang komposisi | **[Praktik industri]** [Google Testing Blog — SMURF](https://testing.googleblog.com/2024/10/?m=0) |
| QA sebagai gerbang terakhir | Bertentangan dengan whole-team approach dan shift-left | Tester terlibat sejak acceptance criteria dan penyusunan test strategy | **[Sertifikasi/resmi badan]** [ISTQB CTFL v4.0 §1.5.2 & §2.1.5](https://tbok.istqb.org/view-pdf/id/2) |
| Shift-left disalahartikan sebagai "pengujian akhir tidak perlu" | ISTQB menyatakan eksplisit sebaliknya | Pertahankan pengujian akhir di samping pengujian awal | **[Sertifikasi/resmi badan]** [ISTQB CTFL v4.0 §2.1.5](https://tbok.istqb.org/view-pdf/id/2) |
| Flaky test hanya di-retry | `flaky` berbeda dari `passed`; retry membuang waktu dan biaya resource | Isolasi state, auto-waiting, karantina + tiket + SLA; `flake_budget = 0` | **[Praktik industri]** [Playwright Docs — Retries](https://playwright.dev/docs/test-retries); [Google Testing Blog — SMURF](https://testing.googleblog.com/2024/10/?m=0) |
| Quality gate yang bisa dilewati | Nama job kembar membuat status check ambigu; artifact hilang membuat kebijakan tidak dapat dievaluasi | Nama check unik + required checks; default `fail: closed` | **[Praktik industri]** [GitHub Docs — About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches); [GitLab Docs — Merge request approval policies](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/) |
| Performance test tanpa threshold | `checks` pada k6 tidak mengubah exit status sehingga pipeline tetap hijau walau SLO dilanggar | Pakai thresholds dengan exit code non-zero | **[Praktik industri]** [Grafana k6 Docs — Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/) |
| Contract test dianggap functional test | Kontrak fokus pada pesan dan data-independent; pemakaian untuk functional behaviour provider menghasilkan test rapuh | Pisahkan verifikasi kontrak dari functional test lain | **[Praktik industri]** [Pact Docs — How Pact works](https://docs.pact.io/getting_started/how_pact_works) |
| Data acak dalam pact / test data tanpa reset | Broker menganggap pact revisi baru dan memicu webhook berulang | Data-independent; catat resetting needs serta archiving/disposal | **[Praktik industri]** + **[Standar resmi]** [Pact Docs — Step 6](https://docs.pact.io/pact_nirvana/step_6); [ISO/IEC/IEEE 29119-3:2021 Klausul 8.5](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf) |
| Laporan tanpa residual risk | Keputusan rilis tidak dapat diaudit | Cantumkan unmitigated risks / defects not fixed di 7.4 | **[Standar resmi]** [ISO/IEC/IEEE 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [ISTQB CTFL v4.0 §5.3.2](https://tbok.istqb.org/view-pdf/id/2) |
| Tidak ada traceability | Melemahkan evaluasi coverage, analisis dampak, audit, dan pemahaman laporan | Rantai requirement → risk → result → incident → residual risk | **[Sertifikasi/resmi badan]** [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2) |
| Tidak ada pengujian/observability di produksi | Kegagalan yang lolos pre-release tidak terdeteksi | Pantau change fail rate, recovery time, steady state, alarm, log, MTTR | **[Praktik industri]** [DORA — Software delivery performance metrics](https://dora.dev/guides/dora-metrics/); [AWS — Chaos Engineering on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/chaos-engineering-on-aws.pdf) |
| Metrik dijadikan target tunggal / kompetisi antar-tim | Goodhart's law, "one metric to rule them all", perbandingan disparat, ownership tersilo | Set metrik berpasangan, per aplikasi/service, fokus pada perbaikan | **[Praktik industri]** [DORA — Software delivery performance metrics](https://dora.dev/guides/dora-metrics/) |
| Aksesibilitas hanya mengandalkan automated scan | WCAG 2.2 dirancang untuk automated **dan** human evaluation; konformasi AAA pun tidak menjamin semua pengguna | Kombinasikan keduanya dan dokumentasikan evaluasi manusia | **[Standar resmi]** [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/) |
| Mengunci versi standar keamanan lama tanpa menyebut versi | Identifier ASVS berubah antarversi; WSTG Latest dan Stable v4.2 berbeda isi | Format `v<version>-<requirement>`; kunci salah satu jalur WSTG | **[Praktik industri]** [OWASP ASVS v5.0.0](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/README.md); [OWASP WSTG](https://wstg.owasp.org/latest/1-About/) |
| Severity disamakan dengan priority | Keduanya assessment berbeda (dampak vs jadwal) | Definisikan skala lokal dan simpan sebagai field terpisah | **[Sertifikasi/resmi badan]** [ISTQB CTFL v4.0 §5.5](https://tbok.istqb.org/view-pdf/id/2?page=56&search=defect%20report&highlight=5.5); [ISO/IEC/IEEE 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf) |

**[Rekomendasi peneliti/tim · Inferensi]** Turunan langsung lain yang perlu dicegah: pass rate 100% dengan test yang di-skip; jumlah test case dijadikan produktivitas; mengklaim "sesuai ISO 29119" tanpa menyatakan full/tailored conformance; mengklaim "sesuai ISO 29119-14" padahal masih DIS; menyatukan Test Status Report dengan Test Completion Report sehingga periode pelaporan dan keputusan rilis tercampur. — [ISO/IEC/IEEE 29119-3:2021 Klausul 4.1 & 7.3–7.4](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [ISO — DIS 29119-14](https://www.iso.org/cms/live/live/es/sites/isoorg/contents/data/standard/08/88/88837.html?browse=tc); [DORA pitfalls](https://dora.dev/guides/dora-metrics/).

Akar masalahnya seragam: mengoptimalkan sinyal yang mudah diukur (jumlah test, pass rate, coverage, kecepatan merge) sampai sinyal itu berhenti berkorelasi dengan risiko produksi. **[Praktik industri]** — [DORA — Common pitfalls](https://dora.dev/guides/dora-metrics/); [Google Testing Blog — Code Coverage Best Practices](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html).

### 4.6 Konflik sumber

| Konflik | Posisi yang dipakai | Catatan |
| --- | --- | --- |
| Penamaan Part 1 edisi 2 | **ISO/IEC/IEEE 29119-1:2022** | Katalog/OBP ISO memakai 2022, halaman IEEE SA menamai standar aktif yang sama **IEEE/ISO/IEC 29119-1-2021**; keduanya edisi 2 pengganti 2013. Cantumkan tahun sesuai badan penerbit yang dirujuk dan jangan mencampur tanpa catatan. **[Standar resmi]** [ISO Online Browsing Platform — 29119-1:2022](https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso-iec-ieee%3A29119%3A-1%3Aed-2%3Av1%3Aen); [IEEE SA — seri 29119 aktif](https://standards.ieee.org/ieee/29119-3/7499/) |
| "Organizational Test Strategy" | Bukan entitas 29119-3:2021 | Istilah masih muncul di literatur edisi 2013; petakan ke Organizational Test Practices (6.3) + Test Strategy (7.2.7). Perlu verifikasi ulang bila organisasi memiliki salinan berlisensi lengkap. **[Rekomendasi peneliti/tim]** [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [ISO — 29119-3:2013](https://www.iso.org/standard/56737.html?browse=ics) |
| ASVS 4.0.3 vs 5.0.0 | **5.0.0 (Mei 2025)** | 4.0.3 (2021) adalah pendahulu; tim yang terikat kontrak pada 4.0.3 wajib mencantumkan versi eksplisit karena identifier berubah. **[Praktik industri]** [OWASP/ASVS v5.0.0 README](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/README.md) |
| WSTG Latest vs Stable | Kunci salah satu URL/versi | `Latest` (copyright 2026, inkremental, tanpa nomor versi semantik yang ditemukan) vs `Stable = v4.2` (2020-12-03); mengunci keduanya penting agar audit reproducible. **[Praktik industri]** [OWASP WSTG — Latest / About](https://wstg.owasp.org/latest/1-About/); [OWASP — WSTG release versions](https://owasp.org/projects/web-security-testing-guide?tab=release-versions) |
| "Four keys" vs lima metrik DORA | **Lima metrik** | Guide 2026 menambah *deployment rework rate* dan memosisikan ulang MTTR menjadi *failed deployment recovery time*. **[Praktik industri]** [DORA — Software delivery performance metrics](https://dora.dev/guides/dora-metrics/) |
| Pyramid vs Testing Trophy | Keduanya heuristik, bukan norma | Pyramid adalah *canonical heuristic* Google/ISTQB; trophy adalah opini satu praktisi untuk UI-heavy. Tidak ada rasio yang distandardisasi. **[Praktik industri]** [Google Testing Blog — SMURF](https://testing.googleblog.com/2024/10/?m=0); [Kent C. Dodds — Testing Trophy](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications) |
| 29119-14 sebagai "standar final" | Masih **DIS/CD per 2026** | IEEE mencatat proyek P29119-14 belum menjadi standar aktif; exit criteria migrasi data tidak boleh diklaim "sesuai standar ISO final". **[Standar resmi]** [ISO — ISO/IEC/IEEE DIS 29119-14](https://www.iso.org/cms/live/live/es/sites/isoorg/contents/data/standard/08/88/88837.html?browse=tc) |
| `fail: open` vs `fail: closed` | **Fail-closed** | `fallback_behavior: fail: open` tersedia, tetapi tidak ditemukan panduan resmi kapan diperbolehkan untuk sistem regulasi; jadikan exception dengan persetujuan risiko. **[Praktik industri]** [GitLab Docs — Merge request approval policies](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/) |
| Whole-team approach vs independensi | Kontekstual | ISTQB menyebut safety-critical sebagai pengecualian, tanpa ambang kuantitatif kapan independensi wajib; keputusan bersifat regulatori. **[Sertifikasi/resmi badan]** [ISTQB CTFL v4.0.1 §1.5.2](https://tbok.istqb.org/view-pdf/id/2) |

### 4.7 Keterbatasan (Gaps)

- Teks lengkap 29119-3:2021, 29119-1:2022, 29119-2:2021, dan 29119-4:2021 berbayar; yang diverifikasi langsung adalah pratinjau resmi 15 halaman (daftar isi, definisi Klausul 3, Klausul 1–4, Foreword/Introduction) dipadukan katalog resmi. **[Standar resmi]** [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [IEEE SA — seri 29119 aktif](https://standards.ieee.org/ieee/29119-3/7499/); [ISO — 29119-2:2021](https://www.iso.org/standard/79428.html)
- **Annex A (normatif)** yang memetakan `shall/should/may` per information item tidak terbuka publik; daftar "section terstandarisasi" tidak boleh diklaim semuanya `shall`. **[Standar resmi]** [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, Klausul 4.1 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- Nomor halaman ISO untuk URL katalog `https://www.iso.org/standard/79429.html` tidak berhasil diambil (timeout); katalog IEEE/IEC dan pratinjau iTeh dipakai sebagai pengganti primer setara.
- Sub-klausul rinci 8.3.3.x (nomor field individual test case) tidak tersedia pada pratinjau publik; penomoran field konvensi di atas tidak diklaim persis sama dengan standar berlisensi. **[Standar resmi]** [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- Tidak ada skala severity/priority baku (S1–S4, P0–P3) di ISO 29119-3 maupun ISTQB CTFL; skala ditetapkan lokal di Test Policy/Organizational Test Practices. **[Sertifikasi/resmi badan]** [ISO/IEC/IEEE 29119-3:2021 Klausul 6.2/8.11](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [ISTQB CTFL v4.0.1 §5.5](https://tbok.istqb.org/view-pdf/id/2?page=56&search=defect%20report&highlight=5.5)
- Tidak ada rasio unit:integration:contract:E2E yang distandardisasi; seluruh angka komposisi adalah heuristic peneliti dan harus dicatat sebagai keputusan tim. **[Rekomendasi peneliti/tim]** [ISTQB CTFL v4.0.1 §5.1.6](https://tbok.istqb.org/view-pdf/id/2); [ISO/IEC/IEEE 29119-3:2021 Klausul 7.2.7](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- Testing Trophy adalah opini satu praktisi tanpa versi/nomor rilis resmi; dipakai hanya sebagai pelengkap. **[Praktik industri]** [Kent C. Dodds — The Testing Trophy and Testing Classifications](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications)
- DORA/ISTQB tidak memberi ambang numerik untuk pass rate, defect density, flake budget, maupun ambang defect density universal; semua ambang adalah placeholder keputusan lokal. **[Praktik industri]** [DORA — Software delivery performance metrics](https://dora.dev/guides/dora-metrics/); [ISTQB CTFL v4.0.1 §5.3.1](https://tbok.istqb.org/view-pdf/id/2)
- Benchmark angka "elite/high/medium/low" DORA tidak dipakai karena guide terbaru memperingatkan agar metrik tidak dijadikan target atau dibandingkan lintas konteks. **[Praktik industri]** [DORA — Software delivery performance metrics](https://dora.dev/guides/dora-metrics/); [DORA Quick Check 2019](https://dora.dev/quickcheck/2019/results/)
- Angka prevalensi flaky test yang beredar hanya ditemukan pada slide kursus pihak ketiga, bukan primer Google; angka tersebut sengaja tidak dipakai. **[Praktik industri]** [Google Testing Blog — SMURF](https://testing.googleblog.com/2024/10/?m=0)
- Tidak ada definisi kanonik **defect escape rate** pada primer ISTQB/ISO yang terbuka publik; formula adalah inferensi dari DDP dan wajib ditetapkan lokal. **[Rekomendasi peneliti/tim]** [ISTQB — CT-ATLaS BoK v2.0](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CT-ATLaS_Body-of-Knowledge_v2.0.pdf)
- Tidak ada tool resmi tunggal untuk compatibility, data migration, dan UAT; rujukannya berupa standar/syllabus, bukan rekomendasi vendor. **[Sertifikasi/resmi badan]** [ISTQB — CT-MAT Syllabus v1.0](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CT-MAT_Syllabus_v1.0_2019.pdf)
- Template utama dan konfigurasi `fallback_behavior.fail: closed` / `vulnerabilities_allowed` memerlukan pengecekan tier GitLab Ultimate serta salinan berlisensi untuk klaim *full conformance*. **[Praktik industri]** [ISO/IEC/IEEE 29119-3:2021 Klausul 4.1](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [GitLab Docs — Merge request approval policies](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/)
- Checklist tidak mencakup review BRD/FSD, desain arsitektur/UI, struktur folder/repo, API versioning, maupun laporan harian; keterlacakan hanya memakai `{{requirement_id}}` sebagai kunci tautan. **[Rekomendasi peneliti/tim]** [ISO/IEC/IEEE 29119-3:2021 Klausul 4.1 tentang tailoring](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- Anti-pattern tidak dikuantifikasi dampak finansialnya (tidak ada angka biaya lintas organisasi 2024–2026); beberapa di antaranya hanya didukung blog resmi Google sehingga tidak boleh dipresentasikan sebagai pelanggaran standar. **[Praktik industri]** [DORA — Accelerate State of DevOps Report 2024](https://dora.dev/research/2024/dora-report/); [Google Testing Blog — Code Coverage Best Practices](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html)

### Sumber bagian ini

**[Standar resmi] — ISO/IEC/IEEE, IEEE SA, ISO, W3C**

- [IEEE SA — IEEE/ISO/IEC 29119-3-2021](https://standards.ieee.org/ieee/29119-3/7499/) (dirujuk pula sebagai [IEEE SA — seri 29119 aktif](https://standards.ieee.org/ieee/29119-3/7499/) dan [IEEE SA — P29119-14](https://standards.ieee.org/ieee/29119-3/7499/))
- [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- [ISO Online Browsing Platform — ISO/IEC/IEEE 29119-1:2022](https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso-iec-ieee%3A29119%3A-1%3Aed-2%3Av1%3Aen)
- [ISO — ISO/IEC/IEEE 29119-1:2013 (Withdrawn)](https://www.iso.org/standard/45142.html)
- [ISO — ISO/IEC/IEEE 29119-2:2021](https://www.iso.org/standard/79428.html)
- [ISO — 29119-3:2013](https://www.iso.org/standard/56737.html?browse=ics)
- [ISO — ISO/IEC/IEEE DIS 29119-14](https://www.iso.org/cms/live/live/es/sites/isoorg/contents/data/standard/08/88/88837.html?browse=tc)
- [W3C — WCAG 2.2 Recommendation](https://www.w3.org/TR/WCAG22/)
- [W3C — REC-WCAG22-20241212](https://www.w3.org/TR/2024/REC-WCAG22-20241212/)
- [W3C WAI — What's New in WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/)

**[Sertifikasi/resmi badan] — ISTQB**

- [ISTQB TBOK — CTFL Syllabus v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- [ISTQB TBOK — CTFL Syllabus v4.0.1, halaman 55–56](https://tbok.istqb.org/view-pdf/id/2?page=56&search=defect%20report&highlight=5.5)
- [Salinan arsip CTFL v4.0](http://archive.org/stream/istqb-ctfl-syllabus-v-4.0/ISTQB_CTFL_Syllabus-v4.0_djvu.txt)
- [ISTQB — CTFL v4.0 Sample Exam Questions](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_v4.0_Sample-Exam-A-Questions_v1.7.pdf)
- [ISTQB — CT-MAT Syllabus v1.0](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CT-MAT_Syllabus_v1.0_2019.pdf)
- [ISTQB — CTAL-TTA Syllabus v4.0](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB-CTAL-TTA_Syllabus_v4.0.pdf)
- [ISTQB — CT-ATLaS BoK v2.0](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CT-ATLaS_Body-of-Knowledge_v2.0.pdf)
- [ISTQB TBOK — Exam questions TA-5.3.1](https://tbok.istqb.org/exam-questions?lo=TA-5.3.1&syllabus_id=7&q=defect+report)

**[Praktik industri] — dokumentasi resmi vendor/proyek**

- [Pact Docs — How Pact works](https://docs.pact.io/getting_started/how_pact_works)
- [Pact Docs — Pact Nirvana Step 6: can-i-deploy](https://docs.pact.io/pact_nirvana/step_6)
- [Pact Docs — Provider verification badges](https://docs.pact.io/pact_broker/advanced_topics/provider_verification_badges)
- [Grafana k6 Docs — Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/)
- [OWASP WSTG — Latest / About](https://wstg.owasp.org/latest/1-About/)
- [OWASP — WSTG release versions](https://owasp.org/projects/web-security-testing-guide?tab=release-versions)
- [OWASP/ASVS v5.0.0 README (repositori resmi)](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/README.md)
- [OWASP ASVS 5.0.0 English PDF](https://github.com/OWASP/ASVS/raw/v5.0.0/5.0/OWASP_Application_Security_Verification_Standard_5.0.0_en.pdf)
- [GitLab Docs — Merge request approval policies](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/)
- [GitLab Docs — Unit test reports](https://docs.gitlab.com/ci/testing/unit_test_reports/)
- [GitHub Docs — About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [GitHub Docs — Store and share data with workflow artifacts](https://docs.github.com/zh/actions/tutorials/store-and-share-data)
- [Playwright Docs — Auto-waiting](https://playwright.dev/docs/actionability)
- [Playwright Docs — Trace viewer](https://playwright.dev/docs/trace-viewer-intro)
- [Playwright Docs — Retries](https://playwright.dev/docs/test-retries)
- [JUnit User Guide 6.1.3 — Overview](https://docs.junit.org/6.1.3/overview.html)
- [AWS — Chaos Engineering on AWS (PDF)](https://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/chaos-engineering-on-aws.pdf)

**[Praktik industri] — riset dan opini primer**

- [Google Testing Blog — SMURF: Beyond the Test Pyramid](https://testing.googleblog.com/2024/10/?m=0)
- [Google Testing Blog — Test Sizes](https://testing.googleblog.com/2010/12/test-sizes.html)
- [Google Testing Blog — Code Coverage Best Practices](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html)
- [Kent C. Dodds — The Testing Trophy and Testing Classifications](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications)
- [DORA — Software delivery performance metrics](https://dora.dev/guides/dora-metrics/)
- [DORA — Accelerate State of DevOps Report 2024](https://dora.dev/research/2024/dora-report/)
- [DORA — Quick Check 2019 results](https://dora.dev/quickcheck/2019/results/)
- [DORA — A history of DORA's software delivery metrics](https://dora.dev/insights/dora-metrics-history/)

**[Rekomendasi peneliti/tim]** Seluruh butir berpenanda ini adalah inferensi dari rujukan di atas (KQ1–KQ10 catatan sumber), tanpa dokumen atau URL terpisah; karenanya tidak diklaim sebagai norma standar.
