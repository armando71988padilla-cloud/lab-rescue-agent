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
        summary = str(
            scenario.get(
                "recovery_summary",
                "Recovery plan targets the confirmed lab failure: " + str(root_cause),
            )
        )

        fix_steps = list(
            scenario.get(
                "fix_steps",
                [
                    "Confirm the lab resource belongs to the synthetic scenario.",
                    "Inspect current configuration before applying changes.",
                    "Apply the smallest safe correction for the confirmed root cause.",
                    "Restart or re-run the affected lab component after correction.",
                ],
            )
        )

        rollback_steps = list(
            scenario.get(
                "rollback_steps",
                [
                    "Record the previous configuration before applying changes.",
                    "Restore the previous configuration if verification fails.",
                    "Re-run verification after rollback.",
                ],
            )
        )

        verification_steps = list(
            scenario.get(
                "verification_steps",
                [
                    "Confirm the original failure no longer appears.",
                    "Confirm the expected lab outcome succeeds.",
                    "Confirm logs show no new safety or configuration errors.",
                ],
            )
        )

        safety_notes = list(
            scenario.get(
                "safety_notes",
                [
                    "Do not print real secrets in logs.",
                    "Do not commit credentials to Git.",
                    "Use synthetic lab identifiers only in demos.",
                ],
            )
        )

        return RecoveryPlanResult(
            agent_name=self.name,
            summary=summary,
            fix_steps=fix_steps,
            rollback_steps=rollback_steps,
            verification_steps=verification_steps,
            safety_notes=safety_notes,
            citations=list(triage.citations),
        )
