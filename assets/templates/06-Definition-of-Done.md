> Sumber: GitHub Docs, "About protected branches" — https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
> Catatan: Dipakai sebagai daftar kriteria wajib sebelum PR, deploy, atau rilis dinyatakan selesai.
# Definition of Done — {{NAMA_PROYEK}}

- Versi: {{VERSI_DOD}}
- Pemilik: {{TIM_PEMILIK}}
- Berlaku sejak: {{YYYY-MM-DD}}
- Sumber tata kelola: [GitHub protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners), [Pact can-i-deploy](https://docs.pact.io/pact_broker/can_i_deploy)

| # | Kriteria | Bukti | Wajib untuk |
|---|---|---|---|
| 1 | Commit memakai Conventional Commits; breaking change memakai `!`/footer | {{TAUTAN_COMMIT}} | Semua |
| 2 | PR disetujui CODEOWNERS; status checks, conversation resolution, linear history hijau | {{TAUTAN_PR}} | Semua |
| 3 | README/docs navigation hub diperbarui; tidak ada duplikasi source-of-truth | {{TAUTAN_DIFF_DOCS}} | Perubahan kontrak/struktur |
| 4 | `CHANGELOG.md` `Unreleased` mencatat Added/Changed/Deprecated/Removed/Fixed/Security yang relevan | {{TAUTAN_DIFF_CHANGELOG}} | Semua rilis |
| 5 | ADR ditulis untuk keputusan arsitektural; keputusan lama ditandai superseded | `docs/adr/{{NNNN}}-{{JUDUL}}.md` | Keputusan besar |
| 6 | OpenAPI per major tervalidasi; `openapi` dan `info.version` benar | {{TAUTAN_CI_OAS}} | Perubahan API |
| 7 | Diff kompatibilitas V1/V2/V3 lolos; breaking hanya pada major baru | {{TAUTAN_COMPAT_REPORT}} | Perubahan API |
| 8 | Pact verification + `can-i-deploy` hijau untuk environment target | {{TAUTAN_PACT_MATRIX}} | Deploy |
| 9 | Feature flag, rollback, backfill, dual-write parity, dan migration guide tersedia | {{TAUTAN_RUNBOOK}} | Expand–Contract |
| 10 | Metrik/alert per `api_version`, `consumer_id`, `canary` aktif | {{TAUTAN_DASHBOARD}} | Deploy |
| 11 | `Deprecation`/`Sunset`/`Link` dan halaman lifecycle sesuai RFC 9745/8594 | {{TAUTAN_HEADER_TEST}} | Deprecation/sunset |
| 12 | Tidak ada secret di repo; config.example dan `.gitignore` diperbarui | {{TAUTAN_SECRET_SCAN}} | Semua |
| 13 | Release tag `v{{MAJOR}}.{{MINOR}}.{{PATCH}}` + SDK per versi terbit | {{TAUTAN_RELEASE}} | Rilis |

Tanda tangan: {{NAMA_APPROVER}} · {{TANGGAL}} · {{TAUTAN_BUKTI}}
