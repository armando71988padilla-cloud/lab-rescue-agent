"""Command entrypoint for Lab Rescue Agent."""

from lab_rescue_agent import __version__


def main() -> int:
    print(f"Lab Rescue Agent v{__version__}")
    print("Status: local demo bootstrap ready")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
