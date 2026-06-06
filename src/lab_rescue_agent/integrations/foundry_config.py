"""No-dependency Foundry configuration helpers.

This module does not import Azure SDK packages. It only reads environment
variables so the local deterministic demo remains runnable without cloud setup.
"""

from __future__ import annotations

from dataclasses import dataclass
import os
from collections.abc import Mapping


@dataclass(frozen=True)
class FoundryConfig:
    runtime: str
    project_endpoint: str
    model_deployment: str
    subscription_id: str
    resource_group: str
    project_name: str

    def is_configured(self) -> bool:
        return bool(self.project_endpoint and self.model_deployment)

    def missing_required(self) -> list[str]:
        missing = []
        if not self.project_endpoint:
            missing.append("AZURE_AI_PROJECT_ENDPOINT")
        if not self.model_deployment:
            missing.append("AZURE_AI_MODEL_DEPLOYMENT")
        return missing


def load_foundry_config(env: Mapping[str, str] | None = None) -> FoundryConfig:
    source = os.environ if env is None else env
    return FoundryConfig(
        runtime=source.get("LAB_RESCUE_RUNTIME", "local"),
        project_endpoint=source.get("AZURE_AI_PROJECT_ENDPOINT", ""),
        model_deployment=source.get("AZURE_AI_MODEL_DEPLOYMENT", ""),
        subscription_id=source.get("AZURE_SUBSCRIPTION_ID", ""),
        resource_group=source.get("AZURE_RESOURCE_GROUP", ""),
        project_name=source.get("AZURE_AI_PROJECT_NAME", ""),
    )


def describe_foundry_status(env: Mapping[str, str] | None = None) -> str:
    config = load_foundry_config(env)
    if config.is_configured():
        return "foundry_configured"
    missing = ", ".join(config.missing_required())
    return "foundry_not_configured_missing: " + missing
