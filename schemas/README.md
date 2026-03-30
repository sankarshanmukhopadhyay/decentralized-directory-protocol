# Schema notes

The schemas in this directory are the canonical record-shape definitions for this repository.

Recent improvements in this pass include:

- migration from non-standard `url` format usage to standard `uri` where applicable,
- tighter `additionalProperties` handling on nested objects,
- stronger lifecycle fields for revocation and key history,
- constrained enumerations for cryptographic metadata,
- and clearer membership status and evidence semantics.

Schema changes should always be reflected in:

- examples,
- OpenAPI references,
- verifier/operator guidance,
- and the versioning policy.
