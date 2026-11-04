> Sumber: OpenAPI Specification 3.1.0 — https://spec.openapis.org/oas/v3.1.0.html
> Catatan: Dipakai saat memelihara kontrak OpenAPI untuk major version V2 dalam masa migrasi ke V3.
# docs/api/v2/openapi.yaml
openapi: 3.1.0
info:
  title: "{{NAMA_API}} V2"
  version: "{{INFO_VERSION_V2}}"
  x-api-id: "{{UUID_API_IMMUTABLE}}"
  x-audience: "{{AUDIENCE}}"
servers:
  - url: "https://{{API_HOST}}/api/v2"
paths:
  /orders/{orderId}:
    get:
      operationId: getOrderV2
      deprecated: true
      parameters:
        - name: orderId
          in: path
          required: true
          schema: { type: string }
      responses:
        "200":
          description: "Order V2: amount object replaces numeric total"
          content:
            application/json:
              schema:
                type: object
                required: [id, amount, status]
                properties:
                  id: { type: string }
                  amount:
                    type: object
                    required: [value, currency]
                    properties:
                      value: { type: string }
                      currency: { type: string }
                  status: { type: string, enum: ["CREATED", "PAID", "CANCELLED"] }
