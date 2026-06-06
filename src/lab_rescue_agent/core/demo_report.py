"""Deterministic local demo report builder for Lab Rescue Agent."""

from __future__ import annotations

import json
from pathlib import Path

from lab_rescue_agent.agents.lab_triage_agent import LabTriageAgent
from lab_rescue_agent.agents.recovery_planner_agent import RecoveryPlannerAgent


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
    lines.append("Grounded sources loaded:")
    for name, text in sources.items():
        lines.append(f"- {name}: {len(text)} characters")
    lines.append("")
    lines.append("Next agent actions:")
    lines.append("- Learning Path Agent maps the issue to certification skills")
    lines.append("- Assessment Agent generates grounded practice questions")
    lines.append("- Safety Verifier Agent checks for secrets, PII, and unsafe claims")
    return "\n".join(lines)
