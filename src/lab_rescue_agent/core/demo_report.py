"""Deterministic local demo report builder for Lab Rescue Agent."""

from __future__ import annotations

import json
from pathlib import Path

from lab_rescue_agent.agents.assessment_agent import AssessmentAgent
from lab_rescue_agent.agents.lab_triage_agent import LabTriageAgent
from lab_rescue_agent.agents.learning_path_agent import LearningPathAgent
from lab_rescue_agent.agents.manager_insights_agent import ManagerInsightsAgent
from lab_rescue_agent.agents.recovery_planner_agent import RecoveryPlannerAgent
from lab_rescue_agent.agents.safety_verifier_agent import SafetyVerifierAgent
from lab_rescue_agent.agents.study_plan_agent import StudyPlanAgent


def project_root():
    return Path(__file__).resolve().parents[3]


def load_scenario(scenario_id):
    path = project_root() / "data" / "synthetic" / "lab_failure_scenarios.json"
    scenarios = json.loads(path.read_text(encoding="utf-8"))
    for scenario in scenarios:
        if scenario.get("scenario_id") == scenario_id:
            return scenario
    raise ValueError(f"Scenario not found: {scenario_id}")


def load_sources(source_names):
    source_map = {}
    base = project_root() / "knowledge"
    for name in source_names:
        path = base / name
        source_map[name] = path.read_text(encoding="utf-8")
    return source_map


def append_list(lines, title, items):
    lines.append(title)
    for item in items:
        lines.append(f"- {item}")
    lines.append("")


def build_report(scenario_id):
    scenario = load_scenario(scenario_id)
    sources = load_sources(scenario["approved_sources"])

    triage = LabTriageAgent().run(scenario)
    recovery = RecoveryPlannerAgent().run(scenario, triage)
    learning = LearningPathAgent().run(scenario, triage, recovery)
    study_plan = StudyPlanAgent().run(scenario, learning, recovery)
    assessment = AssessmentAgent().run(scenario, learning)
    manager = ManagerInsightsAgent().run(scenario, triage, learning, study_plan, assessment)
    safety = SafetyVerifierAgent().run(scenario, triage, recovery, learning, study_plan, assessment, manager)

    lines = []
    lines.append("Lab Rescue Agent Demo Report")
    lines.append("=" * 29)
    lines.append(f"Scenario: {scenario['scenario_id']}")
    lines.append(f"Certification: {scenario['certification']}")
    lines.append(f"Role: {scenario['role']}")
    lines.append("")
    lines.append("Agent 1: Lab Triage Agent")
    lines.append(f"- Confidence: {triage.confidence}")
    lines.append(f"- Diagnosis: {triage.diagnosis}")
    lines.append("")
    append_list(lines, "Evidence reviewed:", triage.evidence)
    append_list(lines, "Mapped skill areas:", triage.skill_areas)
    append_list(lines, "Citations:", triage.citations)

    lines.append("Agent 2: Recovery Planner Agent")
    lines.append(f"- Summary: {recovery.summary}")
    lines.append("")
    append_list(lines, "Fix steps:", recovery.fix_steps)
    append_list(lines, "Rollback steps:", recovery.rollback_steps)
    append_list(lines, "Verification steps:", recovery.verification_steps)
    append_list(lines, "Safety notes:", recovery.safety_notes)
    append_list(lines, "Recovery citations:", recovery.citations)

    lines.append("Agent 3: Learning Path Agent")
    lines.append(f"- Certification: {learning.certification}")
    lines.append(f"- Role: {learning.role}")
    lines.append(f"- Readiness impact: {learning.readiness_impact}")
    lines.append("")
    append_list(lines, "Study focus:", learning.study_focus)
    append_list(lines, "Recommended learner actions:", learning.recommended_actions)
    append_list(lines, "Learning citations:", learning.citations)

    lines.append("Agent 4: Study Plan Agent")
    lines.append(f"- Summary: {study_plan.summary}")
    lines.append(f"- Weekly study hours: {study_plan.weekly_study_hours}")
    lines.append(f"- Preferred slot: {study_plan.preferred_slot}")
    lines.append("")
    append_list(lines, "Capacity-aware schedule:", study_plan.schedule)
    append_list(lines, "Study milestones:", study_plan.milestones)
    append_list(lines, "Capacity notes:", study_plan.capacity_notes)
    append_list(lines, "Study plan citations:", study_plan.citations)

    lines.append("Agent 5: Assessment Agent")
    lines.append(f"- Readiness target: {assessment.readiness_target}")
    lines.append(f"- Scoring guidance: {assessment.scoring_guidance}")
    lines.append("")
    lines.append("Grounded practice questions:")
    for index, question in enumerate(assessment.questions, start=1):
        lines.append(f"- Q{index}: {question.question}")
        lines.append(f"  Expected: {question.expected_answer}")
        lines.append(f"  Skill: {question.skill_area}")
        lines.append(f"  Citation: {question.citation}")
    lines.append("")
    append_list(lines, "Assessment citations:", assessment.citations)

    lines.append("Agent 6: Manager Insights Agent")
    lines.append(f"- Team ID: {manager.team_id}")
    lines.append(f"- Summary: {manager.summary}")
    lines.append("")
    append_list(lines, "Readiness signals:", manager.readiness_signals)
    append_list(lines, "Risk areas:", manager.risk_areas)
    append_list(lines, "Recommended manager actions:", manager.recommended_manager_actions)
    append_list(lines, "Privacy notes:", manager.privacy_notes)
    append_list(lines, "Manager citations:", manager.citations)

    lines.append("Grounded sources loaded:")
    for name, text in sources.items():
        lines.append(f"- {name}: {len(text)} characters")
    lines.append("")

    lines.append("Agent 7: Safety Verifier Agent")
    lines.append(f"- Status: {safety.status}")
    lines.append("")
    append_list(lines, "Checks passed:", safety.checks_passed)
    if safety.warnings:
        append_list(lines, "Warnings:", safety.warnings)
    else:
        append_list(lines, "Warnings:", ["none"])
    append_list(lines, "Safety citations:", safety.citations)

    lines.append("Workflow status:")
    lines.append("- Seven-agent enterprise readiness demo completed with safety verification.")
    return "\n".join(lines)
