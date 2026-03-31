# Compare and position

DeDi becomes easier to evaluate when compared against adjacent patterns.

## DeDi versus a centralized directory

A centralized directory can still be useful, but it often couples discovery, trust assumptions, record shape, and hosting model into one implementation. DeDi instead defines an interoperable protocol and schema layer that can sit across multiple registries and deployments. A team can wrap an existing centralized registry with DeDi-compatible interfaces without replacing it.

## DeDi versus a trust list

A trust list is often a specific artifact or authoritative list used inside an ecosystem. DeDi can expose trust-list-like data through the `revoke.json` and `membership.json` schemas, but it is broader than a single list format. It covers discovery, query behavior, schemas, and record lifecycle semantics.

## DeDi versus DID resolution

DID resolution focuses on dereferencing an identifier into a DID document or related metadata. DeDi is oriented toward public directory data more broadly: memberships, participant registries, revocations, and reference registries. The two approaches can coexist. A DeDi `public_key` record can reference a DID as its identifier without requiring a DID resolver.

## DeDi versus bespoke ecosystem APIs

Bespoke APIs can work for a single deployment, but they shift integration cost onto every downstream consumer. DeDi aims to standardize the recurring public-state retrieval surface so that consumers can reuse validation and lookup patterns across multiple registries.

## DeDi versus OpenID Federation / TRAIN

OpenID Federation and TRAIN focus on federation of identity providers and trust anchors with strong cryptographic binding. DeDi is less opinionated about the cryptographic model and more focused on the operational directory surface: how records are published, discovered, queried, and validated. DeDi and OpenID Federation can complement each other: DeDi can expose the directory data that an OpenID Federation trust anchor references.

## DeDi versus Verifiable Data Registries (VDR)

A Verifiable Data Registry in the W3C VC ecosystem holds data that verifiable credentials reference. DeDi is a natural fit for implementing a VDR: it provides the query and lookup interface through which credential verifiers discover revocation status, public keys, and issuer metadata.

## DeDi versus Beckn registry

Beckn registries are a specific deployment of participant-discovery infrastructure for Beckn-aligned networks. DeDi includes the `Beckn_subscriber.json` and `Beckn_subscriber_reference.json` schemas precisely to support Beckn-style deployments through a standardized interface. A Beckn registry can be DeDi-compatible without any change to its underlying data.

## What DeDi is not trying to do

DeDi does not eliminate governance, assurance, or policy. It gives those layers a more consistent operational substrate. Whether a namespace is trustworthy is a governance question; DeDi makes the trust dependencies explicit and easier to evaluate, not automatic.

## Related

- [Why DeDi exists](why-ddip.md)
- [Architecture](architecture.md)
- [Adoption guide](adoption-guide.md)
- [Use cases](use-cases.md)
