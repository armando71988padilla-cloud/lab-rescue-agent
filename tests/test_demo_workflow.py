"""Stdlib regression smoke test for the Lab Rescue Agent demo."""

from __future__ import annotations

import json
from tempfile import TemporaryDirectory

from lab_rescue_agent.core.demo_report import build_report
from lab_rescue_agent.core.export_report import export_report


def require_contains(report, required):
    missing = [item for item in required if item not in report]
    if missing:
        raise AssertionError("Missing required content: " + ", ".join(missing))


def test_demo_report_contains_required_agent_sections():
    report = build_report("az204-functions-storage-error")
    require_contains(report, [
        "Agent 1: Lab Triage Agent",
        "Agent 2: Recovery Planner Agent",
        "Agent 3: Learning Path Agent",
        "Agent 4: Study Plan Agent",
        "Agent 5: Assessment Agent",
        "Agent 6: Manager Insights Agent",
        "Agent 7: Safety Verifier Agent",
        "Status: pass",
        "Warnings:",
        "- none",
        "Workflow status:",
        "Seven-agent enterprise readiness demo completed with safety verification.",
    ])


def test_demo_report_contains_enterprise_readiness_outputs():
    report = build_report("az204-functions-storage-error")
    require_contains(report, [
        "Capacity-aware schedule:",
        "Study milestones:",
        "Manager Insights Agent",
        "Readiness signals:",
        "Recommended manager actions:",
        "Privacy notes:",
        "Synthetic team size reviewed: 3",
    ])


def test_demo_report_contains_grounded_citations():
    report = build_report("az204-functions-storage-error")
    require_contains(report, [
        "engineering_certification_guide.md",
        "azure_functions_lab_recovery.md",
        "team_learning_signals.json",
        "Citation: azure_functions_lab_recovery.md",
        "Citation: engineering_certification_guide.md",
    ])


def test_export_report_writes_markdown_and_json_outputs():
    with TemporaryDirectory() as temp_dir:
        markdown_path, json_path = export_report("az204-functions-storage-error", output_dir=temp_dir)

        if not markdown_path.exists():
            raise AssertionError("Markdown export was not created.")
        if not json_path.exists():
            raise AssertionError("JSON export was not created.")

        markdown = markdown_path.read_text(encoding="utf-8")
        summary = json.loads(json_path.read_text(encoding="utf-8"))

        require_contains(markdown, [
            "Exported Lab Rescue Agent Report",
            "Agent 7: Safety Verifier Agent",
            "Seven-agent enterprise readiness demo completed with safety verification.",
        ])

        if summary.get("safety_status") != "pass":
            raise AssertionError("Export summary safety_status is not pass.")
        if len(summary.get("workflow", [])) != 7:
            raise AssertionError("Export summary does not contain seven workflow agents.")


def main():
    test_demo_report_contains_required_agent_sections()
    test_demo_report_contains_enterprise_readiness_outputs()
    test_demo_report_contains_grounded_citations()
    test_export_report_writes_markdown_and_json_outputs()
    print("DEMO_WORKFLOW_SMOKE_OK")


if __name__ == "__main__":
    main()
