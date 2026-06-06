"""Manager executive brief export for Lab Rescue Agent."""

from __future__ import annotations

from pathlib import Path

from lab_rescue_agent.agents.assessment_agent import AssessmentAgent
from lab_rescue_agent.agents.lab_triage_agent import LabTriageAgent
from lab_rescue_agent.agents.learning_path_agent import LearningPathAgent
from lab_rescue_agent.agents.manager_insights_agent import ManagerInsightsAgent
from lab_rescue_agent.agents.recovery_planner_agent import RecoveryPlannerAgent
from lab_rescue_agent.agents.study_plan_agent import StudyPlanAgent
from lab_rescue_agent.core.demo_report import load_scenario


def append_items(lines: list[str], title: str, items: list[str]) -> None:
    lines.append(f"## {title}")
    lines.append("")
    for item in items:
        lines.append(f"- {item}")
    lines.append("")


def build_manager_brief(scenario_id: str) -> str:
    scenario = load_scenario(scenario_id)

    triage = LabTriageAgent().run(scenario)
    recovery = RecoveryPlannerAgent().run(scenario, triage)
    learning = LearningPathAgent().run(scenario, triage, recovery)
    study_plan = StudyPlanAgent().run(scenario, learning, recovery)
    assessment = AssessmentAgent().run(scenario, learning)
    manager = ManagerInsightsAgent().run(scenario, triage, learning, study_plan, assessment)

    lines: list[str] = []
    lines.append("# Lab Rescue Agent Manager Executive Brief")
    lines.append("")
    lines.append(f"Scenario: {scenario_id}")
    lines.append(f"Certification: {scenario.get('certification', '')}")
    lines.append(f"Role: {scenario.get('role', '')}")
    lines.append(f"Team: {manager.team_id}")
    lines.append("")
    lines.append("## Executive summary")
    lines.append("")
    lines.append(manager.summary)
    lines.append("")
    lines.append("## Recommended intervention")
    lines.append("")
    lines.append(
        "Run a targeted recovery session where learners explain the root cause, safe fix, rollback plan, verification checks, and citation-backed readiness gaps."
    )
    lines.append("")
    lines.append("## Readiness posture")
    lines.append("")
    lines.append(f"- Readiness impact: {learning.readiness_impact}")
    lines.append(f"- Weekly study capacity: {study_plan.weekly_study_hours} hours")
    lines.append(f"- Assessment target: {assessment.readiness_target}")
    lines.append("")

    append_items(lines, "Readiness signals", manager.readiness_signals)
    append_items(lines, "Risk areas", manager.risk_areas)
    append_items(lines, "Recommended manager actions", manager.recommended_manager_actions)
    append_items(lines, "Privacy and safety notes", manager.privacy_notes)
    append_items(lines, "Citations", manager.citations)

    lines.append("## Data policy")
    lines.append("")
    lines.append("Synthetic demo data only. No real employee data, customer data, credentials, connection strings, tokens, or private logs.")
    lines.append("")

    return "\n".join(lines)


def write_manager_brief(path: Path, scenario_id: str) -> Path:
    path.write_text(build_manager_brief(scenario_id), encoding="utf-8")
    return path
