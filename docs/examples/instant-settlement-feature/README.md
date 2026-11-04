# Contoh End-to-End: Fitur Pencairan Dana Instan (Instant Settlement)

Contoh nyata ini mendemonstrasikan bagaimana sebuah fitur rekayasa perangkat lunak mengalir secara terstruktur dan terhubung melalui ID stabil di setiap fase dokumentasi tanpa ada orphan ID (keterlacakan dua arah utuh):

```text
[BRD] BR-SETTLE-001..003 & KPI-SETTLE-01..02
  ↓
[FSD] FR-SETTLE-001..003 & AC-SETTLE-01..05 & RULE-FEE-01
  ↓
[ADR] ADR-0042 (Transactional Outbox & Idempotency Key)
  ↓
[Test Plan] TC-SETTLE-01..09 (Pact, k6, End-to-End SLA, Fail-Closed CI Gate)
  ↓
[Laporan Harian] Status Operasional Berbasis Bukti (PR #104..106, 0 Blocker, DoD Lolos)
```

## Matriks Keterlacakan (Bidirectional Traceability)

| Level | ID Item | Deskripsi | Ditautkan ke |
|---|---|---|---|
| Business (BRD) | `BR-SETTLE-001` | Pencairan 24/7 ≤ 60 detik | `FR-SETTLE-001`, `TC-SETTLE-01`, `TC-SETTLE-06` |
| Business (BRD) | `BR-SETTLE-002` | Pencegahan double-spending / debit atomik | `FR-SETTLE-002`, `ADR-0042`, `TC-SETTLE-04` |
| Business (BRD) | `BR-SETTLE-003` | Pemotongan biaya instan transparan | `FR-SETTLE-003`, `RULE-FEE-01`, `TC-SETTLE-05` |
| Business KPI | `KPI-SETTLE-01` | SLA End-to-end ≤ 60s (99.5%) | `TC-SETTLE-06` |
| Business KPI | `KPI-SETTLE-02` | Target TPV Rp 5 Miliar / hari | `TC-SETTLE-09` |
| Functional (FSD) | `FR-SETTLE-001` | Validasi & eksekusi transfer | `BR-SETTLE-001`, `AC-SETTLE-01..03` |
| Functional (FSD) | `FR-SETTLE-002` | Atomic locking & idempotency token | `BR-SETTLE-002`, `AC-SETTLE-04` |
| Functional (FSD) | `FR-SETTLE-003` | Kalkulasi biaya tier | `BR-SETTLE-003`, `AC-SETTLE-05`, `RULE-FEE-01` |
| Architecture | `ADR-0042` | Outbox Pattern & Idempotency | `FR-SETTLE-001`, `FR-SETTLE-002` |
| QA (Test Plan) | `TC-SETTLE-01..09` | Suite pengujian otomatis | Seluruh `FR-...` dan `KPI-...` teruji 100% |
| Delivery | PR #104, #105, #106 | Implementasi kode & kontrak | Memenuhi Definition of Done |

## Berkas Contoh

1. [`01-BRD.md`](01-BRD.md) — Dokumen kebutuhan bisnis dengan ruang lingkup in/out, KPI terukur (baseline, target, sumber pengukuran, review date), dan peran RACI konsisten.
2. [`02-FSD.md`](02-FSD.md) — Spesifikasi fungsional dengan skenario Gherkin (happy path, edge case batas kuota, error path saldo kurang, idempotency replay, kalkulasi fee), tabel keputusan biaya DMN (`RULE-FEE-01`), dan matriks RBAC.
3. [`03-ADR.md`](03-ADR.md) — Keputusan arsitektur format MADR 4.0.0 un-nested yang mencatat rasional pemilihan Transactional Outbox daripada 2PC.
4. [`04-Test-Plan.md`](04-Test-Plan.md) — Rencana pengujian tailored ISO/IEC/IEEE 29119 dengan pengujian kontrak konsumen (Pact), pengukuran SLA end-to-end, dan gate CI fail-closed.
5. [`05-Laporan-Harian.md`](05-Laporan-Harian.md) — Pelaporan harian berbasis bukti nyata (PR ID, metrik DORA, status CI) tanpa status theater subyektif.
