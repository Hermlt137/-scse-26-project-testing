import json
from pathlib import Path

from file_io import read_json, write_json
from planner_agent import run_planner

ARTIFACTS_DIR = "artifacts"
REQUIREMENTS_FILE = "requirements.json"
PLAN_FILE = "plan.json"


def main():
    requirements_file = Path(ARTIFACTS_DIR) / REQUIREMENTS_FILE
    requirements = read_json(requirements_file)

    plan = run_planner(requirements)

    if plan is None:
        print("No valid plan was produced. Nothing was saved.")
        return

    print(json.dumps(plan, indent=2))

    output_file = Path(ARTIFACTS_DIR) / PLAN_FILE
    write_json(plan, output_file)
    print(f"\nPlan saved to {output_file}")


if __name__ == "__main__":
    main()
