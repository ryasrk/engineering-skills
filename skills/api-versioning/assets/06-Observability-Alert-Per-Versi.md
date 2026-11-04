> Sumber: AWS API Gateway, "Set up a canary release deployment" — https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md
> Catatan: Dipakai saat menyiapkan metrik dan alert yang dikunci per api_version dan canary.
# Observability dan Alert per Versi

| Sinyal | Label minimum | Alert contoh |
|---|---|---|
| `http_requests_total` | `api_version`, `route`, `method`, `status`, `consumer_id` | Lonjakan 4xx/5xx V3 vs baseline V2 > `{{AMBANG_ERROR}}` |
| `http_request_duration_seconds` | `api_version`, `canary`, `region` | p95/p99 V3 > `{{AMBANG_LATENCY}}` selama `{{JENDELA}}` |
| `api_deprecated_requests_total` | `api_version`, `consumer_id` | Masih ada konsumen prioritas tinggi V1 pada T−30 sunset |
| `api_version_request_ratio` | `api_version` | Share V1 tidak turun sesuai timeline |
| `dual_write_mismatch_total` | `entity`, `migration_id` | Drift > `{{AMBANG_DRIFT}}` |
| `contract_verification_result` | `consumer`, `provider`, `version` | `can-i-deploy` gagal |
| Business KPI | `api_version`, `canary` | Regresi signifikan → auto-reroute ke stable |
