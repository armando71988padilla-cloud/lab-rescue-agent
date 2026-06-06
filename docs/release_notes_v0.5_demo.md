# Lab Rescue Agent v0.5 Maximum Polish Demo Release

## Summary

This release upgrades Lab Rescue Agent into a maximum-polish hackathon demo with visual dashboards, audit-ready agent traces, manager executive briefs, an evaluation harness, and optional Microsoft Foundry live-probe documentation.

## Major upgrades since v0.4

- Added static HTML dashboard exports for each scenario.
- Added agent trace ledger JSON exports for each scenario.
- Added manager executive brief exports for each scenario.
- Added evaluation harness with 25 quality checks across all scenarios.
- Added optional Microsoft Foundry live-probe guide and requirements file.
- Polished README to surface all judge-facing demo artifacts.\n- Added Judge Quick Path section for fast review.\n- Added one-command recording walkthrough script for final demo capture.

## Core workflow

Lab Rescue Agent now demonstrates a seven-agent enterprise readiness workflow: triage, recovery planning, certification mapping, study planning, assessment generation, manager insights, and safety verification.

## Demo artifacts

Each scenario can export:
- Markdown report
- JSON summary
- Static HTML dashboard
- Agent trace ledger JSON
- Manager executive brief

## Key commands

PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent scenarios
PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent demo
PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent export az204-functions-storage-error
PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent evaluate
PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent foundry-status
PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py

## Expected quality gate

EVAL_PASS
Checks passed: 25/25
DEMO_WORKFLOW_SMOKE_OK

## Safety posture

Synthetic data only. No real employee data, customer data, credentials, connection strings, tokens, production logs, or private tenant data.
