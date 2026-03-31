---
title: "Verifier Guide"
nav_order: 3
parent: "Build & Integrate"
---
# Verifier integration guide

This guide is for relying parties that need to consume DeDi safely.

## Verification workflow

1. Determine which namespace you trust.
2. Resolve the registry and record you need.
3. Fetch the record using a lookup or query endpoint.
4. Validate the payload against the declared schema.
5. Validate provenance and signing material according to the namespace trust model.
6. Check freshness and any revocation or supersession semantics.
7. Apply your own business or regulatory policy.

## What a verifier should never assume

A verifier should not assume that:

- schema validity alone means the record is trustworthy,
- absence of a revocation entry implies permanent validity,
- a historical record is still fit for live decisions,
- or a referenced URL inherits trust automatically.

## Cache and freshness guidance

- Cache only when the operator publishes explicit freshness behavior.
- Prefer version-aware caching.
- Treat stale but signed data as a policy exception path, not as normal success.

## Historical lookups

Historical lookup is useful for audit and reconciliation. It SHOULD be separated from live authorization decisions unless the consuming system explicitly needs time-bounded state reconstruction.

## Suggested verifier checks by schema

### Public key
- validate algorithm allow-list,
- validate activation and retirement metadata,
- confirm the key is within accepted policy,
- confirm compromise or revocation state.

### Revocation
- validate scope,
- validate issuer and timestamp,
- check whether reinstatement is supported.

### Membership
- validate status,
- evaluate issuer or evidence source,
- check date validity windows.

### Beckn subscriber
- validate the relationship between `subscriber_id` and URL host,
- validate signing key expectations,
- avoid trusting look-alike domains.
