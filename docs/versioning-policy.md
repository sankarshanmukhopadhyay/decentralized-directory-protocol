# Versioning policy

The repository uses semantic versioning principles for protocol and schema evolution.

## Compatibility rules

- Patch changes SHOULD be documentation, examples, or non-breaking clarifications.
- Minor changes MAY add optional fields, examples, or endpoints without breaking existing consumers.
- Major changes MUST be used for breaking schema, protocol, or API behavior changes.

## Schema evolution

Breaking schema changes MUST:

- update examples,
- update OpenAPI references where applicable,
- update verifier and operator guidance,
- and include migration notes.
