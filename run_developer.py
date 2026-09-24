from pathlib import Path

from developer_agent import run_developer
from file_io import read_json, write_text

ARTIFACTS_DIR = "artifacts"
PLAN_FILE = "plan.json"
OUTPUT_FILE = "navigation_logic.py"


def main():
    plan_file = Path(ARTIFACTS_DIR) / PLAN_FILE
    plan = read_json(plan_file)

    code = run_developer(plan)

    if code is None:
        print("No valid Python code was produced. Nothing was saved.")
        return

    print(code)

    write_text(code, OUTPUT_FILE)
    print(f"\nNavigation logic saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
