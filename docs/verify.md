---
title: Verify
nav_order: 4
permalink: /verify/
has_children: false
---

# Verify directory state

Use this path when your system consumes DeDi data and must decide whether a directory record is safe to rely on now.

Verification is more than checking a signature. A verifier needs to establish **authority, integrity, freshness, lifecycle state, and provenance** before turning directory data into a reliance decision.

## Verification path

1. [Verifier guide](verifier-guide)
2. [Discovery](discovery)
3. [Cryptographic publishing verification](cryptographic-publishing-verification)
4. [Publishing lifecycle and freshness](publishing-lifecycle)
5. [Publisher → indexer → verifier scenario](../examples/end-to-end/publisher-indexer-verifier/README.md)
6. [Conformance evidence](conformance-evidence)

## Minimum reliance sequence

```text
Locate authority
      ↓
Retrieve current manifest
      ↓
Verify publisher key + manifest proof
      ↓
Verify registry artifact + digest/signature
      ↓
Check next_update + registry state
      ↓
Resolve requested record
      ↓
Preserve provenance + authority horizon
      ↓
Make reliance decision
```

A valid signature does not override a removed key, stale manifest, inactive registry, rollback condition, or expired authority horizon.

## Cached/indexed data

If a verifier consumes state through an indexer, it should still know enough to determine:

- the publisher namespace;
- the authority state that backed indexing;
- the source location;
- the relevant freshness horizon; and
- whether later authority changes invalidate continued reliance.

The [three-role scenario](../examples/end-to-end/publisher-indexer-verifier/README.md) demonstrates this composition explicitly.

## Verify the verifier path

Run:

```bash
make conformance
```

The resulting `evidence/conformance-run.json` records the executable checks and repository/upstream refs used for the run.
