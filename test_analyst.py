"""Level 1 smoke test for the Analyst Agent.

Runs the real Analyst Agent with the real brief.txt and stores the validated
requirements artifact in artifacts/requirements.json.
"""

from pathlib import Path

from analyst_agent import run_analyst
from file_io import read_text, write_json

BRIEF_FILE = "brief.txt"
ARTIFACTS_DIR = "artifacts"
REQUIREMENTS_FILE = "requirements.json"


def run_tests():
    print("Testing the Analyst Agent with the real brief...\n")

    brief_text = read_text(BRIEF_FILE)

    requirements = run_analyst(brief_text)

    if requirements is None:
        print("FAILED: the Analyst Agent did not produce valid requirements.")
        return 1

    output_file = Path(ARTIFACTS_DIR) / REQUIREMENTS_FILE
    write_json(requirements, output_file)

    print(f"Analyst Agent output saved to {output_file}:\n")
    print(output_file.read_text(encoding="utf-8"))
    print("\nPASSED: the Analyst Agent produced a usable requirements artifact.")
    return 0


if __name__ == "__main__":
    raise SystemExit(run_tests())
