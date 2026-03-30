# DeDi: Decentralized Directory Protocol

DeDi is an open protocol for publishing and consuming **public, machine-readable directories** that are needed to verify digital transactions, credentials, participants, memberships, keys, and revocation status.

In practical terms, DeDi gives developers and operators a common way to answer questions such as:

- Which public key should I trust for this entity right now?
- Is this participant currently registered, authorized, or revoked?
- Where can I discover the source-of-truth registry for this namespace?
- How can I integrate multiple public registries without custom logic for each one?

This repository is the starting point for understanding the protocol, the core schemas, and how to build with them.

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

A hosted implementation such as `dedi.global` can accelerate adoption, but the protocol itself should be understood independently from any one deployment.

## Who this repo is for

This repo should be useful to four main audiences:

### 1. Registry operators
You maintain a public registry or authoritative directory and want to expose it through a more consistent, machine-readable interface.

### 2. Verifier and relying-party developers
You need to look up public keys, membership status, revocation information, or participant metadata inside verification and onboarding workflows.

### 3. Ecosystem architects
You are designing a trust network, registry layer, or discovery mechanism and want a reusable pattern rather than bespoke integrations.

### 4. Contributors
You want to improve the schemas, examples, guidance, and implementation pathway for the protocol.

## The fastest way to understand the project

Start here in this order:

1. Read this README for the project frame.
2. Read [docs/architecture.md](docs/architecture.md) for the protocol model.
3. Read [docs/build-with-dedi.md](docs/build-with-dedi.md) for implementation patterns.
4. Inspect the example records in [`examples/`](examples/).
5. Review the schemas in [`schemas/`](schemas/).
6. Import the Postman collection in [`api/dedi_postman_collection.json`](api/dedi_postman_collection.json).

## Quick start

### For consumers of a DeDi-compatible directory

1. Identify the directory or namespace you trust.
2. Determine which schema the directory uses.
3. Perform a lookup or query against the directory endpoint.
4. Validate the returned payload against the corresponding JSON schema.
5. Use the result in your decision flow, such as:
   - key discovery,
   - revocation checking,
   - participant lookup,
   - membership verification.

### For publishers and registry operators

1. Choose the directory type you want to expose.
2. Map your existing records to one or more DeDi schemas.
3. Publish the records through a stable API.
4. Ensure records are current, public where appropriate, and traceable to an authoritative source.
5. Add examples and implementation notes so integrators know how to consume your directory.

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

DeDi is especially useful when you need **current public state** as part of a trust decision. Common patterns include:

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
├── docs/
│   ├── adoption-guide.md
│   ├── architecture.md
│   ├── build-with-dedi.md
│   ├── roadmap.md
│   └── use-cases.md
├── api/
│   ├── README.md
│   └── dedi_postman_collection.json
├── examples/
│   ├── README.md
│   ├── beckn-subscriber/
│   ├── beckn-subscriber-reference/
│   ├── membership/
│   ├── public-key/
│   └── revoke/
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

## Adoption priorities

If the goal is broader ecosystem adoption, the highest-leverage moves are usually:

1. **Clear examples** developers can copy.
2. **Predictable schemas** with stable field semantics.
3. **Concrete integration guidance** for both publishers and consumers.
4. **Simple discovery conventions** so developers know where to start.
5. **Visible governance and contribution process** so the project feels alive and evolvable.

This repository now includes the first three directly. The remaining two are called out in [docs/roadmap.md](docs/roadmap.md).

## Design principles

DeDi works best when directories are:

- **Publicly accessible** where policy permits.
- **Machine-readable** with stable schemas.
- **Authoritative** with a clear source of truth.
- **Current** so verifiers are not acting on stale state.
- **Traceable** so provenance and change history can be understood.
- **Composable** so multiple schemas and ecosystems can coexist.

## Working with the schemas

The schemas in this repository are JSON Schema documents that can be used to:

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
- [examples/README.md](examples/README.md) for sample payloads,
- [api/README.md](api/README.md) for working with the Postman collection.

## Get involved

- Open an issue with a concrete protocol, schema, or documentation improvement.
- Contribute examples from real registries.
- Propose additional record classes and interoperability mappings.
- Help tighten validation, discovery, and adoption guidance.

Contribution guidance is in [CONTRIBUTING.md](CONTRIBUTING.md).

## Appendix: the three trust checks DeDi helps operationalize

### Integrity
Has the data been altered?

Integrity is typically checked with digital signatures or hashes.

### Validity
Is the data still current and usable?

Validity often depends on revocation status, expiry, replacement, or other current-state checks.

### Authenticity
Does the data come from an authoritative source?

Authenticity depends on trustworthy provenance, discoverable keys, and confidence that the directory being queried is the correct source of truth.

DeDi is most useful in the second and third layers, where many existing systems are still fragmented, manual, or costly to integrate.
