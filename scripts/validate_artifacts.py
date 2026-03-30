from pathlib import Path
import json
from jsonschema import Draft7Validator
from openapi_spec_validator import validate_spec
import yaml

root = Path(__file__).resolve().parents[1]

schema_files = {
    'public-key': root / 'schemas/public_key.json',
    'membership': root / 'schemas/membership.json',
    'revoke': root / 'schemas/revoke.json',
    'beckn-subscriber': root / 'schemas/Beckn_subscriber.json',
    'beckn-subscriber-reference': root / 'schemas/Beckn_subscriber_reference.json',
}

example_map = {
    'public-key': root / 'examples/public-key',
    'membership': root / 'examples/membership',
    'revoke': root / 'examples/revoke',
    'beckn-subscriber': root / 'examples/beckn-subscriber',
    'beckn-subscriber-reference': root / 'examples/beckn-subscriber-reference',
}

for key, schema_path in schema_files.items():
    schema = json.loads(schema_path.read_text())
    validator = Draft7Validator(schema)
    valid_obj = json.loads((example_map[key] / 'sample.json').read_text())
    errs = sorted(validator.iter_errors(valid_obj), key=lambda e: e.path)
    if errs:
        raise SystemExit(f'Valid example failed for {key}: {errs[0].message}')
    invalid_obj = json.loads((example_map[key] / 'invalid.json').read_text())
    errs = sorted(validator.iter_errors(invalid_obj), key=lambda e: e.path)
    if not errs:
        raise SystemExit(f'Invalid example unexpectedly passed for {key}')

spec = yaml.safe_load((root / 'api/openapi.yaml').read_text())
validate_spec(spec)
print('All validations passed.')
