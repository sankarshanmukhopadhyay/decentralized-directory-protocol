---
title: "Deployment Models"
nav_order: 3
parent: "Adoption & Conformance"
---
# Deployment models

DeDi is deliberately compatible with multiple deployment shapes.

## 1. Centralized directory

A single operator exposes DeDi-compatible endpoints over its system of record.

**Best for:** enterprise internal directories, ecosystem bootstrap, controlled onboarding flows.

## 2. Federated directory

Multiple operators expose compatible endpoints for different namespaces or record classes, with consumer-side trust policy deciding which authorities are accepted.

**Best for:** industry networks, sector-specific registries, cross-domain interoperability.

## 3. Gateway or wrapper deployment

A DeDi service sits in front of an existing registry or legacy API and normalizes its output into DeDi schemas.

**Best for:** low-friction adoption and phased migration.

## 4. Experimental decentralized deployment

Multiple independently operated nodes publish compatible directory surfaces with delegation and reference records used to connect namespaces.

**Best for:** research, ecosystem experimentation, and federation design work.

## Operator guidance

Whatever deployment model is chosen, the operator should make explicit:

- namespace authority,
- publishing rights,
- revocation rights,
- freshness expectations,
- evidence retention,
- and incident response contact paths.
