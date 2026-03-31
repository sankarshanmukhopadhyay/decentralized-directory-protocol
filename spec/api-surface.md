# API surface summary

The repository includes an initial OpenAPI contract for common DeDi behaviors.

## Main interaction patterns

- **Query:** discover records under a namespace
- **Lookup:** retrieve a concrete record by identifier
- **Version or metadata endpoints:** expose compatibility and lifecycle information where supported

## Guidance

Use [`api/openapi.yaml`](../api/openapi.yaml) as the machine-readable contract baseline and treat deployment-specific documentation as the source for operator-specific semantics.
