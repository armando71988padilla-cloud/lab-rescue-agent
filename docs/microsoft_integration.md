# Microsoft Integration Plan

## Current integration status

Lab Rescue Agent currently has a no-dependency Microsoft Foundry configuration scaffold.

The local deterministic demo remains the trusted fallback path. This keeps the project runnable even when Azure CLI, Azure credentials, Microsoft Agent Framework packages, or Foundry SDK packages are not installed.

## Current local proof

```bash
PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py
```

Expected output:

```text
DEMO_WORKFLOW_SMOKE_OK
```

## Foundry configuration probe

The current adapter reads these environment variables without importing Azure SDK packages:

- LAB_RESCUE_RUNTIME
- AZURE_AI_PROJECT_ENDPOINT
- AZURE_AI_MODEL_DEPLOYMENT
- AZURE_SUBSCRIPTION_ID
- AZURE_RESOURCE_GROUP
- AZURE_AI_PROJECT_NAME

Minimum required values for cloud mode:

- AZURE_AI_PROJECT_ENDPOINT
- AZURE_AI_MODEL_DEPLOYMENT

## Status command

Not configured:

```bash
PYTHONPATH="$PWD/src" python3 -c 'from lab_rescue_agent.integrations.foundry_config import describe_foundry_status; print(describe_foundry_status())'
```

Expected output when no Foundry variables are configured:

```text
foundry_not_configured_missing: AZURE_AI_PROJECT_ENDPOINT, AZURE_AI_MODEL_DEPLOYMENT
```

Configured probe:

```bash
PYTHONPATH="$PWD/src" python3 -c 'from lab_rescue_agent.integrations.foundry_config import describe_foundry_status; print(describe_foundry_status({"AZURE_AI_PROJECT_ENDPOINT":"https://example.services.ai.azure.com/api/projects/demo","AZURE_AI_MODEL_DEPLOYMENT":"demo-model"}))'
```

Expected output:

```text
foundry_configured
```

## Why this scaffold exists

The project should not fail locally just because cloud dependencies are missing.

The integration scaffold gives the repository a clear Microsoft Foundry path while preserving reliable local judging and demo behavior.

## Planned integration sequence

1. Keep local deterministic demo as the fallback.
2. Add optional Azure SDK dependencies in a separate requirements file.
3. Add Azure CLI login and environment validation documentation.
4. Add a Foundry-backed runner that mirrors the local five-agent workflow.
5. Add a smoke test that skips cloud calls unless Foundry configuration is present.

## Microsoft technology mapping

| Project area | Microsoft path | Current project status |
|---|---|---|
| Multi-agent orchestration | Microsoft Agent Framework | Local deterministic five-agent workflow implemented |
| Project endpoint configuration | Microsoft Foundry / Azure AI Projects | No-dependency config scaffold implemented |
| Grounding over approved docs | Foundry IQ-style grounding | Synthetic markdown docs and citations implemented |
| Cloud auth | Azure CLI / Azure Identity | Not required for local demo; planned for optional cloud mode |
| Reliability | Local fallback and smoke tests | Implemented |

## Current limitation

This repository does not yet run live cloud calls against Microsoft Foundry. The current integration is a safe configuration bridge and documentation path.

## Official docs to consult during live integration

- Microsoft Agent Framework overview
- Microsoft Agent Framework workflows
- Microsoft Foundry SDKs and endpoints
- Azure AI Projects client library for Python
- Microsoft Foundry provider for Agent Framework
