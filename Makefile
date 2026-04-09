PYTHON ?= python3

.PHONY: setup validate serve quickstart clean

setup:
	$(PYTHON) -m pip install -r requirements-dev.txt

validate:
	$(PYTHON) scripts/validate_artifacts.py

serve:
	$(PYTHON) reference-impl/server/server.py

quickstart:
	$(PYTHON) scripts/query_and_verify.py

clean:
	rm -f evidence/quickstart-run.json evidence/resolution-run.json evidence/signature-verification.json evidence/revocation-check.json
