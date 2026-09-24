import json

from llm import ask_qwen, parse_json_response

REQUIRED_KEYS = {"strategy", "decisions", "stop_condition"}
VALID_ACTIONS = ["FORWARD", "LEFT", "RIGHT", "STOP"]

SYSTEM_PROMPT = """You are the Planner Agent, a software planner for a mobile robot navigation system.

Your only job is to read the validated software requirements produced by the Analyst Agent and decide how the software should behave. You do not write code and you do not answer questions.

Rules you must follow:
- Use ONLY the information given in the requirements.
- "strategy" is a short string that describes the navigation strategy the robot must follow.
- "decisions" is a non-empty list of decision rules the robot can apply during navigation. Each decision must be a string in the form "IF <condition> THEN <ACTION>", where <ACTION> is exactly one of FORWARD, LEFT, RIGHT, STOP in uppercase.
- The goal can be ahead, to the left, or to the right of the robot. The first decision must move the robot toward the goal whenever the goal direction is safe.
- The decisions together must cover all of the following, in this order: moving toward the goal whenever that direction is safe, never moving into a blocked direction, and stopping when no safe direction is available.
- If the goal direction is blocked, the robot must try another safe direction before stopping: it must stop only when no safe direction is available.
- "stop_condition" is a short string that describes the exact point at which the robot must stop.
- Return ONLY one valid JSON object with exactly the three keys shown below. No extra keys, no missing keys, no markdown code fences, no explanations, and no text before or after the JSON.

Output structure:
{
    "strategy": "string",
    "decisions": ["string", "string"],
    "stop_condition": "string"
}"""


def build_prompt(requirement):
    system_prompt = SYSTEM_PROMPT
    user_prompt = f"""Validated requirements:
{json.dumps(requirement, indent=2)}

Create the navigation plan for these requirements."""
    return system_prompt, user_prompt


def validate_plan(data):
    if not isinstance(data, dict):
        return False

    if set(data.keys()) != REQUIRED_KEYS:
        return False

    if not isinstance(data["strategy"], str):
        return False

    if not data["strategy"].strip():
        return False

    if not isinstance(data["decisions"], list):
        return False

    if len(data["decisions"]) == 0:
        return False

    for decision in data["decisions"]:
        if not isinstance(decision, str):
            return False
        if not decision.strip():
            return False
        if not any(action in decision for action in VALID_ACTIONS):
            return False

    if not isinstance(data["stop_condition"], str):
        return False

    if not data["stop_condition"].strip():
        return False

    return True


def run_planner(requirement):
    system_prompt, user_prompt = build_prompt(requirement)

    response_text = ask_qwen(system_prompt, user_prompt)

    plan = parse_json_response(response_text)

    if plan is None:
        print("The Planner Agent did not return valid JSON.")
        return None

    if not validate_plan(plan):
        print("The Planner Agent returned JSON that does not satisfy the software requirements.")
        return None

    return plan
