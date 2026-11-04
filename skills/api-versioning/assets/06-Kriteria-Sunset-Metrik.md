> Sumber: Martin Fowler, "Canary Release" — https://martinfowler.com/bliki/CanaryRelease.html
> Catatan: Dipakai saat menetapkan ambang metrik sebelum mematikan versi API lama.
# Kriteria Mematikan Versi Lama Berbasis Metrik

| Metrik | Definisi operasional | Contoh ambang cutover |
|---|---|---|
| Request share per versi | `sum(http_requests_total{api_version="V1"}) / sum(http_requests_total)` | `<= {{AMBANG_REQUEST_SHARE}}` selama `{{JENDELA_OBSERVASI}}` |
| Unique consumer/client_id | `count_distinct(client_id{api_version="V1"})` | `0` untuk `{{JENDELA_NOL_KONSUMEN}}`, atau daftar exception tertanda tangan |
| Webhook/event delivery | Jumlah endpoint yang masih pin versi lama | `0`; Stripe memungkinkan webhook endpoint mem-pin versi sendiri ([Stripe Docs](https://docs.stripe.com/api-versions)) |
| Error/SLO | 5xx, p95/p99, timeout, business-error rate per versi + canary | Tidak melebihi SLO selama `{{JENDELA_OBSERVASI}}` ([AWS canary metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md)) |
| Kontrak | `can-i-deploy` untuk V3 terhadap versi konsumen yang ada di production | Semua verifikasi sukses ([Pact](https://docs.pact.io/pact_broker/can_i_deploy)) |
| Data parity | Perbandingan dual-write/dual-read | Drift `<= {{AMBANG_DRIFT}}` |
| Dukungan | Tiket/eskalasi aktif, kontrak enterprise, regulatory retention | `0` atau pengecualian berdokumen |
