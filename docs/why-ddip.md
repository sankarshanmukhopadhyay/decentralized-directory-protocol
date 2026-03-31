# Why DeDi exists

Most trust systems eventually hit the same operational bottleneck. A verifier can validate a signature, but still needs to know which public key is current, whether the entity is still recognized, whether a credential or participant has been revoked, and which registry is authoritative for the namespace in question.

Those questions are rarely answered through a consistent interface. Teams end up integrating one registry at a time, re-implementing trust logic for each deployment, and carrying registry-specific assumptions directly into application code.

DeDi exists to reduce that fragmentation. It defines a common protocol and schema surface for publishing and consuming public directory data that matters to trust decisions.

## The practical problem

Without a shared directory protocol, ecosystems tend to accumulate:

- custom resolver logic,
- inconsistent freshness and cache semantics,
- ambiguous authority boundaries,
- ad hoc revocation handling,
- and higher integration and audit cost.

## The design response

DeDi separates a few concerns cleanly:

- **directory infrastructure** from any single hosted product,
- **record shape** from ecosystem-specific policy,
- **discovery and retrieval** from the downstream decision policy,
- and **interoperability** from external assurance claims.

## What success looks like

A successful DeDi deployment makes it easier to:

- expose authoritative public state predictably,
- discover the right registry for a namespace,
- retrieve records through stable interfaces,
- validate payloads against shared schemas,
- and integrate multiple registries without rewriting the same logic repeatedly.
