# Minimal node example

This example is the smallest runnable DeDi service in the repository.

## Run

```bash
python ../../reference-impl/server/server.py
```

## What it exposes

- `GET /health`
- `GET /dedi/query/example.org?page=1&page_size=20`
- `GET /dedi/lookup/example.org/public-key/did:example:merchant-123`

## Sample response

See `sample-response.json`.
