"""Fork-local regression tests for signed digest authority and commitment selection."""
import base64
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import unittest

import rfc8785
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from verify_publishing_crypto import (
    check_digest_bytes, select_digest, verify_digest_with_refresh,
    verify_digests_document,
)


def enc(data):
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def signed(document, private):
    result = copy.deepcopy(document)
    result["proof"] = {"verification_method": "publisher-1", "canonicalization": "JCS"}
    header = enc(b'{"alg":"EdDSA","b64":false,"crit":["b64"]}')
    signature = private.sign(header.encode() + b"." + rfc8785.dumps({k: v for k, v in result.items() if k != "proof"}))
    result["proof"]["jws"] = header + ".." + enc(signature)
    return result


class SignedDigestsContract(unittest.TestCase):
    def setUp(self):
        self.private = Ed25519PrivateKey.from_private_bytes(bytes(range(32)))
        public = self.private.public_key().public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw,
        )
        self.manifest = {
            "domain": "example.org",
            "keys": [{"kid": "publisher-1", "kty": "OKP", "crv": "Ed25519", "x": enc(public)}],
        }
        self.entry = {"registry": "keys", "digest": "sha-256:" + "0" * 64}
        self.content = b"payload"
        self.digest = "sha-256:" + hashlib.sha256(self.content).hexdigest()
        self.now = datetime(2026, 10, 26, tzinfo=timezone.utc)

    def document(self, *, digest=None, domain="example.org", expiry="2026-11-01T00:00:00Z"):
        return signed({
            "domain": domain, "dedi_version": "0.1", "type": "dedi-digests",
            "updated_at": "2026-10-20T00:00:00Z",
            "next_update": expiry, "digests": {"keys": digest or self.digest},
        }, self.private)

    def test_external_precedence_over_conflicting_inline(self):
        doc = self.document()
        self.assertEqual(verify_digest_with_refresh(
            self.content, self.entry, self.manifest, doc, now=self.now),
            ("verified", "external-digests-document"))

    def test_declared_external_source_must_be_resolved(self):
        manifest = dict(self.manifest, digests="https://example.org/dedi/dedi.digests.json")
        with self.assertRaisesRegex(ValueError, "no authenticated digest document"):
            verify_digest_with_refresh(
                self.content, self.entry, manifest, now=self.now)

    def test_inline_fallback(self):
        entry = {"registry": "keys", "digest": self.digest}
        self.assertEqual(verify_digest_with_refresh(
            self.content, entry, self.manifest, now=self.now),
            ("verified", "manifest-inline"))

    def test_uncommitted_is_not_verified(self):
        entry = {"registry": "keys"}
        self.assertEqual(verify_digest_with_refresh(
            self.content, entry, self.manifest, now=self.now),
            ("not-committed", "none"))

    def test_tampered_document_rejected(self):
        doc = self.document()
        doc["digests"]["keys"] = "sha-256:" + "1" * 64
        with self.assertRaises(Exception):
            verify_digests_document(doc, self.manifest)

    def test_wrong_domain_and_removed_key_rejected(self):
        with self.assertRaises(ValueError):
            verify_digests_document(self.document(domain="other.example"), self.manifest)
        with self.assertRaises(ValueError):
            verify_digests_document(self.document(), {"domain": "example.org", "keys": []})

    def test_expired_document_rejected(self):
        with self.assertRaisesRegex(ValueError, "stale"):
            verify_digest_with_refresh(self.content, self.entry, self.manifest,
                                       self.document(expiry="2026-10-01T00:00:00Z"), now=self.now)

    def test_refresh_resolves_mismatch(self):
        old = self.document(digest="sha-256:" + "a" * 64)
        new = self.document()
        self.assertEqual(verify_digest_with_refresh(
            self.content, self.entry, self.manifest, old,
            refresh=lambda: new, now=self.now)[0], "verified")

    def test_refresh_persistent_mismatch_rejected(self):
        old = self.document(digest="sha-256:" + "a" * 64)
        with self.assertRaisesRegex(ValueError, "mismatch"):
            verify_digest_with_refresh(self.content, self.entry, self.manifest,
                                       old, refresh=lambda: old, now=self.now)

    def test_refresh_tampered_or_unavailable_rejected(self):
        old = self.document(digest="sha-256:" + "a" * 64)
        with self.assertRaisesRegex(ValueError, "unavailable"):
            verify_digest_with_refresh(self.content, self.entry, self.manifest,
                                       old, refresh=lambda: None, now=self.now)
        tampered = self.document()
        tampered["digests"]["keys"] = "sha-256:" + "b" * 64
        with self.assertRaises(Exception):
            verify_digest_with_refresh(self.content, self.entry, self.manifest,
                                       old, refresh=lambda: tampered, now=self.now)

    def test_malformed_digest_rejected(self):
        with self.assertRaisesRegex(ValueError, "malformed"):
            check_digest_bytes(self.content, "sha-512:abcd")


if __name__ == "__main__":
    unittest.main()
