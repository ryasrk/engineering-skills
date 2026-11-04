# Test Plan — Instant Settlement Feature

> Mode Konformasi: Tailored Conformance terhadap ISO/IEC/IEEE 29119-3:2021
> Dokumen ID: `TP-SETTLE-001`
> QA Lead: Sarah Lestari

---

## 1. Test Basis & Traceability
- BRD Reference: `BRD-SETTLE-2026-01` (`BR-SETTLE-001`, `BR-SETTLE-002`)
- FSD Reference: `FSD-SETTLE-01` (`FR-SETTLE-001`, `AC-SETTLE-01` s/d `04`)
- Architecture Reference: `ADR-0042` (Outbox & Idempotency)

## 2. Test Cases Specification

| ID Test Case | Requirement ID | Jenis Uji | Prekondisi | Langkah & Input Uji | Hasil Diharapkan |
|---|---|---|---|---|---|
| `TC-SETTLE-01` | `FR-SETTLE-001` | Integration / API | Saldo merchant Rp 10jt, status verified | POST `/api/v1/settlements/instant` nominal Rp 5jt | HTTP 201, saldo locked Rp 5.007.500 |
| `TC-SETTLE-02` | `FR-SETTLE-001` | Contract (Pact) | Mock switching service aktif | Consumer-driven contract test untuk event outbox | Provider verification lolos (Pact `can-i-deploy`) |
| `TC-SETTLE-03` | `FR-SETTLE-002` | Idempotency | Transaksi pertama in-flight | Request kedua dengan `Idempotency-Key` sama dikirim | HTTP 409 atau HTTP 200 dengan payload sama; tidak ada debit kedua |
| `TC-SETTLE-04` | `KPI-SETTLE-01` | Performance (k6) | 100 VU concurrent | Load test 50 rps selama 10 menit | Latensi p95 <= 800ms, error rate 0.00% |

## 3. Exit Criteria & CI Quality Gates (Fail-Closed)
- [x] Unit test line coverage >= 85% untuk modul settlement core.
- [x] 100% pass rate untuk suite `TC-SETTLE-01` s/d `TC-SETTLE-04`.
- [x] Pact verification lolos tanpa breaking contract (`can-i-deploy --to-environment production`).
- [x] Zero blocker / critical defects aktif (Sev-1 = 0, Sev-2 = 0).
- [x] CI gate pipeline status: `gate` job must report `success` (fail-closed).
