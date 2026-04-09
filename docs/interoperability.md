---
title: "Interoperability"
nav_order: 2
parent: "Adoption & Conformance"
---
# Interoperability positioning

DeDi is easier to adopt when its role in the stack is explicit.

## DeDi and DID resolution

DID resolution dereferences an identifier into a DID document or related metadata. DeDi addresses a broader public-directory problem: memberships, participant registries, endpoints, revocations, and public keys. The two can coexist cleanly. A DeDi record can reference a DID without requiring DeDi itself to become a DID method.

## DeDi and trust registries

A trust registry decides which authorities are recognized and under what policy. DeDi does not replace that governance layer. It provides the interoperable directory surface through which public state can be discovered and consumed.

## DeDi and TRQP

TRQP is a trust-query and assurance surface. DeDi is a directory-resolution and public-state retrieval surface. A TRQP deployment can use DeDi-compatible directories as authoritative or supporting inputs.

## DeDi and bespoke APIs

Bespoke APIs can work inside one deployment but push integration cost onto every downstream consumer. DeDi standardizes the recurring query and lookup surface so that consumers can reuse validation, lifecycle, and evidence patterns.

## Practical takeaway

The right way to position DeDi is not as a universal trust layer. It is a reusable directory interoperability layer that works best when paired with clear governance, assurance, and operator documentation.
