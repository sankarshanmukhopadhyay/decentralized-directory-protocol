---
title: Implement
nav_order: 2
permalink: /implement/
has_children: false
---

# Implement DeDi

Use this path when you need to build a publisher, resolver, verifier, directory client, or integration around DeDi.

## Fast path

1. [Run the quickstart](getting-started/quickstart) to establish a working local baseline.
2. [Build with DeDi](build-with-dedi) for implementation patterns and integration choices.
3. [Understand discovery](discovery) before hard-coding directory locations.
4. [Review the protocol surface](protocol-spec) and [API contract](../api/openapi.yaml) before implementing behavior that other systems must rely on.
5. [Run the publisher → indexer → verifier scenario](../examples/end-to-end/publisher-indexer-verifier/README.md) to see authority propagation across roles.

## What to implement first

A useful implementation sequence is:

```text
Discovery
   ↓
Authority retrieval
   ↓
Artifact/schema validation
   ↓
Cryptographic verification
   ↓
Freshness + lifecycle checks
   ↓
Record resolution
   ↓
Evidence-producing reliance decision
```

The important design constraint is that later steps must not erase the evidence established earlier. A cached record is not independent of the publisher authority and freshness state that made it acceptable.

## Core implementation surfaces

| Need | Repository surface |
|---|---|
| First working request | [Quickstart](getting-started/quickstart) |
| Integration patterns | [Build with DeDi](build-with-dedi) |
| Discovery | [Discovery](discovery) |
| Protocol semantics | [Protocol specification](protocol-spec) |
| HTTP/API integration | [`api/openapi.yaml`](../api/openapi.yaml) |
| Schemas | [`schemas/`](../schemas/) |
| Runnable server/client | [`reference-impl/`](../reference-impl/) |
| End-to-end role flow | [Publisher → indexer → verifier](../examples/end-to-end/publisher-indexer-verifier/README.md) |

## Before calling an implementation complete

Run:

```bash
make conformance
```

That executes the fork-local structural, cryptographic, lifecycle, and composed scenario checks and emits machine-readable evidence. See [Test](test) and [conformance evidence](conformance-evidence) for details.
