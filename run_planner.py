import json
from pathlib import Path

from planner_agent import run_planner

ARTIFACTS_DIR = "artifacts"
REQUIREMENTS_FILE = "requirements.json"
PLAN_FILE = "plan.json"


def read_requirements(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def save_plan(plan, filename):
    output_path = Path(filename)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(plan, file, indent=2)


def main():
    requirements_file = Path(ARTIFACTS_DIR) / REQUIREMENTS_FILE
    requirements = read_requirements(requirements_file)

    plan = run_planner(requirements)

    if plan is None:
        print("No valid plan was produced. Nothing was saved.")
        return

    print(json.dumps(plan, indent=2))

    output_file = Path(ARTIFACTS_DIR) / PLAN_FILE
    save_plan(plan, output_file)
    print(f"\nPlan saved to {output_file}")


if __name__ == "__main__":
    main()
