# Lab Rescue Agent v0.2 Demo Release

## Summary

This release upgrades Lab Rescue Agent into a seven-agent enterprise readiness workflow for certification lab recovery.

Lab Rescue Agent helps technical learners recover from failed certification labs, map failures to readiness gaps, generate grounded practice questions, create capacity-aware study plans, summarize manager readiness signals, and verify final output safety.

## Major upgrades

- Added Study Plan Agent for capacity-aware learning schedules.
- Added Manager Insights Agent for aggregate team readiness signals.
- Upgraded the demo report to a seven-agent enterprise readiness workflow.
- Added synthetic team learning signals.
- Added export mode for Markdown and JSON report outputs.
- Added generated demo report artifacts under demo/output/.
- Added multi-scenario demo support for AZ-204, AZ-400, and AZ-104 recovery cases.
- Added scenario list CLI command.
- Added GitHub Actions smoke test workflow.
- Added README CI badge.

## Seven-agent workflow

1. Lab Triage Agent
2. Recovery Planner Agent
3. Learning Path Agent
4. Study Plan Agent
5. Assessment Agent
6. Manager Insights Agent
7. Safety Verifier Agent

## Demo command

PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent scenarios
PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent demo
PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent demo az400-pipeline-approval-blocked

## Export command

PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent export

This writes:

- demo/output/az204-functions-storage-error_report.md
- demo/output/az204-functions-storage-error_summary.json

## Smoke test

PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py

Expected output:

DEMO_WORKFLOW_SMOKE_OK

## Safety posture

This project uses synthetic demo data only. It does not include real employee data, customer data, credentials, connection strings, or private logs.

## Release status

- Public GitHub repository: yes
- Seven-agent local demo: yes
- Exportable report artifacts: yes
- GitHub Actions smoke test: passing
- Demo video linked from repository homepage: yes
