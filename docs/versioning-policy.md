---
title: "Versioning Policy"
nav_order: 2
parent: "Protocol Specification"
---
# Versioning policy

The repository uses semantic versioning principles for protocol and schema evolution. This document defines what constitutes a breaking change, how deprecation works, and what migration support is expected.

## Version scope

Versioning applies to three surfaces independently:

| Surface | Where versioned | Current version |
|---|---|---|
| Protocol specification | `docs/protocol-spec.md` preamble | 0.1 |
| API contract | `api/openapi.yaml` `info.version` | 0.1.0 |
| Schemas | `$schema` URI + catalog version | 0.1.0 |

A change to one surface does not automatically bump the others. Each surface is versioned only when it changes.

## Compatibility rules

### Patch (x.y.**Z**)

Patch changes SHOULD be documentation, examples, or non-breaking clarifications. A patch change MUST NOT:

- change the meaning of an existing field,
- add a required field,
- remove a field,
- or change a normative MUST/SHOULD assertion.

Patch changes MAY:

- fix typos or formatting,
- improve examples without changing payloads,
- add non-normative notes.

### Minor (x.**Y**.0)

Minor changes MAY add optional fields, new endpoints, or new schemas without breaking existing consumers. A minor change MUST NOT:

- remove existing fields or endpoints,
- make an optional field required,
- or change the semantics of an existing field.

Minor changes SHOULD include updated examples, migration notes if any behavioral clarification is included, and updated conformance documentation if a new capability is added.

### Major (**X**.0.0)

Major changes MUST be used for breaking schema, protocol, or API behavior changes. A breaking change is any change that would cause a conformant existing consumer or publisher to produce incorrect results without modification.

Major changes MUST:

- be introduced through the [protocol change process](protocol-change-process.md),
- clearly identify which fields, endpoints, or behaviors are affected,
- update all related examples,
- update the OpenAPI contract and conformance profiles,
- and include migration notes.

## Schema evolution

When a schema changes:

- **Adding an optional field** — minor bump. Existing valid payloads remain valid.
- **Adding a required field** — major bump. Existing payloads without the field become invalid.
- **Removing a field** — major bump. Always treated as breaking.
- **Changing field type or format** — major bump. Changing `string` to `integer`, or `date` to `date-time`, breaks existing payloads.
- **Tightening enum values** — major bump. Restricting allowed values breaks existing publishers.
- **Loosening enum values** — minor bump. Expanding allowed values is backward-compatible.

Breaking schema changes MUST:

- update all sample and invalid examples,
- update OpenAPI schema references where applicable,
- update verifier and operator guidance,
- and include migration notes.

## Deprecation

A field or behavior may be deprecated before removal. Deprecation signals intent to remove in a future major version.

- Deprecated fields SHOULD be marked with a note in the schema `description`.
- The deprecated state MUST be visible in the OpenAPI contract.
- At least one full minor version cycle SHOULD pass between deprecation and removal.
- Migration guidance MUST be published at the time of deprecation.

## Experimental features

New endpoints or schema additions explicitly marked experimental in documentation and the OpenAPI contract may change at minor version boundaries without being considered breaking. Experimental status MUST be clearly documented.

## Related

- [Protocol change process](protocol-change-process.md)
- [Stability signals](stability.md)
- [API contract](../api/openapi.yaml)
- [Conformance profiles](../conformance/profiles.md)
