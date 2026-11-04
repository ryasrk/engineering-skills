> Sumber: RFC 9745, The Deprecation HTTP Response Header Field — https://www.rfc-editor.org/rfc/rfc9745.html
> Catatan: Dipakai saat mengumumkan deprecation dan sunset versi API lewat header respons HTTP.
# Header Respons Deprecation dan Sunset

HTTP/1.1 200 OK
Content-Type: application/json
Deprecation: @{{UNIX_TIMESTAMP_DEPRECATION_V2}}
Sunset: {{HTTP_DATE_SUNSET_V2}}
Link: <https://{{HOST_DOCS}}/api/lifecycle/deprecation>; rel="deprecation"; type="text/html"
Link: <https://{{HOST_DOCS}}/api/lifecycle/sunset>; rel="sunset"; type="text/html"
API-Version: V2
