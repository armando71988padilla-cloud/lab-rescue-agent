# Lab Rescue Agent Demo Video Script

## 60 to 90 second version

Lab Rescue Agent is a multi-agent certification lab recovery system built for Microsoft AI Agents League.

The problem is simple: learners often fail hands-on certification labs and do not know whether the issue is a missing skill, a bad configuration, or a recoverable lab mistake.

This project turns a failed lab into a structured recovery and readiness workflow.

The demo uses a synthetic AZ-204 Azure Functions lab failure. The learner deploys an HTTP trigger, but the Function App host cannot start because AzureWebJobsStorage is missing or empty.

The workflow runs through five agents:

1. Lab Triage Agent diagnoses the failure pattern.
2. Recovery Planner Agent creates fix, rollback, and verification steps.
3. Learning Path Agent maps the issue to certification readiness.
4. Assessment Agent creates grounded practice questions.
5. Safety Verifier Agent checks citations, rollback, verification, synthetic data posture, and secret hygiene.

The demo is deterministic and local-first, so judges can run it with one command:

```bash
PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent demo
```

There is also a no-dependency smoke test:

```bash
PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py
```

Expected result:

```text
DEMO_WORKFLOW_SMOKE_OK
```

The current Microsoft integration path is documented and scaffolded with a no-dependency Foundry config adapter, so the local demo stays reliable while the project remains ready for Microsoft Foundry or Agent Framework integration.

The final output shows a passing safety verifier, grounded citations, rollback steps, verification steps, and synthetic-only data handling.

## Screen recording checklist

1. Show the GitHub README.
2. Show docs/architecture.md.
3. Show docs/submission_notes.md.
4. Run the smoke test.
5. Run the demo command.
6. Scroll to Agent 5 and show Status: pass and Warnings: none.
7. Close by showing the public GitHub repo URL.

## Exact commands to show

```bash
PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py
PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent demo
```
