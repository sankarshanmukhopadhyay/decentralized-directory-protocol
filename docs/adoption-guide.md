---
title: "Adoption & Conformance"
nav_order: 8
has_children: true
---
# Adoption guide

This guide is written for teams deciding whether and how to adopt DeDi.

## The shortest adoption decision

Adopt DeDi if you have public, authoritative information that other systems need to query in a machine-readable way, and you want that surface to be implementable, testable, and portable across registries.

## What improves developer adoption fastest

The highest-ROI adoption moves are:

1. a deterministic quickstart that reaches a successful result,
2. a minimal reference server and client,
3. schemas with valid and invalid examples,
4. machine-readable conformance profiles,
5. governance artifacts that make authority and revocation explicit,
6. and evidence outputs that show what a verifier can rely on.

## Adoption paths

### Path A: Wrap an existing registry

This is the lowest-friction path.

1. Keep your current registry as the system of record.
2. Map records to one or more DeDi schemas.
3. Publish DeDi-compatible endpoints.
4. Add conformance and example coverage.
5. Publish authority and revocation guidance.

### Path B: Build DeDi into a new trust layer

This path makes sense when you are designing a new ecosystem, participant registry, or verifier network.

1. Define namespaces and publishing authorities.
2. Define which directory types are needed.
3. Reuse existing DeDi schemas where possible.
4. Add ecosystem-specific schemas only where necessary.
5. Establish evidence expectations for operators.

### Path C: Consume DeDi from a relying-party workflow

This path fits verifiers, wallets, onboarding platforms, trust registries, and network participants.

1. Identify the directories you need.
2. Define trusted directory sources.
3. Add schema validation and freshness handling.
4. Build policy for outages, negative results, and revocation.
5. Retain evidence for operational or audit review.

## What usually blocks adoption

Common reasons a technically interesting project remains hard to adopt:

- the protocol is described conceptually but not operationally,
- no minimal implementation exists,
- conformance claims are not machine-verifiable,
- governance is implied instead of explicit,
- discovery is underspecified,
- or the project feels tied to one deployment model.

## Recommended maturity sequence

1. Make one schema easy to use.
2. Make one directory easy to publish.
3. Make one consumer integration easy to implement.
4. Make conformance and evidence reproducible.
5. Add more schemas only after the base path is solid.
