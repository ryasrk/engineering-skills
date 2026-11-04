> Sumber: Semantic Versioning 2.0.0 — https://semver.org/spec/v2.0.0.html
> Catatan: Dipakai saat menyusun kalender migrasi bertahap V1→V2→V3 lengkap dengan gate per fase.
# Timeline Migrasi Bertahap V1–V2–V3

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
