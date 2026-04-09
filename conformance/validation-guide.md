# Validation guide

## Local validation

Run:

```bash
python scripts/validate_artifacts.py
```

This validates:

- JSON Schemas and sample payloads
- OpenAPI structure
- conformance profile YAML
- conformance test definitions
- conformance vectors
- governance schema JSON
- evidence artifact JSON

## Quickstart validation

Run:

```bash
python reference-impl/server/server.py
python scripts/query_and_verify.py
```

This performs a real query and lookup against the local reference implementation and writes `evidence/quickstart-run.json`.

## Interpreting evidence

Evidence artifacts should make it possible to answer:

- which test or flow was run,
- what inputs were used,
- what output was received,
- whether validation passed,
- and when the run occurred.
