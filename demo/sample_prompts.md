# Lab Rescue Agent Demo Prompts

## Primary demo command

Run the deterministic local demo:

```bash
PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent demo
```

## Smoke test command

Run the no-dependency regression check:

```bash
PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py
```

## Demo scenario

Synthetic learner L-1001 is preparing for AZ-204 and fails an Azure Functions HTTP trigger lab.

Failure evidence:

- Function host starts but HTTP trigger is unavailable
- AzureWebJobsStorage is missing or empty
- Host initialization fails because storage connection cannot be resolved

## Expected agent flow

1. Lab Triage Agent diagnoses the failure pattern.
2. Recovery Planner Agent creates fix, rollback, and verification steps.
3. Learning Path Agent maps the failure to certification readiness.
4. Assessment Agent generates grounded practice questions.
5. Safety Verifier Agent checks citations, rollback, verification, synthetic data posture, and secret hygiene.

## Expected final status

Safety Verifier Agent should report:

```text
Status: pass
Warnings:
- none
```
