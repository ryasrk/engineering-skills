# Contoh End-to-End: Fitur Pencairan Dana Instan (Instant Settlement)

Contoh nyata ini mendemonstrasikan bagaimana sebuah fitur rekayasa perangkat lunak mengalir secara terstruktur dan terhubung melalui ID stabil di setiap fase dokumentasi:

```text
[BRD] BR-SETTLE-001 (Kebutuhan Bisnis & KPI)
  ↓
[FSD] FR-SETTLE-001 (Kriteria Penerimaan Given/When/Then, Decision Table, RBAC)
  ↓
[ADR] ADR-0042 (Keputusan Arsitektur: Outbox Pattern & Idempotency)
  ↓
[Test Plan] TC-SETTLE-01 .. TC-SETTLE-04 (Pact Contract, k6, Fail-Closed CI Gate)
  ↓
[Laporan Harian] Status Operasional Berbasis Bukti (PR #104, DoD Lolos, 0 Blocker)
```

## Berkas Contoh

1. [`01-BRD.md`](01-BRD.md) — Dokumen kebutuhan bisnis dengan ruang lingkup in/out, metrik sukses terukur (SLA <= 60 detik), dan matriks RACI.
2. [`02-FSD.md`](02-FSD.md) — Spesifikasi fungsional dengan skenario Gherkin (happy path, edge case batas kuota, error path saldo kurang), tabel keputusan biaya DMN, dan matriks hak akses.
3. [`03-ADR.md`](03-ADR.md) — Keputusan arsitektur format MADR 4.0.0 un-nested yang mencatat rasional pemilihan Transactional Outbox daripada 2PC.
4. [`04-Test-Plan.md`](04-Test-Plan.md) — Rencana pengujian tailored ISO/IEC/IEEE 29119 dengan pengujian kontrak konsumen (Pact) dan gate CI fail-closed.
5. [`05-Laporan-Harian.md`](05-Laporan-Harian.md) — Pelaporan harian berbasis bukti nyata (PR ID, metrik DORA, status CI) tanpa status theater subyektif.
