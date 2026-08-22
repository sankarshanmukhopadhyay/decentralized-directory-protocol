from datetime import datetime, timezone
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
VECTOR = ROOT / 'conformance/vectors/publishing/lifecycle.json'


def parse_ts(value: str) -> datetime:
    return datetime.fromisoformat(value.replace('Z', '+00:00')).astimezone(timezone.utc)


def evaluate(case, now):
    kind = case['kind']

    if kind in {'manifest', 'file'}:
        if parse_ts(case['next_update']) <= now:
            return 'reject-stale'
        if kind == 'file' and case.get('registry_state') != 'live':
            return 'reject-inactive'
        return 'accept'

    if kind == 'manifest-sequence':
        observed = parse_ts(case['observed_updated_at'])
        candidate = parse_ts(case['candidate_updated_at'])
        return 'reject-rollback' if candidate < observed else 'accept'

    if kind == 'key-state':
        current = set(case['current_keys'])
        file_key = case['file_key']
        return 'accept' if file_key in current else 'reject-removed-key'

    if kind == 'refresh':
        if case['refresh_succeeded']:
            return 'accept'
        cached_expiry = parse_ts(case['cached_next_update'])
        return 'accept-cached' if cached_expiry > now else 'reject-unavailable-authority'

    raise ValueError(f"Unsupported lifecycle vector kind: {kind}")


def main():
    vector = json.loads(VECTOR.read_text())
    now = parse_ts(vector['evaluation_time'])
    failures = []

    for case in vector['cases']:
        actual = evaluate(case, now)
        expected = case['expected']
        if actual != expected:
            failures.append(f"{case['id']}: expected {expected}, got {actual}")
        else:
            print(f"PASS {case['id']}: {actual}")

    if failures:
        raise SystemExit('Lifecycle verification failed: ' + '; '.join(failures))

    print(f"Publishing lifecycle verification passed ({len(vector['cases'])} cases).")


if __name__ == '__main__':
    main()
