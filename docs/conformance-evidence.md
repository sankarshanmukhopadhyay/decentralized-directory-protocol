# Evidence-producing conformance runs

This fork treats conformance as an executable activity that should leave behind an inspectable record, not only a transient CI status.

The unified runner is:

```bash
python scripts/run_conformance.py
```

or:

```bash
make conformance
```

## What the runner executes

The current publishing suite runs, in order:

1. repository artifact and schema validation;
2. publishing cryptographic verification;
3. publishing lifecycle and freshness verification; and
4. the publisher → indexer → verifier end-to-end scenario.

A failure stops the sequence and is recorded as a failed step.

## Evidence artifact

A successful or failed run writes:

`evidence/conformance-run.json`

The artifact records:

- the fork-local profile under evaluation;
- explicit non-normative status;
- the upstream commit against which the profile is pinned;
- the fork repository commit being evaluated;
- generation time;
- the complete list of profile check IDs;
- each executed command;
- return code;
- captured stdout and stderr; and
- final pass/fail status.

The generated record is validated against:

`schemas/conformance-evidence.schema.json`

## Why this is different from a green CI badge

A CI badge answers a narrow question: did the workflow succeed at that moment?

The conformance evidence answers a more useful set of questions:

- **What profile was evaluated?**
- **Which requirements/check IDs were in scope?**
- **Which upstream baseline was assumed?**
- **Which fork commit was tested?**
- **What executable steps ran?**
- **Where did a failure occur?**
- **Can another evaluator reproduce the same run?**

This makes the result suitable as an assurance input while avoiding the stronger claim that the fork operates an upstream DeDi certification program.

## Evidence lifecycle

The generated `conformance-run.json` is runtime evidence. It is intentionally removed by `make clean` and can be regenerated from the repository state.

Long-lived evidence intended for release or audit purposes should be captured deliberately with the corresponding release/ref, environment details, and immutable artifact digest rather than treating a mutable working-tree file as archival evidence.

## Current scope

The publishing profile currently covers structural, cryptographic, lifecycle, and composed role-flow checks. Future profiles can use the same runner/evidence contract so that different DeDi implementation surfaces produce comparable assurance records.
