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

- Upstream ancestry has been reconciled through a two-parent Git merge against `4804d835d2d0109781536b629133a592d0a08590`. The conformance profile, runner and composed-scenario upstream references are aligned to that commit.
- The publisher→indexer→verifier scenario now runs a deterministic signed external-digest integration path and includes digest provenance and the effective authority expiry in its evidence. This is offline composed verification, not a live network deployment.
- Deterministic digests-document rollback policy vectors are included; cache races, clock skew, live HTTP/TLS and multi-indexer behavior remain outside executable coverage.
- New cases PUB-020 through PUB-027 have explicit bindings to executable test or scenario identifiers in conformance evidence. Older PUB-001 through PUB-019 remain marked `not-individually-attributed`; a passing suite-level step must not be interpreted as independent proof of each individual check.

Track completion and evidence in [issue #9](https://github.com/sankarshanmukhopadhyay/decentralized-directory-protocol/issues/9).
