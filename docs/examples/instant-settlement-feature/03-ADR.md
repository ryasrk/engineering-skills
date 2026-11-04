---
id: ADR-0042
title: "Penerapan Transactional Outbox dan Idempotency Key untuk Settlement Instan"
status: "accepted"
date: "2026-11-04"
decision-makers: "Budi Santoso (Tech Lead), Andi Pratama (Principal Architect)"
consulted: "Rina W. (Product), Tim Infra"
informed: "Seluruh Tim Engineering Backend"
confidence: "high"
supersedes: "none"
superseded-by: "none"
revisit-on: "none"
---

# ADR-0042: Penerapan Transactional Outbox dan Idempotency Key untuk Settlement Instan

## Context and Problem Statement
Pencairan dana instan (`FR-SETTLE-001`) memerlukan pemotongan saldo di database lokal PostgreSQL dan pemanggilan API bank mitra eksternal (BI-FAST). Jika transfer bank gagal setelah saldo lokal dipotong (atau terjadi network partition saat database commit), data akan inkonsisten. Bagaimana menjamin atomisitas dan konsistensi saldo tanpa menggunakan distributed transaction 2PC (Two-Phase Commit) yang lambat?

## Decision Drivers
- Konsistensi finansial mutlak (nol toleransi double-spend atau saldo hilang).
- Latensi pemrosesan p99 harus di bawah 1.5 detik untuk locking saldo.
- Tahan terhadap kegagalan jaringan atau timeout dari switching gateway bank.

## Considered Options
- **Opsi 1:** Transactional Outbox Pattern + Debezium CDC / Message Relay ke Kafka.
- **Opsi 2:** Dual-write langsung dari API handler ke DB dan Bank API secara sekuensial.
- **Opsi 3:** Two-Phase Commit (2PC) / XA Transaction antar database dan payment gateway.

## Decision Outcome
Chosen option: **"Opsi 1 (Transactional Outbox Pattern + Idempotency Key)"**, karena menjamin atomisitas mutlak antara pencatatan transaksi ledger lokal dan pengiriman event transfer ke payment gateway.

### Consequences
- Good: Database transaction commit mencakup debit saldo dan penyimpanan event di tabel `outbox` secara atomik dalam satu ACID transaction lokal.
- Good: Idempotency Key mencegah pemotongan ganda saat klien melakukan network retry.
- Bad: Membutuhkan background relay worker (asynchronous publisher) yang menambah komponen pemeliharaan.
- Neutral: Konfirmasi transfer bank ditangani secara eventual consistent melalui webhook callback.

### Confirmation
Diverifikasi melalui:
1. Automated contract test (Pact) untuk idempotent request handling.
2. Chaos engineering test (network partition injection saat transfer bank berlangsung).
