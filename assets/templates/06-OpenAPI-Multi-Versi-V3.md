> Sumber: OpenAPI Specification 3.2.0 — https://spec.openapis.org/oas/v3.2.0.html
> Catatan: Dipakai saat menerbitkan kontrak OpenAPI untuk major version V3 yang menjadi default.
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
