> Sumber: Write the Docs, "Docs as code" — https://www.writethedocs.org/guide/docs-as-code/
> Catatan: Dipakai saat menyiapkan tata letak dokumentasi proyek baru dengan satu path kanonik per artefak.
# Struktur Folder Dokumentasi Proyek

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
