# Lab Rescue Agent v0.4 Demo Release

## Summary

This release adds Microsoft Foundry readiness reporting while preserving the deterministic local fallback used for reliable judging.

## Major upgrades

- Added foundry-status CLI command.
- Added no-dependency Foundry readiness reporter.
- Added Foundry readiness documentation.
- Added CI coverage for the Foundry readiness command.
- Preserved local deterministic demo behavior when Azure SDK packages, Azure CLI, or Foundry environment variables are missing.

## Foundry status command

PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent foundry-status

## Current honest claim

Lab Rescue Agent includes a Microsoft Foundry-ready configuration scaffold and deterministic local fallback. Live Foundry deployment is not verified in this local environment.

## Required live configuration

- AZURE_AI_PROJECT_ENDPOINT
- AZURE_AI_MODEL_DEPLOYMENT

## Smoke test

PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py

Expected output: DEMO_WORKFLOW_SMOKE_OK

## Safety posture

Synthetic data only. No real employee data, customer data, credentials, connection strings, tokens, or private logs.
