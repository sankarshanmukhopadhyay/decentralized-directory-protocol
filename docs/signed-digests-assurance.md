---
title: Signed digests assurance
nav_order: 7
permalink: /signed-digests-assurance/
---

# Signed digests: fork-local assurance

**Status:** partial implementation, experimental and non-normative. This workbench does not issue upstream DeDi certification.

Upstream [PR #38](https://github.com/LF-Decentralized-Trust-labs/decentralized-directory-protocol/pull/38) permits an optional inline `files[].digest` or an independently signed document named by manifest `digests`. The external document's entry takes precedence if both exist; a registry without either commitment has no *cross-document digest commitment*. Its own signature must be checked independently.

## What is implemented

The fork validates the upstream digest schema and the illustrated external digest document's domain, declared registry names, and current manifest key identity. `scripts/verify_publishing_crypto.py` provides signature verification using Ed25519 detached JWS over RFC 8785 JCS; digest verification selects the external commitment first, falls back to inline only when the external source contains no entry, and records `not-committed` rather than treating missing commitment as integrity verified.

When a digest mismatch occurs, the helper can refresh the external document **once**. It verifies the refreshed signature, current manifest signing-key membership and freshness before trusting the new commitment. Failure to refresh, an invalid signature, stale digest document, or a persistent mismatch fails closed. The caller is responsible for authenticating the manifest through the established manifest proof verification and checking its freshness before calling this helper.

The upstream illustrative `examples/dedi.digests.json` signature is **not cryptographically valid**. The deterministic tests generate their own signed data and must not be confused with that illustrative document.

## Reproduce

```sh
make setup
python -m unittest discover -s tests -p 'test_signed_digests.py'
make conformance
```

The new tests cover external precedence, inline fallback, no commitment, tampering, wrong domain, removed signing key, expiration, success after refresh, persistent mismatch, failed refresh and malformed algorithms. These are **fork-local** tests and do not establish upstream conformance.

## Known gaps

- Upstream Git commit ancestry is not yet synchronized to the current head; the files were reconciled against `4804d835d2d0109781536b629133a592d0a08590`, whereas existing conformance evidence remains pinned to `72d913fb4d17507891a6fea5db1f49ef7b3f461d`.
- The digest selection/refresh helper is not yet connected to the publisher→indexer→verifier scenario. The scenario's existing evidence cannot be interpreted as digests-document coverage.
- Dedicated rollback, cache race, clock skew, live HTTP/TLS and multi-indexer behaviors are not yet established.
- The new test cases are currently reported by a suite-level conformance runner step, not as individually attributed profile check results.

Track completion and evidence in [issue #9](https://github.com/sankarshanmukhopadhyay/decentralized-directory-protocol/issues/9).
