# Cryptographic publishing verification

This fork extends the experimental publishing profile with real cryptographic fixtures and executable verification.

The profile remains **fork-local and non-normative**. It is pinned to upstream DeDi commit `72d913fb4d17507891a6fea5db1f49ef7b3f461d` and does not represent an upstream certification program.

## What is now executable

`make validate` performs both repository validation and cryptographic publishing verification.

The cryptographic path exercises:

- RFC 8785 JSON Canonicalization Scheme (JCS);
- detached compact JWS with the RFC 7797 `b64=false` protected-header form;
- Ed25519 signature verification from the publisher JWK;
- binding of a DeDi file's embedded publisher key to the current manifest;
- rejection when the manifest no longer declares that signing key;
- rejection of content changed after signing; and
- SHA-256 verification of a referenced file against the digest committed by the manifest.

## Test vectors

The vectors under `conformance/vectors/publishing/` are intentionally small and deterministic:

- `valid-manifest.json` — a correctly signed publisher manifest;
- `valid-file.json` — a correctly signed hosted DeDi file whose digest is committed by the manifest;
- `tampered-file.json` — the valid file with signed content changed while retaining the original JWS;
- `removed-key-manifest.json` — a manifest state in which the original signing key has been removed.

The verifier is implemented in `scripts/verify_publishing_crypto.py`.

## Security boundary

The test private key used to construct the deterministic fixtures is **not stored in the repository**. Only the public JWK and resulting signatures appear in committed fixtures.

The verifier currently supports the Ed25519/OKP combination used by these fixtures. That is an implementation boundary of the fork's test harness, not a claim that upstream DeDi is restricted to this algorithm unless upstream text says so.

## Remaining work

This PR closes the gap between structural publishing validation and actual signature/digest verification. The next lifecycle increment should add controlled checks for:

- `next_update` freshness and stale-copy rejection;
- rollback/replay detection;
- key rotation overlap windows;
- inactive registries;
- negative-list changes; and
- failure behavior when current authority state cannot be refreshed.

Live TLS origin retrieval remains separate because deterministic CI should not depend on an external network endpoint.