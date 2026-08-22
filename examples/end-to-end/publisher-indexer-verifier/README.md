# Publisher → indexer → verifier walkthrough

This executable walkthrough connects the fork's publishing, cryptographic verification, freshness, and lifecycle work into a single trust path.

It is **fork-local, experimental, and non-normative**. The synchronized upstream DeDi baseline remains commit `72d913fb4d17507891a6fea5db1f49ef7b3f461d`.

## Run it

```bash
make scenario
```

or:

```bash
python scripts/run_publishing_scenario.py
```

The scenario writes machine-readable evidence to:

`evidence/publisher-indexer-verifier.json`

## Roles

### 1. Publisher

The publisher makes a signed manifest and signed registry artifact available. The scenario uses the deterministic cryptographic vectors introduced by the publishing profile.

### 2. Indexer

Before indexing any record, the indexer:

1. verifies the manifest detached JWS;
2. verifies that the manifest signing key is currently declared;
3. enforces manifest freshness;
4. verifies the registry file against the publisher's current manifest;
5. enforces registry-file freshness;
6. rejects an inactive registry; and
7. constructs an index only from state that has passed those checks.

The index retains the authority freshness horizon and source URL so downstream reliance remains connected to the authority state from which it was built.

### 3. Verifier

The verifier resolves `service-a` from the index and accepts the result only while the authority backing the index remains fresh.

The scenario then advances the evaluation time beyond the authority freshness horizon and confirms that the same indexed record is rejected rather than treated as indefinitely reusable.

## Why this matters

A directory protocol is not useful merely because each artifact can be validated independently. An implementation needs a rule for how authority flows across roles.

This scenario demonstrates the intended composition:

```text
Publisher
   |
   | signed manifest + signed registry
   v
Indexer
   |  verify authority
   |  verify file
   |  enforce lifecycle
   |  construct bounded index
   v
Verifier
   |  resolve record
   |  confirm authority horizon
   v
Reliance decision
```

The important property is that the index does not erase provenance or freshness. A verifier cannot safely convert a once-valid publisher statement into permanent local truth simply because an indexer cached it.

## Current limits

This is an offline executable scenario rather than a live deployment. It does not yet create separate HTTP services, simulate TLS failure, or model multiple independent indexers. Those are deployment-level extensions; the current scenario focuses on preserving verification and lifecycle semantics across the role boundary.
