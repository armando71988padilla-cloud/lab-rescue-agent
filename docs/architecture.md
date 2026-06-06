# Lab Rescue Agent Architecture

## Purpose

Lab Rescue Agent is a local-first multi-agent workflow that helps a learner recover from a failed certification lab and convert that failure into certification readiness actions.

## Demo scenario

A synthetic AZ-204 learner fails an Azure Functions HTTP trigger lab because the Function App runtime cannot resolve the AzureWebJobsStorage setting.

## Agent pipeline

```text
Synthetic lab failure
        |
        v
Lab Triage Agent
        |
        v
Recovery Planner Agent
        |
        v
Learning Path Agent
        |
        v
Assessment Agent
        |
        v
Safety Verifier Agent
        |
        v
Final trusted demo report
```

## Agent responsibilities

| Agent | Responsibility | Output |
|---|---|---|
| Lab Triage Agent | Diagnoses the failure pattern from synthetic lab evidence | diagnosis, confidence, evidence, citations |
| Recovery Planner Agent | Creates safe repair steps | fix steps, rollback steps, verification steps, safety notes |
| Learning Path Agent | Maps the lab failure to certification readiness | study focus, learner actions, readiness impact |
| Assessment Agent | Creates grounded practice questions | questions, expected answers, skill areas, citations |
| Safety Verifier Agent | Checks output reliability and data hygiene | pass/review status, checks passed, warnings, citations |

## Grounding model

The current version uses synthetic markdown knowledge documents as the grounding layer:

- knowledge/azure_functions_lab_recovery.md
- knowledge/engineering_certification_guide.md

This models a Foundry IQ-style retrieval pattern where agents cite approved knowledge sources before producing recovery or readiness guidance.

## Safety controls

- Synthetic learner and team identifiers only
- No real employee data
- No customer data
- No real connection strings
- No secrets in source control
- Recovery plans must include rollback steps
- Recovery plans must include verification steps
- Assessment questions must include citations

## Current runtime

The current implementation is deterministic Python so the demo can run reliably without cloud quota or network dependencies.

## Planned Microsoft integration

The next integration step is to connect the same agent flow to Microsoft Agent Framework or an Azure AI Foundry project endpoint while preserving the local deterministic fallback.
