---
title: Understand
nav_order: 6
permalink: /understand/
has_children: false
---

# Understand DeDi

Use this path when you need the conceptual model, protocol boundaries, governance posture, or interoperability context before implementing or evaluating DeDi.

## Start with the model

1. [Core concepts](core-concepts)
2. [Architecture](architecture)
3. [Protocol specification](protocol-spec)
4. [Discovery](discovery)
5. [Interoperability](interoperability)
6. [Compare and position](compare-and-position)

## Authority and governance

The protocol becomes operationally useful only when readers distinguish data transport from authority.

Read:

- [Governance model](../GOVERNANCE.md)
- [Authority model](../governance/authority-model.md)
- [Revocation model](../governance/revocation-model.md)
- [Fork authority and adoption posture](fork-posture)

The fork explicitly separates upstream DeDi authority from fork-local implementation, conformance, assurance, and experimentation.

## Publishing model

For the synchronized origin-hosted publishing model, read in this order:

1. [Publishing DeDi files](publishing-dedi-files)
2. [Publishing validation](publishing-validation)
3. [Cryptographic publishing verification](cryptographic-publishing-verification)
4. [Publishing lifecycle](publishing-lifecycle)
5. [Three-role scenario](../examples/end-to-end/publisher-indexer-verifier/README.md)

That sequence moves from protocol shape to executable assurance rather than mixing normative and fork-local material.

## Interoperability boundary

DeDi is most useful when it is not asked to perform every trust function itself. In the current repository framing:

- identifier resolution answers how identifiers dereference;
- governance/trust registries establish authority and policy;
- assurance layers answer whether an authority or ecosystem satisfies a particular trust policy;
- DeDi provides discoverable, machine-readable directory state and the mechanics needed to retrieve and verify it.

See [Interoperability](interoperability) for the fuller positioning.
