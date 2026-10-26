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
UPSTREAM_REF = "4804d835d2d0109781536b629133a592d0a08590"

STEPS = [
    ("artifact-validation", [sys.executable, "scripts/validate_artifacts.py"]),
    ("publishing-cryptography", [sys.executable, "scripts/verify_publishing_crypto.py"]),
    ("publishing-lifecycle", [sys.executable, "scripts/verify_publishing_lifecycle.py"]),
    ("publisher-indexer-verifier", [sys.executable, "scripts/run_publishing_scenario.py"]),
    ("signed-digests-regressions", [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_signed_digests.py", "-v"]),
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


CHECK_BINDINGS = {
    "PUB-020": ("signed-digests-regressions", "test_external_precedence_over_conflicting_inline"),
    "PUB-021": ("signed-digests-regressions", "test_uncommitted_is_not_verified"),
    "PUB-022": ("signed-digests-regressions", "test_wrong_domain_and_removed_key_rejected"),
    "PUB-023": ("signed-digests-regressions", "test_expired_document_rejected"),
    "PUB-024": ("publishing-lifecycle", "digests-rollback"),
    "PUB-025": ("signed-digests-regressions", "test_refresh_resolves_mismatch"),
    "PUB-026": ("signed-digests-regressions", "test_refresh_persistent_mismatch_rejected"),
    "PUB-027": ("publisher-indexer-verifier", "resolve-signed-digest-index"),
}


def check_evidence(check_ids: list[str], steps: list[dict]) -> list[dict]:
    """Do not promote a suite PASS into unrelated individual conformance claims."""
    by_name = {step["name"]: step for step in steps}
    results = []
    for check_id in check_ids:
        binding = CHECK_BINDINGS.get(check_id)
        if binding is None:
            results.append({"id": check_id, "state": "not-individually-attributed"})
            continue
        name, token = binding
        step = by_name.get(name)
        if step is None:
            results.append({"id": check_id, "state": "not-run", "step": name})
        else:
            output = step.get("stdout", "") + "\\n" + step.get("stderr", "")
            passed = step["status"] == "pass" and token in output
            results.append({"id": check_id,
                            "state": "verified" if passed else "unverified",
                            "step": name, "test_identifier": token})
    return results


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
        "check_evidence": check_evidence(profile_checks(), steps),
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
