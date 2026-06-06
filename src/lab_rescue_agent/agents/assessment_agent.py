"""Assessment Agent for grounded readiness checks."""

from __future__ import annotations

from dataclasses import dataclass

from lab_rescue_agent.agents.learning_path_agent import LearningPathResult


@dataclass(frozen=True)
class AssessmentQuestion:
    question: str
    expected_answer: str
    skill_area: str
    citation: str


@dataclass(frozen=True)
class AssessmentResult:
    agent_name: str
    readiness_target: str
    questions: list[AssessmentQuestion]
    scoring_guidance: str
    citations: list[str]


class AssessmentAgent:
    """Creates grounded synthetic practice questions."""

    name = "Assessment Agent"

    def run(self, scenario: dict, learning: LearningPathResult):
        certification = str(scenario.get("certification", "Unknown certification"))
        citations = list(learning.citations)

        questions = [
            AssessmentQuestion(
                question="What setting is commonly required for an Azure Functions host to start storage-backed runtime services?",
                expected_answer="AzureWebJobsStorage must be present and valid for the synthetic lab Function App.",
                skill_area="Application settings",
                citation="azure_functions_lab_recovery.md",
            ),
            AssessmentQuestion(
                question="What should the learner verify after repairing the Function App setting?",
                expected_answer="The host starts without storage errors and the HTTP trigger responds.",
                skill_area="Deployment verification",
                citation="azure_functions_lab_recovery.md",
            ),
            AssessmentQuestion(
                question="Why should connection strings not be printed or committed during recovery?",
                expected_answer="They are secrets and must not appear in logs or source control.",
                skill_area="Security hygiene",
                citation="engineering_certification_guide.md",
            ),
        ]

        return AssessmentResult(
            agent_name=self.name,
            readiness_target=certification + " grounded practice readiness",
            questions=questions,
            scoring_guidance="Pass when the learner explains root cause, fix, rollback, verification, and secret safety.",
            citations=citations,
        )
