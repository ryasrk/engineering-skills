> Sumber: OpenAPI Specification 3.2.0 — https://spec.openapis.org/oas/v3.2.0.html
> Catatan: Dipakai saat menyimpan tiga kontrak OpenAPI terpisah untuk major version V1, V2, dan V3.
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

# docs/api/v3/openapi.yaml
openapi: 3.2.0
info:
  title: "{{NAMA_API}} V3"
  version: "{{INFO_VERSION_V3}}"
  x-api-id: "{{UUID_API_IMMUTABLE}}"
  x-audience: "{{AUDIENCE}}"
servers:
  - url: "https://{{API_HOST}}/api/v3"
paths:
  /orders/{orderId}:
    get:
      operationId: getOrderV3
      parameters:
        - name: orderId
          in: path
          required: true
          schema: { type: string }
      responses:
        "200":
          description: "Order V3: cursor pagination + monetary object + RFC 9457 errors"
          content:
            application/json:
              schema:
                type: object
                required: [id, amount, status, links]
                properties:
                  id: { type: string }
                  amount: { $ref: "#/components/schemas/Money" }
                  status: { type: string, enum: ["CREATED", "PAID", "CANCELLED", "REFUNDED"] }
                  links:
                    type: object
                    required: [self, next]
                    properties:
                      self: { type: string, format: uri }
                      next: { type: string, format: uri }
        "404":
          description: "Problem details"
          content:
            application/problem+json:
              schema: { $ref: "#/components/schemas/Problem" }
components:
  schemas:
    Money:
      type: object
      required: [value, currency]
      properties:
        value: { type: string }
        currency: { type: string }
    Problem:
      type: object
      properties:
        type: { type: string, format: uri }
        title: { type: string }
        status: { type: integer }
        detail: { type: string }
        instance: { type: string }
