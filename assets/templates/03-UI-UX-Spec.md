> Sumber: Material Design 3, "Design tokens" — https://m3.material.io/foundations/design-tokens/overview
> Catatan: Dipakai saat handoff spesifikasi komponen UI/UX dari desainer ke engineer, lengkap dengan token, matriks state, dan semantik aksesibilitas.
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
