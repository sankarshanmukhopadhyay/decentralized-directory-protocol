# Lifecycle summary

A DeDi record typically passes through the following lifecycle stages.

1. **Create or publish** a record under an authoritative namespace.
2. **Update** the record when the public state changes.
3. **Supersede** older state when a new state becomes current.
4. **Revoke or suspend** when the subject should no longer be considered valid in scope.
5. **Retain or expose history** when historical auditability is part of the deployment model.

Operators should document which of these stages are supported for each record class.
