"""Report export helpers for Lab Rescue Agent."""

from __future__ import annotations

import json
from pathlib import Path

from lab_rescue_agent.core.demo_report import build_report, load_scenario, project_root


DEFAULT_SCENARIO_ID = "az204-functions-storage-error"


def safe_filename(value: str) -> str:
    allowed = []
    for char in value:
        if char.isalnum() or char in {"-", "_"}:
            allowed.append(char)
        else:
            allowed.append("-")
    return "".join(allowed).strip("-") or "lab-rescue-report"


def build_summary(scenario_id: str) -> dict:
    scenario = load_scenario(scenario_id)
    return {
        "project": "Lab Rescue Agent",
        "scenario_id": scenario_id,
        "certification": scenario.get("certification", ""),
        "role": scenario.get("role", ""),
        "team_id": scenario.get("team_id", ""),
        "learner_id": scenario.get("learner_id", ""),
        "workflow": [
            "Lab Triage Agent",
            "Recovery Planner Agent",
            "Learning Path Agent",
            "Study Plan Agent",
            "Assessment Agent",
            "Manager Insights Agent",
            "Safety Verifier Agent",
        ],
        "safety_status": "pass",
        "data_policy": "Synthetic demo data only. No real employee data, customer data, secrets, or private logs.",
        "expected_smoke_test": "DEMO_WORKFLOW_SMOKE_OK",
    }


def export_report(scenario_id: str = DEFAULT_SCENARIO_ID, output_dir: str | Path | None = None) -> tuple[Path, Path]:
    root = project_root()
    output_path = root / "demo" / "output" if output_dir is None else Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    base_name = safe_filename(scenario_id)
    markdown_path = output_path / f"{base_name}_report.md"
    json_path = output_path / f"{base_name}_summary.json"

    report = build_report(scenario_id)
    summary = build_summary(scenario_id)

    markdown_path.write_text("# Exported Lab Rescue Agent Report\n\n" + report + "\n", encoding="utf-8")
    json_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    return markdown_path, json_path
