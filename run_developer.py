from pathlib import Path

from developer_agent import run_developer
from file_io import read_json, write_text

ARTIFACTS_DIR = "artifacts"
PLAN_FILE = "plan.json"
GENERATED_DIR = "generated"
OUTPUT_FILE = "navigation_logic.py"


def main():
    plan_file = Path(ARTIFACTS_DIR) / PLAN_FILE
    plan = read_json(plan_file)

    code = run_developer(plan)

    if code is None:
        print("No valid Python code was produced. Nothing was saved.")
        return

    print(code)

    output_file = Path(GENERATED_DIR) / OUTPUT_FILE
    write_text(code, output_file)
    print(f"\nNavigation logic saved to {output_file}")


if __name__ == "__main__":
    main()
