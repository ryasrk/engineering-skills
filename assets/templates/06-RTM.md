> Sumber: ISO/IEC/IEEE 29148:2018 — https://www.iso.org/standard/72089.html
> Catatan: Dipakai saat melacak keterhubungan requirement ke ADR, modul, kontrak API, dan bukti verifikasi.
# Requirements Traceability Matrix — {{NAMA_PROYEK}}

- Versi: {{VERSI_RTM}}
- Pemilik: {{TIM_PEMILIK}}
- Terakhir disinkronkan: {{YYYY-MM-DD}}
- Catatan: tabel ini melacak **lokasi dan status**, bukan menyalin isi requirements/desain/test (topik peneliti 1–5).

| ID Requirement | Sumber kanonik | Keputusan/ADR | Modul / adapter | Kontrak API | Verifikasi | Status | Pemilik |
|---|---|---|---|---|---|---|---|
| {{REQ_001}} | `docs/requirements/{{PATH}}#{{ANCHOR}}` | `docs/adr/{{NNNN}}-{{JUDUL}}.md` | `{{PATH_MODUL}}` | `{{VERSI_API}} {{PATH_OAD}}#{{OPERATION_ID}}` | `{{PATH_TEST}}` / Pact `{{NAMA_PACT}}` | {{draft|implemented|verified|deprecated}} | {{OWNER}} |
| {{REQ_002}} | `docs/requirements/{{PATH}}#{{ANCHOR}}` | {{ADR_ATAU_TIDAK_ADA}} | `{{PATH_MODUL}}` | `{{VERSI_API}} {{PATH_OAD}}#{{OPERATION_ID}}` | `{{PATH_TEST}}` | {{STATUS}} | {{OWNER}} |

## Coverage
- Requirements tanpa pemilik: {{JUMLAH_ATAU_NOL}}
- Requirements tanpa verifikasi: {{JUMLAH_ATAU_NOL}}
- Requirements yang terdampak deprecation `{{VERSI_API}}`: {{DAFTAR_ID}}
- Perubahan RTM harus menautkan: {{TAUTAN_PR}} · {{TAUTAN_CHANGELOG}}
