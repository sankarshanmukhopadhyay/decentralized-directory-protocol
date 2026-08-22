from __future__ import annotations

from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys

from jsonschema import Draft7Validator
import yaml

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "conformance/profiles/publishing.yaml"
SCHEMA = ROOT / "schemas/conformance-evidence.schema.json"
OUTPUT = ROOT / "evidence/conformance-run.json"
UPSTREAM_REF = "72d913fb4d17507891a6fea5db1f49ef7b3f461d"

STEPS = [
    ("artifact-validation", [sys.executable, "scripts/validate_artifacts.py"]),
    ("publishing-cryptography", [sys.executable, "scripts/verify_publishing_crypto.py"]),
    ("publishing-lifecycle", [sys.executable, "scripts/verify_publishing_lifecycle.py"]),
    ("publisher-indexer-verifier", [sys.executable, "scripts/run_publishing_scenario.py"]),
]


def repository_ref() -> str:
    env_ref = os.environ.get("GITHUB_SHA")
    if env_ref:
        return env_ref
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        ).strip()
    except Exception:
        return "local-working-tree"


def profile_checks() -> list[str]:
    profile = yaml.safe_load(PROFILE.read_text())
    return [item["id"] for item in profile.get("checks", [])]


def run_step(name: str, command: list[str]) -> dict:
    proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    return {
        "name": name,
        "command": " ".join(command),
        "status": "pass" if proc.returncode == 0 else "fail",
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
    }


def main() -> None:
    steps = []
    for name, command in STEPS:
        step = run_step(name, command)
        steps.append(step)
        print(f"{step['status'].upper()} {name}")
        if step["status"] == "fail":
            break

    status = "pass" if len(steps) == len(STEPS) and all(s["status"] == "pass" for s in steps) else "fail"
    evidence = {
        "artifact": "fork-local-conformance-run",
        "profile": "publishing",
        "status": status,
        "normative": False,
        "upstream_ref": UPSTREAM_REF,
        "repository_ref": repository_ref(),
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "checks": profile_checks(),
        "steps": steps,
    }

    OUTPUT.write_text(json.dumps(evidence, indent=2) + "\n")

    schema = json.loads(SCHEMA.read_text())
    errors = sorted(Draft7Validator(schema).iter_errors(evidence), key=lambda e: list(e.path))
    if errors:
        raise SystemExit(f"Generated conformance evidence failed schema validation: {errors[0].message}")
    if status != "pass":
        failed = next(step for step in steps if step["status"] == "fail")
        raise SystemExit(
            f"Conformance run failed at {failed['name']}: {failed['stderr'] or failed['stdout']}"
        )

    print(f"Conformance run passed with {len(evidence['checks'])} profile checks.")
    print(f"Evidence: {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
