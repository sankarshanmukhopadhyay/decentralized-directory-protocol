---
title: "Publishing Workflow"
nav_order: 5
parent: "Build & Integrate"
---
# Publishing workflow

## Typical publisher sequence

1. Establish namespace authority.
2. Define the registry and schema.
3. Validate the record payload.
4. Sign or otherwise bind the record to the published trust model.
5. Publish through the management API.
6. Confirm the record is retrievable through public read paths.
7. Publish update, revocation, or retirement events as needed.

## Mutation guidance

- Treat key history and revocation history as append-first unless there is a strong reason not to.
- Keep correction workflows distinct from revocation workflows.
- Do not delete historical material without a documented retention policy.
