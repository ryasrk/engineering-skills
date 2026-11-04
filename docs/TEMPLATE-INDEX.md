# Indeks Template — Riset Best Practices Engineering

> 40 template siap pakai untuk BRD, FSD, Desain, Testing, Laporan Harian, Skema Folder/Project, dan API versioning zero downtime V1/V2/V3.
>
> Semua berkas `*.md` di folder ini (kecuali `README.md`) berisi template lengkap dengan placeholder `{{...}}`, diawali dua baris metadata `> Sumber:` dan `> Catatan:`. Ganti seluruh placeholder, sesuaikan konteks proyek, lalu simpan hasil isian di path kanonik mengikuti `06-Struktur-Folder.md`.
>
> Laporan lengkap: `../reports/Riset Best Practices Engineering.md` · Catatan riset: `../research_notes/Riset Best Practices Engineering/`.

## Urutan pemakaian

```
Bisnis → Fungsi → Desain → Uji → Rilis/Operasi
01-BRD → 02-FSD → 03-Design-Doc + 03-ADR → 04-Test-Plan → 06-*Release* + 05-Laporan-Harian
                          ↘ 06-OpenAPI-Multi-Versi* → 06-Runbook-Expand-Contract → 06-Checklist-Zero-Downtime
```

| Fase | Dipakai saat | Template inti | Bergantung pada |
| --- | --- | --- | --- |
| 1. BRD | Inisiatif disetujui, sebelum solusi dirancang | `01-BRD.md` | Business case / charter |
| 2. FSD | Kebutuhan bisnis sudah baselined | `02-FSD.md` | `01-BRD.md`, `01-RTM.md` |
| 3. Desain | Ada keputusan arsitektur atau komponen UI baru | `03-Design-Doc.md`, `03-ADR.md`, `03-UI-UX-Spec.md` | `02-FSD.md` |
| 4. Testing | AC dan kontrak tersedia | `04-Test-Plan.md` | `02-FSD.md`, `02-RTM.md`, OAD |
| 5. Laporan Harian | Setiap hari kerja / setiap siklus asinkron | `05-Laporan-Harian.md` | PR, issue, CI, metrik per versi |
| 6. Skema | Awal repositori atau restrukturisasi | `06-Struktur-Folder.md`, `06-Struktur-Folder-Monorepo.md` | Keputusan monorepo/polyrepo |
| 7. API | Ada breaking change atau major version baru | `06-OpenAPI-Multi-Versi*.md`, `06-Runbook-Expand-Contract.md` | `06-Matriks-Endpoint-Versi.md`, `06-ADR.md` |

---

## 1. BRD — Business Requirements Document

| Berkas | Kapan dipakai | Isi kunci |
| --- | --- | --- |
| `01-BRD.md` | Menyusun kebutuhan & outcome bisnis | Latar belakang, current/future state, scope, RACI, BR, KPI, risiko, approval, riwayat |
| `01-RTM.md` | Menghubungkan `BR-...` ke FSD, desain, dan test case | Matriks keterlacakan + baris kontrol orphan |
| `01-Checklist-Review-BRD.md` | Sebelum baselined/sign-off | Kelengkapan, kualitas requirement, tata kelola |
| `01-Pola-Kalimat-Kebutuhan-Bisnis.md` | Menulis requirement atomic & terukur | Pola kalimat + contoh perbaikan |

## 2. FSD — Functional Specification / Functional Design

| Berkas | Kapan dipakai | Isi kunci |
| --- | --- | --- |
| `02-FSD.md` | Menerjemahkan BRD jadi perilaku teruji | Use case, Gherkin AC, decision table, authorization matrix, OpenAPI, NFR, RTM, Lampiran sumber |
| `02-RTM.md` | Audit keterlacakan dua arah | BRD → FSD → AC → `TC-...`, termasuk kontrol orphan |
| `02-Checklist-Review.md` | Review FSD sebelum design | 25 butir pemeriksaan |

## 3. Desain

| Berkas | Kapan dipakai | Isi kunci |
| --- | --- | --- |
| `03-Design-Doc.md` | RFC/design review | Konteks, goals/non-goals, alternatif ditolak, C4/HLD/LLD, STRIDE, observability, migrasi, rollout/rollback, DoD |
| `03-ADR.md` | Setiap keputusan arsitektur signifikan | Format MADR 4.0.0 + status ledger `Proposed/Accepted/Superseded` |
| `03-UI-UX-Spec.md` | Handoff desainer → engineer | Design tokens, anatomy/variant, matriks state, aksesibilitas & motion, copy |
| `03-DoD-Aksesibilitas.md` | Definisi selesai komponen/fitur | Kriteria A+AA, kebijakan produk di luar AA, metode verifikasi, pernyataan konformasi |

## 4. Testing / QA

| Berkas | Kapan dipakai | Isi kunci |
| --- | --- | --- |
| `04-Test-Plan.md` | Awal siklus rilis | ISO/IEC/IEEE 29119-3:2021 tailored: Test Plan + Strategy + Test Case + Incident + Status + Completion Report |
| `04-Exit-Criteria-Matrix.md` | Menetapkan gerbang keluar | Matriks completion/exit criteria per level & jenis uji |
| `04-Quality-Gate-GitHub-Actions.md` | CI di GitHub | Required checks, job test/contract/performa/keamanan |
| `04-Quality-Gate-GitLab-CI.md` | CI di GitLab | Pipeline + threshold k6 + `can-i-deploy` |
| `04-Quality-Gate-GitLab-Approval-Policy.md` | Kebijakan approval GitLab | Merge request approval policy keamanan |

## 5. Laporan Harian

| Berkas | Kapan dipakai | Isi kunci |
| --- | --- | --- |
| `05-Laporan-Harian.md` | Standup asinkron / status ke manajemen & klien | TL;DR, deliverable, WIP, blocker ber-owner, perubahan scope, metrik event-derived, keputusan, rencana, jejak audit |

## 6. Skema folder, project, dan tata kelola

| Berkas | Kapan dipakai | Isi kunci |
| --- | --- | --- |
| `06-Struktur-Folder.md` | Menata dokumentasi proyek | Pohon `docs/`, `requirements/`, `design/`, `adr/`, `test/`, `reports/`, `templates/` |
| `06-Struktur-Folder-Monorepo.md` | Menata kode aplikasi | Pohon monorepo: apps/services/packages/infra/tests/scripts |
| `06-Documentation-Hub.md` | Membuat README navigasi | Peta artefak per fase, keputusan, kontrak API, versioning dokumen |
| `06-CODEOWNERS.md` | Menetapkan kepemilikan kode | Aturan review per direktori / per `api_version` |
| `06-CHANGELOG.md` | Setiap rilis | Keep a Changelog 1.1.0 + SemVer, kategori Added/…/Security |
| `06-ADR.md` | Keputusan lintas repositori | ADR ringkas MADR untuk tata kelola & versioning |
| `06-Definition-of-Done.md` | Definisi selesai lintas fase | Checklist DoD rilis, termasuk kontrak dan deprecation |
| `06-RTM.md` | Keterlacakan until rilis | RTM dengan kolom `api_version` |
| `06-RACI.md` | Menetapkan peran & eskalasi | Responsible/Accountable/Consulted/Informed |
| `06-Checklist-Release.md` | Pra-rilis, cutover, pasca-rilis | Checklist release + kriteria rollback otomatis |

## 7. API versioning zero downtime V1/V2/V3

### Kontrak dan dokumentasi

| Berkas | Kapan dipakai | Isi kunci |
| --- | --- | --- |
| `06-OpenAPI-Multi-Versi.md` | Indeks kontrak | Daftar OAD per major dan aturan `openapi` vs `info.version` |
| `06-OpenAPI-Multi-Versi-V1.md` | Memelihara `/api/v1` | OAD V1, status deprecation |
| `06-OpenAPI-Multi-Versi-V2.md` | Meluncurkan `/api/v2` | OAD V2, perubahan additive/breaking |
| `06-OpenAPI-Multi-Versi-V3.md` | Meluncurkan `/api/v3` | OAD V3, migrasi lanjutan |
| `06-Matriks-Endpoint-Versi.md` | Perencanaan kompatibilitas | Matriks endpoint V1/V2/V3 + status dukungan |
| `06-Routing-Gateway-Nginx.md` | Konfigurasi gateway | Rute `/api/v1|v2|v3`, header lifecycle, canary |

### Migrasi dan siklus hidup

| Berkas | Kapan dipakai | Isi kunci |
| --- | --- | --- |
| `06-Runbook-Expand-Contract.md` | Setiap breaking change | Expand → backfill → dual-write/read → canary/switch → Contract + rollback |
| `06-Timeline-Migrasi-V1-V2-V3.md` | Perencanaan program migrasi | Timeline bertahap, notice period, coexist N-1/N-2 |
| `06-Header-Lifecycle-Deprecation-Sunset.md` | Menandai versi lama | `Deprecation` (RFC 9745) dan `Sunset` (RFC 8594), urutan tanggal benar |
| `06-Komunikasi-Konsumen-Deprecation.md` | Notifikasi konsumen | Surat/notice, kanal, bukti penerimaan |
| `06-Kriteria-Sunset-Metrik.md` | Mematikan versi lama | Ambang pemakaian per `api_version`, periode observasi, approval |
| `06-Observability-Alert-Per-Versi.md` | Operasi multi-versi | Metrik, log, trace, dan alert dipartisi per versi |
| `06-Checklist-Zero-Downtime.md` | Sebelum & sesudah cutover | Checklist cutover, kriteria rollback, anti-pattern |

---

## Catatan pemakaian

- **Jangan duplikasi requirement.** Simpan teks kanonik di satu artefak; artefak lain merujuk ID (`BR-...`, `FR-...`, `AC-...`, `TC-...`, `ADR-...`, `api_version`).
- **Empat versi adalah empat hal berbeda:** `openapi` (versi spesifikasi dokumen), `info.version` (versi dokumen OAD), `/api/vN` (major kontrak API), dan versi SDK.
- **Koreksi standar:** RFC 8594 = `Sunset`; RFC 9745 = `Deprecation`. Jangan tertukar.
- **Keputusan organisasi** (SLA eskalasi, lama notice period, N-1 vs N-2, rasio test pyramid) wajib diisi eksplisit; tidak ada angka baku dari standar.
- **Sumber** tiap template tercantum di baris `> Sumber:`; rujukan lengkap ada di laporan utama dan di `../research_notes/Riset Best Practices Engineering/`.
