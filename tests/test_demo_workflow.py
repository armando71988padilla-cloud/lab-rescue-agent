"""Stdlib regression smoke test for the Lab Rescue Agent demo."""

from __future__ import annotations

import json
from tempfile import TemporaryDirectory

from lab_rescue_agent.core.demo_report import build_report, load_scenarios
from lab_rescue_agent.core.export_report import export_report
from lab_rescue_agent.integrations.foundry_status import foundry_status_text


EXPECTED_SCENARIO_IDS = [
    "az204-functions-storage-error",
    "az400-pipeline-approval-blocked",
    "az104-vm-nsg-connectivity",
]


def require_contains(report, required):
    missing = [item for item in required if item not in report]
    if missing:
        raise AssertionError("Missing required content: " + ", ".join(missing))


def test_scenario_catalog_contains_expected_scenarios():
    scenarios = load_scenarios()
    scenario_ids = [scenario.get("scenario_id") for scenario in scenarios]

    for expected_id in EXPECTED_SCENARIO_IDS:
        if expected_id not in scenario_ids:
            raise AssertionError("Missing expected scenario: " + expected_id)


def test_all_scenarios_generate_seven_agent_reports():
    for scenario_id in EXPECTED_SCENARIO_IDS:
        report = build_report(scenario_id)
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


def test_default_demo_report_contains_enterprise_readiness_outputs():
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


def test_scenario_specific_outputs_are_grounded():
    checks = {
        "az204-functions-storage-error": [
            "AZ-204",
            "AzureWebJobsStorage",
            "azure_functions_lab_recovery.md",
        ],
        "az400-pipeline-approval-blocked": [
            "AZ-400",
            "environment approval",
            "devops_pipeline_recovery.md",
        ],
        "az104-vm-nsg-connectivity": [
            "AZ-104",
            "NSG",
            "azure_vm_network_recovery.md",
        ],
    }

    for scenario_id, required in checks.items():
        report = build_report(scenario_id)
        require_contains(report, required)


def test_default_demo_report_contains_grounded_citations():
    report = build_report("az204-functions-storage-error")
    require_contains(report, [
        "engineering_certification_guide.md",
        "azure_functions_lab_recovery.md",
        "team_learning_signals.json",
        "Citation: azure_functions_lab_recovery.md",
        "Citation: engineering_certification_guide.md",
    ])


def test_export_report_writes_markdown_and_json_outputs_for_all_scenarios():
    with TemporaryDirectory() as temp_dir:
        for scenario_id in EXPECTED_SCENARIO_IDS:
            markdown_path, json_path = export_report(scenario_id, output_dir=temp_dir)
            html_path = markdown_path.with_name(markdown_path.name.replace("_report.md", "_dashboard.html"))

            if not markdown_path.exists():
                raise AssertionError("Markdown export was not created for " + scenario_id)
            if not json_path.exists():
                raise AssertionError("JSON export was not created for " + scenario_id)
            if not html_path.exists():
                raise AssertionError("HTML dashboard export was not created for " + scenario_id)

            markdown = markdown_path.read_text(encoding="utf-8")
            dashboard = html_path.read_text(encoding="utf-8")
            summary = json.loads(json_path.read_text(encoding="utf-8"))

            require_contains(markdown, [
                "Exported Lab Rescue Agent Report",
                "Agent 7: Safety Verifier Agent",
                "Seven-agent enterprise readiness demo completed with safety verification.",
            ])
            require_contains(dashboard, [
                "Lab Rescue Agent Dashboard",
                "Seven-agent certification lab recovery dashboard",
                "Foundry Readiness",
                scenario_id,
            ])

            if summary.get("scenario_id") != scenario_id:
                raise AssertionError("Export summary scenario_id mismatch for " + scenario_id)
            if summary.get("safety_status") != "pass":
                raise AssertionError("Export summary safety_status is not pass for " + scenario_id)
            if len(summary.get("workflow", [])) != 7:
                raise AssertionError("Export summary does not contain seven workflow agents for " + scenario_id)


def test_foundry_status_reports_local_fallback_when_unconfigured():
    status = foundry_status_text({})
    require_contains(status, [
        "Microsoft Foundry readiness status",
        "Readiness mode: local_fallback_active",
        "live Foundry deployment is not verified",
    ])


def main():
    test_scenario_catalog_contains_expected_scenarios()
    test_all_scenarios_generate_seven_agent_reports()
    test_default_demo_report_contains_enterprise_readiness_outputs()
    test_scenario_specific_outputs_are_grounded()
    test_default_demo_report_contains_grounded_citations()
    test_export_report_writes_markdown_and_json_outputs_for_all_scenarios()
    test_foundry_status_reports_local_fallback_when_unconfigured()
    print("DEMO_WORKFLOW_SMOKE_OK")


if __name__ == "__main__":
    main()
