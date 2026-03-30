# Build with DeDi

This document is for developers who want to move from reading the repo to actually building something.

## What DeDi is good at

DeDi is a strong fit when your application needs **current public state from an authoritative source**.

Typical product and engineering scenarios:

- verifying that a signing key is current,
- checking if an organization is still in good standing,
- discovering a participant endpoint before network interaction,
- rejecting a revoked entity before downstream processing,
- reducing one-off registry integrations.

## Common implementation patterns

### Pattern 1: Key discovery before signature verification

Use `public_key.json` when you need to discover the correct public key for an entity before or during verification.

Typical flow:

1. Receive signed artifact.
2. Extract entity identifier.
3. Query the public key directory.
4. Validate the directory response against the schema.
5. Use the returned key material in verification.
6. Apply local policy for fallback, stale data, or key rotation handling.

### Pattern 2: Revocation check before acceptance

Use `revoke.json` when acceptance depends on whether the presented entity or object has been revoked or blacklisted.

Typical flow:

1. Receive identifier.
2. Query the revocation directory.
3. If a match is returned, reject or escalate.
4. If no match is returned, continue with downstream checks.

### Pattern 3: Membership / affiliation validation

Use `membership.json` when access, trust, or eligibility depends on affiliation.

Typical flow:

1. Receive entity identifier or membership reference.
2. Query the membership directory.
3. Confirm the record is current and sufficient for the requested action.
4. Apply local rules around expiry, evidence, or tiered membership semantics.

### Pattern 4: Participant discovery in a networked ecosystem

Use `Beckn_subscriber.json` for discovery of ecosystem participants, callback endpoints, and related keys.

This is useful when systems need to find the correct party to interact with in a shared network.

## Consumer-side implementation checklist

- Know which namespaces and directories you trust.
- Validate every response against its schema.
- Define cache and freshness policy explicitly.
- Decide how to handle lookup failures.
- Log which directory result informed a decision.
- Treat discovery and verification as separate steps.

## Publisher-side implementation checklist

- Keep records stable and current.
- Publish clear schema mapping.
- Document identifiers and lookup keys.
- Provide example responses.
- Explain freshness and update behavior.
- Make deprecation or replacement visible.

## Minimal build plan

If you want a practical first implementation sprint, do this:

### Sprint 1
- Pick one schema.
- Publish one directory.
- Expose one lookup endpoint.
- Provide 3 to 5 example records.
- Validate outputs against JSON Schema.

### Sprint 2
- Add client integration for one consumer workflow.
- Add caching and error handling.
- Add audit logging for lookup-driven decisions.

### Sprint 3
- Add more directory types.
- Add discovery guidance.
- Add compatibility tests and conformance checks.

## Anti-patterns to avoid

- Treating schema publication as sufficient without examples.
- Making fields technically valid but semantically vague.
- Hiding freshness assumptions.
- Coupling the protocol too tightly to one hosted implementation.
- Assuming developers will infer lookup logic from marketing language.

## Suggested next moves for builders

After reading this document, the next best step is usually to open the examples folder and map one of the schemas to your own verification flow.
