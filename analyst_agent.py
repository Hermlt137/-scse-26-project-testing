import json

from ollama import chat

MODEL = "qwen3:8b"

REQUIRED_KEYS = {"goal", "allowed_actions", "safe_stop", "avoid_obstacles"}
VALID_ACTIONS = ["FORWARD", "LEFT", "RIGHT", "STOP"]

SYSTEM_PROMPT = """You are the Analyst Agent, a software requirements engineer for a mobile robot navigation system.

Your only job is to read the customer brief and convert it into explicit, structured software requirements. You do not write navigation code and you do not answer questions.

Rules you must follow:
- Use ONLY the information given in the brief text.
- "goal" is a short string describing the navigation objective understood from the brief.
- "allowed_actions" is the list of valid steps the robot can take. It must contain exactly these actions: FORWARD, LEFT, RIGHT, STOP. Never invent new actions.
- "safe_stop" is true if the robot must stop safely when it cannot move anywhere, otherwise false.
- "avoid_obstacles" is true if the robot must avoid anything that blocks its path, otherwise false.
- Return ONLY one valid JSON object with exactly the four keys shown below. No extra keys, no missing keys, no markdown code fences, no explanations, and no text before or after the JSON.

Output structure:
{
    "goal": "string",
    "allowed_actions": ["FORWARD", "LEFT", "RIGHT", "STOP"],
    "safe_stop": true,
    "avoid_obstacles": true
}"""


def build_prompt(brief_text):
    system_prompt = SYSTEM_PROMPT
    user_prompt = f"""Customer brief:
{brief_text}

Convert this brief into the software requirements JSON."""
    return system_prompt, user_prompt


def ask_qwen(system_prompt, user_prompt):
    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        think=False,
    )
    return response.message.content


def clean_response(response_text):
    text = response_text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        lines = lines[1:]
        if lines and lines[-1].strip().startswith("```"):
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    return text


def parse_response(response_text):
    try:
        return json.loads(clean_response(response_text))
    except json.JSONDecodeError:
        return None


def validate_requirements(requirements):
    if not isinstance(requirements, dict):
        return False

    if set(requirements.keys()) != REQUIRED_KEYS:
        return False

    if not isinstance(requirements["goal"], str):
        return False

    if not isinstance(requirements["allowed_actions"], list):
        return False

    if len(requirements["allowed_actions"]) == 0:
        return False

    for action in requirements["allowed_actions"]:
        if not isinstance(action, str):
            return False
        if action not in VALID_ACTIONS:
            return False

    if not isinstance(requirements["safe_stop"], bool):
        return False

    if not isinstance(requirements["avoid_obstacles"], bool):
        return False

    return True


def run_analyst(brief_text):
    system_prompt, user_prompt = build_prompt(brief_text)

    response_text = ask_qwen(system_prompt, user_prompt)

    requirements = parse_response(response_text)

    if requirements is None:
        print("The Analyst Agent did not return valid JSON.")
        return None

    if not validate_requirements(requirements):
        print("The Analyst Agent returned JSON that does not satisfy the software requirements.")
        return None

    return requirements
