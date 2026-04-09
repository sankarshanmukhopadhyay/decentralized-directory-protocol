# DeDi: Decentralized Directory Protocol

![Spec status](https://img.shields.io/badge/status-draft-blue)
![CI](https://github.com/sankarshanmukhopadhyay/decentralized-directory-protocol/actions/workflows/validate.yml/badge.svg)
![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-brightgreen)
![Conformance](https://img.shields.io/badge/conformance-machine--verifiable-informational)
![License](https://img.shields.io/badge/license-Apache--2.0-lightgrey)

> 📖 **Documentation site:** [sankarshanmukhopadhyay.github.io/decentralized-directory-protocol](https://sankarshanmukhopadhyay.github.io/decentralized-directory-protocol/)

DeDi is an open protocol for publishing, discovering, and consuming **public, machine-readable directory data** needed to verify participants, memberships, public keys, endpoints, and revocation status across ecosystems.

The project focus is straightforward: **make authoritative directory infrastructure implementable, testable, and auditable**. In practical terms, that means a DeDi deployment should not just expose data. It should make clear:

- which authority controls a namespace,
- who may publish or revoke records,
- which schemas and API surfaces are in play,
- what evidence a verifier can rely on,
- and how an implementation can prove conformance.

## Start here

### What problem does this solve?

Most trust systems can verify signatures. They still struggle with the operational step *before* verification:

- discovering the right authoritative directory,
- retrieving the current public state,
- understanding lifecycle and revocation semantics,
- and applying that state consistently across different registries.

DeDi provides a common protocol and schema surface for that operational trust layer.

### Who is this for?

- **Developers** building verifier, onboarding, resolver, wallet, and trust-network flows
- **Directory operators** exposing authoritative public state through interoperable interfaces
- **Architects and ecosystem designers** defining governance-aware discovery and directory layers
- **Evaluators and contributors** assessing conformance, interoperability, and adoption readiness

### Choose your path

- **Get to first success quickly:** [10-minute quickstart](docs/getting-started/quickstart.md)
- **Run a minimal implementation:** [minimal node example](examples/minimal-node/README.md)
- **Evaluate interoperability:** [interoperability positioning](docs/interoperability.md) and [deployment models](docs/deployment-models.md)
- **Assess implementation quality:** [conformance overview](conformance/README.md), [profiles](conformance/profiles/), and [validation guide](conformance/validation-guide.md)
- **Understand governance:** [governance model](GOVERNANCE.md), [authority model](governance/authority-model.md), and [delegation schema](governance/delegation-schema.json)

## What DeDi is

DeDi is:

- a protocol and schema layer for public directories,
- an interoperability approach for lookup, query, and trust discovery,
- a reusable interface for authoritative public state,
- and a governance-aware control plane surface for directory publishing and resolution.

DeDi is **not**:

- a single hosted product,
- a mandate to replace an existing registry,
- a blockchain requirement,
- or a substitute for deployment governance and assurance.

## 10-minute implementation path

```bash
make setup
make validate
make quickstart
```

What that path does:

1. installs validation dependencies,
2. validates schemas, examples, OpenAPI, conformance profiles, and evidence artifacts,
3. starts a minimal reference server,
4. executes a sample query and lookup,
5. validates the returned payload against the `public_key` schema,
6. and emits machine-readable evidence under `evidence/`.

See [docs/getting-started/quickstart.md](docs/getting-started/quickstart.md) for the full flow.

## Repository structure

```text
.
├── .github/
│   └── workflows/
│       └── validate.yml
├── api/
├── conformance/
│   ├── profiles/
│   ├── tests/
│   ├── vectors/
│   ├── README.md
│   └── validation-guide.md
├── docs/
├── evidence/
├── examples/
│   ├── minimal-node/
│   └── end-to-end/
├── governance/
├── machine-readable/
├── reference-impl/
├── schemas/
├── scripts/
├── spec/
│   └── v0.1/
├── Makefile
├── README.md
└── requirements-dev.txt
```

## Core project surfaces

### Specifications and protocol surface
- [Normative protocol specification](docs/protocol-spec.md)
- [Versioned specification index](spec/README.md)
- [v0.1 specification set](spec/v0.1/README.md)
- [API contract](api/openapi.yaml)
- [Discovery conventions](docs/discovery.md)

### Governance, lifecycle, and control
- [Governance model](GOVERNANCE.md)
- [Authority model](governance/authority-model.md)
- [Delegation schema](governance/delegation-schema.json)
- [Revocation model](governance/revocation-model.md)
- [Protocol change process](docs/protocol-change-process.md)

### Build and adoption
- [Quickstart](docs/getting-started/quickstart.md)
- [Build with DeDi](docs/build-with-dedi.md)
- [Verifier guide](docs/verifier-guide.md)
- [Operator guide](docs/operator-guide.md)
- [Adoption guide](docs/adoption-guide.md)
- [Deployment models](docs/deployment-models.md)
- [Interoperability positioning](docs/interoperability.md)

### Conformance and assurance
- [Conformance overview](conformance/README.md)
- [Conformance profiles](conformance/profiles/)
- [Validation guide](conformance/validation-guide.md)
- [Test matrix](conformance/test-matrix.md)
- [Evidence artifacts](evidence/)
- [Validation script](scripts/validate_artifacts.py)

### Implementations and runnable examples
- [Minimal node example](examples/minimal-node/README.md)
- [Quickstart helper script](scripts/query_and_verify.py)
- [Reference server](reference-impl/server/server.py)
- [Reference client](reference-impl/client/client.py)
- [End-to-end examples](examples/end-to-end/README.md)

## Available schemas

| Schema | Purpose | Typical use |
|---|---|---|
| `public_key.json` | Current and historical public key material | Signature verification, key discovery |
| `revoke.json` | Revocation or deny-list entry | Reject revoked entities, keys, or credentials |
| `membership.json` | Public membership or affiliation state | Standing, enrollment, or participation checks |
| `endpoint.json` | Service endpoint advertisement | Callback and API endpoint discovery |
| `Beckn_subscriber.json` | Beckn participant directory entry | Endpoint and key discovery |
| `Beckn_subscriber_reference.json` | Reference to another directory or record | Federation, delegation, or indirection |

## Interoperability position

DeDi works best when its role is clear:

- **DID resolution** handles identifier dereferencing.
- **Trust registries** define who is authoritative and under what policy.
- **TRQP** handles trust-query semantics and assurance overlays.
- **DeDi** handles directory discovery, record retrieval, schema validation, and lifecycle-aware public state access.

That makes DeDi a useful substrate for directory interoperability without overstating what the protocol itself guarantees.

## Design principles

DeDi works best when directories are:

- **Authoritative** about who controls the namespace and record lifecycle
- **Machine-readable** with stable schemas and predictable API semantics
- **Current** enough for live operational decisions
- **Traceable** so provenance, changes, and revocations can be understood
- **Governed** with explicit delegation, scope, and revocation rules
- **Testable** through schemas, vectors, conformance profiles, and evidence artifacts
- **Composable** across ecosystems and record classes

## Project objective

The goal is not to create another registry silo. The goal is to make **directory infrastructure interoperable, governable, testable, and easier to adopt in real systems**.
