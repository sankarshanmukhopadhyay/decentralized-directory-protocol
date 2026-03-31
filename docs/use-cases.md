---
title: "Use Cases"
nav_order: 2
parent: "Build & Integrate"
---
# Use cases

This document grounds the repository in concrete developer and ecosystem scenarios.

## 1. Public key lookup for verifiable transactions

A verifier receives a signed payload and needs the current public key for the signer.

DeDi role:

- locate the public key record,
- retrieve the current key,
- optionally inspect prior keys,
- and support key-rotation aware verification.

Relevant schema: `public_key.json`

## 2. Revocation checking before acceptance

A system needs to know whether an entity, participant, or credential reference has been revoked before continuing.

DeDi role:

- publish negative-list records,
- make them easy to query,
- and normalize the shape of the response.

Relevant schema: `revoke.json`

## 3. Membership and affiliation validation

An ecosystem participant claims membership in a consortium, program, or recognized group.

DeDi role:

- expose public affiliation records,
- support evidence pointers,
- and provide machine-readable membership dates and identifiers.

Relevant schema: `membership.json`

## 4. Beckn participant discovery

A system in a Beckn-aligned network needs to find participant endpoints and key material.

DeDi role:

- publish subscriber records,
- standardize discovery fields,
- and reduce per-network custom logic.

Relevant schema: `Beckn_subscriber.json`

## 5. Registry indirection and federation

A directory does not store the final record directly but needs to point to another authoritative DeDi-compatible resource.

DeDi role:

- support reference records,
- enable federated discovery,
- and make delegation explicit.

Relevant schema: `Beckn_subscriber_reference.json`

## 6. Cross-ecosystem trust registry normalization

A verifier integrates with multiple registries that publish broadly similar public state but with different field names and query patterns.

DeDi role:

- reduce integration fragmentation,
- provide reusable lookup and validation patterns,
- and make migration between registries easier.

## 7. Public-sector or consortium directories

A public-sector service or industry consortium needs a predictable way to publish recognized participants, service endpoints, keys, or status changes.

DeDi role:

- make authoritative publication easier to consume,
- support better operator and verifier documentation,
- and reduce one-off onboarding logic for each participant ecosystem.
