# DeDi: Decentralized Directory Protocol

DeDi is an open protocol for publishing and consuming **public, machine-readable directories** that are needed to verify digital transactions, credentials, participants, memberships, keys, and revocation status.

In practical terms, DeDi gives developers and operators a common way to answer questions such as:

- Which public key should I trust for this entity right now?
- Is this participant currently registered, authorized, suspended, or revoked?
- Where can I discover the source-of-truth registry for this namespace?
- How can I integrate multiple public registries without custom logic for each one?

This repository is the starting point for understanding the protocol, the schemas, the API surface, the trust model, and how to build with them.

## Why developers should care

Most verification stacks already know how to check **integrity**. The harder problem is operational trust:

- discovering the right source of truth,
- retrieving the current state of a record,
- checking whether something has been revoked or superseded,
- and doing this consistently across multiple registries.

That is the gap DeDi is intended to close.

## What DeDi is

DeDi is:

- a protocol and schema layer for public directories,
- an interoperability approach for lookup, query, and trust discovery,
- a way to make registries easier to integrate into verification flows,
- a foundation that can support multiple ecosystems and data models.

DeDi is **not**:

- a single software product,
- a requirement to replace an existing registry,
- a blockchain mandate,
- or a closed hosted service.

A hosted implementation such as `dedi.global` can accelerate adoption, but the protocol should be understood independently from any one deployment.

## Who this repo is for

### Registry operators
You maintain a public registry or authoritative directory and want to expose it through a more consistent, machine-readable interface.

### Verifier and relying-party developers
You need to look up public keys, membership status, revocation information, or participant metadata inside verification and onboarding workflows.

### Ecosystem architects
You are designing a trust network, registry layer, or discovery mechanism and want a reusable pattern rather than bespoke integrations.

### Contributors
You want to improve the schemas, examples, guidance, and implementation pathway for the protocol.

## Start here

Read in this order if you want the fastest route from orientation to implementation:

1. [Protocol specification](docs/protocol-spec.md)
2. [Architecture](docs/architecture.md)
3. [Security model](docs/security-model.md)
4. [Build with DeDi](docs/build-with-dedi.md)
5. [Verifier integration guide](docs/verifier-guide.md)
6. [Operator guide](docs/operator-guide.md)
7. [`examples/`](examples/)
8. [`schemas/`](schemas/)
9. [`api/openapi.yaml`](api/openapi.yaml)
10. [`api/dedi_postman_collection.json`](api/dedi_postman_collection.json)

## Quick start

### For consumers of a DeDi-compatible directory

1. Identify the namespace and trust anchor you are willing to trust.
2. Determine which registry and schema you need.
3. Perform a lookup or query against the directory endpoint.
4. Validate the returned payload against the corresponding JSON schema.
5. Verify freshness, provenance, and revocation semantics before acting on the data.
6. Apply your own policy decision logic.

### For publishers and registry operators

1. Define namespace ownership and trust-anchor material.
2. Choose the directory types you want to expose.
3. Map existing records to one or more DeDi schemas.
4. Publish DeDi-compatible endpoints with stable response semantics.
5. Publish signing, rotation, and revocation guidance.
6. Add examples and integration notes so consumers know how to use the registry safely.

A more detailed implementation path is available in [docs/adoption-guide.md](docs/adoption-guide.md).

## Core information model

DeDi is organized around three simple constructs.

### Namespace
A namespace is the trust and discovery starting point. In practice this often maps to an organization and, frequently, to a domain name.

### Directory
A directory is a collection of records exposed under a schema. A directory may represent public keys, memberships, revocations, subscribers, or another well-defined record class.

### Record
A record is the individual item that a verifier, integrator, or relying party retrieves and acts upon.

## What you can build with it

DeDi is useful when you need **current public state** as part of a trust decision. Common patterns include:

- **Public key discovery** for signature verification.
- **Revocation or deny-list lookup** before accepting a credential, entity, or transaction.
- **Membership and affiliation checks** for gated access or ecosystem participation.
- **Participant registries** for network discovery, such as Beckn participants and endpoints.
- **Reference registries** that point to other DeDi-compatible records or registries.

See [docs/use-cases.md](docs/use-cases.md) for concrete examples.

## Repository structure

```text
.
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── docs/
│   ├── adoption-guide.md
│   ├── architecture.md
│   ├── build-with-dedi.md
│   ├── conformance.md
│   ├── glossary.md
│   ├── operator-guide.md
│   ├── privacy-abuse-controls.md
│   ├── protocol-spec.md
│   ├── publishing-workflow.md
│   ├── roadmap.md
│   ├── security-model.md
│   ├── use-cases.md
│   ├── verifier-guide.md
│   ├── versioning-policy.md
│   └── observability-and-incident-response.md
├── api/
│   ├── README.md
│   ├── openapi.yaml
│   └── dedi_postman_collection.json
├── examples/
│   ├── README.md
│   ├── */sample.json
│   └── */invalid.json
└── schemas/
    ├── README.md
    ├── Beckn_subscriber.json
    ├── Beckn_subscriber_reference.json
    ├── membership.json
    ├── public_key.json
    └── revoke.json
```

## Available schemas

| Schema | Purpose | Typical use |
|---|---|---|
| `public_key.json` | Current public key material and prior keys | Verify signatures, discover trusted keys |
| `revoke.json` | Negative list or revocation entry | Reject revoked entities, credentials, or members |
| `membership.json` | Public membership / affiliation status | Check participation, enrollment, or standing |
| `Beckn_subscriber.json` | Beckn network participant registry entry | Discover subscriber endpoints and keys |
| `Beckn_subscriber_reference.json` | Reference to another subscriber registry or record | Federation, delegation, or indirection |

See [schemas/README.md](schemas/README.md) for field-level notes and implementation considerations.

## What changed in this developer-focused pass

This repository now includes:

- a **normative protocol specification** separated from the README,
- a **security model** and vulnerability reporting policy,
- an initial **OpenAPI contract**,
- clearer **operator** and **verifier** integration guidance,
- a **publishing workflow**, **glossary**, **versioning policy**, and **conformance guidance**,
- tighter schemas for keys, revocation, and membership lifecycle data,
- valid and invalid examples for every schema,
- and CI checks for schema and OpenAPI validation.

## Design principles

DeDi works best when directories are:

- **Publicly accessible** where policy permits.
- **Machine-readable** with stable schemas.
- **Authoritative** with a clear source of truth.
- **Current** so verifiers are not acting on stale state.
- **Traceable** so provenance and change history can be understood.
- **Composable** so multiple schemas and ecosystems can coexist.
- **Verifiable** so signatures, history, and revocation semantics can be checked consistently.

## Working with the schemas

The schemas in this repository can be used to:

- validate payloads during development,
- document record formats,
- support testing and conformance,
- reduce ambiguity for integrators.

Recommended implementation practice:

- validate every record at publish time,
- validate every response at integration time,
- version breaking schema changes explicitly,
- and publish example payloads alongside APIs.

## Build something with it

If you are trying to move from understanding to implementation, go straight to:

- [docs/build-with-dedi.md](docs/build-with-dedi.md) for application patterns,
- [docs/verifier-guide.md](docs/verifier-guide.md) for safe consumption,
- [docs/operator-guide.md](docs/operator-guide.md) for deployment and operations,
- [examples/README.md](examples/README.md) for sample payloads,
- [api/README.md](api/README.md) for API contract guidance.

## Get involved

- Open an issue with a concrete protocol, schema, or documentation improvement.
- Contribute examples from real registries.
- Propose additional record classes and interoperability mappings.
- Help tighten validation, discovery, and adoption guidance.

Contribution guidance is in [CONTRIBUTING.md](CONTRIBUTING.md). Security reporting is in [SECURITY.md](SECURITY.md).
