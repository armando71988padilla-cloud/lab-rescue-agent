"""Lab Triage Agent for deterministic failure diagnosis."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LabTriageResult:
    agent_name: str
    diagnosis: str
    evidence: list[str]
    confidence: str
    citations: list[str]
    skill_areas: list[str]


class LabTriageAgent:
    """Diagnoses a failed synthetic certification lab scenario."""

    name = "Lab Triage Agent"

    def run(self, scenario: dict) -> LabTriageResult:
        evidence = list(scenario.get("failure_log", []))
        root_cause = str(scenario.get("known_root_cause", "Unknown root cause"))
        citations = list(scenario.get("approved_sources", []))
        skill_areas = list(scenario.get("skill_areas", []))

        diagnosis = "Failure pattern matches a configuration issue: " + root_cause

        return LabTriageResult(
            agent_name=self.name,
            diagnosis=diagnosis,
            evidence=evidence,
            confidence="high",
            citations=citations,
            skill_areas=skill_areas,
        )
