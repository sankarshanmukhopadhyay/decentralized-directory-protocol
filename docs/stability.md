# Stability and maturity guidance

This repository should be read as an implementation-oriented draft with a stronger developer experience than a minimal specification dump.

## Current maturity signals

| Surface | Current signal | What that means |
|---|---|---|
| Core documentation | Expanded | Suitable for orientation, architecture review, and implementation planning |
| Schemas | Draft but usable | Appropriate for experiments, pilots, and feedback-driven refinement |
| API contract | Initial | Useful as a machine-readable baseline, not a guarantee of all deployment behavior |
| Conformance guidance | Baseline | Good for compatibility claims at an initial level, not a full interop regime |
| Governance and contribution | Present | Clearer path for external collaboration and review |

## How to read stability claims

A DeDi-compatible deployment may be operationally stable even if the protocol repository is still evolving. Conversely, a stable repository does not automatically imply a trustworthy or production-ready deployment.

Consumers should evaluate:

- namespace authority,
- freshness semantics,
- signing and provenance,
- revocation handling,
- operational availability,
- and ecosystem-specific trust policy.
