## 6. Lainnya — Skema folder dan skema project

> Template terkait: templates/06-Struktur-Folder.md, templates/06-Struktur-Folder-Monorepo.md, templates/06-Documentation-Hub.md, templates/06-CODEOWNERS.md, templates/06-CHANGELOG.md, templates/06-ADR.md, templates/06-Definition-of-Done.md, templates/06-RTM.md, templates/06-RACI.md, templates/06-Checklist-Release.md

### 6.1 Ringkasan best practices

Inti temuan: struktur paling mudah diaudit adalah **satu canonical path per artefak**, README sebagai *navigation hub*, docs-as-code, ADR yang immutable, serta kepemilikan yang ditegakkan oleh CODEOWNERS dan branch protection; pilihan monorepo atau polyrepo ditentukan oleh kebutuhan *atomic change*, isolasi akses, dan kesiapan *tooling graph/cache*. `[Rekomendasi peneliti/tim]` — `[Standar resmi]` [GitHub Docs, About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes), `[Praktik industri]` [Write the Docs, Docs as code](https://www.writethedocs.org/guide/docs-as-code/), `[Praktik industri]` [MADR 4.0.0](https://adr.github.io/madr/), `[Standar resmi]` [Nx, Monorepo vs Polyrepo](https://nx.dev/docs/concepts/decisions/monorepo-vs-polyrepo).

**Legenda penanda** (pemetaan dari konvensi catatan sumber):

| Penanda laporan | Klasifikasi asli pada catatan | Makna |
|---|---|---|
| `[Standar resmi]` | `[STANDAR]`, `[VENDOR/RESMI]` | RFC/ISO/spesifikasi normatif, serta dokumentasi resmi vendor/proyek |
| `[Praktik industri]` | `[INDUSTRI]`, `[INDUSTRI—template proyek resmi]`, `[INDUSTRI—konvensi proyek]`, `[INDUSTRI—opini penulis model]` | Praktik, konvensi komunitas, atau opini industri; bukan standar |
| `[Rekomendasi peneliti/tim]` | `[REKOMENDASI PENELITI]` | Sintesis tim yang tetap merujuk ke dasar faktualnya |

Ringkasan operasional:

1. **Satu source-of-truth per fakta.** Duplikasi hanya berupa tautan; template disimpan terpisah dari artefak final. `[Rekomendasi peneliti/tim]` — `[Praktik industri]` [Write the Docs, "Docs as code"](https://www.writethedocs.org/guide/docs-as-code/).
2. **README cukup menjadi indeks.** Memuat tujuan, cara memulai, bantuan, dan pemelihara; dokumentasi panjang ditempatkan terpisah. `[Standar resmi]` [GitHub Docs, "About the repository README file"](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes).
3. **Docs-as-code.** Issue tracker, version control, plain-text markup, code review, dan automated tests memungkinkan fitur diblokir bila dokumentasinya belum ada. `[Praktik industri]` [Write the Docs, "Docs as code"](https://www.writethedocs.org/guide/docs-as-code/).
4. **ADR tidak ditimpa.** Keputusan lama ditandai `superseded`; nama berkas mengikuti `NNNN-title-with-dashes.md`. `[Praktik industri]` [Markdown Architectural Decision Records](https://adr.github.io/madr/).
5. **Changelog terkurasi untuk manusia.** `Unreleased`, urutan kronologis terbalik, tanggal ISO, dan kategori baku; git log diff penuh noise. `[Praktik industri]` [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/).
6. **Kepemilikan sebagai gate, bukan prose.** CODEOWNERS memicu review otomatis dan dapat diwajibkan oleh branch protection. `[Standar resmi]` [GitHub Docs, "About code owners"](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners), [GitHub Docs, "About protected branches"](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
7. **Monorepo bukan monolith.** Tiap proyek tetap dapat dibangun, diuji, dan dideploy sendiri; tanpa *graph*, muncul tes berlebih, hilangnya batas modul, dan tooling tidak konsisten. `[Standar resmi]` [Nx, "What is a Monorepo?"](https://nx.dev/docs/concepts/decisions/why-monorepos), [Turborepo](https://turbo.build/repo/docs/core-concepts/monorepos).
8. **Batas modul mengarah ke dalam.** Dependensi sumber hanya ke lapisan dalam; teknologi luar ditempatkan sebagai adapter agar aplikasi dapat diuji tanpa UI/database. `[Praktik industri]` [Robert C. Martin, "The Clean Architecture"](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html), [Alistair Cockburn, "Hexagonal architecture"](https://alistair.cockburn.us/hexagonal-architecture/).
9. **Konfigurasi dipisahkan dari kode.** Nilai yang berubah antar deploy ditempatkan di environment variables; `.gitignore` dan `.editorconfig` ikut version control. `[Praktik industri]` [The Twelve-Factor App, "Config"](https://12factor.net/config); `[Standar resmi]` [git-scm, gitignore](https://git-scm.com/docs/gitignore), [EditorConfig](https://editorconfig.org/).
10. **Alur integrasi pendek.** Trunk yang selalu release-ready dengan perubahan kecil dan sering. `[Praktik industri]` [Trunk-Based Development](https://trunkbaseddevelopment.com/5-min-overview/).

Inferensi yang ditegaskan catatan: docs-as-code, CODEOWNERS, dan branch protection mengubah tata kelola dari prose menjadi gate yang dapat diverifikasi CI; satu canonical path plus pemisahan `templates/` dari artefak final mengurangi drift tanpa melarang tautan navigasi; monorepo hanya menguntungkan bila dependency graph, affected detection, caching, dan module boundaries benar-benar dioperasikan. `[Rekomendasi peneliti/tim]`

### 6.2 Dua pohon direktori konkret

Kedua pohon memakai placeholder `{{...}}` sebagaimana catatan sumber. Entri yang berkaitan dengan topik bagian laporan terpisah sengaja tidak ditampilkan; rujukan lengkapnya ada pada berkas template mandiri.

#### 6.2.1 Pohon dokumentasi proyek

Disusun dari peta artefak per fase, tabel tata kelola, aturan versioning dokumen, dan daftar review dokumentasi pada catatan sumber. `[Rekomendasi peneliti/tim]`

```text
{{NAMA_REPO}}/
├── README.md                              # Navigation hub; HANYA indeks, bukan salinan artefak
├── LICENSE
├── CONTRIBUTING.md                        # Conventional Commits, PR, review, branch, DoD
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md                           # Keep a Changelog 1.1.0; Unreleased; urut terbalik
├── .editorconfig                          # root=true; indent/EOL/charset konsisten
├── .gitignore                             # generated, local env, secret, build artifacts
├── .github/
│   └── CODEOWNERS                         # urutan: .github/, root, docs/; pola terakhir menang
└── docs/
    ├── README.md                          # indeks docs; peta artefak per fase
    ├── requirements/
    │   ├── {{PATH_BRD}}                   # isi di luar scope catatan struktur ini
    │   └── {{PATH_FSD}}                   # isi di luar scope catatan struktur ini
    ├── design/
    │   └── {{PATH_DESAIN}}                # isi di luar scope catatan struktur ini
    ├── test/
    │   └── {{PATH_TESTING}}               # isi di luar scope catatan struktur ini
    ├── reports/
    │   └── {{YYYY}}/
    │       └── {{MM}}/
    │           └── {{PATH_LAPORAN}}       # isi di luar scope catatan struktur ini
    ├── adr/
    │   ├── README.md                      # ADR index
    │   └── {{NNNN}}-{{JUDUL}}.md          # keputusan lama -> superseded, bukan ditimpa
    ├── governance/
    │   ├── definition-of-done.md
    │   ├── rtm.md
    │   ├── raci.md
    │   └── release-checklist.md
    └── templates/                         # template berplaceholder; hasil disalin ke path kanonik
```

Aturan yang melekat: README hanya indeks; satu source-of-truth per fakta; duplikasi hanya berupa tautan; `CHANGELOG.md` memiliki `Unreleased`, tanggal ISO, serta kategori perubahan yang relevan; secret tidak masuk `config/` atau contoh; CODEOWNERS mencakup area kepemilikan dan CI. `[Standar resmi]` [GitHub Docs, About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes), [GitHub Docs, "About code owners"](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners); `[Praktik industri]` [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), [Markdown Architectural Decision Records](https://adr.github.io/madr/).

#### 6.2.2 Pohon project/monorepo

Disarikan dari layout monorepo layanan + klien pada catatan sumber, dengan dasar Clean Architecture, Hexagonal Architecture, Nx module boundaries, 12-Factor config, dan GitHub CODEOWNERS. `[Rekomendasi peneliti/tim]` — `[Praktik industri]` [Robert C. Martin, "The Clean Architecture"](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html), [Alistair Cockburn, "Hexagonal architecture"](https://alistair.cockburn.us/hexagonal-architecture/), [The Twelve-Factor App, "Config"](https://12factor.net/config); `[Standar resmi]` [Nx, "What is a Monorepo?"](https://nx.dev/docs/concepts/decisions/why-monorepos), [GitHub Docs, "About code owners"](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).

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
│       ├── ci.yaml                        # build + unit + lint
│       ├── release.yaml                   # tag + changelog
│       └── docs.yaml                      # link checker, markdown lint, docs build
├── .gitlab-ci.yml                         # opsional bila GitLab; jangan aktif dua CI identik tanpa owner
├── apps/
│   ├── frontend/{{NAMA_WEB}}/             # UI adapter; tidak berisi aturan domain
│   ├── backend/{{NAMA_API}}/
│   │   ├── src/
│   │   │   ├── main/{{BAHASA}}/           # bootstrap, DI, config loader
│   │   │   └── interface/http/shared/     # middleware, correlation ID, error mapper
│   │   └── tests/
│   └── services/{{NAMA_WORKER}}/          # consumer/event worker terpisah
├── packages/                              # atau libs/, sesuai konvensi tooling
│   ├── domain/                            # entitas + aturan bisnis; dependency mengarah ke dalam
│   ├── application/                       # use case + port interface; tidak tahu HTTP/DB
│   ├── adapters/
│   │   ├── persistence/                   # repository SQL/NoSQL; implementasi port
│   │   ├── messaging/                     # publisher/consumer adapter
│   │   └── external/{{VENDOR}}/           # klien pihak ketiga
│   ├── contracts/                         # source-of-truth kontrak; PILIH SATU dengan docs/
│   ├── sdk/                               # generated client; JANGAN edit hasil generate
│   └── shared/                            # util murni, types, error problem+json
├── infra/
│   ├── terraform/ atau helm/              # IaC; environment bukan salinan kode aplikasi
│   ├── k8s/                               # Deployment manifests
│   └── observability/                     # dashboard + alert
├── config/
│   ├── config.example.yaml
│   ├── environments/{development,staging,production}.yaml
│   └── README.md                          # daftar nama env var + pemilik + sumber secret
├── scripts/                               # bootstrap, SDK generation
├── tests/
│   ├── e2e/                               # end-to-end minimal
│   ├── performance/
│   └── fixtures/
└── docs/                                  # pohon pada 6.2.1; kontrak di sini ATAU packages/contracts
    └── README.md
```

**Batas modul.** Dependency Rule melarang lapisan dalam mengetahui framework, UI, database, atau entity luar; data yang melintas batas sebaiknya struktur data sederhana, bukan database row/Entity. Teknologi luar adalah adapter yang dapat diganti, sehingga aplikasi dapat diuji tanpa UI/database. `[Praktik industri]` [Robert C. Martin, "The Clean Architecture"](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html), [Alistair Cockburn, "Hexagonal architecture"](https://alistair.cockburn.us/hexagonal-architecture/).

**Konfigurasi dan editor.** 12-Factor memisahkan config dari kode dan menaruh nilai yang berubah antar deploy pada environment variables; konfigurasi internal yang tidak berubah tetap di kode. `.gitignore` menentukan file untracked yang sengaja diabaikan serta pola yang sebaiknya di-version-control; `.editorconfig` menjaga indentasi/EOL/charset lintas editor. `[Praktik industri]` [The Twelve-Factor App, "Config"](https://12factor.net/config); `[Standar resmi]` [git-scm, gitignore](https://git-scm.com/docs/gitignore), [EditorConfig](https://editorconfig.org/).

### 6.3 Tabel konvensi penting

| Konvensi | Aturan faktual | Penanda + sitasi |
|---|---|---|
| README sebagai hub | Tujuan, cara memulai, bantuan, pemelihara; dokumentasi panjang terpisah; hanya indeks | `[Standar resmi]` [GitHub Docs, "About the repository README file"](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) |
| Docs-as-code | Issue tracker, version control, plain-text markup, code review, automated tests | `[Praktik industri]` [Write the Docs, "Docs as code"](https://www.writethedocs.org/guide/docs-as-code/) |
| ADR immutable | `docs/decisions/`, `NNNN-title-with-dashes.md`, status `superseded`, bukan ditimpa | `[Praktik industri]` [Markdown Architectural Decision Records](https://adr.github.io/madr/) |
| ISO/IEC/IEEE 29148:2018 | Information items requirements engineering serta panduan formatnya; dipakai hanya sebagai konteks tata kelola artefak | `[Standar resmi]` [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) |
| SemVer 2.0.0 | `MAJOR.MINOR.PATCH`; MAJOR = perubahan tidak kompatibel, MINOR = fungsi tambahan kompatibel, PATCH = bug fix kompatibel; deprecation didokumentasikan dan hadir dalam minimal satu MINOR sebelum penghapusan pada MAJOR | `[Praktik industri]` [semver.org, Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) |
| Conventional Commits 1.0.0 | `<type>[optional scope]: <description>`; `fix`≈PATCH, `feat`≈MINOR, `!` atau footer `BREAKING CHANGE:`≈MAJOR; body dan footers opsional | `[Praktik industri]` [conventionalcommits.org v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) |
| Keep a Changelog 1.1.0 | `CHANGELOG.md`, `Unreleased`, kategori Added/Changed/Deprecated/Removed/Fixed/Security, versi terbaru di atas, tanggal ISO, sebutkan SemVer | `[Praktik industri]` [keepachangelog.com 1.1.0](https://keepachangelog.com/en/1.1.0/) |
| Trunk-based | Satu trunk selalu release-ready, integrasi kecil dan sering, short-lived review branch, CI sebagai safety net; rilis dari trunk atau branch-for-release | `[Praktik industri]` [Trunk-Based Development, "Five-minute overview"](https://trunkbaseddevelopment.com/5-min-overview/) |
| GitFlow | `master` + `develop` + feature/release/hotfix; cocok untuk perangkat lunak berversi eksplisit atau beberapa versi di wild | `[Praktik industri]` [nvie, "A successful Git branching model"](https://nvie.com/posts/a-successful-git-branching-model/) |
| Branch protection | Required reviews, CODEOWNERS review, status checks, conversation resolution, linear history, merge queue, signed commits, deploy sukses, larangan bypass; default melarang force push/delete | `[Standar resmi]` [GitHub Docs, "About protected branches"](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) |
| CODEOWNERS | Owner otomatis diminta review; dapat diwajibkan branch protection; lokasi `.github/`, root, `docs/`; pola terakhir menang; path case-sensitive | `[Standar resmi]` [GitHub Docs, "About code owners"](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) |
| Release tag | `v{{MAJOR}}.{{MINOR}}.{{PATCH}}`; `v` adalah konvensi nama tag, bukan bagian dari SemVer; signed tag dianjurkan dalam model GitFlow | `[Praktik industri]` [SemVer FAQ](https://semver.org/spec/v2.0.0.html), [nvie GitFlow](https://nvie.com/posts/a-successful-git-branching-model/) |
| Config/ignore/editor | Config yang berubah antar deploy di environment variables; pola ignore dan `.editorconfig` dibagikan lewat clone | `[Praktik industri]` [The Twelve-Factor App, "Config"](https://12factor.net/config); `[Standar resmi]` [git-scm, gitignore](https://git-scm.com/docs/gitignore), [EditorConfig](https://editorconfig.org/) |

#### 6.3.1 Trunk-based vs GitFlow

| Aspek | Trunk-based | GitFlow |
|---|---|---|
| Bentuk cabang | Satu trunk + short-lived review branch | `master` + `develop` + feature/release/hotfix |
| Integrasi | Kecil dan sering; CI sebagai safety net | Cabang feature/release/hotfix berumur lebih panjang |
| Rilis | Dari trunk atau branch-for-release | Cocok untuk perangkat lunak berversi eksplisit / beberapa versi di wild |
| Catatan penulis | — | Penulis model menyarankan workflow lebih sederhana untuk continuous delivery web apps |
| Dasar | `[Praktik industri]` [Trunk-Based Development](https://trunkbaseddevelopment.com/5-min-overview/) | `[Praktik industri]` [nvie, catatan refleksi 2020](https://nvie.com/posts/a-successful-git-branching-model/) |

**Rekomendasi alur.** `[Rekomendasi peneliti/tim]` Untuk rentang 2024–2026 dan layanan yang terus di-deploy, gunakan **trunk-based + short-lived PR + feature flag**; simpan GitFlow hanya bila organisasi memang harus memelihara beberapa rilis paket/binari lama. Dasar faktual: `[Praktik industri]` [Trunk-Based Development](https://trunkbaseddevelopment.com/5-min-overview/) dan `[Praktik industri]` [nvie, "A successful Git branching model"](https://nvie.com/posts/a-successful-git-branching-model/). Catatan sumber juga menegaskan preferensi trunk-based dan short-lived PR dibanding integrasi branch panjang. `[Rekomendasi peneliti/tim]`

#### 6.3.2 Aturan CODEOWNERS yang perlu ditegakkan

Lokasi yang dikenal: `.github/`, root, `docs/` (urutan dipakai bila beberapa file ada); pola cocok **terakhir** menang dan jalur case-sensitive; owner otomatis diminta review; branch protection dapat mewajibkan approval code owner; workflow CI/CD dapat diotomasi dengan GitHub Actions. `[Standar resmi]` [GitHub Docs, "About code owners"](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners), [GitHub Docs, "About protected branches"](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), [GitHub Actions documentation](https://docs.github.com/en/actions). Contoh isi `CODEOWNERS` berplaceholder tersedia sebagai berkas mandiri; laporan ini tidak menyalinnya. `[Rekomendasi peneliti/tim]`

### 6.4 Monorepo vs polyrepo

| Dimensi | Monorepo | Polyrepo | Multi-repo / beberapa monorepo |
|---|---|---|---|
| Perubahan lintas API + konsumen | Satu PR atomik | Beberapa PR dan rilis berurutan | Atomik di dalam klaster, koordinasi antar klaster |
| Isolasi akses | Per-folder ownership/graph rules | Per-repository permission | Per klaster |
| Cadence rilis | Artefak punya tag sendiri; tidak harus deploy bersama | Independen secara default | Independen antar klaster |
| CI | Perlu affected detection/cache | Banyak pipeline kecil yang diulang | Beberapa pipeline + tooling berulang |
| Dependensi | Single-version policy dapat ditegakkan | Versi mudah drift | Kebijakan per klaster |
| Cocok bila | Banyak shared code, perubahan API+UI sering bersamaan, konvensi disepakati | Isolasi repository-level adalah hard requirement, sedikit kode bersama | Batas domain/legal/public-vs-internal nyata |
| Tooling | Nx/Turborepo/Bazel/Rush, package-manager workspaces, affected graph, module boundaries | Template repo, shared plugin/library versi, CI reusable | Kombinasi keduanya |

Sumber klasifikasi dan trade-off: `[Standar resmi]` [Nx, "Monorepo vs Polyrepo"](https://nx.dev/docs/concepts/decisions/monorepo-vs-polyrepo), [Nx, "What is a Monorepo?"](https://nx.dev/docs/concepts/decisions/why-monorepos), [Turborepo](https://turbo.build/repo/docs/core-concepts/monorepos). Nx mendefinisikan monorepo sebagai satu repositori berisi beberapa proyek dengan relasi terdefinisi, menyebut keuntungan shared code tanpa publish, single source of truth, atomic change, konvensi yang dapat ditegakkan, developer mobility, dan satu kebijakan dependensi; Turborepo menambahkan remote cache dan task scheduling untuk ribuan task. `[Standar resmi]` [Nx, "What is a Monorepo?"](https://nx.dev/docs/concepts/decisions/why-monorepos), [Turborepo, "What is Turborepo?"](https://turbo.build/repo/docs/core-concepts/monorepos).

Nx secara eksplisit menyarankan polyrepo bila kontrol akses tingkat repositori wajib atau tim hampir tidak berbagi kode, serta mengakui beberapa monorepo sebagai jalan tengah dengan biaya CI/tooling berulang. Keputusan akhir bersifat organisasional dan menuntut kesepakatan tentang dependency management, code ownership, dependency rules, folder structure, Git workflow, CI, dan deployment. `[Standar resmi]` [Nx, "Monorepo vs Polyrepo"](https://nx.dev/docs/concepts/decisions/monorepo-vs-polyrepo).

`[Rekomendasi peneliti/tim]` Pilih monorepo bila perubahan lintas modul harus atomik dan shared code dominan; pilih polyrepo bila isolasi akses atau cadence rilis klien benar-benar independen. Apapun pilihannya, operasikan task graph, affected detection, caching, dan module boundaries—tanpa itu manfaat monorepo hilang. `[Rekomendasi peneliti/tim]`

### 6.5 Artefak pendukung dan template mandiri

Seluruh template pada catatan sumber adalah berkas Markdown lengkap berplaceholder `{{...}}` yang disimpan di `docs/templates/`; hasil isi disalin ke path kanonik. Berkas-berkas berikut sudah menjadi template mandiri, sehingga laporan ini hanya menyebut keberadaan dan section kuncinya. `[Rekomendasi peneliti/tim]`

| Berkas template | Section kunci | Dasar pada catatan |
|---|---|---|
| `templates/06-Struktur-Folder.md` | Pohon dokumentasi; aturan satu canonical path; README hanya indeks | `[Standar resmi]` [GitHub Docs, About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) |
| `templates/06-Struktur-Folder-Monorepo.md` | Layout `apps/` + `packages/`; task graph, caching, affected | `[Standar resmi]` [Nx, "What is a Monorepo?"](https://nx.dev/docs/concepts/decisions/why-monorepos), [Turborepo](https://turbo.build/repo/docs/core-concepts/monorepos) |
| `templates/06-Documentation-Hub.md` | "Mulai cepat", "Peta artefak per fase", "Keputusan dan tata kelola", "Versioning dokumen", "Review dokumentasi", "Sumber normatif" | `[Standar resmi]` [GitHub Docs, About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes); `[Praktik industri]` [Write the Docs, "Docs as code"](https://www.writethedocs.org/guide/docs-as-code/) |
| `templates/06-CODEOWNERS.md` | Urutan lokasi, pola terakhir menang, path case-sensitive, area kepemilikan | `[Standar resmi]` [GitHub Docs, "About code owners"](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) |
| `templates/06-CHANGELOG.md` | `Unreleased`, kategori Added/Changed/Deprecated/Removed/Fixed/Security, tanggal ISO, tautan compare | `[Praktik industri]` [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) |
| `templates/06-ADR.md` | "Context and Problem Statement", "Decision Drivers", "Considered Options", "Decision Outcome", "Consequences", "Confirmation", "Pros and Cons of the Options", "More Information" | `[Praktik industri]` [MADR 4.0.0](https://adr.github.io/madr/) |
| `templates/06-Definition-of-Done.md` | Tabel `# / Kriteria / Bukti / Wajib untuk`; baris tanda tangan approver | `[Rekomendasi peneliti/tim]` — `[Standar resmi]` [GitHub Docs, "About protected branches"](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), [GitHub Docs, "About code owners"](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners), [Pact can-i-deploy](https://docs.pact.io/pact_broker/can_i_deploy) |
| `templates/06-RTM.md` | Tabel `ID Requirement → Sumber kanonik → Keputusan/ADR → Modul → Verifikasi → Status → Pemilik`; bagian "Coverage" | `[Rekomendasi peneliti/tim]` — melacak lokasi dan status, bukan menyalin isi requirements |
| `templates/06-RACI.md` | Legenda R/A/C/I; aturan tepat satu A per baris; kolom peran | `[Rekomendasi peneliti/tim]` |
| `templates/06-Checklist-Release.md` | "Pra-rilis", "Cutover", "Pasca-rilis", "Rollback otomatis bila"; tanda tangan release manager | `[Rekomendasi peneliti/tim]` |

Catatan klasifikasi: ADR mengikuti struktur MADR 4.0.0, CHANGELOG mengikuti Keep a Changelog 1.1.0, sedangkan DoD/RTM/RACI/release checklist adalah `[Rekomendasi peneliti/tim]` berdasarkan tata kelola CODEOWNERS, branch protection, dan Pact `can-i-deploy`; sebagian dasar tambahannya berada di luar cakupan bagian ini. `[Praktik industri]` [MADR](https://adr.github.io/madr/), [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); `[Standar resmi]` [GitHub CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners), [branch protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), [Pact can-i-deploy](https://docs.pact.io/pact_broker/can_i_deploy).

### 6.6 Checklist penerapan

- [ ] README root berisi tujuan, prasyarat, perintah lokal, bantuan/eskalasi, dan pemelihara; dokumentasi panjang dipindah ke `docs/`.
- [ ] README dinyatakan **hanya indeks**; tidak ada isi artefak yang diduplikasi ke dalamnya.
- [ ] Satu canonical path ditetapkan per artefak; duplikasi lain berupa tautan relatif.
- [ ] `docs/templates/` dipisahkan dari artefak final; hasil isi disalin ke path kanonik.
- [ ] Tautan relatif valid setelah clone; link checker dan markdown lint aktif di CI dokumentasi.
- [ ] ADR memakai penomoran `NNNN`; keputusan lama berstatus `superseded by`, bukan ditimpa.
- [ ] `CHANGELOG.md` memiliki `Unreleased`, urutan versi terbalik, tanggal ISO, dan kategori Added/Changed/Deprecated/Removed/Fixed/Security yang relevan.
- [ ] Commit memakai Conventional Commits 1.0.0; `!` atau footer `BREAKING CHANGE:` hanya untuk perubahan MAJOR.
- [ ] Bump SemVer 2.0.0 konsisten dengan jenis commit; breaking change tidak masuk MINOR/PATCH.
- [ ] Tag rilis memakai `v{{MAJOR}}.{{MINOR}}.{{PATCH}}`; `v` dipahami sebagai konvensi nama, bukan bagian SemVer.
- [ ] `.github/CODEOWNERS` mencakup `.github/`, root, `docs/`, dan CI; urutan pola diuji karena pola terakhir menang.
- [ ] Branch protection mewajibkan PR review, approval code owner, required status checks, conversation resolution, linear history, dan melarang bypass.
- [ ] Trunk selalu release-ready; PR berumur pendek; feature flag dan kill-switch tersedia untuk perubahan yang belum siap diaktifkan.
- [ ] `.gitignore` mencakup generated file, local env, secret, dan build artifacts; secret scan bersih.
- [ ] `.editorconfig` dengan `root=true` ikut version control; indentasi/EOL/charset konsisten lintas editor.
- [ ] Config yang berubah antar deploy berada di environment variables; `config/config.example.yaml` dan `config/README.md` memuat nama env var, pemilik, dan sumber secret.
- [ ] Dependensi sumber hanya mengarah ke dalam; `domain/` dan `application/` tidak mengetahui HTTP/DB; adapter luar dapat diganti.
- [ ] Pilihan `docs/` **atau** `packages/contracts/` sebagai source-of-truth kontrak diputuskan dan didokumentasikan—bukan keduanya.
- [ ] Task graph, affected detection, caching, dan module boundaries benar-benar dioperasikan bila memakai monorepo.
- [ ] Tidak ada dua pipeline CI identik aktif tanpa owner yang jelas.
- [ ] DoD, RTM, RACI, dan checklist release memiliki pemilik, versi, tanggal berlaku, serta kolom bukti yang dapat diverifikasi.
- [ ] Metadata rilis (release manager, environment, tanggal, tanda tangan) terisi pada checklist release.

Sumber normatif checklist: `[Standar resmi]` [GitHub Docs, About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes), [GitHub Docs, "About code owners"](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners), [GitHub Docs, "About protected branches"](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches); `[Praktik industri]` [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/), [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html), [Trunk-Based Development](https://trunkbaseddevelopment.com/5-min-overview/). `[Rekomendasi peneliti/tim]`

### 6.7 Anti-pattern

1. **README sebagai gudang dokumen.** Menyalin isi artefak ke README menciptakan drift dan melanggar aturan "hanya indeks". `[Standar resmi]` [GitHub Docs, About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes).
2. **Git log diff dijadikan changelog.** Penuh noise dan tidak terkurasi untuk manusia. `[Praktik industri]` [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/).
3. **ADR lama ditimpa.** Menghapus jejak keputusan; seharusnya ditandai `superseded`. `[Praktik industri]` [Markdown Architectural Decision Records](https://adr.github.io/madr/).
4. **Dua source-of-truth untuk kontrak.** Mengaktifkan `docs/` dan `packages/contracts/` sekaligus; catatan meminta "PILIH SATU". `[Rekomendasi peneliti/tim]`
5. **Monorepo tanpa tooling graph.** Memicu tes yang tidak perlu, hilangnya batas kode, dan tooling tidak konsisten. `[Standar resmi]` [Nx, "What is a Monorepo?"](https://nx.dev/docs/concepts/decisions/why-monorepos).
6. **Monorepo dianggap monolith.** Memaksa semua proyek build/test/deploy bersamaan, padahal tiap proyek dapat berdiri sendiri. `[Standar resmi]` [Nx, "Monorepo vs Polyrepo"](https://nx.dev/docs/concepts/decisions/monorepo-vs-polyrepo).
7. **Aturan bisnis mengetahui detail teknologi luar.** Melanggar Dependency Rule dan membuat aplikasi tidak dapat diuji tanpa UI/database. `[Praktik industri]` [Robert C. Martin, "The Clean Architecture"](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html), [Alistair Cockburn, "Hexagonal architecture"](https://alistair.cockburn.us/hexagonal-architecture/).
8. **File config rahasia ikut ter-commit.** Nilai yang berubah antar deploy seharusnya di environment variables. `[Praktik industri]` [The Twelve-Factor App, "Config"](https://12factor.net/config); `[Standar resmi]` [git-scm, gitignore](https://git-scm.com/docs/gitignore).
9. **`.editorconfig` tidak di-version-control.** Gaya indentasi/EOL/charset lalu bergantung pada editor masing-masing. `[Standar resmi]` [EditorConfig](https://editorconfig.org/).
10. **Mengedit hasil generate secara manual.** Perubahan akan hilang pada regenerasi berikutnya. `[Rekomendasi peneliti/tim]`
11. **Branch panjang dan integrasi jarang.** Tidak selaras dengan continuous delivery dan trunk yang release-ready. `[Praktik industri]` [Trunk-Based Development](https://trunkbaseddevelopment.com/5-min-overview/), [nvie, "A successful Git branching model"](https://nvie.com/posts/a-successful-git-branching-model/).
12. **CODEOWNERS disusun tanpa memahami presedensi.** Pola terakhir menang dan path case-sensitive; urutan yang keliru mengalihkan review ke tim yang salah. `[Standar resmi]` [GitHub Docs, "About code owners"](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
13. **Dua CI identik aktif tanpa owner.** Konfigurasi ganda tanpa penanggung jawab memicu drift. `[Rekomendasi peneliti/tim]`
14. **Template dicampur dengan artefak final.** Mengaburkan mana yang canonical dan mana yang placeholder. `[Rekomendasi peneliti/tim]`

### 6.8 Konflik sumber

| # | Perbedaan | Sisi A | Sisi B | Perlakuan |
|---|---|---|---|---|
| 1 | Model GitFlow vs refleksi penulisnya | Model asli: `master` + `develop` + feature/release/hotfix, cocok untuk perangkat lunak berversi eksplisit atau beberapa versi di wild | Penulis menyarankan workflow lebih sederhana untuk continuous delivery web apps (catatan refleksi 2020) | `[Rekomendasi peneliti/tim]` Pakai trunk-based + short-lived PR + feature flag untuk layanan yang terus di-deploy; simpan GitFlow hanya untuk memelihara beberapa rilis lama. `[Praktik industri]` [nvie, "A successful Git branching model"](https://nvie.com/posts/a-successful-git-branching-model/) |
| 2 | Path kanonik ADR | MADR 4.0.0: `docs/decisions/` dengan `NNNN-title-with-dashes.md` | Template hub dan DoD pada catatan: `docs/adr/README.md` serta `docs/adr/{{NNNN}}-{{JUDUL}}.md` | `[Rekomendasi peneliti/tim]` Ini perbedaan konvensi, bukan kontradiksi normatif; tetapkan **satu** canonical path sebelum clone pertama dan catat dalam ADR. `[Praktik industri]` [Markdown Architectural Decision Records](https://adr.github.io/madr/) |
| 3 | Monorepo vs polyrepo | Nx: monorepo memberi atomic change dan single-version policy | Nx juga menyarankan polyrepo bila isolasi akses repositori wajib atau kode bersama sedikit | Bukan kontradiksi: keputusan bersifat organisasional dan perlu kesepakatan dependency management, code ownership, dependency rules, folder structure, Git workflow, CI, deployment. `[Standar resmi]` [Nx, "Monorepo vs Polyrepo"](https://nx.dev/docs/concepts/decisions/monorepo-vs-polyrepo) |

Konflik lain yang tercatat pada ringkasan eksekutif sumber tidak direproduksi di sini karena berada di luar cakupan bagian ini. `[Rekomendasi peneliti/tim]`

### 6.9 Keterbatasan (Gaps)

- Catatan sumber membatasi diri pada struktur dan tata kelola repositori; **isi** BRD, FSD, dokumen desain arsitektur/UI, test plan, dan format laporan harian sengaja tidak dibahas—yang disebut hanya letak file, penamaan, dan tautan navigasinya. `[Rekomendasi peneliti/tim]`
- Cakupan waktu praktik dan versi dokumen adalah 2024–2026 dengan snapshot 4 November 2026, Asia/Jakarta. Versi yang diverifikasi dan relevan di sini: ISO/IEC/IEEE 29148:2018, SemVer 2.0.0, Keep a Changelog 1.1.0, Conventional Commits 1.0.0, serta MADR 4.0.0 (2024). `[Standar resmi]` [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html); `[Praktik industri]` [MADR](https://adr.github.io/madr/).
- ISO/IEC/IEEE 29148:2018 dipakai **hanya sebagai konteks tata kelola artefak**, bukan sebagai rincian isi requirements engineering. `[Standar resmi]` [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html).
- DoD, RTM, RACI, dan checklist release adalah rekomendasi peneliti, bukan standar normatif; validitasnya bergantung pada bukti yang dilampirkan tiap baris. `[Rekomendasi peneliti/tim]`
- Keputusan monorepo/polyrepo tidak memiliki jawaban universal; catatan menyebutnya organisasional dan mensyaratkan kesepakatan lintas tim. `[Standar resmi]` [Nx, "Monorepo vs Polyrepo"](https://nx.dev/docs/concepts/decisions/monorepo-vs-polyrepo).
- Manfaat monorepo bersifat bersyarat: tanpa affected detection, caching, dan module boundaries yang dioperasikan, keuntungannya tidak terealisasi. `[Rekomendasi peneliti/tim]` — `[Standar resmi]` [Nx, "What is a Monorepo?"](https://nx.dev/docs/concepts/decisions/why-monorepos).
- Contoh layout, `CODEOWNERS`, dan seluruh artefak pendukung memakai placeholder `{{...}}`; nilai konkret harus diisi per organisasi dan tidak dapat disimpulkan dari catatan. `[Rekomendasi peneliti/tim]`
- Topik yang ditetapkan sebagai bagian laporan terpisah tidak disintesiskan; entri pohon yang berkaitan dengannya disaring dari 6.2. `[Rekomendasi peneliti/tim]`
- Catatan sumber menandai sub-bab `### Gaps` pada baris 644; isinya berada di luar rentang baca yang diizinkan (1–49, 178–382, 382–644), sehingga daftar ini hanya merangkum keterbatasan yang tersurat pada rentang tersebut. `[Rekomendasi peneliti/tim]`

### Sumber bagian ini

**`[Standar resmi]`** — [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) (konteks tata kelola information items); [GitHub Docs, "About the repository README file"](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) (peran README); [GitHub Docs, "About code owners"](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) (CODEOWNERS); [GitHub Docs, "About protected branches"](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) (required checks, merge queue, larangan bypass); [GitHub Actions documentation](https://docs.github.com/en/actions) (otomasi CI/CD); [Nx, "What is a Monorepo?"](https://nx.dev/docs/concepts/decisions/why-monorepos) (definisi, project graph); [Nx, "Monorepo vs Polyrepo"](https://nx.dev/docs/concepts/decisions/monorepo-vs-polyrepo) (trade-off); [Turborepo](https://turbo.build/repo/docs/core-concepts/monorepos) (remote cache, task scheduling); [git-scm, gitignore](https://git-scm.com/docs/gitignore); [EditorConfig](https://editorconfig.org/); [Pact can-i-deploy](https://docs.pact.io/pact_broker/can_i_deploy) (dasar tata kelola DoD).

**`[Praktik industri]`** — [Write the Docs, "Docs as code"](https://www.writethedocs.org/guide/docs-as-code/); [Markdown Architectural Decision Records / MADR 4.0.0](https://adr.github.io/madr/) (`docs/decisions/`, `superseded`); [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/); [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) (MAJOR/MINOR/PATCH, FAQ tag `v`); [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) (`fix`, `feat`, `BREAKING CHANGE:`); [The Twelve-Factor App, "Config"](https://12factor.net/config); [Robert C. Martin, "The Clean Architecture"](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) (Dependency Rule); [Alistair Cockburn, "Hexagonal architecture"](https://alistair.cockburn.us/hexagonal-architecture/) (ports & adapters); [Trunk-Based Development, "Five-minute overview"](https://trunkbaseddevelopment.com/5-min-overview/); [nvie, "A successful Git branching model"](https://nvie.com/posts/a-successful-git-branching-model/) (GitFlow + refleksi 2020).

Catatan metodologis: seluruh butir `[Rekomendasi peneliti/tim]` merupakan sintesis yang merujuk kembali ke dasar faktual di atas; sitasi berupa nama dokumen + URL dipertahankan, dan tidak ada URL maupun fakta baru yang ditambahkan. `[Rekomendasi peneliti/tim]`
