> Sumber: ISO/IEC/IEEE 29148:2018 (Requirements Engineering) — https://www.iso.org/standard/72086.html ; NASA SWE-047 (Bidirectional Traceability) — https://swehb.msfc.nasa.gov/pages/viewpage.action?pageId=91030146
> Catatan: Template kanonik master untuk keterlacakan dua arah (bidirectional traceability): Kebutuhan Bisnis (BRD) → Kebutuhan Fungsional (FSD) → Kriteria Penerimaan (AC) → Arsitektur (ADR) → Modul/Kode → Kontrak API → Uji (Test Case) → Bukti Rilis.
# Master Requirements Traceability Matrix (RTM) — {{NAMA_PROYEK}}

- Dokumen ID: `RTM-{{PROJECT_ID}}`
- Versi: {{VERSI_RTM}}
- Status: {{STATUS: draft | baselined | in_review | active}}
- Pemilik: {{LEAD_OWNER}}
- Terakhir Disinkronkan: {{YYYY-MM-DD}}

## 1. Matriks Keterlacakan Dua Arah (Bidirectional Matrix)

| ID Bisnis (BRD) | ID Fungsional (FSD) | Kriteria Penerimaan (AC) | Keputusan Arsitektur (ADR) | Modul / Path Kode | Kontrak API (/api/vN) | Test Case ID | Metode Verifikasi | Status | Pemilik |
|---|---|---|---|---|---|---|---|---|---|
| `{{BR_ID}}` | `{{FR_ID}}` | `{{AC_ID}}` | `{{ADR_ID}}` | `{{MODULE_PATH}}` | `{{API_ENDPOINT}}` | `{{TC_ID}}` | {{Unit | Contract | E2E | Load}} | {{STATUS: draft | implemented | verified | deprecated}} | `{{OWNER}}` |

## 2. Pemeriksaan Integritas Keterlacakan (Integrity Audit)

| Parameter Pemeriksaan | Hasil Audit | Tindakan Remediasi |
|---|---|---|
| Setiap kebutuhan bisnis (`BR-...`) memiliki minimal satu turunan teknis | {{YA_TIDAK}} | {{TINDAKAN}} |
| Setiap kebutuhan fungsional (`FR-...`) memiliki upstream `BR-...` yang valid | {{YA_TIDAK}} | {{TINDAKAN}} |
| Setiap kriteria penerimaan (`AC-...`) memiliki minimal satu test case terdaftar | {{YA_TIDAK}} | {{TINDAKAN}} |
| Tidak ada *orphan requirement* yang berstatus `Approved` tanpa pemilik | {{YA_TIDAK}} | {{TINDAKAN}} |

## 3. Cakupan Perubahan (Change Control & Release Evidence)
- Total Requirements Terverifikasi: {{JUMLAH_VERIFIED}} / {{TOTAL_REQUIREMENTS}}
- PR / Commit Terkait: {{TAUTAN_PR}}
- Entri CHANGELOG: {{VERSI_RILIS}}
