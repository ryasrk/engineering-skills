> Sumber: NASA SWE-047, *Traceability Data* — https://swehb.msfc.nasa.gov/pages/viewpage.action?pageId=91030146
> Catatan: Dipakai saat menyusun keterlacakan dua arah dari BRD ke acceptance criteria dan test case, termasuk saat menganalisis dampak change request.
# 15. Matriks keterlacakan (RTM dua arah)

**Arah mundur:** `Sumber BRD`. **Arah maju:** `AC` → `Test case` → `Kontrak`. Prinsip *bidirectional traceability*: NASA SWE-047 — https://swehb.msfc.nasa.gov/pages/viewpage.action?pageId=91030146 ; analisis dampak: IIBA *The Business Analysis Standard* — https://www.iiba.org/globalassets/business-analysis-resources/the-business-analysis-standard/files/the-business-analysis-standard-ja.pdf .

| ID FSD | Pernyataan perilaku | ← Sumber BRD | Aturan / constraint | → AC | → Test case ID | → Kontrak | Status | Versi | Cakupan balik |
|---|---|---|---|---|---|---|---|---|---|
| `{{FSD_FR_ID}}` | `{{PERNYATAAN}}` | `{{ID_BAGIAN_BRD}}` | `{{BR_ID}}` / `{{C_ID}}` | `{{AC_ID}}` | `{{TC_ID}}` | `{{IF_ID}}` | `{{STATUS}}` | `{{VERSI_FSD}}` | `{{HASIL_CAKUPAN_BALIK}}` |
| `{{FSD_NFR_ID}}` | `{{PERNYATAAN}}` | `{{ID_BAGIAN_BRD}}` | `{{NFR_ID}}` | `{{AC_ID}}` | `{{TC_ID}}` | `{{IF_ID}}` | `{{STATUS}}` | `{{VERSI_FSD}}` | `{{HASIL_CAKUPAN_BALIK}}` |
| `{{FSD_ORPHAN_ID}}` | `{{PERNYATAAN}}` | `—` | `—` | `—` | `—` | `—` | `DITOLAK` | `{{VERSI_FSD}}` | `GAP: {{KETERANGAN}}` |

| Pemeriksaan | Hasil | Tindakan |
|---|---|---|
| Setiap baris FSD memiliki `Sumber BRD` | `{{PILIHAN_YA_TIDAK}}` | `{{TINDAKAN}}` |
| Setiap `ID_BAGIAN_BRD` memiliki minimal satu baris FSD | `{{PILIHAN_YA_TIDAK}}` | `{{TINDAKAN}}` |
| Setiap baris FSD memiliki minimal satu `AC` dan `TC_ID` | `{{PILIHAN_YA_TIDAK}}` | `{{TINDAKAN}}` |
| Setiap `AC` memiliki kode keputusan yang cocok dengan §8 | `{{PILIHAN_YA_TIDAK}}` | `{{TINDAKAN}}` |
| Tidak ada `FSD_ORPHAN` yang masih `DISETUJUI` | `{{PILIHAN_YA_TIDAK}}` | `{{TINDAKAN}}` |

> Kolom `Test case ID` hanya berfungsi sebagai **pengenal keterlacakan**; strategi testing tidak dibahas di sini.
