> Sumber: GitHub Docs, "About the repository README file" — https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
> Catatan: Dipakai saat membuat docs/README.md sebagai indeks navigasi artefak, tata kelola, dan kontrak API per versi.
# {{NAMA_PROYEK}} — Documentation Hub

- Status: {{STATUS_DOKUMENTASI}}
- Versi dokumen: {{VERSI_DOKUMEN_SEMVER}}
- Pemilik: {{TIM_PEMILIK}}
- Terakhir diperbarui: {{YYYY-MM-DD}}
- Repository: {{URL_REPOSITORI}}
- Kebijakan: [CHANGELOG](../CHANGELOG.md) · [CONTRIBUTING](../CONTRIBUTING.md) · [LICENSE](../LICENSE)

## 1. Mulai cepat
- Tujuan proyek: {{SATU_PARAGRAF_TUJUAN}}
- Prasyarat: {{PRASYARAT}}
- Perintah lokal: `{{PERINTAH_QUICKSTART}}`
- Bantuan / eskalasi: {{KONTAK_DAN_KANAL}}

## 2. Peta artefak per fase
| Fase | Lokasi kanonik | Artefak | Status | Pemilik | Catatan |
|---|---|---|---|---|---|
| BRD | `docs/requirements/{{PATH_BRD}}` | {{ID_BRD}} | {{STATUS}} | {{OWNER}} | Isi di luar scope catatan struktur ini |
| FSD | `docs/requirements/{{PATH_FSD}}` | {{ID_FSD}} | {{STATUS}} | {{OWNER}} | Isi di luar scope catatan struktur ini |
| Desain | `docs/design/{{PATH_DESAIN}}` | {{ID_DESAIN}} | {{STATUS}} | {{OWNER}} | Isi di luar scope catatan struktur ini |
| Testing | `docs/test/{{PATH_TESTING}}` | {{ID_TESTING}} | {{STATUS}} | {{OWNER}} | Isi di luar scope catatan struktur ini |
| Laporan harian | `docs/reports/{{YYYY}}/{{MM}}/{{PATH_LAPORAN}}` | {{ID_LAPORAN}} | {{STATUS}} | {{OWNER}} | Isi di luar scope catatan struktur ini |

> Aturan: README ini **hanya indeks**. Jangan menyalin isi artefak ke sini.

## 3. Keputusan dan tata kelola
| Artefak | Path | Status | Pemilik |
|---|---|---|---|
| ADR index | `docs/adr/README.md` | {{STATUS}} | {{OWNER}} |
| Definition of Done | `docs/governance/definition-of-done.md` | {{STATUS}} | {{OWNER}} |
| RTM | `docs/governance/rtm.md` | {{STATUS}} | {{OWNER}} |
| RACI | `docs/governance/raci.md` | {{STATUS}} | {{OWNER}} |
| Release checklist | `docs/governance/release-checklist.md` | {{STATUS}} | {{OWNER}} |

## 4. Kontrak API dan siklus hidup
| Versi | OpenAPI | Status | Deprecation | Sunset | SDK | Migration guide |
|---|---|---|---|---|---|---|
| V1 | `docs/api/v1/openapi.yaml` | {{STATUS_V1}} | {{TANGGAL_DEPRECATION_V1}} | {{TANGGAL_SUNSET_V1}} | {{VERSI_SDK_V1}} | {{PATH_MIGRASI_V1}} |
| V2 | `docs/api/v2/openapi.yaml` | {{STATUS_V2}} | {{TANGGAL_DEPRECATION_V2}} | {{TANGGAL_SUNSET_V2}} | {{VERSI_SDK_V2}} | `docs/api/migration/v1-to-v2.md` |
| V3 | `docs/api/v3/openapi.yaml` | {{STATUS_V3}} | {{TANGGAL_DEPRECATION_V3}} | {{TANGGAL_SUNSET_V3}} | {{VERSI_SDK_V3}} | `docs/api/migration/v2-to-v3.md` |

- Kebijakan dukungan: `docs/api/lifecycle/support-policy.md`
- Dokumentasi deprecation: `docs/api/lifecycle/deprecation.md`
- Dokumentasi sunset: `docs/api/lifecycle/sunset.md`

## 5. Versioning dokumen
- Skema: Semantic Versioning 2.0.0 — {{URL_SEMVER}}
- CHANGELOG: [Keep a Changelog 1.1.0](../CHANGELOG.md)
- Commit: Conventional Commits 1.0.0 — {{URL_CONVENTIONAL_COMMITS}}
- Tag rilis: `v{{MAJOR}}.{{MINOR}}.{{PATCH}}`; tag API: `api-v{{MAJOR}}`
- `openapi`: {{VERSI_OAS}}; `info.version`: {{VERSI_DOKUMEN_OAD}}
- Satu source-of-truth per fakta; duplikasi hanya berupa tautan.

## 6. Review dokumentasi
- [ ] Tautan relatif valid setelah clone
- [ ] Tidak ada isi artefak yang diduplikasi ke README
- [ ] ADR lama tidak ditimpa; status `superseded by` benar
- [ ] `CHANGELOG.md` memiliki `Unreleased`, tanggal ISO, deprecation/removal/breaking
- [ ] OpenAPI per versi tervalidasi dan contoh cocok dengan skema
- [ ] Secret tidak masuk `config/` atau contoh
- [ ] CODEOWNERS mencakup kontrak API, lifecycle policy, dan CI

## 7. Sumber normatif
- [STANDAR] ISO/IEC/IEEE 29148:2018 — https://www.iso.org/standard/72089.html
- [STANDAR] OpenAPI Specification 3.2.0 — https://spec.openapis.org/oas/v3.2.0.html
- [INDUSTRI] Write the Docs, Docs as code — https://www.writethedocs.org/guide/docs-as-code/
- [VENDOR/RESMI] GitHub, About READMEs — https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
- [INDUSTRI] Keep a Changelog 1.1.0 — https://keepachangelog.com/en/1.1.0/
- [INDUSTRI] MADR 4.0.0 — https://adr.github.io/madr/
