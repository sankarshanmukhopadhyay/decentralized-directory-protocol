---
title: Operate
nav_order: 3
permalink: /operate/
has_children: false
---

# Operate DeDi

Use this path when you publish authoritative directory state, run a directory service or indexer, or own the operational controls around freshness, delegation, revocation, and incident response.

## Operator path

1. [Operator guide](operator-guide)
2. [Deployment models](deployment-models)
3. [Publishing DeDi files](publishing-dedi-files)
4. [Publishing lifecycle and freshness](publishing-lifecycle)
5. [Governance and authority](../GOVERNANCE.md)
6. [Security considerations](security)

## Operational invariants

A production operator should be able to answer:

- Which domain or authority controls this namespace?
- Which keys are currently authorized to publish?
- When must cached authority be refreshed?
- What happens if refresh fails?
- How is key rotation distinguished from key removal?
- What does `inactive` mean for a registry already cached by relying parties?
- How are revocation and rollback attempts detected?
- What evidence is retained when a verifier or indexer accepts or rejects state?

## Freshness and failure policy

The fork's executable lifecycle profile currently models these decisions:

| State | Operational outcome |
|---|---|
| Authority is fresh | continue subject to verification checks |
| Cached authority is fresh but refresh fails | bounded use of cached authority is permitted |
| Cached authority is stale and refresh fails | fail closed |
| Registry becomes inactive | stop current reliance |
| Key remains present during rotation overlap | continue subject to other checks |
| Key is removed from current authority | reject artifacts relying on that key |
| Older authority state appears after newer accepted state | treat as rollback |

See [Publishing lifecycle](publishing-lifecycle) for the executable policy model.

## Operator validation

Before deployment or after changing publication state, run:

```bash
make conformance
```

For a narrower role-flow check:

```bash
make scenario
```

The scenario demonstrates how publisher authority is checked by an indexer and remains bounded when a verifier later relies on indexed state.
