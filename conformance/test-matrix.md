# Test matrix

| Control | Description | Asset |
|---|---|---|
| DDP-RES-001 | Query endpoint responds with deterministic collection shape | `conformance/tests/resolution/basic-query.yaml` |
| DDP-RES-002 | Lookup endpoint returns schema-declared payload | `conformance/tests/resolution/basic-lookup.yaml` |
| DDP-SEC-001 | Returned `public-key` payload validates against schema | `conformance/tests/integrity/schema-validation.yaml` |
| DDP-LIF-001 | Revocation payload validates against schema | `conformance/tests/revocation/revocation-entry.yaml` |
| DDP-GOV-001 | Delegation artifact is valid JSON Schema | `governance/delegation-schema.json` |
