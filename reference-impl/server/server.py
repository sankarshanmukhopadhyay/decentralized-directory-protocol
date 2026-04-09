from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

PUBLIC_KEY_RECORD = {
    "public_key_id": "did:example:merchant-123",
    "publicKey": "-----BEGIN PUBLIC KEY-----MIIB...-----END PUBLIC KEY-----",
    "keyType": "Ed25519",
    "keyFormat": "PEM",
    "activatedAt": "2026-03-01T00:00:00Z",
    "entity": {
        "name": "Merchant One",
        "url": "https://merchant.example.org",
        "address": "Kolkata, India"
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
}

class Handler(BaseHTTPRequestHandler):
    def _send_json(self, payload, status=200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        if path == "/health":
            return self._send_json({"status": "ok"})
        if path == "/dedi/query/example.org":
            params = parse_qs(parsed.query)
            page = params.get("page", ["1"])[0]
            page_size = params.get("page_size", ["20"])[0]
            return self._send_json({
                "namespace": "example.org",
                "record_type": "public-key",
                "page": int(page),
                "page_size": int(page_size),
                "items": [PUBLIC_KEY_RECORD]
            })
        if path == "/dedi/lookup/example.org/public-key/did:example:merchant-123":
            return self._send_json(PUBLIC_KEY_RECORD)
        return self._send_json({"error": "not_found", "path": path}, status=404)

if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8080), Handler)
    print("DeDi reference server listening on http://127.0.0.1:8080")
    server.serve_forever()
