> Sumber: adr/madr 4.0.0, "adr-template.md" — https://github.com/adr/madr/blob/4.0.0/template/adr-template.md
> Catatan: Dipakai setiap kali satu keputusan arsitektural signifikan perlu dicatat beserta rasional, alternatif, konsekuensi, dan statusnya.
---
id: {{ADR-0000}}
title: "{{JUDUL_SINGKAT_MASALAH_DAN_SOLUSI}}"
status: "{{proposed | accepted | rejected | deprecated | superseded by ADR-0000}}"
date: "{{YYYY-MM-DD}}"
decision-makers: "{{NAMA_1}}, {{NAMA_2}}"
consulted: "{{PAKAR_1}}, {{TIM_1}}"
informed: "{{TIM_2}}, {{STAKEHOLDER_1}}"
confidence: "{{high | medium | low}}"
supersedes: "{{ADR-0000 | none}}"
superseded-by: "{{ADR-0000 | none}}"
revisit-on: "{{YYYY-MM-DD | none}}"
---

# {{ADR-0000}}: {{JUDUL_SINGKAT_MASALAH_DAN_SOLUSI}}

## Context and Problem Statement
{{KONTEKS_2_SAMPAI_3_KALIMAT}}

Pertanyaan keputusan: Bagaimana {{KOMPONEN}} menyimpan {{DATA}} agar {{KUALITAS}} tercapai tanpa {{CONSTRAINT}}? Tautkan {{TAUTAN_ISSUE}}.

## Decision Drivers
- {{DRIVER_1}} — {{BUKTI_1}}
- {{DRIVER_2}} — {{BUKTI_2}}
- {{DRIVER_3}} — {{BUKTI_3}}

## Considered Options
- {{OPSI_1}}
- {{OPSI_2}}
- {{OPSI_3}}
- {{DO_NOTHING}}

## Decision Outcome
Chosen option: "{{OPSI_1}}", because {{JUSTIFIKASI}}.

### Consequences
- Good, because {{KONSEKUENSI_POSITIF_1}}
- Good, because {{KONSEKUENSI_POSITIF_2}}
- Bad, because {{KONSEKUENSI_NEGATIF_1}} (mitigasi: {{MITIGASI_1}})
- Neutral, because {{KONSEKUENSI_NETRAL_1}}

### Confirmation
Bagaimana kepatuhan diverifikasi: design review {{TAUTAN_REVIEW}}, pemeriksaan struktur/interface {{CARA_CEK_1}}, dan sinyal operasional {{SINYAL_1}}. Catat pemilik {{PERAN}} dan tanggal {{TANGGAL}}.

## Pros and Cons of the Options

### {{OPSI_1}}
{{DESKRIPSI_OPSI_1}} — bukti: {{TAUTAN_1}}
- Good, because {{ARGUMEN_A}}
- Good, because {{ARGUMEN_B}}
- Neutral, because {{ARGUMEN_C}}
- Bad, because {{ARGUMEN_D}}

### {{OPSI_2}}
{{DESKRIPSI_OPSI_2}} — bukti: {{TAUTAN_2}}
- Good, because {{ARGUMEN_A}}
- Neutral, because {{ARGUMEN_C}}
- Bad, because {{ARGUMEN_D}}

### {{DO_NOTHING}}
- Good, because {{TANPA_BIAYA_PERUBAHAN}}
- Bad, because {{RISIKO_JIKA_TIDAK_BERUBAH}}

## More Information
- Dasar evidence: {{BENCHMARK/INSIDEN/REGULASI}} — {{TAUTAN_EVIDENCE}}
- Kesepakatan tim dicatat pada: {{TAUTAN_RAPAT}}
- Terkait: {{DD-0000}}, {{ADR-0000}}, {{TAUTAN_DIAGRAM_C4}}
- Jika `confidence: low`, tinjau ulang pada {{REVISIT_ON}} dengan pemicu {{PIMICU_TINJAU}}
- Riwayat status: {{YYYY-MM-DD}} `proposed` → {{YYYY-MM-DD}} `accepted` → {{YYYY-MM-DD}} `superseded by ADR-0000`
