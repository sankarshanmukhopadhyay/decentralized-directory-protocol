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


def load_json(path: Path):
    return json.loads(path.read_text())


def schema_errors(schema, obj):
    validator = Draft7Validator(schema)
    return sorted(validator.iter_errors(obj), key=lambda e: list(e.path))


def validate_examples():
    for key, schema_path in SCHEMA_FILES.items():
        schema = load_json(schema_path)
        validator = Draft7Validator(schema)
        valid_obj = load_json(EXAMPLE_MAP[key] / 'sample.json')
        errs = sorted(validator.iter_errors(valid_obj), key=lambda e: e.path)
        if errs:
            raise SystemExit(f'Valid example failed for {key}: {errs[0].message}')

        invalid_obj = load_json(EXAMPLE_MAP[key] / 'invalid.json')
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
    public_key_schema = load_json(ROOT / 'schemas/public_key.json')
    revoke_schema = load_json(ROOT / 'schemas/revoke.json')

    pairs = [
        (public_key_schema, ROOT / 'conformance/vectors/valid/public-key.json', True),
        (public_key_schema, ROOT / 'conformance/vectors/invalid/public-key.json', False),
        (revoke_schema, ROOT / 'conformance/vectors/valid/revoke.json', True),
        (revoke_schema, ROOT / 'conformance/vectors/invalid/revoke.json', False),
    ]

    for schema, path, should_pass in pairs:
        validator = Draft7Validator(schema)
        obj = load_json(path)
        errs = sorted(validator.iter_errors(obj), key=lambda e: e.path)
        passed = not errs
        if passed != should_pass:
            expectation = 'pass' if should_pass else 'fail'
            raise SystemExit(f'Conformance vector {path.relative_to(ROOT)} did not {expectation} as expected')


def validate_governance_schema():
    schema = load_json(ROOT / 'governance/delegation-schema.json')
    Draft7Validator.check_schema(schema)


def validate_dedi_file(file_obj, manifest_key_ids, expected_domain, label):
    schema = load_json(ROOT / 'schemas/dedi-file.schema.json')
    errs = schema_errors(schema, file_obj)
    if errs:
        raise SystemExit(f'{label} failed DeDi file schema validation: {errs[0].message}')

    publisher = file_obj['publisher']
    publisher_key_id = publisher['key']['kid']
    proof_key_id = file_obj['proof']['verification_method']

    if publisher['domain'] != expected_domain:
        raise SystemExit(f'{label} publisher domain does not match manifest domain')
    if publisher_key_id not in manifest_key_ids:
        raise SystemExit(f'{label} publisher key is not declared by the manifest')
    if proof_key_id != publisher_key_id:
        raise SystemExit(f'{label} proof verification_method does not match publisher key kid')

    record_names = [record['record_name'] for record in file_obj['records']]
    if len(record_names) != len(set(record_names)):
        raise SystemExit(f'{label} contains duplicate record_name values')


def validate_publishing_model():
    """Validate fork-local executable invariants for the synchronized upstream publishing model.

    This is intentionally narrower than cryptographic conformance: example JWS values are illustrative.
    The checks exercise document shape and cross-artifact relationships that can be verified without a
    signing key or network access.
    """
    manifest_path = ROOT / 'examples/dedi.index.json'
    manifest = load_json(manifest_path)

    required_manifest_fields = {
        'dedi_version', 'domain', 'keys', 'updated_at', 'next_update', 'files', 'proof'
    }
    missing = required_manifest_fields - set(manifest)
    if missing:
        raise SystemExit(f'Publishing manifest missing required fields: {sorted(missing)}')
    if manifest.get('type') not in (None, 'dedi-manifest'):
        raise SystemExit('Publishing manifest has an invalid type discriminator')
    if not manifest['keys']:
        raise SystemExit('Publishing manifest must declare at least one key')

    manifest_key_ids = [key['kid'] for key in manifest['keys']]
    if len(manifest_key_ids) != len(set(manifest_key_ids)):
        raise SystemExit('Publishing manifest contains duplicate key ids')
    if manifest['proof']['verification_method'] not in manifest_key_ids:
        raise SystemExit('Publishing manifest proof does not reference a declared key')
    if manifest['proof'].get('canonicalization') != 'JCS':
        raise SystemExit('Publishing manifest proof must declare JCS canonicalization')

    registry_names = []
    referenced_registries = {}
    inline_files = []

    for entry in manifest['files']:
        if entry.get('type') == 'dedi-file':
            registry_name = entry['registry']['name']
            registry_names.append(registry_name)
            inline_files.append((registry_name, entry))
        else:
            required_reference_fields = {'registry', 'url', 'digest'}
            missing_reference_fields = required_reference_fields - set(entry)
            if missing_reference_fields:
                raise SystemExit(
                    f'Publishing manifest reference missing fields: {sorted(missing_reference_fields)}'
                )
            registry_name = entry['registry']
            registry_names.append(registry_name)
            referenced_registries[registry_name] = entry

    if len(registry_names) != len(set(registry_names)):
        raise SystemExit('Publishing manifest contains duplicate registry names')

    for registry_name, inline_file in inline_files:
        validate_dedi_file(
            inline_file,
            manifest_key_ids,
            manifest['domain'],
            f'inline registry {registry_name}',
        )

    hosted_examples = {
        'public-keys': ROOT / 'examples/dedi.public-keys.json',
        'revocations': ROOT / 'examples/dedi.revocations.json',
    }

    for registry_name, path in hosted_examples.items():
        if registry_name not in referenced_registries:
            raise SystemExit(f'Hosted example {registry_name} is not referenced by the manifest')
        file_obj = load_json(path)
        if file_obj['registry']['name'] != registry_name:
            raise SystemExit(f'Hosted example {path.name} registry name does not match manifest entry')
        validate_dedi_file(
            file_obj,
            manifest_key_ids,
            manifest['domain'],
            f'hosted registry {registry_name}',
        )


def validate_required_paths():
    required = [
        ROOT / '.github/workflows/validate.yml',
        ROOT / 'reference-impl/server/server.py',
        ROOT / 'reference-impl/client/client.py',
        ROOT / 'examples/minimal-node/sample-response.json',
        ROOT / 'examples/dedi.index.json',
        ROOT / 'examples/dedi.public-keys.json',
        ROOT / 'examples/dedi.revocations.json',
        ROOT / 'schemas/dedi-file.schema.json',
        ROOT / 'schemas/dedi-manifest.schema.json',
        ROOT / 'spec/v0.1/README.md',
        ROOT / 'conformance/profiles/base.yaml',
        ROOT / 'conformance/profiles/secure.yaml',
        ROOT / 'conformance/profiles/publishing.yaml',
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
    validate_publishing_model()
    validate_json_files(sorted((ROOT / 'evidence').glob('*.json')), 'evidence artifact')
    print('All validations passed.')


if __name__ == '__main__':
    main()
