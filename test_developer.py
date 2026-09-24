"""Level 1 smoke test for the Developer Agent.

Runs the real Developer Agent with the real plan.json artifact and stores the
generated navigation logic in generated/navigation_logic.py.
"""

import importlib.util
from pathlib import Path

from developer_agent import run_developer
from file_io import read_json, write_text

ARTIFACTS_DIR = "artifacts"
PLAN_FILE = "plan.json"
GENERATED_DIR = "generated"
OUTPUT_FILE = "navigation_logic.py"


def load_generated_module(path):
    spec = importlib.util.spec_from_file_location("generated_navigation_logic", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_tests():
    print("Testing the Developer Agent with the real plan artifact...\n")

    plan_file = Path(ARTIFACTS_DIR) / PLAN_FILE
    plan = read_json(plan_file)

    code = run_developer(plan)

    if code is None:
        print("FAILED: the Developer Agent did not produce valid Python code.")
        return 1

    output_file = Path(GENERATED_DIR) / OUTPUT_FILE
    write_text(code, output_file)

    print(f"Developer Agent output saved to {output_file}:\n")
    print(output_file.read_text(encoding="utf-8"))

    module = load_generated_module(output_file)

    if not callable(getattr(module, "decide_next_move", None)):
        print("\nFAILED: decide_next_move(state) was not created.")
        return 1

    print("\nPASSED: the Developer Agent produced navigation logic with decide_next_move(state).")
    return 0


if __name__ == "__main__":
    raise SystemExit(run_tests())
