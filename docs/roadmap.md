---
title: "Roadmap"
nav_order: 11
---
# Roadmap

This roadmap is intentionally practical. It focuses on the moves that most improve implementability, conformance, and developer adoption.

## Completed in this increment

### 1. Add a deterministic quickstart ✓
A time-to-first-success path now exists through [`docs/getting-started/quickstart.md`](getting-started/quickstart.md), [`scripts/query_and_verify.py`](../scripts/query_and_verify.py), and [`examples/minimal-node/`](../examples/minimal-node/).

### 2. Add a minimal runnable implementation ✓
A reference server and client now exist under [`reference-impl/`](../reference-impl/) so implementers can see a concrete query and lookup surface.

### 3. Make conformance machine-verifiable ✓
Machine-readable conformance profiles, tests, and vectors now live under [`conformance/`](../conformance/).

### 4. Make governance more explicit ✓
Authority, delegation, and revocation are now documented and represented under [`governance/`](../governance/).

### 5. Add evidence artifacts ✓
Sample evidence outputs and quickstart-generated evidence now live under [`evidence/`](../evidence/).

## Next priorities

- Expand signed-response examples from illustrative placeholders to cryptographically verifiable fixtures.
- Add more schema families for high-value trust infrastructure use cases.
- Publish implementation notes for pagination, caching, and freshness semantics.
- Add interoperability harnesses for ecosystem-specific profiles.
- Add worked migration guides for wrapping legacy registries.

## Strategic goal

The long-term goal remains simple: make DeDi feel less like an interesting concept and more like a protocol developers can confidently build into real systems.
