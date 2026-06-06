"""Safety Verifier Agent for reliability and data hygiene checks."""

from __future__ import annotations

from dataclasses import dataclass

from lab_rescue_agent.agents.assessment_agent import AssessmentResult
from lab_rescue_agent.agents.lab_triage_agent import LabTriageResult
from lab_rescue_agent.agents.learning_path_agent import LearningPathResult
from lab_rescue_agent.agents.recovery_planner_agent import RecoveryPlanResult


@dataclass(frozen=True)
class SafetyVerificationResult:
    agent_name: str
    status: str
    checks_passed: list[str]
    warnings: list[str]
    citations: list[str]


class SafetyVerifierAgent:
    """Checks output hygiene before a demo report is trusted."""

    name = "Safety Verifier Agent"

    secret_markers = [
        "AccountKey=", "SharedAccessSignature=", "DefaultEndpointsProtocol=", "ghp_", "AZURE_CLIENT_SECRET"
    ]

    def run(
        self,
        scenario: dict,
        triage: LabTriageResult,
        recovery: RecoveryPlanResult,
        learning: LearningPathResult,
        assessment: AssessmentResult,
    ) -> SafetyVerificationResult:
        checks_passed = []
        warnings = []

        learner_id = str(scenario.get("learner_id", ""))
        team_id = str(scenario.get("team_id", ""))
        joined_log = " ".join(str(item) for item in scenario.get("failure_log", []))

        if learner_id.startswith("L-") and team_id.startswith("TEAM-"):
            checks_passed.append("Synthetic learner and team identifiers confirmed.")
        else:
            warnings.append("Learner or team identifier does not match the synthetic demo pattern.")

        if any(marker in joined_log for marker in self.secret_markers):
            warnings.append("Failure log contains a secret-looking marker.")
        else:
            checks_passed.append("No secret-looking markers found in failure log.")

        if recovery.rollback_steps:
            checks_passed.append("Rollback steps are present.")
        else:
            warnings.append("Recovery plan is missing rollback steps.")

        if recovery.verification_steps:
            checks_passed.append("Verification steps are present.")
        else:
            warnings.append("Recovery plan is missing verification steps.")

        if triage.citations and learning.citations and assessment.citations:
            checks_passed.append("Grounded citations are present across agent outputs.")
        else:
            warnings.append("One or more agent outputs are missing citations.")

        missing_question_citations = [q.question for q in assessment.questions if not q.citation]
        if missing_question_citations:
            warnings.append("One or more assessment questions are missing citations.")
        else:
            checks_passed.append("Every assessment question includes a citation.")

        citations = []
        for citation in triage.citations + recovery.citations + learning.citations + assessment.citations:
            if citation not in citations:
                citations.append(citation)

        status = "pass" if not warnings else "review"

        return SafetyVerificationResult(
            agent_name=self.name,
            status=status,
            checks_passed=checks_passed,
            warnings=warnings,
            citations=citations,
        )
