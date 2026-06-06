# Microsoft Foundry Readiness

## Current status

Lab Rescue Agent includes a Microsoft Foundry-ready configuration scaffold and deterministic local fallback.

The current local environment does not prove a live Foundry deployment. The project therefore reports readiness honestly through the foundry-status command.

## Readiness command

PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent foundry-status

## Expected unconfigured output

- Configuration: missing_required_configuration
- Readiness mode: local_fallback_active
- Claim: Foundry-ready scaffold with deterministic local fallback; live Foundry deployment is not verified.

## Required live configuration

- AZURE_AI_PROJECT_ENDPOINT
- AZURE_AI_MODEL_DEPLOYMENT

## Optional metadata

- LAB_RESCUE_RUNTIME
- AZURE_SUBSCRIPTION_ID
- AZURE_RESOURCE_GROUP
- AZURE_AI_PROJECT_NAME

## Dependency notes

The local fallback does not require Azure SDK packages. A future live probe should install Azure SDK dependencies and authenticate with Azure before claiming live deployment.

## Safety rule

Do not place secrets, connection strings, tokens, or private tenant data in this repository.
