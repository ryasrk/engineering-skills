> Sumber: Nx, "What is a Monorepo?" — https://nx.dev/docs/concepts/decisions/why-monorepos
> Catatan: Dipakai saat menata repositori layanan dengan adapter V1/V2/V3, kontrak, SDK, dan CI dalam satu atomic change.
# Struktur Folder Monorepo Layanan

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
