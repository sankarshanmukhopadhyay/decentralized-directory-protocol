# Publishing lifecycle and freshness validation

This fork extends the experimental publishing profile with deterministic lifecycle checks around the synchronized upstream DeDi publishing model.

These checks are **fork-local, non-normative evaluation material** pinned to upstream commit `72d913fb4d17507891a6fea5db1f49ef7b3f461d`.

## Decision model

A verifier should not treat a successfully signed directory artifact as indefinitely usable. Signature validity establishes integrity and key possession; lifecycle state determines whether the artifact remains acceptable for current reliance.

The executable lifecycle profile therefore applies these rules:

| Condition | Decision |
|---|---|
| `next_update` is in the future | artifact may remain usable, subject to other checks |
| `next_update` has been reached or passed | reject as stale and refresh |
| registry state is `inactive` | reject for current reliance |
| candidate manifest `updated_at` is older than last accepted manifest | reject as rollback |
| file key remains in current manifest during rotation overlap | accept, subject to other checks |
| file key has been removed from current manifest | reject |
| authority refresh fails while cached authority is still fresh | permit cached authority until its bound expires |
| authority refresh fails after cached authority expires | fail closed |

## Executable vectors

The deterministic vectors live at:

`conformance/vectors/publishing/lifecycle.json`

They are evaluated by:

```bash
python scripts/verify_publishing_lifecycle.py
```

The evaluator uses a fixed evaluation time from the vector file. This makes CI repeatable and prevents test behavior from changing merely because wall-clock time advances.

## Security rationale

### Freshness is part of authority

A correct historic signature is not enough if a publisher has since removed a key, retired a registry, or replaced a manifest. `next_update` therefore acts as a maximum reliance horizon for cached state rather than as a scheduling hint only.

### Rollback must be distinguishable from refresh

A signed older manifest can still be cryptographically valid. Once a verifier has accepted a newer `updated_at`, accepting an older candidate would reopen previously retired state. The profile therefore treats backwards movement as a rollback condition.

### Rotation overlap and removal are different states

During planned rotation, both old and new keys may appear in the current manifest. Files signed by either currently authorized key can remain acceptable. Removal is the revocation boundary: after a key disappears from the authoritative current manifest, files relying on that key are rejected.

### Availability does not erase freshness bounds

A transient retrieval failure should not automatically invalidate a cached manifest that is still within its declared freshness period. Conversely, availability failure must not extend authority beyond `next_update`. Once the bound expires, the verifier fails closed until current authority can be established.

## Remaining scope

This increment does not yet simulate live network retrieval, TLS-origin validation, multi-verifier clock skew, or distributed cache propagation. Those concerns are better exercised in the multi-role scenario and operator-oriented work that follows.
