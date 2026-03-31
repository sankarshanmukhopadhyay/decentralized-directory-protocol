# Conformance

Conformance matters because a protocol without testable expectations turns interoperability into interpretation.

This directory defines the conformance surface for DeDi-compatible implementations.

## Included here

- [Conformance profiles](profiles.md) — baseline and recommended compatibility expectations
- [Validation guide](validation-guide.md) — how to run and interpret artifact validation locally and in CI
- [Test matrix](test-matrix.md) — a per-capability checklist for assessing minimum support

## Quick validation

```bash
python -m pip install jsonschema openapi-spec-validator PyYAML
python scripts/validate_artifacts.py
```

A clean run prints `All validations passed.`

## CI

The repository ships a GitHub Actions workflow at `.github/workflows/validate.yml` that runs on every push and pull request. Implementations that wish to claim conformance should run equivalent checks in their own CI.
