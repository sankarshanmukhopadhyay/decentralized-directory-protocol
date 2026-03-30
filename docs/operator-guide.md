# Operator guide

This guide is for teams operating a DeDi-compatible namespace or registry.

## Minimum operating model

An operator SHOULD define and publish:

- the namespace authority model,
- the registry inventory and schemas in use,
- the signing and key rotation model,
- authentication and authorization for management APIs,
- logging, monitoring, and incident response expectations,
- and the retention and disclosure policy for historical versions.

## Deployment baseline

A production-grade deployment SHOULD include:

- TLS termination and certificate lifecycle management,
- durable storage for records and version history,
- schema validation on write paths,
- rate limiting and abuse controls,
- audit logging for all protected operations,
- secure secret management,
- and tested backup and restore procedures.

## Namespace management

Document:

- how a namespace is claimed,
- who is allowed to publish,
- how delegation works,
- how authority is transferred,
- and how disputes or suspensions are handled.

## Protected operations

Protected operations SHOULD use short-lived credentials and SHOULD avoid long-lived static bearer tokens where possible. Delegated access SHOULD be scoped to namespace, registry, or record level and SHOULD carry an explicit expiry.

## History and mutation policy

Operators SHOULD document which registries are mutable, append-only, or destructive. Revocation and key-history registries SHOULD strongly prefer append-only behavior.
