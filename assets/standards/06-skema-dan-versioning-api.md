# Topik 6 — Skema Folder, Skema Project, dan API Versioning Zero-Downtime V1/V2/V3

> **Batas ruang lingkup.** Catatan ini hanya membahas **struktur, tata kelola repositori, dan versioning API**. Isi BRD, FSD, dokumen desain arsitektur/UI, test plan, dan format laporan harian sengaja tidak dibahas karena merupakan topik peneliti 1–5; yang disebut di sini hanyalah **letak file, penamaan, dan tautan navigasinya**.
>
> **Konvensi sitasi.** `[STANDAR]` = RFC/ISO/spesifikasi normatif resmi; `[VENDOR/RESMI]` = dokumentasi resmi vendor/proyek; `[INDUSTRI]` = praktik atau opini industri, **bukan standar**. Setiap rekomendasi normatif diberi penanda dan sitasi berupa nama dokumen + URL lengkap. Rekomendasi yang disusun peneliti ditandai `[REKOMENDASI PENELITI]` dan tetap merujuk ke dasar faktualnya.
>
> **Cakupan waktu.** Praktik dan versi dokumen yang relevan 2024–2026; waktu pengambilan snapshot: 4 November 2026, Asia/Jakarta. Versi yang diverifikasi: ISO/IEC/IEEE 29148:2018, SemVer 2.0.0, Keep a Changelog 1.1.0, Conventional Commits 1.0.0, RFC 8594 (2019), RFC 9110/9111 (2022), RFC 9457 (2023), RFC 9745 (Maret 2025), OpenAPI 3.1.0 serta 3.2.0/3.2.1, MADR 4.0.0 (2024), dan Stripe API release model pasca-2024-09-30.acacia.

---

## Pertanyaan kunci 1 — Skema folder, struktur project/repositori, dan artefak pendukung

### Takeaway

Struktur yang paling mudah diaudit adalah **satu canonical path per artefak**, README sebagai navigation hub, docs-as-code, ADR immutable, dan kepemilikan yang ditegakkan melalui CODEOWNERS/branch protection; monorepo atau polyrepo dipilih berdasarkan kebutuhan atomic change, isolasi akses, serta kesiapan tooling graph/cache. `[REKOMENDASI PENELITI]` — [VENDOR/RESMI] [GitHub Docs, About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes), [INDUSTRI] [Write the Docs, Docs as code](https://www.writethedocs.org/guide/docs-as-code/), [INDUSTRI] [MADR 4.0.0](https://adr.github.io/madr/), [VENDOR/RESMI] [Nx, Monorepo vs Polyrepo](https://nx.dev/docs/concepts/decisions/monorepo-vs-polyrepo).

### Cited Findings

- README, license, contribution guidelines, dan code of conduct menyampaikan ekspektasi proyek; README cukup berisi tujuan, cara memulai, bantuan, dan pemelihara, sedangkan dokumentasi panjang ditempatkan terpisah. — [VENDOR/RESMI] [GitHub Docs, “About the repository README file”](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- Docs-as-code memakai issue tracker, version control, plain-text markup, code review, dan automated tests; alur ini memungkinkan fitur diblokir bila dokumentasinya belum ada. — [INDUSTRI] [Write the Docs, “Docs as code”](https://www.writethedocs.org/guide/docs-as-code/)
- MADR 4.0.0 merekomendasikan `docs/decisions/` dan nama `NNNN-title-with-dashes.md`, dengan keputusan lama ditandai `superseded`, bukan ditimpa. — [INDUSTRI—template proyek resmi] [Markdown Architectural Decision Records](https://adr.github.io/madr/)
- CHANGELOG adalah daftar perubahan terkurasi untuk manusia dengan `Unreleased`, urutan kronologis terbalik, tanggal ISO, dan kategori Added/Changed/Deprecated/Removed/Fixed/Security; git log diff penuh noise. — [INDUSTRI—konvensi proyek] [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/)
- ISO/IEC/IEEE 29148:2018 menetapkan information items requirements engineering serta panduan formatnya; dalam catatan ini dipakai hanya sebagai konteks tata kelola artefak. — [STANDAR] [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html)
- SemVer 2.0.0 memetakan MAJOR/MINOR/PATCH; Conventional Commits 1.0.0 memetakan `fix`, `feat`, dan `BREAKING CHANGE`; keduanya memudahkan otomasi rilis. — [INDUSTRI] [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html); [INDUSTRI] [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)
- Monorepo bukan monolith: proyek tetap dapat dibangun/uji/deploy sendiri; tanpa tooling graph muncul tes berlebih, hilangnya batas modul, dan tooling tidak konsisten. — [VENDOR/RESMI] [Nx, “What is a Monorepo?”](https://nx.dev/docs/concepts/decisions/why-monorepos); [VENDOR/RESMI] [Turborepo](https://turbo.build/repo/docs/core-concepts/monorepos)
- Nx menyarankan polyrepo bila isolasi akses tingkat repositori wajib atau kode bersama sedikit, serta mengakui beberapa monorepo sebagai jalan tengah dengan biaya CI/tooling berulang. — [VENDOR/RESMI] [Nx, “Monorepo vs Polyrepo”](https://nx.dev/docs/concepts/decisions/monorepo-vs-polyrepo)
- CODEOWNERS memicu review otomatis dan dapat diwajibkan oleh branch protection; GitHub juga mendukung required status checks, linear history, merge queue, signed commits, dan larangan bypass. — [VENDOR/RESMI] [GitHub Docs, “About code owners”](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners); [VENDOR/RESMI] [GitHub Docs, “About protected branches”](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- Config yang berubah antar deploy dipisahkan dari kode dan ditempatkan di environment variables; `.gitignore` serta `.editorconfig` mengatur file tak ter-track dan konsistensi editor. — [INDUSTRI] [The Twelve-Factor App, “Config”](https://12factor.net/config); [VENDOR/RESMI] [git-scm, gitignore](https://git-scm.com/docs/gitignore); [VENDOR/RESMI] [EditorConfig](https://editorconfig.org/)
- Clean Architecture mensyaratkan dependensi sumber hanya mengarah ke dalam; Hexagonal Architecture menempatkan teknologi luar sebagai adapter agar aplikasi dapat diuji tanpa UI/database. — [INDUSTRI] [Robert C. Martin, “The Clean Architecture”](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html); [INDUSTRI] [Alistair Cockburn, “Hexagonal architecture”](https://alistair.cockburn.us/hexagonal-architecture/)
- Trunk-Based Development menekankan trunk yang selalu release-ready dengan perubahan kecil sering; penulis GitFlow menyarankan workflow lebih sederhana untuk continuous delivery web apps. — [INDUSTRI] [Trunk-Based Development](https://trunkbaseddevelopment.com/5-min-overview/); [INDUSTRI—opini penulis model] [nvie, “A successful Git branching model”](https://nvie.com/posts/a-successful-git-branching-model/)

**Rincian, pohon direktori, matriks, dan template berikut merupakan perluasan dari temuan di atas.**

#### Ringkasan eksekutif dan koreksi fakta


Untuk kasus **“versi V1/V2/V3 tertanam langsung pada permukaan API”**, rekomendasi utama adalah **major version di path: `/api/v1`, `/api/v2`, `/api/v3`**, dengan kontrak OpenAPI terpisah per major version, adapter/presenter per versi di lapisan terluar, satu domain model kanonik di dalam, serta siklus deprecation–sunset yang memiliki tanggal dan metrik pemakaian. `[REKOMENDASI PENELITI]` Ini bukan kewajiban standar HTTP: RFC 9110 memisahkan identitas resource dari representasi dan mendefinisikan content negotiation ([STANDAR] [RFC 9110, HTTP Semantics, STD 97](https://www.rfc-editor.org/rfc/rfc9110.html)); Microsoft Azure menyebut URI versioning sederhana dan eksplisit tetapi dapat membebani routing serta HATEOAS ([VENDOR/RESMI] [Best practices for RESTful web API design, Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design)), sedangkan Zalando justru mewajibkan media-type versioning dan melarang URL versioning untuk kontrak REST internalnya ([INDUSTRI—guideline perusahaan] [Zalando RESTful API and Event Guidelines, rule 114](https://opensource.zalando.com/restful-api-guidelines/)). Google Cloud/Apigee menjelaskan bahwa versi di URL paling cocok untuk **entity versioning**—entitas lama dan baru memang berbeda serta memerlukan routing/penyimpanan berbeda—bukan sekadar format representasi ([INDUSTRI] [Google Cloud Blog, “API design: Which version of versioning is right for you?”](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you)). Karena brief menuntut V1/V2/V3 yang terlihat pada API dan tiga versi hidup bersamaan, path memberi visibilitas, routing, dokumentasi, SDK, dan metrik per versi paling sederhana; batasannya harus diakui secara eksplisit.

##### Koreksi fakta penting

- **RFC 8594 = `Sunset` HTTP response header**, bukan `Deprecation`. [`Sunset` berisi satu HTTP-date dan menandakan resource diperkirakan menjadi tidak responsif; klien SHOULD memperlakukannya sebagai hint](https://www.rfc-editor.org/rfc/rfc8594.html). `[STANDAR]`
- **RFC 9745 = `Deprecation` HTTP response header**, diterbitkan Maret 2025 sebagai Standards Track. [`Deprecation` berupa Structured Field Date, misalnya `Deprecation: @1688169599`; deprecation tidak mengubah perilaku resource](https://www.rfc-editor.org/rfc/rfc9745.html). `[STANDAR]`
- RFC 9745 melarang timestamp `Sunset` lebih awal daripada `Deprecation` dan menyarankan `Link: <...>; rel="deprecation"` ke dokumentasi; RFC 8594 menyediakan `rel="sunset"` untuk kebijakan dan mitigasi. ([STANDAR] [RFC 9745 §3–4](https://www.rfc-editor.org/rfc/rfc9745.html); [RFC 8594 §6, §9](https://www.rfc-editor.org/rfc/rfc8594.html))
- `openapi` dan `info.version` bukan versi API yang sama: `openapi` adalah versi fitur spesifikasi OAS, sedangkan `info.version` adalah versi **OpenAPI document**; keduanya dibedakan dari versi API/implementasi. ([STANDAR] [OpenAPI Specification 3.2.0 §4.1–4.2](https://spec.openapis.org/oas/v3.2.0.html); [3.1.0 §4.8.1–4.8.2](https://spec.openapis.org/oas/v3.1.0.html))
- Zalando dan Google Cloud/Apigee **berbeda pendapat** tentang media-type versioning: Zalando mewajibkannya ([Zalando rule 114](https://opensource.zalando.com/restful-api-guidelines/)), sementara tulisan Apigee menyarankan `Accept-Version` untuk format versioning dan menentang menyisipkan versi/entity type ke `Accept`/`Content-Type` ([Google Cloud Blog](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you)). Keduanya `[INDUSTRI]`, bukan standar IETF. Catatan ini tidak memilih salah satu sebagai “standar”; ia memilih path untuk constraint bisnis brief.

---

#### A. Skema folder/direktori dokumentasi proyek

##### 1. Prinsip penempatan

- Dokumentasi sebaiknya diperlakukan dengan alat dan alur yang sama dengan kode—issue tracker, version control, plain-text markup, code review, dan automated tests—karena itu memungkinkan perubahan fitur diblokir bila dokumentasinya belum tersedia. `[INDUSTRI]` [Write the Docs, “Docs as code”](https://www.writethedocs.org/guide/docs-as-code/).
- README adalah **navigation hub**, bukan tempat seluruh dokumentasi: GitHub merekomendasikan README memuat apa yang dilakukan proyek, manfaatnya, cara memulai, tempat mendapatkan bantuan, dan siapa pemeliharanya; dokumentasi panjang lebih cocok di wiki/docs. README, LICENSE, citation file, CONTRIBUTING, dan code of conduct bersama-sama menyampaikan ekspektasi proyek. `[VENDOR/RESMI]` [GitHub Docs, “About the repository README file”](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes). GitHub mencari README pada `.github/`, root, lalu `docs/`, dan merekomendasikan tautan relatif untuk file dalam repositori agar tetap bekerja pada clone. `[VENDOR/RESMI]` [URL yang sama](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes).
- ADR ditempatkan dekat kode dan di-version-control; MADR 4.0.0 merekomendasikan folder `docs/decisions/` dan pola nama `NNNN-title-with-dashes.md`. `[INDUSTRI—template proyek resmi]` [Markdown Architectural Decision Records (MADR)](https://adr.github.io/madr/).
- Spesifikasi API sebaiknya berada di source control dan dipublikasikan; Zalando mensyaratkan satu YAML self-contained dan hanya membolehkan remote reference yang durable/immutable karena referensi yang dapat berubah diam-diam mengubah semantik kontrak. `[INDUSTRI—company guideline]` [Zalando, rules 101 dan 234](https://opensource.zalando.com/restful-api-guidelines/).
- CHANGELOG adalah daftar perubahan **terkurasi untuk manusia**, urut kronologis terbalik, dengan `Unreleased`, tanggal ISO, dan kategori `Added/Changed/Deprecated/Removed/Fixed/Security`; diff git log bukan pengganti. `[INDUSTRI—konvensi proyek]` [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/).
- ISO/IEC/IEEE 29148:2018 menetapkan proses serta **information items** requirements engineering dan memberi panduan formatnya; standar ini disebut hanya sebagai konteks tata kelola artefak, bukan untuk membahas isi BRD/FSD. `[STANDAR]` [ISO/IEC/IEEE 29148:2018, halaman standar ISO](https://www.iso.org/standard/72089.html).

##### 2. Pohon direktori dokumentasi konkret

```text
{{NAMA_PROYEK}}/
├── README.md                              # Navigation hub: quickstart + peta tautan, BUKAN duplikasi isi dokumen
├── CHANGELOG.md                           # Satu-satunya human-facing release history; format Keep a Changelog
├── CONTRIBUTING.md                        # Cara kontribusi, Conventional Commits, PR, review, DoD
├── LICENSE                                # Lisensi; README/CONTRIBUTING/code of conduct melengkapi ekspektasi proyek
├── CODE_OF_CONDUCT.md
├── .editorconfig                          # Konsistensi indentasi/EOL/encoding lintas editor
├── .gitignore                             # File generated/local yang sengaja tidak tracked
├── .github/
│   ├── CODEOWNERS                         # Kepemilikan per jalur; file ini ikut dilindungi owner-nya
│   ├── ISSUE_TEMPLATE/                    # Template issue; bukan artefak fase dokumen
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/                         # CI config: lint docs, cek link, validasi OpenAPI, contract tests
│       ├── ci.yaml
│       ├── docs.yaml
│       └── release.yaml
├── docs/
│   ├── README.md                          # Indeks docs + status versi dokumen + tautan ke README root
│   ├── index.md                           # Opsional: landing page docs-site / navigation hub teknis
│   ├── getting-started/                   # Onboarding, prasyarat, perintah lokal
│   │   └── local-setup.md
│   ├── requirements/                      # HANYA wadah artefak requirements peneliti lain; isi tidak dibahas di sini
│   │   ├── README.md                      # Daftar source-of-truth + status; hindari duplikasi isi
│   │   └── {{ID_ARTEFAK_REQUIREMENTS}}.md
│   ├── design/                            # HANYA wadah artefak desain peneliti lain
│   │   ├── README.md
│   │   └── {{ID_ARTEFAK_DESAIN}}.md
│   ├── adr/                               # ADR immutable; keputusan baru = file baru, bukan menimpa lama
│   │   ├── README.md                      # Index ADR: nomor, judul, status, superseded-by
│   │   ├── template.md
│   │   └── {{NNNN}}-{{judul-keputusan}}.md
│   ├── api/                               # Kontrak API sebagai source-of-truth per major version
│   │   ├── README.md                      # Matriks status V1/V2/V3 + tautan deprecation policy
│   │   ├── v1/openapi.yaml                # OAS 3.1/3.2; info.version = versi dokumen kontrak
│   │   ├── v2/openapi.yaml
│   │   ├── v3/openapi.yaml
│   │   ├── schemas/                       # Hanya jika memakai multi-document OAD dengan referensi stabil
│   │   │   └── {{NAMA_SCHEMA}}.yaml
│   │   ├── examples/                      # Contoh request/response per versi
│   │   │   ├── v1/{{KASUS}}.json
│   │   │   ├── v2/{{KASUS}}.json
│   │   │   └── v3/{{KASUS}}.json
│   │   ├── migration/                     # Panah migrasi v1→v2, v2→v3; bukan placeholder kosong
│   │   │   ├── v1-to-v2.md
│   │   │   └── v2-to-v3.md
│   │   └── lifecycle/
│   │       ├── support-policy.md          # N-1/N-2, tanggal deprecation & sunset, kriteria metrik
│   │       ├── deprecation.md             # Dokumen yang ditunjuk rel="deprecation"
│   │       └── sunset.md                  # Dokumen yang ditunjuk rel="sunset"
│   ├── test/                              # HANYA wadah artefak testing peneliti lain
│   │   ├── README.md
│   │   └── {{ID_ARTEFAK_TEST}}.md
│   ├── reports/                           # HANYA wadah laporan peneliti lain
│   │   ├── README.md
│   │   └── {{YYYY}}/{{MM}}/
│   ├── templates/                         # Template kosong siap salin; bukan hasil/artefak final
│   │   ├── adr.md
│   │   ├── changelog-entry.md
│   │   ├── definition-of-done.md
│   │   ├── rtm.md
│   │   ├── release-checklist.md
│   │   └── raci.md
│   ├── governance/                        # Tata kelola: DoD, RTM, RACI, release checklist
│   │   ├── definition-of-done.md
│   │   ├── rtm.md
│   │   ├── raci.md
│   │   └── release-checklist.md
│   └── research_notes/                    # Catatan riset sementara; diberi tanggal + status + sumber
│       └── {{YYYY-MM-DD}}-{{TOPIK}}.md
├── config/                                # Konfigurasi application/deploy yang AMAN di-commit
│   ├── config.example.yaml                # Nama/nilai non-rahasia; contoh saja
│   ├── environments/
│   │   ├── development.yaml
│   │   ├── staging.yaml
│   │   └── production.yaml
│   └── README.md                          # Daftar env var; secret hanya dari secret manager
└── Makefile                               # atau Justfile: target build/test/lint/docs/release
```

**Keterangan isi dan aturan anti-duplikasi** `[REKOMENDASI PENELITI]` berdasarkan [GitHub Docs README](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes), [Write the Docs docs-as-code](https://www.writethedocs.org/guide/docs-as-code/), [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), [MADR](https://adr.github.io/madr/), dan [Zalando API First](https://opensource.zalando.com/restful-api-guidelines/):

| Folder | Isi | Tidak boleh diduplikasi ke |
|---|---|---|
| `README.md` ringkas + peta tautan | Quickstart, owner, status, tautan ke docs/API/ADR/CHANGELOG | Isi panjang BRD/FSD/desain/test/laporan |
| `requirements/`, `design/`, `test/`, `reports/` | **Satu file kanonik per artefak** milik peneliti 1–5 | Ringkasan di README, salinan di `research_notes/`, lampiran di ADR |
| `adr/` | Satu keputusan per file, immutable; status `superseded by` bila berubah | CHANGELOG (cukup menautkan ADR) |
| `api/v{1,2,3}/openapi.yaml` | Kontrak wire yang berlaku untuk major version tersebut | Contoh payload yang sudah menjadi `examples/`; salinan “latest.yaml” yang tak bertanggal |
| `templates/` | Placeholder dan instruksi | Artefak final di `governance/` atau `adr/` |
| `research_notes/` | Bukti/sumber dan catatan belum final | CHANGELOG atau dokumen normatif |
| `CHANGELOG.md` | Ringkasan perubahan yang dirilis, dikurasi | Git log mentah, release notes platform yang tidak portabel |
| `config/` | Nama variabel, default aman, template | Secret, kredensial, nilai per-deploy yang harus dari environment |

##### 3. Versioning dokumen dan fase BRD→…→Laporan

`[REKOMENDASI PENELITI]` Berdasarkan [SemVer 2.0.0](https://semver.org/spec/v2.0.0.html), [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), [OpenAPI 3.2.0 §4.1–4.2](https://spec.openapis.org/oas/v3.2.0.html), dan [Zalando rules 116/215](https://opensource.zalando.com/restful-api-guidelines/):

1. **Satu artefak = satu canonical path.** README dan `docs/*/README.md` hanya berisi indeks/status/tautan; jangan menyalin paragraf isi.
2. **Versi dokumen proyek mengikuti SemVer** bila dokumen dipakai sebagai kontrak/publikasi; MAJOR untuk perubahan inkompatibel, MINOR untuk tambahan kompatibel, PATCH untuk perbaikan. `[INDUSTRI—spesifikasi komunitas]` [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).
3. **Versi kontrak OpenAPI** memakai `openapi: 3.1.0`/`3.2.0` untuk fitur spesifikasi dan `info.version` untuk versi dokumen OAD; keduanya tidak identik dengan `/api/v3`. `[STANDAR]` [OpenAPI 3.2.0](https://spec.openapis.org/oas/v3.2.0.html). Zalando mensyaratkan SemVer pada `info.version`, `x-api-id` immutable, dan `x-audience`. `[INDUSTRI—company guideline]` [Zalando rules 116/215/218/219](https://opensource.zalando.com/restful-api-guidelines/).
4. **Major API version = folder kontrak + dokumen migrasi tersendiri.** `v1/openapi.yaml`, `v2/openapi.yaml`, `v3/openapi.yaml` tidak saling menimpa; snapshot lama tetap dapat dibaca pada Git tag.
5. **Tiga lapis rekam:** Git history untuk siapa/mengapa per baris; ADR untuk keputusan; CHANGELOG untuk dampak yang dirasakan konsumen. Jangan memaksa ketiganya berisi narasi identik. `[INDUSTRI]` [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); [MADR](https://adr.github.io/madr/).
6. **Artefak fase** yang diminta brief—BRD → FSD → Desain → Testing → Laporan Harian—dipetakan ke `requirements/`, `requirements/` atau subfolder fase yang disepakati, `design/`, `test/`, `reports/{{YYYY}}/{{MM}}/`. Peneliti ini hanya menetapkan **lokasi + konvensi nama + hub navigasi**; isi, section, dan formatnya berada di luar scope.

##### 4. Template utama: `docs/README.md` navigation hub

```markdown
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
```

---

#### B. Skema project/repositori

##### 1. Monorepo vs polyrepo vs multi-repo

**Definisi resmi Nx:** monorepo adalah satu repositori berisi beberapa proyek dengan relasi yang terdefinisi; monorepo **bukan monolith**, karena tiap proyek tetap dapat dibangun, diuji, dan dideploy sendiri. `[VENDOR/RESMI]` [Nx, “What is a Monorepo?”](https://nx.dev/docs/concepts/decisions/why-monorepos). Nx menyebut keuntungan yang dapat diverifikasi: shared code tanpa publish, single source of truth, atomic change, konvensi yang dapat ditegakkan, developer mobility, dan satu kebijakan dependensi; tanpa tooling yang memahami graph, muncul tes yang tidak perlu, tidak ada batas kode, dan tooling tidak konsisten. `[VENDOR/RESMI]` [URL yang sama](https://nx.dev/docs/concepts/decisions/why-monorepos). Turborepo menambahkan remote cache dan task scheduling untuk mengatasi ribuan task monorepo. `[VENDOR/RESMI]` [Turborepo, “What is Turborepo?”](https://turbo.build/repo/docs/core-concepts/monorepos).

| Dimensi | Monorepo | Polyrepo | Multi-repo / beberapa monorepo |
|---|---|---|---|
| Perubahan lintas API + konsumen | Satu PR atomik | Beberapa PR dan rilis berurutan | Atomik di dalam klaster, koordinasi antar klaster |
| Isolasi akses | Per-folder ownership/graph rules | Per-repository permission | Per klaster |
| Cadence rilis | Artefak punya tag sendiri; tidak harus deploy bersama | Independen secara default | Independen antar klaster |
| CI | Perlu affected detection/cache | Banyak pipeline kecil yang diulang | Beberapa pipeline + tooling berulang |
| Dependensi | Single-version policy dapat ditegakkan | Versi mudah drift | Kebijakan per klaster |
| Cocok bila | Banyak shared code, perubahan API+UI sering bersamaan, konvensi disepakati |Isolasi repository-level adalah hard requirement, sedikit kode bersama | Batas domain/legal/public-vs-internal nyata |
| Tooling | Nx/Turborepo/Bazel/Rush, package-manager workspaces, affected graph, module boundaries | Template repo, shared plugin/library versi, CI reusable | Kombinasi keduanya |

Sumber klasifikasi dan trade-off: `[VENDOR/RESMI]` [Nx, “Monorepo vs Polyrepo”](https://nx.dev/docs/concepts/decisions/monorepo-vs-polyrepo) dan [Nx, “What is a Monorepo?”](https://nx.dev/docs/concepts/decisions/why-monorepos); `[VENDOR/RESMI]` [Turborepo](https://turbo.build/repo/docs/core-concepts/monorepos). Nx secara eksplisit menyarankan polyrepo bila kontrol akses tingkat repositori wajib atau tim hampir tidak berbagi kode, serta mengakui beberapa monorepo sebagai jalan tengah dengan biaya CI/tooling berulang. `[VENDOR/RESMI]` [Nx, “Monorepo vs Polyrepo”](https://nx.dev/docs/concepts/decisions/monorepo-vs-polyrepo). Keputusan akhir bersifat organisasional—Nx menyebut perlunya kesepakatan tentang dependency management, code ownership, dependency rules, folder structure, Git workflow, CI, dan deployment. `[VENDOR/RESMI]` [URL yang sama](https://nx.dev/docs/concepts/decisions/monorepo-vs-polyrepo).

`[REKOMENDASI PENELITI]` Untuk **API V1/V2/V3 dalam satu layanan**, monorepo atau satu repositori layanan lebih mudah menjaga adapter V1/V2/V3, kontrak OpenAPI, SDK generator, dan migration test berada dalam satu atomic change. Pisahkan ke polyrepo hanya bila batas kepemilikan/akses atau siklus rilis klien benar-benar independen. Dasar: atomic change dan project graph [Nx](https://nx.dev/docs/concepts/decisions/why-monorepos), serta praktik parallel change yang menuntut kode lama/baru dapat dirilis pada fase mana pun [Martin Fowler](https://martinfowler.com/bliki/ParallelChange.html).

##### 2. Layout aplikasi, batas modul, dan arsitektur

Pohon berikut adalah layout monorepo layanan + klien dengan tiga adapter API. `[REKOMENDASI PENELITI]` disusun berdasarkan [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html), [Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/), [Nx module boundaries](https://nx.dev/docs/concepts/decisions/why-monorepos), [12-Factor config](https://12factor.net/config), dan [GitHub CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).

```text
{{NAMA_REPO}}/
├── README.md                              # Navigation hub + quickstart + peta dokumen
├── LICENSE
├── CONTRIBUTING.md                        # Conventional Commits, PR, review, branch, DoD
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md                           # Keep a Changelog 1.1.0, urut terbalik, Unreleased
├── .editorconfig                          # root=true; indent/EOL/charset konsisten
├── .gitignore                             # generated, local env, secret, build artifacts
├── Makefile                               # atau Justfile: bootstrap/lint/test/build/docs/release
├── nx.json                                # atau turbo.json: task graph, caching, affected
├── package.json                           # atau go.work / pyproject workspace, sesuai stack
├── .github/
│   ├── CODEOWNERS                         # urutan: .github/, root, docs/; pola terakhir menang
│   └── workflows/
│       ├── ci.yaml                        # build + unit + lint + OpenAPI validation + contract tests
│       ├── release.yaml                   # tag, changelog, SDK generation per API major
│       └── docs.yaml                      # link checker, markdown lint, docs build
├── .gitlab-ci.yml                         # opsional bila GitLab; jangan aktif dua CI identik tanpa owner
├── apps/
│   ├── frontend/{{NAMA_WEB}}/             # UI adapter; tidak berisi aturan domain
│   ├── backend/{{NAMA_API}}/              # HTTP adapter + composition root
│   │   ├── src/
│   │   │   ├── main/{{BAHASA}}/           # bootstrap, DI, config loader
│   │   │   └── interface/http/
│   │   │       ├── v1/                    # controller, request/response DTO, presenter V1
│   │   │       ├── v2/                    # ... V2
│   │   │       ├── v3/                    # ... V3
│   │   │       └── shared/                # middleware, correlation ID, error mapper
│   │   └── tests/
│   │       ├── contract/v1/               # Pact atau contract test V1
│   │       ├── contract/v2/
│   │       └── contract/v3/
│   └── services/{{NAMA_WORKER}}/          # consumer/event worker terpisah
├── packages/                              # atau libs/, sesuai konvensi tooling
│   ├── domain/                            # entitas + aturan bisnis; dependency mengarah ke dalam
│   ├── application/                       # use case + port interface; tidak tahu HTTP/DB
│   ├── adapters/
│   │   ├── persistence/                   # repository SQL/NoSQL; implementasi port
│   │   ├── messaging/                     # publisher/consumer adapter
│   │   └── external/{{VENDOR}}/           # klien pihak ketiga
│   ├── contracts/                         # source-of-truth OpenAPI per versi (atau symlink ke docs/api)
│   │   ├── v1/openapi.yaml
│   │   ├── v2/openapi.yaml
│   │   └── v3/openapi.yaml
│   ├── sdk/                               # generated client per versi; JANGAN edit hasil generate
│   │   ├── v1/{{BAHASA}}/
│   │   ├── v2/{{BAHASA}}/
│   │   └── v3/{{BAHASA}}/
│   └── shared/                            # util murni, types, error problem+json
├── infra/
│   ├── terraform/ atau helm/              # IaC; environment bukan salinan kode aplikasi
│   ├── gateway/                           # route /api/v1, /api/v2, /api/v3 + canary config
│   ├── k8s/                               # Deployment rolling/blue-green/canary manifests
│   └── observability/                     # dashboard + alert per api_version
├── config/
│   ├── config.example.yaml
│   ├── environments/{development,staging,production}.yaml
│   └── README.md                          # daftar nama env var + pemilik + sumber secret
├── scripts/                               # bootstrap, backfill, dual-write verification, SDK generation
│   ├── migrate-expand-{{PERUBAHAN}}.sh
│   ├── backfill-{{PERUBAHAN}}.sh
│   └── verify-parity-v2-v3.sh
├── tests/
│   ├── e2e/                               # end-to-end minimal; kontrak diutamakan oleh Pact
│   ├── compatibility/                     # golden response V1/V2/V3, snapshot skema
│   ├── performance/
│   └── fixtures/
└── docs/                                  # pohon pada bagian A; kontrak bisa di sini atau packages/contracts, PILIH SATU
    └── README.md
```

**Batas modul.** Clean Architecture mensyaratkan **Dependency Rule**: dependensi kode sumber hanya mengarah ke dalam; lapisan dalam tidak boleh mengetahui framework, UI, database, atau nama entity di lapisan luar; data yang melintas batas sebaiknya struktur data sederhana, bukan database row/Entity. `[INDUSTRI]` [Robert C. Martin, “The Clean Architecture”](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html). Hexagonal/Ports & Adapters menempatkan aplikasi di dalam, teknologi luar sebagai adapter yang dapat diganti, sehingga aplikasi dapat diuji tanpa UI/database. `[INDUSTRI]` [Alistair Cockburn, “Hexagonal architecture”](https://alistair.cockburn.us/hexagonal-architecture/). Terjemahan praktis untuk V1/V2/V3: DTO, presenter, dan error mapper **per versi berada di adapter HTTP**, sementara use case dan domain tidak bercabang `if (version == ...)`; adapter yang berubah, bukan kontrak bisnis inti. `[REKOMENDASI PENELITI]`.

**Konfigurasi per environment.** 12-Factor memisahkan config dari kode, menaruh nilai yang berubah antar deploy pada environment variables, dan menghindari file config rahasia yang mudah ikut ter-commit; konfigurasi internal yang tidak berubah antar deploy tetap di kode. `[INDUSTRI]` [The Twelve-Factor App, “Config”](https://12factor.net/config). `.gitignore` officially menentukan file untracked yang sengaja diabaikan dan pola yang sebaiknya di-version-control serta dibagikan melalui clone. `[VENDOR/RESMI—dokumentasi proyek Git]` [git-scm, gitignore](https://git-scm.com/docs/gitignore). EditorConfig menjaga gaya indentasi/EOL/charset lintas editor melalui `.editorconfig` yang ikut version control. `[VENDOR/RESMI—proyek EditorConfig]` [EditorConfig](https://editorconfig.org/).

**Kepemilikan kode.** GitHub `CODEOWNERS` mendefinisikan individu/tim yang bertanggung jawab; owner otomatis diminta review, dan aturan branch protection dapat mewajibkan approval dari code owner. Lokasi yang dikenal: `.github/`, root, `docs/`; jika beberapa file ada, GitHub memakai urutan tersebut; pola cocok terakhir menang dan jalur bersifat case-sensitive. `[VENDOR/RESMI]` [GitHub Docs, “About code owners”](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners). Branch protection secara default melarang force push/delete, serta dapat mewajibkan PR review, status checks, conversation resolution, signed commits, linear history, merge queue, dan deploy sukses; admin dapat pula terkena aturan bila “Do not allow bypassing” diaktifkan. `[VENDOR/RESMI]` [GitHub Docs, “About protected branches”](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches). CI/CD workflows dapat diotomasi di repositori dengan GitHub Actions. `[VENDOR/RESMI]` [GitHub Actions documentation](https://docs.github.com/en/actions).

Contoh `CODEOWNERS` `[REKOMENDASI PENELITI]`:

```text
# .github/CODEOWNERS — pola TERAKHIR yang cocok menang; path case-sensitive
*                                  @{{ORG}}/{{TIM_PLATFORM}}
/.github/                          @{{ORG}}/{{TIM_PLATFORM}}
/.github/CODEOWNERS                @{{ORG}}/{{TIM_PLATFORM}}
/docs/api/                         @{{ORG}}/{{TIM_API}} @{{ORG}}/{{TIM_DOC}}
/docs/api/v1/                      @{{ORG}}/{{TIM_API_LEGACY}}
/docs/api/v2/                      @{{ORG}}/{{TIM_API}}
/docs/api/v3/                      @{{ORG}}/{{TIM_API}}
/docs/api/lifecycle/               @{{ORG}}/{{TIM_API}} @{{ORG}}/{{TIM_SRE}}
/packages/contracts/               @{{ORG}}/{{TIM_API}}
/apps/backend/{{NAMA_API}}/src/interface/http/v1/  @{{ORG}}/{{TIM_API_LEGACY}}
/apps/backend/{{NAMA_API}}/src/interface/http/v2/  @{{ORG}}/{{TIM_API}}
/apps/backend/{{NAMA_API}}/src/interface/http/v3/  @{{ORG}}/{{TIM_API}}
/infra/gateway/                    @{{ORG}}/{{TIM_SRE}}
/infra/observability/              @{{ORG}}/{{TIM_SRE}}
/scripts/                          @{{ORG}}/{{TIM_SRE}} @{{ORG}}/{{TIM_DATA}}
```

##### 3. Konvensi Git, rilis, dan proteksi

| Konvensi | Aturan faktual | Klasifikasi + sitasi |
|---|---|---|
| SemVer 2.0.0 | `MAJOR.MINOR.PATCH`; MAJOR = incompatible API change, MINOR = fungsi tambahan kompatibel, PATCH = bug fix kompatibel; deprecation sebaiknya didokumentasikan dan hadir dalam minimal satu MINOR sebelum penghapusan pada MAJOR | `[INDUSTRI—spesifikasi komunitas]` [semver.org, Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) |
| Conventional Commits 1.0.0 | `<type>[optional scope]: <description>`; `fix`≈PATCH, `feat`≈MINOR, `!` atau footer `BREAKING CHANGE:`≈MAJOR; footers dan body optional | `[INDUSTRI—spesifikasi komunitas]` [conventionalcommits.org v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) |
| Keep a Changelog 1.1.0 | `CHANGELOG.md`, `Unreleased`, kategori Added/Changed/Deprecated/Removed/Fixed/Security, versi terbaru di atas, tanggal ISO, sebutkan SemVer | `[INDUSTRI—konvensi proyek]` [keepachangelog.com 1.1.0](https://keepachangelog.com/en/1.1.0/) |
| Trunk-based | Satu trunk yang selalu release-ready, integrasi kecil dan sering, short-lived review branch, CI sebagai safety net; rilis dari trunk atau branch-for-release | `[INDUSTRI]` [Trunk-Based Development, “Five-minute overview”](https://trunkbaseddevelopment.com/5-min-overview/) |
| GitFlow | `master` + `develop` + feature/release/hotfix; cocok untuk perangkat lunak berversi eksplisit atau beberapa versi di wild, tetapi penulisnya menyarankan workflow lebih sederhana untuk continuous delivery web | `[INDUSTRI—opini penulis model]` [nvie, “A successful Git branching model”, catatan refleksi 2020](https://nvie.com/posts/a-successful-git-branching-model/) |
| Branch protection | required reviews, CODEOWNERS review, status checks, linear history, merge queue, signed commits, larangan bypass | `[VENDOR/RESMI]` [GitHub Docs, “About protected branches”](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) |
| Release tagging | Tag `v{{SEMVER}}`; Conventional Commits/SemVer FAQ menyebut `v` sebagai konvensi nama tag, bukan bagian dari SemVer; signed tag dianjurkan dalam model GitFlow | `[INDUSTRI]` [SemVer FAQ](https://semver.org/spec/v2.0.0.html); [nvie GitFlow](https://nvie.com/posts/a-successful-git-branching-model/) |

`[REKOMENDASI PENELITI]` Untuk 2024–2026 dan API yang terus di-deploy, **trunk-based + short-lived PR + feature flag** lebih selaras dengan continuous delivery dan Expand–Contract daripada GitFlow branch panjang; simpan GitFlow hanya bila organisasi memang harus memelihara beberapa rilis paket/binari lama. Dasar: [Trunk-Based Development](https://trunkbaseddevelopment.com/5-min-overview/), catatan refleksi [GitFlow 2020](https://nvie.com/posts/a-successful-git-branching-model/), dan [Martin Fowler, Parallel Change](https://martinfowler.com/bliki/ParallelChange.html). Tag rilis: `v{{MAJOR}}.{{MINOR}}.{{PATCH}}`; penanda kontrak API: `api-v{{N}}`; tag SDK: `sdk-{{BAHASA}}-v{{N}}-{{SEMVER}}`.

---

#### D. Artefak pendukung “lainnya” — template ringkas

> Semua blok berikut adalah **template Markdown lengkap dengan placeholder `{{...}}`**. Simpan di `docs/templates/`; hasil isi disalin ke path kanonik. ADR mengikuti struktur MADR 4.0.0 ([MADR](https://adr.github.io/madr/)); CHANGELOG mengikuti Keep a Changelog 1.1.0 ([Keep a Changelog](https://keepachangelog.com/en/1.1.0/)); DoD/RTM/RACI/release checklist adalah `[REKOMENDASI PENELITI]` berdasarkan tata kelola [GitHub CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners), [branch protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), [Pact can-i-deploy](https://docs.pact.io/pact_broker/can_i_deploy), dan [RFC 9745/8594](https://www.rfc-editor.org/rfc/rfc9745.html).

##### 1. ADR

```markdown
# {{JUDUL_KEPUTUSAN_SINGKAT}}

- Nomor: {{NNNN}}
- Status: {{proposed|accepted|deprecated|superseded by ADR-{{NNNN_PENGGANTI}}}}
- Tanggal: {{YYYY-MM-DD}}
- Decision makers: {{DAFTAR_PIHAK}}
- Consulted: {{DAFTAR_PIHAK}}
- Informed: {{DAFTAR_PIHAK}}
- Pemilik: {{TIM_PEMILIK}}
- Terkait: {{TAUTAN_ISSUE}} · {{TAUTAN_CHANGELOG}} · {{TAUTAN_OAD}}

## Context and Problem Statement

{{MASKALAH_DAN_KONTEKS_MAKSIMAL_TIGA_KALIMAT}}. Pertanyaan keputusan: {{PERTANYAAN_KEPUTUSAN}}?

## Decision Drivers

- {{DRIVER_1}}
- {{DRIVER_2}}
- {{DRIVER_3}}

## Considered Options

- {{OPSI_1}}
- {{OPSI_2}}
- {{OPSI_3}}

## Decision Outcome

Chosen option: "{{OPSI_TERPILIH}}", karena {{ALASAN_DAN_BUKTI}}. Keputusan ini berlaku untuk {{RUANG_LINGKUP}} sejak {{TANGGAL_EFEKTIF}}.

### Consequences

- Good, because {{KONSEKUENSI_POSITIF}}
- Bad, because {{KONSEKUENSI_NEGATIF}}
- Neutral, because {{KONSEKUENSI_NETRAL}}

### Confirmation

{{CARA_VERIFIKASI: code review, architecture test, contract test, atau audit}}. Bukti: {{TAUTAN_CI_ATAU_REVIEW}}.

## Pros and Cons of the Options

### {{OPSI_1}}
- Good, because {{ARGUMEN}}
- Bad, because {{ARGUMEN}}

### {{OPSI_2}}
- Good, because {{ARGUMEN}}
- Bad, because {{ARGUMEN}}

### {{OPSI_3}}
- Good, because {{ARGUMEN}}
- Bad, because {{ARGUMEN}}

## More Information

- Sumber [STANDAR/VENDOR/RESMI/INDUSTRI]: {{NAMA_DOKUMEN}} — {{URL_LENGKAP}}
- Sumber [STANDAR/VENDOR/RESMI/INDUSTRI]: {{NAMA_DOKUMEN}} — {{URL_LENGKAP}}
- Ditinjau kembali pada: {{TANGGAL_TINJAUAN}} atau "{{TIDAK_ADA}}"
```

##### 2. CHANGELOG

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- {{PERUBAHAN_TAMBAHAN_BELUM_RILIS}}

### Changed
- {{PERUBAHAN_KOMPATIBEL_BELUM_RILIS}}

### Deprecated
- `{{VERSI_API}}` — lihat {{TAUTAN_DEPRECATION}}, sunset {{TANGGAL_SUNSET}}

### Removed
- {{YANG_DIHAPUS_BELUM_RILIS}}

### Fixed
- {{PERBAIKAN_BELUM_RILIS}}

### Security
- {{PERUBAHAN_KEAMANAN_BELUM_RILIS}}

## [{{MAJOR}}.{{MINOR}}.{{PATCH}}] - {{YYYY-MM-DD}}

### Added
- {{FITUR_BARU_KOMPATIBEL}} — ADR-{{NNNN}}

### Changed
- {{PERUBAHAN_PERILAKU_KOMPATIBEL}}

### Deprecated
- Endpoint `{{PATH}}` pada {{VERSI_API}}; pengganti `{{PATH_PENGGANTI}}`

### Removed
- {{FIELD_ATAU_ENDPOINT_YANG_DIHAPUS}} hanya setelah sunset {{TANGGAL_SUNSET}}

### Fixed
- {{BUG_FIX}}

### Security
- {{CVE_ATAU_PERUBAHAN_KEAMANAN}}

[Unreleased]: {{URL_REPO}}/compare/v{{MAJOR}}.{{MINOR}}.{{PATCH}}...HEAD
[{{MAJOR}}.{{MINOR}}.{{PATCH}}]: {{URL_REPO}}/compare/v{{MAJOR_SEBELUMNYA}}.{{MINOR_SEBELUMNYA}}.{{PATCH_SEBELUMNYA}}...v{{MAJOR}}.{{MINOR}}.{{PATCH}}
```

##### 3. Definition of Done

```markdown
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
```

##### 4. RTM (Requirements Traceability Matrix)

```markdown
# Requirements Traceability Matrix — {{NAMA_PROYEK}}

- Versi: {{VERSI_RTM}}
- Pemilik: {{TIM_PEMILIK}}
- Terakhir disinkronkan: {{YYYY-MM-DD}}
- Catatan: tabel ini melacak **lokasi dan status**, bukan menyalin isi requirements/desain/test (topik peneliti 1–5).

| ID Requirement | Sumber kanonik | Keputusan/ADR | Modul / adapter | Kontrak API | Verifikasi | Status | Pemilik |
|---|---|---|---|---|---|---|---|
| {{REQ_001}} | `docs/requirements/{{PATH}}#{{ANCHOR}}` | `docs/adr/{{NNNN}}-{{JUDUL}}.md` | `{{PATH_MODUL}}` | `{{VERSI_API}} {{PATH_OAD}}#{{OPERATION_ID}}` | `{{PATH_TEST}}` / Pact `{{NAMA_PACT}}` | {{draft|implemented|verified|deprecated}} | {{OWNER}} |
| {{REQ_002}} | `docs/requirements/{{PATH}}#{{ANCHOR}}` | {{ADR_ATAU_TIDAK_ADA}} | `{{PATH_MODUL}}` | `{{VERSI_API}} {{PATH_OAD}}#{{OPERATION_ID}}` | `{{PATH_TEST}}` | {{STATUS}} | {{OWNER}} |

## Coverage
- Requirements tanpa pemilik: {{JUMLAH_ATAU_NOL}}
- Requirements tanpa verifikasi: {{JUMLAH_ATAU_NOL}}
- Requirements yang terdampak deprecation `{{VERSI_API}}`: {{DAFTAR_ID}}
- Perubahan RTM harus menautkan: {{TAUTAN_PR}} · {{TAUTAN_CHANGELOG}}
```

##### 5. Checklist release

```markdown
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
```

##### 6. Matriks RACI

```markdown
# RACI — {{PROSES_ATAU_RILIS}}

- Versi: {{VERSI_RACI}}
- Pemilik proses: {{TIM_PEMILIK}}
- Berlaku: {{YYYY-MM-DD}} s.d. {{YYYY-MM-DD}}
- Legenda: R = Responsible, A = Accountable (tepat satu per baris), C = Consulted, I = Informed

| Aktivitas / keputusan | {{PERAN_API}} | {{PERAN_SRE}} | {{PERAN_QA}} | {{PERAN_DOC}} | {{PERAN_PRODUCT}} | {{PERAN_SECURITY}} | A |
|---|---|---|---|---|---|---|---|
| Memilih strategi versioning + menulis ADR | R/A | C | C | C | C | C | {{PERAN_API}} |
| Menjaga OAD V1/V2/V3 dan compatibility gate | R | C | C | C | I | I | {{PERAN_API}} |
| CODEOWNERS, branch protection, release tag | C | R | C | I | I | C | {{PERAN_SRE}} |
| Expand/backfill/dual-write database | R | C | C | I | I | I | {{PERAN_API}} |
| Canary/blue-green/rolling + rollback | C | R/A | C | I | I | I | {{PERAN_SRE}} |
| Pact contract + `can-i-deploy` | R | C | R | I | I | I | {{PERAN_QA}} |
| CHANGELOG, migration guide, deprecation/sunset docs | C | I | C | R | C | I | {{PERAN_DOC}} |
| `Deprecation`/`Sunset` header dan kebijakan N-1/N-2 | R | C | C | C | C | I | {{PERAN_PRODUCT}} |
| Komunikasi konsumen dan pengecualian sunset | C | I | I | R | A | I | {{PERAN_PRODUCT}} |
| Metrik/alert per versi dan kriteria contract | C | R | C | I | C | I | {{PERAN_SRE}} |
| Secret/config/editorconfig/gitignore | C | R | I | I | I | A | {{PERAN_SECURITY}} |
| Persetujuan mematikan V{{N}} | C | C | C | C | A | C | {{PERAN_PRODUCT}} |

Catatan: satu A per baris; bila organisasi memakai GitLab/governance lain, tetapkan pemilik baru dan simpan versi lama dalam Git history.
```

---

### Inferences

- Docs-as-code, CODEOWNERS, dan branch protection mengubah tata kelola dari sekadar prose menjadi gate yang dapat diverifikasi CI.
- Satu canonical path per artefak plus pemisahan `templates/` dari artefak final mengurangi drift tanpa melarang tautan navigasi.
- Monorepo hanya menguntungkan bila graph ketergantungan, affected detection, caching, dan module boundaries benar-benar dioperasikan.
- Trunk-based dan short-lived PR lebih selaras dengan Expand–Contract daripada integrasi branch panjang.

### Gaps

- Tidak ditemukan RFC/ISO yang menetapkan nama folder dokumentasi, daftar file root, atau konvensi `docs/requirements/` secara universal; semuanya berasal dari dokumentasi resmi/proyek dan praktik industri.
- Tidak ada angka baku untuk ukuran tim, jumlah repositori, atau ambang CI yang memaksa monorepo/polyrepo; keputusan tetap organisasional.
- PayPal API Design Guidelines tidak berhasil diverifikasi langsung pada URL repositori yang dicoba (HTTP 404), sehingga sengaja tidak dijadikan dasar klaim.

## Pertanyaan kunci 2 — API versioning zero-downtime V1/V2/V3 (prioritas utama)

### Takeaway

Untuk versi yang **di-embed langsung pada permukaan API**, rekomendasi utama adalah path major `/api/v1`, `/api/v2`, `/api/v3` dengan satu OpenAPI Description per major, Expand–Contract pada database/kontrak, lifecycle `Deprecation`/`Sunset` sesuai RFC 9745/8594, serta keputusan sunset berbasis metrik pemakaian per versi. `[REKOMENDASI PENELITI]` — [VENDOR/RESMI] [Microsoft Learn, RESTful web API design](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design), [STANDAR] [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html), [STANDAR] [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html), [STANDAR] [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html), [INDUSTRI] [Martin Fowler, “Parallel Change”](https://martinfowler.com/bliki/ParallelChange.html).

### Cited Findings

- RFC 9110 memisahkan resource dari representation dan mendefinisikan content negotiation; RFC 9111 menetapkan method + target URI sebagai minimum cache key serta mewajibkan kecocokan header yang dinominasikan `Vary`. — [STANDAR] [RFC 9110, HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html); [STANDAR] [RFC 9111, HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111.html)
- RFC 9745 mendefinisikan `Deprecation` sebagai Structured Field Date (`@<unix-seconds>`), `rel="deprecation"`, dan menegaskan deprecation tidak mengubah perilaku; RFC 8594 mendefinisikan `Sunset` sebagai HTTP-date hint serta `rel="sunset"`. — [STANDAR] [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html); [STANDAR] [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html)
- RFC 9745 melarang `Sunset` lebih awal daripada `Deprecation` dan mencatat perbedaan format tanggal historis kedua header. — [STANDAR] [RFC 9745 §4](https://www.rfc-editor.org/rfc/rfc9745.html)
- OAS 3.1.0/3.2.0 memisahkan `openapi`, `info.version`, versi API, dan versi implementasi; OAS 3.2 memperbolehkan OAD multi-document dan merekomendasikan entry document `openapi.yaml`/`openapi.json`. — [STANDAR] [OpenAPI 3.1.0](https://spec.openapis.org/oas/v3.1.0.html); [STANDAR] [OpenAPI 3.2.0](https://spec.openapis.org/oas/v3.2.0.html); [STANDAR] [OpenAPI 3.2.1](https://spec.openapis.org/oas/v3.2.1.html)
- OpenAPI 3.1.0 menyediakan `deprecated` pada Operation/Parameter; RFC 9457 menetapkan `application/problem+json` dan anggota `type/title/status/detail/instance`. — [STANDAR] [OpenAPI 3.1.0](https://spec.openapis.org/oas/v3.1.0.html#operation-object); [STANDAR] [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html)
- Microsoft menjabarkan URI/query/header/media-type versioning, menyebut URI sederhana-eksplisit dan cache-friendly, serta memperingatkan duplikasi cache untuk header/media type; Zalando mewajibkan media-type versioning dan melarang URL versioning; Google Cloud/Apigee membedakan format vs entity versioning dan merekomendasikan `Accept-Version` untuk format. — [VENDOR/RESMI] [Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design); [INDUSTRI—company guideline] [Zalando RESTful API Guidelines](https://opensource.zalando.com/restful-api-guidelines/); [INDUSTRI—opini penulis Apigee] [Google Cloud Blog](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you)
- Stripe memilih versi per request melalui `Stripe-Version`, SDK pin, atau default akun; versi juga menentukan webhook dan automated operations; release bulanan tanpa breaking change, major dua kali setahun dapat breaking. — [VENDOR/RESMI] [Stripe Docs, “How API versioning works”](https://docs.stripe.com/api-versions)
- Zalando, Google AIP-180, dan Stripe mengklasifikasikan penambahan opsional/response field umumnya kompatibel, sedangkan required field baru, rename/removal, perubahan tipe/default/semantik, validasi lebih ketat, dan format error/pagination berisiko breaking. — [INDUSTRI] [Zalando rules 106–108](https://opensource.zalando.com/restful-api-guidelines/); [INDUSTRI] [Google AIP-180](https://google.aip.dev/180); [VENDOR/RESMI] [Stripe](https://docs.stripe.com/api-versions)
- Martin Fowler membagi Parallel Change menjadi expand, migrate, contract; canary/blue-green adalah aplikasinya, feature flag dapat memisahkan rilis supplier dan klien, dan contract yang tidak dituntaskan memperburuk keadaan. — [INDUSTRI] [Martin Fowler, “Parallel Change”](https://martinfowler.com/bliki/ParallelChange.html); [INDUSTRI] [Martin Fowler, “Canary Release”](https://martinfowler.com/bliki/CanaryRelease.html)
- Kubernetes `RollingUpdate` menaikkan ReplicaSet baru sambil menurunkan lama, menyediakan rollback dan `progressDeadlineSeconds`; AWS API Gateway canary memisahkan rasio traffic serta log/metrik canary. — [VENDOR/RESMI] [Kubernetes Docs, “Deployments”](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/); [VENDOR/RESMI] [AWS API Gateway canary](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md)
- Pact Matrix dan `can-i-deploy`/`record-deployment` memungkinkan keputusan deploy berdasarkan verifikasi kontrak terhadap versi aplikasi yang sudah ada di environment. — [VENDOR/RESMI] [Pact Docs, “Can I Deploy”](https://docs.pact.io/pact_broker/can_i_deploy); [VENDOR/RESMI] [Pact Docs, “CI/CD Setup Guide”](https://docs.pact.io/pact_nirvana)
- SemVer mensyaratkan deprecation didokumentasikan dan hadir dalam minimal satu MINOR sebelum removal pada MAJOR; Conventional Commits memetakan breaking change ke MAJOR. — [INDUSTRI] [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html); [INDUSTRI] [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)

**Rincian tabel perbandingan, aturan kompatibilitas, urutan deploy, contoh endpoint/OpenAPI/routing, matriks V1/V2/V3, dan timeline berikut merupakan perluasan dari temuan di atas.**

#### C. API versioning zero-downtime V1/V2/V3 — prioritas utama

##### 1. Perbandingan opsi menanamkan versi

| Opsi | Contoh | Visibilitas | Cacheability | Routing | Kemudahan klien | OpenAPI/SDK | Kapan dipakai |
|---|---|---|---|---|---|---|---|
| **Path / URI** | `GET /api/v3/orders/{id}` | Sangat tinggi: log, browser, docs, dashboard | Tinggi: method + target URI adalah minimum cache key; tiap versi URI berbeda | Paling sederhana: prefix route di gateway/service | Paling mudah; URL dapat diketuk, dibookmark; tetapi HATEOAS link harus memuat versi | Sangat baik: satu dokumen + satu generator per major | **Pilihan utama** untuk V1/V2/V3 eksplisit, entity versioning, gateway routing dan metrik per versi |
| Query parameter | `GET /api/orders/{id}?version=3` | Tinggi | Umumnya baik bila query masuk cache key; Microsoft mencatat browser/proxy lama kadang tidak menyimpan respons ber-query | Perlu parsing query; default wajib untuk klien lama | Mudah, tetapi mudah tertinggal saat menyalin URL | Perlu parameter versi di semua operasi; generator bisa bingung bila versi juga di path | API sederhana/internal yang ingin resource URI tetap; bukan pilihan utama brief |
| Custom header | `Api-Version: 3` atau `Accept-Version: 2` | Rendah di log/browser; perlu tooling | Rentan: cache wajib `Vary` atas header versi; Microsoft memperingatkan duplikasi data di server-side cache bila header tidak menjadi kunci | Header inspection di gateway | Perlu SDK/Postman; sulit uji GET lewat address bar | Bisa dengan parameter header global, tetapi dokumentasi lintas versi kurang langsung | Format versioning yang menyimpan satu canonical URI; atau kontrol berverbasis SDK |
| Media type / `Accept` | `Accept: application/vnd.{{org}}.v3+json` | Sedang; terlihat pada negotiation | Perlu `Vary: Accept`; RFC 9111 mensyaratkan header yang dinominasikan `Vary` cocok sebelum respons dipakai ulang | Content negotiation, bukan sekadar prefix path | Klien wajib mengelola media type; cocok untuk HATEOAS karena MIME type dapat masuk link | OpenAPI dapat mendeklarasikan beberapa media type, tetapi satu dokumen per major tetap lebih aman | Zalando mewajibkan ini untuk breaking payload schema; Apigee justru menentang versi di `Accept`/`Content-Type` |
| Versi di payload/envelope | `{"apiVersion":"V3", "data":{...}}` | Tinggi di body, rendah di routing/log | Body tidak membantu HTTP cache key; body biasanya tidak dipakai generic cache | Tidak bisa routing sebelum body dibaca; berisiko untuk gateway | Campur metadata dengan domain; Apigee menyarankan entity version justru di body | Buruk sebagai satu-satunya kontrak HTTP; sulit menghasilkan SDK yang rapi | Metadata tambahan/audit, **bukan pengganti** versi permukaan HTTP |
| Date-based / Stripe | `Stripe-Version: 2026-10-28.endive` | Sedang; eksplisit pada request/SDK/account | Sama seperti header: butuh `Vary` bila di-cache | Versi dipilih per request oleh header/SDK/account, juga menentukan webhook dan automated operations | Sangat baik bila SDK mem-pin; klien dapat upgrade terkontrol | Vendor-specific; bukan pola path V1/V2/V3 | API dengan perubahan incremental terjadwal dan ekosistem SDK/webhook yang kuat |

**Sumber per baris:**

- Path/query/header/media type, trade-off cache dan HATEOAS: `[VENDOR/RESMI]` [Microsoft Learn, “Best practices for RESTful web API design”, bagian Implement versioning](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design). Microsoft menyatakan URI/query versioning cache-friendly, sedangkan header/media-type memerlukan pemeriksaan header dan dapat menggandakan data di server-side cache. `[VENDOR/RESMI]` [URL yang sama](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design).
- Cache key minimum = method + target URI; respons content-negotiated dibedakan memakai `Vary`; cache MUST NOT memakai ulang respons bila header yang dinominasikan `Vary` tidak cocok. `[STANDAR]` [RFC 9111, HTTP Caching §2 dan §4.1](https://www.rfc-editor.org/rfc/rfc9111.html).
- Content negotiation dan representasi: `[STANDAR]` [RFC 9110, HTTP Semantics §3.2 dan §12](https://www.rfc-editor.org/rfc/rfc9110.html); contoh vendor media type `application/vnd.github.v3+json` ada pada `[STANDAR]` [OpenAPI 3.1.0 §3.3](https://spec.openapis.org/oas/v3.1.0.html).
- Zalando: `MUST use media type versioning`, `MUST not use URL versioning`, hanya untuk payload schema dan bukan URI/method semantics; versi dinyatakan bersama `Content-Type`/`Accept`. `[INDUSTRI—company guideline]` [Zalando rules 113–114](https://opensource.zalando.com/restful-api-guidelines/).
- Google Cloud/Apigee membedakan format vs entity versioning; merekomendasikan header `Accept-Version`/`Content-Version` untuk format, versi entity di URL, entity version di body, serta menolak versi di `Accept`/`Content-Type`. `[INDUSTRI—opini penulis Apigee]` [Google Cloud Blog, “API design: Which version of versioning is right for you?”](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you).
- Stripe: versi dipilih dari `Stripe-Version` header, pin SDK, atau default akun; menentukan parameter/objek REST, Stripe.js, webhook, dan automated Billing operations; release bulanan tanpa breaking change dan major dua kali setahun dengan breaking change; organization API key wajib menyertakan `Stripe-Version`. `[VENDOR/RESMI]` [Stripe Docs, “How API versioning works”](https://docs.stripe.com/api-versions).

###### REKOMENDASI UTAMA — eksplisit untuk “versi di-embed pada API”

`[REKOMENDASI PENELITI]` **Gunakan major version pada path: `/api/v1/...`, `/api/v2/...`, `/api/v3/...`; jadikan itu satu-satunya penentu major contract.** Alasan yang dapat ditelusuri:

1. Brief mensyaratkan V1/V2/V3 **tertanam/terlihat** dan hidup bersamaan; path paling visibel untuk gateway, log, docs, SDK, dan alert per versi. Microsoft menyebut mekanisme URI sederhana namun eksplisit, dan mengakui kelemahan HATEOAS/akumulasi versi ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design)); Apigee menyebut URL memang diperlukan bila dua entity version diproses oleh implementasi/storage berbeda ([Google Cloud Blog](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you)).
2. URI berbeda menyederhanakan cache key HTTP ([RFC 9111 §2](https://www.rfc-editor.org/rfc/rfc9111.html)) dan menghindari kewajiban `Vary` atas header version yang rawan salah konfigurasi ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design)).
3. Satu OAD per major memudahkan generator klien/server dan dokumentasi; OAS memang memisahkan versi spesifikasi, versi dokumen, dan versi implementasi ([OpenAPI 3.2.0 §4.1–4.2](https://spec.openapis.org/oas/v3.2.0.html)).
4. Perubahan kompatibel **tetap tidak menaikkan major**: tambahkan field opsional pada V3 saat ini daripada menciptakan V4. Zalando mendorong compatible extension dan menghindari versi baru ([Zalando rules 106–113](https://opensource.zalando.com/restful-api-guidelines/)); Google menyarankan mencari perubahan backward-compatible sebelum memversioning ([Google Cloud Blog](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you)); SemVer menempatkan penambahan kompatibel pada MINOR ([SemVer 2.0.0](https://semver.org/spec/v2.0.0.html)).
5. Batasan yang **harus ditulis dalam ADR**: ini mengorbankan kemurnian “satu URI = satu resource” dan membuat HATEOAS link bersifat version-scoped ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design)); Zalando akan menolak desain ini ([Zalando rule 114](https://opensource.zalando.com/restful-api-guidelines/)). Karena keduanya praktik industri, keputusan ini harus menjadi keputusan organisasi yang terdokumentasi, bukan diklaim sebagai kepatuhan standar.

**Lapisan kedua yang opsional:** `Deprecation`, `Sunset`, dan `Link` untuk lifecycle ([RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html), [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html)); `apiVersion` di body hanya untuk audit/telemetri, **bukan** routing. Date-based versioning ala Stripe tetap valid sebagai alternatif vendor, tetapi tidak memenuhi literal V1/V2/V3 dan memindahkan seleksi ke `Stripe-Version`/SDK pin ([Stripe Docs](https://docs.stripe.com/api-versions)).

##### 2. Matriks backward-compatible vs breaking

| Perubahan | Aman di major version berjalan? | Aturan / risiko | Sumber |
|---|---|---|---|
| Menambah resource/endpoint, optional request parameter, response property, event type | **Ya**, bila klien tolerant reader | Stripe mengklasifikasikan ini backward-compatible; klien harus mengabaikan field/event asing | `[VENDOR/RESMI]` [Stripe, “Compatible changes and breaking changes”](https://docs.stripe.com/api-versions) |
| Menambah field required pada request/resource yang sudah ada | **Tidak** | Google AIP-180 melarang required field baru; default perilaku harus tetap seperti sebelum field ada | `[INDUSTRI—guideline Google]` [AIP-180, Backwards compatibility](https://google.aip.dev/180) |
| Menambah field response | Umumnya **ya** | Zalando membolehkan field mandatory/optional pada output-only; klien wajib toleran terhadap field tak dikenal | `[INDUSTRI—company guideline]` [Zalando rule 107/108](https://opensource.zalando.com/restful-api-guidelines/) |
| Mengubah optional menjadi required pada request | **Tidak** | Zalando: input boleh membuat mandatory→optional, bukan sebaliknya | `[INDUSTRI]` [Zalando rule 107](https://opensource.zalando.com/restful-api-guidelines/) |
| Mengubah required menjadi optional pada response | **Tidak** | Zalando: output boleh optional→mandatory, bukan sebaliknya | `[INDUSTRI]` [Zalando rule 107](https://opensource.zalando.com/restful-api-guidelines/) |
| Mengubah tipe data field | **Tidak** | AIP-180 melarang perubahan tipe walaupun wire-compatible karena merusak generated code | `[INDUSTRI]` [AIP-180](https://google.aip.dev/180) |
| Mengubah format nilai, algoritma konstruksi, default value, atau cara serialisasi default | **Tidak** | AIP-180 menggolongkan sebagai perubahan semantik yang dapat merusak klien | `[INDUSTRI]` [AIP-180](https://google.aip.dev/180) |
| Menambah enum value pada request | **Ya**, hati-hati | AIP-180 membolehkan untuk request-only; Zalando membolehkan extended enum input bila server tetap menerima nilai lama | `[INDUSTRI]` [AIP-180](https://google.aip.dev/180); [Zalando rule 107](https://opensource.zalando.com/restful-api-guidelines/) |
| Menambah enum value pada response | **Berisiko / breaking** | Klien dengan enum tertutup dapat gagal; Zalando melarang perluasan enum output dan menyarankan open-ended values; Stripe menyaratkan listener webhook menangani event type asing | `[INDUSTRI]` [Zalando rule 107/108](https://opensource.zalando.com/restful-api-guidelines/); `[VENDOR/RESMI]` [Stripe](https://docs.stripe.com/api-versions) |
| Menghapus atau rename field/parameter/enum/method | **Tidak** | Rename = remove + add; Stripe mencantumkan renamed field/removed parameter/object shape sebagai contoh major breaking change | `[INDUSTRI]` [AIP-180](https://google.aip.dev/180); `[VENDOR/RESMI]` [Stripe](https://docs.stripe.com/api-versions) |
| Memperketat validasi, constraint, batas panjang string | Umumnya **Tidak** | Zalando melarang validasi input lebih restriktif; AIP-180 memperingatkan perubahan batas string/resource name | `[INDUSTRI]` [Zalando rule 107](https://opensource.zalando.com/restful-api-guidelines/); [AIP-180](https://google.aip.dev/180) |
| Mengganti format error | **Tidak** tanpa major baru | RFC 9457 menetapkan `application/problem+json`, anggota `type/title/status/detail/instance`, dan mewajibkan klien mengabaikan extension yang tidak dikenal | `[STANDAR]` [RFC 9457, Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html) |
| Menambahkan pagination setelah sebelumnya mengembalikan semua item | **Berisiko / breaking** | AIP-180: bila default `page_size` baru lebih kecil, klien lama mengira seluruh hasil sudah diterima | `[INDUSTRI]` [AIP-180](https://google.aip.dev/180) |
| Mengganti offset→cursor atau bentuk page object | **Tidak** | Zalando mewajibkan pagination, merekomendasikan cursor, dan mendefinisikan response page `items/self/first/prev/next/last/query` | `[INDUSTRI]` [Zalando rules 159–161, 248](https://opensource.zalando.com/restful-api-guidelines/) |
| Mengubah status code atau semantik metode | **Tidak** | HTTP semantics dan status code adalah bagian dari kontrak; Zalando juga mewajibkan klien siap menerima status code yang tidak didokumentasikan | `[STANDAR]` [RFC 9110 §15](https://www.rfc-editor.org/rfc/rfc9110.html); `[INDUSTRI]` [Zalando rule 108](https://opensource.zalando.com/restful-api-guidelines/) |
| Field removal setelah sunset | Hanya pada **major baru / contract phase** | SemVer mensyaratkan MAJOR untuk perubahan inkompatibel; RFC 9745 menegaskan deprecation tidak mengubah perilaku | `[INDUSTRI]` [SemVer 2.0.0](https://semver.org/spec/v2.0.0.html); `[STANDAR]` [RFC 9745 §5](https://www.rfc-editor.org/rfc/rfc9745.html) |

`[REKOMENDASI PENELITI]` Simpan matriks ini sebagai **compatibility gate CI**: diff OpenAPI V3 terhadap baseline; perubahan yang masuk kategori “Tidak” memblokir rilis minor/patch dan memaksa `feat(api)!:` / ADR V4. Dasar: Conventional Commits memetakan `BREAKING CHANGE` ke MAJOR ([v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)); Zalando membedakan incompatible change dari breaking change yang benar-benar dideploy ([rule 106](https://opensource.zalando.com/restful-api-guidelines/)).

##### 3. Expand–Contract / Parallel Change untuk database dan kontrak

Martin Fowler mendefinisikan tiga fase: **expand** (antarmuka mendukung versi lama dan baru), **migrate** (semua klien berpindah secara inkremental; fase terlama untuk klien eksternal), **contract** (hapus versi lama setelah tidak dipakai). Pola ini memungkinkan rilis pada fase mana pun, cocok dengan Continuous Delivery, serta berlaku untuk refactoring, database refactoring, deployment canary/blue-green, dan remote API evolution; feature flag dapat mengontrol versi yang dipakai selama migrate; bila contract tidak dijalankan, keadaan akhir justru lebih buruk. `[INDUSTRI]` [Martin Fowler, “Parallel Change”](https://martinfowler.com/bliki/ParallelChange.html). Canary release adalah aplikasi Parallel Change dengan migrate sampai seluruh pengguna berpindah; rollback dilakukan dengan mengalihkan pengguna kembali ke versi lama, dan jumlah versi konkuren sebaiknya minimum. `[INDUSTRI]` [Martin Fowler, “Canary Release”](https://martinfowler.com/bliki/CanaryRelease.html).

Urutan deploy yang aman `[REKOMENDASI PENELITI]`, disusun dari [Fowler Parallel Change](https://martinfowler.com/bliki/ParallelChange.html), [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), [AWS API Gateway canary](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md), dan [Pact can-i-deploy](https://docs.pact.io/pact_broker/can_i_deploy):

| # | Fase | Aksi database | Aksi kontrak/API | Aplikasi/deploy | Exit gate |
|---|---|---|---|---|---|
| 0 | Design | Tulis ADR + migration plan + rollback plan | OAD V3 draft, compatibility diff, Pact expectations | Feature flag `{{FLAG_V3}}` off | ADR approved; contract tests merah untuk V3 |
| 1 | **Expand** | Tambah kolom/tabel/index baru yang **nullable** atau kompatibel; jangan drop/rename | Terbitkan `/api/v3` di belakang flag, sementara V1/V2 tetap responsif | Deploy adapter V3 + domain kanonik; rolling update | Old app images masih bisa menulis; health/latency hijau |
| 2 | **Backfill** | Isi data lama ke struktur baru secara idempotent dan terukur | Tidak mengubah response V1/V2 | Jalankan `scripts/backfill-{{PERUBAHAN}}.sh` | Parity check: `{{JUMLAH_BARIS_LAMA}}` vs `{{JUMLAH_BARIS_BARU}}`; drift `{{AMBANG_DRIFT}}` |
| 3 | **Dual-write** | Tulis ke lama **dan** baru dalam satu transaksi/logik yang dapat dikompensasi | Semua versi membaca dari adapter yang sesuai | Rilis kode dual-write lebih dulu daripada konsumen baru | Reconciliation job hijau; tidak ada orphan write |
| 4 | **Dual-read / shadow** | Baca baru, bandingkan dengan lama; sumber kebenaran mulai beralih | V3 dapat diaktifkan untuk internal/canary; V1/V2 tetap kontrak lama | Canary 1%→5%→25%→50%→100%; log/metrik terpisah | Selisih respons di bawah `{{AMBANG_PARITY}}`; error budget terpenuhi |
| 5 | **Switch** | Sumber baca utama = struktur baru, tulis lama masih dijaga untuk rollback | Default docs/SDK → V3; deprecation V2 diumumkan | Promote canary; blue-green cutover bila perlu | `can-i-deploy` hijau; SLO V3 hijau selama `{{JENDELA_OBSERVASI}}` |
| 6 | **Contract** | Setelah sunset dan metrik nol, hapus kolom/tabel/trigger lama pada rilis terpisah | Matikan route V1/V2 → `410 Gone` atau sesuai kebijakan; arsipkan OAD | Hapus adapter/flag lama | Tidak ada traffic versi lama selama `{{JENDELA_NOL_TRAFFIC}}`; backup/rollback tersedia |

**Catatan zero-downtime.** Kubernetes `RollingUpdate` secara bertahap menaikkan ReplicaSet baru dan menurunkan yang lama; default `maxUnavailable` dan `maxSurge` 25%; Deployment dapat di-rollback ke revisi stabil, dan `progressDeadlineSeconds` menandai rollout macet. `[VENDOR/RESMI]` [Kubernetes Docs, “Deployments”](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/). AWS API Gateway canary memisahkan traffic produksi/canary dengan rasio 0.0–100.0, menyediakan stage variable override, serta log dan metrik terpisah; canary dapat dipromosikan atau dibatalkan. `[VENDOR/RESMI]` [AWS API Gateway, “Set up a canary release deployment”](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md). Keduanya adalah **mekanisme deployment**, bukan jaminan kompatibilitas database; Expand–Contract tetap wajib. `[REKOMENDASI PENELITI]`

**Feature flag.** Fowler menyebut feature toggle sisi klien dapat membuat klien forward-compatible dan memisahkan rilis supplier dari klien. `[INDUSTRI]` [Parallel Change](https://martinfowler.com/bliki/ParallelChange.html). Pact docs mencantumkan “Working with Feature Flags” sebagai bagian lanjutan CI/CD guide. `[VENDOR/RESMI—docs proyek Pact]` [Pact, “CI/CD Setup Guide”](https://docs.pact.io/pact_nirvana).

##### 4. Siklus hidup V1→V2→V3: coexistence, N-1/N-2, deprecation, sunset

**Coexistence.** Zalando menyatakan perubahan API tanpa merusak konsumen dapat memakai (a) compatible extension atau (b) versi baru dengan dukungan paralel dan deprecation; jika versi baru terpaksa dibuat, varian lama dan baru didukung bersamaan. `[INDUSTRI]` [Zalando rule 106/113](https://opensource.zalando.com/restful-api-guidelines/). Fowler memperingatkan biaya mempertahankan dua versi selama migrate dan perlunya discipline untuk menuntaskan contract. `[INDUSTRI]` [Parallel Change](https://martinfowler.com/bliki/ParallelChange.html). Stripe menunjukkan production reality: versi request, SDK pin, default akun, webhook endpoint pin, dan automated operations semuanya dapat menentukan versi objek; karena itu versi lama tidak dapat dimatikan hanya karena versi baru sudah dirilis. `[VENDOR/RESMI]` [Stripe Docs](https://docs.stripe.com/api-versions).

**Kebijakan N-1/N-2 adalah keputusan organisasi, bukan angka dari standar.** `[REKOMENDASI PENELITI]` Tidak ada RFC yang menetapkan “dukung N-1 selama 12 bulan”. Tetapkan di `support-policy.md`:

| Kebijakan | Versi aktif | Versi security-only | Versi sunset | Cocok untuk |
|---|---|---|---|---|
| **N-1** | V3 | V2 | V1 | Konsumen internal yang dapat dipaksa upgrade; biaya paling rendah |
| **N-2** | V3 | V2 + V1 | Versi sebelum V1 | Eksternal/mobile/webhook dengan siklus upgrade lambat |
| Kontrak khusus | Sesuai kontrak pelanggan | Sesuai SLA | Sesuai kontrak | Regulated/enterprise; tanggal tidak boleh hanya “nanti” |

Dasar kehati-hatian: RFC 8594 menyatakan `Sunset` hanya hint, bukan jaminan, dan klien SHOULD tetap berfungsi tanpanya; RFC 9745 menyatakan `Deprecation` hanya hint serta tidak mengubah perilaku. ([STANDAR] [RFC 8594 §3, §8](https://www.rfc-editor.org/rfc/rfc8594.html); [RFC 9745 §5, §7](https://www.rfc-editor.org/rfc/rfc9745.html)) Oleh karena itu **komunikasi manusia + metrik** tidak bisa digantikan header saja. `[REKOMENDASI PENELITI]`

**Header standar dan syntax yang benar:**

```http
HTTP/1.1 200 OK
Content-Type: application/json
Deprecation: @{{UNIX_TIMESTAMP_DEPRECATION_V2}}
Sunset: {{HTTP_DATE_SUNSET_V2}}
Link: <https://{{HOST_DOCS}}/api/lifecycle/deprecation>; rel="deprecation"; type="text/html"
Link: <https://{{HOST_DOCS}}/api/lifecycle/sunset>; rel="sunset"; type="text/html"
API-Version: V2
```

- `Deprecation` **MUST** berupa Date Structured Field (`@<unix-seconds>`), dapat di masa lalu atau depan; `rel="deprecation"` menunjuk dokumentasi; keberadaan header tidak mengubah makna/fungsi resource. `[STANDAR]` [RFC 9745 §2–3, §5–6](https://www.rfc-editor.org/rfc/rfc9745.html).
- `Sunset` berisi satu HTTP-date, sebaiknya masa depan; timestamp hanya hint; `rel="sunset"` dapat menghubungkan kebijakan, jadwal, atau mitigasi. `[STANDAR]` [RFC 8594 §3, §6, §8–9](https://www.rfc-editor.org/rfc/rfc8594.html).
- `Sunset` **MUST NOT** lebih awal daripada `Deprecation`; format tanggal keduanya memang berbeda secara historis. `[STANDAR]` [RFC 9745 §4](https://www.rfc-editor.org/rfc/rfc9745.html).
- `API-Version` di contoh di atas **bukan header standar IETF**; itu response metadata internal untuk observability. Jika memakai custom header untuk *menyeleksi* versi, sertakan `Vary` agar cache tidak mencampur respons. `[REKOMENDASI PENELITI]` dasar: [RFC 9111 §4.1](https://www.rfc-editor.org/rfc/rfc9111.html) dan [Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design).
- OpenAPI 3.1.0 menyediakan flag `deprecated` pada Operation dan Parameter, dengan konsumen SHOULD menjauhi operasi yang ditandai. `[STANDAR]` [OpenAPI 3.1.0, Operation Object / Parameter Object](https://spec.openapis.org/oas/v3.1.0.html#operation-object). Gunakan flag ini **bersama** header lifecycle, bukan sebagai pengganti. `[REKOMENDASI PENELITI]`

**Komunikasi ke konsumen** `[REKOMENDASI PENELITI]` berdasarkan [RFC 9745 §3.1](https://www.rfc-editor.org/rfc/rfc9745.html), [RFC 8594 §6](https://www.rfc-editor.org/rfc/rfc8594.html), [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), [SemVer FAQ deprecation](https://semver.org/spec/v2.0.0.html), dan [Stripe API changelog/upgrades](https://docs.stripe.com/api-versions):

1. T+0: ADR + `support-policy.md` + halaman deprecation/sunset dipublikasikan; `Link` rel sudah aktif **sebelum** `Deprecation`.
2. T+0: CHANGELOG entri `Deprecated`, release notes, email/portal developer, dashboard per konsumen, dan migration guide `v2-to-v3.md` dengan contoh request/response.
3. T+0: `Deprecation` header dan `deprecated: true` pada OpenAPI; SDK V2 diberi compile/runtime warning; SDK V3 tersedia.
4. T+{{NOTICE_PERIOD}}: `Sunset` header dengan tanggal pasti; pengingat pada T−90/T−30/T−7 hari; daftar consumer yang masih memakai V2.
5. T+{{SUNSET_DATE}}: route dinonaktifkan sesuai kebijakan—pilih dan dokumentasikan `410 Gone` atau `404 Not Found`; RFC 8594 memberi kedua contoh itu dan menegaskan tidak menjanjikan bentuk respons. `[STANDAR]` [RFC 8594 §9](https://www.rfc-editor.org/rfc/rfc8594.html).
6. Setelah contract: arsipkan OAD, tandai ADR `superseded`, hapus adapter/flag/kolom lama, dan catat di CHANGELOG kategori `Removed`.

**Kriteria mematikan versi lama berbasis metrik** `[REKOMENDASI PENELITI]`; ambang adalah placeholder yang wajib disetujui owner, **bukan angka standar**:

| Metrik | Definisi operasional | Contoh ambang cutover |
|---|---|---|
| Request share per versi | `sum(http_requests_total{api_version="V1"}) / sum(http_requests_total)` | `<= {{AMBANG_REQUEST_SHARE}}` selama `{{JENDELA_OBSERVASI}}` |
| Unique consumer/client_id | `count_distinct(client_id{api_version="V1"})` | `0` untuk `{{JENDELA_NOL_KONSUMEN}}`, atau daftar exception tertanda tangan |
| Webhook/event delivery | Jumlah endpoint yang masih pin versi lama | `0`; Stripe memungkinkan webhook endpoint mem-pin versi sendiri ([Stripe Docs](https://docs.stripe.com/api-versions)) |
| Error/SLO | 5xx, p95/p99, timeout, business-error rate per versi + canary | Tidak melebihi SLO selama `{{JENDELA_OBSERVASI}}` ([AWS canary metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md)) |
| Kontrak | `can-i-deploy` untuk V3 terhadap versi konsumen yang ada di production | Semua verifikasi sukses ([Pact](https://docs.pact.io/pact_broker/can_i_deploy)) |
| Data parity | Perbandingan dual-write/dual-read | Drift `<= {{AMBANG_DRIFT}}` |
| Dukungan | Tiket/eskalasi aktif, kontrak enterprise, regulatory retention | `0` atau pengecualian berdokumen |

Fowler secara eksplisit menyarankan memonitor versi klien yang dipakai dan melakukan contract backend setelah angka pemakaian turun ke level tertentu pada sistem dengan klien yang tidak dapat dipaksa upgrade. `[INDUSTRI]` [Canary Release](https://martinfowler.com/bliki/CanaryRelease.html).

##### 5. Routing/API Gateway, OpenAPI multi-versi, SDK, Pact, observability

**Routing per versi** `[REKOMENDASI PENELITI]`:

- Gateway memetakan prefix `/api/v1`, `/api/v2`, `/api/v3` ke target/service yang sama atau deployment terpisah; setiap route membawa label `api_version`, `route_id`, `consumer_id`, dan correlation ID. Microsoft merekomendasikan propagation `Correlation-ID`/`X-Request-ID`/`X-Trace-ID` untuk end-to-end visibility. `[VENDOR/RESMI]` [Microsoft Learn, distributed tracing section](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design).
- Canary/blue-green/rolling berada **di bawah** pemetaan versi: V3 dapat di-canary tanpa mengubah V1/V2. AWS API Gateway canary memisahkan rasio traffic serta log/metrik canary; Kubernetes Deployment menyediakan rolling update dan rollback. ([VENDOR/RESMI] [AWS](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md); [Kubernetes](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/))
- Untuk versi berbasis header/media type, gateway wajib meneruskan header ke upstream dan cache wajib `Vary`; untuk path, URI menjadi pembeda alami. ([STANDAR] [RFC 9111 §2, §4.1](https://www.rfc-editor.org/rfc/rfc9111.html); [VENDOR/RESMI] [Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design))

Cuplikan konfigurasi routing generik (Nginx-style; **ilustrasi**, bukan dokumentasi vendor tertentu) `[REKOMENDASI PENELITI]`:

```nginx
# infra/gateway/api-versions.conf — ILUSTRASI, sesuaikan dengan gateway Anda
upstream {{UPSTREAM_STABLE}} { server {{HOST_STABLE}}:{{PORT}}; }
upstream {{UPSTREAM_CANARY_V3}} { server {{HOST_CANARY_V3}}:{{PORT}}; }

map $http_x_canary_v3 $target_v3 {
    default {{UPSTREAM_STABLE}};
    "1"     {{UPSTREAM_CANARY_V3}};
}

server {
    listen {{PORT_TLS}} ssl;
    server_name {{API_HOST}};

    location /api/v1/ {
        proxy_set_header X-API-Version "V1";
        proxy_set_header X-Request-ID $request_id;
        add_header Deprecation "@{{UNIX_TIMESTAMP_DEPRECATION_V1}}" always;
        add_header Sunset "{{HTTP_DATE_SUNSET_V1}}" always;
        add_header Link "<https://{{HOST_DOCS}}/api/lifecycle/deprecation>; rel=\"deprecation\"" always;
        add_header Link "<https://{{HOST_DOCS}}/api/lifecycle/sunset>; rel=\"sunset\"" always;
        proxy_pass http://{{UPSTREAM_STABLE}};
    }

    location /api/v2/ {
        proxy_set_header X-API-Version "V2";
        proxy_set_header X-Request-ID $request_id;
        add_header Deprecation "@{{UNIX_TIMESTAMP_DEPRECATION_V2}}" always;
        add_header Sunset "{{HTTP_DATE_SUNSET_V2}}" always;
        proxy_pass http://{{UPSTREAM_STABLE}};
    }

    location /api/v3/ {
        proxy_set_header X-API-Version "V3";
        proxy_set_header X-Request-ID $request_id;
        proxy_pass http://$target_v3;
    }

    # Jika custom header ikut menentukan representasi, jangan lupa:
    # add_header Vary "Accept, API-Version" always;
}
```

**OpenAPI multi-versi.** OAS 3.2.0/3.2.1 mengizinkan OAD satu dokumen atau multi-document dengan referensi URI, merekomendasikan entry document bernama `openapi.json`/`openapi.yaml`, serta memisahkan `openapi`, `info.version`, dan versi API/implementasi; 3.2.1 adalah patch yang tercantum pada daftar versi resmi, sedangkan 3.1.0 memperkenalkan kompatibilitas penuh JSON Schema 2020-12. `[STANDAR]` [OAS 3.2.0](https://spec.openapis.org/oas/v3.2.0.html), [OAS 3.2.1](https://spec.openapis.org/oas/v3.2.1.html), [OAS 3.1.0](https://spec.openapis.org/oas/v3.1.0.html). Zalando merekomendasikan OAS 3.1 untuk API baru, satu YAML self-contained, `x-api-id`, `x-audience`, dan SemVer pada `info.version`. `[INDUSTRI]` [Zalando rules 101/116/215/218/219](https://opensource.zalando.com/restful-api-guidelines/).

Cuplikan tiga OAD `[REKOMENDASI PENELITI]`; ini contoh skematis, bukan seluruh kontrak produksi:

```yaml
# docs/api/v1/openapi.yaml
openapi: 3.1.0
info:
  title: "{{NAMA_API}} V1"
  version: "{{INFO_VERSION_V1}}"           # versi DOKUMEN OAD, bukan "V1" otomatis
  description: "Status: {{STATUS_V1}}. Lihat docs/api/lifecycle/deprecation.md"
  x-api-id: "{{UUID_API_IMMUTABLE}}"
  x-audience: "{{AUDIENCE}}"
servers:
  - url: "https://{{API_HOST}}/api/v1"
paths:
  /orders/{orderId}:
    get:
      operationId: getOrderV1
      deprecated: true
      parameters:
        - name: orderId
          in: path
          required: true
          schema: { type: string }
      responses:
        "200":
          description: "Order V1"
          content:
            application/json:
              schema:
                type: object
                required: [id, total]
                properties:
                  id: { type: string }
                  total: { type: number }
        "404":
          description: "Not found"
          content:
            application/problem+json:
              schema: { $ref: "#/components/schemas/Problem" }
components:
  schemas:
    Problem:
      type: object
      properties:
        type: { type: string, format: uri }
        title: { type: string }
        status: { type: integer }
        detail: { type: string }
        instance: { type: string }
```

```yaml
# docs/api/v2/openapi.yaml
openapi: 3.1.0
info:
  title: "{{NAMA_API}} V2"
  version: "{{INFO_VERSION_V2}}"
  x-api-id: "{{UUID_API_IMMUTABLE}}"
  x-audience: "{{AUDIENCE}}"
servers:
  - url: "https://{{API_HOST}}/api/v2"
paths:
  /orders/{orderId}:
    get:
      operationId: getOrderV2
      deprecated: true
      parameters:
        - name: orderId
          in: path
          required: true
          schema: { type: string }
      responses:
        "200":
          description: "Order V2: amount object replaces numeric total"
          content:
            application/json:
              schema:
                type: object
                required: [id, amount, status]
                properties:
                  id: { type: string }
                  amount:
                    type: object
                    required: [value, currency]
                    properties:
                      value: { type: string }
                      currency: { type: string }
                  status: { type: string, enum: ["CREATED", "PAID", "CANCELLED"] }
```

```yaml
# docs/api/v3/openapi.yaml
openapi: 3.2.0
info:
  title: "{{NAMA_API}} V3"
  version: "{{INFO_VERSION_V3}}"
  x-api-id: "{{UUID_API_IMMUTABLE}}"
  x-audience: "{{AUDIENCE}}"
servers:
  - url: "https://{{API_HOST}}/api/v3"
paths:
  /orders/{orderId}:
    get:
      operationId: getOrderV3
      parameters:
        - name: orderId
          in: path
          required: true
          schema: { type: string }
      responses:
        "200":
          description: "Order V3: cursor pagination + monetary object + RFC 9457 errors"
          content:
            application/json:
              schema:
                type: object
                required: [id, amount, status, links]
                properties:
                  id: { type: string }
                  amount: { $ref: "#/components/schemas/Money" }
                  status: { type: string, enum: ["CREATED", "PAID", "CANCELLED", "REFUNDED"] }
                  links:
                    type: object
                    required: [self, next]
                    properties:
                      self: { type: string, format: uri }
                      next: { type: string, format: uri }
        "404":
          description: "Problem details"
          content:
            application/problem+json:
              schema: { $ref: "#/components/schemas/Problem" }
components:
  schemas:
    Money:
      type: object
      required: [value, currency]
      properties:
        value: { type: string }
        currency: { type: string }
    Problem:
      type: object
      properties:
        type: { type: string, format: uri }
        title: { type: string }
        status: { type: integer }
        detail: { type: string }
        instance: { type: string }
```

**Tiga endpoint versi** `[REKOMENDASI PENELITI]`:

| Versi | Endpoint | Perubahan konkret | Status contoh |
|---|---|---|---|
| V1 | `GET /api/v1/orders/{{ORDER_ID}}` | `total: number` flat; error legacy | Deprecated + Sunset |
| V2 | `POST /api/v2/orders` dan `GET /api/v2/orders/{{ORDER_ID}}` | `total`→`amount{value,currency}`, tambah `status`; breaking terhadap V1 | Deprecated, migrasi ke V3 |
| V3 | `POST /api/v3/orders`, `GET /api/v3/orders/{{ORDER_ID}}`, `GET /api/v3/orders?cursor={{CURSOR}}` | Cursor pagination, `status` extensible, `application/problem+json` | Current |

`application/problem+json` dan anggota `type/title/status/detail/instance` mengikuti `[STANDAR]` [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html); pagination `items/self/next` mengikuti `[INDUSTRI]` [Zalando rules 159–161/248](https://opensource.zalando.com/restful-api-guidelines/); penambahan nilai enum `REFUNDED` pada response V3 sengaja ditempatkan di major baru mengikuti peringatan [Zalando rule 107](https://opensource.zalando.com/restful-api-guidelines/) dan [AIP-180](https://google.aip.dev/180).

**SDK per versi** `[REKOMENDASI PENELITI]` berdasarkan [OpenAPI 3.2.0 §2](https://spec.openapis.org/oas/v3.2.0.html) yang menyebut code-generation tools, serta [Stripe](https://docs.stripe.com/api-versions) yang mem-pin API version lewat SDK:

- Satu OAD → satu package SDK per major: `{{ORG}}-sdk-{{BAHASA}}-v1`, `...-v2`, `...-v3`; generated code jangan diedit manual.
- `v1`/`v2` SDK memuat deprecation warning dan tautan migration guide; V3 SDK menjadi default docs/quickstart.
- Versi SDK mengikuti SemVer sendiri; jangan samakan `sdk-v3@1.4.0` dengan `info.version` atau `/api/v3`.

**Consumer-driven contracts.** Pact Matrix merekam pasangan consumer/provider version yang sudah diuji; `can-i-deploy` sebelum deploy dan `record-deployment` sesudah deploy membuat Broker mengetahui versi aplikasi di tiap environment dan dapat memblokir deploy yang belum terverifikasi. `[VENDOR/RESMI—dokumentasi proyek Pact]` [Pact Docs, “Can I Deploy”](https://docs.pact.io/pact_broker/can_i_deploy). CI/CD guide menempatkan `can-i-deploy` pada Platinum level dan Pact pada deploy pipeline pada Diamond level. `[VENDOR/RESMI]` [Pact Docs, “CI/CD Setup Guide”](https://docs.pact.io/pact_nirvana). Untuk klien mobile yang banyak versinya hidup bersamaan, Pact menyediakan `--all prod` untuk memeriksa semua consumer production. `[VENDOR/RESMI]` [Pact, “Can I Deploy”](https://docs.pact.io/pact_broker/can_i_deploy).

**Observability & alert per versi** `[REKOMENDASI PENELITI]`, berdasarkan [AWS API Gateway canary logs/metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md), [Microsoft correlation headers](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design), dan [Fowler canary monitoring](https://martinfowler.com/bliki/CanaryRelease.html):

| Sinyal | Label minimum | Alert contoh |
|---|---|---|
| `http_requests_total` | `api_version`, `route`, `method`, `status`, `consumer_id` | Lonjakan 4xx/5xx V3 vs baseline V2 > `{{AMBANG_ERROR}}` |
| `http_request_duration_seconds` | `api_version`, `canary`, `region` | p95/p99 V3 > `{{AMBANG_LATENCY}}` selama `{{JENDELA}}` |
| `api_deprecated_requests_total` | `api_version`, `consumer_id` | Masih ada konsumen prioritas tinggi V1 pada T−30 sunset |
| `api_version_request_ratio` | `api_version` | Share V1 tidak turun sesuai timeline |
| `dual_write_mismatch_total` | `entity`, `migration_id` | Drift > `{{AMBANG_DRIFT}}` |
| `contract_verification_result` | `consumer`, `provider`, `version` | `can-i-deploy` gagal |
| Business KPI | `api_version`, `canary` | Regresi signifikan → auto-reroute ke stable |

##### 6. Matriks kompatibilitas V1/V2/V3

`[REKOMENDASI PENELITI]` Matriks ini adalah contoh operasional untuk ilustrasi endpoint di atas. `✅` = didukung, `⚠️` = didukung dengan adaptor/deprecation, `❌` = tidak boleh dipakai.

| Kemampuan / kontrak | V1 | V2 | V3 | Catatan migrasi |
|---|---|---|---|---|
| `GET /orders/{id}` | ✅ | ✅ | ✅ | Path major berbeda, `orderId` domain sama |
| Response `total: number` | ✅ | ❌ | ❌ | V2/V3 memakai `amount.value` string |
| Response `amount{value,currency}` | ❌ | ✅ | ✅ | Adapter V1 memetakan kembali ke `total` |
| Field `status` | ❌ | ✅ | ✅ | Enum V3 lebih luas; klien V2 tidak boleh menerima V3 enum tanpa major baru |
| Enum `REFUNDED` | ❌ | ❌ | ✅ | Perluasan enum response = breaking menurut Zalando/AIP-180 |
| `offset/limit` pagination | ✅ | ✅ | ❌ | V3 memakai cursor; jangan ubah V1/V2 |
| Cursor `self/next` | ❌ | ❌ | ✅ | `next` link bersifat `/api/v3/...` |
| Error `application/problem+json` | ⚠️ | ✅ | ✅ | V1 dipertahankan sesuai kontrak lama; migrasi error handling masuk V3 |
| Header `Deprecation` | ✅ | ✅ | ❌ | V1/V2 saja; syntax RFC 9745 |
| Header `Sunset` | ✅ | ✅ | ❌ | V1 tanggal lebih awal dari V2; RFC 8594 |
| `deprecated: true` pada OpenAPI | ✅ | ✅ | ❌ | OpenAPI 3.1 Operation/Parameter |
| SDK generated | ✅ | ✅ | ✅ | Nama package terpisah |
| Pact contract | ✅ | ✅ | ✅ | `can-i-deploy` per consumer/provider version |
| Default docs/quickstart | ❌ | ❌ | ✅ | README navigation hub menunjuk V3 |
| Write path repo kanonik | ⚠️ | ✅ | ✅ | Expand: dual-write; Switch: V3 source of truth |
| Field removal `total` | ❌ | ❌ | ✅ | Contract hanya setelah sunset V2 + metrik nol |

Sumber aturan: [Zalando compatibility rules 106–108](https://opensource.zalando.com/restful-api-guidelines/), [Google AIP-180](https://google.aip.dev/180), [Stripe compatible/breaking changes](https://docs.stripe.com/api-versions), [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html), [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html), [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html).

##### 7. Timeline migrasi bertahap

Semua tanggal di bawah adalah **placeholder**; isi sesuai kalender organisasi dan zona waktu. `[REKOMENDASI PENELITI]` berdasarkan [SemVer deprecation FAQ](https://semver.org/spec/v2.0.0.html), [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html), [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html), [Fowler Parallel Change](https://martinfowler.com/bliki/ParallelChange.html), dan [AWS canary](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md).

| Tanggal | Fase | V1 | V2 | V3 | Artefak / gate |
|---|---|---|---|---|---|
| `{{T0_V1}}` | V1 GA | Active | — | — | `api-v1` tag, OAD V1, SDK V1 |
| `{{T0_V2}}` | Expand V2 | Active | Active | — | ADR rename `total`; dual-write; Pact V1+V2 hijau |
| `{{T_DEPRECATE_V1}}` | Deprecate V1 | Deprecated | Current | — | `Deprecation` V1, `deprecated: true`, migration v1→v2, CHANGELOG |
| `{{T_SUNSET_V1}}` | Sunset V1 | `410 Gone` | Current | — | `Sunset` V1 terpenuhi; request share V1 = `0`; contract kolom lama tahap 1 |
| `{{T0_V3}}` | Expand V3 | Arsip | Active | Active/canary | OAD V3, SDK V3, feature flag, canary 1% |
| `{{T_CANARY_V3_25}}` | Migrate | Arsip | Active | 25% | Metrik parity, `can-i-deploy`, error budget |
| `{{T_DEPRECATE_V2}}` | Deprecate V2 | Arsip | Deprecated | Current | `Deprecation` V2, migration v2→v3, notifikasi konsumen |
| `{{T_SUNSET_V2_NOTICE}}` | Sunset notice | Arsip | Deprecated + `Sunset` | Current | `{{NOTICE_PERIOD}}` sebelum pemadaman; T−90/T−30/T−7 reminder |
| `{{T_SWITCH_V3}}` | Switch | Arsip | Security-only | Default | Dual-write masih ON untuk rollback; SLO hijau `{{JENDELA_OBSERVASI}}` |
| `{{T_SUNSET_V2}}` | Sunset V2 | Arsip | `410 Gone` | Current | Nol consumer V2, kontrak/webhook sudah dialihkan |
| `{{T_CONTRACT_DB}}` | Contract | Arsip | Arsip | Current | Hapus kolom/flag/adapter lama pada rilis terpisah; CHANGELOG `Removed` |

---

### Inferences

- Path versioning dipilih karena constraint brief—V1/V2/V3 eksplisit dan hidup bersamaan—bukan karena HTTP atau REST mewajibkannya.
- Zero downtime mensyaratkan kompatibilitas image lama/baru sekaligus pada database dan kontrak; rolling/canary saja tidak cukup.
- Karena setiap versi tambahan menaikkan biaya kognitif dan operasional, major baru hanya boleh muncul setelah opsi additive dan deprecation gagal.
- Header lifecycle memberi sinyal machine-readable, tetapi keputusan mematikan versi tetap memerlukan komunikasi dan metrik konsumen.

### Gaps

- Tidak ditemukan standar IETF/ISO yang menetapkan kebijakan N-1/N-2, lama notice period, persentase canary, atau ambang metrik sunset; semua angka sengaja berupa placeholder.
- Panduan industri bertentangan: Zalando mewajibkan media-type versioning, Microsoft menjabarkan URI versioning, dan Apigee menolak versi di `Accept`/`Content-Type`.
- Stripe menganggap penambahan event type/response property kompatibel dengan tolerant reader, sementara Zalando melarang perluasan enum output; pilihan harus didokumentasikan per API.
- Halaman wiki ASP.NET API versioning tidak dapat diverifikasi karena tampilan login GitHub; tanggal rilis OAS 3.2.1 juga tidak diverifikasi, hanya keberadaan versi patch-nya.

## Pertanyaan kunci 3 — Checklist review, anti-pattern, cutover/rollback, dan verifikasi sumber

### Takeaway

Review yang dapat dieksekusi harus menggabungkan compatibility gate CI, contract verification, pengecekan header lifecycle, metrik per `api_version`, dan runbook rollback; anti-pattern paling merusak adalah menghapus/mengubah kontrak langsung, `/v2` yang sekadar alias, sunset tanpa tanggal, serta tidak adanya metrik pemakaian per versi. `[REKOMENDASI PENELITI]` — [VENDOR/RESMI] [Pact Docs, “Can I Deploy”](https://docs.pact.io/pact_broker/can_i_deploy), [STANDAR] [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html), [STANDAR] [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html), [VENDOR/RESMI] [Kubernetes Docs, “Deployments”](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

### Cited Findings

- Branch protection dapat mewajibkan PR review, CODEOWNERS review, status checks, linear history, merge queue, signed commits, dan deploy sukses sebelum merge. — [VENDOR/RESMI] [GitHub Docs, “About protected branches”](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- `can-i-deploy` sebelum deploy dan `record-deployment` sesudah deploy membuat Pact Broker mengetahui versi di tiap environment; CI/CD guide menempatkan keduanya pada level Platinum/Diamond. — [VENDOR/RESMI] [Pact Docs, “Can I Deploy”](https://docs.pact.io/pact_broker/can_i_deploy); [VENDOR/RESMI] [Pact Docs, “CI/CD Setup Guide”](https://docs.pact.io/pact_nirvana)
- `Deprecation` dan `Sunset` hanyalah hint; klien sebaiknya tetap berfungsi tanpa keduanya, sehingga komunikasi dan metrik tidak dapat digantikan header saja. — [STANDAR] [RFC 9745 §5/§7](https://www.rfc-editor.org/rfc/rfc9745.html); [STANDAR] [RFC 8594 §3/§8](https://www.rfc-editor.org/rfc/rfc8594.html)
- Kubernetes menyediakan `kubectl rollout undo`, kondisi `ProgressDeadlineExceeded`, dan default `maxUnavailable`/`maxSurge` 25%; AWS canary dapat dipromosikan atau dibatalkan berdasarkan metrik terpisah. — [VENDOR/RESMI] [Kubernetes Docs](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/); [VENDOR/RESMI] [AWS API Gateway canary](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md)
- Fowler menyarankan rollback canary dengan reroute ke versi lama, memantau versi klien yang masih aktif, dan menunggu angka pemakaian turun sebelum contract. — [INDUSTRI] [Martin Fowler, “Canary Release”](https://martinfowler.com/bliki/CanaryRelease.html)
- Keep a Changelog mewajibkan deprecation, removal, dan breaking change tampak jelas; SemVer menempatkan removal inkompatibel pada MAJOR. — [INDUSTRI] [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/); [INDUSTRI] [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html)
- Zalando memperingatkan banyaknya versi hidup bersamaan menyulitkan pemahaman, pengujian, pemeliharaan, evolusi, operasi, dan rilis; Google menyarankan mencari perubahan backward-compatible sebelum versioning. — [INDUSTRI] [Zalando rule 113](https://opensource.zalando.com/restful-api-guidelines/); [INDUSTRI] [Google Cloud Blog](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you)
- Microsoft merekomendasikan propagation correlation/trace headers untuk end-to-end visibility, dan memperingatkan caching lintas versi ketika header menentukan representasi. — [VENDOR/RESMI] [Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design); [STANDAR] [RFC 9111 §4.1](https://www.rfc-editor.org/rfc/rfc9111.html)
- GitHub README sebaiknya hanya berisi informasi getting-started; duplikasi isi artefak ke README/research notes menciptakan banyak source-of-truth yang drift. — [VENDOR/RESMI] [GitHub Docs, About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes); [INDUSTRI] [Write the Docs, Docs as code](https://www.writethedocs.org/guide/docs-as-code/)
- Monorepo tanpa project graph/cache/module boundaries membuat CI menjalankan semua tes dan kode internal mudah menjadi dependensi lintas tim. — [VENDOR/RESMI] [Nx, What is a Monorepo?](https://nx.dev/docs/concepts/decisions/why-monorepos); [VENDOR/RESMI] [Turborepo](https://turbo.build/repo/docs/core-concepts/monorepos)
- Config rahasia tidak boleh menjadi konstanta atau file config yang mudah ter-commit; `.gitignore` adalah tempat pola file generated yang ingin dibagikan lewat clone. — [INDUSTRI] [12-Factor Config](https://12factor.net/config); [VENDOR/RESMI] [git-scm, gitignore](https://git-scm.com/docs/gitignore)

**Checklist, anti-pattern, kriteria cutover/rollback, konflik sumber, gaps, dan daftar sumber berikut merupakan perluasan dari temuan di atas.**

#### Checklist review

##### 1. Review struktur dokumen & repositori

- [ ] README root berisi ringkasan + peta tautan, bukan salinan BRD/FSD/desain/test/laporan. `[VENDOR/RESMI]` [GitHub Docs, About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [ ] Satu canonical path per artefak; `templates/` berisi placeholder, `research_notes/` berstatus non-normatif. `[INDUSTRI]` [Write the Docs, Docs as code](https://www.writethedocs.org/guide/docs-as-code/); [MADR](https://adr.github.io/madr/)
- [ ] ADR lama immutable; `superseded by`, bukan edit diam-diam. `[INDUSTRI]` [MADR 4.0.0](https://adr.github.io/madr/)
- [ ] CHANGELOG memiliki `Unreleased`, kategori, tanggal ISO, deprecation/removal/breaking. `[INDUSTRI]` [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/)
- [ ] `openapi` ≠ `info.version` ≠ `/api/vN` ≠ versi SDK. `[STANDAR]` [OAS 3.2.0](https://spec.openapis.org/oas/v3.2.0.html)
- [ ] OpenAPI disimpan di source control, self-contained atau memakai referensi durable/immutable. `[INDUSTRI]` [Zalando rules 101/234](https://opensource.zalando.com/restful-api-guidelines/)
- [ ] Root memiliki README, LICENSE, CONTRIBUTING, `.editorconfig`, `.gitignore`, Makefile/Justfile, CI config yang sesuai stack. `[VENDOR/RESMI]` [GitHub README](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes), [EditorConfig](https://editorconfig.org/), [git-scm gitignore](https://git-scm.com/docs/gitignore), [GitHub Actions](https://docs.github.com/en/actions)
- [ ] CODEOWNERS mencakup kontrak, adapter tiap versi, gateway, lifecycle policy, CI; file CODEOWNERS sendiri memiliki owner. `[VENDOR/RESMI]` [GitHub, About code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [ ] Branch protection mewajibkan review owner, status checks, linear history/merge queue sesuai kebutuhan, tanpa bypass admin yang tidak disengaja. `[VENDOR/RESMI]` [GitHub, About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [ ] Config rahasia tidak di-commit; nama env var terdokumentasi. `[INDUSTRI]` [12-Factor Config](https://12factor.net/config)
- [ ] Dependensi source code mengarah ke dalam; adapter V1/V2/V3 tidak membocorkan HTTP/DB ke domain. `[INDUSTRI]` [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html); [Hexagonal](https://alistair.cockburn.us/hexagonal-architecture/)
- [ ] Monorepo/polyrepo dipilih dengan alasan tertulis, dan tooling graph/cache/affected tersedia bila monorepo. `[VENDOR/RESMI]` [Nx Monorepo vs Polyrepo](https://nx.dev/docs/concepts/decisions/monorepo-vs-polyrepo); [Turborepo](https://turbo.build/repo/docs/core-concepts/monorepos)

##### 2. Review API versioning & zero downtime

- [ ] Keputusan path `/api/vN` terdokumentasi dalam ADR bersama pengorbanan HATEOAS dan perbedaan pendapat Zalando/Apigee. `[VENDOR/RESMI]` [Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design); `[INDUSTRI]` [Zalando rule 114](https://opensource.zalando.com/restful-api-guidelines/), [Google Cloud Blog](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you)
- [ ] Perubahan kompatibel tidak menciptakan major baru; breaking change memicu major + `BREAKING CHANGE` commit. `[INDUSTRI]` [SemVer](https://semver.org/spec/v2.0.0.html); [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/); [Zalando rules 106–113](https://opensource.zalando.com/restful-api-guidelines/)
- [ ] Matriks additive/optional/required/enum/type/error/pagination/removal/rename telah dijalankan sebagai CI diff. `[INDUSTRI]` [AIP-180](https://google.aip.dev/180); [Zalando rule 107](https://opensource.zalando.com/restful-api-guidelines/); `[STANDAR]` [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html)
- [ ] Urutan expand → backfill → dual-write → dual-read → switch → contract memiliki exit gate dan runbook rollback. `[INDUSTRI]` [Fowler, Parallel Change](https://martinfowler.com/bliki/ParallelChange.html)
- [ ] Canary/rolling/blue-green memiliki rasio, metrik terpisah, dan rollback otomatis. `[VENDOR/RESMI]` [AWS API Gateway canary](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md); [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [ ] `Deprecation` memakai `@<unix-date>`; `Sunset` memakai HTTP-date; `Sunset >= Deprecation`; `rel="deprecation"`/`rel="sunset"` menunjuk dokumen nyata. `[STANDAR]` [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html); [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html)
- [ ] Kebijakan N-1/N-2, notice period, dan sunset date eksplisit; tidak ada versi tanpa batas waktu. `[REKOMENDASI PENELITI]` dasar [RFC 8594 §1.4](https://www.rfc-editor.org/rfc/rfc8594.html) dan [SemVer FAQ](https://semver.org/spec/v2.0.0.html)
- [ ] `deprecated: true` pada OpenAPI, deprecation warning SDK, migration guide, dan pengumuman konsumen tersedia. `[STANDAR]` [OAS 3.1.0](https://spec.openapis.org/oas/v3.1.0.html#operation-object); `[VENDOR/RESMI]` [Stripe](https://docs.stripe.com/api-versions)
- [ ] Satu OAD dan satu SDK per major; `can-i-deploy` + `record-deployment` ada di pipeline. `[STANDAR]` [OAS 3.2.0 §2](https://spec.openapis.org/oas/v3.2.0.html); `[VENDOR/RESMI]` [Pact Docs](https://docs.pact.io/pact_broker/can_i_deploy)
- [ ] Metrik request/unique consumer/error/latency/webhook pin/parity dikunci per `api_version`; kriteria contract berbasis metrik. `[VENDOR/RESMI]` [AWS canary](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md); `[INDUSTRI]` [Fowler, Canary Release](https://martinfowler.com/bliki/CanaryRelease.html)
- [ ] Header-based negotiation (jika ada) disertai `Vary`; path-based tidak mencampur cache antar versi. `[STANDAR]` [RFC 9111 §4.1](https://www.rfc-editor.org/rfc/rfc9111.html)
- [ ] Checklist cutover dan kriteria rollback pada template Checklist release ditandatangani sebelum produksi. `[REKOMENDASI PENELITI]`

---

#### Anti-pattern yang sering terjadi

| Anti-pattern | Mengapa berbahaya | Sumber / dasar |
|---|---|---|
| Menghapus atau rename field langsung pada V1/V2 yang masih hidup | Klien lama berhenti bekerja; rename setara remove+add | `[INDUSTRI]` [AIP-180](https://google.aip.dev/180); [Zalando rule 107](https://opensource.zalando.com/restful-api-guidelines/); `[VENDOR/RESMI]` [Stripe](https://docs.stripe.com/api-versions) |
| `/v2` yang hanya alias ke `/v1` tanpa kontrak, adapter, dan migration guide berbeda | Menimbulkan ilusi versi; metrik dan deprecation tidak bermakna; kontrak tidak benar-benar berubah | `[REKOMENDASI PENELITI]` dasar [OAS 3.2.0](https://spec.openapis.org/oas/v3.2.0.html) dan [Zalando API First](https://opensource.zalando.com/restful-api-guidelines/) |
| Versi tanpa batas waktu / “deprecated, dipadamkan nanti” | Tidak ada kepastian migrasi; RFC 8594 justru dirancang untuk waktu sunset yang diketahui | `[STANDAR]` [RFC 8594 §1.4, §3](https://www.rfc-editor.org/rfc/rfc8594.html) |
| Tidak ada metrik pemakaian per versi | Contract/sunset diputus berdasarkan dugaan; klien mobile/webhook lama bisa masih aktif | `[INDUSTRI]` [Fowler, Canary Release](https://martinfowler.com/bliki/CanaryRelease.html); `[VENDOR/RESMI]` [Stripe](https://docs.stripe.com/api-versions), [Pact `--all prod`](https://docs.pact.io/pact_broker/can_i_deploy) |
| Tertukar `Deprecation` (RFC 9745) dan `Sunset` (RFC 8594), atau `Sunset` lebih awal dari `Deprecation` | Header salah syntax/semantik dan melanggar urutan normatif | `[STANDAR]` [RFC 9745 §2/§4](https://www.rfc-editor.org/rfc/rfc9745.html); [RFC 8594 §3](https://www.rfc-editor.org/rfc/rfc8594.html) |
| Menganggap path versioning sebagai “standar REST” | Ia trade-off industri; RFC 9110 memisahkan resource dan representasi, Zalando justru melarang URL versioning | `[STANDAR]` [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html); `[INDUSTRI]` [Zalando rule 114](https://opensource.zalando.com/restful-api-guidelines/) |
| Menambah enum value pada response diam-diam | Klien enum tertutup gagal parse; perlu major atau tolerant reader | `[INDUSTRI]` [Zalando rule 107/108](https://opensource.zalando.com/restful-api-guidelines/); `[INDUSTRI]` [AIP-180](https://google.aip.dev/180) |
| Menambahkan required field/validasi lebih ketat pada minor | Request lama yang sebelumnya valid menjadi 4xx | `[INDUSTRI]` [AIP-180](https://google.aip.dev/180); [Zalando rule 107](https://opensource.zalando.com/restful-api-guidelines/) |
| Mengubah error format atau pagination tanpa major | Klien mengandalkan bentuk error/page; perubahan semantik dapat merusak | `[STANDAR]` [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html); `[INDUSTRI]` [Zalando rules 159–161](https://opensource.zalando.com/restful-api-guidelines/), [AIP-180](https://google.aip.dev/180) |
| Deploy V3 dan langsung drop kolom lama | Aplikasi image lama selama rolling/canary masih menulis kolom itu | `[INDUSTRI]` [Fowler, Parallel Change](https://martinfowler.com/bliki/ParallelChange.html); `[VENDOR/RESMI]` [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) |
| Header/media-type versioning tanpa `Vary` | Cache dapat menyajikan representasi versi salah | `[STANDAR]` [RFC 9111 §4.1](https://www.rfc-editor.org/rfc/rfc9111.html); `[VENDOR/RESMI]` [Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design) |
| Satu `openapi.yaml` “latest” yang ditimpa untuk V1/V2/V3 | Kontrak lama hilang, SDK lama tidak dapat direproduksi | `[STANDAR]` [OAS 3.2.0 §4.1–4.2](https://spec.openapis.org/oas/v3.2.0.html); `[INDUSTRI]` [Zalando rules 101/234](https://opensource.zalando.com/restful-api-guidelines/) |
| Menyalin isi BRD/FSD/desain/test/laporan ke README, ADR, dan research_notes | Banyak source-of-truth yang drift; melanggar batas scope peneliti lain | `[INDUSTRI]` [Write the Docs, Docs as code](https://www.writethedocs.org/guide/docs-as-code/); `[VENDOR/RESMI]` [GitHub README](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) |
| Git log mentah dijadikan CHANGELOG; ADR lama ditimpa; release tanpa tag | Konsumen tidak melihat dampak; keputusan kehilangan jejak; rilis tidak reproducible | `[INDUSTRI]` [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); [MADR](https://adr.github.io/madr/); [SemVer FAQ](https://semver.org/spec/v2.0.0.html) |
| Monorepo tanpa project graph/cache/module boundaries | CI menjalankan semua tes; kode internal menjadi dependensi lintas tim | `[VENDOR/RESMI]` [Nx, What is a Monorepo?](https://nx.dev/docs/concepts/decisions/why-monorepos); [Turborepo](https://turbo.build/repo/docs/core-concepts/monorepos) |
| Secret/env production masuk `config/`, atau config per-deploy di-hardcode | Kredensial bocor dan perubahan environment memaksa perubahan kode | `[INDUSTRI]` [12-Factor Config](https://12factor.net/config); `[VENDOR/RESMI]` [git-scm gitignore](https://git-scm.com/docs/gitignore) |
| Branch panjang GitFlow untuk layanan continuous-delivery | Integrasi tertunda; penulis model itself menyarankan workflow lebih sederhana untuk web apps | `[INDUSTRI]` [Trunk-Based Development](https://trunkbaseddevelopment.com/5-min-overview/); [nvie reflection 2020](https://nvie.com/posts/a-successful-git-branching-model/) |

---

#### Checklist cutover & kriteria rollback (ringkasan operasional)

**Checklist cutover** `[REKOMENDASI PENELITI]` lihat template lengkap Checklist release; dasar [Pact can-i-deploy](https://docs.pact.io/pact_broker/can_i_deploy), [AWS canary](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md), [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html), [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html):

1. Kontrak V3, SDK V3, migration guide, dan navigation hub final.
2. Compatibility gate + Pact matrix + `can-i-deploy` hijau.
3. Expand/backfill/dual-write parity dan kill-switch diuji.
4. Canary dengan log/metrik terpisah; SLO dan business KPI hijau.
5. Header lifecycle benar; komunikasi konsumen dan daftar exception lengkap.
6. Promote V3; `record-deployment`; tag rilis; dashboard per versi aktif.
7. Dual-write lama **tetap ON** sampai jendela rollback berakhir; contract dijadwalkan terpisah.

**Kriteria rollback** `[REKOMENDASI PENELITI]`; ambang wajib diisi sebelum cutover:

| Pemicu | Tindakan | Dasar |
|---|---|---|
| 5xx / p95 / business KPI melewati `{{AMBANG}}` | Reroute canary ke stable; matikan `{{FLAG_V3}}`; pertahankan dual-write | `[INDUSTRI]` [Fowler, Canary Release](https://martinfowler.com/bliki/CanaryRelease.html); `[VENDOR/RESMI]` [AWS canary](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md) |
| Rollout `ProgressDeadlineExceeded`, readiness/image failure | `kubectl rollout undo` ke revisi stabil | `[VENDOR/RESMI]` [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) |
| `dual_write_mismatch_total` melebihi ambang | Hentikan switch, jalankan reconciliation, jangan contract | `[INDUSTRI]` [Fowler, Parallel Change](https://martinfowler.com/bliki/ParallelChange.html) |
| Verifikasi kontrak gagal setelah deploy | Blokir promosi berikutnya; rollback konsumen/provider sesuai matrix | `[VENDOR/RESMI]` [Pact, Can I Deploy](https://docs.pact.io/pact_broker/can_i_deploy) |
| Konsumen prioritas tinggi masih aktif pada versi sunset | Tunda pemadaman, perpanjang notice, perbarui `Sunset` | `[STANDAR]` [RFC 8594 §8](https://www.rfc-editor.org/rfc/rfc8594.html); `[VENDOR/RESMI]` [Stripe](https://docs.stripe.com/api-versions) |
| Cache menyajikan representasi versi salah | Matikan caching lintas versi, perbaiki `Vary`/cache key | `[STANDAR]` [RFC 9111 §4.1](https://www.rfc-editor.org/rfc/rfc9111.html) |

---

#### Catatan konflik dan keterbatasan


- Karena tidak ada RFC yang mewajibkan satu metode versioning, keputusan `/api/vN` harus dibaca sebagai **keputusan rekayasa organisasi** yang dioptimalkan untuk visibilitas, routing, cache, SDK, dan observability—bukan konformitas REST. Dasar: [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html), [Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design), [Zalando](https://opensource.zalando.com/restful-api-guidelines/), [Google Cloud Blog](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you).
- Zero downtime bukan sekadar deployment: rolling/canary hanya aman bila **database dan kontrak** kompatibel dengan image lama maupun baru; karena itu Expand–Contract, feature flag, dan consumer contracts harus menjadi satu urutan yang sama. Dasar: [Fowler Parallel Change](https://martinfowler.com/bliki/ParallelChange.html), [Kubernetes](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), [AWS](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md), [Pact](https://docs.pact.io/pact_broker/can_i_deploy).
- Banyaknya versi hidup bersamaan menaikkan biaya pemahaman, pengujian, pemeliharaan, dan rilis; oleh karena itu N-1/N-2 serta tanggal sunset harus eksplisit dan major baru hanya untuk perubahan yang benar-benar tidak dapat dilakukan secara additif. Dasar: [Zalando rule 113](https://opensource.zalando.com/restful-api-guidelines/), [Fowler Canary Release](https://martinfowler.com/bliki/CanaryRelease.html), [Google Cloud Blog](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you).

#### Konflik sumber yang tidak disembunyikan

- **Zalando vs Microsoft/Apigee:** Zalando `MUST use media type versioning` dan `MUST not use URL versioning`; Microsoft menjabarkan URI versioning sebagai opsi sederhana/eksplisit; Apigee menyarankan URL untuk entity versioning tetapi menolak versi di `Accept`/`Content-Type` dan menyarankan `Accept-Version` untuk format. Ketiganya `[VENDOR/RESMI]`/`[INDUSTRI]`, bukan standar IETF. ([Zalando](https://opensource.zalando.com/restful-api-guidelines/); [Microsoft](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design); [Google Cloud Blog](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you))
- **Perluasan enum response:** Stripe menganggap penambahan event type/response property kompatibel dengan syarat klien mengabaikan yang asing; Zalando melarang perluasan enum output karena klien mungkin tidak siap; AIP-180 membolehkan dengan kehati-hatian. Implementasi harus mendokumentasikan pilihan tolerant-reader atau major baru. ([Stripe](https://docs.stripe.com/api-versions); [Zalando rule 107/108](https://opensource.zalando.com/restful-api-guidelines/); [AIP-180](https://google.aip.dev/180))


- Tidak ditemukan standar IETF/ISO yang menetapkan angka universal untuk **N-1/N-2**, lama notice period, persentase canary, atau ambang metrik sunset. Semua nilai dalam catatan ini sengaja berupa placeholder keputusan organisasi.
- Dokumentasi PayPal API Design Guidelines tidak berhasil diverifikasi langsung pada URL repositori yang dicoba (HTTP 404); karena itu tidak dijadikan dasar klaim normatif. Sumber primer yang digunakan sudah mencakup RFC, OAS, Stripe, Microsoft, Google, AWS, Kubernetes, Zalando, Pact, Nx, Turborepo, GitHub, Git, EditorConfig, 12-Factor, SemVer, Keep a Changelog, Conventional Commits, MADR, Clean/Hexagonal, dan Fowler.
- Halaman wiki ASP.NET API versioning yang dicoba tidak menampilkan konten karena halaman login GitHub; oleh karena itu catatan tidak mengklaim detail implementasi library tersebut. Pedoman Microsoft Learn yang dapat diakses dipakai sebagai gantinya.
- Versi OAS yang tercantum pada halaman resmi 3.2.0/3.2.1 mencakup 3.2.1; catatan tidak menyebut tanggal rilis 3.2.1 karena tidak diverifikasi dari halaman tersebut, hanya keberadaan dan status patch-nya. ([OAS 3.2.1](https://spec.openapis.org/oas/v3.2.1.html))

---

#### Daftar sumber primer/resmi dan praktik industri

##### Standar resmi `[STANDAR]`
1. ISO/IEC/IEEE 29148:2018, *Systems and software engineering — Life cycle processes — Requirements engineering* — https://www.iso.org/standard/72089.html
2. RFC 8594, *The Sunset HTTP Header Field* (2019) — https://www.rfc-editor.org/rfc/rfc8594.html
3. RFC 9110, *HTTP Semantics*, STD 97 (2022) — https://www.rfc-editor.org/rfc/rfc9110.html
4. RFC 9111, *HTTP Caching*, STD 98 (2022) — https://www.rfc-editor.org/rfc/rfc9111.html
5. RFC 9457, *Problem Details for HTTP APIs* (2023, menggantikan RFC 7807) — https://www.rfc-editor.org/rfc/rfc9457.html
6. RFC 9745, *The Deprecation HTTP Response Header Field* (Maret 2025) — https://www.rfc-editor.org/rfc/rfc9745.html
7. OpenAPI Specification 3.1.0 — https://spec.openapis.org/oas/v3.1.0.html
8. OpenAPI Specification 3.2.0 — https://spec.openapis.org/oas/v3.2.0.html
9. OpenAPI Specification 3.2.1 — https://spec.openapis.org/oas/v3.2.1.html

##### Dokumentasi resmi vendor/proyek `[VENDOR/RESMI]`
10. Stripe Docs, *How API versioning works* — https://docs.stripe.com/api-versions
11. Microsoft Learn, *Best practices for RESTful web API design* — https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design
12. AWS API Gateway, *Set up a canary release deployment* — https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md
13. Kubernetes Docs, *Deployments* — https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
14. GitHub Docs, *About the repository README file* — https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
15. GitHub Docs, *About code owners* — https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
16. GitHub Docs, *About protected branches* — https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
17. GitHub Actions documentation — https://docs.github.com/en/actions
18. Pact Docs, *CI/CD Setup Guide* — https://docs.pact.io/pact_nirvana
19. Pact Docs, *Can I Deploy* — https://docs.pact.io/pact_broker/can_i_deploy
20. Nx, *What is a Monorepo?* — https://nx.dev/docs/concepts/decisions/why-monorepos
21. Nx, *Monorepo vs Polyrepo* — https://nx.dev/docs/concepts/decisions/monorepo-vs-polyrepo
22. Turborepo, *What is Turborepo? / Introduction* — https://turbo.build/repo/docs/core-concepts/monorepos
23. Git, *gitignore* — https://git-scm.com/docs/gitignore
24. EditorConfig — https://editorconfig.org/

##### Spesifikasi/konvensi komunitas, guideline perusahaan, dan opini industri `[INDUSTRI]`
25. Semantic Versioning 2.0.0 — https://semver.org/spec/v2.0.0.html
26. Keep a Changelog 1.1.0 — https://keepachangelog.com/en/1.1.0/
27. Conventional Commits 1.0.0 — https://www.conventionalcommits.org/en/v1.0.0/
28. Trunk-Based Development, *Five-minute overview* — https://trunkbaseddevelopment.com/5-min-overview/
29. Write the Docs, *Docs as code* — https://www.writethedocs.org/guide/docs-as-code/
30. MADR 4.0.0, *Markdown Architectural Decision Records* — https://adr.github.io/madr/
31. Zalando RESTful API and Event Guidelines — https://opensource.zalando.com/restful-api-guidelines/
32. Google Cloud Blog / Apigee, *API design: Which version of versioning is right for you?* — https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you
33. Google API Improvement Proposals, AIP-180 *Backwards compatibility* — https://google.aip.dev/180
34. Martin Fowler, *Parallel Change* — https://martinfowler.com/bliki/ParallelChange.html
35. Martin Fowler, *Canary Release* — https://martinfowler.com/bliki/CanaryRelease.html
36. Robert C. Martin, *The Clean Architecture* — https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html
37. Alistair Cockburn, *Hexagonal architecture (Ports and Adapters)* — https://alistair.cockburn.us/hexagonal-architecture/
38. The Twelve-Factor App, *Config* — https://12factor.net/config
39. Vincent Driessen, *A successful Git branching model* + catatan refleksi 2020 — https://nvie.com/posts/a-successful-git-branching-model/
### Inferences

- Checklist review sebaiknya berupa gate CI yang gagal bila kontrak, header lifecycle, Pact matrix, atau metrik per versi tidak lengkap.
- Rollback aman mensyaratkan dual-write lama tetap aktif sampai parity dan SLO stabil; contract database harus menjadi rilis terpisah.
- Anti-pattern mengelompok menjadi lima kategori: kontrak, lifecycle, deployment, dokumentasi/repositori, dan konfigurasi.

### Gaps

- Tidak ada standar yang memberi ambang rollback, jendela observasi, atau lama retensi versi sunset; nilai harus disetujui owner dan dicantumkan di release checklist.
- Daftar file root, matriks RACI, RTM, dan Definition of Done adalah sintesis tata kelola, bukan format normatif dari satu standar.
- Sumber sekunder/blog hanya dipakai sebagai pelengkap opini industri dan selalu ditandai `[INDUSTRI]`; tidak ada klaim normatif yang hanya bersandar pada blog sekunder.

