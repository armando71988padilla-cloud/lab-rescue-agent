"""Study Plan Agent for capacity-aware certification recovery planning."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path

from lab_rescue_agent.agents.learning_path_agent import LearningPathResult
from lab_rescue_agent.agents.recovery_planner_agent import RecoveryPlanResult


def project_root() -> Path:
    return Path(__file__).resolve().parents[3]


def load_team_learning_signals() -> dict:
    path = project_root() / "data" / "synthetic" / "team_learning_signals.json"
    return json.loads(path.read_text(encoding="utf-8"))


def load_learner_signal(learner_id: str) -> dict:
    data = load_team_learning_signals()
    for learner in data.get("learners", []):
        if learner.get("learner_id") == learner_id:
            return learner
    return {}


@dataclass(frozen=True)
class StudyPlanResult:
    agent_name: str
    summary: str
    weekly_study_hours: int
    preferred_slot: str
    schedule: list[str]
    milestones: list[str]
    capacity_notes: list[str]
    citations: list[str]


class StudyPlanAgent:
    """Creates a practical study schedule using synthetic work-capacity signals."""

    name = "Study Plan Agent"

    def run(
        self,
        scenario: dict,
        learning: LearningPathResult,
        recovery: RecoveryPlanResult,
    ) -> StudyPlanResult:
        learner_id = str(scenario.get("learner_id", ""))
        learner_signal = load_learner_signal(learner_id)

        weekly_study_hours = int(learner_signal.get("available_study_hours_per_week", 4))
        preferred_slot = str(learner_signal.get("preferred_learning_slot", "Morning"))
        meeting_hours = int(learner_signal.get("meeting_hours_per_week", 0))

        summary = (
            f"Create a capacity-aware {scenario.get('certification', 'certification')} recovery plan "
            f"for {scenario.get('role', 'learner')} using {weekly_study_hours} focused hours per week."
        )

        schedule = [
            f"{preferred_slot} focus block 1: reproduce the synthetic lab failure and collect evidence.",
            f"{preferred_slot} focus block 2: apply the recovery plan and verify the HTTP trigger behavior.",
            "Short review block: write root cause, fix, rollback, and verification notes.",
            "Practice block: answer grounded questions tied to approved recovery and certification sources.",
        ]

        milestones = [
            "Recover the failed lab without introducing secrets into logs or source control.",
            "Explain why the missing application setting blocked the runtime host.",
            "Pass grounded practice checks at or above the readiness threshold.",
            "Demonstrate rollback and verification steps clearly enough for manager review.",
        ]

        capacity_notes = []
        if meeting_hours >= 20:
            capacity_notes.append("High meeting load detected; use short protected focus blocks instead of long study sessions.")
        else:
            capacity_notes.append("Meeting load allows moderate study blocks without heavy schedule disruption.")

        if weekly_study_hours <= 4:
            capacity_notes.append("Limited study capacity; prioritize recovery verification before broad topic review.")
        else:
            capacity_notes.append("Sufficient study capacity for recovery practice plus additional certification review.")

        citations = []
        for citation in learning.citations + recovery.citations + ["team_learning_signals.json"]:
            if citation not in citations:
                citations.append(citation)

        return StudyPlanResult(
            agent_name=self.name,
            summary=summary,
            weekly_study_hours=weekly_study_hours,
            preferred_slot=preferred_slot,
            schedule=schedule,
            milestones=milestones,
            capacity_notes=capacity_notes,
            citations=citations,
        )
