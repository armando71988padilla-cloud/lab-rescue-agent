# Lab Rescue Agent v0.3 Demo Release

## Summary

This release upgrades Lab Rescue Agent with multi-scenario certification lab recovery support across AZ-204, AZ-400, and AZ-104 synthetic lab failures.

## Major upgrades

- Added three-scenario demo catalog.
- Added scenario list CLI command.
- Added scenario-specific recovery planning, assessment questions, manager risk areas, and exports.
- Added AZ-400 pipeline approval recovery scenario.
- Added AZ-104 VM NSG connectivity recovery scenario.
- Added synthetic recovery knowledge docs for DevOps pipeline approvals and Azure VM network recovery.
- Expanded smoke tests to validate all scenarios and exports.

## Scenario commands

PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent scenarios

PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent demo az204-functions-storage-error

PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent demo az400-pipeline-approval-blocked

PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent demo az104-vm-nsg-connectivity

## Export command

PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent export az400-pipeline-approval-blocked

## Smoke test

PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py

Expected output: DEMO_WORKFLOW_SMOKE_OK

## Safety posture

Synthetic data only. No real employee data, customer data, credentials, connection strings, or private logs.
