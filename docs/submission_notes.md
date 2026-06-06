# Lab Rescue Agent Submission Notes

## Project summary

Lab Rescue Agent is a multi-agent certification lab recovery system. It helps a learner recover from a failed technical certification lab, maps the failure to readiness gaps, creates grounded practice questions, and verifies the final output for safety.

## Why this matters

Hands-on labs are where technical learners often get stuck. A normal study planner tells a learner what to study before failure. Lab Rescue Agent helps at the moment of failure and turns that failure into recovery steps, learning actions, assessment questions, and readiness signals.

## Challenge fit

| Requirement | How Lab Rescue Agent addresses it |
|---|---|
| Multi-agent system | Uses seven specialized agents in a sequential enterprise readiness workflow |
| Enterprise learning scenario | Focuses on certification lab recovery and readiness for technical teams |
| Microsoft IQ layer | Uses Foundry IQ-style grounding over approved synthetic lab and certification docs |
| Synthetic data | Uses synthetic learner IDs, synthetic team IDs, synthetic lab logs, and synthetic knowledge docs only |
| Safety and reliability | Requires rollback, verification, citations, synthetic data checks, and secret hygiene checks |
| Demo clarity | Runs locally with one command and includes a no-dependency smoke test |

## Agents

1. Lab Triage Agent: diagnoses the failed lab pattern.
2. Recovery Planner Agent: creates fix, rollback, and verification steps.
3. Learning Path Agent: maps the failure to certification readiness.
4. Study Plan Agent: creates a capacity-aware study schedule and milestones.
5. Assessment Agent: generates grounded practice questions with citations.
6. Manager Insights Agent: summarizes aggregate team readiness and manager actions.
7. Safety Verifier Agent: checks citations, rollback, verification, synthetic data posture, privacy notes, and secret hygiene.

## Judging rubric alignment

| Rubric area | Evidence in project |
|---|---|
| Accuracy and relevance | Diagnosis is tied to synthetic failure evidence and approved knowledge docs |
| Reasoning and multi-step thinking | Output flows from triage to recovery to learning to study planning to assessment to manager insights to safety verification |
| Reliability and safety | Smoke test, deterministic fallback, rollback checks, verification checks, citation checks, and secret hygiene scan |
| Creativity | Combines debugging recovery with certification readiness instead of building a generic study planner |
| User experience | One-command local demo and simple README/docs path |

## Current demo command

```bash
PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent demo
```

## Current smoke test command

```bash
PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py
```

Expected output:

```text
DEMO_WORKFLOW_SMOKE_OK
```

## Current limitation

The current version is deterministic and local-first. The next build step is connecting the same workflow to Microsoft Agent Framework or Azure AI Foundry while preserving the local fallback.
