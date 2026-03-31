---
title: "Discovery Conventions"
nav_order: 1
parent: "Build & Integrate"
---
# Discovery conventions

This document defines how clients locate namespaces, directories, and schema usage in a DeDi deployment. Following these conventions makes integration predictable and removes the need for bespoke discovery logic.

## 1. Namespace discovery

A namespace is the top-level trust anchor in DeDi. Clients discover a namespace by querying:

```
GET /dedi/query/{namespace}
```

The response envelope identifies the registries available under that namespace and the schemas they use.

**Example:**
```bash
curl -s "https://api.dedi.global/dedi/query/example.org"
```

Expected response shape:
```json
{
  "message": "ok",
  "data": {
    "namespace": "example.org",
    "registries": [
      { "name": "public-key", "schema": "public_key" },
      { "name": "membership", "schema": "membership" },
      { "name": "revoke",     "schema": "revoke" }
    ]
  },
  "timestamp": "2026-03-31T00:00:00Z"
}
```

## 2. Registry discovery

Once you know a namespace, enumerate the records inside a specific registry:

```
GET /dedi/query/{namespace}/{registry}?page=1&page_size=20
```

**Example:**
```bash
curl -s "https://api.dedi.global/dedi/query/example.org/public-key?page=1&page_size=20"
```

## 3. Record lookup

Retrieve a specific record by its identifier:

```
GET /dedi/lookup/{namespace}/{registry}/{record_id}
```

**Example:**
```bash
curl -s "https://api.dedi.global/dedi/lookup/example.org/public-key/did:example:merchant-123"
```

## 4. Schema discovery

Every record in a DeDi response includes a `schema` field in the envelope. Use this to determine which JSON Schema to validate against. The machine-readable schema catalog at [`machine-readable/schema-catalog.json`](../machine-readable/schema-catalog.json) lists all schemas with their paths.

**Programmatic schema lookup:**
```python
import json, pathlib
catalog = json.loads(pathlib.Path("machine-readable/schema-catalog.json").read_text())
schema_paths = {s["name"]: s["path"] for s in catalog["schemas"]}
# schema_paths["public_key"] -> "schemas/public_key.json"
```

## 5. Namespace authority discovery

Clients that need to validate namespace authority (not just retrieve records) should look for the authority model documentation published by the operator. The protocol requires this to be documented; see [protocol-spec.md § 3](protocol-spec.md) for the authority model requirements.

## 6. Historical record discovery

To list historical versions of a record:

```
GET /dedi/versions/{namespace}/{registry}/{record_id}
```

To retrieve a record as it existed at a specific point in time:

```
GET /dedi/lookup/{namespace}/{registry}/{record_id}?as_on=2025-01-01T00:00:00Z
```

## 7. Convention summary

| Goal | Endpoint pattern |
|---|---|
| List registries in a namespace | `GET /dedi/query/{namespace}` |
| List records in a registry | `GET /dedi/query/{namespace}/{registry}` |
| Fetch a specific record | `GET /dedi/lookup/{namespace}/{registry}/{record_id}` |
| List historical versions | `GET /dedi/versions/{namespace}/{registry}/{record_id}` |
| Fetch a record at a point in time | `GET /dedi/lookup/{namespace}/{registry}/{record_id}?as_on={datetime}` |

## 8. Client discovery checklist

- [ ] Confirm the base URL of the registry operator.
- [ ] Issue a namespace query to enumerate available registries.
- [ ] Record which schemas each registry uses.
- [ ] Verify the schema references match entries in `machine-readable/schema-catalog.json`.
- [ ] Define which namespaces your application trusts before issuing lookups.

## Related

- [API contract](../api/openapi.yaml)
- [Schema catalog](../machine-readable/schema-catalog.json)
- [Core concepts](core-concepts.md)
- [Architecture](architecture.md)
- [Verifier guide](verifier-guide.md)
