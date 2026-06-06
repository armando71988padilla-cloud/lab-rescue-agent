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

    def run(self, scenario: dict, learning: LearningPathResult) -> AssessmentResult:
        certification = str(scenario.get("certification", "Unknown certification"))
        citations = list(learning.citations)

        configured_questions = list(scenario.get("assessment_questions", []))
        questions = []
        for item in configured_questions:
            questions.append(
                AssessmentQuestion(
                    question=str(item.get("question", "")),
                    expected_answer=str(item.get("expected_answer", "")),
                    skill_area=str(item.get("skill_area", "General readiness")),
                    citation=str(item.get("citation", "")),
                )
            )

        if not questions:
            questions = [
                AssessmentQuestion(
                    question="What was the confirmed root cause of the failed lab?",
                    expected_answer=str(scenario.get("known_root_cause", "Unknown root cause")),
                    skill_area="Root cause analysis",
                    citation=citations[0] if citations else "",
                ),
                AssessmentQuestion(
                    question="What should be verified after applying the recovery plan?",
                    expected_answer="The expected lab outcome should succeed and the original error should no longer appear.",
                    skill_area="Verification",
                    citation=citations[0] if citations else "",
                ),
                AssessmentQuestion(
                    question="Why should recovery steps avoid exposing secrets or private data?",
                    expected_answer="Recovery guidance must preserve safe handling of credentials, logs, and synthetic-only demo data.",
                    skill_area="Security hygiene",
                    citation="engineering_certification_guide.md",
                ),
            ]

        return AssessmentResult(
            agent_name=self.name,
            readiness_target=certification + " grounded practice readiness",
            questions=questions,
            scoring_guidance="Pass when the learner explains root cause, fix, rollback, verification, and safety constraints.",
            citations=citations,
        )
