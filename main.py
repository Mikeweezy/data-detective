"""Data Detective - project entry point."""

import sys
from pathlib import Path

# Make the src/ layout importable when running from the repo root
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from data_detective import get_version


def main() -> None:
    """Run the Data Detective application."""
    print(f"Data Detective v{get_version()}")
    print("Project scaffolding is ready. Start building your analysis!")


if __name__ == "__main__":
    main()