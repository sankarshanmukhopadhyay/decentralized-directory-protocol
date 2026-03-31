# DeDi: Decentralized Directory Protocol

![Spec status](https://img.shields.io/badge/status-draft-blue)
![CI](https://github.com/sankarshanmukhopadhyay/decentralized-directory-protocol/actions/workflows/validate.yml/badge.svg)
![Schemas](https://img.shields.io/badge/schemas-json--schema-informational)
![License](https://img.shields.io/badge/license-Apache--2.0-lightgrey)

DeDi is an open protocol for publishing, discovering, and consuming **public, machine-readable directory data** needed to verify participants, memberships, public keys, endpoints, and revocation status across ecosystems.

It addresses a recurring integration problem: most trust systems can verify signatures, but they still struggle to discover the **right authoritative registry**, retrieve the **current public state**, and apply that state consistently across different registries. DeDi provides a common protocol and schema surface for that operational trust layer.

## Start here

### What problem does this solve?
DeDi helps teams answer operational trust questions such as:

- Which public key should be trusted for this entity right now?
- Is this participant still authorized, active, suspended, or revoked?
- Which namespace or registry is authoritative for this record class?
- How can multiple registries be integrated without bespoke logic for each one?

### Who is this for?
- **Developers** building verification, onboarding, resolver, or trust network flows
- **Registry operators** exposing authoritative public state through interoperable interfaces
- **Architects and ecosystem designers** creating reusable discovery and trust layers
- **Evaluators and contributors** assessing protocol maturity, conformance, and adoption readiness

### Choose your path
- **Build with DeDi:** start with the [10-minute quickstart](docs/getting-started/quickstart.md) and [developer build guide](docs/build-with-dedi.md)
- **Understand the architecture:** read [why DeDi exists](docs/why-ddip.md), [core concepts](docs/core-concepts.md), and [architecture](docs/architecture.md)
- **Evaluate for adoption:** review the [adoption guide](docs/adoption-guide.md), [conformance profile](conformance/profiles.md), and [versioning and stability guidance](docs/stability.md)
- **Propose a change:** follow the [protocol change process](docs/protocol-change-process.md)

## What DeDi is

DeDi is:

- a protocol and schema layer for public directories,
- an interoperability approach for lookup, query, and trust discovery,
- a reusable interface for authoritative public state,
- and a foundation for multiple ecosystems and record classes.

DeDi is **not**:

- a single hosted product,
- a mandate to replace an existing registry,
- a blockchain requirement,
- or a substitute for governance and assurance.

## 10-minute implementation path

1. Read the [quickstart](docs/getting-started/quickstart.md).
2. Pick a schema from [`schemas/`](schemas/).
3. Validate sample data from [`examples/`](examples/).
4. Walk through a [complete end-to-end flow](examples/end-to-end/README.md).
5. Review the API contract in [`api/openapi.yaml`](api/openapi.yaml).
6. Check the [conformance baseline](conformance/profiles.md) before claiming compatibility.

Or run the reference client directly:

```bash
python -m pip install jsonschema
python scripts/client_demo.py discover example.org
python scripts/client_demo.py lookup example.org public-key did:example:merchant-123
python scripts/client_demo.py validate public_key examples/public-key/sample.json
```

## Core project surfaces

### Specifications and protocol surface
- [Normative protocol specification](docs/protocol-spec.md)
- [Spec index](spec/README.md)
- [API contract](api/openapi.yaml)
- [Postman collection](api/dedi_postman_collection.json)
- [Discovery conventions](docs/discovery.md)

### Concepts and architecture
- [Why DeDi exists](docs/why-ddip.md)
- [Core concepts](docs/core-concepts.md)
- [Architecture](docs/architecture.md)
- [Security model](docs/security-model.md)
- [Compare and position](docs/compare-and-position.md)
- [Federation guide](docs/federation.md)

### Build and adoption
- [Build with DeDi](docs/build-with-dedi.md)
- [Verifier guide](docs/verifier-guide.md)
- [Operator guide](docs/operator-guide.md)
- [Publishing workflow](docs/publishing-workflow.md)
- [Adoption guide](docs/adoption-guide.md)
- [Use cases](docs/use-cases.md)

### Testability and quality
- [Conformance overview](conformance/README.md)
- [Conformance profiles](conformance/profiles.md)
- [Validation guide](conformance/validation-guide.md)
- [Test matrix](conformance/test-matrix.md)
- [Validation script](scripts/validate_artifacts.py)
- [Reference client](scripts/client_demo.py)
- [Machine-readable catalogs](machine-readable/)

### Contributing and governance
- [Contributing guide](CONTRIBUTING.md)
- [Protocol change process](docs/protocol-change-process.md)
- [Versioning policy](docs/versioning-policy.md)
- [Governance model](GOVERNANCE.md)

## Repository structure

```text
.
├── .github/
│   ├── CODEOWNERS
│   └── workflows/
│       └── validate.yml        # CI: schema + OpenAPI validation
├── api/
│   ├── openapi.yaml
│   └── dedi_postman_collection.json
├── conformance/
│   ├── profiles.md             # Baseline and recommended conformance profiles
│   ├── validation-guide.md     # How to run and interpret validation
│   └── test-matrix.md          # Per-capability self-assessment checklist
├── docs/
│   ├── getting-started/
│   │   └── quickstart.md
│   ├── discovery.md            # Namespace, registry, and schema discovery conventions
│   ├── federation.md           # Cross-registry and federated discovery
│   ├── protocol-change-process.md  # How to propose protocol changes (PCP)
│   ├── versioning-policy.md    # Semantic versioning, deprecation, migration
│   └── ...
├── examples/
│   ├── end-to-end/             # Complete flows: key lookup, revocation, membership
│   ├── endpoint/
│   ├── public-key/
│   ├── membership/
│   ├── revoke/
│   ├── beckn-subscriber/
│   ├── beckn-subscriber-reference/
│   └── quickstart/
├── machine-readable/
├── schemas/
│   ├── public_key.json
│   ├── revoke.json
│   ├── membership.json
│   ├── endpoint.json           # Service endpoint advertisement (new)
│   ├── Beckn_subscriber.json
│   └── Beckn_subscriber_reference.json
├── scripts/
│   ├── validate_artifacts.py   # Schema + OpenAPI validation
│   └── client_demo.py          # Reference client (discover, query, lookup, validate)
├── spec/
├── CONTRIBUTING.md
├── GOVERNANCE.md
├── README.md
└── SECURITY.md
```

## Available schemas

| Schema | Purpose | Typical use |
|---|---|---|
| `public_key.json` | Current and historical public key material | Signature verification, key discovery |
| `revoke.json` | Revocation or deny-list entry | Reject revoked entities, keys, or credentials |
| `membership.json` | Public membership or affiliation state | Standing, enrollment, or participation checks |
| `endpoint.json` | Service endpoint advertisement | Callback and API endpoint discovery |
| `Beckn_subscriber.json` | Beckn participant directory entry | Endpoint and key discovery |
| `Beckn_subscriber_reference.json` | Reference to another directory or record | Federation, delegation, or indirection |

## Stability and maturity signals

- **Protocol maturity:** draft, implementation-oriented
- **Schemas:** usable for experimentation and integration pilots
- **Conformance surface:** baseline compatibility profile included, CI validation running
- **Assurance:** external assurance and trust policy remain deployment concerns, not protocol guarantees

More detail is in [docs/stability.md](docs/stability.md) and [docs/versioning-policy.md](docs/versioning-policy.md).

## Governance and contribution

This repository includes:

- a [governance model](GOVERNANCE.md),
- an expanded [contribution guide](CONTRIBUTING.md),
- a [protocol change process](docs/protocol-change-process.md) for proposing normative changes,
- CI validation for schemas and OpenAPI on every push and PR,
- and a GitHub Pages-ready docs index in [`docs/index.md`](docs/index.md).

## Design principles

DeDi works best when directories are:

- **Authoritative** about who controls the namespace and record lifecycle
- **Machine-readable** with stable schemas and predictable API semantics
- **Current** enough for live operational decisions
- **Traceable** so provenance, changes, and revocations can be understood
- **Composable** across ecosystems and record classes
- **Verifiable** through signatures, policy, and runtime checks

## Project objective

The goal is not to create yet another registry silo. The goal is to make **directory infrastructure interoperable, testable, and easier to trust operationally**.
