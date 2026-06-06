"""Recovery Planner Agent for safe lab repair planning."""

from __future__ import annotations

from dataclasses import dataclass

from lab_rescue_agent.agents.lab_triage_agent import LabTriageResult


@dataclass(frozen=True)
class RecoveryPlanResult:
    agent_name: str
    summary: str
    fix_steps: list[str]
    rollback_steps: list[str]
    verification_steps: list[str]
    safety_notes: list[str]
    citations: list[str]


class RecoveryPlannerAgent:
    """Creates safe fix, rollback, and verification steps."""

    name = "Recovery Planner Agent"

    def run(self, scenario: dict, triage: LabTriageResult) -> RecoveryPlanResult:
        root_cause = scenario.get("known_root_cause", "Unknown root cause")
        summary = "Recovery plan targets the confirmed lab failure: " + str(root_cause)

        fix_steps = [
            "Confirm the Function App belongs to the synthetic lab scenario.",
            "Inspect current application settings before changing configuration.",
            "Add or repair the AzureWebJobsStorage setting using synthetic lab storage values only.",
            "Restart the Function App after the setting is corrected.",
        ]

        rollback_steps = [
            "Record the previous app setting value before applying changes.",
            "Restore the previous value if the host still fails to start.",
            "Restart the Function App again after rollback.",
        ]

        verification_steps = [
            "Confirm the function host starts without storage configuration errors.",
            "Confirm the HTTP trigger endpoint responds.",
            "Confirm deployment logs no longer mention missing AzureWebJobsStorage.",
        ]

        safety_notes = [
            "Do not print real connection strings in logs.",
            "Do not commit secrets to Git.",
            "Use synthetic lab identifiers only in demos.",
        ]

        return RecoveryPlanResult(
            agent_name=self.name,
            summary=summary,
            fix_steps=fix_steps,
            rollback_steps=rollback_steps,
            verification_steps=verification_steps,
            safety_notes=safety_notes,
            citations=list(triage.citations),
        )
