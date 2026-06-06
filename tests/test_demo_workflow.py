"""Stdlib regression smoke test for the Lab Rescue Agent demo."""

from lab_rescue_agent.core.demo_report import build_report


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


def main():
    test_demo_report_contains_required_agent_sections()
    test_demo_report_contains_enterprise_readiness_outputs()
    test_demo_report_contains_grounded_citations()
    print("DEMO_WORKFLOW_SMOKE_OK")


if __name__ == "__main__":
    main()
