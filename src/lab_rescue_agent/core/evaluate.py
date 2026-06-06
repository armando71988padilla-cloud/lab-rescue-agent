"""Evaluation harness for Lab Rescue Agent demo quality checks."""

from __future__ import annotations

from dataclasses import dataclass
from tempfile import TemporaryDirectory

from lab_rescue_agent.core.demo_report import build_report, load_scenarios
from lab_rescue_agent.core.export_report import export_report
from lab_rescue_agent.integrations.foundry_status import foundry_status_text


@dataclass(frozen=True)
class EvaluationResult:
    name: str
    passed: bool
    detail: str


def contains_all(text: str, required: list[str]) -> bool:
    return all(item in text for item in required)


def evaluate_scenario(scenario: dict) -> list[EvaluationResult]:
    scenario_id = str(scenario.get("scenario_id", ""))
    report = build_report(scenario_id)
    questions = list(scenario.get("assessment_questions", []))

    results = [
        EvaluationResult(
            f"{scenario_id}: seven-agent report",
            contains_all(report, [
                "Agent 1: Lab Triage Agent",
                "Agent 2: Recovery Planner Agent",
                "Agent 3: Learning Path Agent",
                "Agent 4: Study Plan Agent",
                "Agent 5: Assessment Agent",
                "Agent 6: Manager Insights Agent",
                "Agent 7: Safety Verifier Agent",
            ]),
            "All seven agent sections must be present.",
        ),
        EvaluationResult(
            f"{scenario_id}: rollback coverage",
            bool(scenario.get("rollback_steps")) and "Rollback steps:" in report,
            "Scenario and report must include rollback steps.",
        ),
        EvaluationResult(
            f"{scenario_id}: verification coverage",
            bool(scenario.get("verification_steps")) and "Verification steps:" in report,
            "Scenario and report must include verification steps.",
        ),
        EvaluationResult(
            f"{scenario_id}: safety pass",
            "Status: pass" in report and "Warnings:" in report and "- none" in report,
            "Safety verifier must pass with no warnings.",
        ),
        EvaluationResult(
            f"{scenario_id}: assessment citation coverage",
            bool(questions) and all(item.get("citation") for item in questions),
            "Every scenario assessment question must include a citation.",
        ),
    ]

    with TemporaryDirectory() as temp_dir:
        markdown_path, json_path = export_report(scenario_id, output_dir=temp_dir)
        html_path = markdown_path.with_name(markdown_path.name.replace("_report.md", "_dashboard.html"))
        trace_path = markdown_path.with_name(markdown_path.name.replace("_report.md", "_trace.json"))
        manager_brief_path = markdown_path.with_name(markdown_path.name.replace("_report.md", "_manager_brief.md"))
        results.append(
            EvaluationResult(
                f"{scenario_id}: export artifacts",
                markdown_path.exists() and json_path.exists() and html_path.exists() and trace_path.exists() and manager_brief_path.exists(),
                "Markdown, JSON, HTML dashboard, agent trace, and manager brief exports must be created.",
            )
        )
        results.append(
            EvaluationResult(
                f"{scenario_id}: agent trace ledger",
                trace_path.exists() and "agent_reasoning_ledger" in trace_path.read_text(encoding="utf-8"),
                "Agent trace ledger must identify the seven-agent reasoning flow.",
            )
        )
        results.append(
            EvaluationResult(
                f"{scenario_id}: manager executive brief",
                manager_brief_path.exists() and "Recommended manager actions" in manager_brief_path.read_text(encoding="utf-8"),
                "Manager executive brief must provide actionable aggregate readiness guidance.",
            )
        )

    return results


def run_evaluation() -> tuple[bool, list[EvaluationResult]]:
    results: list[EvaluationResult] = []
    scenarios = load_scenarios()

    for scenario in scenarios:
        results.extend(evaluate_scenario(scenario))

    foundry_status = foundry_status_text({})
    results.append(
        EvaluationResult(
            "foundry readiness fallback",
            "Readiness mode: local_fallback_active" in foundry_status
            and "live Foundry deployment is not verified" in foundry_status,
            "Foundry readiness must honestly report local fallback when unconfigured.",
        )
    )

    passed = all(result.passed for result in results)
    return passed, results


def evaluation_text() -> str:
    passed, results = run_evaluation()
    scenarios_checked = len(load_scenarios())

    lines = ["EVAL_PASS" if passed else "EVAL_REVIEW"]
    lines.append(f"Scenarios checked: {scenarios_checked}")

    passed_count = sum(1 for result in results if result.passed)
    lines.append(f"Checks passed: {passed_count}/{len(results)}")
    lines.append("")

    for result in results:
        status = "PASS" if result.passed else "REVIEW"
        lines.append(f"- {status}: {result.name}")
        lines.append(f"  Detail: {result.detail}")

    return "\n".join(lines)
