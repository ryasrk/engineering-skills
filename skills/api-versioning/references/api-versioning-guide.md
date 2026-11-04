## 7. Skema API versioning zero downtime: V1, V2, V3 di-embed pada API

> Template terkait: `../assets/06-OpenAPI-Multi-Versi.md`, `../assets/06-OpenAPI-Multi-Versi-V1.md`, `../assets/06-OpenAPI-Multi-Versi-V2.md`, `../assets/06-OpenAPI-Multi-Versi-V3.md`, `../assets/06-Matriks-Endpoint-Versi.md`, `../assets/06-Routing-Gateway-Nginx.md`, `../assets/06-Runbook-Expand-Contract.md`, `../assets/06-Timeline-Migrasi-V1-V2-V3.md`, `../assets/06-Header-Lifecycle-Deprecation-Sunset.md`, `../assets/06-Komunikasi-Konsumen-Deprecation.md`, `../assets/06-Kriteria-Sunset-Metrik.md`, `../assets/06-Observability-Alert-Per-Versi.md`, `../assets/06-Checklist-Zero-Downtime.md`

### 7.1 Ringkasan best practices dan rekomendasi eksplisit

**Legenda penanda.** Seluruh sitasi pada bagian ini memakai tiga penanda: `[Standar resmi]` untuk RFC dan OpenAPI Specification; `[Praktik industri]` untuk panduan vendor/resmi, guideline perusahaan, opini industri, serta dokumentasi proyek; `[Rekomendasi peneliti/tim]` untuk sintesis, keputusan desain, dan ambang operasional yang ditetapkan tim. Ketiganya dibedakan secara konsisten hingga daftar sumber di akhir sub-bab.

**Takeaway.** `[Rekomendasi peneliti/tim]` Untuk versi yang **di-embed langsung pada permukaan API**, paket utamanya adalah: path major `/api/v1`, `/api/v2`, `/api/v3`; satu OpenAPI Description (OAD) dan satu SDK per major; Expand–Contract pada database dan kontrak; lifecycle `Deprecation`/`Sunset` sesuai RFC 9745/8594; serta keputusan sunset berbasis metrik pemakaian per versi. Landasannya: `[Standar resmi]` [RFC 9110, HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html), [Standar resmi] [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html), [Standar resmi] [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html), `[Praktik industri]` [Microsoft Learn, "Best practices for RESTful web API design"](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design), `[Praktik industri]` [Martin Fowler, "Parallel Change"](https://martinfowler.com/bliki/ParallelChange.html).

> **REKOMENDASI EKSPLISIT** `[Rekomendasi peneliti/tim]`: **Gunakan major version pada path — `/api/v1/...`, `/api/v2/...`, `/api/v3/...` — sebagai satu-satunya penentu major contract, dan terbitkan satu OpenAPI Description serta satu package SDK untuk setiap major.** Tidak ada mekanisme kedua yang ikut menentukan major; `Deprecation`, `Sunset`, `Link`, dan `apiVersion` di body hanyalah lapisan lifecycle/audit.

Alasan yang dapat ditelusuri:

1. Brief mensyaratkan V1/V2/V3 **terlihat** dan hidup bersamaan; path paling visibel untuk gateway, log, docs, SDK, dan alert per versi. `[Praktik industri]` [Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design) menyebut URI sederhana namun eksplisit; `[Praktik industri]` [Google Cloud Blog, "API design: Which version of versioning is right for you?"](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you) menyebut URL memang diperlukan bila dua entity version diproses implementasi/storage berbeda.
2. URI berbeda menyederhanakan cache key HTTP dan menghindari kewajiban `Vary` atas header versi yang rawan salah konfigurasi. `[Standar resmi]` [RFC 9111, HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111.html); `[Praktik industri]` [Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design).
3. Satu OAD per major memudahkan generator klien/server dan dokumentasi, karena OAS memisahkan versi spesifikasi, versi dokumen, dan versi implementasi. `[Standar resmi]` [OpenAPI Specification 3.2.0](https://spec.openapis.org/oas/v3.2.0.html).
4. Perubahan kompatibel **tetap tidak menaikkan major**: tambahkan field opsional pada V3 berjalan daripada menciptakan V4. `[Praktik industri]` [Zalando RESTful API Guidelines](https://opensource.zalando.com/restful-api-guidelines/), [Google Cloud Blog](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you), [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).
5. **Batasan wajib dicatat dalam ADR:** keputusan ini mengorbankan kemurnian "satu URI = satu resource" dan membuat HATEOAS link version-scoped; `[Praktik industri]` [Zalando rule 114](https://opensource.zalando.com/restful-api-guidelines/) akan menolaknya. Ini keputusan organisasi yang terdokumentasi, **bukan** klaim kepatuhan standar HTTP. `[Standar resmi]` [RFC 9110, HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) memisahkan identitas resource dari representasi dan mendefinisikan content negotiation.

**Ringkasan best practices** `[Rekomendasi peneliti/tim]`, dirangkum dari seluruh temuan:

- Satu penentu major (path), satu OAD per major, satu SDK per major, satu domain model kanonik di dalam, adapter/presenter per versi di lapisan terluar.
- Additive change tidak melahirkan major baru; breaking change wajib major baru, ADR, dan compatibility gate CI.
- Zero downtime = kompatibilitas image lama/baru sekaligus pada **database dan kontrak**; rolling/canary saja tidak cukup.
- Urutan deploy: Expand → backfill → dual-write → dual-read/shadow → canary/switch → Contract, dengan feature flag dan `can-i-deploy` sebagai gate.
- Lifecycle machine-readable (`Deprecation`, `Sunset`, `Link`, `deprecated: true`) **selalu** dipasangkan komunikasi manusia dan metrik konsumen.
- Kebijakan N-1/N-2, notice period, persentase canary, dan ambang sunset adalah keputusan organisasi dengan placeholder, bukan angka dari standar.
- Header lifecycle hanya hint: klien SHOULD tetap berfungsi tanpanya, dan deprecation tidak mengubah perilaku resource.
- Observability wajib berlabel `api_version`, `route`, `consumer_id`, `canary`; keputusan cutover dan rollback diambil dari sinyal tersebut.
- Contract dituntaskan pada rilis terpisah setelah metrik nol; menundaContract memperburuk keadaan akhir. `[Praktik industri]` [Martin Fowler, "Parallel Change"](https://martinfowler.com/bliki/ParallelChange.html).

**Peta template (keberadaan dan section kunci saja; isi tidak disalin karena tiap template sudah berkas mandiri)** `[Rekomendasi peneliti/tim]`:

| Berkas template | Section kunci yang dirujuk |
|---|---|
| `../assets/06-OpenAPI-Multi-Versi.md` | 7.3 konvensi OAD; 7.8 dokumentasi multi-versi |
| `../assets/06-OpenAPI-Multi-Versi-V1.md`, `-V2.md`, `-V3.md` | 7.7 cuplikan OAD per major |
| `../assets/06-Matriks-Endpoint-Versi.md` | 7.7 matriks kompatibilitas V1/V2/V3 |
| `../assets/06-Routing-Gateway-Nginx.md` | 7.8 routing gateway dan cuplikan konfigurasi |
| `../assets/06-Runbook-Expand-Contract.md` | 7.5 urutan Expand–Contract dan exit gate |
| `../assets/06-Timeline-Migrasi-V1-V2-V3.md` | 7.7 timeline migrasi bertahap |
| `../assets/06-Header-Lifecycle-Deprecation-Sunset.md` | 7.3 koreksi RFC; 7.6 header lifecycle |
| `../assets/06-Komunikasi-Konsumen-Deprecation.md` | 7.6 langkah komunikasi T+0 hingga contract |
| `../assets/06-Kriteria-Sunset-Metrik.md` | 7.6 kriteria sunset berbasis `api_version` |
| `../assets/06-Observability-Alert-Per-Versi.md` | 7.8 sinyal dan alert per versi |
| `../assets/06-Checklist-Zero-Downtime.md` | 7.9 checklist cutover dan kriteria rollback |

### 7.2 Perbandingan opsi penempatan versi

| Opsi | Contoh | Visibilitas | Cacheability | Routing | Kemudahan klien | Kompatibilitas OpenAPI/SDK | Rekomendasi |
|---|---|---|---|---|---|---|---|
| **Path / URI** | `GET /api/v3/orders/{id}` | Sangat tinggi: log, browser, docs, dashboard | Tinggi: method + target URI adalah minimum cache key; tiap versi URI berbeda | Paling sederhana: prefix route di gateway/service | Paling mudah; URL dapat diketuk, dibookmark; HATEOAS link harus memuat versi | Sangat baik: satu dokumen + satu generator per major | **Pilihan utama** untuk V1/V2/V3 eksplisit, entity versioning, gateway routing, dan metrik per versi |
| Query parameter | `GET /api/orders/{id}?version=3` | Tinggi | Umumnya baik bila query masuk cache key; proxy lama kadang tidak menyimpan respons ber-query | Perlu parsing query; default wajib untuk klien lama | Mudah, tetapi mudah tertinggal saat menyalin URL | Perlu parameter versi di semua operasi; generator bisa bingung bila versi juga di path | API sederhana/internal yang ingin resource URI tetap; bukan pilihan utama brief |
| Custom header | `Api-Version: 3` atau `Accept-Version: 2` | Rendah di log/browser; perlu tooling | Rentan: cache wajib `Vary`; duplikasi data di server-side cache bila header bukan kunci | Header inspection di gateway | Perlu SDK/Postman; sulit uji GET lewat address bar | Parameter header global, tetapi dokumentasi lintas versi kurang langsung | Format versioning dengan satu canonical URI, atau kontrol berbasis SDK |
| Media type / `Accept` | `Accept: application/vnd.{{org}}.v3+json` | Sedang; terlihat pada negotiation | Perlu `Vary: Accept`; cache MUST NOT memakai ulang respons bila header yang dinominasikan tidak cocok | Content negotiation, bukan sekadar prefix path | Klien wajib mengelola media type; cocok untuk HATEOAS karena MIME type masuk link | Beberapa media type dapat dideklarasikan, tetapi satu dokumen per major tetap lebih aman | Zalando mewajibkan untuk breaking payload schema; Apigee justru menentang versi di `Accept`/`Content-Type` |
| Versi di payload/envelope | `{"apiVersion":"V3","data":{...}}` | Tinggi di body, rendah di routing/log | Body tidak membantu HTTP cache key; generic cache biasanya tidak memakai body | Tidak bisa routing sebelum body dibaca; berisiko untuk gateway | Campur metadata dengan domain; versi entity justru disarankan di body | Buruk sebagai satu-satunya kontrak HTTP; sulit menghasilkan SDK rapi | Metadata tambahan/audit, **bukan pengganti** versi permukaan HTTP |
| Date-based ala Stripe | `Stripe-Version: 2026-10-28.endive` | Sedang; eksplisit pada request/SDK/account | Sama seperti header: butuh `Vary` bila di-cache | Dipilih per request oleh header/SDK/account; menentukan webhook dan automated operations | Sangat baik bila SDK mem-pin; upgrade terkontrol | Vendor-specific; bukan pola path V1/V2/V3 | API dengan perubahan incremental terjadwal dan ekosistem SDK/webhook kuat |

**Sumber per baris.** `[Standar resmi]` [RFC 9111, HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111.html) menetapkan method + target URI sebagai minimum cache key dan mewajibkan kecocokan header yang dinominasikan `Vary`. `[Standar resmi]` [RFC 9110, HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) mendefinisikan representasi dan content negotiation; contoh vendor media type `application/vnd.github.v3+json` ada pada `[Standar resmi]` [OpenAPI Specification 3.1.0](https://spec.openapis.org/oas/v3.1.0.html). `[Praktik industri]` [Microsoft Learn, "Best practices for RESTful web API design"](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design) menyebut URI/query versioning cache-friendly dan memperingatkan duplikasi cache pada header/media type. `[Praktik industri]` [Zalando rules 113–114](https://opensource.zalando.com/restful-api-guidelines/) memuat `MUST use media type versioning` dan `MUST not use URL versioning`, hanya untuk payload schema. `[Praktik industri]` [Google Cloud Blog, "API design: Which version of versioning is right for you?"](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you) membedakan format vs entity versioning, menyarankan `Accept-Version`/`Content-Version`, dan menolak versi di `Accept`/`Content-Type`. `[Praktik industri]` [Stripe Docs, "How API versioning works"](https://docs.stripe.com/api-versions) menjelaskan pemilihan lewat `Stripe-Version`, SDK pin, atau default akun, dengan release bulanan tanpa breaking change dan major dua kali setahun yang dapat breaking.

**Lapisan kedua yang opsional** `[Rekomendasi peneliti/tim]`: `Deprecation`, `Sunset`, `Link` untuk lifecycle ([Standar resmi] [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html), [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html)); `apiVersion` di body hanya audit/telemetri. Date-based ala Stripe tetap valid sebagai alternatif vendor, tetapi tidak memenuhi literal V1/V2/V3 dan memindahkan seleksi ke `Stripe-Version`/SDK pin ([Praktik industri] [Stripe Docs](https://docs.stripe.com/api-versions)).

### 7.3 Konvensi penting: koreksi wajib dan empat versi yang berbeda

**Koreksi fakta wajib** `[Standar resmi]`:

| Penegasan | Isi yang benar | Sumber |
|---|---|---|
| RFC 8594 = **`Sunset`** | Bukan `Deprecation`. Berisi satu HTTP-date, menandakan resource diperkirakan menjadi tidak responsif; klien SHOULD memperlakukannya sebagai **hint** | [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html) |
| RFC 9745 = **`Deprecation`** | Diterbitkan Maret 2025 sebagai Standards Track; Structured Field Date, mis. `Deprecation: @1688169599`; deprecation **tidak mengubah perilaku** resource | [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html) |
| Hubungan keduanya | RFC 9745 **melarang timestamp `Sunset` lebih awal daripada `Deprecation`** dan menyarankan `Link: <...>; rel="deprecation"`; RFC 8594 menyediakan `rel="sunset"` untuk kebijakan dan mitigasi. Format tanggal keduanya berbeda secara historis | [RFC 9745 §3–4](https://www.rfc-editor.org/rfc/rfc9745.html); [RFC 8594 §6, §9](https://www.rfc-editor.org/rfc/rfc8594.html) |
| Sifat keduanya | Keduanya **hint**, bukan jaminan; RFC 8594 menyatakan klien SHOULD tetap berfungsi tanpa `Sunset`, RFC 9745 menegaskan `Deprecation` tidak mengubah makna/fungsi resource | [RFC 8594 §3, §8](https://www.rfc-editor.org/rfc/rfc8594.html); [RFC 9745 §5, §7](https://www.rfc-editor.org/rfc/rfc9745.html) |

**Empat hal yang berbeda dan tidak boleh disamakan** `[Standar resmi]` [OpenAPI Specification 3.2.0 §4.1–4.2](https://spec.openapis.org/oas/v3.2.0.html), [OpenAPI Specification 3.1.0 §4.8.1–4.8.2](https://spec.openapis.org/oas/v3.1.0.html); `[Rekomendasi peneliti/tim]` [Stripe Docs](https://docs.stripe.com/api-versions) untuk pin SDK:

| Entitas | Makna | Contoh | Kesalahan yang dicegah |
|---|---|---|---|
| `openapi` | Versi **fitur spesifikasi OAS** yang dipakai dokumen | `openapi: 3.1.0`, `openapi: 3.2.0` | Mengira `3.2.0` berarti "API V3" |
| `info.version` | Versi **OpenAPI document** itu sendiri, bukan versi API | `{{INFO_VERSION_V3}}`, SemVer dokumen | Menulis `"version: V3"` otomatis |
| `/api/vN` | Versi **API / major contract** yang di-embed pada permukaan | `/api/v1`, `/api/v2`, `/api/v3` | Mengganti major lewat header diam-diam |
| Versi SDK | SemVer **package klien**, terpisah | `{{ORG}}-sdk-{{BAHASA}}-v3@1.4.0` | Menyamakan `sdk-v3@1.4.0` dengan `info.version` atau `/api/v3` |

Catatan tambahan: OAS juga memisahkan **versi implementasi** dari ketiganya ([Standar resmi] [OpenAPI Specification 3.2.0](https://spec.openapis.org/oas/v3.2.0.html)). OAS 3.2 mengizinkan OAD satu dokumen atau multi-document dengan referensi URI dan merekomendasikan entry document `openapi.yaml`/`openapi.json`; 3.2.1 tercantum sebagai patch pada daftar versi resmi; 3.1.0 memperkenalkan kompatibilitas penuh JSON Schema 2020-12 ([Standar resmi] [OpenAPI 3.2.1](https://spec.openapis.org/oas/v3.2.1.html)).

**Konvensi header lifecycle** `[Standar resmi]` dan `[Rekomendasi peneliti/tim]`:

| Arahan | Cuplikan | Aturan |
|---|---|---|
| Status response | `HTTP/1.1 200 OK` / `Content-Type: application/json` | Tetap respons normal selama deprecated |
| `Deprecation` | `Deprecation: @{{UNIX_TIMESTAMP_DEPRECATION_V2}}` | MUST berupa Date Structured Field `@<unix-seconds>`; boleh masa lalu atau depan |
| `Sunset` | `Sunset: {{HTTP_DATE_SUNSET_V2}}` | Satu HTTP-date, sebaiknya masa depan; tidak boleh lebih awal dari `Deprecation` |
| `Link` deprecation | `Link: <https://{{HOST_DOCS}}/api/lifecycle/deprecation>; rel="deprecation"; type="text/html"` | Menunjuk dokumentasi; aktif **sebelum** `Deprecation` |
| `Link` sunset | `Link: <https://{{HOST_DOCS}}/api/lifecycle/sunset>; rel="sunset"; type="text/html"` | Kebijakan, jadwal, mitigasi |
| `API-Version` | `API-Version: V2` | `[Rekomendasi peneliti/tim]` **Bukan header standar IETF**; hanya metadata observability |
| `Vary` | `Vary: "Accept, API-Version"` | Wajib bila custom header ikut **menyeleksi** representasi ([Standar resmi] [RFC 9111 §4.1](https://www.rfc-editor.org/rfc/rfc9111.html)) |
| `deprecated: true` | Operation/Parameter Object | `[Standar resmi]` [OpenAPI 3.1.0, Operation Object / Parameter Object](https://spec.openapis.org/oas/v3.1.0.html#operation-object); konsumen SHOULD menjauhi operasi bertanda; dipakai **bersama** header, bukan pengganti |

### 7.4 Matriks additive vs breaking

`[Praktik industri]` [Zalando rules 106–108](https://opensource.zalando.com/restful-api-guidelines/), [Google AIP-180, Backwards compatibility](https://google.aip.dev/180), [Stripe Docs, "How API versioning works"](https://docs.stripe.com/api-versions); `[Standar resmi]` [RFC 9457, Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html), [RFC 9110, HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html).

| Perubahan | Additive / Breaking | Aturan dan risiko |
|---|---|---|
| Menambah resource/endpoint, optional request parameter, response property, event type | **Additive** | Klien wajib *tolerant reader*: abaikan field/event asing (Stripe) |
| Menambah field **required** pada request/resource yang sudah ada | **Breaking** | AIP-180 melarang; default perilaku harus tetap seperti sebelum field ada |
| Menambah field **response** | Umumnya **additive** | Zalando membolehkan field mandatory/optional pada output-only; klien toleran |
| Optional → required pada **request** | **Breaking** | Zalando: input boleh mandatory→optional, bukan sebaliknya |
| Required → optional pada **response** | **Breaking** | Zalando: output boleh optional→mandatory, bukan sebaliknya |
| Mengubah **tipe** data field | **Breaking** | AIP-180 melarang walaupun wire-compatible karena merusak generated code |
| Mengubah format nilai, algoritma konstruksi, **default value**, serialisasi default | **Breaking** | AIP-180 menggolongkan sebagai perubahan semantik |
| Menambah **enum value pada request** | **Additive, hati-hati** | AIP-180 membolehkan request-only; Zalando: server tetap menerima nilai lama |
| Menambah **enum value pada response** | **Berisiko / breaking** | Klien dengan enum tertutup gagal; Zalando melarang perluasan enum output, menyarankan open-ended values; Stripe menyaratkan listener webhook menangani event type asing |
| Menghapus atau **rename** field/parameter/enum/method | **Breaking** | Rename = remove + add; Stripe mencantumkan renamed field/removed parameter/object shape sebagai major breaking change |
| Memperketat validasi, constraint, batas panjang string | Umumnya **breaking** | Zalando melarang validasi input lebih restriktif; AIP-180 memperingatkan batas string/resource name |
| Mengganti **format error** | **Breaking** tanpa major baru | RFC 9457 menetapkan `application/problem+json` dengan `type/title/status/detail/instance`; klien wajib mengabaikan extension asing |
| Menambahkan **pagination** setelah sebelumnya mengembalikan semua item | **Berisiko / breaking** | AIP-180: default `page_size` baru lebih kecil membuat klien lama mengira seluruh hasil diterima |
| Mengganti offset→cursor atau bentuk page object | **Breaking** | Zalando rules 159–161/248: pagination wajib, cursor direkomendasikan, page `items/self/first/prev/next/last/query` |
| Mengubah status code atau semantik metode | **Breaking** | Status code adalah bagian kontrak; Zalando mewajibkan klien siap menerima status tidak didokumentasikan |
| Field removal setelah sunset | Hanya **major baru / contract phase** | `[Praktik industri]` [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html): MAJOR untuk perubahan inkompatibel; `[Standar resmi]` [RFC 9745 §5](https://www.rfc-editor.org/rfc/rfc9745.html): deprecation tidak mengubah perilaku |

**Compatibility gate CI** `[Rekomendasi peneliti/tim]`: simpan matriks ini sebagai gate yang melakukan diff OpenAPI V3 terhadap baseline; setiap perubahan berkategori "Breaking" memblokir rilis minor/patch dan memaksa `feat(api)!:` serta ADR V4. Dasar: `[Praktik industri]` [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) memetakan `BREAKING CHANGE` ke MAJOR, dan [Zalando rule 106](https://opensource.zalando.com/restful-api-guidelines/) membedakan incompatible change dari breaking change yang benar-benar dideploy.

### 7.5 Urutan Expand → backfill → dual-write/read → canary/switch → Contract

`[Praktik industri]` [Martin Fowler, "Parallel Change"](https://martinfowler.com/bliki/ParallelChange.html) mendefinisikan **expand** (antarmuka mendukung lama dan baru), **migrate** (klien berpindah inkremental; fase terlama untuk klien eksternal), **contract** (hapus lama setelah tidak dipakai). Pola ini memungkinkan rilis pada fase mana pun, cocok dengan Continuous Delivery, dan berlaku untuk refactoring, database refactoring, canary/blue-green, serta remote API evolution; **bila contract tidak dijalankan, keadaan akhir justru lebih buruk**. Urutan berikut `[Rekomendasi peneliti/tim]`, disusun dari [Fowler Parallel Change](https://martinfowler.com/bliki/ParallelChange.html), `[Praktik industri]` [Kubernetes Docs, "Deployments"](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), [AWS API Gateway, "Set up a canary release deployment"](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md), dan [Pact Docs, "Can I Deploy"](https://docs.pact.io/pact_broker/can_i_deploy):

| # | Fase | Aksi database | Aksi kontrak/API | Aplikasi/deploy | Exit gate |
|---|---|---|---|---|---|
| 0 | Design | ADR + migration plan + rollback plan | OAD V3 draft, compatibility diff, Pact expectations | Feature flag `{{FLAG_V3}}` off | ADR approved; contract tests merah untuk V3 |
| 1 | **Expand** | Tambah kolom/tabel/index **nullable** atau kompatibel; jangan drop/rename | Terbitkan `/api/v3` di belakang flag; V1/V2 tetap responsif | Deploy adapter V3 + domain kanonik; rolling update | Old app images masih bisa menulis; health/latency hijau |
| 2 | **Backfill** | Isi data lama ke struktur baru secara idempotent dan terukur | Tidak mengubah response V1/V2 | `scripts/backfill-{{PERUBAHAN}}.sh` | Parity check `{{JUMLAH_BARIS_LAMA}}` vs `{{JUMLAH_BARIS_BARU}}`; drift `{{AMBANG_DRIFT}}` |
| 3 | **Dual-write** | Tulis ke lama **dan** baru dalam satu transaksi/logik yang dapat dikompensasi | Semua versi membaca dari adapter sesuai | Rilis kode dual-write lebih dulu daripada konsumen baru | Reconciliation job hijau; tidak ada orphan write |
| 4 | **Dual-read / shadow** | Baca baru, bandingkan dengan lama; sumber kebenaran mulai beralih | V3 aktif untuk internal/canary; V1/V2 tetap kontrak lama | Canary 1%→5%→25%→50%→100%; log/metrik terpisah | Selisih respons di bawah `{{AMBANG_PARITY}}`; error budget terpenuhi |
| 5 | **Canary / Switch** | Sumber baca utama = struktur baru; **tulis lama masih dijaga untuk rollback** | Default docs/SDK → V3; deprecation V2 diumumkan | Promote canary; blue-green cutover bila perlu | `can-i-deploy` hijau; SLO V3 hijau selama `{{JENDELA_OBSERVASI}}` |
| 6 | **Contract** | Setelah sunset dan metrik nol, hapus kolom/tabel/trigger lama **pada rilis terpisah** | Matikan route V1/V2 → `410 Gone` atau sesuai kebijakan; arsipkan OAD | Hapus adapter/flag lama | Tidak ada traffic versi lama selama `{{JENDELA_NOL_TRAFFIC}}`; backup/rollback tersedia |

**Mekanisme deployment vs jaminan kompatibilitas** `[Rekomendasi peneliti/tim]`. `[Praktik industri]` [Kubernetes Docs, "Deployments"](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/): `RollingUpdate` menaikkan ReplicaSet baru sambil menurunkan lama, default `maxUnavailable` dan `maxSurge` 25%, dapat di-rollback ke revisi stabil, dan `progressDeadlineSeconds` menandai rollout macet. `[Praktik industri]` [AWS API Gateway, "Set up a canary release deployment"](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md): canary memisahkan traffic produksi/canary dengan rasio 0.0–100.0, menyediakan stage variable override, log dan metrik terpisah, serta dapat dipromosikan atau dibatalkan. Keduanya **mekanisme deployment, bukan jaminan kompatibilitas database**; Expand–Contract tetap wajib.

**Feature flag.** `[Praktik industri]` [Fowler, "Parallel Change"](https://martinfowler.com/bliki/ParallelChange.html) menyebut feature toggle sisi klien membuat klien forward-compatible dan memisahkan rilis supplier dari klien; [Pact Docs, "CI/CD Setup Guide"](https://docs.pact.io/pact_nirvana) mencantumkan "Working with Feature Flags" pada panduan CI/CD lanjutan. `[Praktik industri]` [Fowler, "Canary Release"](https://martinfowler.com/bliki/CanaryRelease.html): canary adalah aplikasi Parallel Change dengan migrate sampai seluruh pengguna berpindah, **rollback dengan mengalihkan pengguna kembali ke versi lama**, dan jumlah versi konkuren sebaiknya minimum.

**Consumer-driven contracts.** `[Praktik industri]` [Pact Docs, "Can I Deploy"](https://docs.pact.io/pact_broker/can_i_deploy): Pact Matrix merekam pasangan consumer/provider version yang sudah diuji; `can-i-deploy` sebelum deploy dan `record-deployment` sesudah deploy membuat Broker mengetahui versi aplikasi di tiap environment dan dapat memblokir deploy belum terverifikasi. [Pact Docs, "CI/CD Setup Guide"](https://docs.pact.io/pact_nirvana) menempatkan `can-i-deploy` pada Platinum level dan Pact pada deploy pipeline di Diamond level; untuk klien mobile dengan banyak versi hidup bersamaan tersedia `--all prod`.

### 7.6 Siklus hidup V1/V2/V3: coexist, N-1/N-2, notice period, deprecation dan sunset

**Coexistence.** `[Praktik industri]` [Zalando rule 106/113](https://opensource.zalando.com/restful-api-guidelines/): perubahan tanpa merusak konsumen memakai compatible extension atau versi baru dengan dukungan paralel dan deprecation; bila versi baru terpaksa dibuat, varian lama dan baru didukung bersamaan. `[Praktik industri]` [Fowler, "Parallel Change"](https://martinfowler.com/bliki/ParallelChange.html) memperingatkan biaya mempertahankan dua versi selama migrate. `[Praktik industri]` [Stripe Docs](https://docs.stripe.com/api-versions) menunjukkan production reality: versi request, SDK pin, default akun, webhook endpoint pin, dan automated operations semuanya dapat menentukan versi objek — versi lama tidak dapat dimatikan hanya karena versi baru sudah dirilis.

**Kebijakan N-1/N-2 adalah keputusan organisasi, bukan angka dari standar** `[Rekomendasi peneliti/tim]`. Tidak ada RFC yang menetapkan "dukung N-1 selama 12 bulan"; tetapkan di `support-policy.md`:

| Kebijakan | Versi aktif | Versi security-only | Versi sunset | Cocok untuk |
|---|---|---|---|---|
| **N-1** | V3 | V2 | V1 | Konsumen internal yang dapat dipaksa upgrade; biaya paling rendah |
| **N-2** | V3 | V2 + V1 | Versi sebelum V1 | Eksternal/mobile/webhook dengan siklus upgrade lambat |
| Kontrak khusus | Sesuai kontrak pelanggan | Sesuai SLA | Sesuai kontrak | Regulated/enterprise; tanggal tidak boleh hanya "nanti" |

`[Standar resmi]` [RFC 8594 §3, §8](https://www.rfc-editor.org/rfc/rfc8594.html) dan [RFC 9745 §5, §7](https://www.rfc-editor.org/rfc/rfc9745.html) menegaskan kedua header hanya hint, sehingga **komunikasi manusia + metrik tidak bisa digantikan header saja** `[Rekomendasi peneliti/tim]`. `[Praktik industri]` [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) mensyaratkan deprecation didokumentasikan dan hadir dalam minimal satu MINOR sebelum removal pada MAJOR.

**Komunikasi ke konsumen** `[Rekomendasi peneliti/tim]`, berdasarkan [RFC 9745 §3.1](https://www.rfc-editor.org/rfc/rfc9745.html), [RFC 8594 §6](https://www.rfc-editor.org/rfc/rfc8594.html), `[Praktik industri]` [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html), [Stripe Docs](https://docs.stripe.com/api-versions):

1. T+0: ADR + `support-policy.md` + halaman deprecation/sunset dipublikasikan; `Link` rel sudah aktif **sebelum** `Deprecation`.
2. T+0: CHANGELOG entri `Deprecated`, release notes, email/portal developer, dashboard per konsumen, migration guide `v2-to-v3.md` dengan contoh request/response.
3. T+0: `Deprecation` header dan `deprecated: true` pada OpenAPI; SDK V2 diberi compile/runtime warning; SDK V3 tersedia.
4. T+`{{NOTICE_PERIOD}}`: `Sunset` header dengan **tanggal pasti**; pengingat T−90/T−30/T−7 hari; daftar consumer yang masih memakai V2.
5. T+`{{SUNSET_DATE}}`: route dinonaktifkan sesuai kebijakan — pilih dan dokumentasikan `410 Gone` atau `404 Not Found`; `[Standar resmi]` [RFC 8594 §9](https://www.rfc-editor.org/rfc/rfc8594.html) memberi kedua contoh dan menegaskan tidak menjanjikan bentuk respons.
6. Setelah contract: arsipkan OAD, tandai ADR `superseded`, hapus adapter/flag/kolom lama, catat CHANGELOG kategori `Removed`.

**Keputusan sunset dari metrik `api_version`** `[Rekomendasi peneliti/tim]`; ambang adalah placeholder yang wajib disetujui owner, **bukan angka standar**:

| Metrik | Definisi operasional | Contoh ambang cutover |
|---|---|---|
| Request share per versi | `sum(http_requests_total{api_version="V1"}) / sum(http_requests_total)` | `<= {{AMBANG_REQUEST_SHARE}}` selama `{{JENDELA_OBSERVASI}}` |
| Unique consumer/client_id | `count_distinct(client_id{api_version="V1"})` | `0` untuk `{{JENDELA_NOL_KONSUMEN}}`, atau daftar exception tertanda tangan |
| Webhook/event delivery | Jumlah endpoint yang masih pin versi lama | `0`; `[Praktik industri]` [Stripe Docs](https://docs.stripe.com/api-versions) memungkinkan webhook endpoint mem-pin versi sendiri |
| Error/SLO | 5xx, p95/p99, timeout, business-error rate per versi + canary | Tidak melebihi SLO selama `{{JENDELA_OBSERVASI}}` ([Praktik industri] [AWS API Gateway canary](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md)) |
| Kontrak | `can-i-deploy` untuk V3 terhadap versi konsumen di production | Semua verifikasi sukses ([Praktik industri] [Pact Docs, "Can I Deploy"](https://docs.pact.io/pact_broker/can_i_deploy)) |
| Data parity | Perbandingan dual-write/dual-read | Drift `<= {{AMBANG_DRIFT}}` |
| Dukungan | Tiket/eskalasi aktif, kontrak enterprise, regulatory retention | `0` atau pengecualian berdokumen |

`[Praktik industri]` [Fowler, "Canary Release"](https://martinfowler.com/bliki/CanaryRelease.html) secara eksplisit menyarankan memonitor versi klien yang dipakai dan melakukan contract backend setelah angka pemakaian turun ke level tertentu pada sistem dengan klien yang tidak dapat dipaksa upgrade.

### 7.7 Matriks kompatibilitas V1/V2/V3, tiga endpoint, cuplikan, dan timeline

**Matriks kompatibilitas** `[Rekomendasi peneliti/tim]`; `✅` didukung, `⚠️` didukung dengan adaptor/deprecation, `❌` tidak boleh dipakai. Sumber aturan: `[Praktik industri]` [Zalando rules 106–108](https://opensource.zalando.com/restful-api-guidelines/), [Google AIP-180](https://google.aip.dev/180), [Stripe Docs](https://docs.stripe.com/api-versions); `[Standar resmi]` [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html), [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html), [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html).

| Kemampuan / kontrak | V1 | V2 | V3 | Catatan migrasi |
|---|---|---|---|---|
| `GET /orders/{id}` | ✅ | ✅ | ✅ | Path major berbeda, `orderId` domain sama |
| Response `total: number` | ✅ | ❌ | ❌ | V2/V3 memakai `amount.value` string |
| Response `amount{value,currency}` | ❌ | ✅ | ✅ | Adapter V1 memetakan kembali ke `total` |
| Field `status` | ❌ | ✅ | ✅ | Enum V3 lebih luas; klien V2 tidak boleh menerima V3 enum tanpa major baru |
| Enum `REFUNDED` | ❌ | ❌ | ✅ | Perluasan enum response = breaking menurut Zalando/AIP-180 |
| `offset/limit` pagination | ✅ | ✅ | ❌ | V3 memakai cursor; jangan ubah V1/V2 |
| Cursor `self/next` | ❌ | ❌ | ✅ | `next` link bersifat `/api/v3/...` |
| Error `application/problem+json` | ⚠️ | ✅ | ✅ | V1 dipertahankan sesuai kontrak lama; migrasi error handling masuk V3 |
| Header `Deprecation` | ✅ | ✅ | ❌ | V1/V2 saja; syntax RFC 9745 |
| Header `Sunset` | ✅ | ✅ | ❌ | V1 tanggal lebih awal dari V2; RFC 8594 |
| `deprecated: true` pada OpenAPI | ✅ | ✅ | ❌ | OpenAPI 3.1 Operation/Parameter |
| SDK generated | ✅ | ✅ | ✅ | Nama package terpisah |
| Pact contract | ✅ | ✅ | ✅ | `can-i-deploy` per consumer/provider version |
| Default docs/quickstart | ❌ | ❌ | ✅ | README navigation hub menunjuk V3 |
| Write path repo kanonik | ⚠️ | ✅ | ✅ | Expand: dual-write; Switch: V3 source of truth |
| Field removal `total` | ❌ | ❌ | ✅ | Contract hanya setelah sunset V2 + metrik nol |

**Contoh tiga endpoint** `[Rekomendasi peneliti/tim]`:

| Versi | Endpoint | Perubahan konkret | Status contoh |
|---|---|---|---|
| V1 | `GET /api/v1/orders/{{ORDER_ID}}` | `total: number` flat; error legacy | Deprecated + Sunset |
| V2 | `POST /api/v2/orders`, `GET /api/v2/orders/{{ORDER_ID}}` | `total`→`amount{value,currency}`, tambah `status`; breaking terhadap V1 | Deprecated, migrasi ke V3 |
| V3 | `POST /api/v3/orders`, `GET /api/v3/orders/{{ORDER_ID}}`, `GET /api/v3/orders?cursor={{CURSOR}}` | Cursor pagination, `status` extensible, `application/problem+json` | Current |

`application/problem+json` beserta `type/title/status/detail/instance` mengikuti `[Standar resmi]` [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html); pagination `items/self/next` mengikuti `[Praktik industri]` [Zalando rules 159–161/248](https://opensource.zalando.com/restful-api-guidelines/); penambahan enum `REFUNDED` pada response V3 sengaja ditempatkan di major baru mengikuti [Zalando rule 107](https://opensource.zalando.com/restful-api-guidelines/) dan [Google AIP-180](https://google.aip.dev/180).

**Cuplikan OAD per major** `[Rekomendasi peneliti/tim]`, skematis, bukan seluruh kontrak produksi; `[Standar resmi]` [OpenAPI Specification 3.2.0 §4.1–4.2](https://spec.openapis.org/oas/v3.2.0.html):

| OAD | Potongan kunci |
|---|---|
| V1 | `openapi: 3.1.0`; `info.version: "{{INFO_VERSION_V1}}"` (versi dokumen, bukan "V1"); `servers: - url: "https://{{API_HOST}}/api/v1"`; `operationId: getOrderV1`; `deprecated: true`; `required: [id, total]`; `total: { type: number }`; respons `404` → `application/problem+json` |
| V2 | `openapi: 3.1.0`; `info.version: "{{INFO_VERSION_V2}}"`; `servers.url: "https://{{API_HOST}}/api/v2"`; `operationId: getOrderV2`; `deprecated: true`; `required: [id, amount, status]`; `amount.value: { type: string }`; `status.enum: ["CREATED","PAID","CANCELLED"]` |
| V3 | `openapi: 3.2.0`; `info.version: "{{INFO_VERSION_V3}}"`; `servers.url: "https://{{API_HOST}}/api/v3"`; `operationId: getOrderV3`; `required: [id, amount, status, links]`; `amount: { $ref: "#/components/schemas/Money" }`; `status.enum: ["CREATED","PAID","CANCELLED","REFUNDED"]`; `links.required: [self, next]`; `404` → `application/problem+json` |
| Ketiganya | `x-api-id: "{{UUID_API_IMMUTABLE}}"` dan `x-audience: "{{AUDIENCE}}"` mengikuti `[Praktik industri]` [Zalando rules 101/116/215/218/219](https://opensource.zalando.com/restful-api-guidelines/) |

**Cuplikan routing** `[Rekomendasi peneliti/tim]`, Nginx-style ilustrasi generik, bukan dokumentasi vendor tertentu:

| Blok | Potongan konfigurasi |
|---|---|
| Upstream | `upstream {{UPSTREAM_STABLE}} { server {{HOST_STABLE}}:{{PORT}}; }`; `upstream {{UPSTREAM_CANARY_V3}} { server {{HOST_CANARY_V3}}:{{PORT}}; }` |
| Canary map | `map $http_x_canary_v3 $target_v3 { default {{UPSTREAM_STABLE}}; "1" {{UPSTREAM_CANARY_V3}}; }` |
| V1 | `location /api/v1/ {` · `proxy_set_header X-API-Version "V1";` · `proxy_set_header X-Request-ID $request_id;` · `add_header Deprecation "@{{UNIX_TIMESTAMP_DEPRECATION_V1}}" always;` · `add_header Sunset "{{HTTP_DATE_SUNSET_V1}}" always;` · `add_header Link "...; rel=\"deprecation\"" always;` · `add_header Link "...; rel=\"sunset\"" always;` · `proxy_pass http://{{UPSTREAM_STABLE}};` |
| V2 | `location /api/v2/ {` · `proxy_set_header X-API-Version "V2";` · `add_header Deprecation "@{{UNIX_TIMESTAMP_DEPRECATION_V2}}" always;` · `add_header Sunset "{{HTTP_DATE_SUNSET_V2}}" always;` · `proxy_pass http://{{UPSTREAM_STABLE}};` |
| V3 | `location /api/v3/ {` · `proxy_set_header X-API-Version "V3";` · `proxy_pass http://$target_v3;` |
| Cache | Bila custom header ikut menentukan representasi: `add_header Vary "Accept, API-Version" always;` |

**Timeline migrasi bertahap** `[Rekomendasi peneliti/tim]`; **semua tanggal placeholder**, isi sesuai kalender organisasi dan zona waktu. Berdasarkan [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html), `[Praktik industri]` [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), `[Standar resmi]` [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html), [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html), `[Praktik industri]` [Fowler, "Parallel Change"](https://martinfowler.com/bliki/ParallelChange.html), [AWS API Gateway canary](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md):

| Tanggal | Fase | V1 | V2 | V3 | Artefak / gate |
|---|---|---|---|---|---|
| `{{T0_V1}}` | V1 GA | Active | — | — | `api-v1` tag, OAD V1, SDK V1 |
| `{{T0_V2}}` | Expand V2 | Active | Active | — | ADR rename `total`; dual-write; Pact V1+V2 hijau |
| `{{T_DEPRECATE_V1}}` | Deprecate V1 | Deprecated | Current | — | `Deprecation` V1, `deprecated: true`, migration v1→v2, CHANGELOG |
| `{{T_SUNSET_V1}}` | Sunset V1 | `410 Gone` | Current | — | `Sunset` V1 terpenuhi; request share V1 = `0`; contract kolom lama tahap 1 |
| `{{T0_V3}}` | Expand V3 | Arsip | Active | Active/canary | OAD V3, SDK V3, feature flag, canary 1% |
| `{{T_CANARY_V3_25}}` | Migrate | Arsip | Active | 25% | Metrik parity, `can-i-deploy`, error budget |
| `{{T_DEPRECATE_V2}}` | Deprecate V2 | Arsip | Deprecated | Current | `Deprecation` V2, migration v2→v3, notifikasi konsumen |
| `{{T_SUNSET_V2_NOTICE}}` | Sunset notice | Arsip | Deprecated + `Sunset` | Current | `{{NOTICE_PERIOD}}` sebelum pemadaman; T−90/T−30/T−7 reminder |
| `{{T_SWITCH_V3}}` | Switch | Arsip | Security-only | Default | Dual-write masih ON untuk rollback; SLO hijau `{{JENDELA_OBSERVASI}}` |
| `{{T_SUNSET_V2}}` | Sunset V2 | Arsip | `410 Gone` | Current | Nol consumer V2, kontrak/webhook sudah dialihkan |
| `{{T_CONTRACT_DB}}` | Contract | Arsip | Arsip | Current | Hapus kolom/flag/adapter lama pada rilis terpisah; CHANGELOG `Removed` |

### 7.8 Routing gateway, dokumentasi dan SDK multi-versi, Pact, observability

**Routing per versi** `[Rekomendasi peneliti/tim]`:

- Gateway memetakan prefix `/api/v1`, `/api/v2`, `/api/v3` ke target/service yang sama atau deployment terpisah; setiap route membawa label `api_version`, `route_id`, `consumer_id`, dan correlation ID. `[Praktik industri]` [Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design) merekomendasikan propagation `Correlation-ID`/`X-Request-ID`/`X-Trace-ID` untuk end-to-end visibility.
- Canary/blue-green/rolling berada **di bawah** pemetaan versi: V3 dapat di-canary tanpa mengubah V1/V2. `[Praktik industri]` [AWS API Gateway, "Set up a canary release deployment"](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md) memisahkan rasio traffic serta log/metrik canary; [Kubernetes Docs, "Deployments"](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) menyediakan rolling update dan rollback.
- Untuk versi berbasis header/media type, gateway wajib meneruskan header ke upstream dan cache wajib `Vary`; untuk path, URI menjadi pembeda alami. `[Standar resmi]` [RFC 9111, HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111.html); `[Praktik industri]` [Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design).

**Dokumentasi dan SDK multi-versi** `[Rekomendasi peneliti/tim]`. `[Standar resmi]` [OpenAPI Specification 3.2.0](https://spec.openapis.org/oas/v3.2.0.html), [OpenAPI 3.2.1](https://spec.openapis.org/oas/v3.2.1.html), [OpenAPI Specification 3.1.0](https://spec.openapis.org/oas/v3.1.0.html) mengizinkan OAD multi-document dengan referensi URI, merekomendasikan entry document `openapi.json`/`openapi.yaml`, dan memisahkan versi-versi di 7.3. `[Praktik industri]` [Zalando rules 101/116/215/218/219](https://opensource.zalando.com/restful-api-guidelines/) merekomendasikan OAS 3.1 untuk API baru, satu YAML self-contained, `x-api-id`, `x-audience`, dan SemVer pada `info.version`.

- Satu OAD → satu package SDK per major: `{{ORG}}-sdk-{{BAHASA}}-v1`, `...-v2`, `...-v3`; generated code jangan diedit manual. Dasar: `[Standar resmi]` [OpenAPI Specification 3.2.0 §2](https://spec.openapis.org/oas/v3.2.0.html) menyebut code-generation tools; `[Praktik industri]` [Stripe Docs](https://docs.stripe.com/api-versions) mem-pin API version lewat SDK.
- SDK `v1`/`v2` memuat deprecation warning dan tautan migration guide; SDK V3 menjadi default docs/quickstart.
- Versi SDK mengikuti SemVer sendiri; jangan samakan `sdk-v3@1.4.0` dengan `info.version` atau `/api/v3`.

**Observability dan alert per versi** `[Rekomendasi peneliti/tim]`, berdasarkan `[Praktik industri]` [AWS API Gateway canary](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md), [Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design), [Fowler, "Canary Release"](https://martinfowler.com/bliki/CanaryRelease.html):

| Sinyal | Label minimum | Alert contoh |
|---|---|---|
| `http_requests_total` | `api_version`, `route`, `method`, `status`, `consumer_id` | Lonjakan 4xx/5xx V3 vs baseline V2 > `{{AMBANG_ERROR}}` |
| `http_request_duration_seconds` | `api_version`, `canary`, `region` | p95/p99 V3 > `{{AMBANG_LATENCY}}` selama `{{JENDELA}}` |
| `api_deprecated_requests_total` | `api_version`, `consumer_id` | Masih ada konsumen prioritas tinggi V1 pada T−30 sunset |
| `api_version_request_ratio` | `api_version` | Share V1 tidak turun sesuai timeline |
| `dual_write_mismatch_total` | `entity`, `migration_id` | Drift > `{{AMBANG_DRIFT}}` |
| `contract_verification_result` | `consumer`, `provider`, `version` | `can-i-deploy` gagal |
| Business KPI | `api_version`, `canary` | Regresi signifikan → auto-reroute ke stable |

### 7.9 Checklist cutover dan kriteria rollback

**Checklist cutover zero downtime** `[Rekomendasi peneliti/tim]`; isi placeholder disetujui owner sebelum eksekusi:

- [ ] ADR path `/api/vN` disetujui, termasuk pengorbanan HATEOAS/version-scoped link dan penolakan `[Praktik industri]` [Zalando rule 114](https://opensource.zalando.com/restful-api-guidelines/).
- [ ] `support-policy.md` menetapkan N-1/N-2, `{{NOTICE_PERIOD}}`, tanggal `{{SUNSET_DATE}}`, dan pemilik metrik.
- [ ] OAD V3 tersedia, `info.version` terisi sebagai versi dokumen, `openapi` sesuai, `servers.url` menunjuk `/api/v3`.
- [ ] Compatibility diff OAD V3 terhadap baseline hijau; tidak ada perubahan kategori "Breaking" tanpa major/ADR.
- [ ] Satu SDK per major ter-generate; V1/V2 memuat deprecation warning; V3 menjadi default quickstart.
- [ ] Domain model kanonik tunggal; adapter/presenter per versi di lapisan terluar.
- [ ] Fase Expand: kolom/tabel/index baru nullable atau kompatibel; image lama masih bisa menulis.
- [ ] Backfill idempotent selesai; parity `{{JUMLAH_BARIS_LAMA}}` vs `{{JUMLAH_BARIS_BARU}}` dalam `{{AMBANG_DRIFT}}`.
- [ ] Dual-write aktif, reconciliation hijau, tidak ada orphan write.
- [ ] Dual-read/shadow: selisih respons di bawah `{{AMBANG_PARITY}}`.
- [ ] Feature flag `{{FLAG_V3}}` terkonfigurasi; rencana rilis supplier vs klien terdokumentasi.
- [ ] Pact expectations terdaftar; `can-i-deploy` hijau untuk seluruh consumer production (`--all prod` bila mobile).
- [ ] Canary 1%→5%→25%→50%→100% dengan log/metrik terpisah; error budget terpenuhi.
- [ ] SLO V3 hijau selama `{{JENDELA_OBSERVASI}}`; `progressDeadlineSeconds` tidak terlampaui.
- [ ] Gateway memberi label `api_version`, `route_id`, `consumer_id`, correlation ID; alert per versi aktif.
- [ ] `Deprecation`, `Sunset`, `Link` terpasang dengan urutan benar; `Sunset` tidak lebih awal dari `Deprecation`.
- [ ] `deprecated: true` pada Operation/Parameter V1/V2; CHANGELOG, release notes, email/portal, dashboard konsumen, migration guide terbit.
- [ ] Pengingat T−90/T−30/T−7 terjadwal; daftar consumer tersisa dan daftar exception tertanda tangan siap.
- [ ] Metrik `api_version` menunjukkan request share dan unique consumer sesuai ambang; webhook pin dan kontrak enterprise dialihkan.
- [ ] **Dual-write masih ON** saat switch sehingga jalur rollback tersedia.
- [ ] Rencana Contract pada rilis terpisah: `410 Gone`/`404` terdokumentasi, backup tersedia, arsip OAD, ADR `superseded`, CHANGELOG `Removed`.

**Kriteria rollback** `[Rekomendasi peneliti/tim]`, diturunkan dari tabel metrik 7.6 dan tabel sinyal 7.8:

| Pemicu | Tindakan | Dasar |
|---|---|---|
| 4xx/5xx V3 > `{{AMBANG_ERROR}}` atau p95/p99 > `{{AMBANG_LATENCY}}` | Alihkan canary kembali ke stable; turunkan rasio ke 0 | `[Praktik industri]` [Fowler, "Canary Release"](https://martinfowler.com/bliki/CanaryRelease.html), [AWS API Gateway canary](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md) |
| `dual_write_mismatch_total` / drift > `{{AMBANG_DRIFT}}` | Hentikan switch, kembalikan sumber baca ke struktur lama, jalankan reconciliation | Fase dual-write/dual-read pada 7.5 |
| `can-i-deploy` gagal | Blokir deploy, perbaiki kontrak consumer/provider | `[Praktik industri]` [Pact Docs, "Can I Deploy"](https://docs.pact.io/pact_broker/can_i_deploy) |
| Rollout macet / `progressDeadlineSeconds` terlampaui | Rollback Deployment ke revisi stabil | `[Praktik industri]` [Kubernetes Docs, "Deployments"](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) |
| Regresi Business KPI signifikan | Auto-reroute ke stable | Tabel sinyal 7.8 |
| Sunset terlalu dini: masih ada consumer prioritas tinggi / tiket aktif | Tunda pemadaman, perpanjang notice, catat pengecualian berdokumen | `[Standar resmi]` [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html) hint; kriteria dukungan 7.6 |

### 7.10 Anti-pattern

`[Rekomendasi peneliti/tim]` dari seluruh temuan di atas:

- Mengklaim path `/api/vN` sebagai **kewajiban standar HTTP/REST**; `[Standar resmi]` [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html) justru memisahkan resource dari representasi, dan keputusan ini lahir dari constraint brief.
- Tertukar **RFC 8594 = `Sunset`** dan **RFC 9745 = `Deprecation`**, atau menetapkan `Sunset` lebih awal daripada `Deprecation` ([Standar resmi] [RFC 9745 §4](https://www.rfc-editor.org/rfc/rfc9745.html)).
- Menyamakan `openapi`, `info.version`, `/api/vN`, dan versi SDK; atau menulis `info.version: "V3"` otomatis.
- Memakai custom header selektor versi tanpa `Vary`, sehingga cache mencampur respons ([Standar resmi] [RFC 9111](https://www.rfc-editor.org/rfc/rfc9111.html)).
- Menaikkan major untuk perubahan additive, atau sebaliknya menambah required field/response enum/format error pada major berjalan ([Praktik industri] [Zalando rules 106–108](https://opensource.zalando.com/restful-api-guidelines/), [Google AIP-180](https://google.aip.dev/180)).
- Mengubah pagination default atau bentuk page object tanpa major baru, lalu klien lama mengira hasil sudah lengkap.
- Menjadikan `apiVersion` di body sebagai penentu routing, atau mencampur metadata envelope dengan domain.
- Mengandalkan rolling/canary/blue-green **tanpa** Expand–Contract pada database; keduanya bukan jaminan kompatibilitas.
- Melakukan drop/rename kolom, atau Contract sebelum backfill/parity/metrik nol; serta tidak pernah menuntaskan Contract ([Praktik industri] [Fowler, "Parallel Change"](https://martinfowler.com/bliki/ParallelChange.html)).
- Mematikan dual-write sebelum jendela observasi selesai, sehingga rollback tidak mungkin.
- Menganggap header lifecycle sebagai jaminan pemadaman dan menggantikan komunikasi manusia + metrik dengannya ([Standar resmi] [RFC 8594 §3, §8](https://www.rfc-editor.org/rfc/rfc8594.html), [RFC 9745 §5, §7](https://www.rfc-editor.org/rfc/rfc9745.html)).
- Menetapkan N-1, `{{NOTICE_PERIOD}}`, persentase canary, atau ambang sunset seolah-olah angka baku dari RFC.
- HATEOAS link tanpa versi, atau mengedit generated SDK secara manual.
- Menetapkan tanggal sunset tanpa keputusan berbasis metrik `api_version`, webhook pin, dan kontrak enterprise.

### 7.11 Konflik sumber dan keterbatasan (Gaps)

**Konflik sumber.** `[Rekomendasi peneliti/tim]` Catatan tidak memilih salah satu panduan industri sebagai "standar"; ia memilih path karena constraint bisnis brief.

| Pihak | Posisi | Sumber |
|---|---|---|
| Zalando | `MUST use media type versioning`, `MUST not use URL versioning`, hanya untuk payload schema; versi dinyatakan bersama `Content-Type`/`Accept` | `[Praktik industri]` [Zalando RESTful API Guidelines, rules 113–114](https://opensource.zalando.com/restful-api-guidelines/) |
| Microsoft | Menjabarkan URI/query/header/media-type; URI sederhana-eksplisit dan cache-friendly, tetapi membebani routing serta HATEOAS; header/media type dapat menggandakan data di server-side cache | `[Praktik industri]` [Microsoft Learn, "Best practices for RESTful web API design"](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design) |
| Google Cloud/Apigee | Membedakan format vs entity versioning; entity version di URL dan di body; menyarankan `Accept-Version`/`Content-Version` untuk format; **menentang** versi di `Accept`/`Content-Type` | `[Praktik industri]` [Google Cloud Blog, "API design: Which version of versioning is right for you?"](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you) |
| Zalando vs Stripe | Stripe menganggap penambahan event type/response property kompatibel dengan tolerant reader; Zalando melarang perluasan enum output dan menyarankan open-ended values | `[Praktik industri]` [Stripe Docs](https://docs.stripe.com/api-versions), [Zalando rule 107/108](https://opensource.zalando.com/restful-api-guidelines/) |

Ketiga posisi pertama adalah `[Praktik industri]`, bukan standar IETF; pilihan harus didokumentasikan per API dalam ADR. `[Standar resmi]` [RFC 9110, HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) hanya memberi kerangka resource/representasi dan content negotiation.

**Inferensi yang dinyatakan** `[Rekomendasi peneliti/tim]`: path dipilih karena constraint brief, bukan karena HTTP/REST mewajibkannya; zero downtime mensyaratkan kompatibilitas image lama/baru sekaligus pada database dan kontrak; setiap versi tambahan menaikkan biaya kognitif dan operasional sehingga major baru hanya boleh muncul setelah opsi additive dan deprecation gagal; header lifecycle memberi sinyal machine-readable tetapi keputusan mematikan versi tetap memerlukan komunikasi dan metrik konsumen.

**Gaps / keterbatasan** `[Rekomendasi peneliti/tim]`:

- Tidak ditemukan standar IETF/ISO yang menetapkan kebijakan N-1/N-2, lama notice period, persentase canary, atau ambang metrik sunset; **semua angka sengaja berupa placeholder** dan wajib disetujui owner.
- Panduan industri bertentangan sebagaimana tabel di atas; tidak ada rujukan tunggal yang dapat dijadikan kepatuhan normatif.
- **Keterbatasan verifikasi PayPal/ASP.NET:** pada rentang catatan yang menjadi batas kerja bagian ini, yang tercatat eksplisit adalah halaman wiki **ASP.NET API versioning tidak dapat diverifikasi karena tampilan login GitHub**; rujukan **PayPal** tidak tersedia dalam rentang sumber yang diizinkan, sehingga bagian ini tidak mengklaim isi, tanggal, maupun URL-nya.
- Tanggal rilis **OAS 3.2.1 tidak diverifikasi**; hanya keberadaan versi patch-nya yang tercantum pada daftar versi resmi ([Standar resmi] [OpenAPI 3.2.1](https://spec.openapis.org/oas/v3.2.1.html)).
- Contoh endpoint, matriks V1/V2/V3, cuplikan routing/OAD, dan timeline bersifat ilustrasi operasional dengan placeholder, bukan kontrak produksi atau kalender yang sudah disepakati.

### 7.12 Sumber bagian ini

**[Standar resmi]**

- [RFC 9110, HTTP Semantics, STD 97](https://www.rfc-editor.org/rfc/rfc9110.html)
- [RFC 9111, HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111.html)
- [RFC 8594 = `Sunset` HTTP response header](https://www.rfc-editor.org/rfc/rfc8594.html)
- [RFC 9745 = `Deprecation` HTTP response header](https://www.rfc-editor.org/rfc/rfc9745.html)
- [RFC 9457, Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html)
- [OpenAPI Specification 3.1.0](https://spec.openapis.org/oas/v3.1.0.html)
- [OpenAPI 3.1.0, Operation Object / Parameter Object](https://spec.openapis.org/oas/v3.1.0.html#operation-object)
- [OpenAPI Specification 3.2.0](https://spec.openapis.org/oas/v3.2.0.html)
- [OpenAPI 3.2.1](https://spec.openapis.org/oas/v3.2.1.html)

**[Praktik industri]**

- [Microsoft Learn, "Best practices for RESTful web API design"](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design)
- [Zalando RESTful API and Event Guidelines](https://opensource.zalando.com/restful-api-guidelines/)
- [Google Cloud Blog, "API design: Which version of versioning is right for you?"](https://cloud.google.com/blog/products/api-management/api-design-which-version-of-versioning-is-right-for-you)
- [Stripe Docs, "How API versioning works"](https://docs.stripe.com/api-versions)
- [Google AIP-180, Backwards compatibility](https://google.aip.dev/180)
- [Martin Fowler, "Parallel Change"](https://martinfowler.com/bliki/ParallelChange.html)
- [Martin Fowler, "Canary Release"](https://martinfowler.com/bliki/CanaryRelease.html)
- [Kubernetes Docs, "Deployments"](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [AWS API Gateway, "Set up a canary release deployment"](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.md)
- [Pact Docs, "Can I Deploy"](https://docs.pact.io/pact_broker/can_i_deploy)
- [Pact Docs, "CI/CD Setup Guide"](https://docs.pact.io/pact_nirvana)
- [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html)
- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)
- [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/)

**[Rekomendasi peneliti/tim]** — seluruh keputusan desain, tabel turunan, urutan deploy, matriks V1/V2/V3, timeline, checklist, kriteria rollback, dan anti-pattern pada 7.1–7.11 merupakan sintesis tim dari sumber di atas; seluruh ambang, tanggal, dan nama variabel bertanda `{{...}}` adalah placeholder yang belum ditetapkan.
