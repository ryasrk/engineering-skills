> Sumber: Martin Fowler, "Parallel Change" — https://martinfowler.com/bliki/ParallelChange.html
> Catatan: Dipakai saat merencanakan urutan expand–contract migrasi database dan kontrak V1/V2/V3.
# Runbook Expand–Contract — Urutan Deploy Aman

| # | Fase | Aksi database | Aksi kontrak/API | Aplikasi/deploy | Exit gate |
|---|---|---|---|---|---|
| 0 | Design | Tulis ADR + migration plan + rollback plan | OAD V3 draft, compatibility diff, Pact expectations | Feature flag `{{FLAG_V3}}` off | ADR approved; contract tests merah untuk V3 |
| 1 | **Expand** | Tambah kolom/tabel/index baru yang **nullable** atau kompatibel; jangan drop/rename | Terbitkan `/api/v3` di belakang flag, sementara V1/V2 tetap responsif | Deploy adapter V3 + domain kanonik; rolling update | Old app images masih bisa menulis; health/latency hijau |
| 2 | **Backfill** | Isi data lama ke struktur baru secara idempotent dan terukur | Tidak mengubah response V1/V2 | Jalankan `scripts/backfill-{{PERUBAHAN}}.sh` | Parity check: `{{JUMLAH_BARIS_LAMA}}` vs `{{JUMLAH_BARIS_BARU}}`; drift `{{AMBANG_DRIFT}}` |
| 3 | **Dual-write** | Tulis ke lama **dan** baru dalam satu transaksi/logik yang dapat dikompensasi | Semua versi membaca dari adapter yang sesuai | Rilis kode dual-write lebih dulu daripada konsumen baru | Reconciliation job hijau; tidak ada orphan write |
| 4 | **Dual-read / shadow** | Baca baru, bandingkan dengan lama; sumber kebenaran mulai beralih | V3 dapat diaktifkan untuk internal/canary; V1/V2 tetap kontrak lama | Canary 1%→5%→25%→50%→100%; log/metrik terpisah | Selisih respons di bawah `{{AMBANG_PARITY}}`; error budget terpenuhi |
| 5 | **Switch** | Sumber baca utama = struktur baru, tulis lama masih dijaga untuk rollback | Default docs/SDK → V3; deprecation V2 diumumkan | Promote canary; blue-green cutover bila perlu | `can-i-deploy` hijau; SLO V3 hijau selama `{{JENDELA_OBSERVASI}}` |
| 6 | **Contract** | Setelah sunset dan metrik nol, hapus kolom/tabel/trigger lama pada rilis terpisah | Matikan route V1/V2 → `410 Gone` atau sesuai kebijakan; arsipkan OAD | Hapus adapter/flag lama | Tidak ada traffic versi lama selama `{{JENDELA_NOL_TRAFFIC}}`; backup/rollback tersedia |
