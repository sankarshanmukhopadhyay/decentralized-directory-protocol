---
title: Home
nav_order: 1
description: "DeDi is an open protocol for publishing, discovering, and consuming public, machine-readable directory data with explicit governance, conformance, and evidence surfaces."
permalink: /
---

# DeDi: Decentralized Directory Protocol
{: .fs-9 }

An open protocol for public, machine-readable directory infrastructure with governance-aware discovery, conformance, and evidence.
{: .fs-6 .fw-300 }

[Get started in 10 minutes](getting-started/quickstart){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[View on GitHub](https://github.com/sankarshanmukhopadhyay/decentralized-directory-protocol){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## What problem does DeDi solve?

Most trust systems can verify signatures. What they still struggle with is the step before verification: discovering the right authoritative directory, retrieving current public state, understanding lifecycle semantics, and applying that state consistently across different registries.

DeDi provides a common protocol and schema surface for that operational trust layer.

{: .highlight }
> **If your system needs to know** which public key to trust right now, whether an entity is still authorized, or which registry is authoritative for a namespace, DeDi is built for that.

---

## What is new in this repository increment?

- A deterministic **time-to-first-success** path
- A minimal runnable **reference server and client**
- Machine-readable **conformance profiles, tests, and vectors**
- Explicit **authority, delegation, and revocation** artifacts
- Example **evidence outputs** for audit and assurance workflows

---

## Choose your path

| I want to… | Start here |
|---|---|
| Build a verifier or resolver | [Quickstart](getting-started/quickstart) → [Build & Integrate](build-with-dedi) |
| Run a minimal DeDi service | [Minimal node example](../examples/minimal-node/README.md) |
| Operate a directory | [Operator Guide](operator-guide) → [Deployment models](deployment-models) |
| Evaluate DeDi for adoption | [Adoption guide](adoption-guide) → [Interoperability](interoperability) |
| Review machine-verifiable quality | [Conformance](conformance) → [Validation guide](../conformance/validation-guide.md) |
| Understand governance | [Governance model](../GOVERNANCE.md) → [Authority model](../governance/authority-model.md) |

---

## Available schemas

| Schema | Purpose |
|---|---|
| `public_key` | Current and historical public key material for signature verification |
| `revoke` | Revocation and deny-list entries |
| `membership` | Public membership and affiliation state |
| `endpoint` | Service endpoint advertisement |
| `Beckn_subscriber` | Beckn participant directory entries |
| `Beckn_subscriber_reference` | Federation and delegation reference records |

---

## What DeDi is and is not

DeDi **is** a protocol and schema layer for public directories, an interoperability approach for lookup and trust discovery, and a reusable surface for authoritative public state.

DeDi **is not** a trust policy in itself, a single hosted product, or a replacement for deployment governance.
