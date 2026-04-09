# Revocation model

Revocation is not a cosmetic add-on. It is a control-plane function.

## Minimum expectations

A DeDi deployment should make clear:

- which actor can revoke a record,
- whether revocation is terminal or reversible,
- what effective time applies,
- how a verifier should interpret stale cache entries,
- and what response shape indicates a revoked record.

## Repository artifacts

- `schemas/revoke.json` defines the public revocation record shape.
- `examples/revoke/` provides sample valid and invalid payloads.
- `conformance/tests/revocation/revocation-entry.yaml` binds lifecycle validation into a testable surface.
