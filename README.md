# Lab Rescue Agent

Lab Rescue Agent is a multi-agent certification lab recovery system for Microsoft AI Agents League.

It helps a technical learner recover from a failed hands-on certification lab, maps the failure to certification readiness, generates grounded practice questions, and verifies the final output for safety and reliability.

## Core idea

From failed lab to certification readiness in one safe, explainable multi-agent workflow.

## Current demo status

- Local deterministic Python demo works
- Five specialized agents are wired into one workflow
- Synthetic data only
- Grounded synthetic knowledge docs are cited in outputs
- Stdlib smoke test passes without extra test dependencies

## Agent workflow

1. Lab Triage Agent diagnoses the failed lab pattern.
2. Recovery Planner Agent creates fix, rollback, and verification steps.
3. Learning Path Agent maps the failure to certification readiness.
4. Assessment Agent generates grounded practice questions.
5. Safety Verifier Agent checks citations, rollback, verification, synthetic data posture, and secret hygiene.

## Demo scenario

Synthetic learner L-1001 is preparing for AZ-204 and fails an Azure Functions HTTP trigger lab.

The failure evidence indicates that AzureWebJobsStorage is missing or empty, causing the Function App host to fail initialization.

## Run the demo

```bash
PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent demo
```

## Run the smoke test

```bash
PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py
```

Expected result:

```text
DEMO_WORKFLOW_SMOKE_OK
```

## Documentation

- Architecture: docs/architecture.md
- Microsoft integration plan: docs/microsoft_integration.md
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
- data/synthetic: synthetic lab failure scenarios
- knowledge: approved synthetic grounding documents
- demo: sample demo prompts and commands
- tests: no-dependency smoke tests
