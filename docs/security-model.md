---
title: "Operations & Security"
nav_order: 9
has_children: true
---
# Security model

This document provides the initial security baseline for DeDi-compatible implementations.

## Security posture goal

DeDi is designed to reduce ambiguity around public trust data. The core security goal is not secrecy. It is **authenticity, freshness, provenance, controlled mutation, and safe consumption**.

## Protected assets

The most important assets are:

- namespace authority and control,
- registry integrity,
- active public keys,
- revocation state,
- membership and participant status,
- version history,
- delegated administrative rights,
- operator credentials,
- and audit trails.

## Trust boundaries

The main trust boundaries are:

1. between namespace authority and registry operator,
2. between publisher and API management surface,
3. between public read paths and protected write paths,
4. between DeDi responses and downstream consumers,
5. between active key material and historical key material.

## Threat categories

### Spoofing
Examples include namespace impersonation, public-key substitution, fake subscriber endpoints, and reference hijacking.

### Tampering
Examples include unauthorized record mutation, revocation deletion, field injection, and silent schema drift.

### Repudiation
Examples include incomplete history, unverifiable delegation, and missing evidence for when a state changed.

### Information disclosure
Examples include unsafe enumeration, unrestricted historical state disclosure, and accidental credential exposure in tooling.

### Denial of service
Examples include revocation-list flooding, expensive historical queries, and abuse of query pagination or recursion.

### Elevation of privilege
Examples include over-broad delegation, static bearer secret replay, and weak operator credential practices.

## Security assumptions

This repository assumes:

- the operator will provide TLS transport security,
- the namespace authority model will be documented,
- the signing and verification model will be documented,
- and verifiers will not blindly trust schema validity as a substitute for policy.

## Minimum mitigations

Implementations SHOULD adopt the following controls:

- documented namespace authority and trust-anchor discovery,
- scoped and time-bounded delegated administration,
- short-lived credentials for protected operations,
- schema validation on write and read paths,
- rate limits for bulk query and historical access,
- append-only or auditable history for keys and revocations,
- log integrity protection and incident runbooks,
- explicit algorithm allow-lists for public-key records.

## High-priority implementation risks surfaced by repository review

The security review work attached to this repo emphasized several practical concerns:

- public-key substitution risk where identity and key material are weakly bound,
- domain mismatch risk in Beckn subscriber records,
- insufficiently specified revocation lifecycle metadata,
- permissive nested object schemas,
- unsafe handling of reference URLs,
- exposure risk from static Postman credentials,
- enumeration and historical-query abuse potential,
- and under-specified delegation semantics.

These concerns informed the schema, documentation, and CI improvements included in this pass.
