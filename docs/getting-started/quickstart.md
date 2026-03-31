# Quickstart

This quickstart is the fastest route from zero to a working mental model.

## What you will do

1. inspect a schema,
2. validate a sample payload,
3. issue a query request,
4. fetch a record,
5. apply basic verifier checks.

## Step 1: pick a schema

Start with [`schemas/public_key.json`](../../schemas/public_key.json) if your use case involves key discovery.

## Step 2: inspect a valid sample

See [`examples/public-key/sample.json`](../../examples/public-key/sample.json).

## Step 3: validate the repository artifacts

```bash
python -m pip install jsonschema openapi-spec-validator PyYAML
python scripts/validate_artifacts.py
```

## Step 4: query a namespace

```bash
curl -s "https://api.dedi.global/dedi/query/example.org?page=1&page_size=20"
```

## Step 5: look up a concrete record

```bash
curl -s "https://api.dedi.global/dedi/lookup/example.org/public-key/did:example:merchant-123"
```

## Step 6: apply verifier logic

At minimum:

- validate the payload against the declared schema,
- check you trust the namespace authority,
- verify freshness and revocation semantics,
- and only then use the returned state in your decision flow.

## Next steps

- [Build with DeDi](../build-with-dedi.md)
- [Verifier guide](../verifier-guide.md)
- [Operator guide](../operator-guide.md)
- [Conformance profiles](../../conformance/profiles.md)
