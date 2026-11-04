# Business Requirements Document (BRD) — Pencairan Dana Instan (Instant Settlement)

- Inisiatif: Instant Settlement Service
- Versi: 1.0 (Baselined)
- Pemilik Bisnis: Head of Merchant Payments (Rina W.)
- Dokumen ID: `BRD-SETTLE-2026-01`

---

## 1. Ringkasan Eksekutif
Fitur Pencairan Dana Instan memungkinkan mitra merchant mencairkan dana hasil penjualan (settlement balance) secara langsung ke rekening bank dalam waktu kurang dari 60 detik tanpa harus menunggu siklus batch harian (T+1). Inisiatif ini dirancang untuk meningkatkan retensi mitra aktif sebesar 18% dan volume transaksi (TPV) sebesar 25%.

## 2. Tujuan Bisnis & Nilai
- Mengeliminasi kendala likuiditas harian bagi mitra merchant UMKM.
- Menciptakan lini pendapatan baru melalui biaya layanan transaksi instan (0.15% per transaksi).

## 3. Ruang Lingkup
- **In Scope:**
  - Penarikan saldo tertagih (settled funds) hingga batas Rp 50.000.000/hari per merchant.
  - Integrasi BI-FAST dan realtime switching partner.
  - Notifikasi instan via Webhook dan Push Notification.
- **Out of Scope:**
  - Pencairan dana transaksi kartu kredit yang masih dalam status dispute/chargeback.
  - Pembayaran lintas negara (cross-border remittance).

## 4. Kebutuhan Bisnis (Business Requirements)

| ID | Pernyataan Kebutuhan Bisnis | Prioritas | Kriteria Penerimaan Bisnis |
|---|---|---|---|
| `BR-SETTLE-001` | Merchant terverifikasi dapat mencairkan saldo kapan saja (24/7) ke rekening terdaftar. | High | Dana masuk rekening tujuan dalam ≤ 60 detik untuk 99.5% transaksi sukses. |
| `BR-SETTLE-002` | Sistem memotong saldo ledger secara atomik untuk mencegah *double-spending* atau cerukan. | High | Saldo langsung dikunci saat request diterima dan didebet setelah ACK switching. |
| `BR-SETTLE-003` | Skema biaya instan dipotong langsung dari nilai pencairan secara transparan. | Medium | Biaya admin tercatat transparan di invoice dan mutasi rekening sesuai aturan tier. |

## 5. Metrik Sukses (KPI)

| ID | Deskripsi Metrik | Baseline | Target | Sumber Pengukuran | Tanggal Review |
|---|---|---|---|---|---|
| `KPI-SETTLE-01` | Waktu pencairan end-to-end (initiation hingga bank ACK) | T+1 (24 jam) | ≤ 60 detik (SLA 99.5%) | Telemetri Webhook Switching & Ledger Timer | 2026-12-01 |
| `KPI-SETTLE-02` | Volume pencairan instan harian | Rp 0 (fitur baru) | Rp 5 Miliar / hari dalam 3 bulan | Data Warehouse Ledger Analytics | 2027-02-01 |

## 6. Stakeholder & RACI
- **Accountable:** Head of Merchant Payments (Rina W.)
- **Responsible:** Tech Lead (Budi S.), Product Manager (Dimas A.)
- **Consulted:** Head of Compliance, Head of Risk & Fraud
- **Informed:** Customer Support, Finance Operations
