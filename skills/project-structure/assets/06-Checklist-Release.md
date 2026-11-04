> Sumber: Pact Docs, "Can I Deploy" — https://docs.pact.io/pact_broker/can_i_deploy
> Catatan: Dipakai release manager pada tahap pra-rilis, cutover, dan pasca-rilis produksi.
# Release Checklist — v{{MAJOR}}.{{MINOR}}.{{PATCH}}

- Tanggal rilis: {{YYYY-MM-DD}}
- Release manager: {{NAMA}}
- Environment: {{development|staging|production}}
- API versions terdampak: {{V1|V2|V3}}
- ADR: {{TAUTAN_ADR}} · Runbook: {{TAUTAN_RUNBOOK}}

## Pra-rilis
- [ ] `CHANGELOG.md` dipindah dari `Unreleased` ke versi + tanggal ISO
- [ ] Conventional Commits dan SemVer bump sudah sesuai; breaking change berada pada MAJOR
- [ ] Branch protection: review CODEOWNERS + required checks + signed commits hijau
- [ ] OAD V1/V2/V3 tervalidasi; contoh, schema, dan error `problem+json` cocok
- [ ] Compatibility gate tidak menemukan breaking change pada minor/patch
- [ ] Pact `can-i-deploy --pacticipant {{APP}} --version {{VERSION}} --to-environment {{ENV}}` sukses
- [ ] SDK per major di-generate ulang; SDK deprecated memuat warning
- [ ] Migration guide, deprecation policy, sunset policy, dan navigation hub diperbarui
- [ ] Expand/backfill/dual-write parity: drift `<= {{AMBANG_DRIFT}}`
- [ ] Feature flag `{{FLAG}}`, kill-switch, dan rollback image `{{IMAGE_SEBELUMNYA}}` siap
- [ ] Dashboard + alert per `api_version`/`canary` aktif; error budget disetujui
- [ ] Secret scan, dependency scan, dan `.gitignore` bersih

## Cutover
- [ ] Canary {{PERSENTASE_AWAL}}% → {{PERSENTASE_AKHIR}}% dengan log terpisah
- [ ] SLO 5xx/p95/business KPI hijau selama {{JENDELA_OBSERVASI}}
- [ ] `Deprecation`/`Sunset`/`Link` terpasang pada versi yang tepat; `Sunset` tidak lebih awal dari `Deprecation`
- [ ] Komunikasi konsumen terkirim: {{TAUTAN_PENGUMUMAN}}
- [ ] Routing `/api/v1`, `/api/v2`, `/api/v3` diverifikasi dari gateway
- [ ] `record-deployment` ke Pact Broker setelah deploy sukses

## Pasca-rilis
- [ ] Tag `v{{MAJOR}}.{{MINOR}}.{{PATCH}}`; artefak + checksum terbit
- [ ] Release notes dan docs-site menunjuk versi benar
- [ ] Metrik pemakaian per versi dicatat pada {{TAUTAN_DASHBOARD}}
- [ ] Insiden/rollback: {{TIDAK_ADA}} atau {{TAUTAN_INSIDEN}}
- [ ] Contract phase dijadwalkan: {{TANGGAL_CONTRACT}}

## Rollback otomatis bila
- [ ] 5xx V{{N}} > {{AMBANG_5XX}} selama {{JENDELA}}
- [ ] p95/p99 > {{AMBANG_LATENCY}} atau business KPI turun > {{AMBANG_BISNIS}}
- [ ] `dual_write_mismatch_total` > {{AMBANG_DRIFT}}
- [ ] Pact verification gagal setelah cutover
- [ ] Rollout Kubernetes `ProgressDeadlineExceeded` / readiness failure
- [ ] Konsumen prioritas tinggi masih memakai versi lama saat sunset

Tanda tangan: {{RELEASE_MANAGER}} · {{TIM_SRE}} · {{TIM_API}} · {{TANGGAL}}
