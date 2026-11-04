> Sumber: W3C, "Web Content Accessibility Guidelines (WCAG) 2.2" — https://www.w3.org/TR/WCAG22/
> Catatan: Dipakai saat menutup desain fitur atau komponen untuk memverifikasi kepatuhan WCAG 2.2 Level AA pada seluruh alur dan variasi tampilan.
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
