# Conformance

The purpose of this directory is to make implementation claims testable.

## Contents

- `profiles/` contains machine-readable conformance profiles
- `tests/` contains named test definitions
- `vectors/` contains valid and invalid payload fixtures
- `validation-guide.md` explains how to run and interpret validation
- `test-matrix.md` provides a human-readable cross-check

## Baseline expectation

A DeDi implementation should be able to show:

- which profile it targets,
- which tests it passes,
- which vectors it uses,
- and what evidence it can emit from real runs.
