# Validation guide

This document explains how to validate DeDi artifacts locally and in CI, and how to interpret the results. It is the companion to the [conformance profiles](profiles.md).

## Quick start

```bash
python -m pip install jsonschema openapi-spec-validator PyYAML
python scripts/validate_artifacts.py
```

A clean run prints:

```
All validations passed.
```

Any failure prints the schema name and the first validation error. Fix the offending file and re-run.

## What the script checks

`scripts/validate_artifacts.py` performs three checks:

1. **Valid examples pass** — each `examples/{name}/sample.json` is validated against its corresponding schema and must produce no errors.
2. **Invalid examples fail** — each `examples/{name}/invalid.json` must produce at least one validation error. If the invalid example passes, the schema is too permissive.
3. **OpenAPI spec is valid** — `api/openapi.yaml` is validated by `openapi-spec-validator`.

## Validating a single schema manually

```python
import json
from jsonschema import Draft7Validator

schema  = json.loads(open("schemas/public_key.json").read())
payload = json.loads(open("examples/public-key/sample.json").read())

validator = Draft7Validator(schema)
errors = sorted(validator.iter_errors(payload), key=lambda e: e.path)
for err in errors:
    print(err.path, err.message)
```

## Validating a new payload

If you are testing a payload produced by your own system:

```bash
python - <<'EOF'
import json
from jsonschema import Draft7Validator

schema  = json.loads(open("schemas/membership.json").read())
payload = json.loads(open("/path/to/my-payload.json").read())

errs = sorted(Draft7Validator(schema).iter_errors(payload), key=lambda e: e.path)
if errs:
    for e in errs: print(list(e.path), e.message)
else:
    print("Payload is valid.")
EOF
```

## CI validation

The repository ships a GitHub Actions workflow at `.github/workflows/validate.yml` that runs the validation script on every push and pull request to `main`. Pull requests that fail validation should not be merged.

## Conformance evidence for implementations

If you are claiming baseline DeDi conformance, the expected evidence is:

| Requirement | Evidence |
|---|---|
| Namespace query endpoint reachable | `curl` output or test log |
| Lookup endpoint reachable | `curl` output or test log |
| Schema validation on write | Source code, unit test, or CI log |
| Valid sample payloads pass | `validate_artifacts.py` output |
| Invalid payloads correctly fail | `validate_artifacts.py` output |
| Freshness and revocation semantics documented | Link to operator or verifier guide |

For the recommended conformance profile, also provide:

| Requirement | Evidence |
|---|---|
| OpenAPI contract published | Link to hosted or repository file |
| Historical record retention policy documented | Link to operator guide |
| Automated validation in CI | CI badge or log link |

## Adding a new schema

When adding a new schema to the repository, the validation script must be updated to include it. The steps are:

1. Add the schema to `schemas/`.
2. Add valid and invalid example payloads to `examples/{schema-name}/`.
3. Add the schema and example paths to `machine-readable/schema-catalog.json`.
4. Add the key to `schema_files` and `example_map` in `scripts/validate_artifacts.py`.
5. Run the validation script and confirm it passes.

## Related

- [Conformance profiles](profiles.md)
- [Test matrix](test-matrix.md)
- [Contributing guide](../CONTRIBUTING.md)
- [Validation script](../scripts/validate_artifacts.py)
