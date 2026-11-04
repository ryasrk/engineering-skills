> Sumber: OpenAPI Specification 3.1.0 — https://spec.openapis.org/oas/v3.1.0.html
> Catatan: Dipakai saat memelihara kontrak OpenAPI untuk major version V1 yang sudah deprecated.
# docs/api/v1/openapi.yaml
openapi: 3.1.0
info:
  title: "{{NAMA_API}} V1"
  version: "{{INFO_VERSION_V1}}"           # versi DOKUMEN OAD, bukan "V1" otomatis
  description: "Status: {{STATUS_V1}}. Lihat docs/api/lifecycle/deprecation.md"
  x-api-id: "{{UUID_API_IMMUTABLE}}"
  x-audience: "{{AUDIENCE}}"
servers:
  - url: "https://{{API_HOST}}/api/v1"
paths:
  /orders/{orderId}:
    get:
      operationId: getOrderV1
      deprecated: true
      parameters:
        - name: orderId
          in: path
          required: true
          schema: { type: string }
      responses:
        "200":
          description: "Order V1"
          content:
            application/json:
              schema:
                type: object
                required: [id, total]
                properties:
                  id: { type: string }
                  total: { type: number }
        "404":
          description: "Not found"
          content:
            application/problem+json:
              schema: { $ref: "#/components/schemas/Problem" }
components:
  schemas:
    Problem:
      type: object
      properties:
        type: { type: string, format: uri }
        title: { type: string }
        status: { type: integer }
        detail: { type: string }
        instance: { type: string }
