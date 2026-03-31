# Conformance profiles

## Baseline profile

An implementation claiming baseline DeDi compatibility SHOULD:

- expose documented query and lookup behavior,
- identify the namespace authority model,
- validate published records against declared schemas,
- publish examples that pass validation,
- document freshness and cache behavior,
- and document how revocation and supersession are represented.

## Recommended profile

A stronger implementation SHOULD also:

- publish an OpenAPI contract,
- retain historical state where appropriate,
- expose operational guidance for consumers,
- and support automated artifact validation in CI.

## Evidence expectations

A credible compatibility claim should point to:

- the implementation endpoint,
- the schemas used,
- passing validation artifacts,
- example queries and lookups,
- and public documentation explaining trust boundaries.
