#!/usr/bin/env python3
"""
DeDi reference client

A minimal, self-contained example of how to discover, query, look up, and
validate records from a DeDi-compatible registry.

Usage:
    # Discover registries in a namespace
    python scripts/client_demo.py discover example.org

    # Query all records in a registry
    python scripts/client_demo.py query example.org public-key

    # Look up a specific record
    python scripts/client_demo.py lookup example.org public-key did:example:merchant-123

    # Check revocation status
    python scripts/client_demo.py revoke example.org entity-abc

    # Validate a local JSON payload against a schema
    python scripts/client_demo.py validate public_key examples/public-key/sample.json
"""

import argparse
import json
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #

BASE_URL = "https://api.dedi.global"
SCHEMA_DIR = Path(__file__).resolve().parent.parent / "schemas"

# --------------------------------------------------------------------------- #
# HTTP helpers
# --------------------------------------------------------------------------- #


def _get(url: str) -> dict:
    """Fetch a URL and return the parsed JSON body, or print an error and exit."""
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8")
        try:
            err = json.loads(body)
            code = err.get("code", exc.code)
            msg = err.get("message", "no message")
            _die(f"HTTP {exc.code} {code}: {msg}")
        except json.JSONDecodeError:
            _die(f"HTTP {exc.code}: {body[:200]}")
    except urllib.error.URLError as exc:
        _die(f"Network error: {exc.reason}")


def _die(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


# --------------------------------------------------------------------------- #
# Schema validation helper
# --------------------------------------------------------------------------- #


def _validate_payload(schema_name: str, payload: dict) -> list:
    """Return a list of validation errors. Empty list means valid."""
    try:
        from jsonschema import Draft7Validator
    except ImportError:
        _die("jsonschema not installed. Run: pip install jsonschema")

    schema_path = SCHEMA_DIR / f"{schema_name}.json"
    if not schema_path.exists():
        _die(f"Schema not found: {schema_path}")

    schema = json.loads(schema_path.read_text())
    validator = Draft7Validator(schema)
    return sorted(validator.iter_errors(payload), key=lambda e: e.path)


# --------------------------------------------------------------------------- #
# Commands
# --------------------------------------------------------------------------- #


def cmd_discover(namespace: str) -> None:
    """Query a namespace and list its registries."""
    url = f"{BASE_URL}/dedi/query/{namespace}"
    print(f"→ GET {url}\n")
    result = _get(url)
    print(json.dumps(result, indent=2))

    data = result.get("data", {})
    registries = data.get("registries", [])
    if registries:
        print(f"\nFound {len(registries)} registry/registries in namespace '{namespace}':")
        for reg in registries:
            print(f"  • {reg.get('name', '?')}  (schema: {reg.get('schema', '?')})")
    else:
        print(f"\nNo registries listed in namespace '{namespace}'.")


def cmd_query(namespace: str, registry: str, page: int = 1, page_size: int = 20) -> None:
    """List records in a registry."""
    url = f"{BASE_URL}/dedi/query/{namespace}/{registry}?page={page}&page_size={page_size}"
    print(f"→ GET {url}\n")
    result = _get(url)
    print(json.dumps(result, indent=2))


def cmd_lookup(namespace: str, registry: str, record_id: str, as_on: str | None = None) -> None:
    """Fetch and validate a specific record."""
    url = f"{BASE_URL}/dedi/lookup/{namespace}/{registry}/{record_id}"
    if as_on:
        url += f"?as_on={as_on}"

    print(f"→ GET {url}\n")
    result = _get(url)
    print(json.dumps(result, indent=2))

    # Validate the payload against its declared schema
    schema_name = result.get("schema")
    if schema_name:
        payload = result.get("data", {})
        errors = _validate_payload(schema_name, payload)
        if errors:
            print(f"\n⚠  Schema validation FAILED ({len(errors)} error(s)):")
            for err in errors[:5]:
                path = " > ".join(str(p) for p in err.absolute_path) or "(root)"
                print(f"   [{path}] {err.message}")
        else:
            print(f"\n✓  Payload valid against schema '{schema_name}'")

        # Basic freshness check
        ts_str = result.get("timestamp")
        if ts_str:
            record_ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
            age_s = (datetime.now(timezone.utc) - record_ts).total_seconds()
            if age_s > 86400:
                print(f"⚠  Record timestamp is {age_s / 3600:.1f} hours old — consider re-fetching")
            else:
                print(f"✓  Record freshness OK ({age_s:.0f}s old)")
    else:
        print("\n(No 'schema' field in response — skipping validation)")


def cmd_revoke(namespace: str, entity_id: str) -> None:
    """Check whether an entity is revoked."""
    url = f"{BASE_URL}/dedi/lookup/{namespace}/revoke/{entity_id}"
    print(f"→ GET {url}\n")
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            body = resp.read().decode("utf-8")
            result = json.loads(body)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            print(f"✓  No revocation record found for '{entity_id}' — entity is not revoked.")
            return
        body = exc.read().decode("utf-8")
        _die(f"HTTP {exc.code}: {body[:200]}")
    except urllib.error.URLError as exc:
        _die(f"Network error: {exc.reason}")

    data = result.get("data", {})
    print(f"⛔  '{entity_id}' IS REVOKED")
    print(f"    Revoked at : {data.get('revokedAt', 'unknown')}")
    print(f"    Reason     : {data.get('reason', 'unspecified')}")
    print(f"    Scope      : {data.get('scope', 'unspecified')}")
    print(f"    Issuer     : {data.get('issuer', 'unspecified')}")
    reinstate = data.get("reinstatement", None)
    if reinstate is not None:
        print(f"    Reinstate? : {'yes' if reinstate else 'no'}")


def cmd_validate(schema_name: str, file_path: str) -> None:
    """Validate a local JSON file against a DeDi schema."""
    path = Path(file_path)
    if not path.exists():
        _die(f"File not found: {file_path}")

    payload = json.loads(path.read_text())
    errors = _validate_payload(schema_name, payload)

    if errors:
        print(f"✗  Validation FAILED against schema '{schema_name}' ({len(errors)} error(s)):")
        for err in errors:
            path_str = " > ".join(str(p) for p in err.absolute_path) or "(root)"
            print(f"   [{path_str}] {err.message}")
        sys.exit(1)
    else:
        print(f"✓  '{file_path}' is valid against schema '{schema_name}'")


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def main() -> None:
    parser = argparse.ArgumentParser(
        description="DeDi reference client — discover, query, look up, and validate DeDi records.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_discover = sub.add_parser("discover", help="List registries in a namespace")
    p_discover.add_argument("namespace", help="e.g. example.org")

    p_query = sub.add_parser("query", help="List records in a registry")
    p_query.add_argument("namespace")
    p_query.add_argument("registry", help="e.g. public-key")
    p_query.add_argument("--page", type=int, default=1)
    p_query.add_argument("--page-size", type=int, default=20, dest="page_size")

    p_lookup = sub.add_parser("lookup", help="Fetch and validate a specific record")
    p_lookup.add_argument("namespace")
    p_lookup.add_argument("registry")
    p_lookup.add_argument("record_id")
    p_lookup.add_argument("--as-on", dest="as_on", help="ISO datetime for historical lookup")

    p_revoke = sub.add_parser("revoke", help="Check revocation status of an entity")
    p_revoke.add_argument("namespace")
    p_revoke.add_argument("entity_id")

    p_validate = sub.add_parser("validate", help="Validate a local JSON file against a schema")
    p_validate.add_argument("schema_name", help="Schema name, e.g. public_key")
    p_validate.add_argument("file_path", help="Path to the JSON file")

    args = parser.parse_args()

    if args.command == "discover":
        cmd_discover(args.namespace)
    elif args.command == "query":
        cmd_query(args.namespace, args.registry, args.page, args.page_size)
    elif args.command == "lookup":
        cmd_lookup(args.namespace, args.registry, args.record_id, args.as_on)
    elif args.command == "revoke":
        cmd_revoke(args.namespace, args.entity_id)
    elif args.command == "validate":
        cmd_validate(args.schema_name, args.file_path)


if __name__ == "__main__":
    main()
