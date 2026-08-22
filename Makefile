PYTHON ?= python3

.PHONY: setup validate serve quickstart scenario clean

setup:
	$(PYTHON) -m pip install -r requirements-dev.txt

validate:
	$(PYTHON) scripts/validate_artifacts.py
	$(PYTHON) scripts/verify_publishing_crypto.py
	$(PYTHON) scripts/verify_publishing_lifecycle.py
	$(PYTHON) scripts/run_publishing_scenario.py

serve:
	$(PYTHON) reference-impl/server/server.py

quickstart:
	$(PYTHON) scripts/query_and_verify.py

scenario:
	$(PYTHON) scripts/run_publishing_scenario.py

clean:
	rm -f evidence/quickstart-run.json evidence/resolution-run.json evidence/signature-verification.json evidence/revocation-check.json evidence/publisher-indexer-verifier.json
