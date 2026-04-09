from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from urllib.request import urlopen

from jsonschema import Draft7Validator

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "http://127.0.0.1:8080"
EVIDENCE_PATH = ROOT / "evidence" / "quickstart-run.json"


def fetch_json(path: str):
    with urlopen(f"{BASE_URL}{path}") as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    query_result = fetch_json("/dedi/query/example.org?page=1&page_size=20")
    lookup_result = fetch_json("/dedi/lookup/example.org/public-key/did:example:merchant-123")

    schema = json.loads((ROOT / "schemas" / "public_key.json").read_text())
    validator = Draft7Validator(schema)
    errors = sorted(validator.iter_errors(lookup_result), key=lambda e: e.path)
    if errors:
        raise SystemExit(f"Lookup result failed validation: {errors[0].message}")

    payload_hash = hashlib.sha256(json.dumps(lookup_result, sort_keys=True).encode("utf-8")).hexdigest()
    evidence = {
        "test_id": "DDP-QS-001",
        "query_path": "/dedi/query/example.org?page=1&page_size=20",
        "lookup_path": "/dedi/lookup/example.org/public-key/did:example:merchant-123",
        "query_items": len(query_result.get("items", [])),
        "lookup_id": lookup_result["public_key_id"],
        "output_hash": payload_hash,
        "validation": "PASS",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    EVIDENCE_PATH.write_text(json.dumps(evidence, indent=2))
    print(json.dumps(evidence, indent=2))


if __name__ == "__main__":
    main()
