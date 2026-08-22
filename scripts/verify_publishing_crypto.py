from __future__ import annotations

import base64
import copy
import hashlib
import json
from pathlib import Path

import rfc8785
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

ROOT = Path(__file__).resolve().parents[1]
VECTORS = ROOT / "conformance/vectors/publishing"


def b64url_decode(value: str) -> bytes:
    padding = "=" * (-len(value) % 4)
    return base64.urlsafe_b64decode(value + padding)


def verify_detached_jws(document: dict, jwk: dict) -> None:
    proof = document.get("proof") or {}
    jws = proof.get("jws", "")
    parts = jws.split(".")
    if len(parts) != 3 or parts[1] != "":
        raise ValueError("proof.jws must be a detached compact JWS")

    protected_b64, _, signature_b64 = parts
    protected = json.loads(b64url_decode(protected_b64))
    if protected != {"alg": "EdDSA", "b64": False, "crit": ["b64"]}:
        raise ValueError("unsupported protected JWS header")
    if proof.get("canonicalization") != "JCS":
        raise ValueError("proof must declare JCS canonicalization")
    if proof.get("verification_method") != jwk.get("kid"):
        raise ValueError("proof verification_method does not match key kid")
    if jwk.get("kty") != "OKP" or jwk.get("crv") != "Ed25519":
        raise ValueError("fixture verifier supports Ed25519 OKP keys only")

    unsigned = copy.deepcopy(document)
    unsigned.pop("proof", None)
    canonical = rfc8785.dumps(unsigned)
    signing_input = protected_b64.encode("ascii") + b"." + canonical

    public_key = Ed25519PublicKey.from_public_bytes(b64url_decode(jwk["x"]))
    public_key.verify(b64url_decode(signature_b64), signing_input)


def manifest_key(manifest: dict) -> dict:
    proof_key = manifest["proof"]["verification_method"]
    for key in manifest.get("keys", []):
        if key.get("kid") == proof_key:
            return key
    raise ValueError("manifest proof key is not currently declared")


def verify_file_against_manifest(file_obj: dict, manifest: dict) -> None:
    if file_obj["publisher"]["domain"] != manifest["domain"]:
        raise ValueError("publisher domain does not match manifest")

    file_key = file_obj["publisher"]["key"]
    declared = {key["kid"]: key for key in manifest.get("keys", [])}
    if file_key["kid"] not in declared:
        raise ValueError("file publisher key is no longer declared by manifest")
    if declared[file_key["kid"]] != file_key:
        raise ValueError("file publisher key material differs from manifest key")

    verify_detached_jws(file_obj, file_key)


def verify_digest(file_path: Path, manifest: dict, registry_name: str) -> None:
    entry = next((item for item in manifest["files"] if item.get("registry") == registry_name), None)
    if not entry:
        raise ValueError(f"manifest does not reference registry {registry_name}")
    algorithm, expected = entry["digest"].split(":", 1)
    if algorithm != "sha-256":
        raise ValueError("fixture verifier supports sha-256 digests only")
    actual = hashlib.sha256(file_path.read_bytes()).hexdigest()
    if actual != expected:
        raise ValueError("referenced file digest does not match manifest")


def expect_failure(label: str, func) -> None:
    try:
        func()
    except (ValueError, InvalidSignature):
        return
    raise SystemExit(f"Negative vector unexpectedly passed: {label}")


def main() -> None:
    manifest_path = VECTORS / "valid-manifest.json"
    file_path = VECTORS / "valid-file.json"
    manifest = json.loads(manifest_path.read_text())
    file_obj = json.loads(file_path.read_text())

    verify_detached_jws(manifest, manifest_key(manifest))
    verify_file_against_manifest(file_obj, manifest)
    verify_digest(file_path, manifest, "keys")

    tampered = json.loads((VECTORS / "tampered-file.json").read_text())
    expect_failure("tampered file signature", lambda: verify_file_against_manifest(tampered, manifest))

    removed_key_manifest = json.loads((VECTORS / "removed-key-manifest.json").read_text())
    expect_failure("removed manifest proof key", lambda: verify_detached_jws(removed_key_manifest, manifest_key(removed_key_manifest)))
    expect_failure("file signed by removed key", lambda: verify_file_against_manifest(file_obj, removed_key_manifest))

    altered_bytes = file_path.read_bytes() + b" "
    expected = manifest["files"][0]["digest"].split(":", 1)[1]
    if hashlib.sha256(altered_bytes).hexdigest() == expected:
        raise SystemExit("Digest tamper vector unexpectedly matched")

    print("Cryptographic publishing verification passed.")


if __name__ == "__main__":
    main()
