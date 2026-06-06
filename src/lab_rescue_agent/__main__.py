"""Command entrypoint for Lab Rescue Agent."""

from __future__ import annotations

import sys

from lab_rescue_agent import __version__
from lab_rescue_agent.core.demo_report import build_report


DEFAULT_SCENARIO_ID = "az204-functions-storage-error"


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        print(f"Lab Rescue Agent v{__version__}")
        print("Usage: python3 -m lab_rescue_agent demo")
        return 0

    command = args[0]
    if command == "demo":
        scenario_id = args[1] if len(args) > 1 else DEFAULT_SCENARIO_ID
        print(build_report(scenario_id))
        return 0

    print(f"Unknown command: {command}")
    print("Supported commands: demo")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
