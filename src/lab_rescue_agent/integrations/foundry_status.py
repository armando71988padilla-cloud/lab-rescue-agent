"""No-dependency Microsoft Foundry readiness reporting."""

from __future__ import annotations

import importlib.util
import shutil
from dataclasses import dataclass
from collections.abc import Mapping

from lab_rescue_agent.integrations.foundry_config import load_foundry_config


def package_status(module_name: str) -> str:
    try:
        spec = importlib.util.find_spec(module_name)
    except ModuleNotFoundError:
        spec = None
    return "available" if spec is not None else "missing"


@dataclass(frozen=True)
class FoundryReadiness:
    runtime: str
    config_status: str
    missing_required: list[str]
    package_statuses: dict[str, str]
    azure_cli_status: str
    readiness_mode: str
    claim: str


def build_foundry_readiness(env: Mapping[str, str] | None = None) -> FoundryReadiness:
    config = load_foundry_config(env)
    packages = {
        "azure.ai.projects": package_status("azure.ai.projects"),
        "azure.identity": package_status("azure.identity"),
        "azure.ai.agents": package_status("azure.ai.agents"),
    }
    azure_cli_status = "available" if shutil.which("az") else "missing"
    missing_required = config.missing_required()

    if config.is_configured() and packages["azure.ai.projects"] == "available" and packages["azure.identity"] == "available":
        readiness_mode = "live_probe_ready"
        claim = "Foundry configuration and SDK are present; run a non-destructive live probe before claiming deployment."
    elif config.is_configured():
        readiness_mode = "config_present_sdk_missing"
        claim = "Foundry configuration is present, but local SDK dependencies are missing."
    else:
        readiness_mode = "local_fallback_active"
        claim = "Foundry-ready scaffold with deterministic local fallback; live Foundry deployment is not verified."

    config_status = "configured" if config.is_configured() else "missing_required_configuration"
    return FoundryReadiness(config.runtime, config_status, missing_required, packages, azure_cli_status, readiness_mode, claim)


def foundry_status_text(env: Mapping[str, str] | None = None) -> str:
    readiness = build_foundry_readiness(env)
    lines = ["Microsoft Foundry readiness status"]
    lines.append(f"- Runtime: {readiness.runtime}")
    lines.append(f"- Configuration: {readiness.config_status}")
    missing_required = ", ".join(readiness.missing_required) if readiness.missing_required else "none"
    lines.append(f"- Missing required: {missing_required}")
    for package_name, status in readiness.package_statuses.items():
        lines.append(f"- Package {package_name}: {status}")
    lines.append(f"- Azure CLI: {readiness.azure_cli_status}")
    lines.append(f"- Readiness mode: {readiness.readiness_mode}")
    lines.append(f"- Claim: {readiness.claim}")
    return "\n".join(lines)
