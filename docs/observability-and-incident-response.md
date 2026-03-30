# Observability and incident response

## Minimum logs

Operators SHOULD log:

- authenticated management actions,
- record creation and mutation events,
- delegation grants and revocations,
- authentication failures,
- rate-limit triggers,
- and administrative configuration changes.

## Monitoring signals

Useful baseline signals include:

- abnormal write volume,
- large query pagination patterns,
- repeated historical lookup abuse,
- bursts of revocation creation,
- and failed signature validation or schema validation rates.

## Incident classes

At minimum, maintain runbooks for:

- key compromise,
- unauthorized mutation,
- namespace ownership dispute,
- credential leakage,
- and service degradation due to expensive queries.
