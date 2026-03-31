# Test matrix

Use this matrix to self-assess a DeDi implementation before claiming conformance. Link to your evidence in the final column.

## Baseline profile

| Capability | Baseline expectation | How to verify |
|---|---|---|
| Namespace documentation | Present and publicly accessible | Link to public docs |
| Query behavior | Endpoint documented and reachable | Endpoint URL + sample response |
| Lookup behavior | Endpoint documented and reachable | Endpoint URL + sample response |
| Schema validation (valid) | Valid example payloads pass `validate_artifacts.py` | CI log or local run output |
| Schema validation (invalid) | Invalid example payloads correctly fail | CI log or local run output |
| Revocation semantics | Documented in operator or verifier guide | Link to docs |
| Freshness semantics | Documented — max stale-read tolerance stated | Link to docs |
| Namespace authority model | Authority model stated and verifiable | Link to docs |

## Recommended profile

| Capability | Recommended expectation | How to verify |
|---|---|---|
| OpenAPI contract | Published and valid | Link to file or hosted spec |
| Historical record retention | Retention and access policy documented | Link to operator guide |
| Automated validation in CI | Runs on every PR | CI badge or log link |
| End-to-end examples | At least one complete flow documented | Link to examples |
| Federation / reference records | Behavior documented if supported | Link to docs |

## Evidence checklist

A credible conformance claim should point to:

- [ ] Implementation endpoint (base URL)
- [ ] Schemas in use (names and versions)
- [ ] Passing validation artifacts (`validate_artifacts.py` output or equivalent)
- [ ] Example queries and lookup responses
- [ ] Documentation of trust boundaries, freshness policy, and revocation semantics

## Related

- [Conformance profiles](profiles.md)
- [Validation guide](validation-guide.md)
- [Validation script](../scripts/validate_artifacts.py)
