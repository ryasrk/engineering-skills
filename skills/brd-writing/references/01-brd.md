# BRD (Business Requirements Document)

> **Catatan cakupan (2024–2026).** Catatan ini hanya membahas BRD: posisi, batas dokumen, struktur, kualitas kebutuhan bisnis, tata kelola persetujuan, dan RTM sebagai *mekanisme keterhubungan*. Tidak dibahas isi FSD, desain sistem/UI, prosedur testing, laporan harian, struktur folder/repo, atau API versioning. Sebutan FSD/desain/test case di bawah hanya untuk menjelaskan **batas serah terima** dan **kolom referensi RTM**, bukan membahas praktiknya.
>
> **Legenda sitasi.** **[S]** = standar resmi/lembaga standar; **[P]** = dokumentasi resmi badan profesi/vendor/proyek (primer organisasi, bukan standar formal); **[I]** = praktik industri/opini/panduan penerapan yang disusun peneliti. Setiap klaim normatif diberi nama dokumen dan URL lengkap. Praktik yang dirumuskan peneliti ditandai **[I]** dengan dasar standar yang mendasarinya agar tidak dianggap sebagai ketentuan standar.

## Apa landasan normatif dan status standar yang berlaku 2024–2026?

### Takeaway

"BRD" adalah nama artefak yang lazim dipakai industri; standar formal tidak selalu memakai akronim itu. Rujukan normatif paling dekat adalah **Business Requirements Specification (BRS)** dalam ISO/IEC/IEEE 29148:2018, sedangkan IIBA memakai konsep *business requirements* dan *Requirements Life Cycle Management*.

### Cited Findings

- **[S] ISO/IEC/IEEE 29148:2018, *Systems and software engineering — Life cycle processes — Requirements engineering*, edisi 2, terbit 30 November 2018, status *active/approved*** — menetapkan proses, *information items*, isi, dan format terkait requirements; mendefinisikan "construct of a good requirement" serta atribut dan karakteristik requirement; proses diterapkan iteratif dan rekursif sepanjang life cycle. IEEE mencantumkan tanggal publikasi 30 November 2018 dan status aktif — [IEEE Xplore: ISO/IEC/IEEE 29148:2018](https://ieeexplore.ieee.org/document/8559686); ringkasan ruang lingkup resmi ISO — [ISO/IEC JTC 1/SC 7: ISO/IEC/IEEE 29148:2018](https://committee.iso.org/fr/standard/72089.html?browse=ics).
- **[S] ISO/IEC/IEEE 29148:2018, daftar isi yang dipublikasikan DIN** — memuat **8.2 Business requirements specification** (8.2.1 General, 8.2.2 BRS example outline) dan **9.3 Business requirements specification (BRS) content** (9.3.1 BRS overview, 9.3.2 Business purpose, 9.3.3 Business scope). Ini bukti primer bahwa standar mengenal spesifikasi kebutuhan bisnis pada level terpisah dari spesifikasi kebutuhan stakeholder/system — [DIN: Table of contents ISO/IEC/IEEE 29148:2018 (E)](https://www.din.de/de/mitwirken/normenausschuesse/nia/veroeffentlichungen/wdc-beuth:din21:299567544/toc-3025650/download).
- **[S] ISO/IEC/IEEE 15288:2023, edisi 2, terbit Mei 2023** — menetapkan kerangka proses life cycle sistem, melibatkan stakeholder, dan berlaku sepanjang *conception* sampai *retirement*; standar ini **tidak** menetapkan model life cycle, metodologi, teknik, maupun nama/format/content eksplisit *information item* (yang terakhir dirujuk ke ISO/IEC/IEEE 15289). Dengan demikian, 15288 memberi kerangka proses, bukan模板 BRD — [ISO: ISO/IEC/IEEE 15288:2023](https://committee.iso.org/standard/81702.html?browse=ics).
- **[S] ISO 21502:2020, edisi 1, terbit Desember 2020** — memberi *guidance* praktik manajemen proyek yang dianggap bekerja baik, untuk organisasi serta pendekatan predictive/incremental/iterative/adaptive/hybrid/agile; ini **guidelines**, bukan spesifikasi dokumen BRD. Daftar isi resmi memuat 4.3.2 *Business case* dan 7.10 *Change control* — [ISO: ISO 21502:2020](https://www.iso.org/standard/74947.html); [ISO/TC 258: Published ISO 21502](https://committee.iso.org/sites/tc258/home/projects/published/iso-21502.html); [DIN: Table of contents ISO 21502:2020 (E)](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download).
- **[P] IIBA, *A Guide to the Business Analysis Body of Knowledge (BABOK Guide) v3*, 2015** — merupakan rilis ke-4 BABOK (v1.4 2005, v1.6 2006, v2 2009, v3 2015) dan memperkenalkan lima perspektif termasuk Agile — [IIBA: BABOK Guide v3 Celebrates 1 Year Anniversary](https://production.iiba.org/professional-development/knowledge-centre/ba-connection/babok-guide-v3-celebrates-1-year-anniversary/). Untuk 2024–2026, IIBA juga mempublikasikan **[P] *The Business Analysis Standard*** dengan penekanan pada *outcome-driven focus*, hasil terukur, dan nilai — [IIBA: The Business Analysis Standard](http://go.iiba.org/The-Standard-Corporate); [IIBA: The Business Analysis Standard (Preface, PDF)](https://www.iiba.org/globalassets/business-analysis-resources/the-business-analysis-standard/files/the-business-analysis-standard.pdf).
- **[P] IIBA, *Guide to Business Data Analytics*, daftar isi Requirements Life Cycle Management** — mencantumkan 5.1 Trace Requirements, 5.2 Maintain Requirements, 5.3 Prioritize Requirements, 5.4 Assess Requirements Changes, 5.5 Approve Requirements — [IIBA: Guide to Business Data Analytics](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/).
- **[P] PMI, *PMBOK Guide – Seventh Edition FAQs*, 1 Juli 2021** — edisi ke-7 ditujukan agar relevan untuk predictive, hybrid, dan adaptive, serta menempatkan fokus pada *project outcomes* selain deliverables — [PMI: PMBOK Guide Seventh Edition FAQs](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmbok-guide-public-faqs-1-july-2021.pdf).
- **[P] Microsoft Learn, *Tracking requirements*** — menyatakan asosiasi requirement ke test case, bug, dan perubahan kode merupakan aspek fundamental traceability; merekomendasikan Azure DevOps sebagai salah satu alat, dengan alternatif Jira sesuai kebijakan organisasi — [Microsoft Learn: Tracking requirements](https://learn.microsoft.com/en-us/training/modules/analysis-solution-intelligent-order-management/tracking-requirements).
- **[P] Atlassian/Confluence, *Business requirements document template*** — mendefinisikan template BRD sebagai dokumen *essential needs and expectations* proyek untuk keselarasan stakeholder, serta menyebut manfaat konsistensi, kejelasan, komunikasi, dan pengurangan omisi/inconsistency — [Atlassian: Business requirements document template](https://www.atlassian.com/software/confluence/resources/guides/how-to/business-requirements).

### Inferences

- **[I]** Karena ISO 29148 memakai **BRS**, sedangkan IIBA memakai istilah konseptual **business requirements**, "BRD" sebaiknya dinyatakan sebagai **nama artefak organisasi** yang *memetakan* ke BRS/business requirements—bukan diklaim sebagai istilah yang diwajibkan oleh standar. Dasar: [DIN ToC 29148](https://www.din.de/de/mitwirken/normenausschuesse/nia/veroeffentlichungen/wdc-beuth:din21:299567544/toc-3025650/download); [IIBA BABOK v3](https://production.iiba.org/professional-development/knowledge-centre/ba-connection/babok-guide-v3-celebrates-1-year-anniversary/).
- **[I]** Untuk 2024–2026, rujukan yang sah: BABOK v3 tetap referensi BA IIBA; standar sistem yang masih aktif adalah 29148:2018 dan 15288:2023; ISO 21502:2020 berstatus *to be revised*; PMBOK 7 tetap edisi PMI yang dirujuk FAQ resmi. Jangan mengutip angka/edisi standar tanpa mengecek halaman katalog ISO/IEEE/PMI karena status revisi dapat berubah.

### Gaps

- Teks lengkap BABOK v3, ISO 29148:2018, ISO 21502:2020, dan PMBOK 7 berbayar/terbatas; catatan ini hanya mengutip **halaman katalog resmi, abstract, daftar isi resmi, dan materi terbuka resmi**. Karena itu, daftar *semantic* klausul di bawah yang tidak ditampilkan penuh oleh halaman resmi ditandai sebagai inferensi/praktik, bukan kutipan verbatim.
- Tidak ditemukan satu standar resmi yang menetapkan **akronim "BRD"**, **jumlah section BRD**, atau **urutan sign-off** secara universal. Bagian struktur dan workflow di bawah adalah template praktis peneliti, bukan kewajiban standar.

## 1. Definisi dan batas tegas: BRD vs business case, PRD, SRS/FSD, project charter

### Takeaway

BRD berada pada level **kebutuhan organisasi/inisiatif perubahan**: *why* dan *what outcome*, bukan justifikasi investasi, bukan otorisasi proyek, dan bukan spesifikasi solusi. Batas paling penting: business case menjawab kelayakan/nilai, charter memberi otorisasi, BRD menyatakan kebutuhan bisnis, sedangkan PRD/SRS/FSD sudah memasuki kebutuhan produk/solusi.

### Cited Findings

- **[P] IIBA, *REQUIREMENTS – INFOGRAPH*** — *business requirements* adalah pernyataan level tinggi tentang tujuan, objektif, atau kebutuhan enterprise; dokumen ini mengingatkan agar kebutuhan bisnis **tidak memuat elemen solusi**; *stakeholder requirements* menjembatani business requirements dan *solution requirements*; *solution requirements* terbagi menjadi functional dan non-functional/quality/service requirements — [IIBA: REQUIREMENTS – INFOGRAPH](https://www.iiba.org/contentassets/38e412c7b77d456297d953de5bf5ca61/requirement-types-infograph.pdf).
- **[P] IIBA, *The Business Analysis Standard* (Prancis-Kanada), bagian Requirement/Design** — menyebut "Objectif ou besoin", "Valeur", "Description du changement", serta memperoleh persetujuan atas *requirements and designs* sebelum aktivitas lanjutan; BACCM memodelkan *change, need, solution, stakeholder, value, context* — [IIBA: The Business Analysis Standard (fr-CA PDF)](https://www.iiba.org/globalassets/business-analysis-resources/the-business-analysis-standard/files/the-business-analysis-standard-fr-ca.pdf); [IIBA: Preface PDF](https://www.iiba.org/globalassets/business-analysis-resources/the-business-analysis-standard/files/the-business-analysis-standard.pdf).
- **[S] ISO/IEC/IEEE 29148:2018** — memisahkan *Business Requirements Specification (BRS)* dari spesifikasi requirement lain dalam struktur klausul 8/9; BRS memuat *overview, business purpose, business scope* — [DIN: ToC ISO/IEC/IEEE 29148:2018](https://www.din.de/de/mitwirken/normenausschuesse/nia/veroeffentlichungen/wdc-beuth:din21:299567544/toc-3025650/download); [IEEE: 29148-2018](https://ieeexplore.ieee.org/document/8559686).
- **[S] ISO/IEC/IEEE 15288:2023** — proses dapat dipilih dan diterapkan sepanjang life cycle, termasuk *conception*; standar tidak menetapkan satu model life cycle/metodologi — [ISO: 15288:2023](https://committee.iso.org/standard/81702.html?browse=ics).
- **[P] PMI, *What makes a project charter work*** — sponsor **mengotorisasi** charter, sedangkan penyusunan sering dilakukan project manager; charter dapat berupa satu halaman, email, atau rekaman formal asalkan jelas mengotorisasi proyek, menetapkan pemimpin, dan batas kewenangan keputusan — [PMI: What makes a project charter work](https://www.pmi.org/blog/project-charter).
- **[P] PMI, *And away we go*** — *business case* merupakan masukan penting bagi project charter karena menunjukkan target finansial yang harus dicapai agar proyek dianggap sukses — [PMI: And away we go](https://www.pmi.org/learning/library/concise-project-charter-team-focus-2157).
- **[S] ISO 21502:2020** — daftar isi resmi memuat **4.3.2 Business case** dan **7.10 Change control**; standar bersifat guidance dan berlaku lintas pendekatan delivery — [ISO: 21502:2020](https://www.iso.org/standard/74947.html); [DIN: ToC 21502:2020](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download).
- **[P] Atlassian/Confluence, *BRD template*** — BRD diposisikan sebagai dokumen *essential needs and expectations* agar stakeholder memiliki referensi bersama; versi lokal Atlassian menyebut section tipikal: business objectives, project scope, functional/non-functional requirements, key stakeholders, limitations/assumptions — [Atlassian: BRD template](https://www.atlassian.com/software/confluence/resources/guides/how-to/business-requirements); [Atlassian CDN: 中文版 BRD template](https://wac-cdn-a.atlassian.com/zh/software/confluence/resources/guides/how-to/business-requirements).

### Inferences

Tabel berikut **[I] adalah sintesis praktis peneliti** dari pemisahan level requirement IIBA/ISO dan peran artefak PMI/ISO; bukan tabel verbatim dari satu standar. Dasar: [IIBA infograph](https://www.iiba.org/contentassets/38e412c7b77d456297d953de5bf5ca61/requirement-types-infograph.pdf), [DIN ToC 29148](https://www.din.de/de/mitwirken/normenausschuesse/nia/veroeffentlichungen/wdc-beuth:din21:299567544/toc-3025650/download), [PMI charter](https://www.pmi.org/blog/project-charter), [ISO 21502](https://www.iso.org/standard/74947.html).

| Artefak | Pertanyaan inti | Batas tegas | Penulis tipikal **[I]** | Pemilik/akuntabel **[I]** | Dasar |
|---|---|---|---|---|---|
| **Business case** | "Mengapa investasi ini layak?" | Kelayakan, manfaat, target nilai/biaya; **bukan** daftar kebutuhan operasional. Menjadi input ke charter. | Sponsor/portfolio/PMO dengan dukungan BA/Finance | Sponsor/eksekutif pemilik manfaat | [PMI](https://www.pmi.org/learning/library/concise-project-charter-team-focus-2157); [ISO 21502 ToC](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download) |
| **Project charter** | "Siapa mengotorisasi proyek dan apa kewenangannya?" | Otorisasi + pemimpin + kewenangan + ringkasan tujuan; **bukan** requirement detail. | PM menyusun; sponsor mengotorisasi | Sponsor/initiator | [PMI](https://www.pmi.org/blog/project-charter) |
| **BRD / BRS** | "Kebutuhan bisnis/outcome apa yang harus dipenuhi?" | Tujuan, ruang lingkup bisnis, kebutuhan bisnis, KPI, kriteria penerimaan bisnis, asumsi/constraint/risiko/dependensi; **hindari desain solusi**. | Business Analyst / Product Owner bisnis, hasil elicitation dengan SME | Sponsor bisnis / *business owner* sebagai pemilik; BA sebagai *document owner/custodian* | [IIBA infograph](https://www.iiba.org/contentassets/38e412c7b77d456297d953de5bf5ca61/requirement-types-infograph.pdf); [DIN ToC 29148](https://www.din.de/de/mitwirken/normenausschuesse/nia/veroeffentlichungen/wdc-beuth:din21:299567544/toc-3025650/download) |
| **PRD** | "Produk/apa pengalaman pengguna yang dibangun?" | Kebutuhan produk, persona, user flows, prioritas; turunan dari kebutuhan bisnis. **Nama dan isi PRD tidak distandardisasi ISO/IIBA; ini praktik industri.** | Product Manager/Product Owner | Head of Product / Product Owner | [Atlassian BRD](https://www.atlassian.com/software/confluence/resources/guides/how-to/business-requirements); [IIBA infograph](https://www.iiba.org/contentassets/38e412c7b77d456297d953de5bf5ca61/requirement-types-infograph.pdf) |
| **SRS / FSD** | "Apa requirement sistem/solusi secara terverifikasi?" | *Stakeholder/system/solution requirements*, bukan lagi *business need*; berada **di luar cakupan catatan ini**. | BA/System Analyst/Engineering | Pemilik produk/sistem atau arsitek sesuai tata kelola | [DIN ToC 29148](https://www.din.de/de/mitwirken/normenausschuesse/nia/veroeffentlichungen/wdc-beuth:din21:299567544/toc-3025650/download); [IIBA infograph](https://www.iiba.org/contentassets/38e412c7b77d456297d953de5bf5ca61/requirement-types-infograph.pdf) |

**Aturan batas yang direkomendasikan [I]:** kalimat BRD boleh menyebut *capability/outcome*, tetapi jika sudah menyebut teknologi, field, screen, endpoint, algoritma, atau urutan UI, itu **solusi terselubung** dan harus dipindahkan ke artefak downstream. Dasar normatif: larangan memuat *solution elements* pada business requirements — [IIBA infograph](https://www.iiba.org/contentassets/38e412c7b77d456297d953de5bf5ca61/requirement-types-infograph.pdf).

### Gaps

- PMI/IIBA/ISO tidak memberi satu matriks universal "penulis vs pemilik" untuk **PRD**; kolom penulis/pemilik PRD di atas adalah **[I] praktik industri**, bukan sitasi normatif.
- Atlassian menyertakan *functional/non-functional requirements* dalam template BRD-nya; ini **berpotensi tumpang tindih** dengan klasifikasi IIBA yang menempatkan functional/non-functional sebagai *solution requirements*. Untuk menjaga batas tegas, template di bawah memakai istilah **kebutuhan bisnis** dan menolak requirement solusi. Konflik ini dicatat eksplisit: [Atlassian](https://www.atlassian.com/software/confluence/resources/guides/how-to/business-requirements) vs [IIBA](https://www.iiba.org/contentassets/38e412c7b77d456297d953de5bf5ca61/requirement-types-infograph.pdf).

## 2. Posisi BRD dalam siklus hidup requirement dan struktur section wajib

### Takeaway

BRD/BRS berada di hulu: dari *need/change* dan *business case/charter* menuju kebutuhan bisnis yang disetujui, lalu menjadi sumber traceability bagi requirement stakeholder/solution. *Lifecycle management* tidak berhenti di approval: requirement harus ditelusuri, dipelihara, diprioritaskan, dinilai perubahannya, dan disetujui ulang.

### Cited Findings

- **[S] ISO/IEC/IEEE 29148:2018** — proses requirement diterapkan **iteratif dan rekursif** sepanjang life cycle; standar menentukan proses, *information items*, isi, dan formatnya — [IEEE: 29148-2018](https://ieeexplore.ieee.org/document/8559686); [ISO committee: 29148](https://committee.iso.org/fr/standard/72089.html?browse=ics).
- **[S] ISO/IEC/IEEE 15288:2023** — kerangka proses mencakup *conception, development, production, utilization, support, retirement*; proses dapat dipilih, diterapkan iteratif/konkuren, dan rekursif pada elemen sistem; tidak ada satu model life cycle yang diwajibkan — [ISO: 15288:2023](https://committee.iso.org/standard/81702.html?browse=ics).
- **[P] IIBA, *Guide to Business Data Analytics* ToC** — urutan tugas RLM: Trace → Maintain → Prioritize → Assess Requirements Changes → Approve Requirements — [IIBA](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/).
- **[P] IIBA, *The Business Analysis Standard* Preface** — BACCM memusatkan *change, need, solution, stakeholder, value, context*; standar terbaru menekankan *measurable outcomes* dan nilai — [IIBA Standard Preface](https://www.iiba.org/globalassets/business-analysis-resources/the-business-analysis-standard/files/the-business-analysis-standard.pdf); [IIBA Standard landing](http://go.iiba.org/The-Standard-Corporate).
- **[P] PMI, PMBOK 7 FAQ** — fokus pada *project outcomes* selain deliverables, serta relevansi untuk predictive/hybrid/adaptive — [PMI FAQ](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmbok-guide-public-faqs-1-july-2021.pdf).
- **[S] ISO 21502:2020** — *business case* (4.3.2) dan *change control* (7.10: framework, identifying/assessing requests, planning implementation) tercantum dalam daftar isi resmi — [DIN ToC](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download); [ISO](https://www.iso.org/standard/74947.html).
- **[S] ISO/IEC/IEEE 29148:2018 ToC** — section minimum BRS yang tampil dari daftar isi: **BRS overview, Business purpose, Business scope**; klausul 8.2.2 memuat *BRS example outline* — [DIN ToC](https://www.din.de/de/mitwirken/normenausschuesse/nia/veroeffentlichungen/wdc-beuth:din21:299567544/toc-3025650/download).
- **[P] Atlassian BRD template** — section yang disebut: business objectives, project scope, key stakeholders, limitations/assumptions, serta (pada versi praktiknya) functional/non-functional requirements — [Atlassian](https://www.atlassian.com/software/confluence/resources/guides/how-to/business-requirements); [Atlassian CDN zh](https://wac-cdn-a.atlassian.com/zh/software/confluence/resources/guides/how-to/business-requirements).

### Inferences

- **[I] Peta posisi (bukan diagram standar):** `Need/Change → Business case → Project charter → BRD/BRS (business purpose, scope, business requirements, KPI, acceptance) → [serah terima ke artefak downstream] → RTM → perubahan/approval ulang`. Rujukan: [ISO 21502 ToC](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download), [PMI charter](https://www.pmi.org/blog/project-charter), [IIBA RLM](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/), [ISO 29148](https://ieeexplore.ieee.org/document/8559686).
- **[I] Section "wajib"** di bawah adalah **kontrak dokumentasi organisasi** yang disusun peneliti, bukan daftar wajib ISO. Yang benar-benar dapat ditunjuk dari standar hanyalah *overview/purpose/scope* BRS; sisanya melengkapi tata kelola agar BRD dapat diverifikasi, diprioritaskan, dan disetujui. Dasar: [DIN ToC 29148](https://www.din.de/de/mitwirken/normenausschuesse/nia/veroeffentlichungen/wdc-beuth:din21:299567544/toc-3025650/download), [IIBA RLM](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/), [Atlassian](https://www.atlassian.com/software/confluence/resources/guides/how-to/business-requirements).

| Section | Fungsi minimum | Dasar |
|---|---|---|
| Metadata & status | ID, versi, status Draft/Review/Approved/Baselined, tanggal, pemilik | [I] dari [IIBA RLM](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/) + [ISO 21502 change control](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download) |
| Latar belakang & *need/change* | Masalah/pemicu perubahan, konteks organisasi | [BACCM, IIBA Standard](https://www.iiba.org/globalassets/business-analysis-resources/the-business-analysis-standard/files/the-business-analysis-standard.pdf) |
| Tujuan bisnis & nilai | Objectives, outcome terukur, value | [IIBA Standard](http://go.iiba.org/The-Standard-Corporate); [PMI PMBOK 7 FAQ](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmbok-guide-public-faqs-1-july-2021.pdf) |
| *Current vs future state* | Proses/metrik saat ini vs target; gap | [I] praktik, didasari [BACCM need/change/value](https://www.iiba.org/globalassets/business-analysis-resources/the-business-analysis-standard/files/the-business-analysis-standard.pdf) |
| Business scope (in/out) | Batas proses, unit bisnis, data/otoritas, eksklusi | [S] *Business scope* BRS — [DIN ToC 29148](https://www.din.de/de/mitwirken/normenausschuesse/nia/veroeffentlichungen/wdc-beuth:din21:299567544/toc-3025650/download) |
| Stakeholder + RACI | Siapa consulted/informed/responsible/accountable | [I] dari [PMI charter](https://www.pmi.org/blog/project-charter) dan [ISO 15288 stakeholder involvement](https://committee.iso.org/standard/81702.html?browse=ics) |
| Kebutuhan bisnis bernomor | BR-001…, atomic, terverifikasi, prioritas | [IIBA infograph](https://www.iiba.org/contentassets/38e412c7b77d456297d953de5bf5ca61/requirement-types-infograph.pdf); [IEEE 29148 good requirement](https://ieeexplore.ieee.org/document/8559686) |
| Asumsi, constraint, dependensi | Kondisi yang dipercaya, batas yang mengikat, pihak/artefak eksternal | [P] Atlassian menyebut limitations/assumptions — [Atlassian](https://www.atlassian.com/software/confluence/resources/guides/how-to/business-requirements); [S] [ISO 21502](https://www.iso.org/standard/74947.html) |
| Risiko bisnis | Risiko terhadap nilai/outcome, owner, mitigasi | [I] dari [ISO 21502 guidance on control](https://www.iso.org/standard/74947.html) |
| KPI/OKR & baseline/target | Metrik, baseline, target, horizon, sumber data | [IIBA outcome-driven](http://go.iiba.org/The-Standard-Corporate); [PMI outcomes](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmbok-guide-public-faqs-1-july-2021.pdf) |
| Kriteria penerimaan bisnis | Kondisi objektif yang dapat diverifikasi sponsor | [I] dari *construct of a good requirement* — [IEEE 29148](https://ieeexplore.ieee.org/document/8559686) |
| Estimasi nilai/biaya | Manfaat, biaya, sumber estimasi, tingkat keyakinan | [PMI business case](https://www.pmi.org/learning/library/concise-project-charter-team-focus-2157); [ISO 21502 4.3.2](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download) |
| RTM reference | ID BRD ↔ ID artefak downstream | [Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/analysis-solution-intelligent-order-management/tracking-requirements); [IIBA Trace Requirements](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/) |
| Approval/sign-off | Nama, peran, keputusan, tanggal, versi yang disetujui | [IIBA Approve Requirements](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/); [ISO 21502 7.10](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download) |
| Riwayat perubahan | Versi, alasan, section/ID terdampak, referensi CR | [IIBA Maintain/Assess Changes](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/); [ISO 21502 7.10](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download) |

### Gaps

- Daftar isi ISO 29148 yang tersedia publik hanya menampilkan sebagian sub-klausul 9.3; **isi lengkap BRS outline 8.2.2/9.3 tidak terverifikasi verbatim**. Karena itu jangan mengklaim "ISO mewajibkan 15 section BRD".
- RACI bukan istilah yang ditemukan ditetapkan oleh ISO 29148/15288 dalam sumber terbuka yang dibaca; RACI di template adalah **[I] praktik tata kelola**.

## 3. Cara menulis kebutuhan bisnis yang jelas, atomic, SMART/INVEST, dan dapat diverifikasi

### Takeaway

Gunakan kalimat requirement tunggal, bernomor, bebas solusi, dengan metrik dan kondisi verifikasi. ISO 29148 menyediakan konstruk *good requirement* dan karakteristiknya; SMART/INVEST adalah **heuristik industri**, bukan ketentuan standar.

### Cited Findings

- **[S] ISO/IEC/IEEE 29148:2018** — *Abstract* resmi IEEE menyatakan standar "defines the construct of a good requirement, provides attributes and characteristics of requirements" — [IEEE Xplore: 29148-2018](https://ieeexplore.ieee.org/document/8559686); [ISO committee: scope](https://committee.iso.org/fr/standard/72089.html?browse=ics).
- **[P] IIBA infograph** — business requirements adalah pernyataan higher-level goals/objectives/needs enterprise dan **harus diwaspadai agar tidak berisi solution elements**; stakeholder requirements menjembatani ke solution requirements — [IIBA: REQUIREMENTS – INFOGRAPH](https://www.iiba.org/contentassets/38e412c7b77d456297d953de5bf5ca61/requirement-types-infograph.pdf).
- **[P] IIBA Standard / BABOK v3** — BACCM memakai *change, need, solution, stakeholder, value, context*; BABOK v3 adalah rilis 2015 yang masih menjadi rujukan IIBA — [IIBA Standard Preface](https://www.iiba.org/globalassets/business-analysis-resources/the-business-analysis-standard/files/the-business-analysis-standard.pdf); [IIBA BABOK v3 anniversary](https://production.iiba.org/professional-development/knowledge-centre/ba-connection/babok-guide-v3-celebrates-1-year-anniversary/).
- **[P] Microsoft Learn** — asosiasi requirement ke test case, bug, dan perubahan kode disebut sebagai *fundamental aspect* traceability — [Microsoft Learn: Tracking requirements](https://learn.microsoft.com/en-us/training/modules/analysis-solution-intelligent-order-management/tracking-requirements).
- **[P] IIBA RLM ToC** — *Maintain, Prioritize, Assess Changes, Approve* merupakan tugas lifecycle yang melekat pada requirement, sehingga atribut prioritas/status/versi perlu ada sejak awal — [IIBA: Guide to Business Data Analytics](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/).
- **[I] Praktik industri (bukan standar): SMART** lazim dipakai untuk tujuan/metrik yang *Specific, Measurable, Achievable, Relevant, Time-bound*; **INVEST** lazim dipakai untuk unit kerja/requirement yang *Independent, Negotiable, Valuable, Estimable, Small, Testable*. Tidak ditemukan halaman resmi ISO/IIBA/PMI yang menetapkan keduanya sebagai kewajiban BRD; keduanya dipakai di sini sebagai **checklist tambahan** yang selaras dengan konstruk *good requirement* ISO 29148 — [IEEE 29148](https://ieeexplore.ieee.org/document/8559686), [IIBA outcome-driven Standard](http://go.iiba.org/The-Standard-Corporate).

### Inferences

**Pola kalimat yang direkomendasikan [I]** (bukan kutipan standar):

> `BR-{{NNN}} — {{Unit bisnis/aktor organisasi}} harus dapat {{outcome/capability bisnis}} untuk {{proses/konteks}} sehingga {{nilai/KPI}} berubah dari {{baseline}} menjadi {{target}} paling lambat {{tanggal/periode}}; diverifikasi melalui {{sumber data/keputusan bisnis}}; prioritas {{MoSCoW/urutan}}; status {{Draft|Review|Approved|Baselined}}; sumber {{stakeholder/dokumen}}; terkait {{KPI-ID}} / {{AC-ID}}.`

Dasar: konstruk *good requirement* dan karakteristik/atribut ISO 29148 ([IEEE](https://ieeexplore.ieee.org/document/8559686)), larangan solusi terselubung IIBA ([infograph](https://www.iiba.org/contentassets/38e412c7b77d456297d953de5bf5ca61/requirement-types-infograph.pdf)), fokus outcome terukur IIBA/PMI ([IIBA Standard](http://go.iiba.org/The-Standard-Corporate); [PMI PMBOK 7 FAQ](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmbok-guide-public-faqs-1-july-2021.pdf)), serta lifecycle atribut IIBA ([RLM](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/)).

**Contoh perbaikan [I]:**

| Buruk **[I]** | Mengapa buruk | Perbaikan **[I]** |
|---|---|---|
| "Sistem harus cepat dan user-friendly." | Ambiguous, tidak terukur, memaksa "sistem" dan kualitas solusi masuk ke BRD | `BR-014 — Unit Layanan Pelanggan harus dapat menyelesaikan verifikasi data pelanggan dalam ≤ {{X}} menit per kasus untuk {{periode}}, diukur dari {{sumber data}}; target {{Y}}%; diverifikasi melalui laporan KPI {{KPI-ID}}.` |
| "Buat dashboard real-time dengan filter tanggal." | Solusi terselubung (dashboard/filter = desain), bukan kebutuhan bisnis | `BR-015 — Manajer Operasional harus memperoleh status {{objek bisnis}} dengan keterkinian ≤ {{X}} menit agar keputusan {{keputusan}} dapat diambil pada {{siklus}}; sumber kebenaran {{sumber}}; kriteria {{AC-ID}}.` |
| "Semua proses harus otomatis, efisien, dan sesuai best practice." | Kata universal, tidak atomic, tidak dapat diverifikasi | Pecah menjadi `BR-016`, `BR-017`, `BR-018`, masing-masing satu proses + satu metrik + satu sumber verifikasi. |
| "Jika memungkinkan, tingkatkan kepuasan pelanggan." | "Jika memungkinkan" memberi jalan keluar; tidak ada baseline/target/horizon | `BR-019 — {{Unit}} harus menaikkan {{metrik kepuasan}} dari {{baseline}} ke {{target}} pada {{periode}}, diukur {{instrumen/sumber}}; asumsi {{A-ID}}.` |

**Checklist kualitas per requirement [I]:** satu ID; satu subjek organisasi; satu outcome; tanpa kata "dll/cepat/mudah/optimal/sebagaimana mestinya"; ada baseline/target/unit/waktu; ada sumber verifikasi; ada prioritas, status, sumber, dan owner; tidak menyebut UI/teknologi/API/field; dapat ditelusuri ke tujuan dan kriteria penerimaan bisnis. Rujukan pendukung: [IEEE 29148](https://ieeexplore.ieee.org/document/8559686), [IIBA infograph](https://www.iiba.org/contentassets/38e412c7b77d456297d953de5bf5ca61/requirement-types-infograph.pdf), [IIBA RLM](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/), [Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/analysis-solution-intelligent-order-management/tracking-requirements).

### Gaps

- Daftar **lengkap sembilan karakteristik individual requirement** ISO 29148:2018 tidak dapat dikutip verbatim dari teks standar terbuka; catatan ini hanya menyatakan bahwa standar *memiliki* konstruk/atribut/karakteristik tersebut. Jika laporan final membutuhkan nama atribut satu per satu, harus mengacu pada salinan berlisensi ISO/IEEE 29148:2018 — [IEEE Xplore](https://ieeexplore.ieee.org/document/8559686).
- SMART/INVEST tidak memiliki rujukan standar resmi dalam sumber yang diverifikasi; karenanya ditandai **[I]**, bukan **[S]**.

## 4. Requirement Traceability Matrix (RTM): BRD → FSD → desain → test case

### Takeaway

RTM bukan dokumen testing dan bukan desain; di sini RTM dipakai sebagai **peta referensi satu arah dari keputusan bisnis ke artefak downstream**. Minimum yang harus ada: ID requirement bisnis, tujuan/KPI, kriteria penerimaan bisnis, referensi FSD/desain/test case, status, dan versi baseline.

### Cited Findings

- **[P] IIBA, RLM 5.1 Trace Requirements** — *Trace Requirements* merupakan tugas eksplisit dalam Requirements Life Cycle Management, berdampingan dengan Maintain, Prioritize, Assess Changes, Approve — [IIBA: Guide to Business Data Analytics](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/).
- **[P] Microsoft Learn, *Tracking requirements*** — "A fundamental aspect of requirements traceability is the association of the requirements to test cases, bugs, and code changes"; requirement utama perlu dikaitkan dengan task/assignment; disebut *quality traceability, bug traceability, source traceability*; Azure DevOps direkomendasikan, Jira disebut alternatif sesuai kebijakan organisasi — [Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/analysis-solution-intelligent-order-management/tracking-requirements).
- **[S] ISO/IEC/IEEE 29148:2018** — menetapkan *required information items* dan *required contents* yang dihasilkan proses requirements, serta panduan formatnya; prosesnya iteratif/rekursif sepanjang life cycle — [ISO committee scope](https://committee.iso.org/fr/standard/72089.html?browse=ics); [IEEE abstract](https://ieeexplore.ieee.org/document/8559686).
- **[S] ISO/IEC/IEEE 15288:2023** — pertukaran informasi antar *acquirer, supplier, stakeholder* merupakan tujuan kerangka proses; standar tidak menetapkan nama/format/content eksplisit *information item* — [ISO: 15288:2023](https://committee.iso.org/standard/81702.html?browse=ics).
- **[P] Atlassian BRD template** — template digunakan sebagai referensi bersama dan mengurangi risiko omisi/inconsistency, yang merupakan rasio d'être RTM sebagai pengontrol kelengkapan — [Atlassian](https://www.atlassian.com/software/confluence/resources/guides/how-to/business-requirements).

### Inferences

**Contoh tabel RTM [I]** — hanya *identifier* downstream yang dicantumkan; isi FSD, desain, dan test case **sengaja tidak dibahas** sesuai batas topik. Dasar: [IIBA Trace Requirements](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/), [Microsoft Learn association to test cases](https://learn.microsoft.com/en-us/training/modules/analysis-solution-intelligent-order-management/tracking-requirements), [ISO 29148 information items](https://committee.iso.org/fr/standard/72089.html?browse=ics).

| BRD ID | Pernyataan kebutuhan bisnis (ringkas) | Tujuan / KPI | Kriteria penerimaan bisnis | FSD ref | Desain ref | Test case ref | Status | Baseline | Pemilik | Catatan perubahan |
|---|---|---|---|---|---|---|---|---|---|---|
| `BR-001` | `{{outcome bisnis 1}}` | `GOAL-{{NN}}` / `KPI-{{NN}}` | `AC-{{NN}}` | `{{FSD-ID}}` | `{{DESIGN-ID}}` | `{{TC-ID}}` | `{{Approved}}` | `{{v1.0}}` | `{{business owner}}` | `{{CR-001 atau —}}` |
| `BR-002` | `{{outcome bisnis 2}}` | `GOAL-{{NN}}` / `KPI-{{NN}}` | `AC-{{NN}}` | `{{FSD-ID}}` | `{{DESIGN-ID}}` | `{{TC-ID}}` | `{{Draft}}` | `{{—}}` | `{{business owner}}` | `{{alasan belum ada turunan}}` |
| `BR-003` | `{{outcome bisnis 3}}` | `GOAL-{{NN}}` / `KPI-{{NN}}` | `AC-{{NN}}` | `{{FSD-ID}}` | `{{DESIGN-ID}}` | `{{TC-ID}}` | `{{Baselined}}` | `{{v1.2}}` | `{{business owner}}` | `{{CR-002}}` |

**Aturan RTM yang direkomendasikan [I]:**
1. **Satu baris per BR ID**, bukan satu baris per paragraf; ID tidak dipakai ulang setelah dihapus. Dasar [IIBA Maintain Requirements](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/).
2. **Arah jejak dua arah**: dari BR ke turunan, dan dari turunan kembali ke BR/KPI/AC. Dasar asosiasi requirement–test case–bug–code changes [Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/analysis-solution-intelligent-order-management/tracking-requirements).
3. **Kolom ref downstream hanya ID + versi**; konten FSD/desain/test case berada di dokumen pemiliknya masing-masing. Dasar [ISO 15288 tidak menetapkan format information item](https://committee.iso.org/standard/81702.html?browse=ics).
4. **Baris tanpa turunan harus punya status/alasan** agar bukan *silent orphan*; baris turunan tanpa BR harus ditolak atau diminta CR. Dasar [IIBA Assess Requirements Changes](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/) dan [Atlassian mengurangi omisi](https://www.atlassian.com/software/confluence/resources/guides/how-to/business-requirements).
5. RTM diperbarui pada **setiap perubahan yang disetujui**, lalu versi BRD dan baseline RTM direferensikan bersama pada sign-off. Dasar [IIBA RLM](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/) dan [ISO 21502 7.10](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download).

### Gaps

- Tidak ada template RTM universal yang diwajibkan ISO/IIBA; tabel di atas **[I]** disusun agar selaras dengan tugas *Trace Requirements* dan rekomendasi Microsoft.
- Microsoft Learn menyarankan asosiasi ke *code changes*; karena topik struktur repo/API berada di peneliti lain, catatan ini **tidak** mengembangkan kolom tersebut lebih jauh.

## 5. Change control, versioning, dan approval workflow BRD

### Takeaway

Status dokumen bukan sekadar label: `Draft → Review → Approved → Baselined` harus mengikat **versi yang disetujui**, **siapa yang berwenang**, dan **riwayat CR**. IIBA menempatkan *Assess Requirements Changes* dan *Approve Requirements* dalam lifecycle; ISO 21502 menyediakan kerangka *change control* pada level proyek.

### Cited Findings

- **[P] IIBA RLM ToC** — `5.2 Maintain Requirements`, `5.3 Prioritize Requirements`, `5.4 Assess Requirements Changes`, `5.5 Approve Requirements` — [IIBA: Guide to Business Data Analytics](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/).
- **[P] IIBA Standard (fr-CA)** — memperoleh **approval untuk requirements and designs** agar aktivitas setelahnya dapat dilanjutkan; task card memuat stakeholder, description du changement, input/output — [IIBA Standard fr-CA](https://www.iiba.org/globalassets/business-analysis-resources/the-business-analysis-standard/files/the-business-analysis-standard-fr-ca.pdf).
- **[S] ISO 21502:2020 ToC** — `7.10 Change control` mencakup `7.10.2 Establishing a change control framework`, `7.10.3 Identifying and assessing change requests`, `7.10.4 Planning the implementation of change requests` — [DIN ToC ISO 21502:2020](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download); status/guidance resmi — [ISO 21502](https://www.iso.org/standard/74947.html).
- **[S] ISO/IEC/IEEE 29148:2018** — menentukan *required information items* serta isinya dan proses iterative/recursive sepanjang life cycle; dengan demikian perubahan requirement bukan aktivitas ad-hoc di luar proses — [ISO committee](https://committee.iso.org/fr/standard/72089.html?browse=ics); [IEEE](https://ieeexplore.ieee.org/document/8559686).
- **[P] PMI, *What makes a project charter work*** — **sponsor mengotorisasi**, PM sering menyusun; ini analogi tata kelola yang jelas: penyusun ≠ pemberi otorisasi — [PMI](https://www.pmi.org/blog/project-charter).
- **[P] Microsoft Learn** — Azure DevOps/Jira dapat dipilih **sesuai kebijakan organisasi**; alat bukan penentu tata kelola — [Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/analysis-solution-intelligent-order-management/tracking-requirements).
- **[P] Atlassian BRD template** — BRD sebagai *common reference point* yang dikonsultasikan dan diperbarui bersama, serta mendorong konsistensi lintas proyek — [Atlassian](https://www.atlassian.com/software/confluence/resources/guides/how-to/business-requirements).

### Inferences

**Workflow yang direkomendasikan [I]** (bukan urutan yang diwajibkan standar). Dasar: [IIBA RLM](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/), [IIBA Standard](https://www.iiba.org/globalassets/business-analysis-resources/the-business-analysis-standard/files/the-business-analysis-standard-fr-ca.pdf), [ISO 21502 7.10](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download), [PMI sponsor authority](https://www.pmi.org/blog/project-charter).

| Status | Makna | Penanggung jawab **[I]** | Keluar menuju |
|---|---|---|---|
| `Draft` | BA menyusun; ID requirement boleh berubah; belum ada komitmen | Business Analyst | `Review` |
| `Review` | Stakeholder, SME, Finance/Risk/Legal/Compliance memeriksa; komentar dan dampak dicatat | BA memfasilitasi; reviewer sesuai RACI | `Approved` atau kembali `Draft` |
| `Approved` | Versi **`vX.Y`** disetujui; requirement siap ditelusuri ke artefak downstream | Sponsor bisnis / business owner + approver wajib | `Baselined` |
| `Baselined` | Pasangan **BRD vX.Y + RTM vX.Y** dibekukan sebagai acuan perubahan | PMO/Configuration owner mencatat; business owner tetap akuntabel | Perubahan hanya lewat `CR-{{NNN}}` |

**Aturan sign-off [I]:**
- Yang menandatangani **bukan sekadar "tim IT"**: minimal **Sponsor/Business owner** (akuntabel nilai & scope), **Finance/Value owner** (estimasi nilai/biaya), **Risk/Compliance owner** bila ada dampak regulasi, dan **BA** sebagai penyusun/custodian. PM/PMO mencatat baseline dan CR. Dasar peran: [PMI sponsor authorization](https://www.pmi.org/blog/project-charter), [PMI business case financial targets](https://www.pmi.org/learning/library/concise-project-charter-team-focus-2157), [IIBA stakeholder approval](https://www.iiba.org/globalassets/business-analysis-resources/the-business-analysis-standard/files/the-business-analysis-standard-fr-ca.pdf).
- **Setiap CR** memuat: ID, peminta, alasan bisnis, requirement/section terdampak, dampak KPI/nilai/biaya/risiko/dependensi/RTM, keputusan, approver, tanggal, versi baru. Dasar [ISO 21502 7.10.3–7.10.4](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download) dan [IIBA 5.4](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/).
- **Versioning [I]:** `v0.x` = Draft/Review; `v1.0` = Approved baseline pertama; `v1.y` = perubahan minor setelah CR; `v2.0` = perubahan scope/tujuan/KPI material. Nomor ini **konvensi peneliti**, bukan aturan ISO — [ISO 29148 information items](https://committee.iso.org/fr/standard/72089.html?browse=ics).
- **Jangan menimpa baseline**: simpan `Approved vX.Y` sebagai referensi; perubahan menghasilkan versi baru sehingga riwayat keputusan dapat diaudit. Dasar [IIBA Maintain/Assess/Approve](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/) + [ISO 21502 change control framework](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download).

### Gaps

- ISO 21502:2020 adalah **guidance high-level**; ia tidak menetapkan empat status `Draft/Review/Approved/Baselined`, format nomor versi, atau daftar jabatan signer. Semua itu **[I] praktik industri**.
- Sumber resmi yang dibaca tidak memberi ketentuan bahwa BRD harus ditandatangani secara elektronik/legal; kebutuhan tersebut bergantung kebijakan organisasi/regulasi dan dinyatakan sebagai gap, bukan klaim.

## 6. Template BRD lengkap siap pakai, checklist review, dan anti-pattern

### Takeaway

Berikut template utama yang **lengkap** dengan placeholder `{{...}}`, mencakup seluruh section yang diminta, tabel RACI, kebutuhan bisnis bernomor, KPI/OKR, acceptance criteria, RTM ringkas, approval, dan change log. Salin blok Markdown apa adanya lalu isi placeholder. **Seluruh heading di dalam code fence berikut adalah isi template, bukan section dari catatan riset ini.**

### Cited Findings

- **[S] ISO/IEC/IEEE 29148:2018** — BRS memiliki *overview, business purpose, business scope* dalam daftar isi resmi — [DIN ToC](https://www.din.de/de/mitwirken/normenausschuesse/nia/veroeffentlichungen/wdc-beuth:din21:299567544/toc-3025650/download).
- **[P] IIBA infograph** — business requirements tidak boleh memuat solution elements; functional/non-functional adalah solution requirements — [IIBA infograph](https://www.iiba.org/contentassets/38e412c7b77d456297d953de5bf5ca61/requirement-types-infograph.pdf).
- **[P] Atlassian BRD template** — tujuan, scope, stakeholder, limitations/assumptions sebagai section tipikal BRD — [Atlassian](https://www.atlassian.com/software/confluence/resources/guides/how-to/business-requirements).
- **[P] IIBA RLM** — Trace, Maintain, Prioritize, Assess Changes, Approve — [IIBA](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/).
- **[S] ISO 21502:2020** — business case dan change control framework/assessment/implementation planning — [DIN ToC](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download).
- **[P] Microsoft Learn** — asosiasi requirement ke test case/bug/code change sebagai aspek fundamental traceability — [Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/analysis-solution-intelligent-order-management/tracking-requirements).
- **[P] PMI** — charter mengotorisasi proyek, business case memberi target nilai/finansial — [PMI charter](https://www.pmi.org/blog/project-charter); [PMI business case](https://www.pmi.org/learning/library/concise-project-charter-team-focus-2157).

### Template utama: BRD siap pakai

```markdown
# Business Requirements Document (BRD) — {{NAMA_INISIATIF}}

| Metadata | Nilai |
|---|---|
| Document ID | `BRD-{{KODE_PROYEK}}-{{NNN}}` |
| Versi | `{{v0.1}}` |
| Status | `{{Draft|Review|Approved|Baselined}}` |
| Tanggal dokumen | `{{YYYY-MM-DD}}` |
| Pemilik bisnis (Accountable) | `{{NAMA}}, {{JABATAN}}, {{UNIT}}` |
| Penyusun / Document custodian | `{{NAMA_BUSINESS_ANALYST}}` |
| Sponsor | `{{NAMA_SPONSOR}}` |
| Referensi business case | `{{BC-ID}}, {{VERSI}}, {{URL/LOKASI_RESMI}}` |
| Referensi project charter | `{{CHARTER-ID}}, {{VERSI}}, {{TANGGAL_OTORISASI}}` |
| Baseline aktif | `{{v1.0 / belum ada}}` |
| Baseline RTM terkait | `{{RTM-ID}}, {{VERSI}}` |
| Klasifikasi informasi | `{{Publik|Internal|Rahasia}}` |
| Standar acuan | `IIBA BABOK Guide v3 (2015); IIBA The Business Analysis Standard; ISO/IEC/IEEE 29148:2018; ISO/IEC/IEEE 15288:2023; ISO 21502:2020; PMI PMBOK Guide 7th Edition` |

---

## 1. Ringkasan eksekutif

- **Need / pemicu perubahan:** `{{Masalah atau peluang bisnis dalam 2–3 kalimat; sebutkan siapa terdampak dan sejak kapan}}`
- **Outcome yang diharapkan:** `{{Hasil bisnis terukur, bukan fitur atau sistem}}`
- **Keputusan yang diminta dari sponsor:** `{{Setujui ruang lingkup / setujui baseline / setujui alokasi nilai-biaya}}`
- **Estimasi nilai dan biaya ringkas:** `{{Manfaat: ...; Biaya: ...; Sumber/keyakinan: ...}}`
- **Risiko utama:** `{{R-001, R-002}}`
- **Versi yang diajukan untuk approval:** `{{vX.Y}}`

---

## 2. Latar belakang dan konteks

| Aspek | Uraian |
|---|---|
| Konteks organisasi | `{{Unit, produk/layanan, segmen, kondisi pasar/regulasi}}` |
| Pemicu perubahan | `{{Regulasi / keluhan / target strategi / inefisiensi / peluang}}` |
| Bukti awal | `{{Sumber data, periode, angka baseline; cantumkan sumber internal resmi}}` |
| Dampak jika tidak berubah | `{{Dampak finansial, operasional, kepatuhan, atau reputasi}}` |
| Dokumen pendukung | `{{Daftar: nama dokumen + URL/lokasi + versi}}` |

---

## 3. Tujuan bisnis dan nilai

| ID | Tujuan bisnis | Alasan / nilai | Terkait strategi | Terukur melalui |
|---|---|---|---|---|
| `GOAL-001` | `{{Tujuan 1}}` | `{{Nilai bagi organisasi/pelanggan}}` | `{{OKR/strategi-ID}}` | `KPI-{{NN}}` |
| `GOAL-002` | `{{Tujuan 2}}` | `{{Nilai}}` | `{{OKR/strategi-ID}}` | `KPI-{{NN}}` |

**Pernyataan nilai:** `{{Dengan tercapainya GOAL-001..GOAL-N, {{UNIT}} memperoleh {{MANFAAT}} sebesar {{NILAI}} dalam {{HORIZON}}, dengan asumsi {{A-ID}} dan batas {{C-ID}}.}}`

---

## 4. Current state vs Future state

| Dimensi | Current state | Future state | Gap | Bukti/target |
|---|---|---|---|---|
| Proses | `{{Proses saat ini}}` | `{{Proses/outcome yang diharapkan pada level bisnis}}` | `{{Gap}}` | `{{Sumber}}` |
| Metrik | `{{Baseline + periode + sumber}}` | `{{Target + periode + sumber}}` | `{{Delta}}` | `KPI-{{NN}}` |
| Peran & kewenangan | `{{Siapa memutuskan sekarang}}` | `{{Siapa memutuskan nanti}}` | `{{Perubahan kewenangan}}` | `{{Referensi}}` |
| Data/informasi bisnis | `{{Kondisi sekarang}}` | `{{Kondisi yang dibutuhkan, tanpa menyebut desain teknis}}` | `{{Gap}}` | `{{Sumber}}` |
| Regulasi/kebijakan | `{{Kondisi sekarang}}` | `{{Kepatuhan yang harus dipenuhi}}` | `{{Gap}}` | `{{Regulasi/kebijakan + versi}}` |

> **Batas:** bagian ini menjelaskan kondisi dan hasil bisnis. Jangan menuliskan screen, field, arsitektur, endpoint, atau algoritma.

---

## 5. Ruang lingkup bisnis (In / Out)

### 5.1 In scope

| ID | Area/proses | Unit | Batas yang termasuk | Alasan |
|---|---|---|---|---|
| `SC-IN-001` | `{{Area}}` | `{{Unit}}` | `{{Batas proses/periode/segmen}}` | `{{Kaitan ke GOAL-ID}}` |
| `SC-IN-002` | `{{Area}}` | `{{Unit}}` | `{{Batas}}` | `{{Kaitan}}` |

### 5.2 Out of scope

| ID | Area yang dikecualikan | Alasan eksklusi | Pemilik keputusan | Tinjau ulang pada |
|---|---|---|---|---|
| `SC-OUT-001` | `{{Area/proses/segmen}}` | `{{Alasan bisnis}}` | `{{Jabatan}}` | `{{Tanggal/milestone}}` |
| `SC-OUT-002` | `{{Area}}` | `{{Alasan}}` | `{{Jabatan}}` | `{{Tanggal/milestone}}` |

### 5.3 Batas kewenangan dan keputusan bisnis

- Keputusan yang **boleh** diambil dalam inisiatif ini: `{{...}}`
- Keputusan yang **tetap** berada di luar inisiatif: `{{...}}`
- Pihak yang berwenang mengubah scope: `{{Sponsor / Change Board}}`

---

## 6. Stakeholder dan RACI

| ID | Stakeholder / peran | Interest | R | A | C | I | Kebutuhan informasi | Kanal / frekuensi |
|---|---|---|---|---|---|---|---|---|
| `ST-001` | `{{Sponsor bisnis}}` | `{{Tinggi}}` | `{{—}}` | `{{A}}` | `{{—}}` | `{{I}}` | `{{Ringkasan nilai, keputusan scope}}` | `{{...}}` |
| `ST-002` | `{{Business owner}}` | `{{Tinggi}}` | `{{R}}` | `{{A}}` | `{{C}}` | `{{I}}` | `{{Kebutuhan bisnis, KPI, AC}}` | `{{...}}` |
| `ST-003` | `{{Business Analyst}}` | `{{Tinggi}}` | `{{R}}` | `{{—}}` | `{{C}}` | `{{I}}` | `{{Draft, RTM, CR}}` | `{{...}}` |
| `ST-004` | `{{Finance}}` | `{{Sedang}}` | `{{R}}` | `{{—}}` | `{{C}}` | `{{I}}` | `{{Estimasi nilai/biaya}}` | `{{...}}` |
| `ST-005` | `{{Risk / Compliance / Legal}}` | `{{Sesuai dampak}}` | `{{—}}` | `{{—}}` | `{{C}}` | `{{I}}` | `{{Constraint, risiko}}` | `{{...}}` |
| `ST-006` | `{{PM / PMO}}` | `{{Sedang}}` | `{{R}}` | `{{—}}` | `{{C}}` | `{{I}}` | `{{Baseline, CR, dependensi}}` | `{{...}}` |

**Legenda:** R = Responsible, A = Accountable (tepat satu A per keputusan utama), C = Consulted, I = Informed.

---

## 7. Kebutuhan bisnis (Business Requirements)

> Format setiap baris: **satu ID, satu outcome, satu metrik, satu sumber verifikasi, tanpa solusi terselubung.**

| ID | Kebutuhan bisnis (atomic) | Rationale | Prioritas | Sumber | Owner | Status | KPI | Acceptance | Dependensi |
|---|---|---|---|---|---|---|---|---|---|
| `BR-001` | `{{Unit}} harus dapat {{outcome}} untuk {{konteks}} sehingga {{KPI}} berubah dari {{baseline}} menjadi {{target}} paling lambat {{periode}}; diverifikasi melalui {{sumber data/keputusan}}.` | `{{GOAL-ID}}` | `{{Must|Should|Could|Won't}}` | `{{ST-ID / dokumen}}` | `{{ST-ID}}` | `{{Draft|Review|Approved|Baselined}}` | `KPI-{{NN}}` | `AC-{{NN}}` | `{{DEP-ID atau —}}` |
| `BR-002` | `{{...}}` | `{{GOAL-ID}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `KPI-{{NN}}` | `AC-{{NN}}` | `{{...}}` |
| `BR-003` | `{{...}}` | `{{GOAL-ID}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `KPI-{{NN}}` | `AC-{{NN}}` | `{{...}}` |

### 7.1 Kriteria penerimaan bisnis

| ID | Terkait | Kriteria penerimaan (dapat diverifikasi) | Bukti / sumber kebenaran | Ambang batas | Pihak yang menyatakan terpenuhi | Tanggal target |
|---|---|---|---|---|---|---|
| `AC-001` | `BR-001` | `{{Kondisi objektif yang harus benar agar nilai bisnis dinyatakan tercapai}}` | `{{Laporan/data keputusan resmi}}` | `{{≥/≤/target, unit, periode}}` | `{{Business owner}}` | `{{YYYY-MM-DD}}` |
| `AC-002` | `BR-002` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |

---

## 8. KPI / OKR dan pengukuran nilai

| ID | Objective / KPI | Definisi operasional | Baseline | Target | Unit | Horizon | Sumber data | Frekuensi | Owner | Terkait |
|---|---|---|---|---|---|---|---|---|---|---|
| `KPI-001` | `{{Nama KPI}}` | `{{Rumus/definisi, denominator, exclusion}}` | `{{Angka + periode}}` | `{{Angka}}` | `{{%|menit|Rupiah|jumlah}}` | `{{Q1 2026 / 12 bulan}}` | `{{Sistem/laporan resmi}}` | `{{Bulanan}}` | `{{Jabatan}}` | `BR-{{NNN}}, GOAL-{{NN}}` |
| `KPI-002` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |

**OKR opsional:** `Objective: {{...}} | Key Results: {{KR-1}}, {{KR-2}}, {{KR-3}} | Sumber: {{...}}`

---

## 9. Estimasi nilai, biaya, dan keyakinan

| Komponen | Estimasi | Satuan / periode | Sumber | Asumsi | Tingkat keyakinan | Owner validasi |
|---|---|---|---|---|---|---|
| Manfaat finansial | `{{...}}` | `{{...}}` | `{{Business case BC-ID}}` | `{{A-ID}}` | `{{Rendah|Sedang|Tinggi}}` | `{{Finance}}` |
| Manfaat non-finansial | `{{...}}` | `{{...}}` | `{{...}}` | `{{A-ID}}` | `{{...}}` | `{{Business owner}}` |
| Biaya inisiatif | `{{...}}` | `{{...}}` | `{{...}}` | `{{A-ID}}` | `{{...}}` | `{{Finance/PMO}}` |
| Biaya operasi berulang | `{{...}}` | `{{...}}` | `{{...}}` | `{{A-ID}}` | `{{...}}` | `{{Finance}}` |

**Catatan:** tabel ini merujuk business case, bukan menggantikannya. `{{Jelaskan perbedaan angka bila ada perubahan sejak business case disetujui.}}`

---

## 10. Asumsi, constraint, dependensi, dan risiko

### 10.1 Asumsi

| ID | Asumsi | Bukti / dasar | Dampak jika salah | Owner validasi | Tanggal validasi |
|---|---|---|---|---|---|
| `A-001` | `{{Kondisi yang dipercaya benar}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{YYYY-MM-DD}}` |
| `A-002` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |

### 10.2 Constraint

| ID | Constraint | Sumber normatif / keputusan | Konsekuensi pada scope | Tidak dapat dinegosiasi? |
|---|---|---|---|---|
| `C-001` | `{{Batas anggaran/regulasi/kebijakan/waktu}}` | `{{Dokumen + URL/versi}}` | `{{...}}` | `{{Ya|Tidak}}` |
| `C-002` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |

### 10.3 Dependensi

| ID | Dependensi | Pihak / artefak | Jenis | Dibutuhkan pada | Dampak jika terlambat | Owner |
|---|---|---|---|---|---|---|
| `DEP-001` | `{{...}}` | `{{...}}` | `{{Keputusan|Data|Regulasi|Vendor|Anggaran}}` | `{{Milestone/tanggal}}` | `{{...}}` | `{{...}}` |
| `DEP-002` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |

### 10.4 Risiko bisnis

| ID | Risiko | Penyebab | Dampak pada nilai/KPI | Probabilitas | Dampak | Mitigasi | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| `R-001` | `{{...}}` | `{{...}}` | `{{KPI-ID / GOAL-ID}}` | `{{Rendah|Sedang|Tinggi}}` | `{{Rendah|Sedang|Tinggi}}` | `{{...}}` | `{{...}}` | `{{Open|Mitigated|Accepted}}` |
| `R-002` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |

---

## 11. Referensi traceability (RTM ringkas)

> Kolom downstream memuat **ID saja**; isi FSD/desain/test case berada pada dokumen pemiliknya dan tidak dibahas dalam BRD ini.

| BRD ID | GOAL / KPI | AC | FSD ref | Desain ref | Test case ref | Status | Baseline | Catatan |
|---|---|---|---|---|---|---|---|---|
| `BR-001` | `GOAL-001 / KPI-001` | `AC-001` | `{{FSD-ID}}` | `{{DESIGN-ID}}` | `{{TC-ID}}` | `{{Approved}}` | `{{v1.0}}` | `{{...}}` |
| `BR-002` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| `BR-003` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |

**RTM lengkap:** `{{RTM-ID}}, {{VERSI}}, {{URL/LOKASI_RESMI}}`

---

## 12. Tata kelola, approval, dan sign-off

### 12.1 Status dan aturan perubahan

| Status | Definisi internal | Boleh diubah oleh | Keluar menuju |
|---|---|---|---|
| `Draft` | `{{...}}` | `{{BA}}` | `Review` |
| `Review` | `{{...}}` | `{{Reviewer sesuai RACI}}` | `Approved / Draft` |
| `Approved` | `{{Versi vX.Y disetujui}}` | `{{Hanya melalui CR}}` | `Baselined` |
| `Baselined` | `{{BRD vX.Y + RTM vX.Y dibekukan}}` | `{{Change Board / Sponsor}}` | `{{CR-NNN}}` |

### 12.2 Matriks approval

| Peran | Nama | Keputusan yang disetujui | Status input | Versi disetujui | Keputusan | Tanggal | Tanda tangan / referensi elektronik |
|---|---|---|---|---|---|---|---|
| Sponsor / Business owner | `{{NAMA}}` | `{{Scope, tujuan, nilai, AC}}` | `Review` | `{{vX.Y}}` | `{{Approve|Reject|Approve with conditions}}` | `{{YYYY-MM-DD}}` | `{{...}}` |
| Finance / Value owner | `{{NAMA}}` | `{{Estimasi nilai & biaya}}` | `Review` | `{{vX.Y}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| Risk / Compliance / Legal | `{{NAMA}}` | `{{Constraint & risiko}}` | `Review` | `{{vX.Y}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| Business Analyst | `{{NAMA}}` | `{{Kelengkapan & kualitas requirement}}` | `Review` | `{{vX.Y}}` | `{{...}}` | `{{...}}` | `{{...}}` |
| PM / PMO | `{{NAMA}}` | `{{Pencatatan baseline & CR}}` | `Approved` | `{{vX.Y}}` | `{{...}}` | `{{...}}` | `{{...}}` |

**Kondisi approval:** `{{Tuliskan kondisi jika "Approve with conditions", beserta owner dan tenggat.}}`

### 12.3 Change request

| CR ID | Peminta | Tanggal | Alasan bisnis | BR / section terdampak | Dampak KPI, nilai, biaya, risiko, RTM | Keputusan | Approver | Versi baru |
|---|---|---|---|---|---|---|---|---|
| `CR-001` | `{{...}}` | `{{YYYY-MM-DD}}` | `{{...}}` | `{{BR-002, §5, §8}}` | `{{...}}` | `{{Approve|Reject|Defer}}` | `{{...}}` | `{{vX.Y+1}}` |
| `CR-002` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` | `{{...}}` |

---

## 13. Riwayat perubahan

| Versi | Tanggal | Status | Penulis | Ringkasan perubahan | Section / ID terdampak | Referensi CR | Disetujui oleh |
|---|---|---|---|---|---|---|---|
| `v0.1` | `{{YYYY-MM-DD}}` | `Draft` | `{{...}}` | `{{Draft awal}}` | `{{Semua}}` | `—` | `—` |
| `v0.2` | `{{YYYY-MM-DD}}` | `Review` | `{{...}}` | `{{Perbaikan berdasarkan review}}` | `{{BR-001, KPI-001}}` | `—` | `—` |
| `v1.0` | `{{YYYY-MM-DD}}` | `Baselined` | `{{...}}` | `{{Approval baseline awal}}` | `{{Semua}}` | `{{CR-000 atau —}}` | `{{Sponsor}}` |
| `v1.1` | `{{YYYY-MM-DD}}` | `Baselined` | `{{...}}` | `{{...}}` | `{{...}}` | `CR-001` | `{{...}}` |

---

## 14. Lampiran dan daftar referensi

| ID | Nama dokumen | Versi / tanggal | URL atau lokasi resmi | Jenis |
|---|---|---|---|---|
| `REF-001` | `{{Business case}}` | `{{...}}` | `{{...}}` | `{{Internal}}` |
| `REF-002` | `{{Project charter}}` | `{{...}}` | `{{...}}` | `{{Internal}}` |
| `REF-003` | `IIBA, A Guide to the Business Analysis Body of Knowledge (BABOK Guide) v3` | `2015` | `https://production.iiba.org/professional-development/knowledge-centre/ba-connection/babok-guide-v3-celebrates-1-year-anniversary/` | `[P] Badan profesi` |
| `REF-004` | `ISO/IEC/IEEE 29148:2018, Requirements engineering` | `2018, ed. 2` | `https://ieeexplore.ieee.org/document/8559686` | `[S] Standar resmi` |
| `REF-005` | `ISO/IEC/IEEE 15288:2023, System life cycle processes` | `2023, ed. 2` | `https://committee.iso.org/standard/81702.html?browse=ics` | `[S] Standar resmi` |
| `REF-006` | `ISO 21502:2020, Guidance on project management` | `2020, ed. 1` | `https://www.iso.org/standard/74947.html` | `[S] Standar resmi` |
| `REF-007` | `PMI, PMBOK Guide – Seventh Edition FAQs` | `2021-07-01` | `https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmbok-guide-public-faqs-1-july-2021.pdf` | `[P] PMI` |
| `REF-008` | `Microsoft Learn, Tracking requirements` | `{{diakses YYYY-MM-DD}}` | `https://learn.microsoft.com/en-us/training/modules/analysis-solution-intelligent-order-management/tracking-requirements` | `[P] Vendor` |
| `REF-009` | `Atlassian, Business requirements document template` | `{{diakses YYYY-MM-DD}}` | `https://www.atlassian.com/software/confluence/resources/guides/how-to/business-requirements` | `[P] Vendor / praktik` |
```

### Inferences

- Template di atas **[I]** menggabungkan section minimum BRS ISO 29148 dengan kebutuhan tata kelola IIBA/ISO 21502 dan section praktik Atlassian; konflik *functional/non-functional* sengaja dihindari agar BRD tidak berubah menjadi spesifikasi solusi — [DIN ToC 29148](https://www.din.de/de/mitwirken/normenausschuesse/nia/veroeffentlichungen/wdc-beuth:din21:299567544/toc-3025650/download), [IIBA infograph](https://www.iiba.org/contentassets/38e412c7b77d456297d953de5bf5ca61/requirement-types-infograph.pdf), [Atlassian](https://www.atlassian.com/software/confluence/resources/guides/how-to/business-requirements), [ISO 21502 ToC](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download).
- Placeholder `{{...}}` sengaja dipertahankan di **setiap** tabel agar template dapat dipakai langsung, bukan sekadar kerangka heading.

---

### Checklist review

> **[I]** Checklist berikut disusun peneliti dari konstruk *good requirement* ISO 29148, larangan solusi terselubung IIBA, tugas RLM IIBA, dan kerangka change control ISO 21502. Bukan checklist sertifikasi resmi. Dasar: [IEEE 29148](https://ieeexplore.ieee.org/document/8559686), [IIBA infograph](https://www.iiba.org/contentassets/38e412c7b77d456297d953de5bf5ca61/requirement-types-infograph.pdf), [IIBA RLM](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/), [ISO 21502 ToC](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download).

- [ ] **Definisi & batas:** BRD menjawab *need/outcome*, bukan menggantikan business case atau charter; business case dan charter dirujuk dengan ID+versi. — [PMI charter](https://www.pmi.org/blog/project-charter); [ISO 21502](https://www.iso.org/standard/74947.html).
- [ ] **Tidak ada solusi terselubung:** tidak ada UI, field, endpoint, teknologi, algoritma, atau nama fitur pada `BR-xxx`. — [IIBA infograph](https://www.iiba.org/contentassets/38e412c7b77d456297d953de5bf5ca61/requirement-types-infograph.pdf).
- [ ] **Section inti lengkap:** overview/purpose/scope, tujuan, current–future, in/out, stakeholder+RACI, BR, asumsi/constraint/dependensi/risiko, KPI/OKR, AC, nilai/biaya, RTM, approval, change log. — [DIN ToC 29148](https://www.din.de/de/mitwirken/normenausschuesse/nia/veroeffentlichungen/wdc-beuth:din21:299567544/toc-3025650/download); [Atlassian](https://www.atlassian.com/software/confluence/resources/guides/how-to/business-requirements).
- [ ] **Atomic:** satu ID = satu outcome = satu pemilik; tidak ada "dan/atau" yang menggabungkan dua kebutuhan. — [IEEE 29148 good requirement](https://ieeexplore.ieee.org/document/8559686).
- [ ] **Terukur & terverifikasi:** setiap BR punya baseline/target/unit/periode, sumber kebenaran, dan `AC-ID`; tidak ada "cepat/mudah/optimal/dll/sebagaimana mestinya". — [IEEE 29148](https://ieeexplore.ieee.org/document/8559686); [IIBA outcome-driven](http://go.iiba.org/The-Standard-Corporate).
- [ ] **SMART/INVEST dipakai sebagai heuristik**, dan ditandai bukan kewajiban standar. — [IEEE 29148](https://ieeexplore.ieee.org/document/8559686).
- [ ] **KPI jelas definisinya:** rumus/denominator/exclusion, baseline, target, horizon, sumber data, owner. — [IIBA Standard](http://go.iiba.org/The-Standard-Corporate); [PMI PMBOK 7 outcomes](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmbok-guide-public-faqs-1-july-2021.pdf).
- [ ] **RACI valid:** tepat satu `A` untuk keputusan utama; reviewer risiko/finance/compliance hadir bila relevan. — [PMI sponsor authorization](https://www.pmi.org/blog/project-charter); [ISO 15288 stakeholder involvement](https://committee.iso.org/standard/81702.html?browse=ics).
- [ ] **Asumsi punya owner validasi**; constraint punya sumber normatif; dependensi punya tanggal dibutuhkan; risiko punya owner dan mitigasi. — [ISO 21502 guidance](https://www.iso.org/standard/74947.html).
- [ ] **Estimasi tidak menggantikan business case**, dan perbedaan angka sejak business case dijelaskan. — [PMI business case](https://www.pmi.org/learning/library/concise-project-charter-team-focus-2157); [ISO 21502 4.3.2](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download).
- [ ] **RTM dua arah:** setiap `BR` memiliki `GOAL/KPI/AC` dan ID downstream; setiap turunan dapat kembali ke `BR`; orphan diberi status/alasan. — [IIBA Trace Requirements](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/); [Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/analysis-solution-intelligent-order-management/tracking-requirements).
- [ ] **Approval mengikat versi:** tabel sign-off menyebut `vX.Y`, keputusan, tanggal, dan approver; baseline BRD dan RTM memiliki versi yang sama. — [IIBA Approve Requirements](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/); [ISO 21502 7.10](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download).
- [ ] **Perubahan lewat CR:** dampak terhadap KPI/nilai/biaya/risiko/RTM dinilai sebelum approve. — [ISO 21502 7.10.3–7.10.4](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download); [IIBA 5.4](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/).
- [ ] **Sumber primer dikutip:** klaim normatif memuat nama dokumen + URL; praktik industri ditandai `[I]`, standar ditandai `[S]`. — [IEEE 29148](https://ieeexplore.ieee.org/document/8559686); [ISO 29148 scope](https://committee.iso.org/fr/standard/72089.html?browse=ics).

---

### Anti-pattern yang sering terjadi

> **[I]** Daftar ini adalah sintesis peneliti tentang kegagalan yang *diturunkan* dari batas dan kewajiban pada sumber primer; bukan daftar kutipan verbatim satu dokumen. Dasar untuk setiap baris disertakan.

| Anti-pattern **[I]** | Mengapa merugikan | Gejala yang bisa dicek | Perbaikan **[I]** | Dasar |
|---|---|---|---|---|
| BRD dijadikan PRD/SRS: memuat screen, field, endpoint, atau teknologi | Mengunci solusi sebelum kebutuhan bisnis disepakati; menghilangkan ruang alternatif solusi | Kata kerja "klik", "tampilkan kolom", "pakai {{vendor}}" di `BR-xxx` | Pindahkan ke artefak downstream; simpan hanya outcome+metrik | [IIBA infograph: no solution elements](https://www.iiba.org/contentassets/38e412c7b77d456297d953de5bf5ca61/requirement-types-infograph.pdf); [ISO 29148 BRS terpisah](https://www.din.de/de/mitwirken/normenausschuesse/nia/veroeffentlichungen/wdc-beuth:din21:299567544/toc-3025650/download) |
| BRD menggantikan business case atau charter | Tidak ada kejelasan kelayakan investasi/otorisasi; sponsor menandatangani dokumen yang salah | Tidak ada `BC-ID`/`CHARTER-ID`; target finansial hanya ada di BRD | Rujuk business case & charter; BRD fokus need/scope/outcome | [PMI business case](https://www.pmi.org/learning/library/concise-project-charter-team-focus-2157); [PMI charter](https://www.pmi.org/blog/project-charter); [ISO 21502 4.3.2](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download) |
| Requirement kabur: "cepat, mudah, user-friendly, optimal, dll." | Tidak dapat diverifikasi; acceptance menjadi negosiasi di akhir | Tidak ada unit/ambang/sumber data/`AC-ID` | Tulis baseline→target+periode+sumber kebenaran | [IEEE 29148 construct of a good requirement](https://ieeexplore.ieee.org/document/8559686); [IIBA outcome measurable](http://go.iiba.org/The-Standard-Corporate) |
| Satu paragraf berisi banyak kebutuhan ("dan", "serta", "termasuk") | Tidak atomic; sulit diprioritaskan, ditelusuri, dan dinilai dampak perubahannya | Satu `BR` memiliki >1 KPI atau >1 owner | Pecah menjadi beberapa `BR-xxx`, satu outcome per ID | [IEEE 29148 attributes/characteristics](https://ieeexplore.ieee.org/document/8559686); [IIBA Prioritize Requirements](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/) |
| KPI/OKR tanpa baseline, definisi, atau owner | "Sukses" tidak dapat dibuktikan; manfaat tidak bisa direalisasi | Target angka tanpa periode, denominator, sumber data | Lengkapi definisi operasional, baseline, horizon, owner | [IIBA Standard outcome-driven](http://go.iiba.org/The-Standard-Corporate); [PMI PMBOK 7 outcomes](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmbok-guide-public-faqs-1-july-2021.pdf) |
| Scope hanya daftar "in", tidak ada "out" dan kewenangan keputusan | Scope creep; eksklusi baru diperdebatkan saat delivery | `SC-OUT` kosong; tidak ada pemilik keputusan perubahan scope | Isi in/out + batas kewenangan + owner eksklusi | [ISO 29148 business scope](https://www.din.de/de/mitwirken/normenausschuesse/nia/veroeffentlichungen/wdc-beuth:din21:299567544/toc-3025650/download); [ISO 21502 change control](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download) |
| Asumsi tak bertuan dan constraint tanpa sumber | Keputusan bisnis rapuh; pelanggaran regulasi baru ketahuan belakangan | `A-xxx` tanpa owner validasi; `C-xxx` tanpa dokumen/URL | Tambahkan owner, tanggal validasi, sumber normatif | [Atlassian limitations/assumptions](https://www.atlassian.com/software/confluence/resources/guides/how-to/business-requirements); [ISO 21502](https://www.iso.org/standard/74947.html) |
| Risiko dan dependensi dicatat sekadar daftar, tanpa kaitan ke KPI/AC | Mitigasi tidak memprioritaskan nilai bisnis | `R-xxx` tidak merujuk `GOAL/KPI`; `DEP-xxx` tanpa tanggal dampak | Hubungkan setiap risiko/dependensi ke KPI/AC dan owner | [IIBA BACCM value/context](https://www.iiba.org/globalassets/business-analysis-resources/the-business-analysis-standard/files/the-business-analysis-standard.pdf); [ISO 21502 planning & control](https://www.iso.org/standard/74947.html) |
| RTM dibuat setelah delivery, atau hanya satu arah | requirement hilang/orphan; dampak perubahan tidak terlihat | Kolom FSD/desain/test case kosong tanpa alasan; turunan tanpa `BR-ID` | RTM sejak approval; dua arah; orphan diberi status | [IIBA Trace Requirements](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/); [Microsoft Learn association to test cases](https://learn.microsoft.com/en-us/training/modules/analysis-solution-intelligent-order-management/tracking-requirements) |
| "Approved" tanpa menyebut versi, atau baseline ditimpa diam-diam | Auditor/stakeholder tidak tahu keputusan mana yang berlaku | Change log kosong; `v1.0` berubah isi tanpa `CR` | Sign-off mengikat `vX.Y`; simpan baseline; perubahan lewat CR | [IIBA Maintain/Assess/Approve](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/); [ISO 21502 7.10](https://www.din.de/en/getting-involved/standards-committees/nqsz/publications/wdc-beuth:din21:334145134/toc-3233385/download) |
| Semua pihak "A" di RACI, atau approver hanya tim teknis | Tidak ada akuntabilitas nilai; keputusan bisnis didelegasikan tanpa kewenangan | Beberapa `A` per keputusan; tidak ada sponsor/finance | Tepat satu `A`; sponsor/business owner akuntabel; BA custodian | [PMI sponsor mengotorisasi](https://www.pmi.org/blog/project-charter); [ISO 15288 stakeholder involvement](https://committee.iso.org/standard/81702.html?browse=ics) |
| Mengklaim "ISO 29148 mewajibkan 15 section BRD" / "SMART wajib ISO" | *Overclaim* standar; audit kepatuhan menjadi salah sasaran | Sitasi hanya blog; `[S]` dipakai untuk opini | Pisahkan `[S]`, `[P]`, `[I]`; gunakan katalog/ToC resmi | [ISO 29148 scope](https://committee.iso.org/fr/standard/72089.html?browse=ics); [IEEE 29148](https://ieeexplore.ieee.org/document/8559686); [ISO 15288 tidak menetapkan format information item](https://committee.iso.org/standard/81702.html?browse=ics) |
| BRD sekali jadi lalu diarsipkan | Bertentangan dengan lifecycle iteratif; perubahan bisnis tidak tercermin | Status terakhir `Approved` tanpa review berkala/CR | Terapkan Maintain–Prioritize–Assess–Approve sepanjang inisiatif | [ISO 29148 iterative/recursive](https://ieeexplore.ieee.org/document/8559686); [IIBA RLM](https://production.iiba.org/knowledgehub/guide-to-business-data-analytics/) |

### Gaps

- Daftar anti-pattern bersifat **[I] sintesis peneliti**; tidak ada standar tunggal yang mempublikasikan "12 anti-pattern BRD" dengan frekuensi/statistik kerugian proyek. Klaim angka kerugian sengaja **tidak** dibuat.
- Beberapa halaman vendor (Atlassian) menyertakan klaim statistik manfaat template; angka tersebut tidak dipakai sebagai dasar normatif karena tidak diverifikasi ke sumber primer dan bukan fokus catatan ini — [Atlassian](https://www.atlassian.com/software/confluence/resources/guides/how-to/business-requirements).
