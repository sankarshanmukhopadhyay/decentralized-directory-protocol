# Adoption guide

This guide is written for teams deciding whether and how to adopt DeDi.

## The shortest adoption decision

Adopt DeDi if you have public, authoritative information that other systems need to query in a machine-readable way, or if your application needs to consume that kind of information from multiple registries without bespoke integration work each time.

## Adoption paths

### Path A: Wrap an existing registry

This is the lowest-friction path.

1. Keep your current registry as the system of record.
2. Map records to one or more DeDi schemas.
3. Publish DeDi-compatible endpoints.
4. Add examples and consumer documentation.

This path is often enough to unlock interoperability without replatforming.

### Path B: Build DeDi into a new trust layer

This path makes sense when you are designing a new ecosystem, participant registry, or verifier network.

1. Define your namespaces.
2. Define which directory types are needed.
3. Reuse existing DeDi schemas where possible.
4. Add ecosystem-specific schemas only where necessary.
5. Publish clear trust and discovery guidance.

### Path C: Consume DeDi from a relying-party workflow

This path fits verifiers, wallets, onboarding platforms, trust registries, and network participants.

1. Identify the directories you need.
2. Define your trusted sources.
3. Add schema validation.
4. Build policy around freshness, outages, and negative results.

## What increases adoption fastest

If the objective is developer adoption, the highest ROI moves are:

- a clearly structured README,
- copy-paste examples,
- schema-specific implementation notes,
- a realistic end-to-end tutorial,
- and visible governance for changes.

## What usually blocks adoption

These are common reasons a technically interesting project remains hard to adopt:

- the protocol is described conceptually but not operationally,
- example payloads are missing,
- discovery is left implicit,
- schema semantics are underspecified,
- or the project feels tied to one vendor or one deployment.

## Recommended maturity sequence

1. Make one schema easy to use.
2. Make one directory easy to publish.
3. Make one consumer integration easy to implement.
4. Add conformance and interoperability tests.
5. Add governance and versioning discipline.

That sequence tends to create real adoption faster than expanding scope too early.
