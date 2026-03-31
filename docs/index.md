---
title: Home
nav_order: 1
description: "DeDi is an open protocol for publishing, discovering, and consuming public, machine-readable directory data needed to verify participants, memberships, public keys, and revocation status across ecosystems."
permalink: /
---

# DeDi: Decentralized Directory Protocol
{: .fs-9 }

An open protocol for public, machine-readable trust infrastructure — verifiable participants, keys, memberships, and revocation across any ecosystem.
{: .fs-6 .fw-300 }

[Get started in 10 minutes](getting-started/quickstart){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[View on GitHub](https://github.com/sankarshanmukhopadhyay/decentralized-directory-protocol){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## What problem does DeDi solve?

Most trust systems can verify signatures. What they struggle with is the step _before_ verification: discovering the right authoritative registry, retrieving current public state, and applying it consistently across different registries.

DeDi provides a common protocol and schema surface for that operational trust layer.

{: .highlight }
> **If your system needs to know** which public key to trust right now, whether an entity is still authorized, or which registry is authoritative for a namespace — DeDi is built for that.

---

## Choose your path

| I want to… | Start here |
|---|---|
| Build a verifier or resolver | [Quickstart](getting-started/quickstart) → [Build & Integrate](build-with-dedi) |
| Operate a registry | [Operator Guide](operator-guide) |
| Evaluate DeDi for adoption | [Adoption & Conformance](adoption-guide) |
| Understand the protocol | [Core Concepts](core-concepts) → [Architecture](architecture) |
| Propose a change | [Protocol Change Process](protocol-change-process) |

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

## What DeDi is (and isn't)

DeDi **is** a protocol and schema layer for public directories, an interoperability approach for lookup and trust discovery, and a foundation for multiple ecosystems.

DeDi **is not** a single hosted product, a blockchain requirement, or a substitute for governance and assurance.
