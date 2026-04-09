---
title: "Quickstart"
nav_order: 1
parent: "Getting Started"
---
# Quickstart

This quickstart is optimized for **time to first success**. The objective is to go from clone to a working request, validated payload, and evidence artifact in roughly ten minutes.

## What you will do

1. install local validation dependencies,
2. validate repository artifacts,
3. start a minimal DeDi server,
4. issue a query and a lookup,
5. validate the response against the schema,
6. and inspect the evidence output.

## Step 1: install dependencies

```bash
python -m pip install -r requirements-dev.txt
```

## Step 2: validate repository artifacts

```bash
python scripts/validate_artifacts.py
```

This validates:

- schemas and sample payloads,
- OpenAPI,
- conformance profiles,
- conformance vectors,
- governance schema JSON,
- and evidence artifacts.

## Step 3: start the minimal reference server

In one terminal:

```bash
python reference-impl/server/server.py
```

The server listens on `http://127.0.0.1:8080`.

## Step 4: run the end-to-end quickstart helper

In a second terminal:

```bash
python scripts/query_and_verify.py
```

## Step 5: inspect the expected output

A successful run will:

- query the `example.org` namespace,
- look up `did:example:merchant-123` as a `public-key` record,
- validate the payload against `schemas/public_key.json`,
- and write `evidence/quickstart-run.json`.

## Step 6: inspect the evidence artifact

```bash
cat evidence/quickstart-run.json
```

## Alternative: use Make targets

```bash
make setup
make validate
make quickstart
```

## Next steps

- [Build with DeDi](../build-with-dedi.md)
- [Verifier guide](../verifier-guide.md)
- [Operator guide](../operator-guide.md)
- [Conformance overview](../conformance.md)
- [Deployment models](../deployment-models.md)
