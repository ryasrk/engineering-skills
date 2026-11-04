> Sumber: RFC 9457, Problem Details for HTTP APIs — https://www.rfc-editor.org/rfc/rfc9457.html
> Catatan: Dipakai saat mendokumentasikan contoh endpoint dan perubahan kontrak antar major version.
# Matriks Tiga Endpoint Versi

| Versi | Endpoint | Perubahan konkret | Status contoh |
|---|---|---|---|
| V1 | `GET /api/v1/orders/{{ORDER_ID}}` | `total: number` flat; error legacy | Deprecated + Sunset |
| V2 | `POST /api/v2/orders` dan `GET /api/v2/orders/{{ORDER_ID}}` | `total`→`amount{value,currency}`, tambah `status`; breaking terhadap V1 | Deprecated, migrasi ke V3 |
| V3 | `POST /api/v3/orders`, `GET /api/v3/orders/{{ORDER_ID}}`, `GET /api/v3/orders?cursor={{CURSOR}}` | Cursor pagination, `status` extensible, `application/problem+json` | Current |
