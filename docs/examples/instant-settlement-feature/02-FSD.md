# Functional Specification Document (FSD) — Instant Settlement Engine

- Referensi BRD: `BRD-SETTLE-2026-01`
- Versi: 1.0 (Approved)
- Dokumen ID: `FSD-SETTLE-01`
- Tech Lead: Budi Santoso

---

## 1. Keterlacakan Kebutuhan Fungsional (RTM Slice)

| ID Fungsional | Sumber BRD | Deskripsi Perilaku Sistem | Kriteria Penerimaan (AC) | ID Test Case |
|---|---|---|---|---|
| `FR-SETTLE-001` | `BR-SETTLE-001` | Validasi kelayakan merchant, ketersediaan saldo, dan eksekusi transfer instan. | `AC-SETTLE-01`, `AC-SETTLE-02`, `AC-SETTLE-03` | `TC-SETTLE-01`, `TC-SETTLE-02` |
| `FR-SETTLE-002` | `BR-SETTLE-002` | Atomic locking saldo dan idempotency token handling. | `AC-SETTLE-04` | `TC-SETTLE-03` |

## 2. Kriteria Penerimaan Gherkin (Given / When / Then)

### Skenario 1: Happy Path (Pencairan Berhasil)
```gherkin
Scenario: Pencairan saldo instan dalam batas harian berhasil
  Given merchant "MERCH-001" memiliki status "VERIFIED" dan KYC tingkat 2
  And saldo tertagih (settled balance) adalah Rp 10.000.000
  When merchant mengirim request POST /api/v1/settlements/instant dengan nominal Rp 5.000.000
  Then sistem merespons HTTP 201 Created dengan status "PROCESSING"
  And saldo merchant langsung dikunci sebesar Rp 5.007.500 (termasuk biaya layanan Rp 7.500)
  And webhook callback "SETTLEMENT.COMPLETED" dikirim ke merchant dalam <= 60 detik
```

### Skenario 2: Edge Case (Pencairan Mendekati Batas Harian)
```gherkin
Scenario: Pencairan tepat pada sisa limit harian
  Given merchant memiliki sisa kuota penarikan harian Rp 1.000.000
  When merchant mengajukan pencairan nominal Rp 1.000.000
  Then transaksi diizinkan dan sisa kuota harian berubah menjadi Rp 0
```

### Skenario 3: Error Path (Saldo Tidak Mencukupi)
```gherkin
Scenario: Pencairan ditolak karena saldo tertagih kurang dari nominal penarikan
  Given merchant memiliki saldo tertagih Rp 2.000.000
  When merchant mengajukan pencairan nominal Rp 3.000.000
  Then sistem merespons HTTP 422 Unprocessable Entity
  And payload error memuat code "INSUFFICIENT_SETTLED_BALANCE"
  And tidak ada saldo yang dikunci atau didebet
```

## 3. Decision Table: Perhitungan Biaya Layanan

| Level Merchant | Nominal Penarikan | Jam Transaksi | Persentase Biaya | Biaya Minimum | Output Biaya Layanan |
|---|---|---|---|---|---|
| UMKM Standar | < Rp 10.000.000 | Any | 0.15% | Rp 2.500 | max(Nominal * 0.15%, Rp 2.500) |
| UMKM Standar | >= Rp 10.000.000 | Any | 0.10% | Rp 5.000 | max(Nominal * 0.10%, Rp 5.000) |
| Enterprise Tier | Any | Any | 0.05% | Rp 1.500 | max(Nominal * 0.05%, Rp 1.500) |
| *Default Fallback* | Any | Any | 0.15% | Rp 2.500 | max(Nominal * 0.15%, Rp 2.500) |

## 4. Matriks Otorisasi (RBAC)

| Peran Pengguna | Inisiasi Settlement | Approval Manual (> Rp 25jt) | Lihat Riwayat | Retry Transaksi Gagal |
|---|---|---|---|---|
| Merchant Owner | Ya | Tidak (otomatis) | Ya | Tidak |
| Merchant Finance | Ya | Tidak (otomatis) | Ya | Tidak |
| Ops Risk Officer | Tidak | Ya | Ya | Ya |
