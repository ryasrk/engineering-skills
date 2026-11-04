# Desain: design doc, HLD/LLD, C4, ADR, UI/UX, dan aksesibilitas

> **Konvensi sitasi & batas ruang lingkup.** Setiap klaim normatif di bawah diberi label asal: **[STANDAR RESMI]** (ISO/IEC/IEEE, W3C Recommendation, OMG formal specification, IETF RFC), **[SPESIFIKASI KOMUNITAS]** (W3C Community Group Final Specification — *bukan* W3C Standard), **[DRAFT W3C]** (Working Draft, belum Recommendation), **[PANDUAN INFORMATIF W3C WAI]** (bukan normatif), **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** (vendor/proyek: arc42, c4model.com, adr.github.io/MADR, Google, Kubernetes, Rust, React, Microsoft, AWS, Material, Apple, USWDS), **[BLOG SEKUNDER — PELENGKAP]**, dan **[INFERENSI PENELITI]**. Nama dokumen + URL lengkap selalu disertakan. Fokus praktik relevan 2024–2026: **ISO/IEC/IEEE 42010:2022**, **WCAG 2.2** (W3C Recommendation 5 Oktober 2023, direpublikasi dengan errata 12 Desember 2024), **WAI-ARIA 1.2** (Recommendation 6 Juni 2023), **MADR 4.0.0** (17 September 2024), **Design Tokens Format Module 2025.10**, **Media Queries Level 5** (Working Draft 19 Februari 2026), **UML 2.5.1** (OMG `formal/17-12-05`, Desember 2017, masih spesifikasi formal yang dirujuk). Catatan ini sengaja **tidak** membahas struktur folder/direktori repositori, struktur project/monorepo, strategi branching, API versioning zero-downtime, BRD, FSD, test plan, maupun laporan harian.

## 1. Apa struktur design doc / RFC engineering yang baik (konteks, tujuan, non-goals, keputusan, alternatif yang ditolak, risiko, rencana migrasi, observability, keamanan, rollout/rollback)?

### Takeaway
Tidak ada satu standar universal yang *mewajibkan* urutan bab design doc: **[STANDAR RESMI]** ISO/IEC/IEEE 42010:2022 hanya menetapkan persyaratan terhadap *Architecture Description* dan sengaja tidak menentukan proses, notasi, atau format ([IEEE SA](https://standards.ieee.org/ieee/42010/6846/)); struktur konkret justru konsisten muncul dari konvensi RFC proyek resmi yang memisahkan motivasi/goals/non-goals, desain, alternatif yang ditolak, risiko, adopsi/migrasi, dan production readiness ([Kubernetes KEP template](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md), [Rust RFC template](https://raw.githubusercontent.com/rust-lang/rfcs/master/0000-template.md), [React RFC template](https://raw.githubusercontent.com/reactjs/rfcs/main/0000-template.md)).

### Cited Findings
- **[STANDAR RESMI]** *IEEE/ISO/IEC 42010-2022, "Software, systems and enterprise — Architecture description"* berstatus **Active Standard**, disetujui 2022-09-21, dipublikasikan 2022-11-07, menggantikan 42010-2011; menetapkan persyaratan struktur/ekspresi AD, ADF, ADL, *architecture viewpoint*, dan *model kind*, **tetapi tidak menentukan proses, metode, model, notasi, teknik, alat, format, atau media** perekaman AD — [IEEE SA, "IEEE/ISO/IEC 42010-2022"](https://standards.ieee.org/ieee/42010/6846/).
- **[PANDUAN KONSEPTUAL RESMI — bukan teks standar]** Edisi 2022 menggeneralisasi *System of Interest* menjadi **Entity of Interest**, mengubah *Architecture Model* menjadi **View Component**, serta memperkenalkan **Stakeholder Perspectives** dan **Architecture Aspects**; model 2011 mendefinisikan *Architecture Rationale* sebagai penjelasan keputusan **dan alternatif yang tidak dipilih** — [ISO/IEC/IEEE 42010 Conceptual Model, "A Conceptual Model of Architecture Description"](http://www.iso-architecture.org/42010/cm/).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** arc42 §1 meminta ringkasan kebutuhan, **3–5 quality goals teratas** dengan skenario konkret, dan tabel stakeholder beserta ekspektasinya; quality goals harus konkret, bukan *buzzword* — [arc42, "1. Introduction and Goals"](https://docs.arc42.org/section-1/).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** arc42 §8 menyarankan *crosscutting concepts* (mis. format log, autentikasi, pola bersama) ditempatkan sekali secara terpusat dan **"DO NOT ATTEMPT to cover all of the topics"** — [arc42, "8. Crosscutting Concepts"](https://docs.arc42.org/section-8/).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** arc42 §9 meminta keputusan penting/mahal/berisiko didokumentasikan bersama rasionalnya, dan §11 meminta daftar risiko serta technical debt berurutan prioritas beserta mitigasinya — [arc42, "9. Architecture Decisions"](https://docs.arc42.org/section-9/); [arc42, "11. Risks and Technical Debt"](https://docs.arc42.org/section-11/).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Template KEP Kubernetes memuat `Summary`, `Motivation` → `Goals` / `Non-Goals`, `Proposal` → `Risks and Mitigations` (secara eksplisit menanyakan *"How will security be reviewed, and by whom? How will UX be reviewed, and by whom?"*), `Design Details`, `Upgrade / Downgrade Strategy`, `Version Skew Strategy`, `Implementation History`, `Drawbacks`, `Alternatives` — [Kubernetes Enhancements, "KEP-NNNN template README"](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** KEP *Production Readiness Review Questionnaire* menambahkan `Feature Enablement and Rollback`, `Rollout, Upgrade and Rollback Planning`, `Monitoring Requirements`, `Dependencies`, `Scalability`, `Troubleshooting`; tujuan PRR dinyatakan sebagai memastikan fitur **"observable, scalable and supportable"** serta **"can be disabled or rolled back"**, dengan pertanyaan *"What specific metrics should inform a rollback?"* dan *"What are other known failure modes?"* — [Kubernetes Enhancements, "KEP-NNNN template README"](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Template RFC Rust: `Summary`, `Motivation` (masalah + use case), `Guide-level explanation` (termasuk *migration guidance*), `Reference-level explanation` (detail teknis + *corner cases*), `Drawbacks` (*"Why should we not do this?"*), `Rationale and alternatives`, `Prior art`, `Unresolved questions`, `Future possibilities` — [rust-lang/rfcs, "0000-template.md"](https://raw.githubusercontent.com/rust-lang/rfcs/master/0000-template.md).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Template RFC React: `Motivation` harus merumuskan **constraints tanpa terlalu terikat pada solusi** agar jika RFC ditolak motivasinya tetap bisa dipakai untuk solusi alternatif; `Drawbacks` menanyakan implementation cost, kompleksitas, dan *cost of migrating existing applications*; tersedia `Adoption strategy`, `How we teach this`, `Unresolved questions` — [reactjs/rfcs, "0000-template.md"](https://raw.githubusercontent.com/reactjs/rfcs/main/0000-template.md).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Portal *Google Engineering Practices Documentation* menyatakan berisi praktik-general lintas bahasa/proyek, termasuk *Code Review Guidelines*, dilisensikan CC-BY 3.0; portal ini **tidak mempublikasikan template design doc internal tersendiri** — [Google, "Engineering Practices Documentation"](https://google.github.io/eng-practices/).
- **[BLOG SEKUNDER — PELENGKAP, BUKAN DASAR]** Artikel *"Design Docs at Google"* kerap dirujuk sebagai gambaran praktik internal, tetapi merupakan tulisan pihak ketiga dan sengaja tidak dijadikan dasar normatif di catatan ini — [Industrial Empathy, "Design docs at Google"](https://www.industrialempathy.com/posts/design-docs-at-google/).

### Inferences
- **[INFERENSI PENELITI]** Struktur minimum yang dapat dipertanggungjawabkan adalah 12 blok: konteks/motivasi → goals & non-goals → stakeholder/concern & quality goals → constraints → keputusan (+ tautan ADR) → alternatif ditolak → model struktural/perilaku/data → keamanan → observability → migrasi & kompatibilitas → rollout/rollback → risiko/open questions. Ini adalah sintesis, bukan mandat standar, dari [IEEE 42010:2022](https://standards.ieee.org/ieee/42010/6846/), [arc42 §1/§9/§11](https://docs.arc42.org/section-9/), [KEP](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md), [Rust RFC](https://raw.githubusercontent.com/rust-lang/rfcs/master/0000-template.md), dan [React RFC](https://raw.githubusercontent.com/reactjs/rfcs/main/0000-template.md).
- **[INFERENSI PENELITI]** Observability dan rollback **bukan lampiran pasca-implementasi**: KEP menempatkannya sebagai syarat *Production Readiness* sebelum status `implementable`, sehingga design doc yang baik memuat nama sinyal/SLI dan pemicu rollback sejak awal ([KEP template](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md)).
- **[INFERENSI PENELITI]** `Non-Goals` dan `Drawbacks` berfungsi sebagai kontrol ruang lingkup sekaligus kejujuran epistemik: memisahkan constraint dari solusi memungkinkan alternatif lain tetap evaluable bila desain ditolak ([React RFC](https://raw.githubusercontent.com/reactjs/rfcs/main/0000-template.md), [Rust RFC](https://raw.githubusercontent.com/rust-lang/rfcs/master/0000-template.md)).
- **[INFERENSI PENELITI]** Rasional + alternatif yang ditolak sebaiknya ditautkan ke *concern* stakeholder, karena 42010 membedakan AD dari arsitektur dan menuntut korespondensi/traceability antar elemen AD ([Conceptual Model](http://www.iso-architecture.org/42010/cm/), [IEEE SA](https://standards.ieee.org/ieee/42010/6846/)).

### Cited Findings (lanjutan): Template utama Design Doc / RFC engineering

````markdown
# {{JUDUL_DESAIN}} — Design Doc / RFC

| Metadata | Nilai |
| --- | --- |
| ID | {{DD-0000}} |
| Status | {{Draft \| Proposed \| Accepted \| Superseded by DD-0000}} |
| Versi & tanggal | {{v0.1}} — {{YYYY-MM-DD}} |
| Pemilik | {{NAMA_PERAN}} |
| Reviewer wajib | {{ARSITEK}}, {{SECURITY}}, {{SRE}}, {{DESAINER_UX}}, {{DATA_OWNER}} |
| Target keputusan | {{TANGGAL_KEPUTUSAN}} |
| Referensi kebutuhan | {{TAUTAN_REQUIREMENT}} |
| Standar yang dipakai | {{ISO/IEC/IEEE 42010:2022}}, {{WCAG 2.2 AA}}, {{LAINNYA}} |

## 1. Ringkasan
{{Satu paragraf: apa yang berubah, untuk siapa, dan mengapa pembaca harus menyetujuinya.}}

## 2. Konteks & motivasi
{{Keadaan saat ini, data/insiden yang memicu, dan dampak bila tidak ada perubahan. Tulis constraints, bukan solusi, agar alternatif lain tetap bisa diusulkan.}}

## 3. Tujuan, non-goals, dan kriteria sukses
- Goals: {{TUJUAN_1}}, {{TUJUAN_2}}, {{TUJUAN_3}}
- Non-goals: {{DI_LUAR_RUANG_LINGKUP_1}}, {{DI_LUAR_RUANG_LINGKUP_2}}
- Kriteria sukses terukur: {{METRIK_1}} dari {{BASELINE_1}} menjadi {{TARGET_1}} pada {{WAKTU_1}}; {{METRIK_2}} ≤ {{AMBANG_2}}

## 4. Stakeholder, concern, dan quality goals
| Stakeholder | Concern | Quality goal (top 3–5) | Skenario terukur |
| --- | --- | --- | --- |
| {{PERAN_1}} | {{CONCERN_1}} | {{KUALITAS_1}} | {{KONDISI_1}} → {{RESPON_1}} dalam {{BATAS_1}} |
| {{PERAN_2}} | {{CONCERN_2}} | {{KUALITAS_2}} | {{KONDISI_2}} → {{RESPON_2}} dalam {{BATAS_2}} |

## 5. Constraints & asumsi
- Teknis: {{CONSTRAINT_TEKNIS}}
- Organisasi/regulasi: {{CONSTRAINT_REGULASI}}
- Asumsi yang bila salah membatalkan desain: {{ASUMSI_KRITIS}}
- Cara memvalidasi asumsi: {{CARA_VALIDASI}}

## 6. Keputusan desain
| ID | Keputusan | Alasan utama | Concern yang dijawab | ADR |
| --- | --- | --- | --- | --- |
| {{D-01}} | {{KEPUTUSAN_1}} | {{ALASAN_1}} | {{CONCERN_1}} | {{ADR-0000}} |
| {{D-02}} | {{KEPUTUSAN_2}} | {{ALASAN_2}} | {{CONCERN_2}} | {{ADR-0000}} |

## 7. Alternatif yang dipertimbangkan dan ditolak
| Opsi | Kelebihan | Kekurangan | Alasan penolakan | Bukti |
| --- | --- | --- | --- | --- |
| {{OPSI_A}} | {{PRO_A}} | {{KONTRA_A}} | {{TOLAK_A}} | {{TAUTAN_BENCHMARK_A}} |
| {{OPSI_B}} | {{PRO_B}} | {{KONTRA_B}} | {{TOLAK_B}} | {{TAUTAN_BENCHMARK_B}} |
| Do nothing | {{PRO_NOL}} | {{KONTRA_NOL}} | {{TOLAK_NOL}} | {{DATA_DAMPAK}} |

## 8. Desain struktural (HLD → LLD ringkas)
- System Context (C4 L1): {{AKTOR_1}} → {{SISTEM_KITA}} → {{SISTEM_EKSTERNAL_1}}
- Container (C4 L2): {{KONTAINER_1}} ({{TEKNOLOGI_1}}), {{KONTAINER_2}} ({{TEKNOLOGI_2}}); protokol {{PROTOKOL_1}}
- Component (C4 L3, hanya yang berisiko/kompleks): {{KOMPONEN_1}} → {{TANGGUNG_JAWAB_1}}, interface {{INTERFACE_1}}
- Batasan zoom: {{BAGIAN_YANG_TIDAK_DIGAMBAR_L4_DAN_ALASANNYA}}
- Diagram: {{TAUTAN_DIAGRAM_C4}}; notasi {{NOTASI}}; pemilik diagram {{PERAN}}; terakhir diverifikasi {{TANGGAL}}

## 9. Model perilaku & data
- Skenario runtime utama: {{USE_CASE_1}} — {{TAUTAN_SEQUENCE_DIAGRAM}}
- Skenario error/exception: {{FAILURE_1}} → deteksi {{SINYAL_1}} → mitigasi {{MITIGASI_1}}
- State machine: {{ENTITAS_1}}: {{STATE_A}} → {{STATE_B}} → {{STATE_C}}
- Model data: entitas {{ENTITAS_1}}({{ATRIBUT_1}}, {{KUNCI_1}}) berelasi {{KARDINALITAS}} dengan {{ENTITAS_2}}; {{TAUTAN_ER_DIAGRAM}}
- Invariants: {{INVARIANT_1}}; kehilangan data yang tidak boleh terjadi: {{DATA_KRITIS}}

## 10. Crosscutting concepts
{{Konsep bersama yang dipakai banyak blok: format log/correlation id, autentikasi-antar-komponen, strategi retry/idempotency, konvensi error. Pilih hanya yang paling dibutuhkan.}}

## 11. Keamanan & privacy (STRIDE)
| Kategori | Ancaman pada desain ini | Kontrol | Pemilik | Status |
| --- | --- | --- | --- | --- |
| Spoofing | {{ANCAMAN_S}} | {{KONTROL_S}} | {{PERAN_S}} | {{OPEN/MITIGATED}} |
| Tampering | {{ANCAMAN_T}} | {{KONTROL_T}} | {{PERAN_T}} | {{OPEN/MITIGATED}} |
| Repudiation | {{ANCAMAN_R}} | {{KONTROL_R}} | {{PERAN_R}} | {{OPEN/MITIGATED}} |
| Information Disclosure | {{ANCAMAN_I}} | {{KONTROL_I}} | {{PERAN_I}} | {{OPEN/MITIGATED}} |
| Denial of Service | {{ANCAMAN_D}} | {{KONTROL_D}} | {{PERAN_D}} | {{OPEN/MITIGATED}} |
| Elevation of Privilege | {{ANCAMAN_E}} | {{KONTROL_E}} | {{PERAN_E}} | {{OPEN/MITIGATED}} |
- Data pribadi diproses: {{KATEGORI_DATA}}; dasar pemrosesan {{DASAR_HUKUM}}; retensi {{RETENSI}}

## 12. Observability & operability
- SLI: {{SLI_1}}, {{SLI_2}}; SLO: {{SLO_1}} ({{JENDELA_1}})
- Log/telemetri: {{SIGNAL_1}}; correlation id {{CORRELATION_ID}}; dashboard {{TAUTAN_DASHBOARD}}
- Cara operator tahu fitur aktif & sehat: {{CARA_OPERATOR_1}}
- Failure mode terdokumentasi: {{FAILURE_1}} → deteksi {{DETEKSI_1}} → diagnosa {{DIAGNOSA_1}} → mitigasi {{MITIGASI_1}}
- Troubleshooting/playbook: {{TAUTAN_PLAYBOOK}}

## 13. Rencana migrasi & kompatibilitas data
- State lama: {{SKEMA_LAMA}}; state baru: {{SKEMA_BARU}}
- Urutan transformasi: {{TAHAP_1}} → {{TAHAP_2}} → {{TAHAP_3}}
- Backfill: {{ESTIMASI_VOLUME}} dalam {{JENDELA_WAKTU}}; estimasi dampak beban {{DAMPAK_BEBAN}}
- Kompatibilitas konsumen data & perilaku: {{KONSUMEN_1}} tetap membaca {{KONTRAK_1}}; validasi {{CARA_VALIDASI_KOMPATIBILITAS}}
- Rekonsiliasi & verifikasi integritas: {{CHECKSUM/COUNT_QUERY}}; ambang gagal {{AMBANG_GAGAL}}
- Rencana pemulihan state bila transformasi gagal: {{PEMULIHAN_STATE}}

## 14. Rollout, rollback, dan dependensi
- Urutan aktivasi: {{GELOMBANG_1}} → {{GELOMBANG_2}} → {{GELOMBANG_3}}; kriteria lanjut {{KRITERIA_LANJUT}}
- Cara menonaktifkan: {{MEKANISME_DISABLE}}; apakah bisa dinonaktifkan setelah aktif: {{YA/TIDAK + KONSEKUENSI}}
- Sinyal yang memicu rollback: {{METRIK_ROLLBACK_1}} > {{AMBANG_1}} selama {{DURASI_1}}
- Dampak rollback pada beban kerja berjalan: {{DAMPAK_ROLLBACK}}; jalur pulih {{AKTIFKAN_KEMBALI}}
- Dependensi eksternal: {{DEP_1}} — dampak outage {{OUTAGE_1}}, dampak degradasi {{DEGRADASI_1}}
- Perkiraan biaya: {{BIAYA_BULANAN}} (komponen {{KOMPONEN_BIAYA}}); trade-off yang disengaja {{TRADEOFF_BIAYA}}

## 15. Risiko, technical debt, dan keputusan tertunda
| Risiko/utang | Probabilitas | Dampak | Mitigasi/rencana bayar | Pemilik |
| --- | --- | --- | --- | --- |
| {{RISIKO_1}} | {{P1}} | {{D1}} | {{MITIGASI_1}} | {{PERAN_1}} |
- Open questions: {{PERTANYAAN_1}} (penentu {{PERAN_1}}, batas {{TANGGAL_1}})
- Future possibilities yang sengaja di luar ruang lingkup: {{IDE_1}}

## 16. Definisi selesai desain (DoD)
- [ ] Goals/non-goals, alternatif ditolak, dan ADR tertaut — {{BUKTI_1}}
- [ ] Diagram C4 + sequence/ER berversi dan bertanggal pemilik — {{BUKTI_2}}
- [ ] STRIDE lengkap dengan pemilik kontrol — {{BUKTI_3}}
- [ ] SLI/SLO, sinyal rollback, dan playbook disepakati SRE — {{BUKTI_4}}
- [ ] Rencana migrasi punya rekonsiliasi & pemulihan state — {{BUKTI_5}}
- [ ] Kriteria WCAG 2.2 AA + `prefers-reduced-motion` diverifikasi pada semua variasi responsif — {{BUKTI_6}}
- [ ] Estimasi biaya dan trade-off disetujui — {{BUKTI_7}}

## 17. Riwayat keputusan
| Tanggal | Versi | Perubahan | Penyetuju |
| --- | --- | --- | --- |
| {{YYYY-MM-DD}} | {{v0.1}} | {{DRAFT_AWAL}} | {{PERAN}} |
````

### Gaps
- **[INFERENSI PENELITI]** Tidak ditemukan standar formal yang menetapkan urutan bab design doc; ISO/IEC/IEEE 42010:2022 secara eksplisit menolak menentukan format/media ([IEEE SA](https://standards.ieee.org/ieee/42010/6846/)). KEP/Rust/React adalah konvensi proyek, sehingga struktur di atas bersifat sintesis praktik, bukan kepatuhan standar.
- **[INFERENSI PENELITI]** Google tidak mempublikasikan template *design doc* internal di portal resminya; hanya portal praktik umum yang tersedia ([Google eng-practices](https://google.github.io/eng-practices/)). Artikel pihak ketiga tidak dipakai sebagai dasar ([Industrial Empathy](https://www.industrialempathy.com/posts/design-docs-at-google/)).
- **[INFERENSI PENELITI]** Tidak ada ambang angka universal untuk "cukup observability" atau "cukup rollback" dalam sumber yang diverifikasi; KEP memberi *pertanyaan*, bukan nilai default ([KEP template](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md)).

## 2. Bagaimana membedakan HLD dan LLD, dan bagaimana model C4 (Context/Container/Component/Code) serta UML/sequence/ER diagram melengkapinya?

### Takeaway
HLD/LLD adalah **pembedaan level abstraksi praktik industri**, bukan istilah yang didefinisikan oleh standar arsitektur: **[STANDAR RESMI]** ISO/IEC/IEEE 42010:2022 justru melarang dirinya sendiri menentukan notasi ([IEEE SA](https://standards.ieee.org/ieee/42010/6846/)); **[PRAKTIK INDUSTRI]** C4 menyediakan "zoom" Context→Container→Component→Code dan menyatakan context+container sudah cukup untuk kebanyakan tim ([c4model.com, "Diagrams"](https://c4model.com/diagrams)), sementara arc42 memisahkan *Building Block View* statis, *Runtime View* perilaku, dan *Deployment View* ([arc42 §5](https://docs.arc42.org/section-5/), [arc42 §6](https://docs.arc42.org/section-6/), [arc42 §7](https://docs.arc42.org/section-7/)).

### Cited Findings
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** C4 resmi mendefinisikan abstraksi hierarkis: *software system* → *container* (aplikasi/data store) → *component* → *code element*, dengan orang/aktor menggunakan sistem; pendekatan ini *abstraction-first*, **notation independent** dan **tooling independent** — [C4 model, "The C4 model for visualising software architecture"](https://c4model.com/); [C4 model, "Abstractions"](https://c4model.com/abstractions).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Empat diagram inti adalah **System Context, Container, Component, Code**; ada 3 diagram pendukung (**system landscape, dynamic, deployment**); **"you don't need to use all 4 levels of diagram; only those that add value — the system context and container diagrams are sufficient for most software development teams"** — [C4 model, "Diagrams"](https://c4model.com/diagrams); [C4 model home](https://c4model.com/).
- **[STANDAR RESMI]** ISO/IEC/IEEE 42010:2022 membedakan *architecture viewpoint* (konvensi untuk membangun/menganalisis satu tipe view yang membingkai *concern*) dari *architecture view*, serta menetapkan persyaratan ADF/ADL/viewpoint/model kind **tanpa menentukan notasi** — [IEEE SA, "IEEE/ISO/IEC 42010-2022"](https://standards.ieee.org/ieee/42010/6846/); [Conceptual Model](http://www.iso-architecture.org/42010/cm/).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI, edisi lama masih tersedia]** Microsoft mendefinisikan *High-level Design* sebagai "describes the major components and how they interact with one another to achieve the goals of the design"; model **bukan spesifikasi arsitektur lengkap** dan sebaiknya dikembangkan paralel dengan kode/uji awal, **"Avoid trying to complete one of these aspects before you start another"**; class diagram dipakai untuk data model/interface, sequence atau activity diagram untuk interaksi — [Microsoft Learn, "Model your app's architecture"](https://learn.microsoft.com/en-us/visualstudio/modeling/model-your-app-s-architecture?view=visualstudio).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** arc42 §5 *Building Block View* adalah dekomposisi **statis** hierarkis black-box/white-box (Level 1 = white box sistem + black box anak; Level 2/3zoom ke blok terpilih), dinyatakan *mandatory* dalam kerangka arc42, dengan anjuran **"prefer relevance over completeness"** dan hanya mendetailkan blok yang penting/mengejutkan/berisiko/kompleks/volatile — [arc42, "5. Building Block View"](https://docs.arc42.org/section-5/).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** arc42 §6 *Runtime View* mendokumentasikan use case penting, interaksi pada interface eksternal kritis, operasi/administrasi (start/stop), serta **skenario error dan exception**; notasi boleh berupa numbered steps, activity/flow chart, **sequence diagrams**, BPMN, atau **state machines**; cukup **representative selection**, bukan sebanyak mungkin skenario — [arc42, "6. Runtime View"](https://docs.arc42.org/section-6/).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** arc42 §7 *Deployment View* memetakan building block ke infrastruktur (lokasi, environment, node, topologi, kanal) dan menyebut **UML deployment diagram** sebagai salah satu notasi — [arc42, "7. Deployment view"](https://docs.arc42.org/section-7/).
- **[STANDAR RESMI]** **OMG Unified Modeling Language (UML), Version 2.5.1**, dokumen `formal/17-12-05`, status *formal*, Desember 2017: "a graphical language for visualizing, specifying, constructing, and documenting the artifacts of distributed object systems" — [OMG, "UML 2.5.1 specification"](https://www.omg.org/spec/UML/2.5.1/).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Sumber resmi penulis mencatat makalah fondasi ER: Peter P. Chen, *"The Entity-Relationship Model — Toward a Unified View of Data"*, **ACM Transactions on Database Systems, Vol. 1, No. 1, Maret 1976, hlm. 9–36** — [Peter Chen, "Research Papers Online"](http://csc.lsu.edu/~chen/papers.html); metadata bibliografik juga tercantum di [ACM DOI 10.1145/320434.320440](https://dl.acm.org/doi/10.1145/320434.320440).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI LAMA, diverifikasi lewat hasil pencarian]** Oracle *Deployment Design Phase* membedakan pemetaan komponen arsitektur logis ke lingkungan fisik yang menghasilkan **high-level deployment architecture**, dengan **implementation specification** berisi *low-level details* cara membangunnya — [Oracle Docs, "Deployment Design Phase"](https://docs.oracle.com/cd/E19636-01/819-2136/fwbea/index.html).

### Inferences
- **[INFERENSI PENELITI]** Ringkasan operasional yang konsisten dengan sumber di atas (bukan definisi standar):

  | Dimensi | HLD | LLD |
  | --- | --- | --- |
  | Pertanyaan utama | Sistem apa, batasnya, siapa pemanggilnya, quality goal apa | Bagaimana satu container bekerja: komponen, interface, state, urutan pesan, error, data |
  | Audiens | Stakeholder, arsitek, SRE, reviewer lintas tim | Engineer implementator, data owner, reviewer komponen |
  | Padanan C4 | L1 Context + L2 Container (+ system landscape/deployment) | L3 Component, L4 Code **hanya bila menambah nilai** |
  | Padanan arc42 | §1, §3, §5 Level 1, §7 | §5 Level 2/3, §6, §8 |
  | Notasi pelengkap | Context/container + deployment | UML sequence/state/class, ER, tabel interface |

  Dasar: [C4 Diagrams](https://c4model.com/diagrams), [arc42 §5](https://docs.arc42.org/section-5/), [arc42 §6](https://docs.arc42.org/section-6/), [Microsoft](https://learn.microsoft.com/en-us/visualstudio/modeling/model-your-app-s-architecture?view=visualstudio).
- **[INFERENSI PENELITI]** C4 **bukan pengganti** UML/ER: C4 memberi *peta zoom dan kosakata abstraksi*, sedangkan UML/sequence/state machine menjawab perilaku dan ER menjawab struktur data. Karena 42010 tidak menetapkan notasi, menggabungkan keduanya diperbolehkan selama setiap view dinyatakan *viewpoint/concern*-nya ([IEEE SA](https://standards.ieee.org/ieee/42010/6846/), [OMG UML 2.5.1](https://www.omg.org/spec/UML/2.5.1/), [Chen 1976](http://csc.lsu.edu/~chen/papers.html)).
- **[INFERENSI PENELITI]** Anti-BUPF sudah tersirat di dua sumber resmi: C4 memperingatkan tidak perlu ke Level 4, arc42 meminta *relevance over completeness*, dan Microsoft menyarankan desain dikembangkan paralel dengan implementasi awal ([C4 Diagrams](https://c4model.com/diagrams), [arc42 §5](https://docs.arc42.org/section-5/), [Microsoft](https://learn.microsoft.com/en-us/visualstudio/modeling/model-your-app-s-architecture?view=visualstudio)).
- **[INFERENSI PENELITI]** Diagram perilaku wajib mencakup jalur **error/exception**, bukan hanya happy path; ini eksplisit di arc42 §6 dan diperkuat oleh daftar *failure modes* pada KEP PRR ([arc42 §6](https://docs.arc42.org/section-6/), [KEP template](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md)).

### Gaps
- **[INFERENSI PENELITI]** Tidak ada standar formal (ISO/IEEE/W3C/OMG) yang mendefinisikan istilah "HLD" dan "LLD" secara normatif; Microsoft (2016) dan Oracle (2004) adalah dokumentasi resmi lama. Pemisahan di tabel atas adalah **inferensi praktik**, sehingga organisasi perlu mendeklarasikan sendiri kedalaman tiap level.
- **[INFERENSI PENELITI]** Halaman ACM DOI makalah Chen 1976 tidak berhasil diambil utuh saat verifikasi; metadata dikonfirmasi dari halaman publikasi resmi penulis dan katalog Internet Archive, bukan dari PDF ACM ([Peter Chen](http://csc.lsu.edu/~chen/papers.html), [Internet Archive metadata](http://ia801601.us.archive.org/fetchmarc.php?path=/29/items/entityrelationshx00chen/entityrelationshx00chen_marc.xml)).
- **[INFERENSI PENELITI]** Halaman `https://docs.arc42.org/sections/` menghasilkan 404 saat di-fetch; section arc42 diverifikasi satu per satu melalui URL `/section-N/` ([arc42 §1](https://docs.arc42.org/section-1/)).

## 3. Apa itu ADR (Architecture Decision Record), kapan harus dibuat, format MADR / adr.github.io, dan bagaimana mengelola status Proposed/Accepted/Superseded?

### Takeaway
ADR adalah catatan **satu** keputusan arsitektural beserta rasional, trade-off, dan konsekuensinya; kumpulan ADR membentuk *decision log* ([adr.github.io](https://adr.github.io/)). Untuk 2024–2026, **[PRAKTIK INDUSTRI]** rilis **MADR 4.0.0 (2024-09-17)** menyediakan template *bare/minimal* ([adr.github.io/madr](https://adr.github.io/madr/)), sementara **[PRAKTIK INDUSTRI]** Microsoft Azure Well-Architected menetapkan aturan tata kelola paling eksplisit: **append-only**, jangan menyunting record yang sudah *Accepted*, tulis record baru yang *supersedes* dan saling tautkan ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)).

### Cited Findings
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** adr.github.io mendefinisikan *Architectural Decision* sebagai pilihan desain beralasan yang menjawab requirement fungsional/non-fungsional yang **architecturally significant**; *ASR* adalah requirement berdampak terukur pada arsitektur & kualitas; **ADR menangkap satu AD + rationale**, dan kumpulannya adalah *decision log* dalam *Architectural Knowledge Management* — [adr.github.io, "Architecture Decision Records"](https://adr.github.io/).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** **MADR 4.0.0 dirilis 2024-09-17** dengan template *bare* dan *minimal*; MADR = *Markdown Architectural Decision Records*, fokus pada keputusan arsitektural namun bisa dipakai untuk "any decision"; tujuannya agar menulis dan **mem-versi keputusan semudah mungkin** — [adr.github.io/madr, "Markdown Architectural Decision Records"](https://adr.github.io/madr/).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Template MADR 4.0.0 memuat metadata opsional `status: "{proposed | rejected | accepted | deprecated | … | superseded by ADR-0123}"`, `date`, `decision-makers`, `consulted`, `informed`; bagian inti `Context and Problem Statement`, `Decision Drivers`, `Considered Options`, `Decision Outcome` ("Chosen option: ... because ..."), `Consequences` (Good/Bad/Neutral), `Confirmation`, `Pros and Cons of the Options`, `More Information` — [adr/madr 4.0.0, "adr-template.md"](https://github.com/adr/madr/blob/4.0.0/template/adr-template.md); [adr.github.io/madr, "Full template"](https://adr.github.io/madr/).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** MADR menyarankan identifier berurutan dengan pola nama berkas `NNNN-title-with-dashes.md`, serta menyediakan konfigurasi `markdownlint` untuk konsistensi format — [adr.github.io/madr, "Applying MADR to your project"](https://adr.github.io/madr/). *(Catatan: ini konvensi penamaan, bukan pembahasan struktur direktori repositori.)*
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** arc42 §9 mengusulkan struktur Nygard: `Title | Context | Decision | Status | Consequences`, dengan status **proposed** bila stakeholder belum sepakat, **accepted** bila disepakati, serta **deprecated** atau **superseded** "hopefully with a reference to its replacement"; **semua** konsekuensi (positif, negatif, netral) harus dicantumkan — [arc42, "9. Architecture Decisions"](https://docs.arc42.org/section-9/).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** arc42 §9 membatasi cakupan: simpan keputusan yang memengaruhi **struktur, quality characteristic, dependensi/interface penting (khususnya eksternal), atau construction technique**, dan hindari redundansi dengan bagian lain — [arc42, "9. Architecture Decisions"](https://docs.arc42.org/section-9/).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Microsoft: **"Start the ADR at the onset of a workload and maintain it throughout the workload's lifespan"**, termasuk **brownfield** dengan rekonstruksi retroaktif bila data tersedia; hanya catat pilihan yang memengaruhi struktur, key quality attributes, atau **sulit dibalik**; **"The ADR serves as an append-only log. Don't go back and edit accepted records. If a decision changes, write a new record that supersedes the original and link the two together."** — [Microsoft Learn, "Maintain an architecture decision record (ADR)"](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Microsoft menyarankan anatomi konsisten: problem statement + context, options considered, decision outcome, **tradeoff penting**, **confidence level** (keputusan berkeyakinan rendah layak ditandai untuk ditinjau ulang), dan **status Proposed / Accepted / Superseded**; satu keputusan bertahap (short/mid/long term) dipecah menjadi beberapa record; selalu sertakan context & rationale, jangan jadikan ADR *design guide* — [Microsoft Learn, "Maintain an architecture decision record (ADR)"](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** adr.github.io mencatat Azure Well-Architected Framework memfiturkan ADR dan situs tersebut pada 2024-11-10, serta ADR juga direkomendasikan AWS Prescriptive Guidance — [adr.github.io, "Motivation and Definitions"](https://adr.github.io/).

### Inferences
- **[INFERENSI PENELITI]** Pemicu praktis pembuatan ADR: (1) awal workload/perubahan besar, (2) keputusan berdampak pada struktur/quality attribute/interface/sulit dibalik, (3) ada alternatif yang dikalahkan, (4) keyakinan rendah sehingga perlu *revisit date*, (5) keputusan lama brownfield yang belum tercatat. Sintesis dari [Microsoft](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record), [arc42 §9](https://docs.arc42.org/section-9/), [adr.github.io](https://adr.github.io/).
- **[INFERENSI PENELITI]** Transisi status yang aman: `Proposed` → `Accepted` → `Superseded by ADR-XXXX` (record lama **tidak diedit**, hanya ditambahi penunjuk); `Rejected`/`Deprecated` ada di MADR/arc42 tetapi tidak ada di daftar status Microsoft, jadi tim harus mendeklarasikan vocabulary sendiri ([MADR 4.0.0](https://github.com/adr/madr/blob/4.0.0/template/adr-template.md), [arc42 §9](https://docs.arc42.org/section-9/), [Microsoft](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)).
- **[INFERENSI PENELITI]** Bagian `Confirmation` MADR menjembatani ADR ke design review: kepatuhan implementasi terhadap keputusan diverifikasi lewat review, bukan dianggap otomatis ([MADR 4.0.0](https://github.com/adr/madr/blob/4.0.0/template/adr-template.md), [Google eng-practices](https://google.github.io/eng-practices/)).

### Cited Findings (lanjutan): Template ADR MADR 4.0.0 + status ledger

````markdown
---
id: {{ADR-0000}}
title: "{{JUDUL_SINGKAT_MASALAH_DAN_SOLUSI}}"
status: "{{proposed | accepted | rejected | deprecated | superseded by ADR-0000}}"
date: "{{YYYY-MM-DD}}"
decision-makers: "{{NAMA_1}}, {{NAMA_2}}"
consulted: "{{PAKAR_1}}, {{TIM_1}}"
informed: "{{TIM_2}}, {{STAKEHOLDER_1}}"
confidence: "{{high | medium | low}}"
supersedes: "{{ADR-0000 | none}}"
superseded-by: "{{ADR-0000 | none}}"
revisit-on: "{{YYYY-MM-DD | none}}"
---

# {{ADR-0000}}: {{JUDUL_SINGKAT_MASALAH_DAN_SOLUSI}}

## Context and Problem Statement
{{KONTEKS_2_SAMPAI_3_KALIMAT}}

Pertanyaan keputusan: Bagaimana {{KOMPONEN}} menyimpan {{DATA}} agar {{KUALITAS}} tercapai tanpa {{CONSTRAINT}}? Tautkan {{TAUTAN_ISSUE}}.

## Decision Drivers
- {{DRIVER_1}} — {{BUKTI_1}}
- {{DRIVER_2}} — {{BUKTI_2}}
- {{DRIVER_3}} — {{BUKTI_3}}

## Considered Options
- {{OPSI_1}}
- {{OPSI_2}}
- {{OPSI_3}}
- {{DO_NOTHING}}

## Decision Outcome
Chosen option: "{{OPSI_1}}", because {{JUSTIFIKASI}}.

### Consequences
- Good, because {{KONSEKUENSI_POSITIF_1}}
- Good, because {{KONSEKUENSI_POSITIF_2}}
- Bad, because {{KONSEKUENSI_NEGATIF_1}} (mitigasi: {{MITIGASI_1}})
- Neutral, because {{KONSEKUENSI_NETRAL_1}}

### Confirmation
Bagaimana kepatuhan diverifikasi: design review {{TAUTAN_REVIEW}}, pemeriksaan struktur/interface {{CARA_CEK_1}}, dan sinyal operasional {{SINYAL_1}}. Catat pemilik {{PERAN}} dan tanggal {{TANGGAL}}.

## Pros and Cons of the Options

### {{OPSI_1}}
{{DESKRIPSI_OPSI_1}} — bukti: {{TAUTAN_1}}
- Good, because {{ARGUMEN_A}}
- Good, because {{ARGUMEN_B}}
- Neutral, because {{ARGUMEN_C}}
- Bad, because {{ARGUMEN_D}}

### {{OPSI_2}}
{{DESKRIPSI_OPSI_2}} — bukti: {{TAUTAN_2}}
- Good, because {{ARGUMEN_A}}
- Neutral, because {{ARGUMEN_C}}
- Bad, because {{ARGUMEN_D}}

### {{DO_NOTHING}}
- Good, because {{TANPA_BIAYA_PERUBAHAN}}
- Bad, because {{RISIKO_JIKA_TIDAK_BERUBAH}}

## More Information
- Dasar evidence: {{BENCHMARK/INSIDEN/REGULASI}} — {{TAUTAN_EVIDENCE}}
- Kesepakatan tim dicatat pada: {{TAUTAN_RAPAT}}
- Terkait: {{DD-0000}}, {{ADR-0000}}, {{TAUTAN_DIAGRAM_C4}}
- Jika `confidence: low`, tinjau ulang pada {{REVISIT_ON}} dengan pemicu {{PIMICU_TINJAU}}
- Riwayat status: {{YYYY-MM-DD}} `proposed` → {{YYYY-MM-DD}} `accepted` → {{YYYY-MM-DD}} `superseded by ADR-0000`
````

### Gaps
- **[INFERENSI PENELITI]** Vocabulary status **tidak seragam**: MADR 4.0.0 memuat `proposed | rejected | accepted | deprecated | … | superseded by ADR-0123`, arc42 memakai `proposed | accepted | deprecated | superseded`, Microsoft hanya `Proposed | Accepted | Superseded` ([MADR](https://github.com/adr/madr/blob/4.0.0/template/adr-template.md), [arc42 §9](https://docs.arc42.org/section-9/), [Microsoft](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)). Tidak ada standar resmi yang memaksa satu set status.
- **[INFERENSI PENELITI]** Halaman MADR masih memuat kalimat *"There is currently no tooling supporting MADR 3.0.0"* di bagian *Automatic approach* walau rilis yang diumumkan adalah 4.0.0; ini potensi inkonsistensi dokumentasi versi, jangan ditafsirkan sebagai pernyataan dukungan tooling 4.0.0 ([adr.github.io/madr](https://adr.github.io/madr/)).
- **[INFERENSI PENELITI]** Tidak ditemukan ambang kuantitatif resmi untuk "architecturally significant"; adr.github.io memberi definisi kualitatif, Microsoft memberi kriteria "sulit dibalik", keduanya memerlukan judgement tim ([adr.github.io](https://adr.github.io/), [Microsoft](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)).

## 4. Praktik baik desain UI/UX: design tokens, design system, komponen, state (empty/loading/error), hierarchy, konsistensi, handoff desainer ke engineer

### Takeaway
Fondasi yang masih relevan 2024–2026 adalah **token sebagai single source of truth lintas desain–kode** ([Material Design 3](https://m3.material.io/foundations/design-tokens/overview)) yang kini punya format interchange **Design Tokens Format Module 2025.10** — **[SPESIFIKASI KOMUNITAS, bukan W3C Standard]** ([DTCG Final Report](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/)); state dan hierarki diperlakukan sebagai bagian dari spesifikasi komponen, bukan dekorasi, dengan panduan resmi untuk loading/progress, feedback, dan pesan error ([Material progress indicators](https://m3.material.io/components/progress-indicators/guidelines), [Apple HIG Progress Indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators), [Apple HIG Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback)).

### Cited Findings
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Material Design 3: design tokens adalah *building blocks* semua elemen UI; **token yang sama dipakai di desain, tools, dan kode**; token menggantikan nilai statis dengan nama yang *self-explanatory*; token membuat **single source of truth**, memungkinkan pembaruan tema/ konteks sistemik (mis. palet high-contrast), dan **"help designers and engineers 'speak the same language,' reducing confusion during handoff from design to implementation"** — [Material Design 3, "Design tokens"](https://m3.material.io/foundations/design-tokens/overview).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Material 3 membagi token menjadi tiga kelas: **Reference** (`ref`, semua opsi nilai), **System** (`sys`, peran/tema; sebisa mungkin menunjuk reference), **Component** (`comp`, properti elemen komponen; sebisa mungkin menunjuk system/reference, bukan hardcoded); nama token bertingkat dari umum ke spesifik, dan *contexts* (dark theme, dense layout, RTL, form factor) dapat meng-override nilai — [Material Design 3, "Design tokens"](https://m3.material.io/foundations/design-tokens/overview).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Spesifikasi komponen Material mengelompokkan token **berdasarkan state** (enabled, disabled, hover, dll.) baru kemudian berdasarkan elemen (container, label text, icon), dengan kolom Name / Token ID / Description / Context-value; cara verifikasi handoff: salin token ke kode atau bandingkan dengan color role di design tool — [Material Design 3, "Design tokens"](https://m3.material.io/foundations/design-tokens/overview).
- **[SPESIFIKASI KOMUNITAS — BUKAN W3C STANDARD]** *Design Tokens Format Module 2025.10* (DTCG Candidate Recommendation, dinyatakan **stable**, **"not a W3C Standard nor is it on the W3C Standards Track"**): token minimum berupa pasangan nama/`$value`, dengan `$type`, `$description`, `$deprecated`, `$extensions`, **alias**, **composite token**, dan `$extends`; file berbasis JSON; **"If no explicit type has been set for a token, tools MUST consider the token invalid and not attempt to infer any other type from the value"** — [W3C Design Tokens Community Group, "Format Module 2025.10"](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/).
- **[SPESIFIKASI KOMUNITAS — BUKAN W3C STANDARD]** Format tersebut mendefinisikan tipe `color`, `dimension`, `fontFamily`, `fontWeight`, `duration`, `cubicBezier`, `number` serta composite `strokeStyle`, `border`, `transition`, `shadow`, `gradient`, `typography`; media type yang dianjurkan `application/design-tokens+json` — [W3C DTCG, "Format Module 2025.10"](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Material 3 progress indicators: **< 200 ms → tanpa indikator; 200 ms–5 s → loading indicator; > 5 s → progress indicator**; varian **determinate** (progres diketahui, harus akurat) vs **indeterminate**; **"A process should be represented by the same variant of progress indicator throughout the product"**; satu indikator untuk grup, bukan satu per elemen; bila tunggu sangat lama, izinkan pengguna meninggalkan halaman — [Material Design 3, "Progress indicators"](https://m3.material.io/components/progress-indicators/guidelines).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Material 3 juga mensyaratkan konsistensi penempatan (linear di tepi container, circular di tengah), penyesuaian RTL, dan **kontras minimum 3:1** untuk indikator di dalam button — [Material Design 3, "Progress indicators"](https://m3.material.io/components/progress-indicators/guidelines).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Apple HIG: progress indicator **transient**, muncul hanya saat operasi berjalan; utamakan **determinate**; **"If a process stalls for some reason, provide feedback that helps people understand the problem and what they can do about it"**; hindari label samar seperti *"loading"*; tampilkan di lokasi konsisten; sediakan Cancel/Pause bila aman; beri tahu konsekuensi pembatalan — [Apple HIG, "Progress indicators"](https://developer.apple.com/design/human-interface-guidelines/progress-indicators).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Apple HIG mendefinisikan *Feedback* sebagai cara pengguna mengetahui **what's happening, what they can do next, results of actions**, dan menghindari kesalahan — [Apple HIG, "Feedback"](https://developer.apple.com/design/human-interface-guidelines/feedback).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Apple HIG *Accessibility* (change log 9 Juni 2025): antarmuka aksesibel bersifat **Intuitive** ("familiar and consistent interactions"), **Perceivable** (tidak bergantung pada satu modalitas), **Adaptable**; rekomendasi kontras teks **4.5:1** (≤17 pt) / **3:1** (18 pt atau bold), dukungan pembesaran teks **≥200%**, informasi tidak hanya dengan warna, dan kontrol berukuran memadai — [Apple HIG, "Accessibility"](https://developer.apple.com/design/human-interface-guidelines/accessibility).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Material 3 *Text fields* menyatakan state (blank, with input, error, dll.) **harus terlihat sekilas**, serta label dan pesan error **ringkas dan mudah ditindaklanjuti** — [Material Design 3, "Text fields overview"](https://m3.material.io/components/text-fields/overview).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** USWDS menyarankan *contextual helper text*, *inline validation*, dan pesan error yang mengetahui pengguna apa yang salah serta field mana yang belum diisi; pesan error **"Be polite in error messages — don't blame the user"** — [U.S. Web Design System, "Form"](https://designsystem.digital.gov/components/form/); [U.S. Web Design System, "Alert"](https://designsystem.digital.gov/components/alert/).
- **[PANDUAN INFORMATIF W3C WAI]** WAI-ARIA APG: **"Prefer Visible Text"**, **"Prefer Native Techniques"** (HTML `label`, `caption`), **"Avoid Browser Fallback"** (`placeholder`/`title` bukan sumber nama yang baik), dan nama harus **brief, useful, berisi fungsi bukan bentuk** — [W3C WAI-ARIA APG, "Providing Accessible Names and Descriptions"](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/).

### Inferences
- **[INFERENSI PENELITI]** Handoff yang baik bukan sekadar "ekspor asset", melainkan **kontrak token + state + semantics**: nama token yang identik di mockup dan kode, tabel state per komponen, dan accessible name/role untuk tiap kontrol ([Material tokens](https://m3.material.io/foundations/design-tokens/overview), [DTCG 2025.10](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/), [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/)).
- **[INFERENSI PENELITI]** Matriks state minimum per komponen: `empty` (belum ada data + aksi pertama), `loading` (durasi menentukan jenis indikator), `populated`, `error` (pesan yang dapat ditindaklanjuti + pemulihan), `disabled`, `success/status`, dan `reduced-motion fallback`. Empty state diturunkan dari prinsip *Feedback* dan *progress stall*, karena tidak ada halaman resmi khusus "empty state" yang berhasil diverifikasi terpisah ([Apple Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback), [Apple Progress Indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators), [Material progress](https://m3.material.io/components/progress-indicators/guidelines)).
- **[INFERENSI PENELITI]** Hierarki & konsistensi sebaiknya diwujudkan sebagai **keputusan token berskala sistem** (`ref → sys → comp`), bukan nilai per-layout; dengan begitu perubahan tema/high-contrast menyebar konsisten dan sekaligus melayani aksesibilitas ([Material tokens](https://m3.material.io/foundations/design-tokens/overview), [Apple HIG Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)).
- **[INFERENSI PENELITI]** `$deprecated` dalam DTCG 2025.10 memberi mekanisme *sunset* token yang mirip status `superseded` pada ADR; keduanya mendukung prinsip "jejak keputusan tidak dihapus" ([DTCG](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/), [Microsoft ADR](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)).

### Cited Findings (lanjutan): Template spesifikasi komponen UI/UX & handoff

````markdown
# {{NAMA_KOMPONEN}} — UI/UX Spec & Handoff

| Metadata | Nilai |
| --- | --- |
| ID | {{UI-0000}} |
| Versi | {{v1.0}} — {{YYYY-MM-DD}} |
| Pemilik desain | {{DESAINER}} |
| Pemilik implementasi | {{ENGINEER}} |
| Terkait | {{DD-0000}}, {{ADR-0000}} |
| Target aksesibilitas | {{WCAG 2.2 AA}} + {{prefers-reduced-motion}} |
| Sumber token | {{TAUTAN_TOKEN_SOURCE}} |

## 1. Tujuan & hierarki
- Job-to-be-done: {{MASALAH_PENGGUNA}}
- Posisi dalam hierarki halaman: {{H1/H2/SECTION}}; aksi utama {{AKSI_UTAMA}}, aksi sekunder {{AKSI_SEKUNDER}}
- Urutan fokus keyboard: {{FOKUS_1}} → {{FOKUS_2}} → {{FOKUS_3}}
- Alasan hierarki: {{ALASAN_HIERARKI}}; konsistensi dengan {{KOMPONEN_LAIN}}

## 2. Design tokens (bukan hardcoded value)
| Peran | Token ID | Nilai/alias | Konteks | Sumber |
| --- | --- | --- | --- | --- |
| Container | {{sys.color.primary.container}} | {{ref.palette.primary90}} | {{light}} | {{TAUTAN_TOKENS}} |
| Label teks | {{comp.button.label.color}} | {{sys.color.on-primary}} | {{light/dark}} | {{TAUTAN_TOKENS}} |
| Spasi | {{sys.spacing.md}} | {{value: 16, unit: px}} | {{dense/default}} | {{TAUTAN_TOKENS}} |
| Durasi motion | {{comp.transition.duration}} | {{value: 200, unit: ms}} | {{default}} | {{TAUTAN_TOKENS}} |
- Token bertipe `$type`: {{color/dimension/duration/cubicBezier/typography/shadow}}
- Token deprecated: {{TOKEN_LAMA}} → pengganti {{TOKEN_BARU}}, alasan {{ALASAN}}

## 3. Anatomy & variant
- Elemen: {{CONTAINER}}, {{LABEL}}, {{ICON}}, {{STATE_LAYER}}, {{HELPER_TEXT}}
- Variant: {{VARIANT_1}}, {{VARIANT_2}}; ukuran {{SM/MD/LG}}
- Konteks: {{light}}, {{dark}}, {{high-contrast}}, {{RTL}}, {{breakpoint_1}}, {{breakpoint_2}}

## 4. Matriks state (wajib lengkap)
| State | Pemicu | Visual | Teks | Semantik AT | Aksi pemulihan |
| --- | --- | --- | --- | --- | --- |
| Empty | {{BELUM_ADA_DATA}} | {{ILUSTRASI/PLACEHOLDER}} | {{AJAKAN_PERTAMA}} | {{aria-describedby}} | {{BUAT_DATA_1}} |
| Loading <200ms | {{LATENSI_RENDAH}} | tanpa indikator | — | — | — |
| Loading 200ms–5s | {{PROSES_SINGKAT}} | {{LOADING_INDICATOR}} | {{KONTEKS_SINGKAT}} | {{aria-busy="true"}}, {{role="status"}} | {{CANCEL_JIKA_AMAN}} |
| Loading >5s | {{PROSES_PANJANG}} | {{PROGRESS_DETERMINATE}} | {{PERSENTASE/TAHAP}} | {{aria-valuenow}} | {{CANCEL/PAUSE}} |
| Populated | {{DATA_ADA}} | {{TAMPILAN_NORMAL}} | {{KONTEN}} | {{NAME_ROLE_VALUE}} | — |
| Error | {{GAGAL_MUAT/VALIDASI}} | {{WARNA + IKON + TEKS, bukan warna saja}} | {{PESAN_ERROR_SOPAN}} (mis. "{{FIELD}} belum diisi; {{CARA_PERBAIKI}}") | {{aria-invalid}}, {{aria-errormessage}}, {{role="alert"}} | {{COBA_LAGI/ISI_ULANG}} |
| Stalled | {{PROSES_MACET}} | {{FEEDBACK_STALL}} | {{PENJELASAN + LANGKAH}} | {{role="status"}} | {{CANCEL/PAUSE/DIAGNOSA}} |
| Disabled | {{TIDAK_TERSEDIA}} | {{STATE_DISABLED}} | {{ALASAN_DISABLE}} | {{aria-disabled}} | {{SYARAT_AKTIF}} |
| Success/status | {{BERHASIL}} | {{TOAST/INLINE}} | {{HASIL_TINDAKAN}} | {{role="status"}}, {{aria-live="polite"}} | {{LANJUT}} |
- Konsistensi indikator: {{VARIAN_TERPILIH}} dipakai di seluruh produk — {{BUKTI_KONSISTENSI}}

## 5. Aksesibilitas & motion
- Accessible name: {{NAMA_FUNGSI}} (bukan "{{NAMA_BENTUK}}"); teknik {{HTML label | aria-labelledby | aria-label}}
- Role & value: {{ROLE}}, {{aria-checked/expanded/selected/valuenow}}
- Keyboard: {{TAB/ENTER/SPACE/ARROW/ESC}}; tidak ada keyboard trap; fokus tidak tertutup sticky UI
- Kontras: teks ≥ {{4.5:1}} (large ≥ {{3:1}}), non-text/focus/indikator ≥ {{3:1}}; diuji pada {{light}}, {{dark}}, {{high-contrast}}
- Target pointer: ≥ {{24x24 CSS px}} atau spacing setara; alternatif non-drag {{ALTERNATIF}}
- Reduced motion: `@media (prefers-reduced-motion: reduce)` → {{HILANGKAN_TRANSISI, GANTI_DENGAN_FADE}}, fallback {{FALLBACK}}
- Status message tanpa menerima fokus: {{role="status"}} / {{aria-live="polite"}}

## 6. Konten & copy
- Label: {{LABEL_RINGKAS}}; helper: {{HELPER_TEXT}}; error: {{PESAN_SOPAN_DAN_AKTIF}}; hindari {{"loading"}} generik
- Lokalisasi/RTL: {{CATATAN_RTL}}; pluralisasi {{CATATAN_PLURAL}}; panjang teks maks {{BATAS}}

## 7. Handoff desainer → engineer
- [ ] Token ID di mockup identik dengan token di kode — {{BUKTI_DIFF_TOKEN}}
- [ ] Semua state pada matriks tersedia sebagai variant — {{BUKTI_VARIANT}}
- [ ] Accessible name, role, dan urutan fokus tertulis, tidak diserahkan ke interpretasi — {{BUKTI_SEMANTIK}}
- [ ] Nilai kontras terlampir per konteks — {{BUKTI_KONTRAS}}
- [ ] Motion + fallback reduced-motion terdokumentasi — {{BUKTI_MOTION}}
- [ ] Perbedaan visual vs implementasi dicatat sebagai {{ISSUE_ID}} dengan pemilik {{PERAN}}

## 8. Definisi selesai desain UI
- [ ] Review desain oleh {{DESAINER}} + {{ENGINEER}} + {{A11Y_REVIEWER}}
- [ ] Diverifikasi dengan keyboard saja dan screen reader pada {{BREAKPOINT_1}}, {{BREAKPOINT_2}}
- [ ] Tidak ada nilai hardcoded yang menggantikan token — {{BUKTI_LINT_TOKEN}}
- [ ] Terkait {{ADR-0000}} bila ada keputusan sistemik
````

### Gaps
- **[INFERENSI PENELITI]** *Design Tokens Format Module 2025.10* **bukan W3C Recommendation** dan tidak berada di *Standards Track*; statusnya Community Final Specification yang stabil untuk diimplementasi. Mengklaimnya sebagai "standar W3C" adalah kesalahan ([DTCG](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/)).
- **[INFERENSI PENELITI]** Tidak ditemukan halaman resmi terverifikasi yang secara khusus membahas *empty state*; praktik di atas diturunkan dari prinsip *Feedback*, *stall handling*, dan *inline validation* ([Apple Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback), [Apple Progress Indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators), [USWDS Form](https://designsystem.digital.gov/components/form/)).
- **[INFERENSI PENELITI]** Beberapa halaman komponen (Material *Text fields*, USWDS *Form*/*Alert*) diverifikasi melalui cuplikan hasil pencarian resmi, bukan pengambilan halaman penuh; klaimnya sengaja dibatasi pada kalimat yang tampak di cuplikan tersebut ([Material Text fields](https://m3.material.io/components/text-fields/overview), [USWDS Form](https://designsystem.digital.gov/components/form/)).
- **[INFERENSI PENELITI]** Angka durasi 200 ms / 5 s berasal dari **Material Design 3**, bukan standar lintas-vendor; Apple HIG memberi prinsip kualitatif tanpa ambang angka yang sama ([Material progress](https://m3.material.io/components/progress-indicators/guidelines), [Apple Progress Indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)).

## 5. Standar aksesibilitas apa yang wajib (W3C WCAG 2.2 AA, reduced motion, keyboard, kontras) dan bagaimana masuk ke definisi selesai desain?

### Takeaway
**[STANDAR RESMI]** Target yang dapat diklaim adalah **WCAG 2.2 Level AA** (W3C Recommendation; AA = seluruh kriteria A + AA), dan W3C **menyarankan memakai 2.2** sebagai target baru walau kebijakan lama menyebut 2.0/2.1 ([W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/), [W3C WAI, "WCAG 2 Level AA Conformance"](https://www.w3.org/WAI/WCAG2AA-Conformance)). **Koreksi penting:** `reduced motion` **bukan** kewajiban WCAG 2.2 AA — kriteria *Animation from Interactions* (2.3.3) berlevel **AAA**; yang wajib di jalur A/AA adalah keyboard, kontras, *Pause/Stop/Hide*, dan *Status Messages*, sedangkan `prefers-reduced-motion` berstatus **[DRAFT W3C]** di Media Queries Level 5 plus **[PRAKTIK INDUSTRI]** Apple HIG ([W3C new-in-22](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/), [Media Queries Level 5](https://www.w3.org/TR/mediaqueries-5/#prefers-reduced-motion), [Apple HIG Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)).

### Cited Findings
- **[STANDAR RESMI]** *Web Content Accessibility Guidelines (WCAG) 2.2* adalah **W3C Recommendation** (5 Oktober 2023; versi terkini direpublikasi 12 Desember 2024 dengan errata); 2.2 **backwards compatible** dengan 2.0/2.1, menghapus **4.1.1 Parsing**, dan W3C **"advises the use of WCAG 2.2 to maximize future applicability"** — [W3C, "Web Content Accessibility Guidelines (WCAG) 2.2"](https://www.w3.org/TR/WCAG22/); [W3C WAI, "What's New in WCAG 2.2"](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/).
- **[STANDAR RESMI]** Empat prinsip (Perceivable, Operable, Understandable, Robust), 13 guideline, dan **success criteria teruji** dengan level A/AA/AAA; untuk **Level AA** halaman harus memenuhi **semua** kriteria A **dan** AA; konformasi berlaku untuk **full page**, **seluruh halaman dalam satu proses**, dan **setiap variasi responsif**; *Non-Interference* memberlakukan 1.4.2, 2.1.2, 2.3.1, 2.2.2 pada semua konten — [W3C, "WCAG 2.2 §5 Conformance"](https://www.w3.org/TR/WCAG22/); [W3C WAI, "WCAG 2 Level AA Conformance"](https://www.w3.org/WAI/WCAG2AA-Conformance).
- **[STANDAR RESMI]** Kontras: **1.4.3 Contrast (Minimum) AA** = **4.5:1** teks biasa, **3:1** large text, dengan pengecualian incidental/inactive/logotype; **1.4.11 Non-text Contrast AA** = **3:1** untuk komponen UI, indikator state, dan objek grafis yang diperlukan; **1.4.4 Resize Text AA** = hingga **200%** tanpa kehilangan konten/fungsi; **1.4.12 Text Spacing AA** mensyaratkan tidak ada kehilangan fungsi saat line-height 1.5×, paragraph 2×, letter 0.12×, word 0.16× — [W3C, "WCAG 2.2"](https://www.w3.org/TR/WCAG22/).
- **[STANDAR RESMI]** Keyboard: **2.1.1 Keyboard (A)** = seluruh fungsionalitas dapat dioperasikan lewat keyboard tanpa tuntutan waktu per keystroke; **2.1.2 No Keyboard Trap (A)**; **2.1.4 Character Key Shortcuts (A)**; **2.4.7 Focus Visible** tercantum di dokumen; **4.1.2 Name, Role, Value (A)** mewajibkan name/role/state dapat ditentukan secara programatik — [W3C, "WCAG 2.2"](https://www.w3.org/TR/WCAG22/).
- **[STANDAR RESMI]** Kriteria **baru di 2.2** yang relevan untuk desain: **2.4.11 Focus Not Obscured (Minimum) AA**, **2.5.7 Dragging Movements AA**, **2.5.8 Target Size (Minimum) AA** (≥ **24×24 CSS px** atau spacing setara), **3.2.6 Consistent Help A**, **3.3.7 Redundant Entry A**, **3.3.8 Accessible Authentication (Minimum) AA** (dukung password manager / copy-paste); **2.4.13 Focus Appearance** dan **3.3.9 Accessible Authentication (Enhanced)** berlevel **AAA**, bukan AA — [W3C WAI, "What's New in WCAG 2.2"](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/).
- **[STANDAR RESMI]** Motion/animasi: **2.2.2 Pause, Stop, Hide (A)** untuk moving/blinking/scrolling/auto-update otomatis > 5 detik; **2.3.1 Three Flashes or Below Threshold (A)**; **2.3.3 Animation from Interactions (AAA)** = motion animation yang dipicu interaksi **dapat dinonaktifkan** kecuali esensial. Jadi **reduced motion tidak termasuk kewajiban AA** — [W3C, "WCAG 2.2"](https://www.w3.org/TR/WCAG22/).
- **[STANDAR RESMI]** **4.1.3 Status Messages (AA)**: pesan status harus dapat ditentukan secara programatik lewat role/properties sehingga disampaikan AT **tanpa menerima fokus** — ini dasar normatif untuk state loading/error/success pada komponen — [W3C, "WCAG 2.2"](https://www.w3.org/TR/WCAG22/).
- **[DRAFT W3C — BUKAN RECOMMENDATION]** *Media Queries Level 5* (Working Draft 19 Februari 2026) menambahkan **`prefers-reduced-motion`** dengan nilai `no-preference | reduce`; dokumen ini **"inappropriate to cite this document as other than a work in progress"** — [W3C, "Media Queries Level 5"](https://www.w3.org/TR/mediaqueries-5/#prefers-reduced-motion); teknik deteksi juga didokumentasikan WAI pada [W3C, "Technique SCR40: Using the CSS prefers-reduced-motion query"](https://www.w3.org/WAI/WCAG21/Techniques/client-side-script/SCR40).
- **[STANDAR RESMI]** **WAI-ARIA 1.2** (W3C Recommendation, 6 Juni 2023) menyediakan ontologi roles/states/properties; `role="status"` memiliki `aria-live="polite"` dan `aria-atomic="true"` secara implisit; ARIA **"is intended to be used as a supplement for native language semantics, not a replacement"** dan aksesibilitas konten interaktif **tidak bisa dikonfirmasi hanya dengan pemeriksaan statis** — [W3C, "Accessible Rich Internet Applications (WAI-ARIA) 1.2"](https://www.w3.org/TR/wai-aria-1.2/).
- **[PANDUAN INFORMATIF W3C WAI]** APG menekankan visible text, native HTML, menghindari fallback `placeholder`/`title`, dan nama yang menyatakan fungsi — [W3C WAI-ARIA APG, "Providing Accessible Names and Descriptions"](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Apple HIG (diperbarui 9 Juni 2025) meminta aplikasi **merespons setting Reduce Motion** dengan mengurangi animasi otomatis/repetitif (zoom, scaling, peripheral motion), mengencangkan spring, mengganti transisi sumbu dengan fade, serta mendukung Dynamic Type, Full Keyboard Access, VoiceOver, Switch Control, dan kontras 4.5:1/3:1 — [Apple HIG, "Accessibility"](https://developer.apple.com/design/human-interface-guidelines/accessibility).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Material 3 mensyaratkan indikator progress mencapai **3:1** dan menyediakan stop indicator bila track di bawah 3:1 — [Material Design 3, "Progress indicators"](https://m3.material.io/components/progress-indicators/guidelines).
- **[STANDAR RESMI]** Klaim konformasi bersifat opsional, tetapi bila dibuat **wajib** memuat: tanggal, judul+versi+URI (`Web Content Accessibility Guidelines 2.2 at https://www.w3.org/TR/WCAG22/`), level, deskripsi halaman/URI, dan daftar teknologi yang diandalkan; **W3C tidak memverifikasi klaim/logo** — [W3C, "WCAG 2.2 §5.3 Conformance Claims"](https://www.w3.org/TR/WCAG22/); [W3C WAI, "WCAG 2 Level AA Conformance"](https://www.w3.org/WAI/WCAG2AA-Conformance).

### Inferences
- **[INFERENSI PENELITI]** Cara memasukkan aksesibilitas ke **Definition of Done desain**: jangan menulis "aksesibel", melainkan daftar **success criteria + bukti per state + variasi halaman**. Minimal: 1.4.3/1.4.11/1.4.4/1.4.12, 2.1.1/2.1.2, 2.4.11, 2.5.7/2.5.8, 3.3.8, 4.1.2/4.1.3, ditambah 2.2.2 & 2.3.1 untuk motion, dan `prefers-reduced-motion` sebagai **kebijakan produk** di luar kewajiban AA ([WCAG 2.2](https://www.w3.org/TR/WCAG22/), [W3C new-in-22](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/), [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility)).
- **[INFERENSI PENELITI]** Karena konformasi mencakup **seluruh halaman dalam satu proses** dan **setiap variasi responsif**, DoD harus menyebut daftar breakpoint/flow yang diuji, bukan hanya komponen terisolasi ([WCAG 2.2 §5.2.2–5.2.3](https://www.w3.org/TR/WCAG22/)).
- **[INFERENSI PENELITI]** State `loading`/`error` wajib punya semantik `role="status"`/`aria-live`/`aria-busy` agar memenuhi 4.1.3; ARIA melengkapi, bukan menggantikan, HTML native ([WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/), [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/)).
- **[INFERENSI PENELITI]** Pemisahan yang perlu ditegaskan dalam review: **"wajib (normatif AA)"** vs **"praktik baik (AAA / vendor / draft)"**. Mengklaim `reduced motion` sebagai syarat AA adalah *over-claim*; menyertakannya sebagai kebijakan desain tetap dianjurkan ([W3C new-in-22](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/), [Media Queries Level 5](https://www.w3.org/TR/mediaqueries-5/#prefers-reduced-motion), [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility)).

### Cited Findings (lanjutan): Definisi selesai desain (DoD) aksesibilitas

````markdown
# DoD Aksesibilitas — {{NAMA_FITUR/KOMPONEN}}

| Metadata | Nilai |
| --- | --- |
| Target normatif | {{WCAG 2.2 Level AA}} — {{https://www.w3.org/TR/WCAG22/}} |
| Kebijakan tambahan (di luar AA) | {{prefers-reduced-motion}}, {{2.3.3 AAA}}, {{Apple Reduce Motion}} |
| Ruang lingkup halaman | {{URI_1}}, {{URI_2}}, {{SEMUA_LANGKAH_ALUR_1}} |
| Variasi yang diuji | {{breakpoint_1}}, {{breakpoint_2}}, {{light}}, {{dark}}, {{high-contrast}}, {{zoom_200%}}, {{RTL}} |
| Teknologi yang diandalkan | {{HTML}}, {{CSS}}, {{WAI-ARIA 1.2}}, {{FRAMEWORK}} |
| Tanggal verifikasi | {{YYYY-MM-DD}} |

## A. Kriteria normatif (AA = semua A + AA)
- [ ] 1.4.3 teks {{4.5:1}} / large {{3:1}} — bukti {{TAUTAN_HASIL_KONTRAS}}
- [ ] 1.4.11 komponen UI, focus indicator, grafis {{3:1}} — bukti {{TAUTAN_HASIL_KONTRAS_NONTEKS}}
- [ ] 1.4.4 resize teks {{200%}} tanpa kehilangan konten/fungsi — bukti {{TAUTAN_SCREENSHOT_ZOOM}}
- [ ] 1.4.12 text spacing override tanpa kehilangan fungsi — bukti {{TAUTAN_UJI_SPACING}}
- [ ] 1.4.1 informasi tidak hanya dengan warna — bukti {{TAUTAN_UJI_WARNA}}
- [ ] 2.1.1 seluruh fungsi via keyboard; 2.1.2 tanpa keyboard trap — bukti {{TAUTAN_UJI_KEYBOARD}}
- [ ] 2.4.7 focus visible + 2.4.11 fokus tidak seluruhnya tertutup konten sticky — bukti {{TAUTAN_UJI_FOKUS}}
- [ ] 2.5.7 alternatif single-pointer untuk drag; 2.5.8 target {{24x24 CSS px}} / spacing — bukti {{TAUTAN_UJI_TARGET}}
- [ ] 2.2.2 pause/stop/hide untuk animasi otomatis > {{5s}}; 2.3.1 ≤ {{3 flash/detik}} — bukti {{TAUTAN_UJI_MOTION}}
- [ ] 3.2.6 bantuan konsisten; 3.3.7 tidak meminta data ulang; 3.3.8 dukung password manager/copy-paste — bukti {{TAUTAN_UJI_FORM}}
- [ ] 4.1.2 name/role/value dapat ditentukan programatik — bukti {{TAUTAN_AUDIT_SEMANTIK}}
- [ ] 4.1.3 status message (loading/error/success) dikenali AT tanpa fokus — bukti {{TAUTAN_UJI_LIVE_REGION}}
- [ ] 1.1.1 text alternative untuk non-text content — bukti {{TAUTAN_UJI_ALT}}

## B. Kebijakan produk di luar kewajiban AA (tetap wajib secara internal)
- [ ] `@media (prefers-reduced-motion: reduce)` → {{FALLBACK_MOTION}} — bukti {{TAUTAN_UJI_REDUCED_MOTION}}
- [ ] 2.3.3 (AAA) motion akibat interaksi dapat dinonaktifkan — bukti {{TAUTAN_UJI_233}}
- [ ] Platform native: {{Dynamic Type >=200%}}, {{VoiceOver}}, {{Full Keyboard Access}}, {{Switch Control}} — bukti {{TAUTAN_UJI_NATIVE}}
- [ ] Catatan eksplisit: kriteria ini **bukan** syarat konformasi {{WCAG 2.2 AA}} — {{TAUTAN_KEBIJAKAN_INTERNAL}}

## C. Metode verifikasi
- [ ] Uji keyboard-saja pada {{BREAKPOINT_1}} dan {{BREAKPOINT_2}} oleh {{PERAN_1}}
- [ ] Uji screen reader {{AT_1}} / {{AT_2}} pada alur {{ALUR_1}} oleh {{PERAN_2}}
- [ ] Pemeriksaan otomatis {{TOOL_1}} + **pemeriksaan manual** (static check tidak cukup) — {{TAUTAN_LAPORAN}}
- [ ] Accessible name memakai {{HTML label}} bukan {{placeholder/title}} — {{BUKTI_NAMING}}

## D. Pernyataan konformasi (opsional, hanya bila benar-benar diklaim)
- [ ] Tanggal klaim: {{YYYY-MM-DD}}
- [ ] Judul + versi + URI: `Web Content Accessibility Guidelines 2.2 at https://www.w3.org/TR/WCAG22/`
- [ ] Level: {{AA}}; daftar URI: {{DAFTAR_URI}}; teknologi: {{DAFTAR_TEKNOLOGI}}
- [ ] Penafian: {{"Klaim tidak diverifikasi oleh W3C; penyedia konten bertanggung jawab penuh"}}
````

### Gaps
- **[INFERENSI PENELITI]** Tidak ada kewajiban hukum universal yang dapat dinyatakan di sini: WCAG adalah standar teknis W3C; kewajiban hukum bergantung yurisdiksi/kebijakan pengadaan masing-masing, yang **tidak** diteliti dalam catatan ini ([W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)).
- **[INFERENSI PENELITI]** `prefers-reduced-motion` berada di **Working Draft** Media Queries Level 5 per 2026-02-19; W3C sendiri menyatakan dokumen itu tidak patut disitasi selain sebagai *work in progress*, meski dukungan browser luas. Status ini harus dinyatakan eksplisit agar tidak tertukar dengan W3C Recommendation ([Media Queries Level 5](https://www.w3.org/TR/mediaqueries-5/#prefers-reduced-motion)).
- **[INFERENSI PENELITI]** WCAG 2.2 tidak mendefinisikan angka kontras/target untuk aplikasi native; angka 4.5:1/3:1/24×24 CSS px berlaku untuk **web content**. Angka native (mis. 44×44 pt iOS) berasal dari Apple HIG dan merupakan praktik vendor ([WCAG 2.2](https://www.w3.org/TR/WCAG22/), [Apple HIG Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)).
- **[INFERENSI PENELITI]** W3C tidak memverifikasi klaim/logo konformasi; "sudah AA" harus dibuktikan dengan artefak uji internal, bukan badge ([W3C WAI](https://www.w3.org/WAI/WCAG2AA-Conformance)).

## 6. Apa isi checklist design review (scalability, failure mode, keamanan/STRIDE, data migration, biaya, operability) dan anti-pattern desain (big design up front, diagram basi, keputusan tanpa catatan)?

### Takeaway
Checklist review yang kuat menggabungkan tiga kerangka resmi yang saling melengkapi: **[PRAKTIK INDUSTRI]** enam pilar AWS Well-Architected (trade-off eksplisit; *security* dan *operational excellence* umumnya tidak ditukar), **[PRAKTIK INDUSTRI]** STRIDE Microsoft untuk enumerasi ancaman, dan **[PRAKTIK INDUSTRI]** *Production Readiness Review* Kubernetes yang menuntut observability, scalability, failure mode, dependensi, dan rollback sebelum implementasi ([AWS Definitions](https://docs.aws.amazon.com/wellarchitected/latest/framework/definitions.md), [Microsoft STRIDE](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats), [KEP template](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md)).

### Cited Findings
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** AWS Well-Architected Framework berbasis **enam pilar**: *operational excellence, security, reliability, performance efficiency, cost optimization, sustainability*; definisi operasionalnya mencakup "run workloads effectively, gain insight into their operations", reliability mencakup "operate and test the workload through its total lifecycle", dan cost optimization "deliver business value at the lowest price point"; **"When architecting workloads, you make trade-offs between pillars based on your business context ... Security and operational excellence are generally not traded-off against the other pillars"** — [AWS, "Well-Architected Framework — Definitions"](https://docs.aws.amazon.com/wellarchitected/latest/framework/definitions.md); [AWS, "AWS Well-Architected"](https://aws.amazon.com/architecture/well-architected/).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Microsoft Threat Modeling Tool adalah elemen SDL untuk mengidentifikasi mitigasi **sejak awal ketika masih murah**, dengan **STRIDE**: **Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege** — [Microsoft Learn, "Threat Modeling Tool threats"](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** KEP PRR menanyakan secara eksplisit: *"Will enabling / using this feature result in any new API calls?"*, *"increasing size or count of the existing API objects"*, *"non-negligible increase of resource usage (CPU, RAM, disk, IO)"*, *"resource exhaustion of some node resources"*, *"What are other known failure modes?"* (dengan template Detection / Mitigations / Diagnostics / Testing), *"Does this feature depend on any specific services?"*, *"What are the SLIs ... to determine the health of the service?"*, dan *"What specific metrics should inform a rollback?"* — [Kubernetes Enhancements, "KEP-NNNN template README"](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** KEP juga meminta `Upgrade / Downgrade Strategy`, `Version Skew Strategy`, `Rollout, Upgrade and Rollback Planning` (*"How can a rollout or rollback fail? Can it impact already running workloads?"*, *"Were upgrade and rollback tested?"*), serta `Implementation History` untuk mencatat kapan desain diterima/digantikan — [Kubernetes Enhancements, "KEP-NNNN template README"](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** arc42 §11 meminta daftar risiko/technical debt **berurutan prioritas** beserta tindakan meminimalkan/mitigasi/menghindari; arc42 §9 menuntut keputusan dapat **"comprehend and retrace"**; arc42 §8 mengingatkan untuk hanya memilih *crosscutting concepts* yang paling dibutuhkan — [arc42 §11](https://docs.arc42.org/section-11/); [arc42 §9](https://docs.arc42.org/section-9/); [arc42 §8](https://docs.arc42.org/section-8/).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** arc42 §5 (relevance over completeness), C4 (context+container cukup untuk kebanyakan tim), dan Microsoft ("Avoid trying to complete one of these aspects before you start another") secara bersamaan memberi dasar anti-*big design up front* — [arc42 §5](https://docs.arc42.org/section-5/); [C4 model, "Diagrams"](https://c4model.com/diagrams); [Microsoft Learn, "Model your app's architecture"](https://learn.microsoft.com/en-us/visualstudio/modeling/model-your-app-s-architecture?view=visualstudio).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Microsoft ADR: keputusan yang tidak pernah dicatat **"will likely be forgotten, leading to repeated debates or later changes that unknowingly contradict the original intent"**; log harus *append-only* dan tersedia bersama dokumentasi workload untuk referensi, audit, dan incident response — [Microsoft Learn, "Maintain an architecture decision record (ADR)"](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** MADR bagian `Confirmation` dan `More Information` memungkinkan review memverifikasi bahwa implementasi masih sejalan dengan keputusan serta menentukan kapan keputusan ditinjau ulang — [adr.github.io/madr, "Full template"](https://adr.github.io/madr/).
- **[PRAKTIK INDUSTRI — DOKUMEN RESMI]** Portal Google *Engineering Practices* menyatakan kumpulan dokumen tersebut adalah praktik-general hasil pengalaman kolektif, termasuk *Code Review Guidelines* yang dipakai untuk menilai apakah perubahan "well-designed and appropriate for your system" — [Google, "Engineering Practices Documentation"](https://google.github.io/eng-practices/); [Google, "Code Review Guidelines — Introduction"](https://google.github.io/eng-practices/review/).

### Inferences
- **[INFERENSI PENELITI]** Urutan review yang efisien: (1) **concern & quality goals** → (2) **keputusan + alternatif + ADR** → (3) **struktur/perilaku/data** → (4) **STRIDE & privacy** → (5) **failure mode, observability, rollback** → (6) **scalability & biaya** → (7) **aksesibilitas/DoD**. Urutan ini mengikuti logika 42010 (concern → view → rationale) dan KEP PRR ([IEEE 42010:2022](https://standards.ieee.org/ieee/42010/6846/), [KEP](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md)).
- **[INFERENSI PENELITI]** Review harus menghasilkan **keputusan terdokumentasi** (approve / approve-with-conditions / reject + ADR baru), bukan sekadar komentar; bila ada perubahan arah, status ADR lama menjadi `Superseded` dengan tautan dua arah ([Microsoft ADR](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record), [arc42 §9](https://docs.arc42.org/section-9/)).
- **[INFERENSI PENELITI]** Biaya dan sustainability adalah **trade-off yang harus ditulis**, bukan diabaikan; AWS menyatakan trade-off mengikuti konteks bisnis, tetapi keamanan dan operational excellence umumnya tidak dikorbankan ([AWS Definitions](https://docs.aws.amazon.com/wellarchitected/latest/framework/definitions.md)).

### Inferences (lanjutan): Checklist review

- [ ] **Konteks & ruang lingkup** — Goals, non-goals, constraints, dan 3–5 quality goals dengan skenario terukur ada serta disetujui stakeholder — [arc42, "1. Introduction and Goals"](https://docs.arc42.org/section-1/); [React RFC template](https://raw.githubusercontent.com/reactjs/rfcs/main/0000-template.md).
- [ ] **Keputusan & rasional** — Setiap keputusan signifikan punya ADR berstatus jelas, alternatif yang ditolak, konsekuensi positif/negatif, dan `Confirmation` — [adr.github.io/madr](https://adr.github.io/madr/); [Microsoft Learn, "Maintain an ADR"](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record); [arc42 §9](https://docs.arc42.org/section-9/).
- [ ] **Struktur (HLD/LLD/C4)** — Context + Container ada; Component/Code hanya bila menambah nilai; kedalaman LLD dipilih berdasarkan relevansi/risiko, bukan kelengkapan — [C4 model, "Diagrams"](https://c4model.com/diagrams); [arc42 §5](https://docs.arc42.org/section-5/).
- [ ] **Perilaku & data** — Sequence/state/ER mencakup use case kritis, start/stop, dan **skenario error/exception**, dengan invariants serta pemetaan building block ke infrastruktur — [arc42 §6](https://docs.arc42.org/section-6/); [arc42 §7](https://docs.arc42.org/section-7/); [OMG UML 2.5.1](https://www.omg.org/spec/UML/2.5.1/).
- [ ] **Keamanan / STRIDE** — Enam kategori ditinjau dengan kontrol, pemilik, dan status `OPEN/MITIGATED`; identifikasi ancaman dilakukan sejak desain awal — [Microsoft Learn, "Threat Modeling Tool threats"](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats); [KEP template, "Risks and Mitigations"](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md).
- [ ] **Failure mode & reliability** — Daftar failure mode memuat Detection, Mitigations, Diagnostics, Testing; dampak pada beban kerja berjalan dan jalur upgrade→downgrade→upgrade dijelaskan — [KEP template, "Troubleshooting" & "Rollout, Upgrade and Rollback Planning"](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md); [AWS, "Definitions — Reliability"](https://docs.aws.amazon.com/wellarchitected/latest/framework/definitions.md).
- [ ] **Observability & operability** — SLI/SLO, cara operator mengetahui fitur aktif & sehat, dashboard, dan playbook tersedia sebelum implementasi — [KEP template, "Monitoring Requirements"](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md); [AWS, "Definitions — Operational excellence"](https://docs.aws.amazon.com/wellarchitected/latest/framework/definitions.md).
- [ ] **Rollout / rollback** — Mekanisme enable/disable, metrik pemicu rollback, konsekuensi re-enable, dan dampak pada state yang sudah berjalan tertulis — [KEP template, "Feature Enablement and Rollback"](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md).
- [ ] **Data migration & kompatibilitas** — Transformasi state, backfill, rekonsiliasi/integritas, pemulihan state, dan `Upgrade / Downgrade Strategy` / `Version Skew Strategy` tertulis — [KEP template, "Design Details"](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md).
- [ ] **Scalability & resources** — Pertambahan panggilan/objek, CPU/RAM/disk/IO, dan potensi *resource exhaustion* dievaluasi, termasuk kasus patologis — [KEP template, "Scalability"](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md).
- [ ] **Biaya & sustainability** — Estimasi biaya dan trade-off antar pilar dicatat; keamanan dan operational excellence tidak dikorbankan demi biaya — [AWS, "Well-Architected Framework — Definitions"](https://docs.aws.amazon.com/wellarchitected/latest/framework/definitions.md).
- [ ] **Dependensi** — Dampak outage dan degradasi tiap dependensi eksternal/opsional didokumentasikan — [KEP template, "Dependencies"](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md).
- [ ] **Risiko & technical debt** — Daftar berurutan prioritas beserta mitigasi; tidak ada konsekuensi yang sengaja/disengaja disembunyikan — [arc42 §11](https://docs.arc42.org/section-11/); [Microsoft Learn, "Maintain an ADR"](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record).
- [ ] **UI/UX & aksesibilitas** — Matriks state lengkap, token bukan hardcoded, WCAG 2.2 AA + reduced-motion sebagai kebijakan internal masuk DoD — [Material Design 3, "Design tokens"](https://m3.material.io/foundations/design-tokens/overview); [W3C, "WCAG 2.2"](https://www.w3.org/TR/WCAG22/); [Apple HIG, "Accessibility"](https://developer.apple.com/design/human-interface-guidelines/accessibility).
- [ ] **Kesegaran artefak** — Setiap diagram punya pemilik, versi, tanggal verifikasi, dan tautan ke ADR/design doc yang masih aktif — [INFERENSI PENELITI] dari [C4 model, "Diagrams"](https://c4model.com/diagrams), [arc42 §5](https://docs.arc42.org/section-5/), dan [KEP "Implementation History"](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md).

### Inferences (lanjutan): Anti-pattern yang sering terjadi

- **Big Design Up Front (BUPF):** memaksa seluruh Level 4 C4, semua skenario runtime, atau semua *crosscutting topics* selesai sebelum ada kode/umpan balik. **[INFERENSI PENELITI]** Bertentangan dengan [C4 "you don't need to use all 4 levels"](https://c4model.com/diagrams), [arc42 §5 "prefer relevance over completeness"](https://docs.arc42.org/section-5/), [arc42 §6 "representative selection"](https://docs.arc42.org/section-6/), [arc42 §8 "DO NOT ATTEMPT to cover all"](https://docs.arc42.org/section-8/), dan [Microsoft "Avoid trying to complete one of these aspects before you start another"](https://learn.microsoft.com/en-us/visualstudio/modeling/model-your-app-s-architecture?view=visualstudio).
- **Diagram basi / tanpa pemilik:** diagram tidak berversi, tidak bertanggal, dan tetap dipakai setelah keputusan berubah. **[INFERENSI PENELITI]** Lawannya adalah `Implementation History` KEP dan *append-only decision log* Microsoft yang menautkan record lama ke penggantinya ([KEP template](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md), [Microsoft ADR](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)).
- **Keputusan tanpa catatan:** pilihan teknologi/struktur hanya terlihat di implementasi sehingga memicu debat berulang dan perubahan yang tanpa sadar bertentangan dengan niat awal. **[PRAKTIK INDUSTRI]** Ini dikatakan eksplisit oleh [Microsoft Learn, "Maintain an architecture decision record (ADR)"](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record) dan [adr.github.io](https://adr.github.io/).
- **Menyunting ADR yang sudah `Accepted`:** menghapus jejak rasional lama. **[PRAKTIK INDUSTRI]** Microsoft: *"Don't go back and edit accepted records ... write a new record that supersedes the original and link the two together"* ([Microsoft ADR](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)); arc42 juga meminta referensi ke pengganti ([arc42 §9](https://docs.arc42.org/section-9/)).
- **Hanya mencatat konsekuensi positif:** ADR/arc42 dan MADR sama-sama meminta konsekuensi baik, buruk, **dan netral**, serta tradeoff dan *confidence level* ([arc42 §9](https://docs.arc42.org/section-9/), [MADR 4.0.0](https://github.com/adr/madr/blob/4.0.0/template/adr-template.md), [Microsoft ADR](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)).
- **Alternatif yang ditolak tanpa alasan / "do nothing" tidak dievaluasi:** melemahkan *rationale* yang dituntut 42010 dan membuat motivasi tidak bisa dipakai bila desain ditolak ([ISO 42010 Conceptual Model](http://www.iso-architecture.org/42010/cm/), [React RFC](https://raw.githubusercontent.com/reactjs/rfcs/main/0000-template.md), [Rust RFC](https://raw.githubusercontent.com/rust-lang/rfcs/master/0000-template.md), [KEP "Alternatives"](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md)).
- **Observability, rollback, dan failure mode ditunda sampai menjelang rilis:** **[INFERENSI PENELITI]** KEP PRR mensyaratkannya sebelum `implementable`, dan AWS menempatkan operational excellence/reliability sebagai pilar sejak desain ([KEP template](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md), [AWS Definitions](https://docs.aws.amazon.com/wellarchitected/latest/framework/definitions.md)).
- **Hardcoded style & state yang tidak lengkap:** menggantikan token dengan nilai literal, hanya menggambar happy path, serta tidak menyediakan empty/loading/error. **[INFERENSI PENELITI]** Bertentangan dengan [Material tokens](https://m3.material.io/foundations/design-tokens/overview), [Material progress indicators](https://m3.material.io/components/progress-indicators/guidelines), [Apple HIG Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback), dan [WCAG 2.2 §4.1.3](https://www.w3.org/TR/WCAG22/).
- **Over-claim aksesibilitas:** menyatakan `reduced motion` atau `Focus Appearance` sebagai "wajib AA", memakai badge konformasi tanpa bukti, atau menganggap pemeriksaan statis cukup. **[INFERENSI PENELITI]** Koreksi: 2.3.3 dan 2.4.13 berlevel **AAA**, `prefers-reduced-motion` masih **Working Draft**, W3C tidak memverifikasi klaim, dan ARIA 1.2 menyatakan aksesibilitas konten interaktif tidak dapat dikonfirmasi hanya dengan static checks ([W3C new-in-22](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/), [Media Queries Level 5](https://www.w3.org/TR/mediaqueries-5/#prefers-reduced-motion), [W3C WAI](https://www.w3.org/WAI/WCAG2AA-Conformance), [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/)).
- **Menyamakan C4/UML/ER dengan standar wajib:** **[INFERENSI PENELITI]** C4 adalah pendekatan resmi pembuatnya yang *notation/tooling independent*, dan ISO/IEC/IEEE 42010:2022 sengaja tidak menetapkan notasi; menjadikannya "kepatuhan standar" adalah kategori keliru ([c4model.com](https://c4model.com/), [IEEE SA](https://standards.ieee.org/ieee/42010/6846/)).
- **Mengorbankan keamanan/operational excellence demi biaya tanpa catatan:** **[PRAKTIK INDUSTRI]** AWS menyatakan kedua pilar tersebut *"generally not traded-off against the other pillars"* ([AWS Definitions](https://docs.aws.amazon.com/wellarchitected/latest/framework/definitions.md)).

### Gaps
- **[INFERENSI PENELITI]** Istilah "big design up front", "diagram basi", dan "keputusan tanpa catatan" **tidak didefinisikan secara normatif** oleh standar resmi; ketiganya dirumuskan di sini sebagai inferensi dari anjuran C4/arc42/Microsoft/KEP. Hanya "keputusan tanpa catatan" yang memiliki pernyataan eksplisit di dokumentasi Microsoft ([Microsoft ADR](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)).
- **[INFERENSI PENELITI]** Tidak ditemukan ambang biaya, latensi, atau kapasitas universal untuk "lolos review"; AWS memberi kerangka trade-off, KEP memberi pertanyaan, keduanya menyerahkan angka ke konteks organisasi ([AWS Definitions](https://docs.aws.amazon.com/wellarchitected/latest/framework/definitions.md), [KEP "Scalability"](https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md)).
- **[INFERENSI PENELITI]** Halaman spesifik `https://google.github.io/eng-practices/review/reviewer/look-for.html` menghasilkan 404 saat di-fetch; klaim Google di bagian ini dibatasi pada portal utama dan halaman `review/` yang muncul di hasil pencarian resmi ([Google eng-practices](https://google.github.io/eng-practices/), [Google review](https://google.github.io/eng-practices/review/)).
- **[INFERENSI PENELITI]** `https://docs.aws.amazon.com/wellarchitected/latest/framework/definitions.html` hanya mengembalikan banner cookie; isi keenam pilar diverifikasi dari versi `.md` resmi yang berhasil diambil ([AWS Definitions (.md)](https://docs.aws.amazon.com/wellarchitected/latest/framework/definitions.md)).
