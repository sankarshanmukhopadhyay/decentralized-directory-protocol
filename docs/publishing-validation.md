# Executable publishing validation

This fork includes an **experimental, non-normative publishing profile** that turns part of the synchronized upstream origin-hosted publishing model into executable checks.

The upstream source pinned for this profile is:

- repository: `LF-Decentralized-Trust-labs/decentralized-directory-protocol`
- commit: `72d913fb4d17507891a6fea5db1f49ef7b3f461d`
- synchronized into this fork: 2026-08-22

The upstream project remains authoritative for DeDi protocol semantics. This profile is fork-local evaluation material.

## What the profile checks

Running:

```bash
python scripts/validate_artifacts.py
```

now exercises the origin-hosted publishing examples in addition to the fork's existing schemas, OpenAPI contract, conformance vectors, governance schema, and evidence artifacts.

The publishing checks cover:

1. required manifest fields and presence of a publisher key;
2. binding of the manifest proof to a declared key;
3. uniqueness of registry names across referenced and inline entries;
4. DeDi file schema validation for hosted and inline files;
5. binding of each file to the manifest's publisher domain;
6. binding of each file's embedded publisher key to a manifest key;
7. binding of each file proof to its embedded publisher key;
8. uniqueness of record names within a registry; and
9. correspondence between hosted example files and manifest references.

The machine-readable profile is in [`conformance/profiles/publishing.yaml`](../conformance/profiles/publishing.yaml), and its test declaration is in [`conformance/tests/publishing/origin-hosted.yaml`](../conformance/tests/publishing/origin-hosted.yaml).

## What it does not yet check

The synchronized examples intentionally contain illustrative, non-valid JWS values. Accordingly, this profile does **not** claim cryptographic conformance.

The current increment also does not perform:

- detached JWS verification;
- JCS canonicalization tests;
- live retrieval from `/.well-known/dedi.index.json`;
- TLS origin-binding verification;
- digest recomputation for referenced files;
- freshness or stale-copy rejection using `next_update`; or
- negative tests for compromised, rotated, or removed publisher keys.

Those are appropriate follow-on increments because they require executable cryptographic fixtures and/or controlled network fixtures rather than shape-only examples.

## Why this is useful

Before this change, the synchronized publishing model existed mainly as specification text, schemas, and examples. The fork could preserve those artifacts but could not demonstrate that they remained mutually consistent as the repository evolved.

The publishing profile creates a minimum regression barrier: changes to the manifest, hosted files, schemas, or key relationships can now fail validation rather than silently drifting apart.

This is the development pattern the fork will use more broadly: preserve upstream authority, then add reproducible implementation and assurance surfaces around upstream behavior.