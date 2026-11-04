---

## Penutup: Definition of Done lintas fase dan anti-pattern lintas topik

### Definition of Done ringkas

| Fase | Selesai hanya jika |
| --- | --- |
| BRD | Kebutuhan bisnis atomic dan terukur; ruang lingkup in/out jelas; KPI, asumsi, constraint, risiko tercatat; RACI dan sign-off lengkap; status `Baselined`; setiap `BR-...` punya baris RTM. |
| FSD | Setiap `FR-...` punya AC `Given/When/Then` (happy/edge/gagal); aturan bisnis bernomor + decision table + baris default; kontrak OpenAPI dengan `security` eksplisit; RTM dua arah ke BRD dan test case; tidak ada solusi teknis terselubung. |
| Desain | Goals/non-goals, alternatif yang ditolak, konsekuensi, rencana migrasi, observability, STRIDE, rollout/rollback tercatat; ADR bernomor dan bertaut; diagram punya pemilik dan versi; DoD aksesibilitas A+AA terpenuhi. |
| Testing | Entry/exit criteria terpenuhi; quality gate fail-closed hijau (unit, integration, contract, E2E, performa, keamanan, aksesibilitas); flaky test dikarantina; residual risk dan defect escape rate dilaporkan; test completion report ditandatangani. |
| Release | CHANGELOG + SemVer + tag; OAD dan SDK per `api_version`; header `Deprecation` (RFC 9745) dan `Sunset` (RFC 8594) bertanggal dan urut benar; canary/blue-green sehat; metrik per versi stabil; runbook rollback tersedia. |
| Operasi harian | Laporan memuat bukti PR/issue, deliverable sesuai DoD, blocker ber-owner + target, perubahan scope/jadwal, keputusan yang diminta, dan rencana hari berikutnya; kanal disesuaikan audiens; data pribadi tidak bocor. |

### Anti-pattern lintas topik

1. **Dokumen tanpa pemilik atau tanpa status** — tidak ada yang tahu mana versi berlaku.
2. **Duplikasi requirement di BRD, FSD, dan test case** — kontradiksi tak terdeteksi; gunakan ID + referensi, bukan salinan teks.
3. **RTM satu arah atau tidak ada** — perubahan BRD tidak pernah sampai ke test case dan `api_version`.
4. **Kriteria penerimaan berupa prosa subyektif** ("cepat", "user friendly", "progres 85%") tanpa ambang terukur.
5. **Keputusan arsitektur hanya di chat/rapat** — hilang saat orang pindah tim; wajib ADR append-only.
6. **Diagram tanpa tanggal, versi, atau pemilik** — menjadi fiksi setelah rilis pertama.
7. **Quality gate yang bisa di-bypass** atau metrik vanity (pass rate tanpa denominator, 100% line coverage).
8. **Laporan harian sebagai surveilans** — rapat duplikatif, blocker tanpa owner, copy-paste tanpa keputusan.
9. **Breaking change langsung di versi berjalan** — hapus/rename field, required field baru, ubah tipe/default/enum respons, ubah format error atau pagination tanpa major baru.
10. **`/api/v2` yang hanya alias ke `/api/v1`** — klien mengira sudah migrasi padahal kontrak identik.
11. **Versi tanpa kebijakan sunset** atau sunset diumumkan tanpa metrik pemakaian per `api_version`.
12. **Mencampur empat jenis versi** (`openapi`, `info.version`, `/api/vN`, versi SDK) seolah-olah satu angka.
13. **Mengklaim konformasi standar yang tidak diverifikasi** — misalnya menyebut reduced-motion sebagai syarat WCAG 2.2 AA, atau membalik RFC 8594/9745.

### Keterbatasan riset yang dinyatakan jujur

- Teks penuh sebagian standar ISO/IEC/IEEE dan PMI berbayar/terbatas; verifikasi dilakukan pada katalog resmi, abstract, daftar isi, dan pratinjau resmi. Konsekuensinya: laporan tidak mengklaim daftar section BRD/FSD yang "diwajibkan" standar.
- Beberapa rujukan sekunder tidak dapat diverifikasi langsung (mis. 404 pada Google re:Work, halaman flow metrics DORA, sebagian dokumen PayPal/ASP.NET, dan catatan tanggal rilis OAS 3.2.1). Detail ada di Bab 8.
- Rasio unit/integration/E2E, SLA eskalasi internal, lama notice period deprecation, serta kebijakan N-1 vs N-2 adalah **keputusan organisasi**, bukan angka yang distandardisasi.
- Template di `templates/` adalah hasil sintesis dari standar dan praktik industri pada catatan riset; placeholder `{{...}}` wajib diganti dan disesuaikan konteks proyek sebelum dipakai.

### Cara memakai paket ini

1. Salin `templates/06-Struktur-Folder.md` dan `templates/06-Struktur-Folder-Monorepo.md` ke repositori; jadikan `templates/06-Documentation-Hub.md` sebagai `README.md` navigasi.
2. Isi `01-BRD.md` → `02-FSD.md` → `03-Design-Doc.md` + `03-ADR.md`; jaga ID tetap stabil.
3. Turunkan `04-Test-Plan.md` dari AC dan kontrak; pasang `04-Quality-Gate-*.md` di CI.
4. Untuk perubahan API: mulai dari `06-Runbook-Expand-Contract.md`, siapkan OAD per versi, lalu jalankan `06-Checklist-Zero-Downtime.md` sebelum cutover.
5. Pakai `05-Laporan-Harian.md` untuk pelaporan berbasis bukti; eskalasi blocker mengikuti `06-RACI.md`.
6. Tinjau kembali koreksi standar di Bab 8 setiap kali ada audit atau pembaruan dependensi dokumen.

---

**Berkas terkait**

- Laporan ini: `reports/Riset Best Practices Engineering.md`
- Catatan riset: `research_notes/Riset Best Practices Engineering/01-brd.md` … `06-skema-dan-versioning-api.md`
- Template: `templates/` — lihat `templates/README.md`
