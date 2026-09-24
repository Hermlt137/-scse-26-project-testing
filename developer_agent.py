import ast
import json

from llm import ask_qwen, clean_response

REQUIRED_FUNCTION = "decide_action"
REQUIRED_PARAMETER_NAMES = [
    "goal_ahead",
    "goal_on_left",
    "goal_on_right",
    "front_blocked",
    "left_blocked",
    "right_blocked",
]

SYSTEM_PROMPT = """You are the Developer Agent, a Python developer for a mobile robot navigation system.

Your only job is to read the validated navigation plan produced by the Planner Agent and turn it into working Python code. You do not answer questions and you do not write anything except Python code.

Rules you must follow:
- Write pure Python code that uses only the standard library.
- Define a function named decide_action(goal_ahead, goal_on_left, goal_on_right, front_blocked, left_blocked, right_blocked).
- All six parameters are booleans: goal_ahead, goal_on_left and goal_on_right tell whether the goal is in that direction; front_blocked, left_blocked and right_blocked tell whether that direction is blocked.
- The function must return exactly one of these strings: "FORWARD", "LEFT", "RIGHT", "STOP".
- The function must apply this exact decision order:
  1. If the goal is ahead and the front is not blocked, return "FORWARD".
  2. If the goal is on the left and the left is not blocked, return "LEFT".
  3. If the goal is on the right and the right is not blocked, return "RIGHT".
  4. If the front is not blocked, return "FORWARD".
  5. If the left is not blocked, return "LEFT".
  6. If the right is not blocked, return "RIGHT".
  7. Return "STOP" only when all three directions are blocked.
- The function must never return a direction that is blocked.
- The function must never return "STOP" while at least one direction is not blocked.
- Return ONLY the Python code, with no markdown code fences, no explanations, and no text before or after the code."""


def build_prompt(plan):
    system_prompt = SYSTEM_PROMPT
    user_prompt = f"""Validated navigation plan:
{json.dumps(plan, indent=2)}

Write the Python navigation logic for this plan."""
    return system_prompt, user_prompt


def validate_code(code):
    if not isinstance(code, str):
        return False

    if not code.strip():
        return False

    try:
        tree = ast.parse(code)
    except SyntaxError:
        return False

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == REQUIRED_FUNCTION:
            parameter_names = [arg.arg for arg in node.args.args]
            return parameter_names == REQUIRED_PARAMETER_NAMES

    return False


def run_developer(plan):
    system_prompt, user_prompt = build_prompt(plan)

    response_text = ask_qwen(system_prompt, user_prompt)

    code = clean_response(response_text)

    if not validate_code(code):
        print("The Developer Agent did not return valid Python code.")
        return None

    return code
