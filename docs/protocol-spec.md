---
title: "Protocol Specification"
nav_order: 7
has_children: true
---
# DeDi protocol specification

## Status

This document is the normative protocol baseline for the repository. It defines the minimum interoperable behavior expected from DeDi-compatible publishers, operators, and consumers.

Normative keywords **MUST**, **SHOULD**, and **MAY** are to be interpreted as described in RFC 2119.

## 1. Roles

### Namespace authority
The party that controls a namespace and is responsible for authoritative publication under that namespace.

### Registry operator
The party that runs the API surface and persistence layer for one or more DeDi registries.

### Publisher
The party that creates, signs, updates, or revokes records.

### Verifier or relying party
The party that consumes DeDi records and uses them as inputs into trust decisions.

## 2. Core model

A DeDi publication surface consists of:

- a **namespace** that establishes trust and discovery scope,
- one or more **registries** within that namespace,
- and individual **records** within each registry.

A record MUST conform to a declared schema. A registry SHOULD contain only one record class. A namespace MUST publish enough metadata for verifiers to determine who controls it and which trust anchor applies.

## 3. Namespace authority and trust bootstrap

A namespace MUST be bound to an authority model that verifiers can evaluate. Acceptable authority models MAY include:

- domain-based control,
- certificate-bound service identity,
- ledger-anchored control record,
- or an equivalent signed trust-anchor document.

The chosen authority model MUST be documented by the namespace operator.

Delegation, transfer, suspension, and revocation of namespace control MUST be documented. A verifier SHOULD reject records from a namespace when control cannot be determined or when competing claims cannot be resolved by local policy.

## 4. Endpoint taxonomy

### Query endpoints
Query endpoints return collections, summaries, or filtered slices of namespace or registry data.

### Lookup endpoints
Lookup endpoints return the current or requested historical state of a specific namespace, registry, or record.

### Versions endpoints
Versions endpoints return version references or historical states for records and MUST be protected if the operator does not intend full public history disclosure.

## 5. Response semantics

A DeDi response SHOULD return:

- an explicit status,
- the response data,
- schema or record type information,
- timestamps relevant to freshness,
- and version identifiers where applicable.

Machine-readable errors MUST be returned for validation failures, authorization failures, missing records, conflicts, and transient server errors.

## 6. Proof and signing requirements

A DeDi deployment MUST define what is signed and how it is verified. At minimum:

- registry operators MUST document whether records are signed, responses are signed, or both,
- canonicalization rules MUST be defined,
- public-key discovery for verification MUST be documented,
- and verifier failure behavior MUST be specified.

Implementations SHOULD prefer detached or envelope-based signatures with explicit algorithm identifiers.

## 7. Freshness and replay handling

Every record class used in trust-sensitive flows SHOULD expose enough metadata for freshness decisions. Implementations SHOULD support:

- issuance or publication time,
- update time,
- version identifiers,
- and revocation or supersession semantics.

Operators SHOULD document maximum stale-read tolerances. Verifiers SHOULD treat stale but validly signed data as a policy input, not as automatically trustworthy data.

## 8. Key lifecycle

Public-key publication MUST document:

- active key semantics,
- previous key history,
- rotation windows,
- compromise and emergency replacement behavior,
- and verifier expectations for old signatures.

Emergency key compromise response MUST include revocation or retirement metadata.

## 9. Revocation and status semantics

Revocation records MUST identify the revoked subject. Trust-sensitive implementations SHOULD also expose:

- the revocation time,
- the revoking authority,
- the scope of revocation,
- and whether reinstatement is possible.

Verifiers MUST NOT assume that the absence of a revocation record proves permanent validity unless the operator explicitly defines that behavior.

## 10. Authentication and authorization

Public discovery endpoints MAY be unauthenticated. Protected publication, management, and delegated administration endpoints MUST use a documented authentication and authorization model.

Operators SHOULD prefer short-lived credentials over static bearer secrets. Delegation SHOULD be scoped and time-bounded.

## 11. Historical lookup

If `as_on` or historical version queries are supported, operators MUST define:

- the retention policy,
- the access policy,
- the performance constraints,
- and the authoritative semantics for historical reconstruction.

## 12. Versioning and compatibility

Protocol, API, and schema changes MUST follow the repository versioning policy in [versioning-policy.md](versioning-policy.md).

Breaking changes MUST be clearly identified and SHOULD ship with migration guidance and updated examples.
