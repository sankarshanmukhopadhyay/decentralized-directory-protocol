# End-to-end flows

This folder contains complete request/response sequences for the most common DeDi integration scenarios. Each flow covers discovery, retrieval, schema validation, and the verifier decision.

## Flow 1: Key discovery before signature verification

**Scenario.** A verifier receives a signed payload from `did:example:merchant-123` and needs to fetch the current public key before verifying the signature.

### Step 1 — Query the namespace

```bash
curl -s "https://api.dedi.global/dedi/query/example.org"
```

Response:
```json
{
  "message": "ok",
  "data": {
    "namespace": "example.org",
    "registries": [
      { "name": "public-key", "schema": "public_key" },
      { "name": "membership", "schema": "membership" },
      { "name": "revoke",     "schema": "revoke" }
    ]
  },
  "timestamp": "2026-03-31T00:00:00Z"
}
```

The namespace exposes a `public-key` registry using the `public_key` schema. Proceed to look up the specific record.

### Step 2 — Look up the public key record

```bash
curl -s "https://api.dedi.global/dedi/lookup/example.org/public-key/did:example:merchant-123"
```

Response:
```json
{
  "message": "ok",
  "data": {
    "public_key_id": "did:example:merchant-123",
    "publicKey": "-----BEGIN PUBLIC KEY-----\nMIIB...-----END PUBLIC KEY-----",
    "keyType": "Ed25519",
    "keyFormat": "PEM",
    "activatedAt": "2026-03-01T00:00:00Z",
    "entity": {
      "name": "Merchant One",
      "url": "https://merchant.example.org"
    },
    "previousKeys": [
      {
        "keyId": "merchant-123-key-2025",
        "publicKey": "abc123==",
        "keyType": "Ed25519",
        "keyFormat": "base64url",
        "revokedAt": "2026-02-28T12:00:00Z",
        "reason": "routine-rotation"
      }
    ]
  },
  "schema": "public_key",
  "version_id": "v3",
  "timestamp": "2026-03-31T00:00:00Z"
}
```

### Step 3 — Validate the payload

```python
import json
from jsonschema import Draft7Validator

schema  = json.loads(open("schemas/public_key.json").read())
payload = response["data"]  # from step 2

errors = sorted(Draft7Validator(schema).iter_errors(payload), key=lambda e: e.path)
assert not errors, f"Schema validation failed: {errors[0].message}"
```

### Step 4 — Apply verifier checks

```python
from datetime import datetime, timezone

now = datetime.now(timezone.utc)

# Check the key is active
activated = datetime.fromisoformat(payload["activatedAt"])
assert activated <= now, "Key activation date is in the future"

# Check the key type is in our allow-list
ALLOWED_KEY_TYPES = {"Ed25519", "RSA", "P-256"}
assert payload["keyType"] in ALLOWED_KEY_TYPES, f"Unexpected key type: {payload['keyType']}"

# Check freshness: reject if the record is more than 24 hours old
record_time = datetime.fromisoformat(response["timestamp"])
staleness = now - record_time
assert staleness.total_seconds() < 86400, "Record is stale"

# Now use the public key for signature verification
public_key_pem = payload["publicKey"]
```

---

## Flow 2: Revocation check before processing

**Scenario.** Before processing a request from `entity-abc`, check whether it has been revoked.

### Step 1 — Look up the revocation record

```bash
curl -s "https://api.dedi.global/dedi/lookup/example.org/revoke/entity-abc"
```

If the entity is **not revoked**, the server returns a 404:
```json
{
  "code": "NOT_FOUND",
  "message": "No revocation record found for entity-abc"
}
```

→ Continue processing.

If the entity **is revoked**, the server returns 200:
```json
{
  "message": "ok",
  "data": {
    "revoke_id": "entity-abc",
    "revokedAt": "2026-03-15T08:00:00Z",
    "issuer": "org.example.trust-authority",
    "reason": "policy-violation",
    "scope": "all",
    "reinstatement": false
  },
  "schema": "revoke",
  "timestamp": "2026-03-31T00:00:00Z"
}
```

→ Reject the request.

### Step 2 — Handle both outcomes

```python
import httpx

resp = httpx.get(
    "https://api.dedi.global/dedi/lookup/example.org/revoke/entity-abc",
    timeout=5.0
)

if resp.status_code == 404:
    # No revocation record found — entity is not revoked
    pass  # continue with downstream logic
elif resp.status_code == 200:
    record = resp.json()["data"]
    raise PermissionError(
        f"Entity revoked at {record['revokedAt']} — reason: {record.get('reason', 'unspecified')}"
    )
else:
    # Treat lookup failures conservatively
    raise RuntimeError(f"Revocation check failed with status {resp.status_code}")
```

---

## Flow 3: Membership validation

**Scenario.** Confirm that `member-001` holds an active membership before granting access.

### Step 1 — Look up the membership record

```bash
curl -s "https://api.dedi.global/dedi/lookup/example.org/membership/member-001"
```

Response:
```json
{
  "message": "ok",
  "data": {
    "membership_id": "member-001",
    "status": "active",
    "issuer": "org.example.membership-authority",
    "detail": {
      "name": "Alice Example",
      "url": "https://example.org/members/alice"
    },
    "evidence": "https://example.org/evidence/member-001",
    "memberSince": "2024-01-01",
    "memberTill": "2026-12-31"
  },
  "schema": "membership",
  "timestamp": "2026-03-31T00:00:00Z"
}
```

### Step 2 — Validate and apply policy

```python
from datetime import date

data = response["data"]
today = date.today()

assert data["status"] == "active", f"Membership is not active: {data['status']}"
assert date.fromisoformat(data["memberSince"]) <= today, "Membership start date is in the future"
assert date.fromisoformat(data["memberTill"]) >= today,  "Membership has expired"
```

---

## Flow 4: Historical key lookup for audit

**Scenario.** During an audit, verify which key was active on 2025-06-01.

```bash
curl -s "https://api.dedi.global/dedi/lookup/example.org/public-key/did:example:merchant-123?as_on=2025-06-01T00:00:00Z"
```

And to list all available historical versions:

```bash
curl -s "https://api.dedi.global/dedi/versions/example.org/public-key/did:example:merchant-123"
```

Response:
```json
{
  "message": "ok",
  "data": {
    "versions": [
      { "version_id": "v1", "created_at": "2024-01-01T00:00:00Z" },
      { "version_id": "v2", "created_at": "2025-01-15T00:00:00Z" },
      { "version_id": "v3", "created_at": "2026-03-01T00:00:00Z" }
    ]
  },
  "timestamp": "2026-03-31T00:00:00Z"
}
```

---

## Related

- [Quickstart](../../docs/getting-started/quickstart.md)
- [Build with DeDi](../../docs/build-with-dedi.md)
- [Verifier guide](../../docs/verifier-guide.md)
- [Discovery conventions](../../docs/discovery.md)
