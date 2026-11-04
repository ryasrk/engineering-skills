> Sumber: Pact Docs, "Can I Deploy" — https://docs.pact.io/pact_broker/can_i_deploy
> Catatan: Dipakai saat cutover produksi untuk memastikan zero downtime dan kriteria rollback sudah terisi.
# Checklist Zero Downtime — Cutover dan Rollback

## Checklist cutover

1. Kontrak V3, SDK V3, migration guide, dan navigation hub final.
2. Compatibility gate + Pact matrix + `can-i-deploy` hijau.
3. Expand/backfill/dual-write parity dan kill-switch diuji.
4. Canary dengan log/metrik terpisah; SLO dan business KPI hijau.
5. Header lifecycle benar; komunikasi konsumen dan daftar exception lengkap.
6. Promote V3; `record-deployment`; tag rilis; dashboard per versi aktif.
7. Dual-write lama **tetap ON** sampai jendela rollback berakhir; contract dijadwalkan terpisah.

## Kriteria rollback

| Pemicu | Tindakan | Dasar |
|---|---|---|
| 5xx / p95 / business KPI melewati `{{AMBANG}}` | Reroute canary ke stable; matikan `{{FLAG_V3}}`; pertahankan dual-write | `[INDUSTRI]` [Fowler, Canary Release](https://martinfowler.com/bliki/CanaryRelease.html); `[VENDOR/RESMI]` [AWS canary](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md) |
| Rollout `ProgressDeadlineExceeded`, readiness/image failure | `kubectl rollout undo` ke revisi stabil | `[VENDOR/RESMI]` [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) |
| `dual_write_mismatch_total` melebihi ambang | Hentikan switch, jalankan reconciliation, jangan contract | `[INDUSTRI]` [Fowler, Parallel Change](https://martinfowler.com/bliki/ParallelChange.html) |
| Verifikasi kontrak gagal setelah deploy | Blokir promosi berikutnya; rollback konsumen/provider sesuai matrix | `[VENDOR/RESMI]` [Pact, Can I Deploy](https://docs.pact.io/pact_broker/can_i_deploy) |
| Konsumen prioritas tinggi masih aktif pada versi sunset | Tunda pemadaman, perpanjang notice, perbarui `Sunset` | `[STANDAR]` [RFC 8594 §8](https://www.rfc-editor.org/rfc/rfc8594.html); `[VENDOR/RESMI]` [Stripe](https://docs.stripe.com/api-versions) |
| Cache menyajikan representasi versi salah | Matikan caching lintas versi, perbaiki `Vary`/cache key | `[STANDAR]` [RFC 9111 §4.1](https://www.rfc-editor.org/rfc/rfc9111.html) |
