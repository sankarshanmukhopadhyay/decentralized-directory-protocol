from __future__ import annotations

from datetime import datetime, timezone
import base64
import copy
import hashlib
import json

import rfc8785
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization
from pathlib import Path

from verify_publishing_crypto import (manifest_key, verify_detached_jws,
    verify_file_against_manifest, verify_digest_with_refresh)

ROOT = Path(__file__).resolve().parents[1]
VECTORS = ROOT / "conformance/vectors/publishing"
EVIDENCE = ROOT / "evidence/publisher-indexer-verifier.json"


def parse_ts(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def assert_fresh(document: dict, now: datetime, label: str) -> None:
    if parse_ts(document["next_update"]) <= now:
        raise ValueError(f"{label} is stale")



def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def sign_document(document: dict, private: Ed25519PrivateKey, kid: str) -> dict:
    """Build deterministic offline signed vectors without private keys in source fixtures."""
    result = copy.deepcopy(document)
    result["proof"] = {"verification_method": kid, "canonicalization": "JCS"}
    protected = b64url(b'{"alg":"EdDSA","b64":false,"crit":["b64"]}')
    unsigned = {name: value for name, value in result.items() if name != "proof"}
    signature = private.sign(protected.encode() + b"." + rfc8785.dumps(unsigned))
    result["proof"]["jws"] = protected + ".." + b64url(signature)
    return result


def composed_digest_reliance(now: datetime) -> dict:
    """Exercise a publisher -> indexer -> verifier path with signed external digest authority."""
    private = Ed25519PrivateKey.from_private_bytes(bytes(range(32)))
    kid = "publisher-test-key"
    jwk = {
        "kid": kid, "kty": "OKP", "crv": "Ed25519",
        "x": b64url(private.public_key().public_bytes(
            encoding=serialization.Encoding.Raw, format=serialization.PublicFormat.Raw))
    }
    file_obj = json.loads((VECTORS / "valid-file.json").read_text())
    file_obj["publisher"]["key"] = jwk
    file_obj = sign_document(file_obj, private, kid)
    file_bytes = (json.dumps(file_obj, sort_keys=True, separators=(",", ":")) + "\n").encode()
    registry = file_obj["registry"]["name"]
    # A conflicting inline digest deliberately demonstrates external precedence.
    manifest = {
        "dedi_version": "0.1", "domain": file_obj["publisher"]["domain"],
        "keys": [jwk], "updated_at": "2026-08-22T05:00:00Z",
        "next_update": "2026-09-01T00:00:00Z",
        "digests": "https://example.org/dedi/dedi.digests.json",
        "files": [{"registry": registry, "url": file_obj["source_url"], "digest": "sha-256:" + "0" * 64}],
    }
    manifest = sign_document(manifest, private, kid)
    digest_doc = sign_document({
        "dedi_version": "0.1", "type": "dedi-digests",
        "domain": manifest["domain"], "updated_at": "2026-08-22T05:10:00Z",
        "next_update": "2026-08-25T00:00:00Z",
        "digests": {registry: "sha-256:" + hashlib.sha256(file_bytes).hexdigest()},
    }, private, kid)

    # Indexer establishes authorization, signatures, lifecycle and digest commitment.
    verify_detached_jws(manifest, manifest_key(manifest))
    assert_fresh(manifest, now, "manifest")
    verify_file_against_manifest(file_obj, manifest)
    assert_fresh(file_obj, now, "registry file")
    assert_fresh(digest_doc, now, "digests")
    status, source = verify_digest_with_refresh(
        file_bytes, manifest["files"][0], manifest, digest_doc, now=now)
    if (status, source) != ("verified", "external-digests-document"):
        raise ValueError("indexer did not establish external digest authority")
    if file_obj["registry"]["state"] != "live":
        raise ValueError("indexer refuses inactive registry")
    index = {
        "records": {record["record_name"]: record["details"] for record in file_obj["records"]},
        "publisher_domain": manifest["domain"], "registry": registry,
        "digest_source": source, "digest_status": status,
        "digest_commitment": digest_doc["digests"][registry],
        "manifest_updated_at": manifest["updated_at"],
        "digests_updated_at": digest_doc["updated_at"],
        "authority_next_update": min(manifest["next_update"], file_obj["next_update"],
                                     digest_doc["next_update"]),
    }
    if not index["records"]:
        raise ValueError("composed index has no records")
    if parse_ts(index["authority_next_update"]) <= now:
        raise ValueError("index was backed by stale authority")
    # A verifier must reject the same index after the earliest authority expires.
    after_digests_expiry = datetime(2026, 8, 26, tzinfo=timezone.utc)
    if parse_ts(index["authority_next_update"]) > after_digests_expiry:
        raise ValueError("verifier erroneously retained expired external authority")
    return {
        "role": "verifier", "action": "resolve-signed-digest-index",
        "result": "accepted-with-expiry-rejection",
        "record_count": len(index["records"]), "digest_provenance": {
            "publisher": index["publisher_domain"], "registry": index["registry"],
            "commitment_source": index["digest_source"],
            "commitment": index["digest_commitment"],
            "state": index["digest_status"],
            "manifest_updated_at": index["manifest_updated_at"],
            "digests_updated_at": index["digests_updated_at"],
            "effective_authority_next_update": index["authority_next_update"],
        }
    }


def run() -> dict:
    now = datetime(2026, 8, 22, 6, 30, tzinfo=timezone.utc)
    manifest = json.loads((VECTORS / "valid-manifest.json").read_text())
    file_obj = json.loads((VECTORS / "valid-file.json").read_text())

    steps = []

    # Publisher: produce signed authority and registry state.
    steps.append({
        "role": "publisher",
        "action": "publish",
        "result": "manifest-and-registry-available",
        "domain": manifest["domain"],
        "registry": file_obj["registry"]["name"],
    })

    # Indexer: establish that the publisher's authority and registry artifact are acceptable.
    verify_detached_jws(manifest, manifest_key(manifest))
    assert_fresh(manifest, now, "manifest")
    verify_file_against_manifest(file_obj, manifest)
    assert_fresh(file_obj, now, "registry file")
    if file_obj["registry"]["state"] != "live":
        raise ValueError("indexer refuses inactive registry")

    index = {
        "namespace": file_obj["namespace"],
        "registry": file_obj["registry"]["name"],
        "records": {record["record_name"]: record["details"] for record in file_obj["records"]},
        "authority_updated_at": manifest["updated_at"],
        "authority_next_update": manifest["next_update"],
        "source_url": file_obj["source_url"],
    }
    steps.append({
        "role": "indexer",
        "action": "verify-and-index",
        "result": "accepted",
        "record_count": len(index["records"]),
    })

    # Verifier: resolve a named record only from index state backed by current authority.
    record_name = "service-a"
    record = index["records"].get(record_name)
    if record is None:
        raise ValueError("verifier could not resolve requested record")
    if parse_ts(index["authority_next_update"]) <= now:
        raise ValueError("verifier refuses index backed by stale authority")

    steps.append({
        "role": "verifier",
        "action": "resolve-and-rely",
        "result": "accepted",
        "record_name": record_name,
        "details": record,
    })

    # Negative path: a verifier must not rely on an index once its authority horizon is exceeded.
    future = datetime(2026, 9, 2, 0, 0, tzinfo=timezone.utc)
    stale_rejected = parse_ts(index["authority_next_update"]) <= future
    if not stale_rejected:
        raise ValueError("stale authority negative path unexpectedly remained acceptable")
    steps.append({
        "role": "verifier",
        "action": "resolve-after-authority-expiry",
        "result": "rejected-stale-authority",
    })

    steps.append(composed_digest_reliance(now))

    return {
        "artifact": "fork-local-scenario-evidence",
        "scenario": "publisher-indexer-verifier",
        "evaluation_time": now.isoformat().replace("+00:00", "Z"),
        "upstream_ref": "4804d835d2d0109781536b629133a592d0a08590",
        "normative": False,
        "status": "pass",
        "steps": steps,
    }


def main() -> None:
    evidence = run()
    EVIDENCE.write_text(json.dumps(evidence, indent=2) + "\n")
    print("Publisher -> indexer -> verifier scenario passed.")
    for step in evidence["steps"]:
        print("SCENARIO " + step["action"] + ": " + step["result"])
    print(f"Evidence: {EVIDENCE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
