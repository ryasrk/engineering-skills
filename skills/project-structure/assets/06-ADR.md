> Sumber: MADR 4.0.0, Markdown Architectural Decision Records — https://adr.github.io/madr/
> Catatan: Dipakai setiap kali tim mencatat keputusan arsitektural atau tata kelola baru, termasuk migrasi arsitektur dan versioning API.
---
id: {{ADR-0000}}
title: "{{JUDUL_SINGKAT_MASALAH_DAN_SOLUSI}}"
status: "{{STATUS: proposed | accepted | rejected | deprecated | superseded}}"
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

- Nomor: {{ADR-0000}}
- Status: {{STATUS: proposed | accepted | rejected | deprecated | superseded}}
- Superseded by: {{SUPERSEDED_BY_ADR_NUMBER_OR_NONE}}
- Tanggal: {{YYYY-MM-DD}}
- Decision makers: {{DAFTAR_PIHAK}}
- Consulted: {{DAFTAR_PIHAK}}
- Informed: {{DAFTAR_PIHAK}}
- Pemilik: {{TIM_PEMILIK}}
- Terkait: {{TAUTAN_ISSUE}} · {{TAUTAN_CHANGELOG}} · {{TAUTAN_OAD}}

## Context and Problem Statement
{{MASALAH_DAN_KONTEKS_MAKSIMAL_TIGA_KALIMAT}}. Pertanyaan keputusan: {{PERTANYAAN_KEPUTUSAN}}?

## Decision Drivers
- {{DRIVER_1}} — {{BUKTI_1}}
- {{DRIVER_2}} — {{BUKTI_2}}
- {{DRIVER_3}} — {{BUKTI_3}}

## Considered Options
- {{OPSI_1}}
- {{OPSI_2}}
- {{OPSI_3}}

## Decision Outcome
Chosen option: "{{OPSI_TERPILIH}}", karena {{ALASAN_DAN_BUKTI}}. Keputusan ini berlaku untuk {{RUANG_LINGKUP}} sejak {{TANGGAL_EFEKTIF}}.

### Consequences
- Good, because {{KONSEKUENSI_POSITIF}}
- Bad, because {{KONSEKUENSI_NEGATIF}}
- Neutral, because {{KONSEKUENSI_NETRAL}}

### Confirmation
{{CARA_VERIFIKASI: code review, architecture test, contract test, atau audit}}. Bukti: {{TAUTAN_CI_ATAU_REVIEW}}.

## Pros and Cons of the Options

### {{OPSI_1}}
- Good, because {{ARGUMEN_POSITIF}}
- Bad, because {{ARGUMEN_NEGATIF}}

### {{OPSI_2}}
- Good, because {{ARGUMEN_POSITIF}}
- Bad, because {{ARGUMEN_NEGATIF}}

### {{OPSI_3}}
- Good, because {{ARGUMEN_POSITIF}}
- Bad, because {{ARGUMEN_NEGATIF}}

## More Information
- Sumber [STANDAR/VENDOR/RESMI/INDUSTRI]: {{NAMA_DOKUMEN}} — {{URL_LENGKAP}}
- Ditinjau kembali pada: {{TANGGAL_TINJAUAN_ATAU_NONE}}
