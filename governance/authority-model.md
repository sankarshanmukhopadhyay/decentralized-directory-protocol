# Authority model

DeDi itself does not assign legitimacy. It does, however, need deployments to make authority legible.

## Minimum authority questions

A deployment should document:

- which organization controls a namespace,
- who can publish records into that namespace,
- who can suspend or revoke records,
- what delegation is permitted,
- how delegation expires or is revoked,
- and where verifiers can inspect current authority state.

## Recommended control pattern

1. **Namespace authority** is rooted in an identified operator.
2. **Delegated operators** receive explicit scope and expiry.
3. **Publishing actions** are logged as reviewable state changes.
4. **Revocation** can be exercised independently of publication.
5. **Evidence** is retained for operational review.
