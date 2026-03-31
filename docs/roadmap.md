---
title: "Roadmap"
nav_order: 11
---
# Roadmap

This roadmap is intentionally practical. It focuses on the moves that most improve implementability and adoption.

## Immediate priorities

### 1. Tighten discovery conventions ✓
Discovery is now documented in [`docs/discovery.md`](discovery.md) with concrete endpoint patterns, curl examples, and a client-side checklist. The reference client (`scripts/client_demo.py`) implements discovery programmatically.

### 2. Add conformance and validation guidance ✓
A lightweight conformance profile and validation guide now live in [`conformance/`](../conformance/). The validation script runs in CI on every push and PR via `.github/workflows/validate.yml`. The [`conformance/validation-guide.md`](../conformance/validation-guide.md) covers local runs, manual payload validation, and evidence expectations for conformance claims.

### 3. Expand examples into end-to-end flows ✓
[`examples/end-to-end/README.md`](../examples/end-to-end/README.md) covers four complete flows with step-by-step curl commands and Python verification logic: key discovery, revocation checking, membership validation, and historical audit lookup.

### 4. Clarify versioning policy ✓
[`docs/versioning-policy.md`](versioning-policy.md) now defines patch/minor/major compatibility rules, schema evolution cases (adding optional fields, adding required fields, removing fields, changing types), deprecation behavior, and experimental feature handling.

### 5. Improve contribution process ✓
[`docs/protocol-change-process.md`](protocol-change-process.md) defines the Protocol Change Proposal (PCP) process with a structured issue template, lifecycle labels, and acceptance criteria. [`CONTRIBUTING.md`](../CONTRIBUTING.md) is updated to reference it.

## Medium-term priorities

- More schema families for common trust use cases. ✓ `endpoint.json` added for service endpoint advertisement.
- Example client and server implementations. ✓ `scripts/client_demo.py` is a reference CLI client covering discover, query, lookup, revocation check, and local validation.
- Better federation and cross-registry discovery guidance. ✓ [`docs/federation.md`](federation.md) covers reference records, namespace delegation, and cross-registry consumer patterns.
- Ecosystem mappings beyond current included schemas. ✓ [`docs/compare-and-position.md`](compare-and-position.md) now covers DID resolution, OpenID Federation, TRAIN, Verifiable Data Registries, and Beckn registries.

## Strategic goal

The long-term goal should be simple: make DeDi feel less like an interesting concept and more like a protocol developers can confidently build into real systems.
