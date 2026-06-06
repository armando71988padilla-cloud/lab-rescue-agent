"""Learning Path Agent for certification skill mapping."""

from __future__ import annotations

from dataclasses import dataclass

from lab_rescue_agent.agents.lab_triage_agent import LabTriageResult
from lab_rescue_agent.agents.recovery_planner_agent import RecoveryPlanResult


@dataclass(frozen=True)
class LearningPathResult:
    agent_name: str
    certification: str
    role: str
    study_focus: list[str]
    recommended_actions: list[str]
    readiness_impact: str
    citations: list[str]


class LearningPathAgent:
    """Maps lab failures to certification readiness needs."""

    name = "Learning Path Agent"

    def run(self, scenario: dict, triage: LabTriageResult, recovery: RecoveryPlanResult) -> LearningPathResult:
        certification = str(scenario.get("certification", "Unknown certification"))
        role = str(scenario.get("role", "Unknown role"))
        skill_areas = list(triage.skill_areas)

        study_focus = []
        for skill in skill_areas:
            study_focus.append(skill + " practice and recovery review")

        recommended_actions = [
            "Repeat the failed lab after applying the recovery plan.",
            "Write a short explanation of root cause, fix, rollback, and verification.",
            "Complete a focused practice check on Azure Functions configuration.",
            "Review approved synthetic knowledge sources before the next lab attempt.",
        ]

        readiness_impact = "This failure raises readiness risk until the learner can recover the lab and explain the configuration dependency."

        citations = []
        for citation in triage.citations + recovery.citations:
            if citation not in citations:
                citations.append(citation)

        return LearningPathResult(
            agent_name=self.name,
            certification=certification,
            role=role,
            study_focus=study_focus,
            recommended_actions=recommended_actions,
            readiness_impact=readiness_impact,
            citations=citations,
        )
