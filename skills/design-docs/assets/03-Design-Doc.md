> Sumber: Kubernetes Enhancements, "KEP-NNNN template README" — https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md
> Catatan: Dipakai saat menyusun design doc/RFC untuk perubahan arsitektur yang perlu disetujui lintas tim sebelum implementasi.
# {{JUDUL_DESAIN}} — Design Doc / RFC

| Metadata | Nilai |
| --- | --- |
| ID | {{DD-0000}} |
| Status | {{Draft \| Proposed \| Accepted \| Superseded by DD-0000}} |
| Versi & tanggal | {{v0.1}} — {{YYYY-MM-DD}} |
| Pemilik | {{NAMA_PERAN}} |
| Reviewer wajib | {{ARSITEK}}, {{SECURITY}}, {{SRE}}, {{DESAINER_UX}}, {{DATA_OWNER}} |
| Target keputusan | {{TANGGAL_KEPUTUSAN}} |
| Referensi kebutuhan | {{TAUTAN_REQUIREMENT}} |
| Standar yang dipakai | {{ISO/IEC/IEEE 42010:2022}}, {{WCAG 2.2 AA}}, {{LAINNYA}} |

## 1. Ringkasan
{{Satu paragraf: apa yang berubah, untuk siapa, dan mengapa pembaca harus menyetujuinya.}}

## 2. Konteks & motivasi
{{Keadaan saat ini, data/insiden yang memicu, dan dampak bila tidak ada perubahan. Tulis constraints, bukan solusi, agar alternatif lain tetap bisa diusulkan.}}

## 3. Tujuan, non-goals, dan kriteria sukses
- Goals: {{TUJUAN_1}}, {{TUJUAN_2}}, {{TUJUAN_3}}
- Non-goals: {{DI_LUAR_RUANG_LINGKUP_1}}, {{DI_LUAR_RUANG_LINGKUP_2}}
- Kriteria sukses terukur: {{METRIK_1}} dari {{BASELINE_1}} menjadi {{TARGET_1}} pada {{WAKTU_1}}; {{METRIK_2}} ≤ {{AMBANG_2}}

## 4. Stakeholder, concern, dan quality goals
| Stakeholder | Concern | Quality goal (top 3–5) | Skenario terukur |
| --- | --- | --- | --- |
| {{PERAN_1}} | {{CONCERN_1}} | {{KUALITAS_1}} | {{KONDISI_1}} → {{RESPON_1}} dalam {{BATAS_1}} |
| {{PERAN_2}} | {{CONCERN_2}} | {{KUALITAS_2}} | {{KONDISI_2}} → {{RESPON_2}} dalam {{BATAS_2}} |

## 5. Constraints & asumsi
- Teknis: {{CONSTRAINT_TEKNIS}}
- Organisasi/regulasi: {{CONSTRAINT_REGULASI}}
- Asumsi yang bila salah membatalkan desain: {{ASUMSI_KRITIS}}
- Cara memvalidasi asumsi: {{CARA_VALIDASI}}

## 6. Keputusan desain
| ID | Keputusan | Alasan utama | Concern yang dijawab | ADR |
| --- | --- | --- | --- | --- |
| {{D-01}} | {{KEPUTUSAN_1}} | {{ALASAN_1}} | {{CONCERN_1}} | {{ADR-0000}} |
| {{D-02}} | {{KEPUTUSAN_2}} | {{ALASAN_2}} | {{CONCERN_2}} | {{ADR-0000}} |

## 7. Alternatif yang dipertimbangkan dan ditolak
| Opsi | Kelebihan | Kekurangan | Alasan penolakan | Bukti |
| --- | --- | --- | --- | --- |
| {{OPSI_A}} | {{PRO_A}} | {{KONTRA_A}} | {{TOLAK_A}} | {{TAUTAN_BENCHMARK_A}} |
| {{OPSI_B}} | {{PRO_B}} | {{KONTRA_B}} | {{TOLAK_B}} | {{TAUTAN_BENCHMARK_B}} |
| Do nothing | {{PRO_NOL}} | {{KONTRA_NOL}} | {{TOLAK_NOL}} | {{DATA_DAMPAK}} |

## 8. Desain struktural (HLD → LLD ringkas)
- System Context (C4 L1): {{AKTOR_1}} → {{SISTEM_KITA}} → {{SISTEM_EKSTERNAL_1}}
- Container (C4 L2): {{KONTAINER_1}} ({{TEKNOLOGI_1}}), {{KONTAINER_2}} ({{TEKNOLOGI_2}}); protokol {{PROTOKOL_1}}
- Component (C4 L3, hanya yang berisiko/kompleks): {{KOMPONEN_1}} → {{TANGGUNG_JAWAB_1}}, interface {{INTERFACE_1}}
- Batasan zoom: {{BAGIAN_YANG_TIDAK_DIGAMBAR_L4_DAN_ALASANNYA}}
- Diagram: {{TAUTAN_DIAGRAM_C4}}; notasi {{NOTASI}}; pemilik diagram {{PERAN}}; terakhir diverifikasi {{TANGGAL}}

## 9. Model perilaku & data
- Skenario runtime utama: {{USE_CASE_1}} — {{TAUTAN_SEQUENCE_DIAGRAM}}
- Skenario error/exception: {{FAILURE_1}} → deteksi {{SINYAL_1}} → mitigasi {{MITIGASI_1}}
- State machine: {{ENTITAS_1}}: {{STATE_A}} → {{STATE_B}} → {{STATE_C}}
- Model data: entitas {{ENTITAS_1}}({{ATRIBUT_1}}, {{KUNCI_1}}) berelasi {{KARDINALITAS}} dengan {{ENTITAS_2}}; {{TAUTAN_ER_DIAGRAM}}
- Invariants: {{INVARIANT_1}}; kehilangan data yang tidak boleh terjadi: {{DATA_KRITIS}}

## 10. Crosscutting concepts
{{Konsep bersama yang dipakai banyak blok: format log/correlation id, autentikasi-antar-komponen, strategi retry/idempotency, konvensi error. Pilih hanya yang paling dibutuhkan.}}

## 11. Keamanan & privacy (STRIDE)
| Kategori | Ancaman pada desain ini | Kontrol | Pemilik | Status |
| --- | --- | --- | --- | --- |
| Spoofing | {{ANCAMAN_S}} | {{KONTROL_S}} | {{PERAN_S}} | {{OPEN/MITIGATED}} |
| Tampering | {{ANCAMAN_T}} | {{KONTROL_T}} | {{PERAN_T}} | {{OPEN/MITIGATED}} |
| Repudiation | {{ANCAMAN_R}} | {{KONTROL_R}} | {{PERAN_R}} | {{OPEN/MITIGATED}} |
| Information Disclosure | {{ANCAMAN_I}} | {{KONTROL_I}} | {{PERAN_I}} | {{OPEN/MITIGATED}} |
| Denial of Service | {{ANCAMAN_D}} | {{KONTROL_D}} | {{PERAN_D}} | {{OPEN/MITIGATED}} |
| Elevation of Privilege | {{ANCAMAN_E}} | {{KONTROL_E}} | {{PERAN_E}} | {{OPEN/MITIGATED}} |
- Data pribadi diproses: {{KATEGORI_DATA}}; dasar pemrosesan {{DASAR_HUKUM}}; retensi {{RETENSI}}

## 12. Observability & operability
- SLI: {{SLI_1}}, {{SLI_2}}; SLO: {{SLO_1}} ({{JENDELA_1}})
- Log/telemetri: {{SIGNAL_1}}; correlation id {{CORRELATION_ID}}; dashboard {{TAUTAN_DASHBOARD}}
- Cara operator tahu fitur aktif & sehat: {{CARA_OPERATOR_1}}
- Failure mode terdokumentasi: {{FAILURE_1}} → deteksi {{DETEKSI_1}} → diagnosa {{DIAGNOSA_1}} → mitigasi {{MITIGASI_1}}
- Troubleshooting/playbook: {{TAUTAN_PLAYBOOK}}

## 13. Rencana migrasi & kompatibilitas data
- State lama: {{SKEMA_LAMA}}; state baru: {{SKEMA_BARU}}
- Urutan transformasi: {{TAHAP_1}} → {{TAHAP_2}} → {{TAHAP_3}}
- Backfill: {{ESTIMASI_VOLUME}} dalam {{JENDELA_WAKTU}}; estimasi dampak beban {{DAMPAK_BEBAN}}
- Kompatibilitas konsumen data & perilaku: {{KONSUMEN_1}} tetap membaca {{KONTRAK_1}}; validasi {{CARA_VALIDASI_KOMPATIBILITAS}}
- Rekonsiliasi & verifikasi integritas: {{CHECKSUM/COUNT_QUERY}}; ambang gagal {{AMBANG_GAGAL}}
- Rencana pemulihan state bila transformasi gagal: {{PEMULIHAN_STATE}}

## 14. Rollout, rollback, dan dependensi
- Urutan aktivasi: {{GELOMBANG_1}} → {{GELOMBANG_2}} → {{GELOMBANG_3}}; kriteria lanjut {{KRITERIA_LANJUT}}
- Cara menonaktifkan: {{MEKANISME_DISABLE}}; apakah bisa dinonaktifkan setelah aktif: {{YA/TIDAK + KONSEKUENSI}}
- Sinyal yang memicu rollback: {{METRIK_ROLLBACK_1}} > {{AMBANG_1}} selama {{DURASI_1}}
- Dampak rollback pada beban kerja berjalan: {{DAMPAK_ROLLBACK}}; jalur pulih {{AKTIFKAN_KEMBALI}}
- Dependensi eksternal: {{DEP_1}} — dampak outage {{OUTAGE_1}}, dampak degradasi {{DEGRADASI_1}}
- Perkiraan biaya: {{BIAYA_BULANAN}} (komponen {{KOMPONEN_BIAYA}}); trade-off yang disengaja {{TRADEOFF_BIAYA}}

## 15. Risiko, technical debt, dan keputusan tertunda
| Risiko/utang | Probabilitas | Dampak | Mitigasi/rencana bayar | Pemilik |
| --- | --- | --- | --- | --- |
| {{RISIKO_1}} | {{P1}} | {{D1}} | {{MITIGASI_1}} | {{PERAN_1}} |
- Open questions: {{PERTANYAAN_1}} (penentu {{PERAN_1}}, batas {{TANGGAL_1}})
- Future possibilities yang sengaja di luar ruang lingkup: {{IDE_1}}

## 16. Definisi selesai desain (DoD)
- [ ] Goals/non-goals, alternatif ditolak, dan ADR tertaut — {{BUKTI_1}}
- [ ] Diagram C4 + sequence/ER berversi dan bertanggal pemilik — {{BUKTI_2}}
- [ ] STRIDE lengkap dengan pemilik kontrol — {{BUKTI_3}}
- [ ] SLI/SLO, sinyal rollback, dan playbook disepakati SRE — {{BUKTI_4}}
- [ ] Rencana migrasi punya rekonsiliasi & pemulihan state — {{BUKTI_5}}
- [ ] Kriteria WCAG 2.2 AA + `prefers-reduced-motion` diverifikasi pada semua variasi responsif — {{BUKTI_6}}
- [ ] Estimasi biaya dan trade-off disetujui — {{BUKTI_7}}

## 17. Riwayat keputusan
| Tanggal | Versi | Perubahan | Penyetuju |
| --- | --- | --- | --- |
| {{YYYY-MM-DD}} | {{v0.1}} | {{DRAFT_AWAL}} | {{PERAN}} |
