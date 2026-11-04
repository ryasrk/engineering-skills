## 8. Checklist, koreksi standar, keterbatasan, dan daftar sumber API versioning

> Template terkait: `templates/06-Checklist-Zero-Downtime.md`, `templates/06-Checklist-Release.md`, `templates/06-Header-Lifecycle-Deprecation-Sunset.md`.

Ketiga berkas tersebut adalah artefak mandiri; bagian ini hanya menyebut keberadaannya dan tidak menyalin isinya. Bagian kunci yang perlu dibuka pada masing-masing template sesuai rujukan catatan: exit gate dan runbook rollback untuk urutan Expand–Contract (`templates/06-Checklist-Zero-Downtime.md`), checklist cutover beserta ambang rollback yang ditandatangani sebelum produksi (`templates/06-Checklist-Release.md`), serta syntax dan urutan `Deprecation`–`Sunset`, `rel`, dan notice period (`templates/06-Header-Lifecycle-Deprecation-Sunset.md`). `[Rekomendasi peneliti/tim]` — [Pact Docs, "Can I Deploy"](https://docs.pact.io/pact_broker/can_i_deploy), [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html), [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html), [Kubernetes Docs, "Deployments"](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

### 8.1 Konvensi penanda sitasi

Seluruh sitasi mempertahankan nama dokumen dan URL persis sebagaimana tercantum pada catatan sumber (baris 1099–1281 dari `06-skema-dan-versioning-api.md`). Penanda asli catatan dipetakan secara transparan ke tiga penanda laporan:

| Penanda pada catatan | Penanda pada bagian ini | Makna |
|---|---|---|
| `[STANDAR]` | `[Standar resmi]` | RFC, ISO/IEC/IEEE, dan OpenAPI Specification; bersifat normatif. |
| `[VENDOR/RESMI]` | `[Praktik industri]` (sub-label: dokumentasi resmi vendor/proyek) | Dokumentasi primer, tetapi bukan standar IETF/ISO; catatan menegaskan status ini secara eksplisit. |
| `[INDUSTRI]` | `[Praktik industri]` | Konvensi komunitas, guideline perusahaan, dan opini industri; tidak menjadi satu-satunya dasar klaim normatif. |
| `[REKOMENDASI PENELITI]` | `[Rekomendasi peneliti/tim]` | Sintesis tim peneliti, bukan klaim normatif dari standar. |

Pemetaan ini tidak mengubah bunyi sitasi. `[VENDOR/RESMI]` dan `[INDUSTRI]` disatukan di bawah `[Praktik industri]` karena catatan menyatakan keduanya "bukan standar IETF" ([Zalando](https://opensource.zalando.com/restful-api-guidelines/), [Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design), [Google Cloud Blog](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you)) serta menegaskan bahwa sumber sekunder/blog hanya dipakai sebagai pelengkap opini industri. `[Standar resmi]` dipakai eksklusif untuk RFC, ISO/IEC/IEEE, dan OAS.

### 8.2 Ringkasan best practices

Review yang dapat dieksekusi harus menggabungkan compatibility gate CI, contract verification, pengecekan header lifecycle, metrik per `api_version`, dan runbook rollback; anti-pattern paling merusak adalah menghapus/mengubah kontrak langsung, `/v2` yang sekadar alias, sunset tanpa tanggal, serta tidak adanya metrik pemakaian per versi. `[Rekomendasi peneliti/tim]` — [Pact Docs, "Can I Deploy"](https://docs.pact.io/pact_broker/can_i_deploy), [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html), [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html), [Kubernetes Docs, "Deployments"](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

- **Jadikan review sebagai gate CI, bukan dokumen pasif.** Checklist review sebaiknya berupa gate CI yang gagal bila kontrak, header lifecycle, Pact matrix, atau metrik per versi tidak lengkap. `[Rekomendasi peneliti/tim]`
- **Pisahkan empat pengertian "versi".** `openapi` ≠ `info.version` ≠ `/api/vN` ≠ versi SDK; satu OpenAPI document dan satu SDK per major. `[Standar resmi]` — [OAS 3.2.0](https://spec.openapis.org/oas/v3.2.0.html)
- **Utamakan perubahan backward-compatible.** Cari perubahan additif sebelum memutuskan versioning; removal inkompatibel menempati MAJOR dan breaking change harus tampak jelas di CHANGELOG. `[Praktik industri]` — [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html), [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), [Google Cloud Blog](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you)
- **Perlakukan header lifecycle sebagai hint.** `Deprecation` dan `Sunset` hanyalah hint; klien sebaiknya tetap berfungsi tanpa keduanya, sehingga komunikasi dan metrik tidak dapat digantikan header saja. `[Standar resmi]` — [RFC 9745 §5/§7](https://www.rfc-editor.org/rfc/rfc9745.html), [RFC 8594 §3/§8](https://www.rfc-editor.org/rfc/rfc8594.html)
- **Ikat deploy ke verifikasi kontrak.** `can-i-deploy` sebelum deploy dan `record-deployment` sesudah deploy membuat Pact Broker mengetahui versi di tiap environment; CI/CD guide menempatkan keduanya pada level Platinum/Diamond. `[Praktik industri]` — [Pact Docs, "Can I Deploy"](https://docs.pact.io/pact_broker/can_i_deploy), [Pact Docs, "CI/CD Setup Guide"](https://docs.pact.io/pact_nirvana)
- **Kunci observability per `api_version`.** Request, unique consumer, error, latency, webhook pin, dan parity dikunci per versi; kriteria contract berbasis metrik, bukan dugaan. `[Praktik industri]` — [Martin Fowler, "Canary Release"](https://martinfowler.com/bliki/CanaryRelease.html), [Stripe Docs, "How API versioning works"](https://docs.stripe.com/api-versions)
- **Jaga kompatibilitas image lama dan baru.** Zero downtime bukan sekadar deployment: rolling/canary hanya aman bila database dan kontrak kompatibel dengan kedua image, sehingga Expand–Contract, feature flag, dan consumer contracts menjadi satu urutan yang sama. `[Praktik industri]` — [Martin Fowler, "Parallel Change"](https://martinfowler.com/bliki/ParallelChange.html), [Kubernetes Docs](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), [AWS API Gateway canary](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md)
- **Batasi versi yang hidup bersamaan.** Terlalu banyak versi menyulitkan pemahaman, pengujian, pemeliharaan, evolusi, operasi, dan rilis; N-1/N-2 serta tanggal sunset harus eksplisit. `[Rekomendasi peneliti/tim]`; `[Praktik industri]` — [Zalando rule 113](https://opensource.zalando.com/restful-api-guidelines/), [Google Cloud Blog](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you)

### 8.3 Tabel konvensi penting dan koreksi standar lintas riset

Tabel berikut merangkum koreksi penamaan/versi yang dapat dipertanggungjawabkan dari catatan sumber bagian ini. Baris yang tidak memiliki dasar pada baris 1099–1281 sengaja dibiarkan tanpa URL dan tanpa bunyi koreksi.

| Rujukan / versi | Koreksi atau konvensi yang berlaku | Penanda | Dasar (nama dokumen + URL) |
|---|---|---|---|
| RFC 8594 dan RFC 9745 | Dua header berbeda, jangan tertukar: `Deprecation` memakai `@<unix-date>` (RFC 9745), `Sunset` memakai HTTP-date (RFC 8594), dan `Sunset >= Deprecation`. RFC 9745 terbit Maret 2025; RFC 8594 terbit 2019. | `[Standar resmi]` | [RFC 9745, *The Deprecation HTTP Response Header Field*](https://www.rfc-editor.org/rfc/rfc9745.html); [RFC 8594, *The Sunset HTTP Header Field*](https://www.rfc-editor.org/rfc/rfc8594.html) |
| RFC 9457 | *Problem Details for HTTP APIs* (2023) menggantikan RFC 7807; perubahan format error termasuk perubahan semantik yang memicu major. | `[Standar resmi]` | [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html) |
| RFC 9110 / RFC 9111 | HTTP Semantics = STD 97 (2022); HTTP Caching = STD 98 (2022). RFC 9110 memisahkan resource dan representasi; RFC 9111 §4.1 mengatur `Vary` untuk caching lintas versi. | `[Standar resmi]` | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html); [RFC 9111](https://www.rfc-editor.org/rfc/rfc9111.html) |
| ISO/IEC/IEEE 29148:2018 | Rujukan requirements engineering yang tercantum adalah edisi 2018 dengan nomor standar 72089 pada katalog ISO. | `[Standar resmi]` | [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) |
| ISO 29119-3:2021 | Nama ini muncul pada permintaan penulisan, tetapi tidak tercantum pada catatan sumber bagian ini; koreksi dan URL tidak diverifikasi. | — | Tidak ada pada catatan bagian ini; URL sengaja tidak diisi. |
| WCAG 2.2 AA vs 2.3.3 AAA | Perbandingan tingkat kepatuhan ini tidak tercantum pada catatan sumber bagian ini; koreksi dan URL tidak diverifikasi. | — | Tidak ada pada catatan bagian ini; URL sengaja tidak diisi. |
| MADR 4.0.0 | Versi tepat yang disitir adalah 4.0.0. ADR lama bersifat immutable; pergantian keputusan memakai `superseded by`, bukan edit diam-diam. | `[Praktik industri]` | [MADR 4.0.0, *Markdown Architectural Decision Records*](https://adr.github.io/madr/) |
| OWASP ASVS 5.0.0 | Nomor versi ini tidak tercantum pada catatan sumber bagian ini; koreksi dan URL tidak diverifikasi. | — | Tidak ada pada catatan bagian ini; URL sengaja tidak diisi. |
| IEEE 830 (status *superseded*) | Status *superseded* disebut pada permintaan penulisan, tetapi tidak dapat diverifikasi dari catatan sumber bagian ini; bagian ini tidak menyatakannya sebagai fakta. Rujukan requirements engineering yang tersedia hanyalah ISO/IEC/IEEE 29148:2018. | — | Tidak ada pada catatan bagian ini; URL sengaja tidak diisi. |
| OAS 3.1.0 | `deprecated: true` berada pada Operation Object; OAS 3.1.0 adalah basis penanda deprecation pada spesifikasi. | `[Standar resmi]` | [OpenAPI Specification 3.1.0](https://spec.openapis.org/oas/v3.1.0.html); [OAS 3.1.0, Operation Object](https://spec.openapis.org/oas/v3.1.0.html#operation-object) |
| OAS 3.2.0 | Versi yang dijadikan dasar pemisahan `openapi`/`info.version`/path/SDK dan prinsip satu OAD per major (§2), serta kewajiban kontrak self-contained/referensi durable (§4.1–4.2). | `[Standar resmi]` | [OpenAPI Specification 3.2.0](https://spec.openapis.org/oas/v3.2.0.html) |
| OAS 3.2.1 | Halaman resmi mencantumkan 3.2.0/3.2.1; status patch 3.2.1 tercatat, tetapi tanggal rilisnya tidak diverifikasi dan karena itu tidak disebut. | `[Standar resmi]` | [OpenAPI Specification 3.2.1](https://spec.openapis.org/oas/v3.2.1.html) |
| SemVer 2.0.0, Keep a Changelog 1.1.0, Conventional Commits 1.0.0 | Ketiganya adalah konvensi komunitas berversi, bukan standar resmi; penulisan versinya harus tepat dan tidak disamakan dengan versi OAS. | `[Praktik industri]` | [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html); [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/); [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) |

Catatan disiplin: empat rujukan yang ditandai "—" di atas (ISO 29119-3:2021, WCAG 2.2 AA vs 2.3.3 AAA, OWASP ASVS 5.0.0, IEEE 830) tidak diberi URL maupun bunyi koreksi karena keduanya tidak ada pada rentang catatan yang diizinkan. Mengisinya akan menciptakan fakta atau URL baru, yang dilarang. Keempatnya dicatat di sini murni sebagai batas verifikasi, sejalan dengan prinsip catatan bahwa tidak ada klaim normatif yang hanya bersandar pada sumber yang tidak diverifikasi.

### 8.4 Checklist review versioning

Checklist berikut adalah ringkasan operasional yang dapat dijadikan gate CI. Setiap item mempertahankan dasar sitasinya; bagian cutover lengkap berada pada template, bukan disalin di sini.

#### 8.4.1 Kontrak, kompatibilitas, dan gate CI

- [ ] Keputusan path `/api/vN` terdokumentasi dalam ADR bersama pengorbanan HATEOAS dan perbedaan pendapat Zalando/Apigee. `[Praktik industri]` — [Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design); [Zalando rule 114](https://opensource.zalando.com/restful-api-guidelines/), [Google Cloud Blog](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you)
- [ ] Perubahan kompatibel tidak menciptakan major baru; breaking change memicu major + `BREAKING CHANGE` commit. `[Praktik industri]` — [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html), [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/), [Zalando rules 106–113](https://opensource.zalando.com/restful-api-guidelines/)
- [ ] Matriks additive/optional/required/enum/type/error/pagination/removal/rename dijalankan sebagai CI diff. `[Praktik industri]` — [AIP-180](https://google.aip.dev/180), [Zalando rule 107](https://opensource.zalando.com/restful-api-guidelines/); `[Standar resmi]` — [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html)
- [ ] Urutan expand → backfill → dual-write → dual-read → switch → contract memiliki exit gate dan runbook rollback. `[Praktik industri]` — [Martin Fowler, "Parallel Change"](https://martinfowler.com/bliki/ParallelChange.html)
- [ ] Canary/rolling/blue-green memiliki rasio, metrik terpisah, dan rollback otomatis. `[Praktik industri]` — [AWS API Gateway canary](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md), [Kubernetes Docs, "Deployments"](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [ ] `openapi` ≠ `info.version` ≠ `/api/vN` ≠ versi SDK. `[Standar resmi]` — [OAS 3.2.0](https://spec.openapis.org/oas/v3.2.0.html)
- [ ] OpenAPI disimpan di source control, self-contained atau memakai referensi durable/immutable. `[Praktik industri]` — [Zalando rules 101/234](https://opensource.zalando.com/restful-api-guidelines/)
- [ ] Satu OAD dan satu SDK per major; `can-i-deploy` + `record-deployment` ada di pipeline. `[Standar resmi]` — [OAS 3.2.0 §2](https://spec.openapis.org/oas/v3.2.0.html); `[Praktik industri]` — [Pact Docs, "Can I Deploy"](https://docs.pact.io/pact_broker/can_i_deploy), [Pact Docs, "CI/CD Setup Guide"](https://docs.pact.io/pact_nirvana)
- [ ] Branch protection mewajibkan review owner, status checks, linear history/merge queue sesuai kebutuhan, tanpa bypass admin yang tidak disengaja. `[Praktik industri]` — [GitHub Docs, "About protected branches"](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [ ] CODEOWNERS mencakup kontrak, adapter tiap versi, gateway, lifecycle policy, dan CI; file CODEOWNERS sendiri memiliki owner. `[Praktik industri]` — [GitHub Docs, "About code owners"](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [ ] Dependensi source code mengarah ke dalam; adapter V1/V2/V3 tidak membocorkan HTTP/DB ke domain. `[Praktik industri]` — [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html), [Hexagonal architecture](https://alistair.cockburn.us/hexagonal-architecture/)

#### 8.4.2 Lifecycle, observability, cache, dan tata kelola dokumen

- [ ] `Deprecation` memakai `@<unix-date>`; `Sunset` memakai HTTP-date; `Sunset >= Deprecation`; `rel="deprecation"`/`rel="sunset"` menunjuk dokumen nyata. `[Standar resmi]` — [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html), [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html)
- [ ] Kebijakan N-1/N-2, notice period, dan sunset date eksplisit; tidak ada versi tanpa batas waktu. `[Rekomendasi peneliti/tim]` — dasar [RFC 8594 §1.4](https://www.rfc-editor.org/rfc/rfc8594.html) dan [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html)
- [ ] `deprecated: true` pada OpenAPI, deprecation warning SDK, migration guide, dan pengumuman konsumen tersedia. `[Standar resmi]` — [OAS 3.1.0, Operation Object](https://spec.openapis.org/oas/v3.1.0.html#operation-object); `[Praktik industri]` — [Stripe Docs](https://docs.stripe.com/api-versions)
- [ ] Metrik request/unique consumer/error/latency/webhook pin/parity dikunci per `api_version`; kriteria contract berbasis metrik. `[Praktik industri]` — [AWS API Gateway canary](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md), [Martin Fowler, "Canary Release"](https://martinfowler.com/bliki/CanaryRelease.html)
- [ ] Correlation/trace headers dipropagasi untuk end-to-end visibility. `[Praktik industri]` — [Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design)
- [ ] Header-based negotiation (jika ada) disertai `Vary`; path-based tidak mencampur cache antar versi. `[Standar resmi]` — [RFC 9111 §4.1](https://www.rfc-editor.org/rfc/rfc9111.html)
- [ ] Checklist cutover dan kriteria rollback pada template Checklist release ditandatangani sebelum produksi. `[Rekomendasi peneliti/tim]`
- [ ] README root berisi ringkasan + peta tautan, bukan salinan BRD/FSD/desain/test/laporan. `[Praktik industri]` — [GitHub Docs, "About the repository README file"](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [ ] Satu canonical path per artefak; `templates/` berisi placeholder, `research_notes/` berstatus non-normatif; ADR lama immutable dengan `superseded by`. `[Praktik industri]` — [Write the Docs, "Docs as code"](https://www.writethedocs.org/guide/docs-as-code/), [MADR 4.0.0](https://adr.github.io/madr/)
- [ ] CHANGELOG memiliki `Unreleased`, kategori, tanggal ISO, serta deprecation/removal/breaking. `[Praktik industri]` — [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/)
- [ ] Root memiliki README, LICENSE, CONTRIBUTING, `.editorconfig`, `.gitignore`, Makefile/Justfile, dan CI config yang sesuai stack. `[Praktik industri]` — [GitHub Docs, README](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes), [EditorConfig](https://editorconfig.org/), [git-scm, "gitignore"](https://git-scm.com/docs/gitignore), [GitHub Actions documentation](https://docs.github.com/en/actions)
- [ ] Config rahasia tidak di-commit; nama env var terdokumentasi; pola file generated dibagikan lewat `.gitignore`. `[Praktik industri]` — [The Twelve-Factor App, "Config"](https://12factor.net/config), [git-scm, "gitignore"](https://git-scm.com/docs/gitignore)
- [ ] Monorepo/polyrepo dipilih dengan alasan tertulis, dan tooling graph/cache/affected tersedia bila monorepo. `[Praktik industri]` — [Nx, "Monorepo vs Polyrepo"](https://nx.dev/docs/concepts/decisions/monorepo-vs-polyrepo), [Turborepo](https://turbo.build/repo/docs/core-concepts/monorepos)

### 8.5 Anti-pattern

Anti-pattern mengelompok menjadi lima kategori: kontrak, lifecycle, deployment, dokumentasi/repositori, dan konfigurasi. `[Rekomendasi peneliti/tim]`

| Kategori | Anti-pattern | Mengapa berbahaya | Sumber / dasar |
|---|---|---|---|
| Kontrak | Menghapus atau rename field langsung pada V1/V2 yang masih hidup | Klien lama berhenti bekerja; rename setara remove+add | `[Praktik industri]` [AIP-180](https://google.aip.dev/180), [Zalando rule 107](https://opensource.zalando.com/restful-api-guidelines/), [Stripe Docs](https://docs.stripe.com/api-versions) |
| Kontrak | `/v2` yang hanya alias ke `/v1` tanpa kontrak, adapter, dan migration guide berbeda | Menimbulkan ilusi versi; metrik dan deprecation tidak bermakna; kontrak tidak benar-benar berubah | `[Rekomendasi peneliti/tim]` dasar [OAS 3.2.0](https://spec.openapis.org/oas/v3.2.0.html) dan [Zalando API First](https://opensource.zalando.com/restful-api-guidelines/) |
| Kontrak | Menambah enum value pada response diam-diam | Klien enum tertutup gagal parse; perlu major atau tolerant reader | `[Praktik industri]` [Zalando rule 107/108](https://opensource.zalando.com/restful-api-guidelines/), [AIP-180](https://google.aip.dev/180) |
| Kontrak | Menambahkan required field/validasi lebih ketat pada minor | Request lama yang sebelumnya valid menjadi 4xx | `[Praktik industri]` [AIP-180](https://google.aip.dev/180), [Zalando rule 107](https://opensource.zalando.com/restful-api-guidelines/) |
| Kontrak | Mengubah error format atau pagination tanpa major | Klien mengandalkan bentuk error/page; perubahan semantik dapat merusak | `[Standar resmi]` [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html); `[Praktik industri]` [Zalando rules 159–161](https://opensource.zalando.com/restful-api-guidelines/), [AIP-180](https://google.aip.dev/180) |
| Kontrak | Menganggap path versioning sebagai "standar REST" | Ia trade-off industri; RFC 9110 memisahkan resource dan representasi, Zalando justru melarang URL versioning | `[Standar resmi]` [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html); `[Praktik industri]` [Zalando rule 114](https://opensource.zalando.com/restful-api-guidelines/) |
| Lifecycle | Versi tanpa batas waktu / "deprecated, dipadamkan nanti" | Tidak ada kepastian migrasi; RFC 8594 justru dirancang untuk waktu sunset yang diketahui | `[Standar resmi]` [RFC 8594 §1.4, §3](https://www.rfc-editor.org/rfc/rfc8594.html) |
| Lifecycle | Tertukar `Deprecation` (RFC 9745) dan `Sunset` (RFC 8594), atau `Sunset` lebih awal dari `Deprecation` | Header salah syntax/semantik dan melanggar urutan normatif | `[Standar resmi]` [RFC 9745 §2/§4](https://www.rfc-editor.org/rfc/rfc9745.html), [RFC 8594 §3](https://www.rfc-editor.org/rfc/rfc8594.html) |
| Lifecycle | Tidak ada metrik pemakaian per versi | Contract/sunset diputus berdasarkan dugaan; klien mobile/webhook lama bisa masih aktif | `[Praktik industri]` [Martin Fowler, "Canary Release"](https://martinfowler.com/bliki/CanaryRelease.html), [Stripe Docs](https://docs.stripe.com/api-versions), [Pact `--all prod`](https://docs.pact.io/pact_broker/can_i_deploy) |
| Deployment | Deploy V3 dan langsung drop kolom lama | Aplikasi image lama selama rolling/canary masih menulis kolom itu | `[Praktik industri]` [Martin Fowler, "Parallel Change"](https://martinfowler.com/bliki/ParallelChange.html), [Kubernetes Docs](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) |
| Deployment | Header/media-type versioning tanpa `Vary` | Cache dapat menyajikan representasi versi salah | `[Standar resmi]` [RFC 9111 §4.1](https://www.rfc-editor.org/rfc/rfc9111.html); `[Praktik industri]` [Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design) |
| Dokumentasi | Satu `openapi.yaml` "latest" yang ditimpa untuk V1/V2/V3 | Kontrak lama hilang, SDK lama tidak dapat direproduksi | `[Standar resmi]` [OAS 3.2.0 §4.1–4.2](https://spec.openapis.org/oas/v3.2.0.html); `[Praktik industri]` [Zalando rules 101/234](https://opensource.zalando.com/restful-api-guidelines/) |
| Dokumentasi | Menyalin isi BRD/FSD/desain/test/laporan ke README, ADR, dan research_notes | Banyak source-of-truth yang drift; melanggar batas scope peneliti lain | `[Praktik industri]` [Write the Docs, "Docs as code"](https://www.writethedocs.org/guide/docs-as-code/), [GitHub Docs, README](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) |
| Dokumentasi | Git log mentah dijadikan CHANGELOG; ADR lama ditimpa; release tanpa tag | Konsumen tidak melihat dampak; keputusan kehilangan jejak; rilis tidak reproducible | `[Praktik industri]` [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), [MADR 4.0.0](https://adr.github.io/madr/), [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) |
| Dokumentasi | Monorepo tanpa project graph/cache/module boundaries | CI menjalankan semua tes; kode internal menjadi dependensi lintas tim | `[Praktik industri]` [Nx, "What is a Monorepo?"](https://nx.dev/docs/concepts/decisions/why-monorepos), [Turborepo](https://turbo.build/repo/docs/core-concepts/monorepos) |
| Konfigurasi | Secret/env production masuk `config/`, atau config per-deploy di-hardcode | Kredensial bocor dan perubahan environment memaksa perubahan kode | `[Praktik industri]` [The Twelve-Factor App, "Config"](https://12factor.net/config), [git-scm, "gitignore"](https://git-scm.com/docs/gitignore) |
| Konfigurasi | Branch panjang GitFlow untuk layanan continuous-delivery | Integrasi tertunda; penulis model itself menyarankan workflow lebih sederhana untuk web apps | `[Praktik industri]` [Trunk-Based Development](https://trunkbaseddevelopment.com/5-min-overview/), [nvie reflection 2020](https://nvie.com/posts/a-successful-git-branching-model/) |

### 8.6 Checklist cutover dan kriteria rollback

**Checklist cutover.** `[Rekomendasi peneliti/tim]` — lihat template lengkap `templates/06-Checklist-Release.md`; dasar [Pact Docs, "Can I Deploy"](https://docs.pact.io/pact_broker/can_i_deploy), [AWS API Gateway canary](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md), [Kubernetes Docs, "Deployments"](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html), [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html):

1. Kontrak V3, SDK V3, migration guide, dan navigation hub final.
2. Compatibility gate + Pact matrix + `can-i-deploy` hijau.
3. Expand/backfill/dual-write parity dan kill-switch diuji.
4. Canary dengan log/metrik terpisah; SLO dan business KPI hijau.
5. Header lifecycle benar; komunikasi konsumen dan daftar exception lengkap.
6. Promote V3; `record-deployment`; tag rilis; dashboard per versi aktif.
7. Dual-write lama **tetap ON** sampai jendela rollback berakhir; contract dijadwalkan terpisah.

Rollback aman mensyaratkan dual-write lama tetap aktif sampai parity dan SLO stabil; contract database harus menjadi rilis terpisah. `[Rekomendasi peneliti/tim]` — [Martin Fowler, "Parallel Change"](https://martinfowler.com/bliki/ParallelChange.html), [Kubernetes Docs, "Deployments"](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

**Kriteria rollback.** `[Rekomendasi peneliti/tim]` — ambang wajib diisi sebelum cutover:

| Pemicu | Tindakan | Dasar |
|---|---|---|
| 5xx / p95 / business KPI melewati `{{AMBANG}}` | Reroute canary ke stable; matikan `{{FLAG_V3}}`; pertahankan dual-write | `[Praktik industri]` [Martin Fowler, "Canary Release"](https://martinfowler.com/bliki/CanaryRelease.html), [AWS API Gateway canary](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md) |
| Rollout `ProgressDeadlineExceeded`, readiness/image failure | `kubectl rollout undo` ke revisi stabil | `[Praktik industri]` [Kubernetes Docs, "Deployments"](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) |
| `dual_write_mismatch_total` melebihi ambang | Hentikan switch, jalankan reconciliation, jangan contract | `[Praktik industri]` [Martin Fowler, "Parallel Change"](https://martinfowler.com/bliki/ParallelChange.html) |
| Verifikasi kontrak gagal setelah deploy | Blokir promosi berikutnya; rollback konsumen/provider sesuai matrix | `[Praktik industri]` [Pact Docs, "Can I Deploy"](https://docs.pact.io/pact_broker/can_i_deploy) |
| Konsumen prioritas tinggi masih aktif pada versi sunset | Tunda pemadaman, perpanjang notice, perbarui `Sunset` | `[Standar resmi]` [RFC 8594 §8](https://www.rfc-editor.org/rfc/rfc8594.html); `[Praktik industri]` [Stripe Docs](https://docs.stripe.com/api-versions) |
| Cache menyajikan representasi versi salah | Matikan caching lintas versi, perbaiki `Vary`/cache key | `[Standar resmi]` [RFC 9111 §4.1](https://www.rfc-editor.org/rfc/rfc9111.html) |

Kubernetes menyediakan `kubectl rollout undo`, kondisi `ProgressDeadlineExceeded`, dan default `maxUnavailable`/`maxSurge` 25%; AWS canary dapat dipromosikan atau dibatalkan berdasarkan metrik terpisah. `[Praktik industri]` — [Kubernetes Docs](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), [AWS API Gateway canary](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md).

### 8.7 Catatan konflik, keterbatasan verifikasi, dan Gaps

#### 8.7.1 Catatan konflik yang melekat pada keputusan

- Karena tidak ada RFC yang mewajibkan satu metode versioning, keputusan `/api/vN` harus dibaca sebagai **keputusan rekayasa organisasi** yang dioptimalkan untuk visibilitas, routing, cache, SDK, dan observability—bukan konformitas REST. `[Rekomendasi peneliti/tim]` — [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html), [Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design), [Zalando](https://opensource.zalando.com/restful-api-guidelines/), [Google Cloud Blog](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you)
- Zero downtime bukan sekadar deployment: rolling/canary hanya aman bila **database dan kontrak** kompatibel dengan image lama maupun baru; karena itu Expand–Contract, feature flag, dan consumer contracts harus menjadi satu urutan yang sama. `[Rekomendasi peneliti/tim]` — [Martin Fowler, "Parallel Change"](https://martinfowler.com/bliki/ParallelChange.html), [Kubernetes Docs](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), [AWS API Gateway canary](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md), [Pact Docs, "Can I Deploy"](https://docs.pact.io/pact_broker/can_i_deploy)
- Banyaknya versi hidup bersamaan menaikkan biaya pemahaman, pengujian, pemeliharaan, dan rilis; oleh karena itu N-1/N-2 serta tanggal sunset harus eksplisit dan major baru hanya untuk perubahan yang benar-benar tidak dapat dilakukan secara additif. `[Rekomendasi peneliti/tim]` — [Zalando rule 113](https://opensource.zalando.com/restful-api-guidelines/), [Martin Fowler, "Canary Release"](https://martinfowler.com/bliki/CanaryRelease.html), [Google Cloud Blog](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you)

#### 8.7.2 Konflik sumber yang tidak disembunyikan

- **Zalando vs Microsoft/Apigee.** Zalando `MUST use media type versioning` dan `MUST not use URL versioning`; Microsoft menjabarkan URI versioning sebagai opsi sederhana/eksplisit; Apigee menyarankan URL untuk entity versioning tetapi menolak versi di `Accept`/`Content-Type` dan menyarankan `Accept-Version` untuk format. Ketiganya `[Praktik industri]`, bukan standar IETF. — [Zalando](https://opensource.zalando.com/restful-api-guidelines/), [Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design), [Google Cloud Blog](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you)
- **Perluasan enum response.** Stripe menganggap penambahan event type/response property kompatibel dengan syarat klien mengabaikan yang asing; Zalando melarang perluasan enum output karena klien mungkin tidak siap; AIP-180 membolehkan dengan kehati-hatian. Implementasi harus mendokumentasikan pilihan tolerant-reader atau major baru. `[Praktik industri]` — [Stripe Docs](https://docs.stripe.com/api-versions), [Zalando rule 107/108](https://opensource.zalando.com/restful-api-guidelines/), [AIP-180](https://google.aip.dev/180)
- **Konsekuensi.** Fowler menyarankan rollback canary dengan reroute ke versi lama, memantau versi klien yang masih aktif, dan menunggu angka pemakaian turun sebelum contract; ini sejalan dengan kewajiban metrik per versi, tetapi berbenturan dengan praktik pemadaman berdasarkan kalender semata. `[Praktik industri]` — [Martin Fowler, "Canary Release"](https://martinfowler.com/bliki/CanaryRelease.html); `[Standar resmi]` — [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html)

#### 8.7.3 Keterbatasan verifikasi sumber

- Tidak ditemukan standar IETF/ISO yang menetapkan angka universal untuk **N-1/N-2**, lama notice period, persentase canary, atau ambang metrik sunset. Semua nilai dalam catatan ini sengaja berupa placeholder keputusan organisasi. `[Rekomendasi peneliti/tim]`
- Dokumentasi **PayPal API Design Guidelines** tidak berhasil diverifikasi langsung pada URL repositori yang dicoba (HTTP 404); karena itu tidak dijadikan dasar klaim normatif. Sumber primer yang digunakan sudah mencakup RFC, OAS, Stripe, Microsoft, Google, AWS, Kubernetes, Zalando, Pact, Nx, Turborepo, GitHub, Git, EditorConfig, 12-Factor, SemVer, Keep a Changelog, Conventional Commits, MADR, Clean/Hexagonal, dan Fowler. `[Rekomendasi peneliti/tim]`
- Halaman wiki **ASP.NET API versioning** yang dicoba tidak menampilkan konten karena halaman login GitHub; oleh karena itu catatan tidak mengklaim detail implementasi library tersebut. Pedoman Microsoft Learn yang dapat diakses dipakai sebagai gantinya. `[Rekomendasi peneliti/tim]` — [Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design)
- Versi OAS yang tercantum pada halaman resmi 3.2.0/3.2.1 mencakup 3.2.1; catatan tidak menyebut tanggal rilis 3.2.1 karena tidak diverifikasi dari halaman tersebut, hanya keberadaan dan status patch-nya. `[Standar resmi]` — [OAS 3.2.1](https://spec.openapis.org/oas/v3.2.1.html)
- Entri koreksi standar yang tidak tercantum pada rentang catatan ini (lihat 8.3) tidak diverifikasi dan sengaja tidak diberi URL, mengikuti larangan mengarang fakta atau URL baru. `[Rekomendasi peneliti/tim]`

#### 8.7.4 Gaps

- Tidak ada standar yang memberi ambang rollback, jendela observasi, atau lama retensi versi sunset; nilai harus disetujui owner dan dicantumkan di release checklist. `[Rekomendasi peneliti/tim]`
- Daftar file root, matriks RACI, RTM, dan Definition of Done adalah sintesis tata kelola, bukan format normatif dari satu standar. `[Rekomendasi peneliti/tim]`
- Sumber sekunder/blog hanya dipakai sebagai pelengkap opini industri dan selalu ditandai `[Praktik industri]`; tidak ada klaim normatif yang hanya bersandar pada blog sekunder. `[Rekomendasi peneliti/tim]`

### 8.8 Sumber bagian ini

Seluruh URL berikut dikutip apa adanya dari catatan sumber; tidak ada URL tambahan. Pengelompokan memisahkan `[Standar resmi]`, dokumentasi primer vendor/proyek, dan `[Praktik industri]` sesuai konvensi pada 8.1.

#### Standar resmi `[Standar resmi]`

1. ISO/IEC/IEEE 29148:2018, *Systems and software engineering — Life cycle processes — Requirements engineering* — https://www.iso.org/standard/72089.html
2. RFC 8594, *The Sunset HTTP Header Field* (2019) — https://www.rfc-editor.org/rfc/rfc8594.html
3. RFC 9110, *HTTP Semantics*, STD 97 (2022) — https://www.rfc-editor.org/rfc/rfc9110.html
4. RFC 9111, *HTTP Caching*, STD 98 (2022) — https://www.rfc-editor.org/rfc/rfc9111.html
5. RFC 9457, *Problem Details for HTTP APIs* (2023, menggantikan RFC 7807) — https://www.rfc-editor.org/rfc/rfc9457.html
6. RFC 9745, *The Deprecation HTTP Response Header Field* (Maret 2025) — https://www.rfc-editor.org/rfc/rfc9745.html
7. OpenAPI Specification 3.1.0 — https://spec.openapis.org/oas/v3.1.0.html
8. OpenAPI Specification 3.2.0 — https://spec.openapis.org/oas/v3.2.0.html
9. OpenAPI Specification 3.2.1 — https://spec.openapis.org/oas/v3.2.1.html

#### Dokumentasi resmi vendor/proyek `[Praktik industri]` (sumber primer)

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

#### Spesifikasi/konvensi komunitas, guideline perusahaan, dan opini industri `[Praktik industri]`

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
