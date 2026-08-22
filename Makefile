PYTHON ?= python3

.PHONY: setup validate conformance serve quickstart scenario clean

setup:
	$(PYTHON) -m pip install -r requirements-dev.txt

validate:
	$(PYTHON) scripts/run_conformance.py

conformance:
	$(PYTHON) scripts/run_conformance.py

serve:
	$(PYTHON) reference-impl/server/server.py

quickstart:
	$(PYTHON) scripts/query_and_verify.py

scenario:
	$(PYTHON) scripts/run_publishing_scenario.py

clean:
	rm -f evidence/quickstart-run.json evidence/resolution-run.json evidence/signature-verification.json evidence/revocation-check.json evidence/publisher-indexer-verifier.json evidence/conformance-run.json
