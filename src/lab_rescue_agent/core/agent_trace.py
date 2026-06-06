"""Agent trace ledger export for Lab Rescue Agent."""

from __future__ import annotations

from lab_rescue_agent.core.demo_report import load_scenario


def build_agent_trace(scenario_id: str) -> dict:
    scenario = load_scenario(scenario_id)
    approved_sources = list(scenario.get("approved_sources", []))

    workflow = [
        {
            "agent": "Lab Triage Agent",
            "input_refs": ["scenario.failure_log", "scenario.expected_outcome", "scenario.observed_outcome"],
            "decision": "Diagnose the failure pattern and map it to certification skill areas.",
            "outputs": ["diagnosis", "confidence", "evidence", "skill_areas", "citations"],
            "citations": approved_sources,
            "safety_gates": ["synthetic_scenario_only", "grounded_citations_required"],
        },
        {
            "agent": "Recovery Planner Agent",
            "input_refs": ["triage_result", "scenario.known_root_cause", "scenario.fix_steps"],
            "decision": "Create safe repair steps for the confirmed failure pattern.",
            "outputs": ["summary", "fix_steps", "rollback_steps", "verification_steps", "safety_notes"],
            "citations": approved_sources,
            "safety_gates": ["rollback_required", "verification_required", "secret_hygiene_required"],
        },
        {
            "agent": "Learning Path Agent",
            "input_refs": ["triage_result.skill_areas", "recovery_plan"],
            "decision": "Convert the lab failure into certification readiness gaps and learner actions.",
            "outputs": ["readiness_impact", "study_focus", "recommended_actions"],
            "citations": approved_sources,
            "safety_gates": ["certification_mapping_required", "synthetic_learner_only"],
        },
        {
            "agent": "Study Plan Agent",
            "input_refs": ["learning_path", "team_learning_signals.json"],
            "decision": "Create a capacity-aware recovery schedule using synthetic learner constraints.",
            "outputs": ["weekly_study_hours", "capacity_aware_schedule", "milestones"],
            "citations": approved_sources + ["team_learning_signals.json"],
            "safety_gates": ["capacity_constraints_respected", "synthetic_team_signals_only"],
        },
        {
            "agent": "Assessment Agent",
            "input_refs": ["learning_path", "scenario.assessment_questions"],
            "decision": "Generate grounded practice questions that validate recovery understanding.",
            "outputs": ["questions", "expected_answers", "skill_areas", "citations"],
            "citations": approved_sources,
            "safety_gates": ["every_question_requires_citation", "answers_grounded_in_sources"],
        },
        {
            "agent": "Manager Insights Agent",
            "input_refs": ["triage_result", "learning_path", "study_plan", "assessment_result", "team_learning_signals.json"],
            "decision": "Summarize aggregate team readiness signals without exposing sensitive personal data.",
            "outputs": ["summary", "readiness_signals", "risk_areas", "recommended_manager_actions", "privacy_notes"],
            "citations": approved_sources + ["team_learning_signals.json"],
            "safety_gates": ["aggregate_only", "privacy_notes_required", "no_real_employee_data"],
        },
        {
            "agent": "Safety Verifier Agent",
            "input_refs": ["triage_result", "recovery_plan", "learning_path", "assessment_result", "manager_insights"],
            "decision": "Trust the final report only if citations, rollback, verification, synthetic data posture, and secret hygiene pass.",
            "outputs": ["status", "checks_passed", "warnings", "citations"],
            "citations": approved_sources + ["team_learning_signals.json"],
            "safety_gates": ["status_must_pass", "warnings_must_be_none", "secret_markers_block_report"],
        },
    ]

    return {
        "project": "Lab Rescue Agent",
        "scenario_id": scenario_id,
        "certification": scenario.get("certification", ""),
        "role": scenario.get("role", ""),
        "trace_type": "agent_reasoning_ledger",
        "workflow_count": len(workflow),
        "workflow": workflow,
        "data_policy": "Synthetic demo data only. No real employee data, customer data, credentials, connection strings, tokens, or private logs.",
    }
