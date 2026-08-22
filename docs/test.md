---
title: Test
nav_order: 5
permalink: /test/
has_children: false
---

# Test and evaluate DeDi

Use this path when you need to test an implementation, compare behavior against the fork-local profiles, reproduce CI results, or inspect machine-readable evidence.

## One-command evaluation

```bash
make conformance
```

The unified runner executes:

1. repository artifact and schema validation;
2. publishing cryptographic verification;
3. publishing lifecycle and freshness verification; and
4. the publisher → indexer → verifier scenario.

It then writes a schema-validated run record to:

`evidence/conformance-run.json`

## Test surfaces

| Surface | Start here |
|---|---|
| Profiles and check IDs | [`conformance/profiles/`](../conformance/profiles/) |
| Test declarations | [`conformance/tests/`](../conformance/tests/) |
| Positive/negative vectors | [`conformance/vectors/`](../conformance/vectors/) |
| Validation guidance | [`conformance/validation-guide.md`](../conformance/validation-guide.md) |
| Evidence contract | [Conformance evidence](conformance-evidence) |
| Evidence schema | [`schemas/conformance-evidence.schema.json`](../schemas/conformance-evidence.schema.json) |
| Three-role scenario | [Publisher → indexer → verifier](../examples/end-to-end/publisher-indexer-verifier/README.md) |

## What the publishing profile currently covers

The fork-local publishing profile now exercises four layers:

### Structural

Manifest/file shape, publisher-domain relationships, key bindings, unique registries and records, and hosted example consistency.

### Cryptographic

RFC 8785 JCS canonicalization, detached Ed25519 JWS verification, tamper detection, current-key enforcement, and referenced-file digest checks.

### Lifecycle

Freshness, inactive registries, rollback, rotation overlap, removed-key rejection, and bounded cached-authority behavior during refresh failure.

### Composition

The publisher → indexer → verifier scenario checks that verified authority and freshness constraints survive indexing and remain visible to the verifier's reliance decision.

## Reading results correctly

Passing this suite means the tested fork state satisfied the fork-local profile at the recorded repository and upstream refs. It does **not** mean that upstream DeDi has certified the implementation or adopted fork-local requirements.
