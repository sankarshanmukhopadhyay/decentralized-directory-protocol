# Federation and cross-registry discovery

This document describes how DeDi handles federation: the ability to discover and consume records that span multiple registries or namespaces without bespoke integration logic for each one.

## What federation means in DeDi

In DeDi, federation is not a single mechanism. It covers three related patterns:

1. **Reference records** — one registry holds a pointer to a record in another registry.
2. **Namespace delegation** — a namespace authority documents that a sub-namespace is controlled by another party.
3. **Cross-registry consumers** — a verifier queries multiple registries and applies unified validation logic.

## Pattern 1: Reference records

The `Beckn_subscriber_reference.json` schema allows a directory entry to point to an authoritative record in another DeDi-compatible directory instead of storing the data directly.

**When to use it:** when an ecosystem registry does not own the underlying record but needs to expose a stable lookup path for consumers.

**Example flow:**

1. Consumer queries `GET /dedi/lookup/network.example/participants/merchant-xyz`.
2. The response contains a reference record pointing to `registry.merchant.example/dedi/lookup/merchant-xyz/public-key/current`.
3. Consumer follows the reference, fetches the record from the target registry, and validates it against the `public_key` schema.

**Consumer responsibility:** validate both the reference record and the resolved record. Do not inherit trust from the referencing registry — verify the target namespace independently.

## Pattern 2: Namespace delegation

A namespace authority may document that a child namespace is controlled by a different party. This is expressed through the namespace authority documentation required by [protocol-spec.md § 3](protocol-spec.md).

**Operator responsibility:** publish explicit documentation of any namespace delegation, including the delegated scope, the delegated party, and how the delegation can be verified.

**Consumer responsibility:** verify delegation at the trust bootstrap step, not at query time. Delegation does not automatically extend trust — the consumer must evaluate the trust model of the delegated namespace separately.

## Pattern 3: Cross-registry consumers

A verifier that consumes from multiple registries should:

1. Maintain a trusted namespace list — which namespaces are considered authoritative for which record types.
2. Apply the same schema validation and freshness checks regardless of which registry a record came from.
3. Log which registry and namespace provided each decision-relevant record.
4. Handle failures independently per namespace — a lookup failure in one namespace should not cascade into failures for unrelated namespaces.

**Anti-pattern:** treating a record from one trusted namespace as sufficient evidence for decisions that span a different namespace. Trust is namespace-scoped.

## Discovery in a federated context

When discovering registries across namespaces:

1. Start from a known-good namespace (configured by your operator or governance model).
2. Issue a namespace query to enumerate registries and schemas.
3. Follow reference records only to namespaces already on your trusted list, or explicitly evaluate the new namespace before following.
4. Do not follow reference chains beyond a depth your policy allows.

## Practical checklist for federated deployments

- [ ] Define which namespaces your system trusts, and document the decision.
- [ ] Validate each namespace independently — do not inherit trust across namespace boundaries.
- [ ] Follow reference records only within defined trust scope.
- [ ] Log namespace and registry provenance for every decision.
- [ ] Handle cross-registry lookup failures with independent fallback paths.
- [ ] Review the `Beckn_subscriber_reference` schema for the reference record structure.

## Related

- [Discovery conventions](discovery.md)
- [Verifier guide](verifier-guide.md)
- [Architecture](architecture.md)
- [Beckn subscriber reference schema](../schemas/Beckn_subscriber_reference.json)
- [Beckn subscriber reference examples](../examples/beckn-subscriber-reference/)
