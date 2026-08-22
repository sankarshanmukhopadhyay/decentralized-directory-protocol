from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path

from verify_publishing_crypto import manifest_key, verify_detached_jws, verify_file_against_manifest

ROOT = Path(__file__).resolve().parents[1]
VECTORS = ROOT / "conformance/vectors/publishing"
EVIDENCE = ROOT / "evidence/publisher-indexer-verifier.json"


def parse_ts(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def assert_fresh(document: dict, now: datetime, label: str) -> None:
    if parse_ts(document["next_update"]) <= now:
        raise ValueError(f"{label} is stale")


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

    return {
        "artifact": "fork-local-scenario-evidence",
        "scenario": "publisher-indexer-verifier",
        "evaluation_time": now.isoformat().replace("+00:00", "Z"),
        "upstream_ref": "72d913fb4d17507891a6fea5db1f49ef7b3f461d",
        "normative": False,
        "status": "pass",
        "steps": steps,
    }


def main() -> None:
    evidence = run()
    EVIDENCE.write_text(json.dumps(evidence, indent=2) + "\n")
    print("Publisher -> indexer -> verifier scenario passed.")
    print(f"Evidence: {EVIDENCE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
