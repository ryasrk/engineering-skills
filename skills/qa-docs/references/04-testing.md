# TOPIK 4: Testing / QA (strategi, rencana, dan artefak pengujian)

> Konvensi sitasi yang dipakai di seluruh catatan: **[Standar resmi]** = ISO/IEC/IEEE, W3C, atau badan standardisasi; **[Sertifikasi/resmi badan]** = syllabus/badan resmi ISTQB; **[Dokumentasi resmi vendor/proyek]** = spesifikasi/API produk resmi Pact, k6, Playwright, OWASP (WSTG/ASVS), GitHub, GitLab, AWS, JUnit; **[Praktik industri / opini]** = Google Testing Blog, riset DORA (dora.dev), tulisan Kent C. Dodds, atau tulisan praktisi lainnya — semuanya **sumber primer pada situs resminya**, tetapi bukan standar normatif; **[Inferensi]** = turunan peneliti dari sumber di atas, bukan klaim standar. Seluruh norma di bawah relevan untuk rentang 2024–2026; nomor edisi disebut eksplisit. Batas scope: BRD, FSD, dokumen desain arsitektur/UI, laporan harian, struktur folder/repo, dan API versioning sengaja tidak dibahas karena menjadi topik peneliti 1–3, 5, dan 6. Keterlacakan hanya disebut sebatas `{{requirement_id}}` pada *test basis*.

## KQ1 — Perbedaan Test Policy, Test Strategy, Test Plan, Test Case, dan Test Summary Report menurut ISO/IEC/IEEE 29119

### Takeaway
Edisi yang masih aktif adalah **ISO/IEC/IEEE 29119-1:2022, 29119-2:2021, 29119-3:2021, 29119-4:2021, dan 29119-5:2024**; 29119-3:2013 sudah digantikan. Perbedaan paling sering disalahpahami: dalam **29119-3:2021**, *Test Strategy* bukan lagi dokumen organisasi yang berdiri sendiri, melainkan **bagian dari Test Plan (Klausul 7.2.7)**, sedangkan dokumen tingkat organisasi adalah **Test Policy (6.2)** dan **Organizational Test Practices (6.3)**. *Test Summary Report* adalah sinonim lama untuk **Test Completion Report (7.4)**. — [IEEE SA — seri 29119 aktif](https://standards.ieee.org/ieee/29119-3/7499/); [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)

### Cited Findings
- **[Standar resmi]** ISO/IEC/IEEE 29119-3:2021 (Second edition, 2021-10) adalah standar aktif untuk *Test documentation*; IEEE mencatat status *Active Standard*, disetujui 2021-09-23, published 2021-10-28, dan *superseding* 29119-3:2013. — [IEEE SA — IEEE/ISO/IEC 29119-3-2021](https://standards.ieee.org/ieee/29119-3/7499/)
- **[Standar resmi]** Halaman IEEE yang sama mendaftarkan standar aktif lain dalam seri: 29119-1-2021 (*General concepts*), 29119-2-2021 (*Test processes*), 29119-4-2021 (*Test techniques*), 29119-5-2024 (*Keyword-Driven Testing*), serta menyatakan 29119-3:2013 dan 29119-1/2-2013 sudah *superseded*. — [IEEE SA — IEEE/ISO/IEC 29119-3-2021](https://standards.ieee.org/ieee/29119-3/7499/)
- **[Standar resmi]** ISO/IEC/IEEE 29119-1:2013 berstatus **Withdrawn**; edisi penggantinya adalah 29119-1:2022 (edisi 2, *General concepts*), yang antara lain tidak lagi memakai konsep *test conditions* dan menggantinya dengan *test model*. — [ISO — ISO/IEC/IEEE 29119-1:2013 (Withdrawn)](https://www.iso.org/standard/45142.html); [ISO Online Browsing Platform — ISO/IEC/IEEE 29119-1:2022](https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso-iec-ieee%3A29119%3A-1%3Aed-2%3Av1%3Aen)
- **[Standar resmi — catatan perbedaan penamaan]** Katalog/OBP ISO menamai Part 1 edisi 2 sebagai **ISO/IEC/IEEE 29119-1:2022**, sedangkan halaman IEEE SA menamai standar aktif yang sama sebagai **IEEE/ISO/IEC 29119-1-2021**; keduanya merujuk edisi 2 yang menggantikan edisi 2013. Untuk Part 2, 3, dan 4, ISO dan IEEE sama-sama memakai tahun 2021. Penulis laporan sebaiknya mencantumkan tahun sesuai badan penerbit yang dirujuk dan tidak mencampur dua penamaan tanpa catatan. — [ISO Online Browsing Platform — 29119-1:2022](https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso-iec-ieee%3A29119%3A-1%3Aed-2%3Av1%3Aen); [IEEE SA — seri 29119 aktif](https://standards.ieee.org/ieee/29119-3/7499/)
- **[Standar resmi]** ISO/IEC/IEEE 29119-2:2021 (edisi 2, published 2021-10) menetapkan proses pengujian untuk organisasi, proyek, atau aktivitas pengujian apa pun dan berlaku untuk semua model SDLC. — [ISO — ISO/IEC/IEEE 29119-2:2021](https://www.iso.org/standard/79428.html)
- **[Standar resmi]** 29119-3:2021 mendefinisikan *test policy* sebagai dokumentasi tingkat eksekutif yang menjelaskan *purpose, goals, principles, dan scope* pengujian dalam organisasi; secara eksplisit **tidak merinci bagaimana pengujian dilakukan**. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, definisi 3.20 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** 29119-3:2021 mendefinisikan *test strategy* sebagai **bagian dari test plan** yang menjelaskan pendekatan untuk proyek, *test level*, atau *test type* tertentu; isinya biasanya mencakup test levels/types, retesting & regression testing, teknik desain beserta *test completion criteria*, test data, test environment, kebutuhan tool, dan ekspektasi deliverable. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, definisi 3.25 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** 29119-3:2021 mendefinisikan *test plan* sebagai deskripsi terperinci tentang tujuan pengujian serta sarana dan jadwal untuk mencapainya; satu proyek boleh punya lebih dari satu test plan (master/level/type plan). — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, definisi 3.19 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** 29119-3:2021 mendefinisikan *test case specification* sebagai dokumentasi satu atau lebih test case, *test result* sebagai indikasi pass/fail berdasarkan kesesuaian *actual results* dengan *expected results*, dan *incident report* sebagai dokumentasi kejadian anomali (juga disebut *bug report/defect report*). — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, definisi 3.1, 3.2, 3.4, 3.8, 3.22 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** 29119-3:2021 menyamakan **test completion report = test summary report**, yaitu laporan ringkasan pengujian yang telah dilakukan; *test status report* didefinisikan terpisah sebagai laporan status dalam satu periode pelaporan tertentu. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, definisi 3.9 dan 3.24 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** 29119-3:2021 juga mendefinisikan *test traceability matrix* (disebut pula *requirements test matrix*) sebagai dokumen/spreadsheet/tool untuk menghubungkan item terkait, misalnya requirement dengan test-nya; serta *organizational test practices* sebagai dokumentasi pendekatan yang direkomendasikan di tingkat organisasi dan selaras dengan test policy. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, definisi 3.5, 3.6, 3.26 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** Klausul 5.2 29119-3:2021 menetapkan *common information elements* untuk **semua** dokumen pengujian: unique identifier, issuing organization, approval authority, change history, status, introduction, scope, references, glossary. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, Klausul 5.2 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** Daftar isi 29119-3:2021 menetapkan section **Test Policy (6.2)**: 6.2.1 Overview, 6.2.2 Objectives of testing, 6.2.3 Test process, 6.2.4 Test organization structure, 6.2.5 Tester training, 6.2.6 Tester ethics, 6.2.7 Standards, 6.2.8 Other relevant policies, 6.2.9 Measuring the value of testing, 6.2.10 Test asset archiving and reuse, 6.2.11 Test process improvement. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, daftar isi (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** Daftar isi yang sama menetapkan section **Test Plan (7.2)**: 7.2.1 Overview, 7.2.2 Context of testing, 7.2.3 Assumptions and constraints, 7.2.4 Stakeholders, 7.2.5 Testing communication, 7.2.6 Risk register, **7.2.7 Test strategy**, 7.2.8 Testing activities and estimates, 7.2.9 Staffing, 7.2.10 Schedule. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, daftar isi (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** Section **Test Case Specification (8.3)** terdiri atas 8.3.1 Overview, 8.3.2 Test coverage items, 8.3.3 Test cases; section **Test Incident Report (8.11)** mencakup timing information, originator, context, description of the incident, assessment of severity, assessment of priority, risk, dan status of the incident. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, daftar isi Klausul 8.3 dan 8.11 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** Section **Test Status Report (7.3)**: test status, reporting period, progress against test plan, factors blocking progress, test measures, new and changed risks, planned testing. Section **Test Completion Report (7.4)**: summary of testing performed, deviations from planned testing, test completion evaluation, factors that blocked progress, test measures, residual risks, test deliverables, reusable test assets, lessons learned. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, daftar isi Klausul 7.3–7.4 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** Klausul 4.1 29119-3:2021 mengizinkan **tailored conformance**: judul/heading dokumen boleh diubah, dokumen boleh digabung atau dipisah, dan organisasi **shall** menyatakan apakah klaimnya *full* atau *tailored conformance*; justifikasi **shall** diberikan saat tailoring. Status *shall/should/may* untuk tiap information item dirinci di **Annex A (normative)**. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, Klausul 4.1 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** 29119-3:2021 mendukung dynamic/non-dynamic, functional/non-functional, manual/otomatis, scripted/unscripted testing, serta semua model lifecycle termasuk agile dan DevOps; dokumentasi boleh berupa kertas maupun elektronik (records di test tool, spreadsheet, mind map, foto whiteboard). — [IEEE SA — IEEE/ISO/IEC 29119-3-2021](https://standards.ieee.org/ieee/29119-3/7499/); [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, Introduction (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** Perubahan teknis utama edisi 2021 terhadap 2013: konsep *test conditions* **digantikan** oleh *test models*; Annex T menjelaskan alasannya, Annex S memetakan ke IEEE 829:2008 yang sudah *superseded*. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, Foreword dan Annex S/T (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Sertifikasi/resmi badan]** ISTQB CTFL v4.0 (2023-04-21) / v4.0.1 (2024-09-15) menyatakan test plan mendokumentasikan sarana dan jadwal pencapaian tujuan, menjamin aktivitas memenuhi kriteria, menjadi alat komunikasi, dan mendemonstrasikan kepatuhan pada test policy/test strategy (atau menjelaskan deviasinya); konten tipikal meliputi context, assumptions/constraints, stakeholders, communication, risk register, test approach, budget, dan schedule, dengan rujukan eksplisit ke ISO/IEC/IEEE 29119-3. — [ISTQB TBOK — CTFL Syllabus v4.0.1 PDF viewer](https://tbok.istqb.org/view-pdf/id/2); [Salinan arsip CTFL v4.0](http://archive.org/stream/istqb-ctfl-syllabus-v-4.0/ISTQB_CTFL_Syllabus-v4.0_djvu.txt)
- **[Sertifikasi/resmi badan]** ISTQB CTFL v4.0 §5.3.2 membedakan *test progress reports* (berkala, untuk monitoring & control) dengan *test completion reports* (pada selesainya project/test level/test type, idealnya setelah exit criteria terpenuhi) dan menyebut standar 29119-3 memakai istilah *test status reports* serta *test completion reports*. — [ISTQB TBOK — CTFL Syllabus v4.0.1](https://tbok.istqb.org/view-pdf/id/2?page=56&search=defect%20report&highlight=5.5)

### Inferences
- **[Inferensi]** Hierarki yang aman dipakai tim: **Test Policy** (organisasi, *why/what*, jarang berubah) → **Organizational Test Practices** (organisasi, *how* generik, boleh banyak dokumen per konteks) → **Test Plan** (proyek/rilis, *who/when/with what*, memuat **Test Strategy** di 7.2.7) → **Test Model/Test Case/Test Procedure Specification plus Test Data & Environment Requirements** (dinamis, per test item) → **Test Status Report** (berkala) dan **Test Completion Report / Test Summary Report** (sekali per penutupan). Turunan dari [ISO/IEC/IEEE 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf) dan [ISTQB CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2).
- **[Inferensi]** Sebutan "section wajib" perlu kehati-hatian: daftar isi di atas adalah **section terstandarisasi**, tetapi tingkat kewajiban per information item (`shall`/`should`/`may`) ada di Annex A yang tidak tersedia pada pratinjau publik. Untuk organisasi yang tidak mengklaim *full conformance*, **tailored conformance** adalah jalur resmi, bukan pelanggaran. — [ISO/IEC/IEEE 29119-3:2021 Klausul 4.1](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Inferensi]** Jika organisasi masih memakai template lama bertajuk "Organizational Test Strategy" atau "Test Summary Report", itu bukan istilah kanonik 29119-3:2021; petakan ke **Organizational Test Practices (6.3)** + **Test Strategy (7.2.7)** dan ke **Test Completion Report (7.4)** agar audit tidak ambigu. — [ISO/IEC/IEEE 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Inferensi]** 29119-4:2021 (teknik desain) dan 29119-5:2024 (keyword-driven testing) melengkapi 29119-3:2021: yang pertama dipakai untuk mengisi 7.2.7, yang kedua untuk standardisasi test case modular dan pertukaran artefak antar-tool. — [IEEE SA — seri 29119 aktif](https://standards.ieee.org/ieee/29119-3/7499/)

### Gaps
- Teks lengkap 29119-3:2021, 29119-1:2022, 29119-2:2021, dan 29119-4:2021 berbayar; yang diverifikasi langsung adalah pratinjau resmi 15 halaman (daftar isi, definisi Klausul 3, Klausul 1–4, Foreword/Introduction) dikawinkan dengan halaman katalog resmi ISO/IEC/IEEE. **Annex A (normatif)** yang memetakan `shall/should/may` per item tidak terbuka publik, sehingga daftar "wajib" di atas tidak boleh diklaim sebagai semuanya `shall`. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [IEEE SA — seri 29119 aktif](https://standards.ieee.org/ieee/29119-3/7499/); [ISO — 29119-2:2021](https://www.iso.org/standard/79428.html)
- Saya tidak menemukan entitas dokumen **"Organizational Test Strategy"** di daftar isi edisi 2021; istilah itu masih muncul di literatur edisi 2013. Catatan ini perlu diverifikasi ulang jika organisasi memiliki salinan berlisensi lengkap. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [ISO — 29119-3:2013](https://www.iso.org/standard/56737.html?browse=ics)
- Nomor halaman ISO untuk URL katalog `https://www.iso.org/standard/79429.html` tidak berhasil diambil (timeout); katalog IEEE/IEC dan pratinjau iTeh digunakan sebagai pengganti primer yang setara.

## KQ2 — Test pyramid, testing trophy, shift-left, dan komposisi unit/integration/contract/E2E

### Takeaway
**Test pyramid** adalah heuristik jumlah/granularitas, **testing trophy** adalah opini industri yang menggeser bobot terbesar ke integration untuk aplikasi UI, sedangkan **shift-left** bukan komposisi melainkan pergeseran **waktu** pengujian ke awal SDLC. Tidak ada standar yang menetapkan persentase; Google (2024) justru mengusulkan memperluas pyramid dengan trade-off **SMURF** (Speed, Maintainability, Utilization, Reliability, Fidelity). — [Google Testing Blog — SMURF](https://testing.googleblog.com/2024/10/?m=0); [ISTQB CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2); [Kent C. Dodds — Testing Trophy](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications)

### Cited Findings
- **[Praktik industri / opini]** Google Testing Blog (2024-10-15, "SMURF: Beyond the Test Pyramid") menyebut test pyramid sebagai *canonical heuristic* dengan pesan "prefer more unit tests than integration tests, and prefer more integration tests than end-to-end tests", tetapi mengingatkan pyramid kurang rinci saat suite membesar; SMURF memetakan lima dimensi yang sering bertension: Speed, Maintainability, Utilization, Reliability, Fidelity. Unit unggul pada speed/utilization; integration dan E2E unggul pada *fidelity* terhadap kondisi produksi. — [Google Testing Blog — SMURF: Beyond the Test Pyramid](https://testing.googleblog.com/2024/10/?m=0)
- **[Praktik industri / opini]** Google juga menegaskan reliable tests hanya gagal saat ada masalah nyata; menyortir flaky test membuang waktu developer dan biaya rerun, dan non-determinisme meningkat seiring ukuran sistem. — [Google Testing Blog — SMURF: Beyond the Test Pyramid](https://testing.googleblog.com/2024/10/?m=0)
- **[Praktik industri / opini]** Google "Test Sizes" (2010) memetakan Small ≈ unit test, Medium ≈ integration test (dua tier berkomunikasi), Large ≈ end-to-end/system test; ini tetap menjadi rujukan kosakata ukuran test. — [Google Testing Blog — Test Sizes](https://testing.googleblog.com/2010/12/test-sizes.html)
- **[Sertifikasi/resmi badan]** ISTQB CTFL v4.0 §5.1.6 menyatakan pyramid membantu alokasi effort otomasi: lapisan bawah kecil, terisolasi, cepat, dan jumlahnya banyak; lapisan atas E2E kompleks, lebih lambat, dan jumlahnya sedikit; **jumlah dan penamaan lapisan boleh berbeda** (model asli Cohn 2009: unit/service/UI; model populer: unit/component integration/E2E). — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2); [ISTQB — CTFL v4.0 Sample Exam Questions](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_v4.0_Sample-Exam-A-Questions_v1.7.pdf)
- **[Sertifikasi/resmi badan]** ISTQB CTFL v4.0 §2.1.5 mendefinisikan shift-left sebagai pengujian lebih awal (bukan meniadakan pengujian akhir): review spesifikasi dari sudut pandang testing, menulis test case sebelum kode, CI/CD dengan feedback cepat dan component tests, static analysis sebelum dynamic testing, serta non-functional testing sejak component level. — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Sertifikasi/resmi badan]** ISTQB §5.1.7 (Testing Quadrants) menempatkan component/component integration tests pada Q1 (technology-facing, mendukung tim, otomatis di CI); functional tests, contoh, user story tests, API testing pada Q2; exploratory, usability, UAT pada Q3 (sering manual); smoke dan non-functional tests pada Q4 (sering otomatis). — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Praktik industri / opini]** Kent C. Dodds mendefinisikan unit test sebagai test atas unit tanpa collaborator atau dengan collaborator yang di-mock, integration test sebagai test atas beberapa unit yang saling berintegrasi, dan mempromosikan **Testing Trophy** dengan integration sebagai lapisan terbesar; ini tulisan praktisi (2021-06-02), bukan standar. — [Kent C. Dodds — The Testing Trophy and Testing Classifications](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications)
- **[Dokumentasi resmi vendor/proyek]** Pact mendokumentasikan consumer-driven contracts: consumer test memakai mock provider, menghasilkan *pact file*, lalu provider verification membandingkan respons aktual dengan *minimal expected response*; kontrak sebaiknya fokus pada pesan (request/response), bukan functional behaviour provider, dan **data-independent**. — [Pact Docs — How Pact works](https://docs.pact.io/getting_started/how_pact_works)
- **[Dokumentasi resmi vendor/proyek]** Pact `can-i-deploy` memeriksa matriks kompatibilitas consumer/provider sebelum deploy; dokumen resmi menyarankan pengecekan ulang menjelang release bila jeda antara verifikasi dan deploy lama, serta memperingatkan agar **tidak memakai data acak dalam pact** karena broker akan menganggapnya revisi kontrak baru. — [Pact Docs — Pact Nirvana Step 6: can-i-deploy](https://docs.pact.io/pact_nirvana/step_6)
- **[Dokumentasi resmi vendor/proyek]** Pact Broker membedakan **can-i-merge** (kompatibilitas cabang untuk mergeability) dan **can-i-deploy** (deployability ke environment tertentu). — [Pact Docs — Provider verification badges](https://docs.pact.io/pact_broker/advanced_topics/provider_verification_badges)

### Inferences
- **[Inferensi]** Ketiganya menjawab pertanyaan berbeda dan **boleh dipakai bersamaan**: pyramid/trophy = *seberapa banyak tiap lapisan*; shift-left = *kapan*; SMURF = *kriteria trade-off* saat menimbang ulang komposisi. Tidak ada yang saling menggantikan. — [Google Testing Blog 2024](https://testing.googleblog.com/2024/10/?m=0); [ISTQB CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Inferensi — angka heuristic, BUKAN norma standar]** Tidak satu pun sumber primer di atas memberi persentase. Untuk diskusi awal tim (bukan target audit), komposisi yang masuk akal: **(a) service/backend murni**: unit ≈ 60–70%, integration ≈ 20–30%, contract ≈ 5–10% per pasangan consumer–provider, E2E ≈ 5% untuk critical journeys; **(b) aplikasi UI-heavy**: ikuti trophy, integration (component + API + rendered UI) menjadi lapisan terbesar, unit untuk logika murni, E2E hanya happy path dan journey berisiko tinggi; **(c) microservices dengan deploy independen**: contract test wajib ada per pasangan dan `can-i-deploy` menjadi gate, sehingga porsi E2E bisa ditekan; **(d) sistem safety-critical/regulasi**: naikkan porsi integration/E2E dan teknik coverage formal karena *fidelity* dan bukti audit lebih penting daripada speed. Semua angka harus ditetapkan ulang lewat analisis risiko produk, bukan dijadikan KPI. — [ISTQB CTFL v4.0 §5.2.3](https://tbok.istqb.org/view-pdf/id/2); [Google SMURF](https://testing.googleblog.com/2024/10/?m=0); [Pact Docs](https://docs.pact.io/pact_nirvana/step_6)
- **[Inferensi]** Pilih **pyramid** bila biaya CI, kecepatan feedback, dan maintainability menjadi kendala utama; pilih **trophy** bila kebanyakan defect muncul di batas komponen/UI sehingga mock berlebih menurunkan fidelity; pilih **shift-left** sebagai filosofi wajib di semua kasus karena ia tidak berbenturan dengan keduanya. — [Google SMURF](https://testing.googleblog.com/2024/10/?m=0); [ISTQB CTFL v4.0 §2.1.5](https://tbok.istqb.org/view-pdf/id/2); [Kent C. Dodds](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications)
- **[Inferensi]** Contract test bukan pengganti integration test: Pact secara eksplisit menggantikan *intermediary* dan memverifikasi bentuk pesan, sedangkan perilaku end-to-end tetap perlu functional test lain. — [Pact Docs — How Pact works](https://docs.pact.io/getting_started/how_pact_works)

### Gaps
- Tidak ada standar resmi (ISO/IEC/IEEE maupun ISTQB) yang menetapkan rasio unit:integration:contract:E2E; semua angka di atas adalah heuristic peneliti dan harus dicatat sebagai keputusan tim, bukan klaim normatif. — [ISTQB CTFL v4.0.1 §5.1.6](https://tbok.istqb.org/view-pdf/id/2); [Google Testing Blog — SMURF](https://testing.googleblog.com/2024/10/?m=0); [ISO/IEC/IEEE 29119-3:2021 Klausul 7.2.7](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- Tulisan Testing Trophy adalah opini satu praktisi dan tidak memiliki versi standar/nomor rilis resmi; ia dipakai di sini hanya sebagai pelengkap, bukan satu-satunya dasar. — [Kent C. Dodds — The Testing Trophy and Testing Classifications](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications); [ISTQB CTFL v4.0.1 §5.1.6](https://tbok.istqb.org/view-pdf/id/2)

## KQ3 — Jenis pengujian yang perlu direncanakan: tujuan, tools resmi, dan exit criteria

### Takeaway
Rencanakan jenis pengujian dari **risk register**, bukan dari daftar checklist generik. Exit criteria yang dapat diotomasi (threshold k6, `can-i-deploy`, required status checks, policy vulnerability, WCAG success criteria) jauh lebih dapat dipertanggungjawabkan daripada "semua test hijau". — [ISO/IEC/IEEE 29119-3:2021 Klausul 7.2.6–7.2.7](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [Grafana k6 Docs — Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/); [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/)

### Cited Findings
- **[Standar resmi]** 29119-3:2021 Klausul 7.2.7 menempatkan pemilihan *test levels*, *test types*, retesting/regression, teknik desain dan *test completion criteria*, test data, environment, serta tool di dalam **Test Strategy** pada Test Plan; Klausul 8.5–8.8 menstandarisasi test data requirements, test environment requirements, dan dua *readiness report*. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** IEEE mencatat 29119-2:2013 mengikuti pendekatan risk-based karena testing adalah mitigasi risiko, dan 29119-4:2021 menyatakan risk-based testing dapat dipakai untuk memilih teknik yang aplicable serta dirujuk di 29119-1 dan 29119-2. — [IEEE SA — seri 29119](https://standards.ieee.org/ieee/29119-3/7499/); [ISO — 29119-2:2021](https://www.iso.org/standard/79428.html)
- **[Dokumentasi resmi vendor/proyek]** k6 thresholds adalah *pass/fail criteria* untuk metrik load test; bila threshold gagal, k6 keluar dengan **non-zero exit code** (cocok untuk CI gate). Contoh resmi: `http_req_failed: ['rate<0.01']` dan `http_req_duration: ['p(95)<200']`; `checks` **tidak** memengaruhi exit status, sehingga harus dipasangkan dengan threshold. — [Grafana k6 Docs — Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/)
- **[Dokumentasi resmi vendor/proyek]** OWASP Web Security Testing Guide (WSTG) `Latest` saat ini (copyright 2026) adalah penyempurnaan inkremental dengan format skenario dan objective distandardisasi; versi **Stable masih menunjuk ke v4.2** yang dirilis 2020-12-03. — [OWASP WSTG — Latest / About](https://wstg.owasp.org/latest/1-About/); [OWASP — WSTG release versions](https://owasp.org/projects/web-security-testing-guide?tab=release-versions)
- **[Dokumentasi resmi vendor/proyek]** **OWASP ASVS 5.0.0** (Mei 2025) adalah versi stabil terkini, menggantikan 4.0.3 (2021); requirement dirujuk dengan format `v<version>-<chapter>.<section>.<requirement>`, mis. `v5.0.0-1.2.5`, dan penulis dokumen lain dianjurkan menyertakan versi karena identifier bisa berubah. — [OWASP/ASVS v5.0.0 README (repositori resmi)](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/README.md); [OWASP ASVS 5.0.0 English PDF](https://github.com/OWASP/ASVS/raw/v5.0.0/5.0/OWASP_Application_Security_Verification_Standard_5.0.0_en.pdf)
- **[Dokumentasi resmi vendor/proyek]** GitLab merge request approval policies dapat mewajibkan approval berdasarkan temuan scanner (`scan_finding`), dengan `severity_levels`, `vulnerabilities_allowed`, dan `vulnerability_states`; bila aturan invalid/tidak dapat dievaluasi, **default `fail: closed` memblokir MR**. Semua scanner yang ditentukan harus menghasilkan report artifact, baik di source maupun target branch. — [GitLab Docs — Merge request approval policies](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/)
- **[Standar resmi]** **WCAG 2.2** adalah W3C Recommendation (dipublikasikan ulang 2024-12-12 dengan errata); success criteria ditulis sebagai pernyataan **teruji**, tidak terikat teknologi, dengan level A/AA/AAA, dan dirancang untuk diuji dengan **kombinasi automated testing dan human evaluation**. W3C menyarankan memakai versi paling baru saat menyusun kebijakan aksesibilitas. — [W3C — WCAG 2.2 Recommendation](https://www.w3.org/TR/WCAG22/); [W3C — REC-WCAG22-20241212](https://www.w3.org/TR/2024/REC-WCAG22-20241212/); [W3C WAI — What's New in WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/)
- **[Dokumentasi resmi vendor/proyek]** Playwright menyediakan auto-waiting/actionability checks dan auto-retrying assertions untuk mengurangi flakiness, Trace Viewer untuk inspeksi DOM/CSS pasca-kegagalan, serta kategori hasil `passed` / `flaky` / `failed` saat retries aktif. — [Playwright Docs — Auto-waiting](https://playwright.dev/docs/actionability); [Playwright Docs — Trace viewer](https://playwright.dev/docs/trace-viewer-intro); [Playwright Docs — Retries](https://playwright.dev/docs/test-retries)
- **[Dokumentasi resmi vendor/proyek]** JUnit User Guide (docs.junit.org, rilis 6.1.3) adalah rujukan resmi untuk penulisan test, extension author, dan integrasi build tool/IDE; fitur `@Tag`/`@DisplayName` mendukung pengelompokan suite unit/integration. — [JUnit User Guide 6.1.3 — Overview](https://docs.junit.org/6.1.3/overview.html)
- **[Sertifikasi/resmi badan]** ISTQB CTFL v4.0 §5.1.3 menyebut smoke tests sebagai contoh *initial quality level* pada entry criteria dan menempatkan smoke tests pada Quadrant Q4; §5.1.7 menempatkan UAT, usability, dan exploratory testing pada Q3. — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Sertifikasi/resmi badan]** ISTQB CT-MAT Syllabus v1.0 (2019) membahas pendekatan automation test lab, remote device access (RDA), user-agent based vs device-based testing, serta keterbatasan sensor/cloud lab untuk kompatibilitas perangkat. — [ISTQB — CT-MAT Syllabus v1.0](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CT-MAT_Syllabus_v1.0_2019.pdf)
- **[Standar resmi — masih draft]** **ISO/IEC/IEEE DIS 29119-14** (*Data migration testing*) masih berstatus draft (CD/DIS per 2026) dan mendefinisikan proses, dokumentasi, serta pendekatan pengujian migrasi data dengan menerapkan 29119-1/2/3/4 dan ISO/IEC 20246; IEEE mencatatnya sebagai proyek **P29119-14** yang belum menjadi standar aktif. — [ISO — ISO/IEC/IEEE DIS 29119-14](https://www.iso.org/cms/live/live/es/sites/isoorg/contents/data/standard/08/88/88837.html?browse=tc); [IEEE SA — P29119-14](https://standards.ieee.org/ieee/29119-3/7499/)
- **[Dokumentasi resmi vendor/proyek]** AWS Prescriptive Guidance untuk chaos engineering mensyaratkan definisi **steady state**, metrik steady state, observability steady state, requirement observability (alarm, log, MTTR, debug), serta dokumen perencanaan dan hasil eksperimen. — [AWS — Chaos Engineering on AWS (PDF)](https://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/chaos-engineering-on-aws.pdf)
- **[Praktik industri / opini]** DORA 2024 menyatakan adopsi AI meningkatkan produktivitas individu tetapi berdampak negatif pada stabilitas dan throughput pengiriman, sehingga fundamental seperti **small batch sizes dan robust testing tetap krusial**. — [DORA — Accelerate State of DevOps Report 2024](https://dora.dev/research/2024/dora-report/)
- **[Sertifikasi/resmi badan]** ISTQB CTFL v4.0 §5.3.1 mendaftar metrik produk (availability, response time, mean time to failure), metrik defect, metrik risiko (residual risk level), dan metrik coverage sebagai dasar monitoring. — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)

### Inferences
Matriks berikut adalah **[Inferensi]** berupa *contoh exit criteria yang harus disahkan di Test Plan*, diturunkan dari [ISO/IEC/IEEE 29119-3:2021 Klausul 7.2.7](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf), [ISTQB CTFL v4.0 §5.1.3](https://tbok.istqb.org/view-pdf/id/2), dan docs vendor yang disebut di kolom sumber. Tidak ada angka di bawah yang berstatus norma standar.

| Jenis | Tujuan | Tools / docs resmi | Contoh exit criteria |
| --- | --- | --- | --- |
| Unit / component | Verifikasi logika terisolasi, feedback tercepat | [JUnit 6.1.3](https://docs.junit.org/6.1.3/overview.html); [ISTQB Q1](https://tbok.istqb.org/view-pdf/id/2) | Seluruh test pada diff berstatus pass; coverage kode baru ≥ `{{new_code_coverage_threshold}}`; tidak ada assertion yang dikosongkan |
| Integration | Verifikasi kolaborasi antar-unit, DB, queue, adapter | [ISTQB Q1/Q2](https://tbok.istqb.org/view-pdf/id/2); [Google Test Sizes](https://testing.googleblog.com/2010/12/test-sizes.html) | Semua integration case untuk `{{critical_integrations}}` pass; state di-reset antar-test; tidak ada koneksi ke data produksi |
| API / contract (consumer-driven) | Menjaga kompatibilitas pesan consumer–provider tanpa menjalankan kedua service sekaligus | [Pact — How Pact works](https://docs.pact.io/getting_started/how_pact_works); [Pact — can-i-deploy](https://docs.pact.io/pact_nirvana/step_6); [Pact badges](https://docs.pact.io/pact_broker/advanced_topics/provider_verification_badges) | Pact dipublikasikan per versi aplikasi; provider verification result terpublikasi ke broker; `can-i-deploy --to-environment {{env}}` sukses; `can-i-merge` sukses untuk PR |
| E2E / UI | Membuktikan critical journey dari sudut pandang pengguna | [Playwright — Actionability](https://playwright.dev/docs/actionability); [Trace viewer](https://playwright.dev/docs/trace-viewer-intro); [Retries](https://playwright.dev/docs/test-retries) | `{{critical_journeys}}` pass pada run pertama; jumlah `flaky` = `{{flake_budget}}` (target 0 untuk gate); trace disimpan untuk tiap failure |
| Regression | Mencegah perubahan merusak perilaku yang sudah ada | [ISO 29119-3:2021 def. 3.25](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [ISTQB](https://tbok.istqb.org/view-pdf/id/2) | Suite regression wajib `{{regression_suite_id}}` 100% dieksekusi dan pass; tidak ada defect baru di atas `{{severity_threshold}}` |
| Smoke | Menjadi entry criteria sebelum level pengujian lain / deploy | [ISTQB §5.1.3 & Q4](https://tbok.istqb.org/view-pdf/id/2) | Smoke `{{smoke_suite_id}}` pass pada artefak `{{build_sha}}`; kegagalan memblokir entry ke tahap berikutnya |
| Performance / load | Membuktikan SLO di bawah beban representatif | [Grafana k6 — Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/) | Semua threshold bernilai true dan k6 exit code 0; `rate<{{error_rate_max}}`, `p({{percentile}})<{{latency_ms}}`; `checks` tetap dipasang threshold |
| Security | Menemukan kerentanan dan memverifikasi kontrol aplikasi | [OWASP WSTG Latest](https://wstg.owasp.org/latest/1-About/); [OWASP ASVS 5.0.0](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/README.md); [GitLab approval policies](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/) | Tidak ada temuan baru critical/high dengan `fix_available: true` pada `{{asvs_level}}`; report artifact ada di source & target; policy terverifikasi (bukan `fail: open` tanpa persetujuan risiko) |
| Accessibility | Memenuhi success criteria yang dapat diuji | [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/); [W3C WAI new-in-2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/) | Seluruh success criteria level `{{wcag_target_level}}` untuk `{{scope_pages}}` terpenuhi; temuan automated = 0 **dan** evaluasi manusia terdokumentasi |
| Compatibility | Perilaku konsisten lintas browser/OS/perangkat | [ISTQB CT-MAT v1.0](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CT-MAT_Syllabus_v1.0_2019.pdf); [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Matriks `{{browser_device_matrix}}` dieksekusi; tidak ada defect blocking pada kombinasi yang dideklarasikan didukung |
| Data migration | Integritas, kelengkapan, dan rekonsiliasi data saat migrasi | [ISO/IEC/IEEE DIS 29119-14 (draft)](https://www.iso.org/cms/live/live/es/sites/isoorg/contents/data/standard/08/88/88837.html?browse=tc); [29119-3:2021 Klausul 8.5](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf) | Row count/checksum cocok; referential integrity 0 violation; dry-run rollback berhasil; *readiness report* data & environment berstatus siap |
| UAT | Konfirmasi penerimaan oleh pemangku kepentingan bisnis | [ISTQB Q3 & §5.3.2](https://tbok.istqb.org/view-pdf/id/2) | Acceptance criteria `{{acceptance_criteria_ids}}` terpenuhi; sign-off `{{business_owner}}`; residual risk dicatat dan diterima |
| Chaos / resilience | Menguji hipotesis steady state saat kegagalan diinjeksikan | [AWS Chaos Engineering on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/chaos-engineering-on-aws.pdf); [DORA 2024](https://dora.dev/research/2024/dora-report/) | Metrik steady state tetap dalam `{{slo}}`; alarm & log terverifikasi; MTTR terukur; eksperimen dapat di-abort; tidak ada dampak di luar `{{blast_radius}}` |
| Observability / produksi | Mendeteksi kegagalan yang lolos dari pre-release | [DORA — software delivery performance metrics](https://dora.dev/guides/dora-metrics/); [ISTQB §5.3.3 dashboards CI/CD](https://tbok.istqb.org/view-pdf/id/2) | Change fail rate dan failed deployment recovery time terukur per aplikasi; alert berbunyi dalam `{{detection_slo}}`; synthetic check aktif |

### Gaps
- **ASVS 4.0.3** yang disebut dalam daftar sumber prioritas sudah bukan versi stabil terkini; catatan ini memakai **5.0.0 (Mei 2025)** dan tetap menyebut 4.0.3 sebagai pendahulu. Tim yang terikat kontrak pada 4.0.3 harus mencantumkan versi secara eksplisit karena identifier requirement berubah. — [OWASP/ASVS v5.0.0 README](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/README.md)
- WSTG memiliki dua jalur: `Latest` (2026, inkremental) dan `Stable = v4.2` (2020). Saya tidak menemukan nomor versi semantik untuk `Latest`; rencana pengujian sebaiknya mengunci salah satu URL/versi agar hasil audit reproducible. — [OWASP WSTG — Latest / About](https://wstg.owasp.org/latest/1-About/); [OWASP — WSTG release versions](https://owasp.org/projects/web-security-testing-guide?tab=release-versions)
- **29119-14 masih DIS/CD**, sehingga exit criteria migrasi data di atas **tidak** boleh diklaim sebagai "sesuai standar ISO final". — [ISO — ISO/IEC/IEEE DIS 29119-14](https://www.iso.org/cms/live/live/es/sites/isoorg/contents/data/standard/08/88/88837.html?browse=tc)
- Tidak ada tool resmi tunggal untuk compatibility, data migration, dan UAT; kolom "tools resmi" untuk ketiganya berupa rujukan standar/syllabus, bukan rekomendasi vendor. — [ISTQB CT-MAT Syllabus v1.0](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CT-MAT_Syllabus_v1.0_2019.pdf); [ISTQB CTFL v4.0.1 §5.1.7](https://tbok.istqb.org/view-pdf/id/2)

## KQ4 — Test case yang baik, bug report yang baik, dan keterlacakan

### Takeaway
Test case yang baik memisahkan **spesifikasi** (prekondisi, data uji, langkah, expected result) dari **hasil eksekusi** (actual result, pass/fail, log). Bug report yang baik memisahkan **severity** (dampak) dari **priority** (urutan perbaikan) dan selalu menyertakan bukti serta konteks lingkungan. Keterlacakan menghubungkan *test basis → testware → result → defect → residual risk*. — [ISO/IEC/IEEE 29119-3:2021 definisi 3.1/3.2/3.22](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [ISTQB CTFL v4.0 §1.4.4 & §5.5](https://tbok.istqb.org/view-pdf/id/2?page=56&search=defect%20report&highlight=5.5)

### Cited Findings
- **[Standar resmi]** 29119-3:2021 memisahkan secara eksplisit: *actual results* (perilaku/kondisi yang teramati saat eksekusi), *expected results* (perilaku prediksi berdasarkan spesifikasi), dan *test result* (pass/fail bila actual sesuai/tidak sesuai expected); Klausul 8.9 menstandarisasi *Actual results and test result*, Klausul 8.10 *Test execution log*, Klausul 8.11 *Test incident report*. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, definisi 3.1/3.2/3.22 dan daftar isi (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** Klausul 8.3 *Test case specification* terdiri atas *test coverage items* dan *test cases*; Klausul 8.2 *Test model specification* memuat objective, priority, *test strategy extract*, test model, dan **traceability**; Klausul 8.5 *Test data requirements* memuat description, responsibility, period needed, **resetting needs**, serta **archiving or disposal**. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, daftar isi Klausul 8.2–8.5 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** Klausul 8.11 *Test incident report* mencakup timing information, originator, context, description of the incident, **originator's assessment of severity**, **originator's assessment of priority**, risk, dan status of the incident; Annex R berisi contoh *Incident report*. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, daftar isi (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** 29119-3:2021 mendefinisikan *test traceability matrix* sebagai dokumen/spreadsheet/tool untuk mengidentifikasi item yang saling terkait, misalnya requirement dengan test terkait, dengan catatan bahwa format dan tingkat detailnya boleh berbeda. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021, definisi 3.26 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Sertifikasi/resmi badan]** ISTQB CTFL v4.0 §1.4.4 mewajibkan (nilai praktik) keterlacakan antara elemen *test basis*, *testware* (test conditions, risks, test cases), *test results*, dan *detected defects*; manfaatnya: evaluasi coverage, evaluasi **residual risk**, analisis dampak perubahan, audit, pemenuhan IT governance, serta kemudahan memahami progress/completion report. — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Sertifikasi/resmi badan]** ISTQB CTFL v4.0 §5.5 menyatakan defect report yang dibuat saat dynamic testing lazim memuat: unique identifier; title ringkas; tanggal, organisasi penerbit, penulis beserta peran; identifikasi test object dan test environment; konteks (test case, aktivitas, fase SDLC, teknik/checklist/data uji); deskripsi failure yang memungkinkan reproduksi (langkah, log, database dump, screenshot, rekaman); **expected results dan actual results**; **severity**; **priority to fix**; status; referensi (mis. ke test case). ISTQB mencatat 29119-3 menyebutnya *incident reports*. — [ISTQB TBOK — CTFL v4.0.1, halaman 55–56](https://tbok.istqb.org/view-pdf/id/2?page=56&search=defect%20report&highlight=5.5)
- **[Sertifikasi/resmi badan]** ISTQB §5.4 Configuration Management mensyaratkan semua configuration item (test plan, strategy, test cases, scripts, results, logs, reports) diidentifikasi unik, version-controlled, dilacak perubahannya, dan saling direlasikan agar traceability terjaga; baseline yang disetujui hanya berubah lewat change control, sehingga hasil eksekusi lama dapat direproduksi. — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Sertifikasi/resmi badan]** ISTQB §5.1.5 memprioritaskan eksekusi test case berbasis risiko, coverage, atau prioritas requirement; urutan harus mempertimbangkan dependensi antar-test dan ketersediaan tool/environment/orang. — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Sertifikasi/resmi badan / praktik industri]** ISTQB CTAL-TA v4.0 mencatat 100% statement coverage tidak menjamin seluruh decision logic teruji, dan coverage berbasis teknik (equivalence partitioning, boundary value, decision table, state transition) diukur terhadap *coverage items* yang didefinisikan, bukan sekadar baris kode. — [ISTQB — CTAL-TTA Syllabus v4.0](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB-CTAL-TTA_Syllabus_v4.0.pdf)
- **[Dokumentasi resmi vendor/proyek]** Pact menyarankan *provider states* untuk menyatakan prekondisi dan memperingatkan agar tiap interaction independen ("create user 123, then log in" sebaiknya dipecah menjadi dua interaction); pact sebaiknya data-independent agar verifikasi tidak bergantung pada nilai data tertentu. — [Pact Docs — How Pact works](https://docs.pact.io/getting_started/how_pact_works)
- **[Dokumentasi resmi vendor/proyek]** Playwright menyediakan `testInfo.retry` untuk membersihkan state server sebelum retry dan menganjurkan test yang **terisolasi** agar dapat di-retry secara independen, bukan `describe.serial` yang menggantungkan test satu sama lain. — [Playwright Docs — Retries](https://playwright.dev/docs/test-retries)
- **[Dokumentasi resmi vendor/proyek]** GitHub Actions dapat mengunggah build dan test output (mis. laporan code coverage) sebagai artifact untuk debugging kegagalan test; GitLab menerima **JUnit XML** sebagai unit test report pada merge request. — [GitHub Docs — Store and share data with workflow artifacts](https://docs.github.com/zh/actions/tutorials/store-and-share-data); [GitLab Docs — Unit test reports](https://docs.gitlab.com/ci/testing/unit_test_reports/)

### Inferences
- **[Inferensi]** Field minimum test case yang diajukan (gabungan standar + praktik): `{{test_case_id}}`, `{{objective}}`, `{{requirement_id}}` (cukup ID dari *test basis*; isi BRD/FSD di luar scope), `{{risk_id}}`, `{{priority}}`, `{{preconditions}}`, `{{test_data_id}}`, `{{steps}}`, `{{expected_results}}`, `{{postconditions_cleanup}}`, lalu saat eksekusi `{{actual_results}}`, `{{result_pass_fail}}`, `{{build_sha}}`, `{{environment_id}}`, `{{evidence_links}}`, `{{incident_id}}`. — [ISO/IEC/IEEE 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [ISTQB CTFL v4.0 §1.4.4, §5.4, §5.5](https://tbok.istqb.org/view-pdf/id/2)
- **[Inferensi]** `severity` menjawab "seberapa parah dampaknya bagi pemangku kepentingan/requirement", `priority` menjawab "kapan diperbaiki"; keduanya boleh berbeda (mis. typo di halaman legal severity rendah namun priority tinggi menjelang peluncuran). Memisahkannya mencegah negosiasi yang mencampur dampak dan jadwal. — [ISTQB CTFL v4.0 §5.5](https://tbok.istqb.org/view-pdf/id/2?page=56&search=defect%20report&highlight=5.5); [ISO 29119-3:2021 Klausul 8.11.6–8.11.7](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Inferensi]** Traceability yang berguna bukan sekadar tabel requirement↔test case, melainkan rantai `{{requirement_id}} → {{risk_id}} → {{test_model_id}} → {{test_case_id}} → {{test_result}} → {{incident_id}} → {{residual_risk}}`, karena ISTQB memakai hasil test yang ditautkan ke risiko untuk menilai residual risk. — [ISTQB CTFL v4.0 §1.4.4](https://tbok.istqb.org/view-pdf/id/2); [ISO 29119-3:2021 Klausul 7.4.7](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Inferensi]** Bukti (log, screenshot, trace, database dump) sebaiknya diunggah sebagai artifact CI yang tertaut ke `{{build_sha}}`, bukan ditempel sebagai teks bebas, agar konfigurasi dapat direproduksi sesuai prinsip configuration management. — [GitHub Docs — workflow artifacts](https://docs.github.com/zh/actions/tutorials/store-and-share-data); [GitLab Docs — Unit test reports](https://docs.gitlab.com/ci/testing/unit_test_reports/); [ISTQB §5.4](https://tbok.istqb.org/view-pdf/id/2)

### Gaps
- Sub-klausul rinci 8.3.3.x (nomor field individual test case) tidak tersedia pada pratinjau publik; template di bawah disusun dari definisi Klausul 3, daftar isi Klausul 8.2–8.3, ISTQB §5.5, dan pemetaan Annex S, sehingga penomoran field tidak diklaim persis sama dengan standar berlisensi. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [ISTQB CTFL v4.0.1 §5.5](https://tbok.istqb.org/view-pdf/id/2?page=56&search=defect%20report&highlight=5.5)
- Tidak ada skala severity/priority baku (S1–S4, P0–P3) di ISO 29119-3 maupun ISTQB CTFL; skala harus didefinisikan secara lokal di test policy/organizational test practices. — [ISO/IEC/IEEE 29119-3:2021 Klausul 6.2/8.11](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [ISTQB CTFL v4.0.1 §5.5](https://tbok.istqb.org/view-pdf/id/2?page=56&search=defect%20report&highlight=5.5)
- Struktur dan isi BRD/FSD tidak diteliti sesuai batas topik; hanya `{{requirement_id}}` yang dipakai sebagai kunci tautan. — [ISO/IEC/IEEE 29119-3:2021 Klausul 4.1 tentang tailoring](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [ISTQB CTFL v4.0.1 §1.4.4](https://tbok.istqb.org/view-pdf/id/2)

## KQ5 — Entry/exit criteria, Definition of Done, coverage target, quality gate CI, flaky test, dan test data management

### Takeaway
Entry/exit criteria adalah kontrak yang **diukur**, bukan perasaan "sudah selesai". Quality gate yang baik bersifat *fail-closed*, berbasis artefak yang tidak bisa dilewati, dan memperlakukan test flaky sebagai defect yang harus diperbaiki—bukan sekadar di-retry. — [ISTQB CTFL v4.0 §5.1.3](https://tbok.istqb.org/view-pdf/id/2); [GitHub Docs — About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches); [GitLab Docs — Merge request approval policies](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/)

### Cited Findings
- **[Sertifikasi/resmi badan]** ISTQB CTFL v4.0 §5.1.3: *entry criteria* = prasyarat memulai aktivitas (ketersediaan orang, tool, environment, test data, budget, waktu; ketersediaan testware; initial quality level mis. semua smoke test pass); *exit criteria* = apa yang harus tercapai untuk menyatakan aktivitas selesai (tingkat coverage, jumlah unresolved defect, defect density, jumlah failed test, planned tests tereksekusi, static testing dilakukan, semua defect dilaporkan). Entry/exit **harus didefinisikan per test level** dan berbeda sesuai tujuan. — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Sertifikasi/resmi badan]** ISTQB §5.1.3 juga menyatakan kehabisan waktu/budget dapat menjadi exit criteria yang sah **hanya bila pemangku kepentingan meninjau dan menerima risikonya**; di Agile, exit criteria sering disebut **Definition of Done** (metrik objektif untuk item yang dapat dirilis) dan entry criteria disebut **Definition of Ready**. — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Sertifikasi/resmi badan]** ISTQB §5.3.1 membedakan test monitoring (mengumpulkan informasi untuk menilai progress dan terpenuhinya exit criteria) dari test control (memberikan directive: reprioritisasi test saat risiko menjadi isu, evaluasi ulang entry/exit, sesuaikan jadwal, tambah sumber daya). — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Praktik industri / opini]** Google Testing Blog (2020-08-07) menyatakan **tidak ada angka coverage ideal universal**; faktor penentunya adalah business impact/criticality, frekuensi perubahan kode, usia/ kompleksitas kode. Panduan internal Google: 60% *acceptable*, 75% *commendable*, 90% *exemplary*, tetapi mereka menolak mandat top-down. — [Google Testing Blog — Code Coverage Best Practices](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html)
- **[Praktik industri / opini]** Google yang sama: mengejar 100% memberi *false sense of security* dan memboroskan cycle serta utang pemeliharaan test bernilai rendah; **apa yang tidak tercakup lebih bermakna** daripada angka yang tercakup; per-commit coverage 99% dianggap reasonable dengan 90% sebagai batas bawah; gate deployment diperbolehkan tetapi hati-hati jangan jadi checkbox; mutation testing lebih baik untuk menilai kualitas assertion; coverage agregat unit + integration/E2E lebih penting daripada unit saja. — [Google Testing Blog — Code Coverage Best Practices](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html)
- **[Sertifikasi/resmi badan]** ISTQB CTFL v4.0 §4.3.1–4.3.2: 100% statement coverage tidak menjamin decision logic maupun defect yang bergantung pada data teruji; **branch coverage subsumes statement coverage** (100% branch ⇒ 100% statement, tidak berlaku sebaliknya). — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Dokumentasi resmi vendor/proyek]** GitHub branch protection: required status checks harus berstatus *successful, skipped, atau neutral* sebelum perubahan dapat masuk branch terlindungi; mode *strict* mensyaratkan branch up-to-date dengan base; merge queue menjalankan ulang required checks terhadap target terbaru; GitHub memperingatkan agar **nama job unik lintas workflow** supaya status check tidak ambigu; tersedia pula "require deployments to succeed before merging". — [GitHub Docs — About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- **[Dokumentasi resmi vendor/proyek]** GitLab: kebijakan approval dievaluasi setelah CI scanning job selesai berdasarkan artifact report; bila aturan invalid/tidak dapat dievaluasi, approval tetap diwajibkan (default `fail: closed`); scan yang gagal/dibatalkan tanpa report memicu approval; artefak harus ada untuk source **dan** target branch; disarankan scan di default branch sebelum kebijakan diterapkan dan konfigurasi scanner konsisten. — [GitLab Docs — Merge request approval policies](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/)
- **[Dokumentasi resmi vendor/proyek]** k6: threshold gagal ⇒ **exit code non-zero**, sehingga dapat langsung memblokir pipeline; `checks` saja tidak mengubah exit status. — [Grafana k6 Docs — Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/)
- **[Dokumentasi resmi vendor/proyek]** Pact: `can-i-deploy` dipasang pada consumer PR pipeline dengan webhook yang memicu provider verification saat pact berubah; `--retry-while-unknown` dapat menunggu hasil verifikasi; verifikasi terikat pada **konten pact**, bukan versi aplikasi, sehingga data acak akan memicu revisi kontrak baru. — [Pact Docs — Pact Nirvana Step 6](https://docs.pact.io/pact_nirvana/step_6)
- **[Dokumentasi resmi vendor/proyek]** Playwright: retries **tidak aktif secara default**; hasil dikategorikan `passed` (lolos di run pertama), `flaky` (gagal lalu lolos saat retry), dan `failed` (gagal di semua retry); `testInfo.retry` tersedia; isolasi test lebih dianjurkan daripada serial mode. — [Playwright Docs — Retries](https://playwright.dev/docs/test-retries)
- **[Dokumentasi resmi vendor/proyek]** Playwright Trace Viewer merekam trace saat first retry (konfigurasi bawaan yang didokumentasikan: retries 2 di CI, 0 lokal) dan menyediakan DOM snapshot untuk inspeksi. — [Playwright Docs — Trace viewer](https://playwright.dev/docs/trace-viewer-intro)
- **[Standar resmi]** 29119-3:2021 Klausul 8.5 *Test data requirements* mencakup description, responsibility, period needed, **resetting needs**, **archiving or disposal**; Klausul 8.7 dan 8.8 menstandarisasi *test data readiness report* dan *test environment readiness report*. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Sertifikasi/resmi badan]** ISTQB §5.4: configuration item diidentifikasi unik, version-controlled, dan saling direlasikan; baseline memungkinkan reproduksi hasil test sebelumnya. — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Praktik industri / opini]** Google SMURF (2024): reliability berarti test hanya gagal saat masalah nyata; flaky membuang waktu developer dan biaya rerun. — [Google Testing Blog — SMURF](https://testing.googleblog.com/2024/10/?m=0)

### Inferences
- **[Inferensi]** Urutan gate yang disarankan untuk PR: static analysis/unit → integration + contract (`can-i-merge`) → E2E smoke → security/accessibility scan → required status checks → review/approval; lalu sebelum deploy: `can-i-deploy --to-environment {{env}}` + k6 threshold + post-deploy synthetic/observability check. Ini turunan dari [GitHub Docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), [GitLab Docs](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/), [Pact Docs](https://docs.pact.io/pact_nirvana/step_6), dan [k6 Docs](https://grafana.com/docs/k6/latest/using-k6/thresholds/).
- **[Inferensi]** Kebijakan flaky yang dapat dipertahankan: (1) catat `flaky` sebagai metrik terpisah, jangan ikut dihitung `passed`; (2) karantina test ke `{{quarantine_suite}}` dengan tiket `{{incident_id}}` dan batas waktu `{{flake_fix_sla}}`; (3) retry hanya sebagai penyerap sementara, bukan perbaikan; (4) perbaiki akar penyebab dengan isolasi state, auto-waiting, data unik, dan penghapusan `waitForTimeout`; (5) jadikan `flake_budget = 0` untuk gate rilis. — [Playwright Docs — Retries](https://playwright.dev/docs/test-retries); [Playwright Docs — Actionability](https://playwright.dev/docs/actionability); [Google SMURF](https://testing.googleblog.com/2024/10/?m=0)
- **[Inferensi]** Test data management minimum: data sintetik/ter-masking, `{{test_data_id}}` unik per test, fixture dengan teardown, `resetting needs` terdokumentasi, `archiving or disposal` sesuai kebijakan retensi, readiness report sebelum eksekusi, dan **tanpa data acak di kontrak Pact**. — [ISO 29119-3:2021 Klausul 8.5/8.7](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [Pact Docs](https://docs.pact.io/pact_nirvana/step_6); [ISTQB §5.4](https://tbok.istqb.org/view-pdf/id/2)
- **[Inferensi]** Coverage target yang tidak menyesatkan: gate pada **kode yang berubah** (diff/per-commit) dengan ambang `{{new_code_coverage_threshold}}`, bukan mandat 100% repositori; tambahkan requirement coverage dan risk coverage, serta mutation testing pada modul kritikal. — [Google Testing Blog 2020](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html); [ISTQB §4.3.1–4.3.2](https://tbok.istqb.org/view-pdf/id/2)

### Gaps
- Angka prevalensi flaky test di Google (mis. "1,5% test flaky, 16% memiliki flakiness") hanya ditemukan pada slide kursus pihak ketiga, bukan pada primer Google; angka tersebut **sengaja tidak dipakai**. — [Google Testing Blog — SMURF](https://testing.googleblog.com/2024/10/?m=0); [Playwright Docs — Retries](https://playwright.dev/docs/test-retries)
- DORA/ISTQB tidak memberi ambang numerik untuk pass rate, defect density, atau flake budget; semua ambang di template adalah placeholder keputusan lokal. — [DORA — Software delivery performance metrics](https://dora.dev/guides/dora-metrics/); [ISTQB CTFL v4.0.1 §5.3.1](https://tbok.istqb.org/view-pdf/id/2)
- GitLab `fallback_behavior: fail: open` tersedia, tetapi saya tidak menemukan panduan resmi yang menetapkan kapan penggunaannya diperbolehkan untuk sistem regulasi; keputusan itu harus menjadi exceptions yang terdokumentasi dengan persetujuan risiko. — [GitLab Docs — Merge request approval policies](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/)

## KQ6 — Metrik yang bermakna vs metrik yang menyesatkan

### Takeaway
Metrik yang bermakna mengukur **outcome** (defect yang lolos, waktu pulih, stabilitas perubahan) dan dipasangkan dalam satu set yang memiliki tension sehat; metrik yang menyesatkan mengukur **aktivitas** lalu dijadikan target (Goodhart's law). DORA per 2026 memakai **lima** metrik, bukan lagi "four keys". — [DORA — Software delivery performance metrics](https://dora.dev/guides/dora-metrics/); [Google Testing Blog — Code Coverage Best Practices](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html); [ISTQB CTFL v4.0 §5.3.1](https://tbok.istqb.org/view-pdf/id/2)

### Cited Findings
- **[Praktik industri / opini]** DORA (guide diperbarui 2026-01-05) kini memakai model **lima metrik**: *change lead time*, *deployment frequency*, *failed deployment recovery time* (throughput), serta *change fail rate* dan *deployment rework rate* (instability). *Change fail rate* = rasio deployment yang memerlukan intervensi segera (rollback/hotfix); *deployment rework rate* = rasio deployment tidak terencana akibat insiden produksi. — [DORA — Software delivery performance metrics](https://dora.dev/guides/dora-metrics/)
- **[Praktik industri / opini]** DORA menyatakan speed dan stability **bukan trade-off** (berkorelasi pada kebanyakan tim), metrik sebaiknya diukur **per aplikasi/services** bukan digabung lintas tim, serta berfungsi sebagai *leading indicator* bagi kinerja organisasi dan *lagging indicator* bagi praktik delivery. — [DORA — Software delivery performance metrics](https://dora.dev/guides/dora-metrics/)
- **[Praktik industri / opini]** DORA mendaftar *common pitfalls*: menjadikan metrik sebagai goal (Goodhart's law), "one metric to rule them all", memakai industri sebagai alasan tidak berubah, perbandingan disparat (mobile app vs mainframe), ownership tersilo, kompetisi antar-tim, dan fokus pada pengukuran sampai mengabaikan perbaikan. — [DORA — Software delivery performance metrics](https://dora.dev/guides/dora-metrics/)
- **[Praktik industri / opini]** DORA Quick Check 2019 mendefinisikan *lead time for changes* sebagai waktu dari **code committed** hingga **code successfully running in production**. — [DORA — Quick Check 2019 results](https://dora.dev/quickcheck/2019/results/)
- **[Praktik industri / opini]** Sejarah metrik DORA mencatat *change failure rate* (persentase deployment yang memerlukan hotfix/rollback) dipakai sebagai proksi jumlah *rework* yang harus dilakukan tim. — [DORA — A history of DORA's software delivery metrics](https://dora.dev/insights/dora-metrics-history/)
- **[Sertifikasi/resmi badan]** ISTQB CTFL v4.0 §5.3.1 mendaftar metrik: project progress, test progress (test case run/not run, passed/failed, execution time), product quality (availability, response time, mean time to failure), defect (jumlah & prioritas defect found/fixed, defect density, **defect detection percentage**), risk (residual risk level), coverage (requirements coverage, code coverage), dan cost. — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Sertifikasi/resmi badan]** ISTQB CT-ATLaS Body of Knowledge v2.0 membedakan metrik *phase containment* dari **Defect Detection Percentage (DDP)**: DDP berfokus pada suatu *test level*, sedangkan phase containment pada suatu *working step* dan hanya defect yang dibuat di step itu. — [ISTQB — CT-ATLaS BoK v2.0](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CT-ATLaS_Body-of-Knowledge_v2.0.pdf)
- **[Sertifikasi/resmi badan]** ISTQB CTAL-TM/CTAL-TTA memakai DDP sebagai *test effectiveness measure* untuk memilih fase yang perlu ditingkatkan. — [ISTQB TBOK — Exam questions TA-5.3.1](https://tbok.istqb.org/exam-questions?lo=TA-5.3.1&syllabus_id=7&q=defect+report); [ISTQB — CTAL-TTA Syllabus v4.0](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB-CTAL-TTA_Syllabus_v4.0.pdf)
- **[Praktik industri / opini]** Google (2020): coverage tinggi **tidak menjamin** kualitas test coverage; 100% menciptakan false sense of security dan technical debt dari test bernilai rendah; coverage rendah menjamin banyak area tidak teruji otomatis; tidak ada angka ideal universal. — [Google Testing Blog — Code Coverage Best Practices](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html)
- **[Sertifikasi/resmi badan]** ISTQB CTFL §4.3.1: 100% statement coverage tidak menjamin seluruh decision logic teruji dan tidak menangkap defect yang data-dependent. — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Standar resmi]** 29119-3:2021 Klausul 7.4.6 dan 7.4.7 menempatkan *test measures* dan **residual risks** di dalam Test Completion Report; Klausul 6.2.9 menempatkan *measuring the value of testing* di Test Policy. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Praktik industri / opini]** DORA 2024 menemukan adopsi AI menaikkan produktivitas/flow/kepuasan individu tetapi menurunkan **stability dan throughput**; small batch sizes dan robust testing tetap krusial. — [DORA — 2024 Report](https://dora.dev/research/2024/dora-report/)

### Inferences
- **[Inferensi]** Metrik yang **bermakna** (pasangkan minimal satu dari tiap kelompok): *outcome produksi* = change fail rate, deployment rework rate, failed deployment recovery time; *efektivitas pengujian* = DDP / defect escape rate, defect density pada area kritikal, residual risk level; *kecepatan feedback* = change lead time, durasi pipeline ke keputusan merge; *kesehatan suite* = flaky rate, duration p95, test yang diskip; *cakupan risiko* = requirements/acceptance-criteria coverage untuk `{{critical_requirements}}`. — [DORA Guides](https://dora.dev/guides/dora-metrics/); [ISTQB §5.3.1](https://tbok.istqb.org/view-pdf/id/2); [ISO 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Inferensi]** **Defect escape rate** tidak saya temukan sebagai istilah normatif di primer yang diverifikasi; ia lazim dipakai sebagai komplemen DDP, yaitu `defect ditemukan setelah test level / (defect ditemukan pada level tersebut + defect yang lolos)`. Definisi operasional dan denominator **wajib** ditulis di test plan agar tidak berubah-ubah. — [ISTQB CT-ATLaS BoK v2.0](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CT-ATLaS_Body-of-Knowledge_v2.0.pdf); [ISTQB §5.3.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Inferensi]** Metrik yang **menyesatkan**: pass rate 100% tanpa denominator jumlah test yang diskip; jumlah test case sebagai proxy kualitas; 100% line coverage sebagai tujuan; jumlah bug yang ditemukan sebagai KPI individu (mendorong split bug); velocity test execution tanpa defect escape rate; perbandingan DORA lintas aplikasi yang sangat berbeda; satu metrik tunggal sebagai target tahunan. — [DORA pitfalls](https://dora.dev/guides/dora-metrics/); [Google 2020](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html); [ISTQB §4.3.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Inferensi]** Karena DORA 2026 sudah lima metrik, laporan yang masih menyebut "four keys" perlu dicatat sebagai terminologi lama; MTTR kini diposisikan ulang menjadi *failed deployment recovery time*. — [DORA — Software delivery performance metrics](https://dora.dev/guides/dora-metrics/)

### Gaps
- Saya tidak menemukan definisi kanonik **defect escape rate** pada halaman primer ISTQB/ISO yang terbuka publik; formula di atas adalah inferensi dari DDP dan harus ditetapkan secara lokal. — [ISTQB CT-ATLaS BoK v2.0](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CT-ATLaS_Body-of-Knowledge_v2.0.pdf); [ISTQB CTFL v4.0.1 §5.3.1](https://tbok.istqb.org/view-pdf/id/2)
- Benchmark angka "elite/high/medium/low" DORA tidak dipakai karena DORA guide terbaru justru memperingatkan agar metrik tidak dijadikan target dan tidak dibandingkan lintas konteks. — [DORA — Software delivery performance metrics](https://dora.dev/guides/dora-metrics/); [DORA Quick Check 2019](https://dora.dev/quickcheck/2019/results/)
- Tidak ada sumber primer yang memberi ambang pass rate atau defect density universal; keduanya kontekstual. — [ISTQB CTFL v4.0.1 §5.3.1](https://tbok.istqb.org/view-pdf/id/2); [DORA — Common pitfalls](https://dora.dev/guides/dora-metrics/)

## KQ7 — Risk-based testing, keterlacakan, dan pelaporan

### Takeaway
Risk-based testing bukan sekadar memberi warna pada risk matrix; ia **menentukan** scope, level, jenis, teknik, coverage, estimasi, urutan eksekusi, dan residual risk yang dilaporkan. Pelaporan yang benar memisahkan *test status report* (periode tertentu, untuk kontrol) dari *test completion report* (penutupan, untuk keputusan rilis). — [ISTQB CTFL v4.0 §5.2 & §5.3.2](https://tbok.istqb.org/view-pdf/id/2); [ISO/IEC/IEEE 29119-3:2021 Klausul 7.2.6/7.3/7.4](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)

### Cited Findings
- **[Sertifikasi/resmi badan]** ISTQB CTFL v4.0 §5.2: *test approach* yang memilih, memprioritaskan, dan mengelola aktivitas berdasarkan risk analysis dan risk control disebut **risk-based testing**; risiko dikarakterisasi oleh *likelihood* dan *impact*, dan *risk level* adalah ukurannya. — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Sertifikasi/resmi badan]** ISTQB §5.2.2 membedakan **project risks** (organisasi, orang, teknis, supplier; berdampak pada jadwal/budget/scope) dan **product risks** (missing/wrong functionality, perhitungan salah, runtime error, response time buruk, UX buruk, kerentanan keamanan; berdampak pada pengguna, pendapatan, reputasi, hingga sanksi). — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Sertifikasi/resmi badan]** ISTQB §5.2.3: product risk analysis = identifikasi + assessment (kategorisasi, likelihood, impact, level, prioritas, penanganan), dapat kuantitatif (likelihood × impact) atau kualitatif (risk matrix); hasilnya dipakai untuk menentukan scope, test levels/types, teknik dan coverage, estimasi effort, **prioritas menemukan defect kritis lebih awal**, serta aktivitas di luar testing untuk menurunkan risiko. — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Sertifikasi/resmi badan]** ISTQB §5.1.5 memprioritaskan eksekusi berdasarkan risiko, coverage, atau prioritas requirement, dengan mempertimbangkan dependensi dan ketersediaan sumber daya. — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Standar resmi]** 29119-3:2021 Klausul 7.2.6 menempatkan **Risk register** di dalam Test Plan; Klausul 7.3.7 (*New and changed risks*) di Test Status Report; Klausul 7.4.7 (*Residual risks*) di Test Completion Report; Klausul 8.11.8 (*Risk*) di Test Incident Report. Dengan demikian risiko hadir di empat artefak berbeda. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** 29119-3:2021 Klausul 7.3 *Test status report* memuat reporting period, progress against test plan, factors blocking progress, test measures, new/changed risks, dan planned testing; Klausul 7.4 *Test completion report* memuat summary, deviations, completion evaluation, blocking factors, measures, residual risks, deliverables, reusable assets, lessons learned. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Sertifikasi/resmi badan]** ISTQB §5.3.2: test progress report memuat test period, progress (ahead/behind schedule) beserta deviasi, impediments & workarounds, test metrics, risiko baru/berubah, dan rencana periode berikutnya; test completion report memuat test summary, evaluasi kualitas terhadap test plan (tujuan & exit criteria), deviasi dari rencana, impediments, metrik, **unmitigated risks / defects not fixed**, dan lessons learned. Audiens berbeda menentukan formalitas dan frekuensi. — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Sertifikasi/resmi badan]** ISTQB §5.3.3 mencantumkan pilihan kanal status: komunikasi verbal, **dashboard (CI/CD dashboards, task boards, burn-down charts)**, kanal elektronik, dokumentasi online, dan formal test reports; tim terdistribusi cenderung membutuhkan komunikasi lebih formal. — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Sertifikasi/resmi badan]** ISTQB §1.5.2 *Whole Team Approach*: setiap anggota dengan keahlian yang memadai dapat mengerjakan tugas apa pun dan **semua orang bertanggung jawab atas kualitas**; tester berkolaborasi dengan perwakilan bisnis untuk acceptance test dan dengan developer untuk menyepakati test strategy serta pendekatan otomasi. ISTQB mencatat konteks safety-critical mungkin tetap membutuhkan independensi tinggi. — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Praktik industri / opini]** DORA 2024 menegaskan *user-centricity* sebagai pendorong utama kualitas produk dan menekankan pendekatan eksperimen: tetapkan baseline, rumuskan hipotesis, ukur dampak secara iteratif. — [DORA — 2024 Report](https://dora.dev/research/2024/dora-report/)

### Inferences
- **[Inferensi]** Risk register minimum: `{{risk_id}}`, `{{risk_category}}` (project/product), `{{likelihood}}`, `{{impact}}`, `{{risk_level}}`, `{{mitigation_test_type}}`, `{{linked_test_case_ids}}`, `{{owner}}`, `{{residual_risk_after_testing}}`, `{{acceptance_decision}}`. Tanpa dua kolom terakhir, Test Completion Report tidak dapat menjawab "risiko apa yang masih dibawa ke produksi". — [ISTQB §5.2](https://tbok.istqb.org/view-pdf/id/2); [ISO 29119-3:2021 Klausul 7.2.6/7.4.7](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Inferensi]** Pelaporan yang efektif: *Test Status Report* untuk keputusan **test control** (reprioritisasi, tambah resource, ubah jadwal); *Test Completion Report / Test Summary Report* untuk keputusan **rilis** (exit criteria terpenuhi atau tidak + persetujuan risiko); dashboard CI/CD untuk status operasional tim. Ketiganya tidak boleh disatukan menjadi satu dokumen tunggal yang kehilangan periode dan audiens. — [ISTQB §5.3.1–5.3.3](https://tbok.istqb.org/view-pdf/id/2); [ISO 29119-3:2021 Klausul 7.3–7.4](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Inferensi]** "QA sebagai gerbang terakhir" bertentangan langsung dengan whole-team approach dan shift-left; QA/tester berperan sejak review acceptance criteria dan penyusunan test strategy, bukan hanya mengeksekusi suite di akhir. — [ISTQB §1.5.2 & §2.1.5](https://tbok.istqb.org/view-pdf/id/2)

### Gaps
- Format laporan harian/status harian, struktur BRD/FSD, dan desain arsitektur/UI sengaja tidak dibahas (topik peneliti lain); catatan ini hanya memakai "periode pelaporan yang ditetapkan di Test Plan". — [ISO/IEC/IEEE 29119-3:2021 Klausul 7.2.5/7.3.3](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- ISTQB menyebut safety-critical sebagai pengecualian whole-team approach, tetapi tidak memberi ambang kuantitatif kapan independensi wajib; keputusan itu bersifat kontekstual/regulatori. — [ISTQB CTFL v4.0.1 §1.5.2](https://tbok.istqb.org/view-pdf/id/2)

## KQ8 — Template artefak pengujian siap pakai

### Takeaway
Satu template utama di bawah menggabungkan **Test Plan (7.2) + Test Strategy (7.2.7) + Test Case Specification (8.3) + Test Incident Report (8.11) + Test Status Report (7.3) + Test Completion Report/Test Summary Report (7.4)** dalam satu dokumen bertanda *tailored conformance*, sehingga cocok untuk tim produk tanpa harus memelihara enam file terpisah. — [ISO/IEC/IEEE 29119-3:2021 Klausul 4.1](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)

### Cited Findings
- **[Standar resmi]** Penggabungan beberapa dokumen menjadi satu dokumen diizinkan secara eksplisit oleh Klausul 4.1 29119-3:2021, selama organisasi menyatakan *tailored conformance* dan mencatat subset dokumentasi yang diklaim. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** Urutan section template utama mengikuti daftar isi Klausul 5.2, 6.2, 7.2, 7.3, 7.4, 8.2–8.11 standar yang sama. — [Pratinjau resmi ISO/IEC/IEEE 29119-3:2021 (PDF)](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Sertifikasi/resmi badan]** Field defect report pada template incident mengikuti ISTQB CTFL v4.0 §5.5. — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2?page=56&search=defect%20report&highlight=5.5)
- **[Dokumentasi resmi vendor/proyek]** Blok quality gate mengikuti mekanisme required status checks GitHub, approval policies GitLab, `can-i-deploy` Pact, dan threshold k6. — [GitHub Docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches); [GitLab Docs](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/); [Pact Docs](https://docs.pact.io/pact_nirvana/step_6); [k6 Docs](https://grafana.com/docs/k6/latest/using-k6/thresholds/)

### Template utama — Test Plan & Test Strategy + artefak turunan

```markdown
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
```

### Template quality gate CI — GitHub Actions

```yaml
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
```

> Catatan konfigurasi (bukan kode): daftar `{{UNIQUE_CHECK_NAME_*}}` harus **unik lintas workflow** dan didaftarkan sebagai required status checks pada branch protection; aktifkan *strict* atau merge queue sesuai kebijakan; artefak laporan dipakai sebagai bukti audit. Sumber: [GitHub Docs — About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), [GitHub Docs — workflow artifacts](https://docs.github.com/zh/actions/tutorials/store-and-share-data), [k6 Docs](https://grafana.com/docs/k6/latest/using-k6/thresholds/), [Pact Docs](https://docs.pact.io/pact_nirvana/step_6).

### Template quality gate CI — GitLab CI

```yaml
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
```

```yaml
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
```

> Sumber: [GitLab Docs — Unit test reports](https://docs.gitlab.com/ci/testing/unit_test_reports/), [GitLab Docs — Merge request approval policies](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/), [Pact Docs — can-i-deploy](https://docs.pact.io/pact_nirvana/step_6).

### Inferences
- **[Inferensi]** Template utama sengaja memakai **satu tabel per artefak** agar setiap baris dapat menjadi *record* di test management tool, spreadsheet, atau issue tracker—sesuai Klausul 4.1 yang mengizinkan dokumentasi elektronik. — [ISO/IEC/IEEE 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Inferensi]** Placeholder `{{REQUIREMENT_ID}}` hanya menjadi kunci tautan; isi dan struktur dokumen asal requirement tidak dijelaskan di sini sesuai batas scope topik. — [ISTQB CTFL v4.0 §1.4.4](https://tbok.istqb.org/view-pdf/id/2)

### Gaps
- Template di atas adalah **tailored**, bukan *full conformance*: Annex A (daftar `shall` per information item) tidak tersedia publik, sehingga organisasi yang butuh klaim *full conformance* wajib memeriksa salinan berlisensi. — [ISO/IEC/IEEE 29119-3:2021 Klausul 4.1](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- Konfigurasi `fallback_behavior.fail: closed` dan `vulnerabilities_allowed` memerlukan tier GitLab Ultimate; versi/tier harus dicek terhadap dokumentasi yang berlaku saat implementasi. — [GitLab Docs — Merge request approval policies](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/)

## KQ9 — Checklist review

### Takeaway
Checklist ini dipakai saat mereview **Test Plan, Test Case, bug report, dan konfigurasi quality gate** sebelum rilis. — [ISO/IEC/IEEE 29119-3:2021 Klausul 5.2/7.2/7.4](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [ISTQB CTFL v4.0 §5.1.3](https://tbok.istqb.org/view-pdf/id/2)

### Cited Findings
- **[Standar resmi]** Cek konformasi: apakah klaim *full/tailored conformance* dan justifikasi tailoring tercatat? — [ISO/IEC/IEEE 29119-3:2021 Klausul 4.1](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** Cek kelengkapan common information: unique ID, issuing organization, approval authority, change history, status, introduction, scope, references, glossary. — [ISO/IEC/IEEE 29119-3:2021 Klausul 5.2](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** Cek Test Plan memuat context, assumptions/constraints, stakeholders, communication, risk register, test strategy, activities/estimates, staffing, schedule. — [ISO/IEC/IEEE 29119-3:2021 Klausul 7.2](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** Cek Test Strategy mencantumkan levels/types, retesting & regression, teknik desain + completion criteria, test data, environment, tool, dan deliverable. — [ISO/IEC/IEEE 29119-3:2021 definisi 3.25](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** Cek readiness report test data & environment sebelum eksekusi, termasuk resetting needs dan archiving/disposal. — [ISO/IEC/IEEE 29119-3:2021 Klausul 8.5–8.8](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** Cek Completion Report memuat residual risks, deviations, test measures, reusable assets, dan lessons learned—bukan hanya ringkasan pass/fail. — [ISO/IEC/IEEE 29119-3:2021 Klausul 7.4](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Sertifikasi/resmi badan]** Cek entry/exit criteria per test level, definisi DoD/DoR, dan apakah exit karena waktu/budget memiliki persetujuan risiko tertulis. — [ISTQB CTFL v4.0 §5.1.3](https://tbok.istqb.org/view-pdf/id/2)
- **[Sertifikasi/resmi badan]** Cek setiap test case punya prekondisi, data uji, langkah, expected result; setiap eksekusi punya actual result, pass/fail, dan log; setiap incident punya severity **dan** priority yang terpisah. — [ISTQB CTFL v4.0 §5.5](https://tbok.istqb.org/view-pdf/id/2?page=56&search=defect%20report&highlight=5.5); [ISO 29119-3:2021 Klausul 8.9–8.11](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Sertifikasi/resmi badan]** Cek traceability `requirement → risk → test case → result → incident → residual risk` dan version-control pada semua configuration item. — [ISTQB CTFL v4.0 §1.4.4 & §5.4](https://tbok.istqb.org/view-pdf/id/2)
- **[Sertifikasi/resmi badan]** Cek prioritas eksekusi berbasis risiko dan dependensi antar-test sudah dipertimbangkan. — [ISTQB CTFL v4.0 §5.1.5](https://tbok.istqb.org/view-pdf/id/2)
- **[Dokumentasi resmi vendor/proyek]** Cek required status checks unik lintas workflow, berstatus successful/skipped/neutral, dan kebijakan strict/merge queue sesuai risiko integrasi. — [GitHub Docs — About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- **[Dokumentasi resmi vendor/proyek]** Cek artefak scanner tersedia di source **dan** target branch, scanner tidak dihapus dari MR, dan fallback tidak sengaja `fail: open`. — [GitLab Docs — Merge request approval policies](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/)
- **[Dokumentasi resmi vendor/proyek]** Cek `can-i-deploy` dijalankan menjelang deploy (bukan hanya saat verifikasi awal) dan pact bebas data acak. — [Pact Docs — Step 6](https://docs.pact.io/pact_nirvana/step_6)
- **[Dokumentasi resmi vendor/proyek]** Cek performance gate memakai **thresholds** (bukan hanya `checks`) agar exit code benar-benar memblokir pipeline. — [Grafana k6 Docs — Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/)
- **[Dokumentasi resmi vendor/proyek]** Cek metrik flaky dilaporkan terpisah dari passed dan trace tersimpan untuk first retry. — [Playwright Docs — Retries](https://playwright.dev/docs/test-retries); [Playwright Docs — Trace viewer](https://playwright.dev/docs/trace-viewer-intro)
- **[Standar resmi]** Cek target aksesibilitas mengunci versi WCAG (2.2) dan level konformasi, serta mencantumkan evaluasi manusia selain automated scan. — [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- **[Dokumentasi resmi vendor/proyek]** Cek requirement keamanan dirujuk dengan format berversi `v5.0.0-...` dan WSTG mengunci Latest atau Stable v4.2. — [OWASP ASVS v5.0.0](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/README.md); [OWASP WSTG](https://wstg.owasp.org/latest/1-About/)
- **[Praktik industri / opini]** Cek metrik tidak dijadikan target tunggal dan diukur per aplikasi/service. — [DORA — Software delivery performance metrics](https://dora.dev/guides/dora-metrics/)

### Inferences
- **[Inferensi]** Checklist sebaiknya dijalankan dua kali: saat **review Test Plan** (sebelum implementasi test) dan saat **review Test Completion Report** (sebelum keputusan rilis), dengan bukti berupa `{{CI_RUN_URL}}`, bukan sekadar centang manual. — [ISTQB §5.3.1–5.3.3](https://tbok.istqb.org/view-pdf/id/2); [GitHub Docs](https://docs.github.com/zh/actions/tutorials/store-and-share-data)

### Gaps
- Checklist tidak mencakup review BRD/FSD, desain arsitektur/UI, struktur repo, API versioning, atau laporan harian sesuai pembagian topik peneliti lain; batas ini ditetapkan oleh koordinator riset dan tercermin dalam [ISO/IEC/IEEE 29119-3:2021 Klausul 4.1 tentang tailoring](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf).

## KQ10 — Anti-pattern yang sering terjadi

### Takeaway
Hampir semua anti-pattern di bawah bermuara pada satu kesalahan yang sama: **mengoptimalkan sinyal yang mudah diukur (jumlah test, pass rate, coverage, kecepatan merge) sampai sinyal itu berhenti berkorelasi dengan risiko produksi**. — [DORA — Common pitfalls](https://dora.dev/guides/dora-metrics/); [Google Testing Blog — Code Coverage Best Practices](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html)

### Cited Findings
- **[Praktik industri / opini — blog resmi Google]** **Tes yang selalu hijau / assertion kosong**: Google (2020) memperingatkan copy-paste test demi menaikkan angka coverage dan menyarankan mutation testing untuk memeriksa apakah assertion benar-benar menangkap failure; tes yang dieksekusi belum tentu diuji dengan benar. — [Google Testing Blog — Code Coverage Best Practices](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html)
- **[Praktik industri / opini]** **Mengejar 100% line coverage**: Google menyatakan tidak ada angka ideal universal, 100% memberi false sense of security dan technical debt; ISTQB menambahkan 100% statement coverage tidak menjamin decision logic maupun defect data-dependent. — [Google Testing Blog 2020](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html); [ISTQB CTFL v4.0 §4.3.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Praktik industri / opini]** **E2E berlebih**: pyramid tetap menyarankan lebih banyak unit daripada integration dan lebih banyak integration daripada E2E; Google SMURF mencatat E2E menaikkan fidelity tetapi mengorbankan Speed, Maintainability, Utilization, dan Reliability. — [Google Testing Blog — SMURF](https://testing.googleblog.com/2024/10/?m=0); [ISTQB CTFL v4.0 §5.1.6](https://tbok.istqb.org/view-pdf/id/2)
- **[Sertifikasi/resmi badan]** **QA sebagai gerbang terakhir**: whole-team approach menyatakan semua anggota bertanggung jawab atas kualitas dan tester terlibat sejak acceptance criteria serta penyusunan test strategy; shift-left menambahkan review spesifikasi, test sebelum kode, CI, dan static analysis. — [ISTQB CTFL v4.0 §1.5.2 & §2.1.5](https://tbok.istqb.org/view-pdf/id/2)
- **[Sertifikasi/resmi badan]** **Shift-left disalahartikan sebagai "pengujian akhir tidak perlu"**: ISTQB secara eksplisit menyatakan shift-left **tidak berarti** pengujian di akhir SDLC diabaikan. — [ISTQB CTFL v4.0 §2.1.5](https://tbok.istqb.org/view-pdf/id/2)
- **[Praktik industri / opini]** **Flaky test hanya di-retry**: Playwright mengkategorikan `flaky` terpisah dari `passed` dan menganjurkan isolasi test; Google SMURF menyebut retry membuang waktu developer dan biaya resource. — [Playwright Docs — Retries](https://playwright.dev/docs/test-retries); [Google Testing Blog — SMURF](https://testing.googleblog.com/2024/10/?m=0)
- **[Dokumentasi resmi vendor/proyek]** **Quality gate yang bisa dilewati**: GitHub memperingatkan nama job yang sama lintas workflow menyebabkan status check ambigu; GitLab mencatat penghapusan scanner dari MR memicu approval tambahan dan artifact yang hilang membuat kebijakan tidak dapat dievaluasi. — [GitHub Docs — About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches); [GitLab Docs — Merge request approval policies](https://docs.gitlab.com/user/application_security/policies/merge_request_approval_policies/)
- **[Dokumentasi resmi vendor/proyek]** **Performance test tanpa threshold**: `checks` pada k6 tidak mengubah exit status, sehingga pipeline tetap hijau walau SLO dilanggar. — [Grafana k6 Docs — Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/)
- **[Dokumentasi resmi vendor/proyek]** **Contract test dianggap functional test**: Pact memperingatkan penggunaan contract test untuk functional test umum provider menghasilkan test yang rapuh, dan kontrak sebaiknya fokus pada pesan serta data-independent. — [Pact Docs — How Pact works](https://docs.pact.io/getting_started/how_pact_works)
- **[Dokumentasi resmi vendor/proyek]** **Data acak dalam pact / test data tanpa reset**: data acak membuat broker menganggap pact sebagai revisi baru dan memicu webhook berulang; 29119-3:2021 mewajibkan pencatatan resetting needs serta archiving/disposal test data. — [Pact Docs — Step 6](https://docs.pact.io/pact_nirvana/step_6); [ISO/IEC/IEEE 29119-3:2021 Klausul 8.5](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
- **[Standar resmi]** **Laporan tanpa residual risk**: 29119-3:2021 Klausul 7.4.7 dan ISTQB §5.3.2 sama-sama mensyaratkan unmitigated risks/defects not fixed dalam completion report; menghilangkannya membuat keputusan rilis tidak dapat diaudit. — [ISO/IEC/IEEE 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [ISTQB CTFL v4.0 §5.3.2](https://tbok.istqb.org/view-pdf/id/2)
- **[Sertifikasi/resmi badan]** **Tidak ada traceability**: ISTQB §1.4.4 mencatat hilangnya traceability melemahkan evaluasi coverage, analisis dampak perubahan, audit, dan pemahaman laporan. — [ISTQB TBOK — CTFL v4.0.1](https://tbok.istqb.org/view-pdf/id/2)
- **[Praktik industri / opini]** **Tidak ada pengujian/observability di produksi**: DORA memantau change fail rate dan failed deployment recovery time sebagai metrik outcome, dan laporan 2024 mengingatkan robust testing serta small batch sizes tetap krusial; AWS chaos guidance mensyaratkan steady state, alarm, log, dan MTTR terukur saat kegagalan diinjeksikan. — [DORA — Software delivery performance metrics](https://dora.dev/guides/dora-metrics/); [DORA — 2024 Report](https://dora.dev/research/2024/dora-report/); [AWS — Chaos Engineering on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/chaos-engineering-on-aws.pdf)
- **[Praktik industri / opini]** **Metrik dijadikan target tunggal / kompetisi antar-tim**: DORA menyebut Goodhart's law, "one metric to rule them all", perbandingan disparat, ownership tersilo, dan kompetisi sebagai common pitfalls. — [DORA — Software delivery performance metrics](https://dora.dev/guides/dora-metrics/)
- **[Standar resmi]** **Aksesibilitas hanya mengandalkan automated scan**: WCAG 2.2 dirancang untuk diuji dengan kombinasi automated testing **dan** human evaluation, dan bahkan konformasi AAA tidak menjamin aksesibilitas bagi semua pengguna. — [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- **[Dokumentasi resmi vendor/proyek]** **Mengunci versi standar keamanan lama tanpa menyebut versi**: ASVS 5.0.0 memperingatkan identifier requirement dapat berubah antarversi dan menganjurkan format `v<version>-<requirement>`; WSTG `Latest` dan `Stable v4.2` berbeda isi. — [OWASP ASVS v5.0.0](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/README.md); [OWASP WSTG](https://wstg.owasp.org/latest/1-About/)
- **[Sertifikasi/resmi badan]** **Severity disamakan dengan priority**: ISTQB §5.5 dan ISO 29119-3 Klausul 8.11.6–8.11.7 memisahkan keduanya sebagai assessment yang berbeda. — [ISTQB CTFL v4.0 §5.5](https://tbok.istqb.org/view-pdf/id/2?page=56&search=defect%20report&highlight=5.5); [ISO/IEC/IEEE 29119-3:2021](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)

### Inferences
- **[Inferensi]** Anti-pattern tambahan yang merupakan turunan langsung: **pass rate 100% dengan test yang di-skip**, **menghitung jumlah test case sebagai produktivitas**, **mengklaim "sesuai ISO 29119" tanpa menyatakan full/tailored conformance**, **mengklaim "sesuai ISO 29119-14" padahal masih DIS**, dan **menyatukan Test Status Report dengan Test Completion Report** sehingga periode pelaporan dan keputusan rilis tercampur. — [ISO/IEC/IEEE 29119-3:2021 Klausul 4.1 & 7.3–7.4](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf); [ISO — DIS 29119-14](https://www.iso.org/cms/live/live/es/sites/isoorg/contents/data/standard/08/88/88837.html?browse=tc); [ISTQB §5.3.1–5.3.2](https://tbok.istqb.org/view-pdf/id/2); [DORA pitfalls](https://dora.dev/guides/dora-metrics/)

### Gaps
- Daftar anti-pattern di atas tidak mencoba mengkuantifikasi dampak finansial dari masing-masing; tidak ada sumber primer yang memberi angka biaya lintas organisasi untuk 2024–2026. — [DORA — Accelerate State of DevOps Report 2024](https://dora.dev/research/2024/dora-report/); [Google Testing Blog — Code Coverage Best Practices](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html)
- Beberapa anti-pattern (mis. "tes yang selalu hijau") hanya didukung oleh blog resmi Google, bukan oleh standar normatif; karenanya ditandai **[Praktik industri / opini]** dan tidak boleh dipresentasikan sebagai pelanggaran standar. — [Google Testing Blog — Code Coverage Best Practices](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html); [ISO/IEC/IEEE 29119-3:2021 Klausul 4.1](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)
