# Contributing to DeDi

Thanks for contributing.

This repository is still evolving, so the highest-value contributions are the ones that reduce ambiguity, improve implementability, and make trust assumptions easier to evaluate.

## High-value contribution areas

We especially welcome contributions that improve:

- developer onboarding and quickstart quality,
- schema clarity and consistency,
- realistic examples and lifecycle cases,
- protocol documentation and diagrams,
- conformance and validation guidance,
- ecosystem-specific mappings and comparison notes.

## Contribution principles

A strong change usually does one or more of the following:

1. clarifies a field, flow, or lifecycle ambiguity,
2. adds or improves a realistic example,
3. keeps documentation, schema, and example changes aligned,
4. improves testability or machine readability,
5. reduces guesswork for implementers.

## Before you open a pull request

Please aim for focused, reviewable changes.

Before submitting:

1. update the relevant docs,
2. update sample and invalid examples when schema behavior changes,
3. update machine-readable catalogs when new schemas are added,
4. run the validation script locally if you changed schemas, examples, or the OpenAPI file.

## Local validation

```bash
python -m pip install jsonschema openapi-spec-validator PyYAML
python scripts/validate_artifacts.py
```

## Pull request checklist

- [ ] The change is scoped and explained clearly.
- [ ] Documentation is updated where needed.
- [ ] Examples are aligned with schema expectations.
- [ ] Validation passes locally.
- [ ] Compatibility impact is described for protocol or schema changes.

## Issues and proposals

For substantive protocol changes, open an issue or pull request that explains:

- the current ambiguity or pain point,
- the proposed behavior,
- the compatibility impact,
- and the docs or examples that need to move together.
