# Microsoft Foundry Live Probe Guide

## Purpose

This guide documents the safe path for validating Lab Rescue Agent against a live Microsoft Foundry project.

The repository does not require live Azure access for judging. The default demo uses deterministic local execution so judges can run it reliably without cloud quota, credentials, tenant access, or tenant-specific setup.

## Current honest status

Lab Rescue Agent includes:

- A Microsoft Foundry-ready configuration scaffold
- A no-dependency foundry-status command
- Deterministic local fallback
- CI coverage that verifies the fallback path

The current local environment should not be described as a verified live Foundry deployment unless a non-destructive live probe succeeds.

## Optional dependencies

Install optional Foundry dependencies only when testing live Foundry access:

    python3 -m pip install -r requirements-foundry.txt

## Required live configuration

Set the project endpoint and model deployment name in your local shell or CI secret environment only.

Example shape:

    AZURE_AI_PROJECT_ENDPOINT=https://<resource-name>.services.ai.azure.com/api/projects/<project-name>
    AZURE_AI_MODEL_DEPLOYMENT=<model-deployment-name>
    LAB_RESCUE_RUNTIME=foundry

Optional metadata:

    AZURE_SUBSCRIPTION_ID=<subscription-id>
    AZURE_RESOURCE_GROUP=<resource-group>
    AZURE_AI_PROJECT_NAME=<project-name>

## Authentication

Use Azure CLI authentication before attempting a live probe:

    az login

Do not commit tenant IDs, access tokens, client secrets, connection strings, project endpoints from private tenants, or other private values.

## Readiness command

Run:

    PYTHONPATH="$PWD/src" python3 -m lab_rescue_agent foundry-status

Expected local fallback output when unconfigured:

    Readiness mode: local_fallback_active
    Claim: Foundry-ready scaffold with deterministic local fallback; live Foundry deployment is not verified.

Expected readiness direction when configured and SDK packages are installed:

    Readiness mode: live_probe_ready
    Claim: Foundry configuration and SDK are present; run a non-destructive live probe before claiming deployment.

## Safe live probe rule

A live probe should be non-destructive. It should only confirm that the Foundry project endpoint, authentication, and model deployment are reachable.

Do not upload real employee data, customer data, production logs, credentials, secrets, tokens, or private tenant content.

## Submission wording

Safe wording:

Lab Rescue Agent includes a Microsoft Foundry-ready configuration scaffold and deterministic local fallback, making the workflow ready for future Foundry or Agent Framework integration while remaining reliable for hackathon judging.

Unsafe wording unless proven by a successful live probe:

Lab Rescue Agent is deployed to Microsoft Foundry.
