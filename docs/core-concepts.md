---
title: "Core Concepts"
nav_order: 3
---
# Core concepts

This page defines the minimum conceptual model needed to read the rest of the repository without constantly translating terms.

## Namespace
A namespace is the discovery and trust starting point under which one or more DeDi directories are published. In practice, it will often align with an organization, domain, or ecosystem authority boundary.

## Registry or directory
A registry is a published collection of records of a defined class under a namespace. This repository uses **directory** and **registry** in closely related ways, but the important point is that the collection has an authority boundary, access pattern, and lifecycle behavior.

## Record
A record is the individual published item returned to a consumer. A record may represent a public key, membership state, participant endpoint, or revocation event.

## Publisher
The actor or service responsible for creating, updating, or revoking records under the authority model of the namespace.

## Resolver or consumer
The software component that queries or looks up records from a DeDi-compatible directory.

## Verifier
The relying party that uses directory data as part of a trust decision. Verification is not only schema validation. It also involves provenance, freshness, and policy checks.

## Namespace authority
The actor or mechanism that establishes who is authorized to publish for a namespace. This can be documented through governance, signing material, operational controls, or linked trust anchors.

## Assertion
A published public-state claim carried by a record, such as a status, endpoint, or public key.

## Revocation
A published state indicating that an entity, key, credential, membership, or participant should no longer be treated as valid for a defined scope.

## Freshness
The degree to which a returned record is current enough for the decision being made. Freshness is contextual and should be documented by operators and enforced by consumers.
