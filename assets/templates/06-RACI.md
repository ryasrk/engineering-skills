> Sumber: GitHub Docs, "About code owners" — https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
> Catatan: Dipakai saat menyepakati pembagian peran untuk satu proses atau rilis API.
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
