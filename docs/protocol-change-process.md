---
title: "Protocol Change Process"
nav_order: 3
parent: "Protocol Specification"
---
# Protocol change process

This document defines how substantive changes to the DeDi protocol, schemas, or API contract are proposed, discussed, and accepted. It replaces informal ad-hoc discussion for anything that affects interoperability or compatibility.

## Scope

This process applies to changes that:

- modify the semantics of an existing schema field,
- add or remove required fields from any schema,
- change API endpoint paths, parameters, or response shapes,
- alter normative MUST/SHOULD language in the protocol specification,
- or affect documented conformance behavior.

Documentation-only changes, typo fixes, new non-normative examples, and clarifications that do not change behavior may be submitted as regular pull requests without a formal proposal.

## Protocol Change Proposal (PCP)

A Protocol Change Proposal is a structured GitHub issue that frames the change before implementation work begins. It is not heavyweight — the goal is to make trade-offs visible and give the community a stable place to discuss the idea.

### Opening a PCP

Create a GitHub issue with the title prefix `PCP:` and include the following sections:

```markdown
## Summary
One or two sentences describing the change.

## Motivation
What problem does this solve? What ambiguity or limitation is addressed?
Describe the current behavior and why it is insufficient.

## Proposed change
What should the new behavior be? Include field names, endpoint changes, or
normative language where relevant.

## Compatibility impact
Is this a breaking change? Which versions are affected?
What migration path exists for existing implementations?

## Artifacts to update
List the files that will need to change:
- [ ] Schema file(s)
- [ ] Example payloads
- [ ] OpenAPI contract
- [ ] Protocol specification
- [ ] Versioning or compatibility notes
- [ ] Other docs

## Open questions
What is still uncertain? What feedback are you seeking?
```

### PCP lifecycle

| State | Meaning |
|---|---|
| `pcp: open` | Proposal is open for discussion |
| `pcp: accepted` | Maintainers have approved it for implementation |
| `pcp: deferred` | Good idea, but not in scope for current work |
| `pcp: withdrawn` | Proposer has withdrawn it |
| `pcp: rejected` | Not aligned with protocol goals; explained in the issue |

Apply the appropriate label when the state changes.

### Acceptance criteria

A PCP is accepted when:

- the compatibility impact is clearly stated and the breaking/non-breaking classification is agreed upon,
- the list of artifacts to update is complete,
- and a maintainer has explicitly approved it in the issue.

Acceptance does not require consensus from all commenters, but significant unresolved objections from the community should be addressed or acknowledged before closing.

## Implementation

Once a PCP is accepted:

1. Open a pull request that links to the PCP issue (e.g., `Implements PCP #42`).
2. Ensure all artifacts listed in the PCP are updated.
3. Run the validation script locally before requesting review.
4. A maintainer reviews and merges the PR.
5. The PCP issue is closed with a link to the merged PR.

## Versioning

Protocol changes follow the versioning policy in [versioning-policy.md](versioning-policy.md). The PCP process does not change those rules — it provides the discussion record before the version bump is decided.

## Backward-compatible changes

For non-breaking additions (e.g., a new optional field or a new schema family), a full PCP is encouraged but not required if the change is narrow and clearly non-breaking. A PR with a clear description and updated examples is sufficient.

## Related

- [Versioning policy](versioning-policy.md)
- [Contributing guide](../CONTRIBUTING.md)
- [Protocol specification](protocol-spec.md)
