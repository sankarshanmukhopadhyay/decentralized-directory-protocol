# Governance

This repository is managed as an open protocol project.

## Project goals

The project exists to make directory infrastructure easier to understand, implement, evaluate, and interoperate with across ecosystems.

## Scope of this repository

This repository covers:

- protocol documentation,
- schemas and examples,
- API contract artifacts,
- conformance guidance,
- and contributor-facing implementation material.

This repository does **not** by itself define ecosystem trust policy, assurance obligations, or legal operating rules for every deployment.

## Decision model

The maintainers aim to make changes through reviewable pull requests with rationale captured in commit history and documentation updates.

The default expectation is:

1. clarify the problem,
2. propose the smallest reviewable change,
3. update the relevant docs, examples, and schemas together,
4. keep protocol and implementation claims aligned.

## Change classes

### Clarifications
Non-breaking improvements to wording, examples, and diagrams.

### Additive changes
New optional fields, guides, examples, or non-breaking API and schema extensions.

### Breaking changes
Schema or protocol changes that alter existing expectations for consumers or publishers. These should be clearly called out and reflected in versioning and migration notes.

## Roles

### Maintainers
Review and merge changes, curate project direction, and keep documentation aligned with the evolving protocol surface.

### Contributors
Improve schemas, examples, diagrams, implementation guidance, testability, and issue quality.

### Implementers
Use the repository artifacts in deployments, pilots, and integrations, and report ambiguity or interoperability gaps.

## Proposal pathway

Substantive protocol changes should be proposed through a focused issue or pull request that explains:

- the current ambiguity or pain point,
- the intended change,
- the compatibility impact,
- the docs and examples that need to move together,
- and any conformance implications.

## Release and stability signaling

The repository uses semantic-versioning principles for tagged releases, but maturity should always be read together with the stability guidance in [`docs/stability.md`](docs/stability.md).
