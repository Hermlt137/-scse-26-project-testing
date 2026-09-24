"""Level 1 smoke test for the Planner Agent.

Runs the real Planner Agent with the real requirements.json artifact and
stores the validated plan in artifacts/plan.json.
"""

from pathlib import Path

from file_io import read_json, write_json
from planner_agent import run_planner

ARTIFACTS_DIR = "artifacts"
REQUIREMENTS_FILE = "requirements.json"
PLAN_FILE = "plan.json"


def run_tests():
    print("Testing the Planner Agent with the real requirements artifact...\n")

    requirements_file = Path(ARTIFACTS_DIR) / REQUIREMENTS_FILE
    requirements = read_json(requirements_file)

    plan = run_planner(requirements)

    if plan is None:
        print("FAILED: the Planner Agent did not produce a valid plan.")
        return 1

    output_file = Path(ARTIFACTS_DIR) / PLAN_FILE
    write_json(plan, output_file)

    print(f"Planner Agent output saved to {output_file}:\n")
    print(output_file.read_text(encoding="utf-8"))
    print("\nPASSED: the Planner Agent produced a plan the Developer Agent can use.")
    return 0


if __name__ == "__main__":
    raise SystemExit(run_tests())
