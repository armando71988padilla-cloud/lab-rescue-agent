"""Manager Insights Agent for synthetic team readiness signals."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path

from lab_rescue_agent.agents.assessment_agent import AssessmentResult
from lab_rescue_agent.agents.lab_triage_agent import LabTriageResult
from lab_rescue_agent.agents.learning_path_agent import LearningPathResult
from lab_rescue_agent.agents.study_plan_agent import StudyPlanResult


def project_root() -> Path:
    return Path(__file__).resolve().parents[3]


def load_team_learning_signals() -> dict:
    path = project_root() / "data" / "synthetic" / "team_learning_signals.json"
    return json.loads(path.read_text(encoding="utf-8"))


@dataclass(frozen=True)
class ManagerInsightsResult:
    agent_name: str
    team_id: str
    summary: str
    readiness_signals: list[str]
    risk_areas: list[str]
    recommended_manager_actions: list[str]
    privacy_notes: list[str]
    citations: list[str]


class ManagerInsightsAgent:
    """Summarizes team readiness without exposing sensitive personal data."""

    name = "Manager Insights Agent"

    def run(
        self,
        scenario: dict,
        triage: LabTriageResult,
        learning: LearningPathResult,
        study_plan: StudyPlanResult,
        assessment: AssessmentResult,
    ) -> ManagerInsightsResult:
        team_data = load_team_learning_signals()
        team_id = str(scenario.get("team_id", team_data.get("team_id", "TEAM-UNKNOWN")))
        learners = list(team_data.get("learners", []))

        team_size = len(learners)
        low_score_count = sum(1 for learner in learners if int(learner.get("practice_score_avg", 0)) < 75)
        failed_or_review_count = sum(
            1 for learner in learners
            if str(learner.get("recent_lab_outcome", "")).lower() in {"fail", "review"}
        )

        summary = (
            f"{team_id} shows elevated readiness risk around {scenario.get('certification', 'the target certification')} "
            f"because the current failed lab maps to core skill areas: {', '.join(triage.skill_areas)}."
        )

        readiness_signals = [
            f"Synthetic team size reviewed: {team_size}",
            f"Learners below 75 percent practice readiness: {low_score_count}",
            f"Learners with failed or review lab outcomes: {failed_or_review_count}",
            f"Current learner study capacity: {study_plan.weekly_study_hours} hours per week",
            f"Assessment target: {assessment.readiness_target}",
        ]

        risk_areas = [
            "Azure Functions configuration recovery",
            "Application setting verification before code changes",
            "Rollback discipline after failed recovery attempts",
            "Grounded explanation of root cause and verification evidence",
        ]

        recommended_manager_actions = [
            "Protect short focus blocks for learners with high meeting load.",
            "Assign a targeted Azure Functions recovery practice session.",
            "Review whether learners can explain root cause, fix, rollback, and verification steps.",
            "Use aggregate readiness signals only; do not expose private learner details in manager summaries.",
        ]

        privacy_notes = [
            "Uses synthetic learner and employee identifiers only.",
            "Summarizes aggregate readiness signals instead of exposing sensitive personal data.",
            "Does not use real employee records, customer data, credentials, or private logs.",
        ]

        citations = []
        for citation in learning.citations + study_plan.citations + assessment.citations + ["team_learning_signals.json"]:
            if citation not in citations:
                citations.append(citation)

        return ManagerInsightsResult(
            agent_name=self.name,
            team_id=team_id,
            summary=summary,
            readiness_signals=readiness_signals,
            risk_areas=risk_areas,
            recommended_manager_actions=recommended_manager_actions,
            privacy_notes=privacy_notes,
            citations=citations,
        )
