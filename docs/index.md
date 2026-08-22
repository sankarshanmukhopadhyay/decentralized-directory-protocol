---
title: Home
nav_order: 1
description: "DeDi implementation and assurance workbench: implement, operate, verify, test, and understand public machine-readable directory infrastructure."
permalink: /
---

# DeDi: Decentralized Directory Protocol
{: .fs-9 }

An implementation, operations, verification, and assurance workbench around the upstream DeDi protocol.
{: .fs-6 .fw-300 }

[Get started in 10 minutes](getting-started/quickstart){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Run conformance](test){: .btn .fs-5 .mb-4 .mb-md-0 .mr-2 }
[View on GitHub](https://github.com/sankarshanmukhopadhyay/decentralized-directory-protocol){: .btn .fs-5 .mb-4 .mb-md-0 }

---

{: .important }
> **Fork posture:** upstream `LF-Decentralized-Trust-labs/decentralized-directory-protocol` remains authoritative for upstream governance, normative protocol decisions, and upstream releases. This fork adds implementation, testing, conformance, evidence, and experimental operational material without implying upstream adoption. See [Fork authority and adoption posture](fork-posture).

## Choose what you need to do

The documentation is organized around five working paths.

| Goal | Start here | You will find |
|---|---|---|
| **Build or integrate** | [Implement](implement) | quickstart, protocol/API surfaces, schemas, reference implementation, integration flow |
| **Run directory infrastructure** | [Operate](operate) | publishing, deployment, freshness, key rotation, revocation, failure handling |
| **Make reliance decisions** | [Verify](verify) | authority discovery, signatures, freshness, lifecycle, indexed-state provenance |
| **Evaluate an implementation** | [Test](test) | profiles, vectors, crypto/lifecycle checks, scenarios, conformance evidence |
| **Understand the system** | [Understand](understand) | concepts, architecture, governance boundary, interoperability, fork posture |

---

## The executable trust path

The fork increasingly treats DeDi as a working system rather than a collection of independent documents.

```text
Publisher
   |
   | signed authority + registry state
   v
Indexer
   |  discover authority
   |  verify signatures and digests
   |  enforce freshness and lifecycle
   |  preserve provenance
   v
Verifier
   |  resolve requested record
   |  confirm authority horizon
   v
Reliance decision + evidence
```

Run the composed scenario with:

```bash
make scenario
```

Run the complete fork-local conformance surface with:

```bash
make conformance
```

The conformance runner executes structural, cryptographic, lifecycle, and composed role-flow checks and writes a schema-validated evidence record.

---

## What the fork can test today

### Structural consistency

- manifest and DeDi-file shape;
- publisher-domain and key relationships;
- unique registry and record names;
- hosted and inline file relationships; and
- repository schemas, examples, OpenAPI, governance artifacts, and test declarations.

### Cryptographic integrity

- RFC 8785 JCS canonicalization;
- detached Ed25519 JWS verification;
- tamper detection;
- current publisher-key enforcement; and
- referenced-file SHA-256 digest verification.

### Lifecycle and freshness

- `next_update` freshness bounds;
- inactive registries;
- rollback detection;
- rotation overlap versus key removal; and
- fail-closed behavior when authority refresh fails after cached state expires.

### Cross-role composition

- publisher → indexer → verifier authority propagation;
- bounded caching/indexing; and
- rejection when the authority supporting indexed state has expired.

See [Test](test) and [Conformance evidence](conformance-evidence) for the executable surfaces.

---

## What problem does DeDi solve?

Most trust systems can verify signatures. What they still struggle with is the operational step before and around verification: discovering the right authoritative directory, retrieving current public state, understanding lifecycle semantics, preserving provenance through caching or indexing, and applying that state consistently across different registries.

DeDi provides a common protocol and schema surface for that operational trust layer.

{: .highlight }
> If your system needs to know which public key to trust now, whether an entity is still authorized, or which registry is authoritative for a namespace, DeDi is intended to make that state discoverable and machine-readable.

---

## Core repository surfaces

| Surface | Purpose |
|---|---|
| [`spec/`](../spec/) | versioned protocol/specification material |
| [`api/`](../api/) | API contract and client-facing interface artifacts |
| [`schemas/`](../schemas/) | machine-readable data and evidence schemas |
| [`reference-impl/`](../reference-impl/) | runnable reference implementation |
| [`conformance/`](../conformance/) | profiles, tests, vectors, and validation guidance |
| [`scripts/`](../scripts/) | executable validation, cryptographic, lifecycle, scenario, and conformance runners |
| [`examples/`](../examples/) | examples and end-to-end walkthroughs |
| [`governance/`](../governance/) | authority, delegation, and revocation artifacts |
| [`evidence/`](../evidence/) | example/static and runtime-generated assurance evidence |

---

## Protocol boundary

DeDi is a protocol and schema layer for public directory state and discovery. It is not by itself a universal trust policy, a certification program, a blockchain requirement, or a substitute for deployment governance.

For the conceptual and interoperability boundaries, continue to [Understand](understand).
