> Sumber: RFC 8594, The Sunset HTTP Header Field — https://www.rfc-editor.org/rfc/rfc8594.html
> Catatan: Dipakai saat menjadwalkan pengumuman deprecation, sunset, dan pengingat kepada konsumen API.
# Komunikasi ke Konsumen saat Deprecation dan Sunset

1. T+0: ADR + `support-policy.md` + halaman deprecation/sunset dipublikasikan; `Link` rel sudah aktif **sebelum** `Deprecation`.
2. T+0: CHANGELOG entri `Deprecated`, release notes, email/portal developer, dashboard per konsumen, dan migration guide `v2-to-v3.md` dengan contoh request/response.
3. T+0: `Deprecation` header dan `deprecated: true` pada OpenAPI; SDK V2 diberi compile/runtime warning; SDK V3 tersedia.
4. T+{{NOTICE_PERIOD}}: `Sunset` header dengan tanggal pasti; pengingat pada T−90/T−30/T−7 hari; daftar consumer yang masih memakai V2.
5. T+{{SUNSET_DATE}}: route dinonaktifkan sesuai kebijakan—pilih dan dokumentasikan `410 Gone` atau `404 Not Found`; RFC 8594 memberi kedua contoh itu dan menegaskan tidak menjanjikan bentuk respons. `[STANDAR]` [RFC 8594 §9](https://www.rfc-editor.org/rfc/rfc8594.html).
6. Setelah contract: arsipkan OAD, tandai ADR `superseded`, hapus adapter/flag/kolom lama, dan catat di CHANGELOG kategori `Removed`.
