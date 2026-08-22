# Fork authority and adoption posture

This repository is a working fork of the upstream **Decentralized Directory Protocol (DeDi)** project maintained at `LF-Decentralized-Trust-labs/decentralized-directory-protocol`.

The purpose of this fork is to make DeDi easier to implement, evaluate, test, operate, and integrate into real trust systems. It may contain implementation aids, conformance material, assurance evidence, deployment guidance, experimental profiles, additional examples, and other fork-local artifacts that are not part of the upstream project.

## Authority boundary

The upstream project remains authoritative for upstream DeDi governance, normative protocol decisions, upstream releases, and upstream conformance claims.

This fork does **not** claim:

- authorship or ownership of upstream DeDi;
- authority to redefine upstream normative semantics;
- authority to publish an upstream DeDi release;
- that a fork-local feature has been accepted by upstream maintainers; or
- that fork-local conformance or assurance material represents an upstream certification program.

Where this fork mirrors upstream material, the upstream source remains the reference for upstream intent.

## What the fork is for

Fork-local work is intended to improve the practical utility of DeDi by providing a stronger implementation and evaluation surface around the protocol. Typical additions include:

- runnable reference implementations and end-to-end walkthroughs;
- machine-verifiable schemas, test vectors, and conformance profiles;
- operator and verifier guidance;
- governance, delegation, revocation, observability, and incident-response patterns;
- evidence artifacts that make validation results inspectable and reproducible;
- interoperability mappings to adjacent trust infrastructure; and
- experimental profiles used to pressure-test adoption patterns before any upstream proposal is considered.

The objective is not to create a competing DeDi protocol. The objective is to maintain a useful workbench around the upstream protocol while preserving provenance and governance boundaries.

## Upstream synchronization

The fork should periodically synchronize with upstream `main` before substantial new development begins.

Synchronization should:

1. preserve upstream commit ancestry;
2. retain fork-local implementation and assurance work where it does not conflict with upstream semantics;
3. reconcile overlapping documentation and schemas deliberately rather than silently replacing either side; and
4. avoid opening a pull request against upstream unless an upstream contribution is explicitly intended.

A fork being ahead of upstream after synchronization is expected: those additional commits represent fork-local work.

## Normative and non-normative material

Fork-local documents should state their status clearly.

A useful default classification is:

| Material | Fork posture |
|---|---|
| Upstream specification text mirrored in the fork | Upstream-derived; upstream remains authoritative |
| Fork implementation code | Fork-local implementation |
| Fork conformance profiles and tests | Fork-local evaluation material |
| Fork assurance evidence | Fork-local evidence; not upstream certification |
| Experimental profiles or mappings | Non-normative and experimental unless explicitly adopted upstream |
| Deployment and operator guidance | Fork-local implementation guidance |

When an artifact extends beyond what upstream specifies, it should avoid language that implies an upstream requirement unless the requirement can be traced to upstream normative text.

## Adoption principle

The fork should optimize for **working-system utility**, not repository activity for its own sake.

A substantive improvement should ideally make at least one of the following measurably better:

- **time to first success** for an implementer;
- **interoperability confidence** between implementations;
- **operational clarity** for publishers, indexers, verifiers, or relying parties;
- **testability** of protocol behavior;
- **auditability** of decisions and validation results;
- **governance traceability** for authority, delegation, and revocation; or
- **evidence quality** available to an evaluator or operator.

Documentation is valuable when it enables one of those outcomes. Documentation volume alone is not an objective.

## Experimental work

Experimental integrations should be explicitly marked **non-normative**, should pin the DeDi version or upstream commit they were evaluated against, and should avoid modifying the meaning of upstream protocol elements merely to fit another system.

If an experiment reveals a genuine protocol gap, the fork should document:

1. the observed implementation problem;
2. the upstream behavior or text that creates the constraint;
3. the fork-local workaround, if any;
4. interoperability or security implications; and
5. the smallest possible upstream change that could resolve the gap.

Only the last step should become an upstream contribution, and only when explicitly chosen.

## Current development direction

The near-term development strategy for this fork is to build a coherent implementer and operator workbench around DeDi:

1. preserve a clean upstream/fork authority boundary;
2. reconcile the upstream origin-hosted publishing model with the fork's implementation and conformance surfaces;
3. turn conformance profiles into executable, evidence-producing tests;
4. improve operational lifecycle coverage, especially freshness, revocation, delegation, and failure handling;
5. build richer end-to-end scenarios that exercise the protocol across publisher, discovery/indexing, and verifier roles; and
6. expose the resulting implementation, test, and assurance surfaces clearly through the documentation site.

This sequence keeps the fork differentiated through utility while keeping upstream DeDi canonical for upstream protocol governance.