> Sumber: ISO/IEC/IEEE 29148:2018 — https://ieeexplore.ieee.org/document/8559686; IIBA BABOK Guide v3 — https://production.iiba.org/professional-development/knowledge-centre/ba-connection/babok-guide-v3-celebrates-1-year-anniversary/; Atlassian, Business requirements document template — https://www.atlassian.com/software/confluence/resources/guides/how-to/business-requirements
> Catatan: Dipakai saat menyusun BRD baru untuk suatu inisiatif perubahan sebelum kebutuhan bisnis diserahkan ke artefak downstream.

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
