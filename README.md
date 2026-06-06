# Lab Rescue Agent

[![Smoke Test](https://github.com/armando71988padilla-cloud/lab-rescue-agent/actions/workflows/smoke-test.yml/badge.svg)](https://github.com/armando71988padilla-cloud/lab-rescue-agent/actions/workflows/smoke-test.yml)

Lab Rescue Agent is a multi-agent certification lab recovery system for Microsoft AI Agents League.

It helps a technical learner recover from a failed hands-on certification lab, maps the failure to certification readiness, generates grounded practice questions, and verifies the final output for safety and reliability.

## Core idea

From failed lab to certification readiness in one safe, explainable multi-agent workflow.

## Current demo status

- Local deterministic Python demo works
- Seven specialized agents are wired into one enterprise readiness workflow
- Synthetic data only
- Grounded synthetic knowledge docs are cited in outputs
- Stdlib smoke test passes without extra test dependencies

## Agent workflow

1. Lab Triage Agent diagnoses the failed lab pattern.
2. Recovery Planner Agent creates fix, rollback, and verification steps.
3. Learning Path Agent maps the failure to certification readiness.
4. Study Plan Agent creates a capacity-aware recovery schedule.
5. Assessment Agent generates grounded practice questions.
6. Manager Insights Agent summarizes aggregate team readiness signals.
7. Safety Verifier Agent checks citations, rollback, verification, synthetic data posture, and secret hygiene.

## Demo scenario

Synthetic learner L-1001 is preparing for AZ-204 and fails an Azure Functions HTTP trigger lab.

The default scenario uses an AZ-204 Azure Functions failure where AzureWebJobsStorage is missing or empty. The project now also includes AZ-400 pipeline approval and AZ-104 VM NSG connectivity recovery scenarios.

## List demo scenarios

```bash
PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent scenarios
```

## Run the default demo

```bash
PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent demo
```

## Run a specific scenario

```bash
PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent demo az400-pipeline-approval-blocked
```

## Run the smoke test

```bash
PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py
```

## Export demo reports

```bash
PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent export
```

This writes Markdown reports and JSON summaries under `demo/output/`. Exports are scenario-specific when a scenario ID is provided.

Expected result:

```text
DEMO_WORKFLOW_SMOKE_OK
```

## Documentation

- Architecture: docs/architecture.md
- Microsoft integration plan: docs/microsoft_integration.md
- Microsoft Foundry readiness: docs/foundry_readiness.md
- Microsoft Foundry live probe guide: docs/foundry_live_probe.md
- Submission notes: docs/submission_notes.md
- Demo video script: docs/demo_video_script.md
- Demo prompts: demo/sample_prompts.md

## Hackathon alignment

- Track focus: reasoning agents
- Architecture: local-first Python multi-agent workflow
- Microsoft IQ layer focus: Foundry IQ style grounding over synthetic lab and certification knowledge
- Safety posture: synthetic data only, no secrets, rollback required, verification required
- Next integration target: Microsoft Agent Framework or Azure AI Foundry project endpoint

## Data policy

This repository uses synthetic learner data, synthetic lab logs, and synthetic knowledge documents only.

No real employee data, customer data, connection strings, secrets, or private logs belong in this repository.

## Current limitations

- The current version is deterministic and local-first.
- Live Microsoft Foundry integration is planned next.
- The first scenario covers Azure Functions storage configuration recovery only.

## Project structure

- src/lab_rescue_agent/agents: specialized agent modules
- src/lab_rescue_agent/core: deterministic report orchestration
- data/synthetic: synthetic lab failure scenarios, multi-scenario catalog, and team learning signals
- knowledge: approved synthetic grounding documents
- demo: sample demo prompts, commands, and exported report outputs
- tests: no-dependency smoke tests
