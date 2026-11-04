---
name: api-versioning
description: "Use when designing, migrating, or deprecating REST APIs across multiple versions (V1, V2, V3) with zero downtime and versions embedded in the API path. Also use when executing Expand-Contract database migrations, configuring RFC 9745 Deprecation and RFC 8594 Sunset headers, or writing OpenAPI multi-version specifications."
---

# Zero-downtime API versioning (V1, V2, V3)

Design, run, and migrate versioned APIs concurrently without service interruption, consumer breaking changes, or deployment downtime.

## Work from the source artefact

1. Read `references/08-api-versioning-inti.md` for the core architecture, routing rules, and Expand-Contract execution phases. Read `references/09-api-checklist-sumber.md` for standard corrections, cutover checklists, and cited RFC specifications.
2. For OpenAPI specifications: copy `assets/06-OpenAPI-Multi-Versi.md` as the master guide, and instantiate version-specific contracts using `assets/06-OpenAPI-Multi-Versi-V1.md`, `06-OpenAPI-Multi-Versi-V2.md`, and `06-OpenAPI-Multi-Versi-V3.md`.
3. For gateway and traffic control: configure reverse proxy routes using `assets/06-Routing-Gateway-Nginx.md` and track version compatibility via `assets/06-Matriks-Endpoint-Versi.md`.
4. For zero-downtime database and schema changes: execute the 5-phase procedure in `assets/06-Runbook-Expand-Contract.md`.
5. For version deprecation, communication, and sunset:
   - `assets/06-Header-Lifecycle-Deprecation-Sunset.md` — RFC 9745 and RFC 8594 HTTP response headers.
   - `assets/06-Komunikasi-Konsumen-Deprecation.md` — consumer notification schedule.
   - `assets/06-Kriteria-Sunset-Metrik.md` — metric-driven decommissioning criteria.
   - `assets/06-Observability-Alert-Per-Versi.md` — metrics, telemetry, and alerting partitioned by `api_version`.
   - `assets/06-Timeline-Migrasi-V1-V2-V3.md` — multi-quarter migration roadmap.
   - `assets/06-Checklist-Zero-Downtime.md` — pre-cutover, traffic switch, and rollback verification.

## Decisions that materially change the result

- **Primary recommendation for embedded versioning:** Embed the major version directly in the URI path (`/api/v1`, `/api/v2`, `/api/v3`). Maintain **one dedicated OpenAPI Description (OAD) and one client SDK per major version**. Path embedding provides optimal discoverability, deterministic gateway routing, transparent edge caching, and isolated documentation.
- **Differentiate four distinct version identifiers:**
  1. `openapi` (e.g. `3.1.0`) — version of the specification grammar.
  2. `info.version` (e.g. `1.3.2`) — release version of the OpenAPI document itself.
  3. `/api/vN` — major contract surface exposed to consumers.
  4. Client SDK version (e.g. `v2.4.0`) — language package distribution version.
- **Standard corrections for lifecycle headers:**
  - **RFC 8594 defines the `Sunset` header** (contains an HTTP-date specifying when the resource will be retired).
  - **RFC 9745 defines the `Deprecation` header** (published March 2025 Standards Track, specifies the date or timestamp when the resource became deprecated).
  - Both headers are client hints. RFC 9745 explicitly **forbids a `Sunset` timestamp from being earlier than `Deprecation`**.
- **Additive vs breaking change policy:**
  - *Additive (minor/patch, same major version):* Adding optional request fields, adding new response fields, introducing new endpoints, or relaxing validation constraints.
  - *Breaking (requires a new `/api/v(N+1)` version):* Renaming or removing fields, adding mandatory request fields, altering field data types or response enum options, modifying error payload structures, or changing pagination mechanics.
- **Expand-Contract procedure for zero downtime:**
  1. *Expand:* Deploy additive database columns and schemas; deploy service supporting both old and new data fields.
  2. *Backfill:* Asynchronously populate historical data into newly expanded structures.
  3. *Dual-write / dual-read:* Write to both representations; read from new with fallback to legacy.
  4. *Canary / switch:* Gradually route consumer traffic to `/api/v2` via API gateway and feature flags while `/api/v1` remains fully operational.
  5. *Contract:* After sunset period expires and legacy traffic metrics reach near-zero, decommission `/api/v1` routes and drop deprecated database columns.
- **Metric-based sunset gating:** Never turn off a legacy API version based solely on an arbitrary calendar date. Decommissioning requires traffic telemetry confirming that traffic on `/api/v1` has dropped below the agreed threshold (e.g. < 0.1% of total requests) and remaining consumers have acknowledged migration.

## Zero-downtime cutover and rollback checklist

- Backward compatibility verified with consumer-driven contract tests (Pact `can-i-deploy`).
- Gateway routes both versions simultaneously (`/api/v1` -> v1 handler, `/api/v2` -> v2 handler).
- Automated rollback triggers defined (e.g. 5xx rate > 0.5% or p99 latency > 300ms over 5 minutes immediately reverts traffic).
- Deprecation notices include RFC 9745 `Deprecation` header, RFC 8594 `Sunset` header, and `Link` relation to migration documentation.
