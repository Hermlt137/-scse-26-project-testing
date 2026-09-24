import json
from pathlib import Path

from developer_agent import run_developer

ARTIFACTS_DIR = "artifacts"
PLAN_FILE = "plan.json"
OUTPUT_FILE = "navigation_logic.py"


def read_plan(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def save_code(code, filename):
    Path(filename).write_text(code, encoding="utf-8")


def main():
    plan_file = Path(ARTIFACTS_DIR) / PLAN_FILE
    plan = read_plan(plan_file)

    code = run_developer(plan)

    if code is None:
        print("No valid Python code was produced. Nothing was saved.")
        return

    print(code)

    save_code(code, OUTPUT_FILE)
    print(f"\nNavigation logic saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
