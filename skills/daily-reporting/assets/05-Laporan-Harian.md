> Sumber: Atlassian Team Playbook, "Weekly Project Updates" — https://www.atlassian.com/team-playbook/plays/weekly-project-updates ; GitLab Handbook, "Weekly Async Updates" — https://handbook.gitlab.com/handbook/engineering/ai/ai-coding/how-we-work/async-updates/ ; GitHub Docs, "About Projects" — https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects ; The 2020 Scrum Guide — https://scrumguides.org/scrum-guide.html
> Catatan: Pakai template ini untuk menyusun laporan harian tertulis bagi tim internal, engineering manager, manajemen, atau klien ketika hari itu ada deliverable, blocker/eskalasi, keputusan, atau perubahan scope, jadwal, dan risiko yang perlu dicatat.

# Laporan Harian — {{nama_proyek}} — {{tanggal_YYYY-MM-DD}}

| Field | Nilai |
| --- | --- |
| ID proyek / workspace | {{id_proyek}} |
| Periode laporan | {{periode_mulai}} s.d. {{periode_selesai}} (TZ {{zona_waktu}}) |
| Disusun oleh / owner laporan | {{nama_penyusun}} / {{kontak}} |
| Audiens & kanal | {{audiens: tim_internal \| EM \| manajemen \| klien}} — {{kanal}} |
| Status keseluruhan | {{On track \| At risk \| Off track}} — alasan: {{alasan_status}} |
| Sprint / milestone / Sprint Goal | {{sprint_id}} — {{sprint_goal}} |
| Target date & ETA | {{target_date}} / ETA {{eta}} (sumber: {{sumber_eta}}) |
| Tautan single source of truth | {{url_board_atau_project}} |
| Tautan laporan sebelumnya | {{url_laporan_sebelumnya}} |
| Versi template | {{versi_template}} |

## 1. TL;DR (maks. 3 kalimat)
{{ringkasan_eksekutif}}
Perubahan sejak laporan sebelumnya: {{delta_atau_tidak_ada_perubahan}}

## 2. Deliverable selesai (hanya yang memenuhi Definition of Done)
| Deliverable | Bukti (issue/PR/MR/CI run ID) | Status DoD | Dampak |
| --- | --- | --- | --- |
| {{deliverable_1}} | {{url_evidence_1}} | {{lulus \| belum}} | {{dampak_1}} |
| {{deliverable_2}} | {{url_evidence_2}} | {{lulus \| belum}} | {{dampak_2}} |

Catatan: item yang belum memenuhi Definition of Done dipindah ke bagian 3, **tidak** dihitung selesai.

## 3. Pekerjaan berjalan (WIP)
| Work item | Owner | Status | Mulai | Target | Bukti terakhir |
| --- | --- | --- | --- | --- | --- |
| {{issue_id_1}} — {{judul_1}} | {{owner_1}} | {{In Progress \| Review \| Blocked}} | {{tgl_mulai_1}} | {{tgl_target_1}} | {{url_pr_atau_commit_1}} |
| {{issue_id_2}} — {{judul_2}} | {{owner_2}} | {{In Progress \| Review \| Blocked}} | {{tgl_mulai_2}} | {{tgl_target_2}} | {{url_pr_atau_commit_2}} |

## 4. Blocker & eskalasi
| ID blocker | Deskripsi & dampak | Level | Owner | Dihubungi | SLA respons | Target selesai | Status tindak lanjut | Work item |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| {{blocker_id_1}} | {{deskripsi_blocker_1}} | {{L1_tim \| L2_EM_PO \| L3_manajemen_klien}} | {{owner_blocker_1}} | {{kontak_eskalasi_1}} | {{sla_L1_atau_nilai_kontrak}} | {{target_selesai_1}} | {{Terbuka \| Dalam penanganan \| Closed}} | {{url_issue_blocker_1}} |
| {{blocker_id_2}} | {{deskripsi_blocker_2}} | {{L1_tim \| L2_EM_PO \| L3_manajemen_klien}} | {{owner_blocker_2}} | {{kontak_eskalasi_2}} | {{sla_L2_atau_nilai_kontrak}} | {{target_selesai_2}} | {{Terbuka \| Dalam penanganan \| Closed}} | {{url_issue_blocker_2}} |

Flag blocker lebih awal; eskalasi naik satu level bila `{{batas_respons}}` terlampaui. SLA di atas adalah **kebijakan internal/kontrak**, bukan angka dari standar.

## 5. Perubahan scope, jadwal, dan risiko
| Jenis | Sebelum | Sesudah | Alasan / pemicu | Disetujui oleh | Tanggal keputusan | Bukti |
| --- | --- | --- | --- | --- | --- | --- |
| {{scope \| jadwal \| risiko}} | {{nilai_lama}} | {{nilai_baru}} | {{alasan_perubahan}} | {{approver}} | {{tgl_keputusan}} | {{url_change_atau_risk}} |

Daftar risiko aktif: {{risiko_id_1}} — {{dampak_1}} — mitigasi {{mitigasi_1}} — owner {{owner_risiko_1}}.

## 6. Metrik (event-derived, bukan persentase subyektif)
| Metrik | Nilai | Periode / snapshot | Sumber data | Catatan |
| --- | --- | --- | --- | --- |
| Item Done / total item sprint | {{done_count}}/{{total_count}} | {{periode_snapshot}} | {{url_board}} | dihitung dari status DoD |
| Burndown (sisa kerja) | {{sisa_kerja}} | {{tgl_snapshot}} | {{url_burndown}} | forecast, bukan kepastian |
| Velocity iterasi | {{velocity}} | {{iterasi}} | {{url_insights}} | untuk perencanaan internal |
| Change lead time | {{lead_time}} | {{periode_snapshot}} | {{url_dora}} | DORA, per aplikasi/service |
| Deployment frequency | {{deploy_freq}} | {{periode_snapshot}} | {{url_dora}} | DORA |
| Failed deployment recovery time | {{recovery_time}} | {{periode_snapshot}} | {{url_dora}} | DORA (model 2026) |
| Change fail rate | {{change_fail_rate}} | {{periode_snapshot}} | {{url_dora}} | DORA |
| Deployment rework rate | {{rework_rate}} | {{periode_snapshot}} | {{url_dora}} | DORA (model 2026) |
| Defect baru / tertutup | {{defect_baru}}/{{defect_tertutup}} | {{periode_snapshot}} | {{url_issue_tracker}} | label `bug` / `triage` |
| ETA | {{eta}} | {{tgl_snapshot}} | {{sumber_eta}} | sebutkan asumsi: {{asumsi_eta}} |

Larangan: jangan menulis "progres {{persentase}}%" tanpa daftar work item `Done` yang dapat diverifikasi; jangan menjadikan metrik di atas sebagai target individu.

## 7. Keputusan yang dibutuhkan
| ID | Keputusan | Owner keputusan | Respond by | Opsi yang dipertimbangkan | Dampak bila tertunda | Status |
| --- | --- | --- | --- | --- | --- | --- |
| {{decision_id_1}} | {{pertanyaan_keputusan_1}} | {{decision_owner_1}} | {{respond_by_1}} | {{opsi_1}} | {{dampak_tunda_1}} | {{Menunggu \| Diputuskan}} |

Keputusan yang diambil dalam rapat sinkron wajib ditutup tertulis di work item terkait dalam {{batas_dokumentasi_keputusan}} (default internal: 24 jam).

## 8. Rencana hari berikutnya
1. {{rencana_1}} — owner {{owner_rencana_1}} — work item {{issue_rencana_1}}
2. {{rencana_2}} — owner {{owner_rencana_2}} — work item {{issue_rencana_2}}
3. {{rencana_3}} — owner {{owner_rencana_3}} — work item {{issue_rencana_3}}

## 9. Catatan audiens (isi sesuai kanal; hapus baris yang tidak relevan)
- Tim internal: detail teknis, PR/MR ID, blocker per owner — **boleh**.
- Engineering manager: kapasitas, hambatan sistemik, confidence, bantuan yang dibutuhkan — **boleh**.
- Manajemen: status RAG, tren milestone/ETA, risiko & dampak jadwal/biaya — **boleh**.
- Klien: deliverable `Done`, perubahan yang sudah disetujui, risiko berdampak kontrak — **boleh**.
- Untuk klien: evaluasi kinerja individu, isi 1:1, data pribadi/kategori sensitif, secret/kredensial, perbandingan metrik antar tim — **TIDAK boleh**.
- Kebijakan privasi & retensi: {{kebijakan_privasi}}; masa retensi arsip {{masa_retensi}}; dasar hukum/kontrak {{dasar_retensi}}.

## 10. Jejak audit
| Waktu (TZ) | Aktor | Aksi | Objek | Bukti |
| --- | --- | --- | --- | --- |
| {{timestamp_1}} | {{aktor_1}} | {{aksi_1}} | {{objek_1}} | {{url_diff_atau_comment_1}} |
| {{timestamp_2}} | {{aktor_2}} | {{aksi_2}} | {{objek_2}} | {{url_diff_atau_comment_2}} |

Ditutup oleh: {{nama_penyusun}} — {{timestamp_tutup}} — tautan arsip: {{url_arsip}}
