# Conformance guidance

This repository includes a starter conformance surface rather than a full interop suite.

## Minimum profile

A minimum DeDi-compatible implementation SHOULD:

- expose documented query and lookup behavior,
- validate published records against declared schemas,
- document namespace authority,
- document signing and verification expectations,
- and publish examples that pass validation.

## Extended profile

An extended implementation SHOULD also:

- expose historical lookup behavior,
- document freshness and caching semantics,
- support append-auditable key and revocation history,
- and publish machine-readable API contracts.
