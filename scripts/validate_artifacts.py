from pathlib import Path
import json

from jsonschema import Draft7Validator
from openapi_spec_validator import validate_spec
import yaml

ROOT = Path(__file__).resolve().parents[1]

SCHEMA_FILES = {
    'public-key': ROOT / 'schemas/public_key.json',
    'membership': ROOT / 'schemas/membership.json',
    'revoke': ROOT / 'schemas/revoke.json',
    'beckn-subscriber': ROOT / 'schemas/Beckn_subscriber.json',
    'beckn-subscriber-reference': ROOT / 'schemas/Beckn_subscriber_reference.json',
    'endpoint': ROOT / 'schemas/endpoint.json',
}

EXAMPLE_MAP = {
    'public-key': ROOT / 'examples/public-key',
    'membership': ROOT / 'examples/membership',
    'revoke': ROOT / 'examples/revoke',
    'beckn-subscriber': ROOT / 'examples/beckn-subscriber',
    'beckn-subscriber-reference': ROOT / 'examples/beckn-subscriber-reference',
    'endpoint': ROOT / 'examples/endpoint',
}


def validate_examples():
    for key, schema_path in SCHEMA_FILES.items():
        schema = json.loads(schema_path.read_text())
        validator = Draft7Validator(schema)
        valid_obj = json.loads((EXAMPLE_MAP[key] / 'sample.json').read_text())
        errs = sorted(validator.iter_errors(valid_obj), key=lambda e: e.path)
        if errs:
            raise SystemExit(f'Valid example failed for {key}: {errs[0].message}')

        invalid_obj = json.loads((EXAMPLE_MAP[key] / 'invalid.json').read_text())
        errs = sorted(validator.iter_errors(invalid_obj), key=lambda e: e.path)
        if not errs:
            raise SystemExit(f'Invalid example unexpectedly passed for {key}')


def validate_openapi():
    spec = yaml.safe_load((ROOT / 'api/openapi.yaml').read_text())
    validate_spec(spec)


def validate_yaml_tree(path: Path, label: str):
    for item in sorted(path.rglob('*.yaml')):
        try:
            yaml.safe_load(item.read_text())
        except Exception as exc:  # pragma: no cover - narrow parsing failures at runtime
            raise SystemExit(f'Failed to parse {label} YAML {item.relative_to(ROOT)}: {exc}') from exc


def validate_json_files(paths, label: str):
    for item in paths:
        try:
            json.loads(item.read_text())
        except Exception as exc:
            raise SystemExit(f'Failed to parse {label} JSON {item.relative_to(ROOT)}: {exc}') from exc


def validate_conformance_vectors():
    public_key_schema = json.loads((ROOT / 'schemas/public_key.json').read_text())
    revoke_schema = json.loads((ROOT / 'schemas/revoke.json').read_text())

    pairs = [
        (public_key_schema, ROOT / 'conformance/vectors/valid/public-key.json', True),
        (public_key_schema, ROOT / 'conformance/vectors/invalid/public-key.json', False),
        (revoke_schema, ROOT / 'conformance/vectors/valid/revoke.json', True),
        (revoke_schema, ROOT / 'conformance/vectors/invalid/revoke.json', False),
    ]

    for schema, path, should_pass in pairs:
        validator = Draft7Validator(schema)
        obj = json.loads(path.read_text())
        errs = sorted(validator.iter_errors(obj), key=lambda e: e.path)
        passed = not errs
        if passed != should_pass:
            expectation = 'pass' if should_pass else 'fail'
            raise SystemExit(f'Conformance vector {path.relative_to(ROOT)} did not {expectation} as expected')


def validate_governance_schema():
    schema = json.loads((ROOT / 'governance/delegation-schema.json').read_text())
    Draft7Validator.check_schema(schema)


def validate_required_paths():
    required = [
        ROOT / '.github/workflows/validate.yml',
        ROOT / 'reference-impl/server/server.py',
        ROOT / 'reference-impl/client/client.py',
        ROOT / 'examples/minimal-node/sample-response.json',
        ROOT / 'spec/v0.1/README.md',
        ROOT / 'conformance/profiles/base.yaml',
        ROOT / 'conformance/profiles/secure.yaml',
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
    if missing:
        raise SystemExit(f'Missing required files: {missing}')


def main():
    validate_required_paths()
    validate_examples()
    validate_openapi()
    validate_yaml_tree(ROOT / 'conformance/profiles', 'conformance profile')
    validate_yaml_tree(ROOT / 'conformance/tests', 'conformance test')
    validate_conformance_vectors()
    validate_governance_schema()
    validate_json_files(sorted((ROOT / 'evidence').glob('*.json')), 'evidence artifact')
    print('All validations passed.')


if __name__ == '__main__':
    main()
