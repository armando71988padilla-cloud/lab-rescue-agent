"""Command entrypoint for Lab Rescue Agent."""

from __future__ import annotations

import sys

from lab_rescue_agent import __version__
from lab_rescue_agent.core.demo_report import build_report, load_scenarios
from lab_rescue_agent.core.export_report import DEFAULT_SCENARIO_ID, export_report


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        print(f"Lab Rescue Agent v{__version__}")
        print("Usage: python3 -m lab_rescue_agent scenarios|demo|export [scenario_id]")
        return 0

    command = args[0]
    if command == "scenarios":
        for scenario in load_scenarios():
            scenario_id = scenario.get("scenario_id", "")
            certification = scenario.get("certification", "")
            role = scenario.get("role", "")
            title = scenario.get("title", "")
            print(f"{scenario_id} | {certification} | {role} | {title}")
        return 0

    if command == "demo":
        scenario_id = args[1] if len(args) > 1 else DEFAULT_SCENARIO_ID
        print(build_report(scenario_id))
        return 0

    if command == "export":
        scenario_id = args[1] if len(args) > 1 else DEFAULT_SCENARIO_ID
        markdown_path, json_path = export_report(scenario_id)
        print("Export complete")
        print(f"Markdown report: {markdown_path}")
        print(f"JSON summary: {json_path}")
        return 0

    print(f"Unknown command: {command}")
    print("Supported commands: scenarios, demo, export")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
