# Test Plan — Instant Settlement Feature

> Mode Konformasi: Tailored Conformance terhadap ISO/IEC/IEEE 29119-3:2021
> Dokumen ID: `TP-SETTLE-001`
> QA Lead: Sarah Lestari

---

## 1. Test Basis & Traceability
- BRD Reference: `BRD-SETTLE-2026-01` (`BR-SETTLE-001`, `BR-SETTLE-002`, `BR-SETTLE-003`, `KPI-SETTLE-01`, `KPI-SETTLE-02`)
- FSD Reference: `FSD-SETTLE-01` (`FR-SETTLE-001`, `FR-SETTLE-002`, `FR-SETTLE-003`, `AC-SETTLE-01` s/d `05`, `RULE-FEE-01`)
- Architecture Reference: `ADR-0042` (Transactional Outbox & Idempotency Key)

## 2. Test Cases Specification

| ID Test Case | Requirement ID | Jenis Uji | Prekondisi | Langkah & Input Uji | Hasil Diharapkan |
|---|---|---|---|---|---|
| `TC-SETTLE-01` | `FR-SETTLE-001` / `AC-SETTLE-01` | Integration / API | Saldo merchant Rp 10jt, status verified | POST `/api/v1/settlements/instant` nominal Rp 5jt | HTTP 201 Created, status PROCESSING, saldo locked Rp 5.007.500 |
| `TC-SETTLE-02` | `FR-SETTLE-001` / `AC-SETTLE-02` | Boundary / Edge | Kuota sisa penarikan Rp 1jt | POST penarikan tepat Rp 1.000.000 | HTTP 201 Created, kuota harian tersisa menjadi Rp 0 |
| `TC-SETTLE-03` | `FR-SETTLE-001` / `AC-SETTLE-03` | Negative / Error | Saldo tertagih Rp 2jt | POST penarikan nominal Rp 3.000.000 | HTTP 422 Unprocessable Entity, error code `INSUFFICIENT_SETTLED_BALANCE` |
| `TC-SETTLE-04` | `FR-SETTLE-002` / `AC-SETTLE-04` | Idempotency | Request pertama sukses diproses | Mengirim request ulang dengan `Idempotency-Key` sama | HTTP 200 OK deterministik, header `Idempotent-Replayed: true`, payload identik, tanpa debit ganda |
| `TC-SETTLE-05` | `FR-SETTLE-003` / `AC-SETTLE-05` | Business Rule | Merchant UMKM Standar | Penarikan Rp 2.000.000 | Biaya dipotong tepat Rp 3.000 (`RULE-FEE-01`) |
| `TC-SETTLE-06` | `KPI-SETTLE-01` | E2E SLA Timer | Gateway BI-FAST aktif | Mengukur durasi dari POST request hingga Webhook `SETTLEMENT.COMPLETED` | Durasi ≤ 60 detik pada 99.5% dari 1.000 transaksi uji |
| `TC-SETTLE-07` | Non-Functional | Performance (k6) | 100 VU concurrent | Load test 50 rps selama 10 menit pada endpoint inisiasi | Latensi API p95 ≤ 800ms, error rate 0.00% |
| `TC-SETTLE-08` | `FR-SETTLE-001` | Contract (Pact) | Mock switching service aktif | Consumer-driven contract test untuk event outbox transfer | Provider verification lolos (Pact `can-i-deploy`) |
| `TC-SETTLE-09` | `KPI-SETTLE-02` | Reporting / Data | Data transaksi harian terisi | Verifikasi query agregasi analytics data warehouse | Agregasi volume harian terakumulasi akurat tanpa transaksi duplicate |

## 3. Exit Criteria & CI Quality Gates (Fail-Closed)
- [x] Unit test line coverage >= 85% untuk modul settlement core.
- [x] 100% pass rate untuk suite `TC-SETTLE-01` s/d `TC-SETTLE-09`.
- [x] Pact verification lolos tanpa breaking contract (`can-i-deploy --to-environment production`).
- [x] Zero blocker / critical defects aktif (Sev-1 = 0, Sev-2 = 0).
- [x] CI gate pipeline status: `gate` job must report `success` (fail-closed).
