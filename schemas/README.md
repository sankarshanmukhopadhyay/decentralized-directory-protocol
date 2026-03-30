# Schemas

These JSON Schema files define the currently documented DeDi record formats.

## How to use them

Use the schemas to:

- validate records before publishing,
- validate responses when integrating with a directory,
- document the shape of directory entries,
- and reduce ambiguity across implementations.

## Schema notes

### `public_key.json`
Use for current public key discovery. Particularly useful in signature verification and trust bootstrapping.

Key implementation considerations:

- document identifier semantics for `public_key_id`,
- explain how key rotation is handled,
- clarify whether `previousKeys` is advisory or complete history.

### `revoke.json`
Use for any negative-list or revocation state.

Key implementation considerations:

- define what identifier is being revoked,
- explain whether absence means not revoked or unknown,
- document freshness expectations clearly.

### `membership.json`
Use for public affiliation or membership state.

Key implementation considerations:

- explain the authority behind the membership claim,
- define the semantics of `memberSince` and `memberTill`,
- document how `evidence` should be interpreted.

### `Beckn_subscriber.json`
Use for publishing Beckn participant records.

Key implementation considerations:

- ensure `subscriber_id` and `url` semantics are consistent,
- define expected domain constraints,
- document key usage expectations.

### `Beckn_subscriber_reference.json`
Use for indirection to another registry or record.

Key implementation considerations:

- define reference resolution behavior,
- explain trust assumptions when dereferencing another resource.
