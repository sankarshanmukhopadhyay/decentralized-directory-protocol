# Governance

This repository is managed as an open protocol project with a bias toward machine-verifiable artifacts, incremental implementability, and evidence-backed change.

## Project goals

The project exists to make directory infrastructure easier to implement, evaluate, interoperate with, and govern across ecosystems.

## Scope of this repository

This repository covers:

- protocol documentation,
- schemas and examples,
- API contract artifacts,
- conformance profiles and vectors,
- evidence artifact formats,
- and contributor-facing implementation material.

This repository does **not** by itself define ecosystem trust policy, assurance obligations, or legal operating rules for every deployment.

## Governance lens

The protocol should make it possible to answer, and test, the following questions:

- Which authority controls a namespace?
- Who may publish, update, suspend, or revoke records?
- What delegation exists, and with what scope and expiry?
- What evidence is produced when state changes?
- What can a verifier test locally before trusting a response?

## Decision model

The maintainers aim to make changes through reviewable pull requests with rationale captured in commit history, linked issues, and documentation updates.

The default expectation is:

1. clarify the problem,
2. propose the smallest reviewable change,
3. update protocol, docs, examples, tests, and evidence expectations together,
4. keep protocol claims aligned with what can be implemented and validated.

## Change classes

### Clarifications
Non-breaking improvements to wording, examples, diagrams, or implementation guidance.

### Additive changes
New optional fields, guides, examples, profile definitions, vectors, or non-breaking API and schema extensions.

### Breaking changes
Schema or protocol changes that alter existing expectations for publishers, consumers, or verifiers. These must be called out in versioning and migration notes and reflected in the versioned spec surface.

## Roles

### Maintainers
Review and merge changes, curate project direction, approve compatibility-impacting changes, and keep protocol and docs aligned.

### Contributors
Improve schemas, examples, governance artifacts, tests, guides, and issue quality.

### Implementers
Use the repository artifacts in deployments, pilots, and integrations, and report ambiguity or interoperability gaps.

### Operators
Run directory services, publish evidence, and ensure their deployment-specific authority and revocation policies are externally documented.

## Proposal pathway

Substantive protocol changes should be proposed through a focused issue or pull request that explains:

- the current ambiguity or pain point,
- the intended change,
- the compatibility impact,
- the governance and lifecycle implications,
- the docs and examples that need to move together,
- and any conformance or evidence implications.

## Release and stability signaling

The repository uses semantic-versioning principles for tagged releases, but maturity should always be read together with:

- [`docs/stability.md`](docs/stability.md)
- [`docs/versioning-policy.md`](docs/versioning-policy.md)
- [`conformance/profiles/`](conformance/profiles/)
- [`evidence/`](evidence/)
